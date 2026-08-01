
```quiz
type: blank
id: m5-2lec-q1
require_exact: true
content: |-
  **Question 1**

  A block of mass $M$ hangs from a wire over a pulley. The wire segment between the wall and pulley has length $L$ and mass $m_w$. Find the speed at which a transverse wave propagates along the wire. Assume the hanging block is stationary, so the wire tension is $T=Mg$.

  Use $M=0.82\ \mathrm{kg}$, $m_w=0.018\ \mathrm{kg}$, $L=1.4\ \mathrm{m}$, and $g=9.8\ \mathrm{m/s^2}$.

  ![](<Images/wire-pulley-hanging-mass.png>)

  Enter the wave speed in meters per second as a number only: ==25==
feedback: |-
  The wire's linear mass density is

  $$
  \mu=\frac{m_w}{L}.
  $$

  Because the block is stationary, $T=Mg$. Therefore,

  $$
  v=\sqrt{\frac{T}{\mu}}
  =\sqrt{\frac{MgL}{m_w}}
  =\sqrt{\frac{(0.82)(9.8)(1.4)}{0.018}}
  =24.999\ldots\ \mathrm{m/s}.
  $$

  The measured givens have two significant figures, so $v=25\ \mathrm{m/s}$.
```

---

```quiz
type: blank
id: m5-2lec-q2
require_exact: true
content: |-
  **Question 2**

  A block of mass $M$ hangs from a wire over a pulley. The wire segment between the wall and pulley has length $L$ and mass $m_w$. A sinusoidal wave with amplitude $A$ and wavelength $\lambda$ propagates along the wire. Find the maximum transverse speed of a particle in the wire. Disregard reflections.

  Use $M=0.75\ \mathrm{kg}$, $m_w=0.015\ \mathrm{kg}$, $A=0.85\ \mathrm{cm}$, $\lambda=0.65\ \mathrm{cm}$, $L=1.2\ \mathrm{m}$, and $g=9.81\ \mathrm{m/s^2}$.

  ![](<Images/wire-pulley-hanging-mass.png>)

  Enter the maximum particle speed in meters per second as a number only: ==200==
feedback: |-
  First find the wave speed:

  $$
  v_{\mathrm{wave}}
  =\sqrt{\frac{MgL}{m_w}}
  =\sqrt{\frac{(0.75)(9.81)(1.2)}{0.015}}
  =24.261\ldots\ \mathrm{m/s}.
  $$

  For a sinusoidal wave, the maximum transverse particle speed is

  $$
  v_{\mathrm{particle,max}}
  =A\omega
  =\frac{2\pi A}{\lambda}v_{\mathrm{wave}}.
  $$

  With $A=0.0085\ \mathrm{m}$ and $\lambda=0.0065\ \mathrm{m}$,

  $$
  v_{\mathrm{particle,max}}
  =\frac{2\pi(0.0085)}{0.0065}(24.261\ldots)
  =199.3\ldots\ \mathrm{m/s}.
  $$

  The measured givens have two significant figures, so $v_{\mathrm{particle,max}}=2.0\times10^2\ \mathrm{m/s}$, entered as `200`.
```

---

```quiz
type: blank
id: m5-2lec-q3
require_exact: true
content: |-
  **Question 3**

  A sound source lies somewhere on the $x$-axis. Listeners at $x=-7.0\ \mathrm{m}$ and $x=+3.0\ \mathrm{m}$ detect the same wavefront simultaneously. A third listener on the positive $y$-axis also detects that wavefront at the same time. What is her $y$-coordinate?

  Enter the coordinate in meters as a number only: ==4.6==
feedback: |-
  The source is equidistant from the two listeners on the $x$-axis, so it lies at their midpoint:

  $$
  x_s=\frac{-7.0+3.0}{2}=-2.0\ \mathrm{m}.
  $$

  The wavefront radius is $5.0\ \mathrm{m}$. The third listener is at $(0,y)$, so

  $$
  (2.0\ \mathrm{m})^2+y^2=(5.0\ \mathrm{m})^2.
  $$

  Therefore,

  $$
  y=\sqrt{21}\ \mathrm{m}=4.5825\ldots\ \mathrm{m}.
  $$

  The measured positions have two significant figures, so $y=4.6\ \mathrm{m}$.
```

---

```quiz
type: radio
id: m5-2lec-q4
content: |-
  **Question 4**

  A snapshot shows the same-frequency wave traveling through media $A$, $B$, and $C$. The wavelength is shortest in medium $B$ and longest in medium $C$. Which medium has the largest index of refraction? Explain your reasoning.
options:
- id: a
  content: Medium $A$
  feedback: Medium $A$ has an intermediate wavelength, so its index is smaller than $n_B$ and larger than $n_C$.
- id: b
  content: Medium $B$
  correct: true
  feedback: Frequency remains constant across the boundaries. Since $v=f\lambda$ and $n=c/v$, the shortest wavelength corresponds to the smallest wave speed and largest index of refraction. Therefore, $n_B>n_A>n_C$.
- id: c
  content: Medium $C$
  feedback: Medium $C$ has the longest wavelength, so it has the greatest wave speed and the smallest index of refraction.
```

---

```quiz
type: blank
id: m5-2lec-q5
require_exact: true
content: |-
  **Question 5**

  Orange light with wavelength $650\ \mathrm{nm}$ travels through air and strikes a $1.2\ \mathrm{mm}$-thick glass slide perpendicular to its surface. The glass has index of refraction $n=1.5$. How many wavelengths of the light fit inside the glass slide?

  Enter the number of wavelengths as a number only: ==2800==
feedback: |-
  The light's frequency remains constant as it enters the glass, so

  $$
  \lambda_{\mathrm{glass}}
  =\frac{\lambda_{\mathrm{air}}}{n}
  =\frac{650\ \mathrm{nm}}{1.5}
  =433.3\ldots\ \mathrm{nm}.
  $$

  Convert the slide thickness:

  $$
  1.2\ \mathrm{mm}=1.2\times10^6\ \mathrm{nm}.
  $$

  The number of wavelengths is

  $$
  N=\frac{1.2\times10^6}{433.3\ldots}
  =2769.2\ldots.
  $$

  The measured givens have two significant figures, so $N=2.8\times10^3$ wavelengths, entered as `2800`.
```
