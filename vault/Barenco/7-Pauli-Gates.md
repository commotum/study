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

## Pauli Gate Truth Tables

These tables use the uncollapsed physical-qubit action from [[6-Physical-Qubits]]:

$$
G_{\mathcal Q}(r,\phi)=(u_G r,\phi\delta_G).
$$

Here the input physical-qubit is the two-quaternion value

$$
q=(r,\phi),
$$

sampled over the canonical split basis representatives

$$
r,\phi\in\{1,i,j,k\}.
$$

Since there are four choices for $r$ and four choices for $\phi$, each canonical split table has $4\cdot4=16$ rows. If the signed representatives

$$
\{\pm1,\pm i,\pm j,\pm k\}
$$

are used for both components, the corresponding table has $8\cdot8=64$ rows. The gate itself is still the continuous map on $S^3\times S^3$; the table is only a finite canonical sample.

The collapsed-input column records

$$
\bar q=r\phi.
$$

The collapsed-state column records the collapsed output

$$
\bar q'=r'\phi',
$$

where

$$
(r',\phi')=G_{\mathcal Q}(r,\phi).
$$

The bit-reading columns use the projection $\Psi$ from [[3-Unit-Quaternions-Unitary-Matrices]]. On these canonical collapsed states, signs and $k$-axis factors are global phases, so

$$
\{1,-1,k,-k\}\mapsto |0\rangle,
\qquad
\{i,-i,j,-j\}\mapsto |1\rangle.
$$

Thus $(1,1)$ collapses to $1$ and reads as $|0\rangle$, while $(i,-k)$ collapses to $j$ and reads as $|1\rangle$.

### Pauli X

For

$$
X_{\mathcal Q}=(i,-k),
$$

the split update is

$$
(r,\phi)\mapsto(ir,\phi(-k)).
$$

| Input $(r,\phi)$ | Collapsed input $\bar q$ | Input read       | Output $X_{\mathcal Q}(r,\phi)$ | Collapsed state $\bar q'$ | Output read      |
| ---------------- | ------------------------ | ---------------- | ------------------------------- | ------------------------- | ---------------- |
| $(1,1)$          | $1$                      | $\lvert0\rangle$ | $(i,-k)$                        | $j$                       | $\lvert1\rangle$ |
| $(1,i)$          | $i$                      | $\lvert1\rangle$ | $(i,j)$                         | $k$                       | $\lvert0\rangle$ |
| $(1,j)$          | $j$                      | $\lvert1\rangle$ | $(i,-i)$                        | $1$                       | $\lvert0\rangle$ |
| $(1,k)$          | $k$                      | $\lvert0\rangle$ | $(i,1)$                         | $i$                       | $\lvert1\rangle$ |
| $(i,1)$          | $i$                      | $\lvert1\rangle$ | $(-1,-k)$                       | $k$                       | $\lvert0\rangle$ |
| $(i,i)$          | $-1$                     | $\lvert0\rangle$ | $(-1,j)$                        | $-j$                      | $\lvert1\rangle$ |
| $(i,j)$          | $k$                      | $\lvert0\rangle$ | $(-1,-i)$                       | $i$                       | $\lvert1\rangle$ |
| $(i,k)$          | $-j$                     | $\lvert1\rangle$ | $(-1,1)$                        | $-1$                      | $\lvert0\rangle$ |
| $(j,1)$          | $j$                      | $\lvert1\rangle$ | $(k,-k)$                        | $1$                       | $\lvert0\rangle$ |
| $(j,i)$          | $-k$                     | $\lvert0\rangle$ | $(k,j)$                         | $-i$                      | $\lvert1\rangle$ |
| $(j,j)$          | $-1$                     | $\lvert0\rangle$ | $(k,-i)$                        | $-j$                      | $\lvert1\rangle$ |
| $(j,k)$          | $i$                      | $\lvert1\rangle$ | $(k,1)$                         | $k$                       | $\lvert0\rangle$ |
| $(k,1)$          | $k$                      | $\lvert0\rangle$ | $(-j,-k)$                       | $i$                       | $\lvert1\rangle$ |
| $(k,i)$          | $j$                      | $\lvert1\rangle$ | $(-j,j)$                        | $1$                       | $\lvert0\rangle$ |
| $(k,j)$          | $-i$                     | $\lvert1\rangle$ | $(-j,-i)$                       | $-k$                      | $\lvert0\rangle$ |
| $(k,k)$          | $-1$                     | $\lvert0\rangle$ | $(-j,1)$                        | $-j$                      | $\lvert1\rangle$ |

### Negative Pauli X

The $-X$ gate differs from $X$ by a global phase. In the split representation this changes the right phase component:

$$
(-X)_{\mathcal Q}=(i,k).
$$

The split update is

$$
(r,\phi)\mapsto(ir,\phi k).
$$

Since $-X$ only changes the global phase relative to $X$, the bit reading is the same as for $X$, even though the collapsed quaternion representative may change sign.

| Input $(r,\phi)$ | Collapsed input $\bar q$ | Input read | Output $(-X)_{\mathcal Q}(r,\phi)$ | Collapsed state $\bar q'$ | Output read |
|---|---|---|---|---|---|
| $(1,1)$ | $1$ | $\lvert0\rangle$ | $(i,k)$ | $-j$ | $\lvert1\rangle$ |
| $(1,i)$ | $i$ | $\lvert1\rangle$ | $(i,-j)$ | $-k$ | $\lvert0\rangle$ |
| $(1,j)$ | $j$ | $\lvert1\rangle$ | $(i,i)$ | $-1$ | $\lvert0\rangle$ |
| $(1,k)$ | $k$ | $\lvert0\rangle$ | $(i,-1)$ | $-i$ | $\lvert1\rangle$ |
| $(i,1)$ | $i$ | $\lvert1\rangle$ | $(-1,k)$ | $-k$ | $\lvert0\rangle$ |
| $(i,i)$ | $-1$ | $\lvert0\rangle$ | $(-1,-j)$ | $j$ | $\lvert1\rangle$ |
| $(i,j)$ | $k$ | $\lvert0\rangle$ | $(-1,i)$ | $-i$ | $\lvert1\rangle$ |
| $(i,k)$ | $-j$ | $\lvert1\rangle$ | $(-1,-1)$ | $1$ | $\lvert0\rangle$ |
| $(j,1)$ | $j$ | $\lvert1\rangle$ | $(k,k)$ | $-1$ | $\lvert0\rangle$ |
| $(j,i)$ | $-k$ | $\lvert0\rangle$ | $(k,-j)$ | $i$ | $\lvert1\rangle$ |
| $(j,j)$ | $-1$ | $\lvert0\rangle$ | $(k,i)$ | $j$ | $\lvert1\rangle$ |
| $(j,k)$ | $i$ | $\lvert1\rangle$ | $(k,-1)$ | $-k$ | $\lvert0\rangle$ |
| $(k,1)$ | $k$ | $\lvert0\rangle$ | $(-j,k)$ | $-i$ | $\lvert1\rangle$ |
| $(k,i)$ | $j$ | $\lvert1\rangle$ | $(-j,-j)$ | $-1$ | $\lvert0\rangle$ |
| $(k,j)$ | $-i$ | $\lvert1\rangle$ | $(-j,i)$ | $k$ | $\lvert0\rangle$ |
| $(k,k)$ | $-1$ | $\lvert0\rangle$ | $(-j,-1)$ | $j$ | $\lvert1\rangle$ |

### Pauli Y

For

$$
Y_{\mathcal Q}=(j,k),
$$

the split update is

$$
(r,\phi)\mapsto(jr,\phi k).
$$

| Input $(r,\phi)$ | Collapsed input $\bar q$ | Input read | Output $Y_{\mathcal Q}(r,\phi)$ | Collapsed state $\bar q'$ | Output read |
|---|---|---|---|---|---|
| $(1,1)$ | $1$ | $\lvert0\rangle$ | $(j,k)$ | $i$ | $\lvert1\rangle$ |
| $(1,i)$ | $i$ | $\lvert1\rangle$ | $(j,-j)$ | $1$ | $\lvert0\rangle$ |
| $(1,j)$ | $j$ | $\lvert1\rangle$ | $(j,i)$ | $-k$ | $\lvert0\rangle$ |
| $(1,k)$ | $k$ | $\lvert0\rangle$ | $(j,-1)$ | $-j$ | $\lvert1\rangle$ |
| $(i,1)$ | $i$ | $\lvert1\rangle$ | $(-k,k)$ | $1$ | $\lvert0\rangle$ |
| $(i,i)$ | $-1$ | $\lvert0\rangle$ | $(-k,-j)$ | $-i$ | $\lvert1\rangle$ |
| $(i,j)$ | $k$ | $\lvert0\rangle$ | $(-k,i)$ | $-j$ | $\lvert1\rangle$ |
| $(i,k)$ | $-j$ | $\lvert1\rangle$ | $(-k,-1)$ | $k$ | $\lvert0\rangle$ |
| $(j,1)$ | $j$ | $\lvert1\rangle$ | $(-1,k)$ | $-k$ | $\lvert0\rangle$ |
| $(j,i)$ | $-k$ | $\lvert0\rangle$ | $(-1,-j)$ | $j$ | $\lvert1\rangle$ |
| $(j,j)$ | $-1$ | $\lvert0\rangle$ | $(-1,i)$ | $-i$ | $\lvert1\rangle$ |
| $(j,k)$ | $i$ | $\lvert1\rangle$ | $(-1,-1)$ | $1$ | $\lvert0\rangle$ |
| $(k,1)$ | $k$ | $\lvert0\rangle$ | $(i,k)$ | $-j$ | $\lvert1\rangle$ |
| $(k,i)$ | $j$ | $\lvert1\rangle$ | $(i,-j)$ | $-k$ | $\lvert0\rangle$ |
| $(k,j)$ | $-i$ | $\lvert1\rangle$ | $(i,i)$ | $-1$ | $\lvert0\rangle$ |
| $(k,k)$ | $-1$ | $\lvert0\rangle$ | $(i,-1)$ | $-i$ | $\lvert1\rangle$ |

