
```quiz
type: blank
id: m2-1lec-q1
require_exact: true
content: |-
  **Question 1**

  The two blocks balance in stable equilibrium. Find their center of mass relative to the position of $m_1$, where $m_1=3m_2$. Neglect the mass of the $0.88\ \mathrm{m}$ rod.

  ![](<Images/two-mass-balance.png>)

  Enter the center-of-mass position in meters as a number only: ==0.22==
feedback: |-
  Place $m_1$ at $x_1=0$ and $m_2$ at $x_2=0.88\ \mathrm{m}$:

  $$
  x_{\mathrm{cm}}
  =\frac{m_1x_1+m_2x_2}{m_1+m_2}
  =\frac{(3m_2)(0)+m_2(0.88\ \mathrm{m})}{3m_2+m_2}
  =0.22\ \mathrm{m}.
  $$
```

---

```quiz
type: blank
id: m2-1lec-q2
require_exact: true
content: |-
  **Question 2**

  The blocks in the diagram are identical, have uniform density, and each have mass $M$. Find the $x$-coordinate of the system's center of mass relative to the origin. Enter your answer in centimeters.

  ![](<Images/identical-block-arrangement.png>)

  Enter the $x$-coordinate in centimeters as a number only: ==3.06==
feedback: |-
  Because the nine blocks have equal mass, average the $x$-coordinates of their centers. The six bottom centers are at

  $$
  0.5,\ 1.5,\ 2.5,\ 3.5,\ 4.5,\ 5.5\ \mathrm{cm},
  $$

  and the three top centers are at

  $$
  1.5,\ 2.5,\ 5.5\ \mathrm{cm}.
  $$

  Thus,

  $$
  x_{\mathrm{cm}}=\frac{27.5}{9}\ \mathrm{cm}=3.06\ \mathrm{cm}.
  $$
```

---

```quiz
type: blank
id: m2-1lec-q3
require_exact: true
content: |-
  **Question 3**

  The cubic blocks shown have constant density $\rho$. Find the center of mass $x_{\mathrm{cm}}$ relative to the origin at the left edge of the large block. Use $\rho=1.5\ \mathrm{kg/m^3}$ and $L=0.75\ \mathrm{m}$, and enter your answer in meters.

  ![](<Images/composite-cubes.png>)

  Enter the center-of-mass position in meters as a number only: ==0.88==
feedback: |-
  The large cube has mass $m_1=\rho(2L)^3=8\rho L^3$ and center $x_1=L$. The small cube has mass $m_2=\rho L^3$ and center $x_2=2L+L/2=5L/2$. Therefore,

  $$
  x_{\mathrm{cm}}
  =\frac{m_1x_1+m_2x_2}{m_1+m_2}
  =\frac{(8\rho L^3)L+(\rho L^3)(5L/2)}{9\rho L^3}
  =\frac{7L}{6}.
  $$

  With $L=0.75\ \mathrm{m}$,

  $$
  x_{\mathrm{cm}}=\frac76(0.75\ \mathrm{m})=0.875\ \mathrm{m}.
  $$

  The measured length has two significant figures, so $x_{\mathrm{cm}}=0.88\ \mathrm{m}$.
```

---

```quiz
type: radio
id: m2-1lec-q4
content: |-
  **Question 4**

  For the same constant-density cubic blocks, where should the center of mass $x_{\mathrm{cm}}$ lie relative to the origin at the left edge of the large block?

  ![](<Images/composite-cubes.png>)
options:
- id: a
  content: |-
    $x_{\mathrm{cm}}<L$
- id: b
  content: |-
    $x_{\mathrm{cm}}=L$
- id: c
  content: |-
    $L<x_{\mathrm{cm}}<2L$
  correct: true
  feedback: |-
    The large cube alone has its center of mass at $x=L$. Adding the smaller cube on the right shifts the combined center of mass to the right of $L$, but the much larger mass of the large cube keeps it to the left of $2L$.
- id: d
  content: |-
    $x_{\mathrm{cm}}=2L$
- id: e
  content: |-
    $2L<x_{\mathrm{cm}}<3L$
```

---

```quiz
type: blank
id: m2-1lec-q5
require_exact: true
content: |-
  **Question 5**

  A rod of mass $m$ and length $l$ has linear mass density $\lambda(x)=cx$. Find $c$ when $m=0.65\ \mathrm{kg}$ and $l=1.8\ \mathrm{m}$. Enter your answer in $\mathrm{kg/m^2}$.

  ![](<Images/rod-with-linearly-increasing-density.png>)

  Enter $c$ in $\mathrm{kg/m^2}$ as a number only: ==0.40==
feedback: |-
  Integrate the density over the rod to obtain its total mass:

  $$
  m=\int_0^l\lambda(x)\,dx
  =\int_0^l cx\,dx
  =\frac{cl^2}{2}.
  $$

  Hence,

  $$
  c=\frac{2m}{l^2}
  =\frac{2(0.65\ \mathrm{kg})}{(1.8\ \mathrm{m})^2}
  \approx0.40\ \mathrm{kg/m^2}.
  $$
```
