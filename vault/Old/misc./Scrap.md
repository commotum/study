# Circuit Equality Notions and Controlled-Circuit Notes

Strictly speaking, we required distinct equivalence relations; each relation then determines equivalence classes.

## Circuit Equality Notions

### 1. Exact Equality — `ExactCircuitEq`

$$
\operatorname{eval}(C)=\operatorname{eval}(D)
$$

The circuits implement exactly the same unitary matrix. No phase difference is ignored.

### 2. Equality up to One Global Phase — `GlobalPhaseEq`

$$
V=\zeta U,\qquad |\zeta|=1
$$

The same scalar multiplies every input and output amplitude.

### 3. Equality up to Input-Basis-Dependent Phase — `BasisPhaseEq`

$$
V_{r,x}=\phi(x)U_{r,x},\qquad |\phi(x)|=1
$$

Each computational-basis input column $x$ may have a different phase. This preserves behavior on individual basis inputs, but generally changes interference between superposed inputs.

### 4. Same Classical Reversible Behavior — `SameBasisBehavior`

For every computational-basis input $x$ and output $y$,

$$
U|x\rangle \sim |y\rangle
\quad\Longleftrightarrow\quad
V|x\rangle \sim |y\rangle
$$

where $\sim$ permits a phase. This records only the induced classical basis permutation and deliberately forgets general quantum action.

### 5. Same Computational-Basis Measurement Probabilities — `BasisMeasurementEq`

$$
|U_{y,x}|^2=|V_{y,x}|^2
$$

for every computational-basis preparation $x$ and basis measurement outcome $y$. It cannot detect phases that would become observable after further interference.

### 6. Same Channel or All-Measurement Behavior — `ChannelEq` / `AllMeasurementEq`

Channel equality means

$$
U\rho U^\dagger=V\rho V^\dagger
$$

for every input matrix $\rho$.

The equivalent all-effect formulation requires

$$
\operatorname{tr}(EU\rho U^\dagger)
=
\operatorname{tr}(EV\rho V^\dagger)
$$

for every input matrix $\rho$ and effect matrix $E$. The library proves `ChannelEq ↔ AllMeasurementEq`.

The proved implication structure is:

```text
Exact equality
      │
      ▼
GlobalPhaseEq ───────────────▶ ChannelEq ⇔ AllMeasurementEq
      │                                      │
      ▼                                      ▼
BasisPhaseEq ───────────────────────▶ BasisMeasurementEq
      │
      ▼
SameBasisBehavior
```

Two important cautions:

- `BasisPhaseEq` generally does not imply channel equality because different input columns can acquire different relative phases.
- Approximation via $\operatorname{operatorDistance}(U,V)\le\varepsilon$ is not another equivalence relation; it is a metric error bound.

The definitive definitions are collected in `docs/conventions.md:547`.

## Controlled-Circuit Notes

- The target-block abstraction made Section 5 unusually clean: controlled-circuit equality reduces to exact inactive and active one-qubit products while still proving equality on arbitrary-width registers.
- A controlled scalar “global” phase is not globally ignorable; it becomes an exact diagonal gate on the control wire.
- Two small source claims were unexpectedly false at boundaries:
  - Zero-qubit unitaries are arbitrary $U(1)$ phases, not unique.
  - “$R_x(\theta)$ is not of this form” has scalar endpoint exceptions such as $R_x(0)=I$.

### 1. Why the Target-Block Abstraction Worked So Well

Choose a target wire $t$. Every computational-basis assignment can be split into

$$
(\text{target bit},\ \text{all remaining bits})
$$

For each fixed assignment $r$ of the remaining $n-1$ wires, a gate that only changes $t$ acts through a $2\times2$ matrix $F(r)$. Therefore, the full $2^n\times2^n$ matrix is block diagonal:

$$
\operatorname{targetBlock}(F)
= \bigoplus_{r\in\{0,1\}^{n-1}} F(r)
$$

This is implemented by `Barenco/ControlledCircuit/Block.lean:22`. It has three particularly useful properties:

- A local one-qubit gate $A$ has $F(r)=A$ for every $r$.
- A controlled-$U$ has

  $$
  F(r)=
  \begin{cases}
  U, & \text{if the control bit in }r\text{ is }1, \\
  I, & \text{otherwise}.
  \end{cases}
  $$

