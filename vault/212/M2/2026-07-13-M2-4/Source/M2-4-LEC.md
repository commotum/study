
```quiz
type: blank
id: m2-4lec-q1
require_exact: true
content: |-
  **Question 1**

  A uniform board of mass $M$ and length $L$ rests on supports A and B. Support A is $L/5$ from the board's left end, and support B is $2L/3$ from the left end. A box of mass $m$ is placed a distance $x$ to the right of support B.

  Find the distance $x$ at which the board is just about to tip. Use $M=2.4\ \mathrm{kg}$, $L=1.4\ \mathrm{m}$, and $m=1.6\ \mathrm{kg}$.

  ![](<Images/uniform-board-tipping.png>)

  Enter the distance in meters as a number only: ==0.35==
feedback: |-
  At the tipping point, the board pivots about support B and the force from support A is zero. The board's center of mass is $L/2$ from the left end, so its lever arm about B is

  $$
  \frac{2L}{3}-\frac{L}{2}=\frac{L}{6}.
  $$

  Torque balance about B gives

  $$
  mgx=Mg\frac{L}{6},
  \qquad
  x=\frac{ML}{6m}.
  $$

  Therefore,

  $$
  x=\frac{(2.4\ \mathrm{kg})(1.4\ \mathrm{m})}{6(1.6\ \mathrm{kg})}
  =0.35\ \mathrm{m}.
  $$

  The measured givens have two significant figures.
```

---

```quiz
type: blank
id: m2-4lec-q2
require_exact: true
content: |-
  **Question 2**

  A uniform ladder of mass $m$ and length $L$ leans against a frictionless wall at an angle $\theta$. Find the minimum coefficient of static friction between the ladder and the ground that prevents slipping.

  Use $m=4.5\ \mathrm{kg}$, $L=2.8\ \mathrm{m}$, and $\theta=52^\circ$.

  ![](<Images/ladder-against-frictionless-wall.png>)

  Enter the coefficient as a number only: ==0.39==
feedback: |-
  Taking torques about the ladder's bottom gives

  $$
  N_wL\sin\theta=mg\frac{L}{2}\cos\theta,
  \qquad
  N_w=\frac{mg}{2}\cot\theta.
  $$

  Horizontal equilibrium requires $f_s=N_w$, while vertical equilibrium gives $N_g=mg$. At impending slip,

  $$
  \mu_s=\frac{f_s}{N_g}=\frac12\cot\theta.
  $$

  Thus,

  $$
  \mu_s=\frac12\cot(52^\circ)=0.39064\ldots\approx0.39.
  $$

  The mass and length cancel, and the angle supports two significant figures.
```

---

```quiz
type: blank
id: m2-4lec-q3
require_exact: true
content: |-
  **Question 3**

  Block 1 of mass $m_1$ and block 2 of mass $m_2$ are connected by a massless string over a frictionless uniform-disk pulley of mass $m_p$ and radius $r$. Find the system's acceleration for $m_1=1.2\ \mathrm{kg}$, $m_2=2.6\ \mathrm{kg}$, $m_p=3.3\ \mathrm{kg}$, and $r=0.56\ \mathrm{m}$.

  ![](<Images/massive-pulley-atwood-machine.png>)

  Enter the acceleration magnitude in meters per second squared as a number only: ==2.5==
feedback: |-
  The block equations and pulley torque equation combine to give

  $$
  a=\frac{(m_2-m_1)g}{m_1+m_2+I/r^2}.
  $$

  For a uniform-disk pulley, $I=\frac12m_pr^2$, so

  $$
  a=\frac{(m_2-m_1)g}{m_1+m_2+\frac12m_p}.
  $$

  Substitution gives

  $$
  a=\frac{(2.6-1.2)(9.81)}{1.2+2.6+\frac12(3.3)}
  =2.519\ldots\ \mathrm{m/s^2}.
  $$

  The measured givens have two significant figures, so $a=2.5\ \mathrm{m/s^2}$. Block 2 accelerates downward while block 1 accelerates upward.
```