### Pauli Z

For

$$
Z_{\mathcal Q}=(k,-k),
$$

the split update is

$$
(r,\phi)\mapsto(kr,\phi(-k)).
$$

| Input $(r,\phi)$ | Collapsed input $\bar q$ | Input read       | Output $Z_{\mathcal Q}(r,\phi)$ | Collapsed state $\bar q'$ | Output read      |
| ---------------- | ------------------------ | ---------------- | ------------------------------- | ------------------------- | ---------------- |
| $(1,1)$          | $1$                      | $\lvert0\rangle$ | $(k,-k)$                        | $1$                       | $\lvert0\rangle$ |
| $(1,i)$          | $i$                      | $\lvert1\rangle$ | $(k,j)$                         | $-i$                      | $\lvert1\rangle$ |
| $(1,j)$          | $j$                      | $\lvert1\rangle$ | $(k,-i)$                        | $-j$                      | $\lvert1\rangle$ |
| $(1,k)$          | $k$                      | $\lvert0\rangle$ | $(k,1)$                         | $k$                       | $\lvert0\rangle$ |
| $(i,1)$          | $i$                      | $\lvert1\rangle$ | $(j,-k)$                        | $-i$                      | $\lvert1\rangle$ |
| $(i,i)$          | $-1$                     | $\lvert0\rangle$ | $(j,j)$                         | $-1$                      | $\lvert0\rangle$ |
| $(i,j)$          | $k$                      | $\lvert0\rangle$ | $(j,-i)$                        | $k$                       | $\lvert0\rangle$ |
| $(i,k)$          | $-j$                     | $\lvert1\rangle$ | $(j,1)$                         | $j$                       | $\lvert1\rangle$ |
| $(j,1)$          | $j$                      | $\lvert1\rangle$ | $(-i,-k)$                       | $-j$                      | $\lvert1\rangle$ |
| $(j,i)$          | $-k$                     | $\lvert0\rangle$ | $(-i,j)$                        | $-k$                      | $\lvert0\rangle$ |
| $(j,j)$          | $-1$                     | $\lvert0\rangle$ | $(-i,-i)$                       | $-1$                      | $\lvert0\rangle$ |
| $(j,k)$          | $i$                      | $\lvert1\rangle$ | $(-i,1)$                        | $-i$                      | $\lvert1\rangle$ |
| $(k,1)$          | $k$                      | $\lvert0\rangle$ | $(-1,-k)$                       | $k$                       | $\lvert0\rangle$ |
| $(k,i)$          | $j$                      | $\lvert1\rangle$ | $(-1,j)$                        | $-j$                      | $\lvert1\rangle$ |
| $(k,j)$          | $-i$                     | $\lvert1\rangle$ | $(-1,-i)$                       | $i$                       | $\lvert1\rangle$ |
| $(k,k)$          | $-1$                     | $\lvert0\rangle$ | $(-1,1)$                        | $-1$                      | $\lvert0\rangle$ |

### Negative Pauli Z

The $-Z$ gate differs from $Z$ by a global phase. In the split representation this changes the right phase component:

$$
(-Z)_{\mathcal Q}=(k,k).
$$

The split update is

$$
(r,\phi)\mapsto(kr,\phi k).
$$

Since $-Z$ only changes the global phase relative to $Z$, the bit reading is the same as for $Z$, even though the collapsed quaternion representative may change sign.

| Input $(r,\phi)$ | Collapsed input $\bar q$ | Input read | Output $(-Z)_{\mathcal Q}(r,\phi)$ | Collapsed state $\bar q'$ | Output read |
|---|---|---|---|---|---|
| $(1,1)$ | $1$ | $\lvert0\rangle$ | $(k,k)$ | $-1$ | $\lvert0\rangle$ |
| $(1,i)$ | $i$ | $\lvert1\rangle$ | $(k,-j)$ | $i$ | $\lvert1\rangle$ |
| $(1,j)$ | $j$ | $\lvert1\rangle$ | $(k,i)$ | $j$ | $\lvert1\rangle$ |
| $(1,k)$ | $k$ | $\lvert0\rangle$ | $(k,-1)$ | $-k$ | $\lvert0\rangle$ |
| $(i,1)$ | $i$ | $\lvert1\rangle$ | $(j,k)$ | $i$ | $\lvert1\rangle$ |
| $(i,i)$ | $-1$ | $\lvert0\rangle$ | $(j,-j)$ | $1$ | $\lvert0\rangle$ |
| $(i,j)$ | $k$ | $\lvert0\rangle$ | $(j,i)$ | $-k$ | $\lvert0\rangle$ |
| $(i,k)$ | $-j$ | $\lvert1\rangle$ | $(j,-1)$ | $-j$ | $\lvert1\rangle$ |
| $(j,1)$ | $j$ | $\lvert1\rangle$ | $(-i,k)$ | $j$ | $\lvert1\rangle$ |
| $(j,i)$ | $-k$ | $\lvert0\rangle$ | $(-i,-j)$ | $k$ | $\lvert0\rangle$ |
| $(j,j)$ | $-1$ | $\lvert0\rangle$ | $(-i,i)$ | $1$ | $\lvert0\rangle$ |
| $(j,k)$ | $i$ | $\lvert1\rangle$ | $(-i,-1)$ | $i$ | $\lvert1\rangle$ |
| $(k,1)$ | $k$ | $\lvert0\rangle$ | $(-1,k)$ | $-k$ | $\lvert0\rangle$ |
| $(k,i)$ | $j$ | $\lvert1\rangle$ | $(-1,-j)$ | $j$ | $\lvert1\rangle$ |
| $(k,j)$ | $-i$ | $\lvert1\rangle$ | $(-1,i)$ | $-i$ | $\lvert1\rangle$ |
| $(k,k)$ | $-1$ | $\lvert0\rangle$ | $(-1,-1)$ | $1$ | $\lvert0\rangle$ |

## Two-Qubit Z-Control-As-Gate Truth Table

This is a control-as-gate table, not the usual textbook controlled-$Z$ table. I write the phase-state as $\phi$, rather than $\theta$, to match [[6-Physical-Qubits]].

The two input physical qubits are

$$
Q_c=(r_c,\phi_c),
\qquad
Q_t=(r_t,\phi_t),
$$

sampled over the same canonical split representatives

$$
r_c,\phi_c,r_t,\phi_t\in\{1,i,j,k\}.
$$

The collapsed input states are

$$
\bar q_c=r_c\phi_c,
\qquad
\bar q_t=r_t\phi_t.
$$

First apply the Pauli $Z$ gate to the control qubit:

$$
Q_c'=Z_{\mathcal Q}(Q_c)=(kr_c,\phi_c(-k)).
$$

Then use that output pair as the physical gate applied to the target input:

$$
Q_t'=Q_c'(Q_t)=(r_c'r_t,\phi_t\phi_c').
$$

The collapsed output states are

$$
\bar q_c'=r_c'\phi_c',
\qquad
\bar q_t'=r_t'\phi_t'.
$$

Since each input qubit has 16 canonical split states, the two-qubit canonical table has $16\cdot16=256$ rows.

