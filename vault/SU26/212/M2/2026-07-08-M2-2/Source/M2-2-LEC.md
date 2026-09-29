
```quiz
type: blank
id: m2-2lec-q1
require_exact: true
content: |-
  **Question 1**

  A rod of mass $m$ and length $l$ has linear mass density $\lambda(x)=cx$. Find the center-of-mass position measured from the origin for $m=0.65\ \mathrm{kg}$ and $l=1.8\ \mathrm{m}$.

  ![](<Images/rod-with-linearly-increasing-density.png>)

  Enter the position in meters as a number only: ==1.2==
feedback: |-
  The center of mass is

  $$
  x_{\mathrm{cm}}
  =\frac{\int_0^l x\lambda(x)\,dx}{\int_0^l\lambda(x)\,dx}
  =\frac{cl^3/3}{cl^2/2}
  =\frac{2l}{3}.
  $$

  Thus,

  $$
  x_{\mathrm{cm}}=\frac{2(1.8\ \mathrm{m})}{3}=1.2\ \mathrm{m}.
  $$

  The mass cancels, and the measured length supports two significant figures.
```

---

```quiz
type: blank
id: m2-2lec-q2
require_exact: true
content: |-
  **Question 2**

  The same rod has mass $m=0.65\ \mathrm{kg}$, length $l=1.8\ \mathrm{m}$, and density $\lambda(x)=cx$. Find its moment of inertia about the origin.

  ![](<Images/rod-with-linearly-increasing-density.png>)

  Enter the moment of inertia in kilogram square meters as a number only: ==1.1==
feedback: |-
  First use the total mass to eliminate $c$:

  $$
  m=\int_0^l cx\,dx=\frac{cl^2}{2},
  \qquad
  c=\frac{2m}{l^2}.
  $$

  Then

  $$
  I=\int_0^l x^2\lambda(x)\,dx
  =\int_0^l cx^3\,dx
  =\frac{cl^4}{4}
  =\frac12ml^2.
  $$

  Substitution gives

  $$
  I=\frac12(0.65\ \mathrm{kg})(1.8\ \mathrm{m})^2
  =1.053\ \mathrm{kg\,m^2}.
  $$

  The measured givens have two significant figures, so $I=1.1\ \mathrm{kg\,m^2}$.
```

---

```quiz
type: blank
id: m2-2lec-q3
require_exact: true
content: |-
  **Question 3**

  A uniform thin rod of mass $m$ and length $L$ rotates about a point located $L/3$ from its left end. Find its moment of inertia in terms of $mL^2$.

  Enter the coefficient multiplying $mL^2$ using ordinary keyboard notation: ==1/9==
feedback: |-
  The rod's center is at $L/2$, so the pivot is a distance

  $$
  d=\frac{L}{2}-\frac{L}{3}=\frac{L}{6}
  $$

  from the center. By the parallel-axis theorem,

  $$
  I=I_{\mathrm{cm}}+md^2
  =\frac{1}{12}mL^2+m\left(\frac{L}{6}\right)^2
  =\frac19mL^2.
  $$
```
