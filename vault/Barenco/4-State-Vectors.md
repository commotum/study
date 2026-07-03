## State Vectors

A unitary matrix can be applied to a fixed input vector to produce a single state vector.

Use the identity basis vector

$$
e_0=
\begin{pmatrix}
1\\
0
\end{pmatrix}.
$$

If $U\in U(2)$, then

$$
\psi = Ue_0
$$

is a normalized complex state vector:

$$
\|\psi\|=1.
$$

In other words, the unitary matrix sends the identity basis vector to a state vector:

$$
e_0\mapsto \psi.
$$

Since $U$ is unitary, the output remains on the unit sphere in $\mathbb C^2$:

$$
\psi\in S^3\subset \mathbb C^2.
$$

However, this state vector does not contain the full information of the unitary matrix. A general unitary matrix has four real degrees of freedom:

$$
\dim U(2)=4.
$$

But a normalized complex vector in $\mathbb C^2$ has only three real degrees of freedom:

$$
\dim S^3=3.
$$

Thus the map

$$
U\mapsto Ue_0
$$

collapses one degree of freedom. It remembers the output state, but not the full unitary action.

## State Quaternions

Under the quaternion dictionary, the same thing happens.

The full two-sided Hamilton action is

$$
q\mapsto uq\delta_\theta,
$$

where $u\in S^3$ and $\delta_\theta\in S^1_k$. As an uncollapsed pair,

$$
(u,\delta_\theta)\in S^3\times S^1_k
$$

has four real degrees of freedom, matching $U(2)$.

Now apply the action only to the identity quaternion

$$
1=(1,0,0,0).
$$

Then

$$
1\mapsto u1\delta_\theta=u\delta_\theta.
$$

So the output is a single unit quaternion:

$$
p=u\delta_\theta\in S^3.
$$

This is the quaternionic analogue of the state vector. The correspondence is

$$
\psi=Ue_0
\qquad
\Longleftrightarrow
\qquad
p=u\delta_\theta.
$$

The projection $\Psi$ makes this correspondence explicit:

$$
\Psi(u\delta_\theta)
=
e^{i\theta}\Phi(u)
\begin{pmatrix}
1\\
0
\end{pmatrix}.
$$

Therefore, if $p=u\delta_\theta$, then

$$
\Psi(p)=\psi.
$$

So the same distinction appears on both sides. The unitary matrix $U$ is a full unitary operator, while $Ue_0$ is a single state vector. Likewise, the two-sided Hamilton action $q\mapsto uq\delta_\theta$ is a full action, while $1\mapsto u\delta_\theta$ is a single state quaternion.

In both cases, applying the full action to one fixed input collapses the degrees of freedom:

$$
U(2)\longrightarrow S^3,
$$

or equivalently,

$$
S^3\times S^1_k\longrightarrow S^3.
$$

Thus the state vector and the state quaternion both preserve the normalized output state, but they no longer preserve the full operator that produced it.

## Avoiding Collapse

The collapse only happens if we keep only the output state and discard the operator-level data.

If we preserve the matrix itself, then no degrees of freedom are lost:

$$
U\in U(2)
$$

still has four real degrees of freedom. Equivalently, if we preserve the decomposition

$$
U=e^{i\theta}S,
\qquad
S\in SU(2),
$$

then we preserve both pieces:

$$
e^{i\theta}\in U(1),
\qquad
S\in SU(2).
$$

The phase contributes one real degree of freedom, and the special-unitary part contributes three:

$$
\dim U(1)+\dim SU(2)=1+3=4.
$$

So the matrix-side collapse happens only when we apply $U$ to one fixed vector and keep only the result:

$$
U\mapsto Ue_0.
$$

If instead we keep $U$, or keep the uncollapsed pair $(e^{i\theta},S)$, then we preserve the full four degrees of freedom.

The quaternion side works the same way. If we keep only the state quaternion

$$
p=u\delta_\theta,
$$

then we have collapsed down to a single element of $S^3$, which has three real degrees of freedom.

But if we preserve the two-sided action data as the pair

$$
(u,\delta_\theta)\in S^3\times S^1_k,
$$

then we preserve the full four real degrees of freedom:

$$
\dim S^3+\dim S^1_k=3+1=4.
$$

So the uncollapsed pair

$$
(u,\delta_\theta)
$$

is the quaternionic analogue of preserving the matrix-side pair

$$
(e^{i\theta},S).
$$

The collapsed product

$$
u\delta_\theta
$$

is instead the quaternionic analogue of the state vector

$$
Ue_0.
$$

There is a double-cover redundancy in the uncollapsed descriptions:

$$
(e^{i\theta},S)\sim(-e^{i\theta},-S),
$$

and similarly

$$
(u,\delta_\theta)\sim(-u,-\delta_\theta).
$$

Equivalently,

$$
U(2)\cong \frac{U(1)\times SU(2)}{\mathbb Z_2}.
$$

Under the quaternion dictionary, this is

$$
U(2)\cong \frac{S^3\times S^1_k}{\mathbb Z_2}.
$$

The $\mathbb Z_2$ quotient identifies the two representatives in each double cover. Since this redundancy is discrete, it does not remove a continuous degree of freedom. The uncollapsed descriptions still carry four real degrees of freedom.