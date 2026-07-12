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
