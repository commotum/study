# Physical Qubits

The phenomenal-qubit description represents only the projected, measurement-relevant state. The physical-qubit description, by contrast, is allowed to carry local internal structure that is not directly exposed by the projection $\pi$, but is still essential for deterministic physical evolution.

As shown earlier, a $2\times2$ unitary action can be represented using a two-sided Hamilton action: a left rotor quaternion acts from the left, while a right phase quaternion acts from the right. The physical-qubit description uses the same two-sided structure to define both quantum gates and qubit state, preserving unobserved structure.

## Rotor-state and phase-state

A **rotor-state** is a unit quaternion:

$$
r\in S^3.
$$

A **phase-state** is a unit quaternion

$$
\phi\in S^3.
$$

A **physical-qubit** is a pair of unit quaternions consisting of a rotor-state and a phase-state:

$$
q=(r,\phi).
$$

Thus the physical-qubit space is

$$
\mathcal Q=S^3\times S^3.
$$

Equivalently,

$$
q\in\mathcal Q
$$

means

$$
q=(r,\phi),
\qquad
r,\phi\in S^3.
$$

The rotor-state $r$ represents the directly oriented part of the local physical state. The phase-state $\phi$ carries additional local phase-frame information needed for deterministic physical evolution. Not all of this information is necessarily exposed by a single projection $\pi$ or readout, but the pair

$$
(r,\phi)
$$

is the full local physical carrier used by the update rules.

## Uncollapsed physical state

The physical-qubit is intentionally represented as an uncollapsed pair:

$$
q=(r,\phi).
$$

This is different from keeping only the product

$$
\bar q=r\phi.
$$

The product $\bar q$ is a single unit quaternion, since the Hamilton product of unit quaternions is again a unit quaternion:

$$
\bar q\in S^3.
$$

However, this product does not contain the full information of the physical-qubit state. Many different pairs

$$
(r,\phi)\in S^3\times S^3
$$

can produce the same product

$$
\bar q=r\phi.
$$

Therefore,

$$
(r,\phi)
$$

is the physical state, while

$$
\bar q=r\phi
$$

is only its collapsed quaternion view.

Furthermore, the the collapsed quaternion

$$
\bar q=r\phi
$$

should not be identified with the projection $\pi$, nor with the final measurement result. The collapsed quaternion is still a state-level object. In general, it is equivalent to the normalized complex state-vector representation: it keeps the qubit as a continuous unit state, rather than reducing it to a classical outcome, but with the reduced degree of freedom the collapse induces.

The projection $\pi$ is the map from the physical state to its phenomenal or observable description, and the measurement projection is the further reduction to a classical bit assignment. For a single qubit, measurement assigns probabilities to the two possible outcomes,

$$
(p_0,p_1),
\qquad
p_0+p_1=1,
$$

and an actual measurement returns one bit,

$$
b\in\{0,1\}.
$$

Thus the levels are distinct: the physical state is the uncollapsed pair $(r,\phi)$, the collapsed quaternion $\bar q$ corresponds to the usual state-vector level, and measurement produces the classical bit outcome.

## Physical gates

A **physical gate** is also represented by a pair of unit quaternions

$$
g=(u,\delta),
\qquad
u,\delta\in S^3.
$$

Here $u$ is the left rotor component of the gate, and $\delta$ is the right phase component of the gate.

For exact equivalence with an ordinary complex-linear $2\times2$ unitary matrix under the fixed projection $\Psi$, the right phase component is restricted to the $k$-axis circle

$$
\delta\in S^1_k\subset S^3.
$$

At the physical-qubit level, however, the stored phase-state $\phi$ is allowed to range over all of $S^3$. This allows the local physical carrier to contain internal phase-frame structure that is not necessarily visible in a single phenomenal projection.

## Physical update rule

Let

$$
q=(r,\phi)\in\mathcal Q
$$

be a physical-qubit, and let

$$
g=(u,\delta)
$$

be a physical gate.

The gate updates the two components separately:

$$
g(q)=(ur,\phi\delta).
$$

Thus,

$$
(r,\phi)\mapsto(ur,\phi\delta).
$$

The rotor-state updates by left Hamilton multiplication:

$$
r'=ur.
$$

The phase-state updates by right Hamilton multiplication:

$$
\phi'=\phi\delta.
$$

Since $u$, $\delta$, $r$, and $\phi$ are unit quaternions, both updated components remain unit quaternions:

$$
r'\in S^3,
\qquad
\phi'\in S^3.
$$

Therefore the physical update preserves the physical-qubit space:

$$
g:\mathcal Q\to\mathcal Q.
$$

## Matrix form of the split update

Using the left and right Hamilton multiplication matrices, the two component updates can be written as

$$
r'=L(u)r,
$$

and

$$
\phi'=R(\delta)\phi.
$$

If $r$ and $\phi$ are treated as real four-component column vectors, then the full split update is

$$
\boxed{
\begin{pmatrix}
r'\\
\phi'
\end{pmatrix}
=
\begin{pmatrix}
L(u)&0\\
0&R(\delta)
\end{pmatrix}
\begin{pmatrix}
r\\
\phi
\end{pmatrix}.
}
$$

This is the uncollapsed physical update. It evolves the rotor-state and phase-state separately, preserving the local internal structure of the physical-qubit.