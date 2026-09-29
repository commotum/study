
```quiz
type: blank
id: m3-1lec-q1
require_exact: true
content: |-
  **Question 1**

  A satellite is in a circular orbit at an altitude equal to one-third of Earth's radius $r_E$. What is the satellite's gravitational acceleration $g_h$ in units of the surface acceleration $g$?

  Enter $g_h/g$ using two significant figures: ==0.56==
feedback: |-
  The orbital radius measured from Earth's center is

  $$
  r=r_E+\frac13r_E=\frac43r_E.
  $$

  Since gravitational acceleration varies as $1/r^2$,

  $$
  \frac{g_h}{g}
  =\left(\frac{r_E}{r}\right)^2
  =\left(\frac34\right)^2
  =0.5625.
  $$

  To two significant figures, $g_h/g=0.56$.
```

---

```quiz
type: blank
id: m3-1lec-q2
require_exact: true
content: |-
  **Question 2**

  Find the altitude of a geostationary satellite. Use $G=6.67\times10^{-11}\ \mathrm{N\,m^2/kg^2}$, $M_E=5.97\times10^{24}\ \mathrm{kg}$, $r_E=6.38\times10^6\ \mathrm{m}$, and a $24\ \mathrm{h}$ orbital period.

  Enter the altitude in kilometers as a number only: ==35800==
feedback: |-
  For a circular orbit,

  $$
  T^2=\frac{4\pi^2r^3}{GM_E},
  \qquad
  r=\left(\frac{GM_ET^2}{4\pi^2}\right)^{1/3}.
  $$

  With $T=86400\ \mathrm{s}$,

  $$
  r=4.2227\times10^7\ \mathrm{m}.
  $$

  Subtracting Earth's radius gives

  $$
  h=r-r_E
  =3.5847\times10^7\ \mathrm{m}
  =3.5847\times10^4\ \mathrm{km}.
  $$

  The supplied constants support three significant figures, so $h=3.58\times10^4\ \mathrm{km}$, entered as `35800`.
```

---

```quiz
type: blank
id: m3-1lec-q3
require_exact: true
content: |-
  **Question 3**

  A hypothetical planet takes $8.0$ Earth years to complete one orbit around the Sun. How far is it from the Sun?

  Enter the orbital distance in astronomical units as a number only: ==4.0==
feedback: |-
  Relative to Earth's orbit, Kepler's third law is

  $$
  T^2=a^3,
  $$

  with $T$ in Earth years and $a$ in astronomical units. Therefore,

  $$
  a=T^{2/3}=(8.0)^{2/3}=4.0\ \mathrm{AU}.
  $$

  The period is given with two significant figures, so the distance is $4.0\ \mathrm{AU}$.
```