- Multiplication of enormous full-register matrices becomes pointwise $2\times2$ multiplication:

  $$
  \operatorname{targetBlock}(F)\operatorname{targetBlock}(G)
  =
  \operatorname{targetBlock}\bigl(r\mapsto F(r)G(r)\bigr)
  $$

That last identity is `Barenco/ControlledCircuit/Block.lean:37`.

For example, the chronological Section 5 circuit

$$
A;\ \mathrm{CNOT};\ B;\ \mathrm{CNOT};\ C
$$

has, under column-vector semantics, the block

$$
CX^cBX^cA
$$

where $c$ is the control bit. Hence there are only two cases:

$$
\begin{aligned}
c=0 &: CBA, \\
c=1 &: CXBXA.
\end{aligned}
$$

So the circuit implements controlled-$W$ exactly if and only if

$$
CBA=I
\quad\text{and}\quad
CXBXA=W
$$

That is precisely the full-register characterization in `Barenco/ControlledCircuit/Decomposition.lean:72`.

The important point is that this is not merely a $4\times4$ calculation that we hope generalizes. Every spectator wire is explicitly included in $r$, and block injectivity recovers equality of the complete arbitrary-width matrices. It simultaneously proves that all other wires are preserved.

Its limitation is also informative: it works so cleanly in Section 5 because every CNOT targets the same selected target wire. In Section 6, some CNOTs alter one control wire using another control wire. Relative to the final target, those gates move between complementary assignments rather than remaining within one block. That is one reason the three-qubit stage requires new infrastructure.

### 2. Why a Controlled “Global Phase” Becomes Observable

For an isolated target system,

$$
S=e^{i\delta}I
$$

is a global phase. Acting on any state gives $S|\psi\rangle=e^{i\delta}|\psi\rangle$, which represents the same physical ray.

But controlling it produces

$$
\begin{aligned}
C(S)
&=|0\rangle\!\langle 0|_c\otimes I
+|1\rangle\!\langle 1|_c\otimes e^{i\delta}I.
\end{aligned}
$$

Factoring out the target identity gives

$$
C(S)
=
\begin{pmatrix}
1 & 0 \\
0 & e^{i\delta}
\end{pmatrix}_c
\otimes I_{\text{everything else}}.
$$

Thus, it is exactly a phase gate on the control wire. This full-register identity is proved in `Barenco/ControlledCircuit/Phase.lean:115`.

The phase is now relative between two control branches. For example,

$$
|+\rangle_c|\psi\rangle
=
\frac{|0\rangle+|1\rangle}{\sqrt{2}}|\psi\rangle
$$

becomes

$$
\frac{|0\rangle+e^{i\delta}|1\rangle}{\sqrt{2}}|\psi\rangle.
$$

At $\delta=\pi$, the control changes from $|+\rangle$ to $|-\rangle$, which is perfectly distinguishable by an $X$-basis measurement.

So although

$$
e^{i\delta}W \sim W
$$

up to global phase as isolated one-qubit gates, generally

$$
C(e^{i\delta}W)\not\sim C(W)
$$

even up to global phase. Their inactive branches agree while their active branches differ by $e^{i\delta}$. This is essentially phase kickback.

It is also the key to the six-gate arbitrary controlled-$U(2)$ construction: split

$$
U=e^{i\delta}W,\qquad W\in SU(2),
$$

implement controlled-$W$ with the five-gate decomposition, and implement the controlled scalar using one phase gate on the control.

### 3. Zero Qubits Do Not Mean a Zero-Dimensional State Space

A correction to my earlier phrasing: this was a boundary-condition trap in the formal model, not an explicit false sentence I found in the paper.

The library defines an $n$-qubit basis as functions

$$
\mathrm{Fin}(n)\to\mathrm{Bool}.
$$

Its cardinality is $2^n$, as recorded in `Barenco/Basic.lean:34`. At $n=0$,

$$
2^0=1.
$$

There is one basis assignment: the empty bit string. Therefore, the zero-qubit Hilbert space is not the zero vector space; it is the empty tensor product,

