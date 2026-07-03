## Phenomenal Qubits

Following the physical/phenomenal distinction from local realism, a physical-qubit may contain state information that is not directly observable. The projection $\pi$ of a physical-qubit represents only what can be measured, so a complete phenomenal description must account not only for the qubit’s current physical state, but for the full space of possible measurement outcomes and correlations.

Traditionally, the qubit’s state is represented as a normalized complex vector,

$$
|\psi\rangle=\alpha|0\rangle+\beta|1\rangle,
\qquad
\alpha,\beta\in\mathbb C,
\qquad
|\alpha|^2+|\beta|^2=1,
$$

where the coefficients $\alpha$ and $\beta$ describe the phenomenal state, and determine the measurement probabilities and interference behavior of the qubit.

The phenomenal state evolves by unitary transformations. For a single qubit, a valid evolution is represented by a $2\times2$ unitary matrix $U$ satisfying

$$
U^\dagger U=I.
$$

The state update is

$$
|\psi'\rangle=U|\psi\rangle.
$$

Because $U$ is unitary, it preserves normalization:

$$
\langle\psi'|\psi'\rangle
=
\langle\psi|U^\dagger U|\psi\rangle
=
\langle\psi|\psi\rangle
=
1.
$$

Thus unitary evolution preserves the total probability of all measurement outcomes.

To represent the state of a multi-qubit system, one simply takes the tensor products of these single-qubit state spaces. For two qubits, the state has the form  
  
$$  
|\psi\rangle  
=  
\alpha_{00}|00\rangle  
+\alpha_{01}|01\rangle  
+\alpha_{10}|10\rangle  
+\alpha_{11}|11\rangle,  
$$
  
with normalization  
  
$$  
|\alpha_{00}|^2  
+  
|\alpha_{01}|^2  
+  
|\alpha_{10}|^2  
+  
|\alpha_{11}|^2  
=  
1.  
$$

As the number of qubits in a system grows, the cost of representation (the number of complex coefficients) grows exponentially.

For three qubits, the state has $2^3$ complex coefficients:

$$
\begin{aligned}
|\psi\rangle
={}&
\alpha_{000}|000\rangle+
\alpha_{001}|001\rangle+
\alpha_{010}|010\rangle+
\alpha_{011}|011\rangle \\
+ \ &\alpha_{100}|100\rangle+
\alpha_{101}|101\rangle+
\alpha_{110}|110\rangle+
\alpha_{111}|111\rangle .
\end{aligned}
$$

For $n$ qubits, the state has $2^n$ complex coefficients:

$$  
\begin{aligned}  
|\psi\rangle  
={}&  
\alpha_{00\cdots000}|00\cdots000\rangle+  
\alpha_{00\cdots001}|00\cdots001\rangle \\  
+ \ &  
\alpha_{00\cdots010}|00\cdots010\rangle+  
\alpha_{00\cdots011}|00\cdots011\rangle \\  
+ \ &  
\cdots \\  
+ \ &  
\alpha_{11\cdots100}|11\cdots100\rangle+  
\alpha_{11\cdots101}|11\cdots101\rangle \\  
+ \ &  
\alpha_{11\cdots110}|11\cdots110\rangle+  
\alpha_{11\cdots111}|11\cdots111\rangle .  
\end{aligned}  
$$

Represented compactly, an $n$-qubit phenomenal state is defined as:

$$
|\psi\rangle
=
\sum_{x\in\{0,1\}^n}\alpha_x|x\rangle,
$$
where

$$
\sum_{x\in\{0,1\}^n}|\alpha_x|^2=1.
$$

A phenomenal $n$-qubit state evolves by a dense unitary matrix acting on the full $2^n$-dimensional state space. A valid $n$-qubit evolution is represented by a $2^n\times2^n$ unitary matrix $U$ satisfying

$$
U^\dagger U=I.
$$

The state update is

$$
|\psi'\rangle=U|\psi\rangle.
$$

Written against the computational basis, this has the form

$$
\begin{pmatrix}
\alpha'_0\\
\alpha'_1\\
\alpha'_2\\
\vdots\\
\alpha'_{2^n-3}\\
\alpha'_{2^n-2}\\
\alpha'_{2^n-1}
\end{pmatrix}
=
\begin{pmatrix}
U_{0,0} & U_{0,1} & \cdots & U_{0,2^n-1}\\
U_{1,0} & U_{1,1} & \cdots & U_{1,2^n-1}\\
U_{2,0} & U_{2,1} & \cdots & U_{2,2^n-1}\\
\vdots  & \vdots  & \ddots & \vdots\\
U_{2^n-1,0} & U_{2^n-1,1} & \cdots & U_{2^n-1,2^n-1}
\end{pmatrix}
\begin{pmatrix}
\alpha_0\\
\alpha_1\\
\alpha_2\\
\vdots\\
\alpha_{2^n-3}\\
\alpha_{2^n-2}\\
\alpha_{2^n-1}
\end{pmatrix}.
$$

Because $U$ is unitary, it preserves normalization:

$$
\langle\psi'|\psi'\rangle
=
\langle\psi|U^\dagger U|\psi\rangle
=
\langle\psi|\psi\rangle
=
1.
$$

Working at the phenomenal level requires the projected state to encode every measurement-relevant possibility at once, so its state vector grows as $2^n$ and its dense unitary evolution grows as $2^n\times2^n$. This projected description is often treated as fundamental: there is no deeper local physical carrier with a definite absolute state whose evolution causally explains the observed correlations. In that view, the unobservable physical world is not given an independent mechanical description, and phenomena such as entanglement are accepted as irreducible features of the projected formalism. 

But if a causal physical description can be found, the exponential representation is no longer required. Instead, a realistic initialization, a deterministic physical evolution law, and a projection $\pi$ are sufficient: the physical state evolves causally, and $\pi$ maps that evolution into the observable measurement statistics.