## One Qubit Gates

For each gate, we will give three forms:

1. the matrix form $G_{\mathbb C}$,
2. the split quaternion form $G_{\mathcal Q}=(u_G,\delta_G)$,
3. and the induced action on the canonical split basis states.

For a split quaternion gate

$$
G_{\mathcal Q}=(u_G,\delta_G),
$$

the split action on the physical-qubit $q=(r,\phi)$ is

$$
G_{\mathcal Q}(r,\phi)
=
(u_G r,\phi\delta_G).
$$

To compare with the collapsed quaternion basis $\{1,i,j,k\}$, we use the canonical split representatives

$$
(1,1),
\qquad
(i,1),
\qquad
(j,1),
\qquad
(k,1).
$$

After applying the split action, we collapse by Hamilton product:

$$
\bar q'=r'\phi'.
$$

Equivalently,

$$
\bar G(\bar q)=u_G\bar q\delta_G.
$$

## Identity Gate

The identity gate is the neutral example. It leaves the matrix state, the split physical-qubit state, and the collapsed quaternion basis unchanged.

The matrix form is

$$
I_{\mathbb C}
=
\begin{pmatrix}
1&0\\
0&1
\end{pmatrix}.
$$

The split quaternion form is

$$
I_{\mathcal Q}
=
(u_I,\delta_I)
=
(1,1),
$$

where

$$
u_I=\delta_I=1=(1,0,0,0).
$$

The split action on the basis states is

$$
I_{\mathcal Q}(1,1)=(1,1),
\qquad
I_{\mathcal Q}(i,1)=(i,1),
$$
$$
I_{\mathcal Q}(j,1)=(j,1),
\qquad
I_{\mathcal Q}(k,1)=(k,1).
$$

Collapsing each output by Hamilton product gives

$$
\bar I(1)=1,
\qquad
\bar I(i)=i,
\qquad
\bar I(j)=j,
\qquad
\bar I(k)=k.
$$

## Pauli X Gate

It may be tempting to identify the Pauli $X$ gate with the quaternion

$$
i=(0,1,0,0),
$$

because this is the quaternion basis element associated with the $x$-axis. However, under our unitary-to-quaternion dictionary, this quaternion does not produce $\sigma_x$ directly. It produces $\sigma_x$ with an extra scalar phase. The right phase component corrects this.

The matrix form is

$$
X_{\mathbb C}
=
\sigma_x
=
\begin{pmatrix}
0&1\\
1&0
\end{pmatrix}.
$$

The split quaternion form is

$$
X_{\mathcal Q}
=
(u_X,\delta_X)
=
(i,-k),
$$

where

$$
u_X=i=(0,1,0,0),
\qquad
\delta_X=-k=(0,0,0,-1).
$$

The split action on the basis states is

$$
X_{\mathcal Q}(1,1)=(i,-k),
\qquad
X_{\mathcal Q}(i,1)=(-1,-k),
$$
$$
X_{\mathcal Q}(j,1)=(k,-k),
\qquad
X_{\mathcal Q}(k,1)=(-j,-k).
$$

Collapsing each output by Hamilton product gives

$$
\bar X(1)=j,
\qquad
\bar X(i)=k,
\qquad
\bar X(j)=1,
\qquad
\bar X(k)=i.
$$

## Pauli Y Gate

The Pauli $Y$ gate is naturally associated with the $y$-axis, but the split representation still includes the right-side scalar phase component needed to match the exact Pauli matrix.

The matrix form is

$$
Y_{\mathbb C}
=
\sigma_y
=
\begin{pmatrix}
0&-i\\
i&0
\end{pmatrix}.
$$

The split quaternion form is

$$
Y_{\mathcal Q}
=
(u_Y,\delta_Y)
=
(j,k),
$$

where

$$
u_Y=j=(0,0,1,0),
\qquad
\delta_Y=k=(0,0,0,1).
$$

The split action on the basis states is

$$
Y_{\mathcal Q}(1,1)=(j,k),
\qquad
Y_{\mathcal Q}(i,1)=(-k,k),
$$
$$
Y_{\mathcal Q}(j,1)=(-1,k),
\qquad
Y_{\mathcal Q}(k,1)=(i,k).
$$

Collapsing each output by Hamilton product gives

$$
\bar Y(1)=i,
\qquad
\bar Y(i)=1,
\qquad
\bar Y(j)=-k,
\qquad
\bar Y(k)=-j.
$$

## Pauli Z Gate

The Pauli $Z$ gate is associated with the $z$-axis. Like $X$, the split representation includes a right-side phase correction.

The matrix form is

$$
Z_{\mathbb C}
=
\sigma_z
=
\begin{pmatrix}
1&0\\
0&-1
\end{pmatrix}.
$$

The split quaternion form is

$$
Z_{\mathcal Q}
=
(u_Z,\delta_Z)
=
(k,-k),
$$

where

$$
u_Z=k=(0,0,0,1),
\qquad
\delta_Z=-k=(0,0,0,-1).
$$

The split action on the basis states is

$$
Z_{\mathcal Q}(1,1)=(k,-k),
\qquad
Z_{\mathcal Q}(i,1)=(j,-k),
$$
$$
Z_{\mathcal Q}(j,1)=(-i,-k),
\qquad
Z_{\mathcal Q}(k,1)=(-1,-k).
$$

Collapsing each output by Hamilton product gives

$$
\bar Z(1)=1,
\qquad
\bar Z(i)=-i,
\qquad
\bar Z(j)=-j,
\qquad
\bar Z(k)=k.
$$