$$
\mathcal H_0\cong\mathbb C.
$$

A zero-qubit matrix is consequently a $1\times1$ matrix $[z]$, and it is unitary whenever

$$
|z|=1.
$$

Thus, the exact zero-qubit unitary group is $U(1)$, not a singleton.

What is unique is the computational-basis label, and the empty circuit evaluates to the identity. But the ambient semantic type also contains all scalar phases. If we quotient by global phase, they become physically equivalent; under exact matrix equality, they remain distinct. That distinction matters for roots, exact decomposition statements, and boundary theorems.

### 4. The $R_x(\theta)$ Endpoint Exceptions

The paper says unconditionally that $R_x(\theta)$ is not in the Lemma 5.4 family. Generically, that is right, but the endpoints defeat the blanket statement.

The Lemma 5.4 family has off-diagonal entries that are real and opposite:

$$
\begin{pmatrix}
e^{i\alpha}\cos(\phi/2) & \sin(\phi/2) \\
-\sin(\phi/2) & e^{-i\alpha}\cos(\phi/2)
\end{pmatrix}.
$$

Meanwhile,

$$
R_x(\theta)=
\begin{pmatrix}
\cos(\theta/2) & i\sin(\theta/2) \\
i\sin(\theta/2) & \cos(\theta/2)
\end{pmatrix}
$$

has equal, purely imaginary off-diagonal entries. When $\sin(\theta/2)\ne0$, those patterns cannot agree.

But if

$$
\sin(\theta/2)=0,
$$

then $\theta=2\pi k$ and

$$
R_x(2\pi k)=(-1)^kI.
$$

Both possibilities belong to the Lemma 5.4 family:

$$
I=\operatorname{symmetricEuler}(0,0),
\qquad
-I=\operatorname{symmetricEuler}(\pi,0).
$$

The especially quantum-looking detail is

$$
R_x(2\pi)=-I,
\qquad
R_x(4\pi)=I.
$$

So the rotation is $2\pi$-periodic only up to global phase, but $4\pi$-periodic under exact matrix equality.

This correction affects only the paper’s illustrative sentence; none of its main decompositions or resource bounds depend on it. It is recorded as `docs/corrections.md:351`.

----

- For one qubit, $n=1$ and $d=2$.

Choose the pure preparation

$$
|\psi\rangle = |+\rangle
=\frac{1}{\sqrt 2}
\begin{pmatrix}
1\\
1
\end{pmatrix}.
$$

Its preparation matrix, or density matrix, is

$$
\rho=|\psi\rangle\langle\psi|
=\frac12
\begin{pmatrix}
1&1\\
1&1
\end{pmatrix}.
$$

Now consider the yes/no question:

> “Is the qubit in the computational-basis state $|0\rangle$?”

The corresponding measurement-event matrix is

$$
E=|0\rangle\langle0|
=
\begin{pmatrix}
1&0\\
0&0
\end{pmatrix}.
$$

The probability of obtaining “yes” is

$$
\begin{aligned}
p
&=\operatorname{Tr}(\rho E)\\
&=\operatorname{Tr}\left[
\frac12
\begin{pmatrix}
1&1\\
1&1
\end{pmatrix}
\begin{pmatrix}
1&0\\
0&0
\end{pmatrix}
\right]\\
&=\operatorname{Tr}\left[
\frac12
\begin{pmatrix}
1&0\\
1&0
\end{pmatrix}
\right]\\
&=\frac12.
\end{aligned}
$$

Thus:

$$
\boxed{
\rho=\frac12
\begin{pmatrix}
1&1\\
1&1
\end{pmatrix}
}
\qquad\text{and}\qquad
\boxed{
E=
\begin{pmatrix}
1&0\\
0&0
\end{pmatrix}
}
$$

are examples of a preparation matrix and a measurement matrix, respectively. They represent different physical objects, and their pairing through $\operatorname{Tr}(\rho E)$ produces the probability $p=\tfrac12$.

The complementary “no” event is represented by

$$
I_2-E=
\begin{pmatrix}
0&0\\
0&1
\end{pmatrix},
$$

which also has probability $1/2$.

---

- Think of a measurement-event matrix $E$ as a mathematical question posed to the prepared state:

