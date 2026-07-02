## Unit quaternions

The norm of a quaternion

$$
q=(q_w,q_x,q_y,q_z)
$$

is

$$
|q|=\sqrt{q_w^2+q_x^2+q_y^2+q_z^2}.
$$

The conjugate of $q$ is

$$
q^*=(q_w,-q_x,-q_y,-q_z),
$$

and satisfies

$$
qq^*=q^*q=|q|^2.
$$

A **unit quaternion** is a quaternion with norm one:

$$
|q|=1.
$$

The set of all unit quaternions is the unit 3-sphere, denoted $S^3$:

$$
S^3
=
\left\{
q=(q_w,q_x,q_y,q_z)\in\mathbb R^4
\;:\;
q_w^2+q_x^2+q_y^2+q_z^2=1
\right\}.
$$

So writing

$$
q\in S^3
$$

means that $q$ is a unit quaternion.

Quaternion norms multiply under the Hamilton product:

$$
|pq|=|p||q|.
$$

Therefore, if $p\in S^3$, then left multiplication by $p$ preserves norm:

$$
|pq|=|q|.
$$

Likewise, right multiplication by $p$ preserves norm:

$$
|qp|=|q|.
$$

In matrix form, this means that if $p\in S^3$, then both $L(p)$ and $R(p)$ are orthogonal real $4\times4$ matrices:

$$
L(p)^T L(p)=I,
\qquad
R(p)^T R(p)=I.
$$

## Unitary matrices

A complex matrix $U$ is **unitary** when

$$
U^\dagger U=I,
$$

where $U^\dagger$ is the conjugate transpose of $U$.

For a $2\times2$ matrix, unitarity means that the columns, and equivalently the rows, are orthonormal complex vectors. Thus a unitary matrix preserves the complex norm:

$$
\|Uv\|=\|v\|.
$$

The group of all $2\times2$ unitary matrices is denoted $U(2)$.

The subgroup of unitary matrices with determinant one is denoted $SU(2)$:

$$
SU(2)=\{U\in U(2):\det U=1\}.
$$

Every matrix in $U(2)$ can be written as a scalar phase times a matrix in $SU(2)$:

$$
U=e^{i\theta}S,
\qquad
S\in SU(2).
$$

Equivalently,

$$
U(2)=U(1)\cdot SU(2).
$$

So a general $2\times2$ unitary matrix has two parts:

$$
\text{unitary matrix}
=
\text{scalar phase}
\times
\text{special-unitary matrix}.
$$

## Two-sided Hamilton action and matrix equivalence

Define the complex projection

$$
\Psi(w,x,y,z)
=
\begin{pmatrix}
w+iz\\
y+ix
\end{pmatrix}.
$$

For a unit quaternion

$$
u=(w,x,y,z)\in S^3,
$$

define

$$
\Phi(u)=
\begin{pmatrix}
w+iz & -y+ix\\
y+ix & w-iz
\end{pmatrix}.
$$

Then

$$
\Phi(u)\in SU(2).
$$

Left Hamilton multiplication by $u$ corresponds to left matrix multiplication by $\Phi(u)$:

$$
\Psi(uq)=\Phi(u)\Psi(q).
$$

Thus every special unitary $2\times2$ matrix can be represented by left Hamilton multiplication by a unit quaternion.

A general unitary $2\times2$ matrix has one additional scalar phase. Write

$$
U=e^{i\theta}\Phi(u),
\qquad
u\in S^3.
$$

Represent the scalar phase $e^{i\theta}$ by the $k$-axis unit quaternion

$$
\delta_\theta=(\cos\theta,0,0,\sin\theta).
$$

Then

$$
\delta_\theta\in S^3.
$$

Under the same projection,

$$
\Psi(q\delta_\theta)=e^{i\theta}\Psi(q).
$$

Therefore the two-sided Hamilton action satisfies

$$
\Psi(uq\delta_\theta)
=
e^{i\theta}\Phi(u)\Psi(q).
$$

So the unitary matrix dictionary is

$$
\boxed{
U=e^{i\theta}\Phi(u)
\quad\Longleftrightarrow\quad
(u,\delta_\theta)
}
$$

with action

$$
\boxed{
q\mapsto uq\delta_\theta.
}
$$

Here $u$ is the rotor quaternion and $\delta_\theta$ is the phase quaternion.

For exact $2\times2$ complex-unitary equivalence under this projection, the phase quaternion is restricted to the $k$-axis circle

$$
S^1_k
=
\left\{
(\cos\theta,0,0,\sin\theta):\theta\in\mathbb R
\right\}
\subset S^3.
$$

If the right-side quaternion is allowed to be an arbitrary element of $S^3$, then $q\mapsto uq\delta$ is still norm-preserving as a real quaternionic transformation, but it is no longer necessarily the representation of a complex-linear $2\times2$ unitary matrix under the fixed projection $\Psi$.

