
```quiz
type: blank
id: m4-2lec-q1
require_exact: true
content: |-
  **Question 1**

  A simple pendulum has length $0.35\ \mathrm{m}$ and bob mass $0.026\ \mathrm{kg}$. It is released from rest at an angle of $14^\circ$. Using the small-angle approximation, what is its frequency of oscillation?

  ![](<Images/simple-pendulum.png>)

  Enter the frequency in hertz as a number only: ==0.84==
feedback: |-
  For a simple pendulum at small angle,

  $$
  f=\frac{1}{2\pi}\sqrt{\frac{g}{L}}.
  $$

  Therefore,

  $$
  f=\frac{1}{2\pi}\sqrt{\frac{9.81\ \mathrm{m/s^2}}{0.35\ \mathrm{m}}}
  =0.8426\ldots\ \mathrm{Hz}.
  $$

  The measured length has two significant figures, so $f=0.84\ \mathrm{Hz}$. The bob's mass does not affect the frequency.
```

---

```quiz
type: blank
id: m4-2lec-q2
require_exact: true
content: |-
  **Question 2**

  A uniform rod of mass $m$ and length $L$ swings about a pivot at one end. Find its small-angle oscillation period for $L=0.92\ \mathrm{m}$ and $m=0.037\ \mathrm{kg}$.

  ![](<Images/uniform-rod-end-pivot.png>)

  Enter the period in seconds as a number only: ==1.6==
feedback: |-
  For a physical pendulum,

  $$
  T=2\pi\sqrt{\frac{I}{mgd}}.
  $$

  A uniform rod pivoted at one end has $I=\frac13mL^2$ and $d=L/2$, so

  $$
  T=2\pi\sqrt{\frac{2L}{3g}}
  =2\pi\sqrt{\frac{2(0.92\ \mathrm{m})}{3(9.81\ \mathrm{m/s^2})}}
  =1.5711\ldots\ \mathrm{s}.
  $$

  The measured length has two significant figures, so $T=1.6\ \mathrm{s}$. The rod's mass cancels.
```

---

```quiz
type: blank
id: m4-2lec-q3
require_exact: true
content: |-
  **Question 3**

  A uniform rod of mass $m$ and length $L$ pivots about a point $L/6$ below its upper end. Find its small-angle oscillation period for $L=0.75\ \mathrm{m}$ and $m=0.56\ \mathrm{kg}$.

  ![](<Images/uniform-rod-offset-pivot.png>)

  Enter the period in seconds as a number only: ==1.3==
feedback: |-
  The pivot lies a distance

  $$
  d=\frac{L}{2}-\frac{L}{6}=\frac{L}{3}
  $$

  from the rod's center of mass. By the parallel-axis theorem,

  $$
  I_p=\frac{1}{12}mL^2+m\left(\frac{L}{3}\right)^2
  =\frac{7}{36}mL^2.
  $$

  Therefore,

  $$
  T=2\pi\sqrt{\frac{I_p}{mgd}}
  =2\pi\sqrt{\frac{7L}{12g}}
  =1.3269\ldots\ \mathrm{s}.
  $$

  The measured length has two significant figures, so $T=1.3\ \mathrm{s}$. The rod's mass cancels.
```

---

```quiz
type: blank
id: m4-2lec-q4
require_exact: true
content: |-
  **Question 4**

  A physical pendulum consists of a uniform rod of mass $m_r$ and length $L$, with a point mass $m_p$ attached at its lower end. Find the small-angle period for $m_r=0.35\ \mathrm{kg}$, $m_p=0.25\ \mathrm{kg}$, and $L=1.2\ \mathrm{m}$.

  ![](<Images/rod-point-mass-pendulum.png>)

  Enter the period in seconds as a number only: ==2.0==
feedback: |-
  The total moment of inertia about the pivot is

  $$
  I=\frac13m_rL^2+m_pL^2.
  $$

  The gravitational torque factor is $g[m_r(L/2)+m_pL]$, so

  $$
  T=2\pi\sqrt{\frac{\frac13m_rL^2+m_pL^2}{g[m_r(L/2)+m_pL]}}
  =2.0412\ldots\ \mathrm{s}.
  $$

  The measured givens have two significant figures, so $T=2.0\ \mathrm{s}$.
```

---

```quiz
type: blank
id: m4-2lec-q5
require_exact: true
content: |-
  **Question 5**

  A physical pendulum consists of a uniform rod of mass $m_r$ and length $L$, with a solid disk of mass $m_d$ and radius $r$ attached at the rod's lower end. Find the small-angle period for $m_r=0.35\ \mathrm{kg}$, $m_d=0.65\ \mathrm{kg}$, $r=0.42\ \mathrm{m}$, and $L=1.2\ \mathrm{m}$.

  ![](<Images/rod-disk-pendulum.png>)

  Enter the period in seconds as a number only: ==2.5==
feedback: |-
  The disk's center is a distance $L+r$ from the pivot. The total moment of inertia is

  $$
  I=\frac13m_rL^2+\frac12m_dr^2+m_d(L+r)^2.
  $$

  The gravitational torque factor is $g[m_r(L/2)+m_d(L+r)]$, so

  $$
  T=2\pi\sqrt{\frac{\frac13m_rL^2+\frac12m_dr^2+m_d(L+r)^2}{g[m_r(L/2)+m_d(L+r)]}}
  =2.4806\ldots\ \mathrm{s}.
  $$

  The measured givens have two significant figures, so $T=2.5\ \mathrm{s}$.
```