> “How much of this state matches the outcome I am looking for?”

The rule

$$
p=\operatorname{Tr}(\rho E)
$$

turns that question and the preparation $\rho$ into a probability.

## 1. A Measurement in the Computational Basis

Write a general one-qubit preparation as

$$
\rho=
\begin{pmatrix}
a & c\\
c^* & 1-a
\end{pmatrix}.
$$

Here:

- $a$ is the probability associated with $|0\rangle$.
- $1-a$ is the probability associated with $|1\rangle$.
- $c$ describes quantum coherence between $|0\rangle$ and $|1\rangle$.

Suppose we want to know:

> “Will the measurement result be $0$?”

The corresponding event matrix is

$$
E_0=|0\rangle\langle0|
=
\begin{pmatrix}
1&0\\
0&0
\end{pmatrix}.
$$

Now multiply:

$$
\rho E_0
=
\begin{pmatrix}
a&c\\
c^*&1-a
\end{pmatrix}
\begin{pmatrix}
1&0\\
0&0
\end{pmatrix}
=
\begin{pmatrix}
a&0\\
c^*&0
\end{pmatrix}.
$$

Taking the trace means adding the diagonal entries:

$$
p(0)=\operatorname{Tr}(\rho E_0)=a.
$$

So $E_0$ acts like a selector: it selects the part of $\rho$ associated with $|0\rangle$.

Similarly,

$$
E_1=|1\rangle\langle1|
=
\begin{pmatrix}
0&0\\
0&1
\end{pmatrix}
$$

gives

$$
p(1)=\operatorname{Tr}(\rho E_1)=1-a.
$$

Because

$$
E_0+E_1=I_2,
$$

the probabilities add to one:

$$
p(0)+p(1)
=\operatorname{Tr}\bigl(\rho(E_0+E_1)\bigr)
=\operatorname{Tr}(\rho)
=1.
$$

## 2. Why the Entries of $E$ Select Information

For arbitrary $d\times d$ matrices,

$$
\operatorname{Tr}(\rho E)
=
\sum_{i,j}\rho_{ij}E_{ji}.
$$

Thus, every entry of $E$ specifies how an entry of $\rho$ contributes to the final probability.

For the event $E_0$, the only nonzero entry is

$$
(E_0)_{00}=1,
$$

so

$$
\operatorname{Tr}(\rho E_0)=\rho_{00}.
$$

That is why this measurement matrix reads out the probability of $|0\rangle$.

## 3. Measuring in a Different Basis

A measurement matrix does not have to select a computational-basis state.

Suppose we ask:

> “Is the qubit in the state $|+\rangle$?”

where

$$
|+\rangle=\frac{|0\rangle+|1\rangle}{\sqrt2}.
$$

The corresponding event matrix is

$$
E_+
=|+\rangle\langle+|
=\frac12
\begin{pmatrix}
1&1\\
1&1
\end{pmatrix}.
$$

Then

$$
\begin{aligned}
p(+)
&=\operatorname{Tr}(\rho E_+)\\
&=
\frac12
\operatorname{Tr}
\left[
\begin{pmatrix}
a&c\\
c^*&1-a
\end{pmatrix}
\begin{pmatrix}
1&1\\
1&1
\end{pmatrix}
\right]\\
&=\frac12\left(1+c+c^*\right)\\
&=\frac12+\operatorname{Re}(c).
\end{aligned}
$$

This measurement accesses the off-diagonal entries of $\rho$. Those entries contain information about quantum coherence that a computational-basis measurement cannot see.

For example, compare

$$
\rho_+
=
\frac12
\begin{pmatrix}
1&1\\
1&1
\end{pmatrix}
$$

with the incoherent mixture

$$
\rho_{\text{mix}}
=
\frac12
\begin{pmatrix}
1&0\\
0&1
\end{pmatrix}.
$$

Both give equal probabilities for $0$ and $1$:

$$
\operatorname{Tr}(\rho_+E_0)
=
\operatorname{Tr}(\rho_{\text{mix}}E_0)
=\frac12.
$$

But the $E_+$ measurement distinguishes them:

$$
\operatorname{Tr}(\rho_+E_+)=1,
\qquad
\operatorname{Tr}(\rho_{\text{mix}}E_+)=\frac12.
$$