| Input $Q_c$ | Collapsed $\bar q_c$ | Input $Q_t$ | Collapsed $\bar q_t$ | Input read | Output $Q_c'=Z_{\mathcal Q}(Q_c)$ | Output $Q_t'=Q_c'(Q_t)$ | Collapsed $\bar q_c'$ | Collapsed $\bar q_t'$ | Output read |
|---|---|---|---|---|---|---|---|---|---|
| $(1,1)$ | $1$ | $(1,1)$ | $1$ | $\lvert00\rangle$ | $(k,-k)$ | $(k,-k)$ | $1$ | $1$ | $\lvert00\rangle$ |
| $(1,1)$ | $1$ | $(1,i)$ | $i$ | $\lvert01\rangle$ | $(k,-k)$ | $(k,j)$ | $1$ | $-i$ | $\lvert01\rangle$ |
| $(1,1)$ | $1$ | $(1,j)$ | $j$ | $\lvert01\rangle$ | $(k,-k)$ | $(k,-i)$ | $1$ | $-j$ | $\lvert01\rangle$ |
| $(1,1)$ | $1$ | $(1,k)$ | $k$ | $\lvert00\rangle$ | $(k,-k)$ | $(k,1)$ | $1$ | $k$ | $\lvert00\rangle$ |
| $(1,1)$ | $1$ | $(i,1)$ | $i$ | $\lvert01\rangle$ | $(k,-k)$ | $(j,-k)$ | $1$ | $-i$ | $\lvert01\rangle$ |
| $(1,1)$ | $1$ | $(i,i)$ | $-1$ | $\lvert00\rangle$ | $(k,-k)$ | $(j,j)$ | $1$ | $-1$ | $\lvert00\rangle$ |
| $(1,1)$ | $1$ | $(i,j)$ | $k$ | $\lvert00\rangle$ | $(k,-k)$ | $(j,-i)$ | $1$ | $k$ | $\lvert00\rangle$ |
| $(1,1)$ | $1$ | $(i,k)$ | $-j$ | $\lvert01\rangle$ | $(k,-k)$ | $(j,1)$ | $1$ | $j$ | $\lvert01\rangle$ |
| $(1,1)$ | $1$ | $(j,1)$ | $j$ | $\lvert01\rangle$ | $(k,-k)$ | $(-i,-k)$ | $1$ | $-j$ | $\lvert01\rangle$ |
| $(1,1)$ | $1$ | $(j,i)$ | $-k$ | $\lvert00\rangle$ | $(k,-k)$ | $(-i,j)$ | $1$ | $-k$ | $\lvert00\rangle$ |
| $(1,1)$ | $1$ | $(j,j)$ | $-1$ | $\lvert00\rangle$ | $(k,-k)$ | $(-i,-i)$ | $1$ | $-1$ | $\lvert00\rangle$ |
| $(1,1)$ | $1$ | $(j,k)$ | $i$ | $\lvert01\rangle$ | $(k,-k)$ | $(-i,1)$ | $1$ | $-i$ | $\lvert01\rangle$ |
| $(1,1)$ | $1$ | $(k,1)$ | $k$ | $\lvert00\rangle$ | $(k,-k)$ | $(-1,-k)$ | $1$ | $k$ | $\lvert00\rangle$ |
| $(1,1)$ | $1$ | $(k,i)$ | $j$ | $\lvert01\rangle$ | $(k,-k)$ | $(-1,j)$ | $1$ | $-j$ | $\lvert01\rangle$ |
| $(1,1)$ | $1$ | $(k,j)$ | $-i$ | $\lvert01\rangle$ | $(k,-k)$ | $(-1,-i)$ | $1$ | $i$ | $\lvert01\rangle$ |
| $(1,1)$ | $1$ | $(k,k)$ | $-1$ | $\lvert00\rangle$ | $(k,-k)$ | $(-1,1)$ | $1$ | $-1$ | $\lvert00\rangle$ |
| $(1,i)$ | $i$ | $(1,1)$ | $1$ | $\lvert10\rangle$ | $(k,j)$ | $(k,j)$ | $-i$ | $-i$ | $\lvert11\rangle$ |
| $(1,i)$ | $i$ | $(1,i)$ | $i$ | $\lvert11\rangle$ | $(k,j)$ | $(k,k)$ | $-i$ | $-1$ | $\lvert10\rangle$ |
| $(1,i)$ | $i$ | $(1,j)$ | $j$ | $\lvert11\rangle$ | $(k,j)$ | $(k,-1)$ | $-i$ | $-k$ | $\lvert10\rangle$ |
| $(1,i)$ | $i$ | $(1,k)$ | $k$ | $\lvert10\rangle$ | $(k,j)$ | $(k,-i)$ | $-i$ | $-j$ | $\lvert11\rangle$ |
| $(1,i)$ | $i$ | $(i,1)$ | $i$ | $\lvert11\rangle$ | $(k,j)$ | $(j,j)$ | $-i$ | $-1$ | $\lvert10\rangle$ |
| $(1,i)$ | $i$ | $(i,i)$ | $-1$ | $\lvert10\rangle$ | $(k,j)$ | $(j,k)$ | $-i$ | $i$ | $\lvert11\rangle$ |
| $(1,i)$ | $i$ | $(i,j)$ | $k$ | $\lvert10\rangle$ | $(k,j)$ | $(j,-1)$ | $-i$ | $-j$ | $\lvert11\rangle$ |
| $(1,i)$ | $i$ | $(i,k)$ | $-j$ | $\lvert11\rangle$ | $(k,j)$ | $(j,-i)$ | $-i$ | $k$ | $\lvert10\rangle$ |
| $(1,i)$ | $i$ | $(j,1)$ | $j$ | $\lvert11\rangle$ | $(k,j)$ | $(-i,j)$ | $-i$ | $-k$ | $\lvert10\rangle$ |
| $(1,i)$ | $i$ | $(j,i)$ | $-k$ | $\lvert10\rangle$ | $(k,j)$ | $(-i,k)$ | $-i$ | $j$ | $\lvert11\rangle$ |
| $(1,i)$ | $i$ | $(j,j)$ | $-1$ | $\lvert10\rangle$ | $(k,j)$ | $(-i,-1)$ | $-i$ | $i$ | $\lvert11\rangle$ |
| $(1,i)$ | $i$ | $(j,k)$ | $i$ | $\lvert11\rangle$ | $(k,j)$ | $(-i,-i)$ | $-i$ | $-1$ | $\lvert10\rangle$ |
| $(1,i)$ | $i$ | $(k,1)$ | $k$ | $\lvert10\rangle$ | $(k,j)$ | $(-1,j)$ | $-i$ | $-j$ | $\lvert11\rangle$ |
| $(1,i)$ | $i$ | $(k,i)$ | $j$ | $\lvert11\rangle$ | $(k,j)$ | $(-1,k)$ | $-i$ | $-k$ | $\lvert10\rangle$ |
| $(1,i)$ | $i$ | $(k,j)$ | $-i$ | $\lvert11\rangle$ | $(k,j)$ | $(-1,-1)$ | $-i$ | $1$ | $\lvert10\rangle$ |
| $(1,i)$ | $i$ | $(k,k)$ | $-1$ | $\lvert10\rangle$ | $(k,j)$ | $(-1,-i)$ | $-i$ | $i$ | $\lvert11\rangle$ |
| $(1,j)$ | $j$ | $(1,1)$ | $1$ | $\lvert10\rangle$ | $(k,-i)$ | $(k,-i)$ | $-j$ | $-j$ | $\lvert11\rangle$ |
| $(1,j)$ | $j$ | $(1,i)$ | $i$ | $\lvert11\rangle$ | $(k,-i)$ | $(k,1)$ | $-j$ | $k$ | $\lvert10\rangle$ |
| $(1,j)$ | $j$ | $(1,j)$ | $j$ | $\lvert11\rangle$ | $(k,-i)$ | $(k,k)$ | $-j$ | $-1$ | $\lvert10\rangle$ |
| $(1,j)$ | $j$ | $(1,k)$ | $k$ | $\lvert10\rangle$ | $(k,-i)$ | $(k,-j)$ | $-j$ | $i$ | $\lvert11\rangle$ |
| $(1,j)$ | $j$ | $(i,1)$ | $i$ | $\lvert11\rangle$ | $(k,-i)$ | $(j,-i)$ | $-j$ | $k$ | $\lvert10\rangle$ |
| $(1,j)$ | $j$ | $(i,i)$ | $-1$ | $\lvert10\rangle$ | $(k,-i)$ | $(j,1)$ | $-j$ | $j$ | $\lvert11\rangle$ |
| $(1,j)$ | $j$ | $(i,j)$ | $k$ | $\lvert10\rangle$ | $(k,-i)$ | $(j,k)$ | $-j$ | $i$ | $\lvert11\rangle$ |
| $(1,j)$ | $j$ | $(i,k)$ | $-j$ | $\lvert11\rangle$ | $(k,-i)$ | $(j,-j)$ | $-j$ | $1$ | $\lvert10\rangle$ |
| $(1,j)$ | $j$ | $(j,1)$ | $j$ | $\lvert11\rangle$ | $(k,-i)$ | $(-i,-i)$ | $-j$ | $-1$ | $\lvert10\rangle$ |
| $(1,j)$ | $j$ | $(j,i)$ | $-k$ | $\lvert10\rangle$ | $(k,-i)$ | $(-i,1)$ | $-j$ | $-i$ | $\lvert11\rangle$ |
| $(1,j)$ | $j$ | $(j,j)$ | $-1$ | $\lvert10\rangle$ | $(k,-i)$ | $(-i,k)$ | $-j$ | $j$ | $\lvert11\rangle$ |
| $(1,j)$ | $j$ | $(j,k)$ | $i$ | $\lvert11\rangle$ | $(k,-i)$ | $(-i,-j)$ | $-j$ | $k$ | $\lvert10\rangle$ |
| $(1,j)$ | $j$ | $(k,1)$ | $k$ | $\lvert10\rangle$ | $(k,-i)$ | $(-1,-i)$ | $-j$ | $i$ | $\lvert11\rangle$ |
| $(1,j)$ | $j$ | $(k,i)$ | $j$ | $\lvert11\rangle$ | $(k,-i)$ | $(-1,1)$ | $-j$ | $-1$ | $\lvert10\rangle$ |
| $(1,j)$ | $j$ | $(k,j)$ | $-i$ | $\lvert11\rangle$ | $(k,-i)$ | $(-1,k)$ | $-j$ | $-k$ | $\lvert10\rangle$ |
| $(1,j)$ | $j$ | $(k,k)$ | $-1$ | $\lvert10\rangle$ | $(k,-i)$ | $(-1,-j)$ | $-j$ | $j$ | $\lvert11\rangle$ |
| $(1,k)$ | $k$ | $(1,1)$ | $1$ | $\lvert00\rangle$ | $(k,1)$ | $(k,1)$ | $k$ | $k$ | $\lvert00\rangle$ |
| $(1,k)$ | $k$ | $(1,i)$ | $i$ | $\lvert01\rangle$ | $(k,1)$ | $(k,i)$ | $k$ | $j$ | $\lvert01\rangle$ |
| $(1,k)$ | $k$ | $(1,j)$ | $j$ | $\lvert01\rangle$ | $(k,1)$ | $(k,j)$ | $k$ | $-i$ | $\lvert01\rangle$ |
| $(1,k)$ | $k$ | $(1,k)$ | $k$ | $\lvert00\rangle$ | $(k,1)$ | $(k,k)$ | $k$ | $-1$ | $\lvert00\rangle$ |
| $(1,k)$ | $k$ | $(i,1)$ | $i$ | $\lvert01\rangle$ | $(k,1)$ | $(j,1)$ | $k$ | $j$ | $\lvert01\rangle$ |
| $(1,k)$ | $k$ | $(i,i)$ | $-1$ | $\lvert00\rangle$ | $(k,1)$ | $(j,i)$ | $k$ | $-k$ | $\lvert00\rangle$ |
| $(1,k)$ | $k$ | $(i,j)$ | $k$ | $\lvert00\rangle$ | $(k,1)$ | $(j,j)$ | $k$ | $-1$ | $\lvert00\rangle$ |
| $(1,k)$ | $k$ | $(i,k)$ | $-j$ | $\lvert01\rangle$ | $(k,1)$ | $(j,k)$ | $k$ | $i$ | $\lvert01\rangle$ |
| $(1,k)$ | $k$ | $(j,1)$ | $j$ | $\lvert01\rangle$ | $(k,1)$ | $(-i,1)$ | $k$ | $-i$ | $\lvert01\rangle$ |
| $(1,k)$ | $k$ | $(j,i)$ | $-k$ | $\lvert00\rangle$ | $(k,1)$ | $(-i,i)$ | $k$ | $1$ | $\lvert00\rangle$ |
| $(1,k)$ | $k$ | $(j,j)$ | $-1$ | $\lvert00\rangle$ | $(k,1)$ | $(-i,j)$ | $k$ | $-k$ | $\lvert00\rangle$ |
| $(1,k)$ | $k$ | $(j,k)$ | $i$ | $\lvert01\rangle$ | $(k,1)$ | $(-i,k)$ | $k$ | $j$ | $\lvert01\rangle$ |
| $(1,k)$ | $k$ | $(k,1)$ | $k$ | $\lvert00\rangle$ | $(k,1)$ | $(-1,1)$ | $k$ | $-1$ | $\lvert00\rangle$ |
| $(1,k)$ | $k$ | $(k,i)$ | $j$ | $\lvert01\rangle$ | $(k,1)$ | $(-1,i)$ | $k$ | $-i$ | $\lvert01\rangle$ |
| $(1,k)$ | $k$ | $(k,j)$ | $-i$ | $\lvert01\rangle$ | $(k,1)$ | $(-1,j)$ | $k$ | $-j$ | $\lvert01\rangle$ |
| $(1,k)$ | $k$ | $(k,k)$ | $-1$ | $\lvert00\rangle$ | $(k,1)$ | $(-1,k)$ | $k$ | $-k$ | $\lvert00\rangle$ |
| $(i,1)$ | $i$ | $(1,1)$ | $1$ | $\lvert10\rangle$ | $(j,-k)$ | $(j,-k)$ | $-i$ | $-i$ | $\lvert11\rangle$ |
| $(i,1)$ | $i$ | $(1,i)$ | $i$ | $\lvert11\rangle$ | $(j,-k)$ | $(j,j)$ | $-i$ | $-1$ | $\lvert10\rangle$ |
| $(i,1)$ | $i$ | $(1,j)$ | $j$ | $\lvert11\rangle$ | $(j,-k)$ | $(j,-i)$ | $-i$ | $k$ | $\lvert10\rangle$ |
| $(i,1)$ | $i$ | $(1,k)$ | $k$ | $\lvert10\rangle$ | $(j,-k)$ | $(j,1)$ | $-i$ | $j$ | $\lvert11\rangle$ |
| $(i,1)$ | $i$ | $(i,1)$ | $i$ | $\lvert11\rangle$ | $(j,-k)$ | $(-k,-k)$ | $-i$ | $-1$ | $\lvert10\rangle$ |
| $(i,1)$ | $i$ | $(i,i)$ | $-1$ | $\lvert10\rangle$ | $(j,-k)$ | $(-k,j)$ | $-i$ | $i$ | $\lvert11\rangle$ |
| $(i,1)$ | $i$ | $(i,j)$ | $k$ | $\lvert10\rangle$ | $(j,-k)$ | $(-k,-i)$ | $-i$ | $j$ | $\lvert11\rangle$ |
| $(i,1)$ | $i$ | $(i,k)$ | $-j$ | $\lvert11\rangle$ | $(j,-k)$ | $(-k,1)$ | $-i$ | $-k$ | $\lvert10\rangle$ |
| $(i,1)$ | $i$ | $(j,1)$ | $j$ | $\lvert11\rangle$ | $(j,-k)$ | $(-1,-k)$ | $-i$ | $k$ | $\lvert10\rangle$ |
| $(i,1)$ | $i$ | $(j,i)$ | $-k$ | $\lvert10\rangle$ | $(j,-k)$ | $(-1,j)$ | $-i$ | $-j$ | $\lvert11\rangle$ |
| $(i,1)$ | $i$ | $(j,j)$ | $-1$ | $\lvert10\rangle$ | $(j,-k)$ | $(-1,-i)$ | $-i$ | $i$ | $\lvert11\rangle$ |
| $(i,1)$ | $i$ | $(j,k)$ | $i$ | $\lvert11\rangle$ | $(j,-k)$ | $(-1,1)$ | $-i$ | $-1$ | $\lvert10\rangle$ |
| $(i,1)$ | $i$ | $(k,1)$ | $k$ | $\lvert10\rangle$ | $(j,-k)$ | $(i,-k)$ | $-i$ | $j$ | $\lvert11\rangle$ |
| $(i,1)$ | $i$ | $(k,i)$ | $j$ | $\lvert11\rangle$ | $(j,-k)$ | $(i,j)$ | $-i$ | $k$ | $\lvert10\rangle$ |
| $(i,1)$ | $i$ | $(k,j)$ | $-i$ | $\lvert11\rangle$ | $(j,-k)$ | $(i,-i)$ | $-i$ | $1$ | $\lvert10\rangle$ |
| $(i,1)$ | $i$ | $(k,k)$ | $-1$ | $\lvert10\rangle$ | $(j,-k)$ | $(i,1)$ | $-i$ | $i$ | $\lvert11\rangle$ |
| $(i,i)$ | $-1$ | $(1,1)$ | $1$ | $\lvert00\rangle$ | $(j,j)$ | $(j,j)$ | $-1$ | $-1$ | $\lvert00\rangle$ |
| $(i,i)$ | $-1$ | $(1,i)$ | $i$ | $\lvert01\rangle$ | $(j,j)$ | $(j,k)$ | $-1$ | $i$ | $\lvert01\rangle$ |
| $(i,i)$ | $-1$ | $(1,j)$ | $j$ | $\lvert01\rangle$ | $(j,j)$ | $(j,-1)$ | $-1$ | $-j$ | $\lvert01\rangle$ |
| $(i,i)$ | $-1$ | $(1,k)$ | $k$ | $\lvert00\rangle$ | $(j,j)$ | $(j,-i)$ | $-1$ | $k$ | $\lvert00\rangle$ |
| $(i,i)$ | $-1$ | $(i,1)$ | $i$ | $\lvert01\rangle$ | $(j,j)$ | $(-k,j)$ | $-1$ | $i$ | $\lvert01\rangle$ |
| $(i,i)$ | $-1$ | $(i,i)$ | $-1$ | $\lvert00\rangle$ | $(j,j)$ | $(-k,k)$ | $-1$ | $1$ | $\lvert00\rangle$ |
| $(i,i)$ | $-1$ | $(i,j)$ | $k$ | $\lvert00\rangle$ | $(j,j)$ | $(-k,-1)$ | $-1$ | $k$ | $\lvert00\rangle$ |
| $(i,i)$ | $-1$ | $(i,k)$ | $-j$ | $\lvert01\rangle$ | $(j,j)$ | $(-k,-i)$ | $-1$ | $j$ | $\lvert01\rangle$ |
| $(i,i)$ | $-1$ | $(j,1)$ | $j$ | $\lvert01\rangle$ | $(j,j)$ | $(-1,j)$ | $-1$ | $-j$ | $\lvert01\rangle$ |
| $(i,i)$ | $-1$ | $(j,i)$ | $-k$ | $\lvert00\rangle$ | $(j,j)$ | $(-1,k)$ | $-1$ | $-k$ | $\lvert00\rangle$ |
| $(i,i)$ | $-1$ | $(j,j)$ | $-1$ | $\lvert00\rangle$ | $(j,j)$ | $(-1,-1)$ | $-1$ | $1$ | $\lvert00\rangle$ |
| $(i,i)$ | $-1$ | $(j,k)$ | $i$ | $\lvert01\rangle$ | $(j,j)$ | $(-1,-i)$ | $-1$ | $i$ | $\lvert01\rangle$ |
| $(i,i)$ | $-1$ | $(k,1)$ | $k$ | $\lvert00\rangle$ | $(j,j)$ | $(i,j)$ | $-1$ | $k$ | $\lvert00\rangle$ |
| $(i,i)$ | $-1$ | $(k,i)$ | $j$ | $\lvert01\rangle$ | $(j,j)$ | $(i,k)$ | $-1$ | $-j$ | $\lvert01\rangle$ |
| $(i,i)$ | $-1$ | $(k,j)$ | $-i$ | $\lvert01\rangle$ | $(j,j)$ | $(i,-1)$ | $-1$ | $-i$ | $\lvert01\rangle$ |
| $(i,i)$ | $-1$ | $(k,k)$ | $-1$ | $\lvert00\rangle$ | $(j,j)$ | $(i,-i)$ | $-1$ | $1$ | $\lvert00\rangle$ |
| $(i,j)$ | $k$ | $(1,1)$ | $1$ | $\lvert00\rangle$ | $(j,-i)$ | $(j,-i)$ | $k$ | $k$ | $\lvert00\rangle$ |
| $(i,j)$ | $k$ | $(1,i)$ | $i$ | $\lvert01\rangle$ | $(j,-i)$ | $(j,1)$ | $k$ | $j$ | $\lvert01\rangle$ |
| $(i,j)$ | $k$ | $(1,j)$ | $j$ | $\lvert01\rangle$ | $(j,-i)$ | $(j,k)$ | $k$ | $i$ | $\lvert01\rangle$ |
| $(i,j)$ | $k$ | $(1,k)$ | $k$ | $\lvert00\rangle$ | $(j,-i)$ | $(j,-j)$ | $k$ | $1$ | $\lvert00\rangle$ |
| $(i,j)$ | $k$ | $(i,1)$ | $i$ | $\lvert01\rangle$ | $(j,-i)$ | $(-k,-i)$ | $k$ | $j$ | $\lvert01\rangle$ |
| $(i,j)$ | $k$ | $(i,i)$ | $-1$ | $\lvert00\rangle$ | $(j,-i)$ | $(-k,1)$ | $k$ | $-k$ | $\lvert00\rangle$ |
| $(i,j)$ | $k$ | $(i,j)$ | $k$ | $\lvert00\rangle$ | $(j,-i)$ | $(-k,k)$ | $k$ | $1$ | $\lvert00\rangle$ |
| $(i,j)$ | $k$ | $(i,k)$ | $-j$ | $\lvert01\rangle$ | $(j,-i)$ | $(-k,-j)$ | $k$ | $-i$ | $\lvert01\rangle$ |
| $(i,j)$ | $k$ | $(j,1)$ | $j$ | $\lvert01\rangle$ | $(j,-i)$ | $(-1,-i)$ | $k$ | $i$ | $\lvert01\rangle$ |
| $(i,j)$ | $k$ | $(j,i)$ | $-k$ | $\lvert00\rangle$ | $(j,-i)$ | $(-1,1)$ | $k$ | $-1$ | $\lvert00\rangle$ |
| $(i,j)$ | $k$ | $(j,j)$ | $-1$ | $\lvert00\rangle$ | $(j,-i)$ | $(-1,k)$ | $k$ | $-k$ | $\lvert00\rangle$ |
| $(i,j)$ | $k$ | $(j,k)$ | $i$ | $\lvert01\rangle$ | $(j,-i)$ | $(-1,-j)$ | $k$ | $j$ | $\lvert01\rangle$ |
| $(i,j)$ | $k$ | $(k,1)$ | $k$ | $\lvert00\rangle$ | $(j,-i)$ | $(i,-i)$ | $k$ | $1$ | $\lvert00\rangle$ |
| $(i,j)$ | $k$ | $(k,i)$ | $j$ | $\lvert01\rangle$ | $(j,-i)$ | $(i,1)$ | $k$ | $i$ | $\lvert01\rangle$ |
| $(i,j)$ | $k$ | $(k,j)$ | $-i$ | $\lvert01\rangle$ | $(j,-i)$ | $(i,k)$ | $k$ | $-j$ | $\lvert01\rangle$ |
| $(i,j)$ | $k$ | $(k,k)$ | $-1$ | $\lvert00\rangle$ | $(j,-i)$ | $(i,-j)$ | $k$ | $-k$ | $\lvert00\rangle$ |
| $(i,k)$ | $-j$ | $(1,1)$ | $1$ | $\lvert10\rangle$ | $(j,1)$ | $(j,1)$ | $j$ | $j$ | $\lvert11\rangle$ |
| $(i,k)$ | $-j$ | $(1,i)$ | $i$ | $\lvert11\rangle$ | $(j,1)$ | $(j,i)$ | $j$ | $-k$ | $\lvert10\rangle$ |
| $(i,k)$ | $-j$ | $(1,j)$ | $j$ | $\lvert11\rangle$ | $(j,1)$ | $(j,j)$ | $j$ | $-1$ | $\lvert10\rangle$ |
| $(i,k)$ | $-j$ | $(1,k)$ | $k$ | $\lvert10\rangle$ | $(j,1)$ | $(j,k)$ | $j$ | $i$ | $\lvert11\rangle$ |
| $(i,k)$ | $-j$ | $(i,1)$ | $i$ | $\lvert11\rangle$ | $(j,1)$ | $(-k,1)$ | $j$ | $-k$ | $\lvert10\rangle$ |
| $(i,k)$ | $-j$ | $(i,i)$ | $-1$ | $\lvert10\rangle$ | $(j,1)$ | $(-k,i)$ | $j$ | $-j$ | $\lvert11\rangle$ |
| $(i,k)$ | $-j$ | $(i,j)$ | $k$ | $\lvert10\rangle$ | $(j,1)$ | $(-k,j)$ | $j$ | $i$ | $\lvert11\rangle$ |
| $(i,k)$ | $-j$ | $(i,k)$ | $-j$ | $\lvert11\rangle$ | $(j,1)$ | $(-k,k)$ | $j$ | $1$ | $\lvert10\rangle$ |
| $(i,k)$ | $-j$ | $(j,1)$ | $j$ | $\lvert11\rangle$ | $(j,1)$ | $(-1,1)$ | $j$ | $-1$ | $\lvert10\rangle$ |
| $(i,k)$ | $-j$ | $(j,i)$ | $-k$ | $\lvert10\rangle$ | $(j,1)$ | $(-1,i)$ | $j$ | $-i$ | $\lvert11\rangle$ |
| $(i,k)$ | $-j$ | $(j,j)$ | $-1$ | $\lvert10\rangle$ | $(j,1)$ | $(-1,j)$ | $j$ | $-j$ | $\lvert11\rangle$ |
| $(i,k)$ | $-j$ | $(j,k)$ | $i$ | $\lvert11\rangle$ | $(j,1)$ | $(-1,k)$ | $j$ | $-k$ | $\lvert10\rangle$ |
| $(i,k)$ | $-j$ | $(k,1)$ | $k$ | $\lvert10\rangle$ | $(j,1)$ | $(i,1)$ | $j$ | $i$ | $\lvert11\rangle$ |
| $(i,k)$ | $-j$ | $(k,i)$ | $j$ | $\lvert11\rangle$ | $(j,1)$ | $(i,i)$ | $j$ | $-1$ | $\lvert10\rangle$ |
| $(i,k)$ | $-j$ | $(k,j)$ | $-i$ | $\lvert11\rangle$ | $(j,1)$ | $(i,j)$ | $j$ | $k$ | $\lvert10\rangle$ |
| $(i,k)$ | $-j$ | $(k,k)$ | $-1$ | $\lvert10\rangle$ | $(j,1)$ | $(i,k)$ | $j$ | $-j$ | $\lvert11\rangle$ |
| $(j,1)$ | $j$ | $(1,1)$ | $1$ | $\lvert10\rangle$ | $(-i,-k)$ | $(-i,-k)$ | $-j$ | $-j$ | $\lvert11\rangle$ |
| $(j,1)$ | $j$ | $(1,i)$ | $i$ | $\lvert11\rangle$ | $(-i,-k)$ | $(-i,j)$ | $-j$ | $-k$ | $\lvert10\rangle$ |
| $(j,1)$ | $j$ | $(1,j)$ | $j$ | $\lvert11\rangle$ | $(-i,-k)$ | $(-i,-i)$ | $-j$ | $-1$ | $\lvert10\rangle$ |
| $(j,1)$ | $j$ | $(1,k)$ | $k$ | $\lvert10\rangle$ | $(-i,-k)$ | $(-i,1)$ | $-j$ | $-i$ | $\lvert11\rangle$ |
| $(j,1)$ | $j$ | $(i,1)$ | $i$ | $\lvert11\rangle$ | $(-i,-k)$ | $(1,-k)$ | $-j$ | $-k$ | $\lvert10\rangle$ |
| $(j,1)$ | $j$ | $(i,i)$ | $-1$ | $\lvert10\rangle$ | $(-i,-k)$ | $(1,j)$ | $-j$ | $j$ | $\lvert11\rangle$ |
| $(j,1)$ | $j$ | $(i,j)$ | $k$ | $\lvert10\rangle$ | $(-i,-k)$ | $(1,-i)$ | $-j$ | $-i$ | $\lvert11\rangle$ |
| $(j,1)$ | $j$ | $(i,k)$ | $-j$ | $\lvert11\rangle$ | $(-i,-k)$ | $(1,1)$ | $-j$ | $1$ | $\lvert10\rangle$ |
| $(j,1)$ | $j$ | $(j,1)$ | $j$ | $\lvert11\rangle$ | $(-i,-k)$ | $(-k,-k)$ | $-j$ | $-1$ | $\lvert10\rangle$ |
| $(j,1)$ | $j$ | $(j,i)$ | $-k$ | $\lvert10\rangle$ | $(-i,-k)$ | $(-k,j)$ | $-j$ | $i$ | $\lvert11\rangle$ |
| $(j,1)$ | $j$ | $(j,j)$ | $-1$ | $\lvert10\rangle$ | $(-i,-k)$ | $(-k,-i)$ | $-j$ | $j$ | $\lvert11\rangle$ |
| $(j,1)$ | $j$ | $(j,k)$ | $i$ | $\lvert11\rangle$ | $(-i,-k)$ | $(-k,1)$ | $-j$ | $-k$ | $\lvert10\rangle$ |
| $(j,1)$ | $j$ | $(k,1)$ | $k$ | $\lvert10\rangle$ | $(-i,-k)$ | $(j,-k)$ | $-j$ | $-i$ | $\lvert11\rangle$ |
| $(j,1)$ | $j$ | $(k,i)$ | $j$ | $\lvert11\rangle$ | $(-i,-k)$ | $(j,j)$ | $-j$ | $-1$ | $\lvert10\rangle$ |
| $(j,1)$ | $j$ | $(k,j)$ | $-i$ | $\lvert11\rangle$ | $(-i,-k)$ | $(j,-i)$ | $-j$ | $k$ | $\lvert10\rangle$ |
| $(j,1)$ | $j$ | $(k,k)$ | $-1$ | $\lvert10\rangle$ | $(-i,-k)$ | $(j,1)$ | $-j$ | $j$ | $\lvert11\rangle$ |
| $(j,i)$ | $-k$ | $(1,1)$ | $1$ | $\lvert00\rangle$ | $(-i,j)$ | $(-i,j)$ | $-k$ | $-k$ | $\lvert00\rangle$ |
| $(j,i)$ | $-k$ | $(1,i)$ | $i$ | $\lvert01\rangle$ | $(-i,j)$ | $(-i,k)$ | $-k$ | $j$ | $\lvert01\rangle$ |
| $(j,i)$ | $-k$ | $(1,j)$ | $j$ | $\lvert01\rangle$ | $(-i,j)$ | $(-i,-1)$ | $-k$ | $i$ | $\lvert01\rangle$ |
| $(j,i)$ | $-k$ | $(1,k)$ | $k$ | $\lvert00\rangle$ | $(-i,j)$ | $(-i,-i)$ | $-k$ | $-1$ | $\lvert00\rangle$ |
| $(j,i)$ | $-k$ | $(i,1)$ | $i$ | $\lvert01\rangle$ | $(-i,j)$ | $(1,j)$ | $-k$ | $j$ | $\lvert01\rangle$ |
| $(j,i)$ | $-k$ | $(i,i)$ | $-1$ | $\lvert00\rangle$ | $(-i,j)$ | $(1,k)$ | $-k$ | $k$ | $\lvert00\rangle$ |
| $(j,i)$ | $-k$ | $(i,j)$ | $k$ | $\lvert00\rangle$ | $(-i,j)$ | $(1,-1)$ | $-k$ | $-1$ | $\lvert00\rangle$ |
| $(j,i)$ | $-k$ | $(i,k)$ | $-j$ | $\lvert01\rangle$ | $(-i,j)$ | $(1,-i)$ | $-k$ | $-i$ | $\lvert01\rangle$ |
| $(j,i)$ | $-k$ | $(j,1)$ | $j$ | $\lvert01\rangle$ | $(-i,j)$ | $(-k,j)$ | $-k$ | $i$ | $\lvert01\rangle$ |
| $(j,i)$ | $-k$ | $(j,i)$ | $-k$ | $\lvert00\rangle$ | $(-i,j)$ | $(-k,k)$ | $-k$ | $1$ | $\lvert00\rangle$ |
| $(j,i)$ | $-k$ | $(j,j)$ | $-1$ | $\lvert00\rangle$ | $(-i,j)$ | $(-k,-1)$ | $-k$ | $k$ | $\lvert00\rangle$ |
| $(j,i)$ | $-k$ | $(j,k)$ | $i$ | $\lvert01\rangle$ | $(-i,j)$ | $(-k,-i)$ | $-k$ | $j$ | $\lvert01\rangle$ |
| $(j,i)$ | $-k$ | $(k,1)$ | $k$ | $\lvert00\rangle$ | $(-i,j)$ | $(j,j)$ | $-k$ | $-1$ | $\lvert00\rangle$ |
| $(j,i)$ | $-k$ | $(k,i)$ | $j$ | $\lvert01\rangle$ | $(-i,j)$ | $(j,k)$ | $-k$ | $i$ | $\lvert01\rangle$ |
| $(j,i)$ | $-k$ | $(k,j)$ | $-i$ | $\lvert01\rangle$ | $(-i,j)$ | $(j,-1)$ | $-k$ | $-j$ | $\lvert01\rangle$ |
| $(j,i)$ | $-k$ | $(k,k)$ | $-1$ | $\lvert00\rangle$ | $(-i,j)$ | $(j,-i)$ | $-k$ | $k$ | $\lvert00\rangle$ |
| $(j,j)$ | $-1$ | $(1,1)$ | $1$ | $\lvert00\rangle$ | $(-i,-i)$ | $(-i,-i)$ | $-1$ | $-1$ | $\lvert00\rangle$ |
| $(j,j)$ | $-1$ | $(1,i)$ | $i$ | $\lvert01\rangle$ | $(-i,-i)$ | $(-i,1)$ | $-1$ | $-i$ | $\lvert01\rangle$ |
| $(j,j)$ | $-1$ | $(1,j)$ | $j$ | $\lvert01\rangle$ | $(-i,-i)$ | $(-i,k)$ | $-1$ | $j$ | $\lvert01\rangle$ |
| $(j,j)$ | $-1$ | $(1,k)$ | $k$ | $\lvert00\rangle$ | $(-i,-i)$ | $(-i,-j)$ | $-1$ | $k$ | $\lvert00\rangle$ |
| $(j,j)$ | $-1$ | $(i,1)$ | $i$ | $\lvert01\rangle$ | $(-i,-i)$ | $(1,-i)$ | $-1$ | $-i$ | $\lvert01\rangle$ |
| $(j,j)$ | $-1$ | $(i,i)$ | $-1$ | $\lvert00\rangle$ | $(-i,-i)$ | $(1,1)$ | $-1$ | $1$ | $\lvert00\rangle$ |
| $(j,j)$ | $-1$ | $(i,j)$ | $k$ | $\lvert00\rangle$ | $(-i,-i)$ | $(1,k)$ | $-1$ | $k$ | $\lvert00\rangle$ |
| $(j,j)$ | $-1$ | $(i,k)$ | $-j$ | $\lvert01\rangle$ | $(-i,-i)$ | $(1,-j)$ | $-1$ | $-j$ | $\lvert01\rangle$ |
| $(j,j)$ | $-1$ | $(j,1)$ | $j$ | $\lvert01\rangle$ | $(-i,-i)$ | $(-k,-i)$ | $-1$ | $j$ | $\lvert01\rangle$ |
| $(j,j)$ | $-1$ | $(j,i)$ | $-k$ | $\lvert00\rangle$ | $(-i,-i)$ | $(-k,1)$ | $-1$ | $-k$ | $\lvert00\rangle$ |
| $(j,j)$ | $-1$ | $(j,j)$ | $-1$ | $\lvert00\rangle$ | $(-i,-i)$ | $(-k,k)$ | $-1$ | $1$ | $\lvert00\rangle$ |
| $(j,j)$ | $-1$ | $(j,k)$ | $i$ | $\lvert01\rangle$ | $(-i,-i)$ | $(-k,-j)$ | $-1$ | $-i$ | $\lvert01\rangle$ |
| $(j,j)$ | $-1$ | $(k,1)$ | $k$ | $\lvert00\rangle$ | $(-i,-i)$ | $(j,-i)$ | $-1$ | $k$ | $\lvert00\rangle$ |
| $(j,j)$ | $-1$ | $(k,i)$ | $j$ | $\lvert01\rangle$ | $(-i,-i)$ | $(j,1)$ | $-1$ | $j$ | $\lvert01\rangle$ |
| $(j,j)$ | $-1$ | $(k,j)$ | $-i$ | $\lvert01\rangle$ | $(-i,-i)$ | $(j,k)$ | $-1$ | $i$ | $\lvert01\rangle$ |
| $(j,j)$ | $-1$ | $(k,k)$ | $-1$ | $\lvert00\rangle$ | $(-i,-i)$ | $(j,-j)$ | $-1$ | $1$ | $\lvert00\rangle$ |
| $(j,k)$ | $i$ | $(1,1)$ | $1$ | $\lvert10\rangle$ | $(-i,1)$ | $(-i,1)$ | $-i$ | $-i$ | $\lvert11\rangle$ |
| $(j,k)$ | $i$ | $(1,i)$ | $i$ | $\lvert11\rangle$ | $(-i,1)$ | $(-i,i)$ | $-i$ | $1$ | $\lvert10\rangle$ |
| $(j,k)$ | $i$ | $(1,j)$ | $j$ | $\lvert11\rangle$ | $(-i,1)$ | $(-i,j)$ | $-i$ | $-k$ | $\lvert10\rangle$ |
| $(j,k)$ | $i$ | $(1,k)$ | $k$ | $\lvert10\rangle$ | $(-i,1)$ | $(-i,k)$ | $-i$ | $j$ | $\lvert11\rangle$ |
| $(j,k)$ | $i$ | $(i,1)$ | $i$ | $\lvert11\rangle$ | $(-i,1)$ | $(1,1)$ | $-i$ | $1$ | $\lvert10\rangle$ |
| $(j,k)$ | $i$ | $(i,i)$ | $-1$ | $\lvert10\rangle$ | $(-i,1)$ | $(1,i)$ | $-i$ | $i$ | $\lvert11\rangle$ |
| $(j,k)$ | $i$ | $(i,j)$ | $k$ | $\lvert10\rangle$ | $(-i,1)$ | $(1,j)$ | $-i$ | $j$ | $\lvert11\rangle$ |
| $(j,k)$ | $i$ | $(i,k)$ | $-j$ | $\lvert11\rangle$ | $(-i,1)$ | $(1,k)$ | $-i$ | $k$ | $\lvert10\rangle$ |
| $(j,k)$ | $i$ | $(j,1)$ | $j$ | $\lvert11\rangle$ | $(-i,1)$ | $(-k,1)$ | $-i$ | $-k$ | $\lvert10\rangle$ |
| $(j,k)$ | $i$ | $(j,i)$ | $-k$ | $\lvert10\rangle$ | $(-i,1)$ | $(-k,i)$ | $-i$ | $-j$ | $\lvert11\rangle$ |
| $(j,k)$ | $i$ | $(j,j)$ | $-1$ | $\lvert10\rangle$ | $(-i,1)$ | $(-k,j)$ | $-i$ | $i$ | $\lvert11\rangle$ |
| $(j,k)$ | $i$ | $(j,k)$ | $i$ | $\lvert11\rangle$ | $(-i,1)$ | $(-k,k)$ | $-i$ | $1$ | $\lvert10\rangle$ |
| $(j,k)$ | $i$ | $(k,1)$ | $k$ | $\lvert10\rangle$ | $(-i,1)$ | $(j,1)$ | $-i$ | $j$ | $\lvert11\rangle$ |
| $(j,k)$ | $i$ | $(k,i)$ | $j$ | $\lvert11\rangle$ | $(-i,1)$ | $(j,i)$ | $-i$ | $-k$ | $\lvert10\rangle$ |
| $(j,k)$ | $i$ | $(k,j)$ | $-i$ | $\lvert11\rangle$ | $(-i,1)$ | $(j,j)$ | $-i$ | $-1$ | $\lvert10\rangle$ |
| $(j,k)$ | $i$ | $(k,k)$ | $-1$ | $\lvert10\rangle$ | $(-i,1)$ | $(j,k)$ | $-i$ | $i$ | $\lvert11\rangle$ |
| $(k,1)$ | $k$ | $(1,1)$ | $1$ | $\lvert00\rangle$ | $(-1,-k)$ | $(-1,-k)$ | $k$ | $k$ | $\lvert00\rangle$ |
| $(k,1)$ | $k$ | $(1,i)$ | $i$ | $\lvert01\rangle$ | $(-1,-k)$ | $(-1,j)$ | $k$ | $-j$ | $\lvert01\rangle$ |
| $(k,1)$ | $k$ | $(1,j)$ | $j$ | $\lvert01\rangle$ | $(-1,-k)$ | $(-1,-i)$ | $k$ | $i$ | $\lvert01\rangle$ |
| $(k,1)$ | $k$ | $(1,k)$ | $k$ | $\lvert00\rangle$ | $(-1,-k)$ | $(-1,1)$ | $k$ | $-1$ | $\lvert00\rangle$ |
| $(k,1)$ | $k$ | $(i,1)$ | $i$ | $\lvert01\rangle$ | $(-1,-k)$ | $(-i,-k)$ | $k$ | $-j$ | $\lvert01\rangle$ |
| $(k,1)$ | $k$ | $(i,i)$ | $-1$ | $\lvert00\rangle$ | $(-1,-k)$ | $(-i,j)$ | $k$ | $-k$ | $\lvert00\rangle$ |
| $(k,1)$ | $k$ | $(i,j)$ | $k$ | $\lvert00\rangle$ | $(-1,-k)$ | $(-i,-i)$ | $k$ | $-1$ | $\lvert00\rangle$ |
| $(k,1)$ | $k$ | $(i,k)$ | $-j$ | $\lvert01\rangle$ | $(-1,-k)$ | $(-i,1)$ | $k$ | $-i$ | $\lvert01\rangle$ |
| $(k,1)$ | $k$ | $(j,1)$ | $j$ | $\lvert01\rangle$ | $(-1,-k)$ | $(-j,-k)$ | $k$ | $i$ | $\lvert01\rangle$ |
| $(k,1)$ | $k$ | $(j,i)$ | $-k$ | $\lvert00\rangle$ | $(-1,-k)$ | $(-j,j)$ | $k$ | $1$ | $\lvert00\rangle$ |
| $(k,1)$ | $k$ | $(j,j)$ | $-1$ | $\lvert00\rangle$ | $(-1,-k)$ | $(-j,-i)$ | $k$ | $-k$ | $\lvert00\rangle$ |
| $(k,1)$ | $k$ | $(j,k)$ | $i$ | $\lvert01\rangle$ | $(-1,-k)$ | $(-j,1)$ | $k$ | $-j$ | $\lvert01\rangle$ |
| $(k,1)$ | $k$ | $(k,1)$ | $k$ | $\lvert00\rangle$ | $(-1,-k)$ | $(-k,-k)$ | $k$ | $-1$ | $\lvert00\rangle$ |
| $(k,1)$ | $k$ | $(k,i)$ | $j$ | $\lvert01\rangle$ | $(-1,-k)$ | $(-k,j)$ | $k$ | $i$ | $\lvert01\rangle$ |
| $(k,1)$ | $k$ | $(k,j)$ | $-i$ | $\lvert01\rangle$ | $(-1,-k)$ | $(-k,-i)$ | $k$ | $j$ | $\lvert01\rangle$ |
| $(k,1)$ | $k$ | $(k,k)$ | $-1$ | $\lvert00\rangle$ | $(-1,-k)$ | $(-k,1)$ | $k$ | $-k$ | $\lvert00\rangle$ |
| $(k,i)$ | $j$ | $(1,1)$ | $1$ | $\lvert10\rangle$ | $(-1,j)$ | $(-1,j)$ | $-j$ | $-j$ | $\lvert11\rangle$ |
| $(k,i)$ | $j$ | $(1,i)$ | $i$ | $\lvert11\rangle$ | $(-1,j)$ | $(-1,k)$ | $-j$ | $-k$ | $\lvert10\rangle$ |
| $(k,i)$ | $j$ | $(1,j)$ | $j$ | $\lvert11\rangle$ | $(-1,j)$ | $(-1,-1)$ | $-j$ | $1$ | $\lvert10\rangle$ |
| $(k,i)$ | $j$ | $(1,k)$ | $k$ | $\lvert10\rangle$ | $(-1,j)$ | $(-1,-i)$ | $-j$ | $i$ | $\lvert11\rangle$ |
| $(k,i)$ | $j$ | $(i,1)$ | $i$ | $\lvert11\rangle$ | $(-1,j)$ | $(-i,j)$ | $-j$ | $-k$ | $\lvert10\rangle$ |
| $(k,i)$ | $j$ | $(i,i)$ | $-1$ | $\lvert10\rangle$ | $(-1,j)$ | $(-i,k)$ | $-j$ | $j$ | $\lvert11\rangle$ |
| $(k,i)$ | $j$ | $(i,j)$ | $k$ | $\lvert10\rangle$ | $(-1,j)$ | $(-i,-1)$ | $-j$ | $i$ | $\lvert11\rangle$ |
| $(k,i)$ | $j$ | $(i,k)$ | $-j$ | $\lvert11\rangle$ | $(-1,j)$ | $(-i,-i)$ | $-j$ | $-1$ | $\lvert10\rangle$ |
| $(k,i)$ | $j$ | $(j,1)$ | $j$ | $\lvert11\rangle$ | $(-1,j)$ | $(-j,j)$ | $-j$ | $1$ | $\lvert10\rangle$ |
| $(k,i)$ | $j$ | $(j,i)$ | $-k$ | $\lvert10\rangle$ | $(-1,j)$ | $(-j,k)$ | $-j$ | $-i$ | $\lvert11\rangle$ |
| $(k,i)$ | $j$ | $(j,j)$ | $-1$ | $\lvert10\rangle$ | $(-1,j)$ | $(-j,-1)$ | $-j$ | $j$ | $\lvert11\rangle$ |
| $(k,i)$ | $j$ | $(j,k)$ | $i$ | $\lvert11\rangle$ | $(-1,j)$ | $(-j,-i)$ | $-j$ | $-k$ | $\lvert10\rangle$ |
| $(k,i)$ | $j$ | $(k,1)$ | $k$ | $\lvert10\rangle$ | $(-1,j)$ | $(-k,j)$ | $-j$ | $i$ | $\lvert11\rangle$ |
| $(k,i)$ | $j$ | $(k,i)$ | $j$ | $\lvert11\rangle$ | $(-1,j)$ | $(-k,k)$ | $-j$ | $1$ | $\lvert10\rangle$ |
| $(k,i)$ | $j$ | $(k,j)$ | $-i$ | $\lvert11\rangle$ | $(-1,j)$ | $(-k,-1)$ | $-j$ | $k$ | $\lvert10\rangle$ |
| $(k,i)$ | $j$ | $(k,k)$ | $-1$ | $\lvert10\rangle$ | $(-1,j)$ | $(-k,-i)$ | $-j$ | $j$ | $\lvert11\rangle$ |
| $(k,j)$ | $-i$ | $(1,1)$ | $1$ | $\lvert10\rangle$ | $(-1,-i)$ | $(-1,-i)$ | $i$ | $i$ | $\lvert11\rangle$ |
| $(k,j)$ | $-i$ | $(1,i)$ | $i$ | $\lvert11\rangle$ | $(-1,-i)$ | $(-1,1)$ | $i$ | $-1$ | $\lvert10\rangle$ |
| $(k,j)$ | $-i$ | $(1,j)$ | $j$ | $\lvert11\rangle$ | $(-1,-i)$ | $(-1,k)$ | $i$ | $-k$ | $\lvert10\rangle$ |
| $(k,j)$ | $-i$ | $(1,k)$ | $k$ | $\lvert10\rangle$ | $(-1,-i)$ | $(-1,-j)$ | $i$ | $j$ | $\lvert11\rangle$ |
| $(k,j)$ | $-i$ | $(i,1)$ | $i$ | $\lvert11\rangle$ | $(-1,-i)$ | $(-i,-i)$ | $i$ | $-1$ | $\lvert10\rangle$ |
| $(k,j)$ | $-i$ | $(i,i)$ | $-1$ | $\lvert10\rangle$ | $(-1,-i)$ | $(-i,1)$ | $i$ | $-i$ | $\lvert11\rangle$ |
| $(k,j)$ | $-i$ | $(i,j)$ | $k$ | $\lvert10\rangle$ | $(-1,-i)$ | $(-i,k)$ | $i$ | $j$ | $\lvert11\rangle$ |
| $(k,j)$ | $-i$ | $(i,k)$ | $-j$ | $\lvert11\rangle$ | $(-1,-i)$ | $(-i,-j)$ | $i$ | $k$ | $\lvert10\rangle$ |
| $(k,j)$ | $-i$ | $(j,1)$ | $j$ | $\lvert11\rangle$ | $(-1,-i)$ | $(-j,-i)$ | $i$ | $-k$ | $\lvert10\rangle$ |
| $(k,j)$ | $-i$ | $(j,i)$ | $-k$ | $\lvert10\rangle$ | $(-1,-i)$ | $(-j,1)$ | $i$ | $-j$ | $\lvert11\rangle$ |
| $(k,j)$ | $-i$ | $(j,j)$ | $-1$ | $\lvert10\rangle$ | $(-1,-i)$ | $(-j,k)$ | $i$ | $-i$ | $\lvert11\rangle$ |
| $(k,j)$ | $-i$ | $(j,k)$ | $i$ | $\lvert11\rangle$ | $(-1,-i)$ | $(-j,-j)$ | $i$ | $-1$ | $\lvert10\rangle$ |
| $(k,j)$ | $-i$ | $(k,1)$ | $k$ | $\lvert10\rangle$ | $(-1,-i)$ | $(-k,-i)$ | $i$ | $j$ | $\lvert11\rangle$ |
| $(k,j)$ | $-i$ | $(k,i)$ | $j$ | $\lvert11\rangle$ | $(-1,-i)$ | $(-k,1)$ | $i$ | $-k$ | $\lvert10\rangle$ |
| $(k,j)$ | $-i$ | $(k,j)$ | $-i$ | $\lvert11\rangle$ | $(-1,-i)$ | $(-k,k)$ | $i$ | $1$ | $\lvert10\rangle$ |
| $(k,j)$ | $-i$ | $(k,k)$ | $-1$ | $\lvert10\rangle$ | $(-1,-i)$ | $(-k,-j)$ | $i$ | $-i$ | $\lvert11\rangle$ |
| $(k,k)$ | $-1$ | $(1,1)$ | $1$ | $\lvert00\rangle$ | $(-1,1)$ | $(-1,1)$ | $-1$ | $-1$ | $\lvert00\rangle$ |
| $(k,k)$ | $-1$ | $(1,i)$ | $i$ | $\lvert01\rangle$ | $(-1,1)$ | $(-1,i)$ | $-1$ | $-i$ | $\lvert01\rangle$ |
| $(k,k)$ | $-1$ | $(1,j)$ | $j$ | $\lvert01\rangle$ | $(-1,1)$ | $(-1,j)$ | $-1$ | $-j$ | $\lvert01\rangle$ |
| $(k,k)$ | $-1$ | $(1,k)$ | $k$ | $\lvert00\rangle$ | $(-1,1)$ | $(-1,k)$ | $-1$ | $-k$ | $\lvert00\rangle$ |
| $(k,k)$ | $-1$ | $(i,1)$ | $i$ | $\lvert01\rangle$ | $(-1,1)$ | $(-i,1)$ | $-1$ | $-i$ | $\lvert01\rangle$ |
| $(k,k)$ | $-1$ | $(i,i)$ | $-1$ | $\lvert00\rangle$ | $(-1,1)$ | $(-i,i)$ | $-1$ | $1$ | $\lvert00\rangle$ |
| $(k,k)$ | $-1$ | $(i,j)$ | $k$ | $\lvert00\rangle$ | $(-1,1)$ | $(-i,j)$ | $-1$ | $-k$ | $\lvert00\rangle$ |
| $(k,k)$ | $-1$ | $(i,k)$ | $-j$ | $\lvert01\rangle$ | $(-1,1)$ | $(-i,k)$ | $-1$ | $j$ | $\lvert01\rangle$ |
| $(k,k)$ | $-1$ | $(j,1)$ | $j$ | $\lvert01\rangle$ | $(-1,1)$ | $(-j,1)$ | $-1$ | $-j$ | $\lvert01\rangle$ |
| $(k,k)$ | $-1$ | $(j,i)$ | $-k$ | $\lvert00\rangle$ | $(-1,1)$ | $(-j,i)$ | $-1$ | $k$ | $\lvert00\rangle$ |
| $(k,k)$ | $-1$ | $(j,j)$ | $-1$ | $\lvert00\rangle$ | $(-1,1)$ | $(-j,j)$ | $-1$ | $1$ | $\lvert00\rangle$ |
| $(k,k)$ | $-1$ | $(j,k)$ | $i$ | $\lvert01\rangle$ | $(-1,1)$ | $(-j,k)$ | $-1$ | $-i$ | $\lvert01\rangle$ |
| $(k,k)$ | $-1$ | $(k,1)$ | $k$ | $\lvert00\rangle$ | $(-1,1)$ | $(-k,1)$ | $-1$ | $-k$ | $\lvert00\rangle$ |
| $(k,k)$ | $-1$ | $(k,i)$ | $j$ | $\lvert01\rangle$ | $(-1,1)$ | $(-k,i)$ | $-1$ | $-j$ | $\lvert01\rangle$ |
| $(k,k)$ | $-1$ | $(k,j)$ | $-i$ | $\lvert01\rangle$ | $(-1,1)$ | $(-k,j)$ | $-1$ | $i$ | $\lvert01\rangle$ |
| $(k,k)$ | $-1$ | $(k,k)$ | $-1$ | $\lvert00\rangle$ | $(-1,1)$ | $(-k,k)$ | $-1$ | $1$ | $\lvert00\rangle$ |
