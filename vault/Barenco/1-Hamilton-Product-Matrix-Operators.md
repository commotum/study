## The Hamilton product and matrix operators

The Hamilton product is the multiplication operation for two quaternions. Since quaternion multiplication is non-commutative,

$$
pq \neq qp
$$

in general.

Define two quaternions:

$$
p=(p_w,p_x,p_y,p_z)
=
p_w+p_x i+p_y j+p_z k
$$
$$
q=(q_w,q_x,q_y,q_z)
=
q_w+q_x i+q_y j+q_z k
$$

with the usual rules:

$$
i^2=j^2=k^2=ijk=-1
$$
$$
ij=k,\qquad jk=i,\qquad ki=j
$$
$$
ji=-k,\qquad kj=-i,\qquad ik=-j.
$$

There are two core operator forms.

**Left multiplication by $p$** means:

$$
q\mapsto pq.
$$

The multiplication representation, operator representation, and matrix representation are:

$$
\boxed{
pq
=
\left(
\begin{aligned}
& p_wq_w-p_xq_x-p_yq_y-p_zq_z,\\
& p_wq_x+p_xq_w+p_yq_z-p_zq_y,\\
& p_wq_y-p_xq_z+p_yq_w+p_zq_x,\\
& p_wq_z+p_xq_y-p_yq_x+p_zq_w
\end{aligned}
\right)
=
L(p)q
}
$$

where

$$
\boxed{
L(p)=
\begin{pmatrix}
p_w&-p_x&-p_y&-p_z\\
p_x&p_w&-p_z&p_y\\
p_y&p_z&p_w&-p_x\\
p_z&-p_y&p_x&p_w
\end{pmatrix}.
}
$$

Equivalently,

$$
\begin{pmatrix}
(pq)_w\\
(pq)_x\\
(pq)_y\\
(pq)_z
\end{pmatrix}
=
\begin{pmatrix}
p_w&-p_x&-p_y&-p_z\\
p_x&p_w&-p_z&p_y\\
p_y&p_z&p_w&-p_x\\
p_z&-p_y&p_x&p_w
\end{pmatrix}
\begin{pmatrix}
q_w\\
q_x\\
q_y\\
q_z
\end{pmatrix}.
$$

**Right multiplication by $p$** means:

$$
q\mapsto qp.
$$

The multiplication representation, operator representation, and matrix representation are:

$$
\boxed{
qp
=
\left(
\begin{aligned}
& q_wp_w-q_xp_x-q_yp_y-q_zp_z,\\
& q_wp_x+q_xp_w+q_yp_z-q_zp_y,\\
& q_wp_y-q_xp_z+q_yp_w+q_zp_x,\\
& q_wp_z+q_xp_y-q_yp_x+q_zp_w
\end{aligned}
\right)
=
R(p)q
}
$$

where

$$
\boxed{
R(p)=
\begin{pmatrix}
p_w&-p_x&-p_y&-p_z\\
p_x&p_w&p_z&-p_y\\
p_y&-p_z&p_w&p_x\\
p_z&p_y&-p_x&p_w
\end{pmatrix}.
}
$$

Equivalently,

$$
\begin{pmatrix}
(qp)_w\\
(qp)_x\\
(qp)_y\\
(qp)_z
\end{pmatrix}
=
\begin{pmatrix}
p_w&-p_x&-p_y&-p_z\\
p_x&p_w&p_z&-p_y\\
p_y&-p_z&p_w&p_x\\
p_z&p_y&-p_x&p_w
\end{pmatrix}
\begin{pmatrix}
q_w\\
q_x\\
q_y\\
q_z
\end{pmatrix}.
$$