So different measurement matrices reveal different information contained in the same preparation matrix.

## 4. The Geometric Meaning

When

$$
E_\phi=|\phi\rangle\langle\phi|,
$$

the event matrix is the projector onto the direction $|\phi\rangle$.

For a pure preparation $\rho=|\psi\rangle\langle\psi|$,

$$
\begin{aligned}
p
&=\operatorname{Tr}(\rho E_\phi)\\
&=\operatorname{Tr}
\left(
|\psi\rangle\langle\psi|
|\phi\rangle\langle\phi|
\right)\\
&=|\langle\phi|\psi\rangle|^2.
\end{aligned}
$$

Thus, matrix multiplication computes the overlap between the prepared state and the measurement direction, while squaring its magnitude turns that overlap into a probability.

## 5. General Measurement-Event Matrices

A general event matrix need not be a sharp projector. It only has to satisfy

$$
0\leq E\leq I.
$$

Its eigenvalue decomposition is

$$
E=\sum_k e_k|e_k\rangle\langle e_k|,
\qquad 0\leq e_k\leq1.
$$

Therefore,

$$
\operatorname{Tr}(\rho E)
=
\sum_k e_k\langle e_k|\rho|e_k\rangle.
$$

This gives a useful interpretation:

- $\langle e_k|\rho|e_k\rangle$ says how much of the preparation lies in direction $|e_k\rangle$.
- $e_k$ says how strongly that direction counts toward the “yes” outcome.
- Their weighted sum is the probability of “yes.”

For a projector, every $e_k$ is either $0$ or $1$, so the relevant components are rejected or accepted completely. General effects allow partial or noisy acceptance.

One important distinction: $E$ determines the probability of an outcome, but it does not by itself specify the state after measurement. Describing the post-measurement state requires additional measurement operators, often called Kraus operators.

---

## Stochastic-kernel reduction

A stochastic local hidden-variable model does not assign definite outcomes immediately. Instead, for each hidden state $\lambda$ and local setting, it assigns probability distributions—or kernels—over outcomes:

$$
K_A(x \mid a,\lambda),\qquad K_B(y \mid b,\lambda),\qquad x,y \in \{-1,+1\}.
$$

Locality must include conditional factorization:

$$
P(x,y \mid a,b,\lambda)=K_A(x \mid a,\lambda)K_B(y \mid b,\lambda).
$$

Merely specifying local marginals is not enough; Alice’s and Bob’s outcomes could still be conditionally correlated. Define their conditional biases:

$$
\bar A(a,\lambda)=\mathbb E[x \mid a,\lambda],\qquad \bar B(b,\lambda)=\mathbb E[y \mid b,\lambda].
$$

These lie in $[-1,1]$. Factorization then gives

$$
\mathbb E[xy \mid a,b,\lambda]=\bar A(a,\lambda)\bar B(b,\lambda),
$$

so the observable correlation becomes

$$
P(a,b)=\int \bar A(a,\lambda)\bar B(b,\lambda)\,d\mu(\lambda).
$$

Thus, for correlation inequalities, a stochastic local model reduces to the library’s bounded effective-response model. Its Bell and CHSH inequalities already apply to those biases.

A stronger reduction would make the model literally deterministic by adjoining independent random seeds $u_A,u_B \in [0,1]$ and thresholding them according to each kernel. That construction is deferred because it needs measurable kernels, product probability spaces, seed independence, and Fubini. The distinction is recorded in goal-1/0-plan.md:454.

## Modern CHSH

“Modern” here means post-1964: the Clauser–Horne–Shimony–Holt form introduced later and now commonly used.

Choose two settings per party, $a_0,a_1$ and $b_0,b_1$, and form

$$
S=P(a_0,b_0)+P(a_0,b_1)+P(a_1,b_0)-P(a_1,b_1).
$$

Every normalized local model with responses bounded by one satisfies

$$
|S| \le 2.
$$

Pointwise, this follows by rewriting the expression as

$$
A_0(B_0+B_1)+A_1(B_0-B_1).
$$

Unlike Bell’s original 1964 inequality, CHSH:

- does not require perfect anticorrelation;
- works directly with bounded responses, including stochastic conditional biases;
- uses four correlations from two settings on each side.

For the singlet correlation $P(a,b)=-a \cdot b$, the library’s four unit directions give

$$
S=-2\sqrt{2},\qquad |S|=2\sqrt{2}>2.
$$

It also proves that if all four singlet correlations are approximated within a common error $\eta$, then

$$
\eta \ge \frac{\sqrt{2}-1}{2}.
$$

The abstract inequality is in `formal/Bell/Inequality/CHSH.lean`, and the calculated quantum violation is in `formal/Bell/Geometry/CHSHViolation.lean`.

## Deterministic seed reduction

This means we can move all remaining randomness into an enlarged hidden variable.

Suppose that, given $\lambda$ and setting $a$, Alice’s stochastic rule says

$$
P(A=+1 \mid a,\lambda)=p_A(a,\lambda).
$$

Introduce a fresh uniform random number $u_A \in [0,1]$, and define

$$
A(a,\lambda,u_A)=
\begin{cases}
+1, & u_A \le p_A(a,\lambda),\\
-1, & u_A > p_A(a,\lambda).
\end{cases}
$$

For example, if $p_A=0.7$, then 70% of uniform seeds produce $+1$. But once $u_A$ is fixed, Alice’s answer is completely determined.

Do the same for Bob with an independent seed $u_B$:

$$
B(b,\lambda,u_B)=
\begin{cases}
+1, & u_B \le p_B(b,\lambda),\\
-1, & u_B > p_B(b,\lambda).
\end{cases}
$$

Now enlarge the hidden state to

$$
\widetilde\lambda=(\lambda,u_A,u_B)
$$

with distribution

$$
\mu \otimes \mathrm{Uniform}[0,1] \otimes \mathrm{Uniform}[0,1].
$$

For each fixed $\widetilde\lambda$, both outcomes are literal deterministic $\pm 1$ functions. Averaging over the seeds reproduces the original stochastic probabilities.

The independence of $u_A$ and $u_B$ ensures

$$
P(A=x,B=y \mid a,b,\lambda)=P(A=x \mid a,\lambda)P(B=y \mid b,\lambda).
$$

So this works when the original stochastic model already has conditional factorization. It does not magically convert an arbitrary correlated conditional law into a local one.

It is stronger than replacing each kernel by its mean because:

- The mean trick produces values in $[-1,1]$ and preserves the correlations needed by Bell/CHSH.
- The seed construction produces actual deterministic $\pm 1$ outcomes and reproduces the full factorized outcome distribution.

This is a mathematical representation theorem—not a claim that physical randomness is secretly predetermined. Formalizing it cleanly requires measurable probability kernels, product measures, threshold measurability, and integration/Fubini arguments.

---

$$
\begin{aligned}
|0\rangle=\binom{1}{0} &\Longleftrightarrow 1, \\
|1\rangle=\binom{0}{1} &\Longleftrightarrow j, \\
\frac{1}{\sqrt{2}}\binom{1}{1} &\Longleftrightarrow e^{j\pi/4}, \\
\frac{1}{\sqrt{2}}\binom{1}{-1} &\Longleftrightarrow e^{-j\pi/4}, \\
\frac{1}{\sqrt{2}}\binom{1}{i} &\Longleftrightarrow e^{k\pi/4}, \\
\frac{1}{\sqrt{2}}\binom{1}{-i} &\Longleftrightarrow e^{-k\pi/4}.
\end{aligned}
$$

## Deutsch Map

Each local carrier has three descriptors,

$$
Q_i=(Q_i^X,Q_i^Y,Q_i^Z)
$$

and CNOT updates only its two endpoints:

$$
\begin{aligned}
Q_c^X &\mapsto Q_c^XQ_t^X, \\[1em]
Q_c^Y &\mapsto Q_c^YQ_t^X, \\[1em]
Q_c^Z &\mapsto Q_c^Z, \\[1em]
Q_t^X &\mapsto Q_t^X, \\[1em]
Q_t^Y &\mapsto Q_c^ZQ_t^Y, \\[1em]
Q_t^Z &\mapsto Q_c^ZQ_t^Z.
\end{aligned}
$$
