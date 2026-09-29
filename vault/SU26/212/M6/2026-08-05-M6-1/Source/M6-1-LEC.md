
```quiz
type: radio
id: m6-1lec-q1
shuffle: true
content: |-
  **Question 1**

  A laboratory experiment produces a double-slit interference pattern on a screen. If the screen is moved farther away from the slits, the fringes will be _____.

  ![](<Images/double-slit-fringe-spacing-pattern.png>)
options:
- id: a
  content: |-
    Closer together
  feedback: |-
    The fringe angles are fixed by the slit spacing and wavelength, but the screen position is $y=L\tan\theta$. Increasing $L$ makes the same angular separation span a larger distance, so the fringes do not move closer together.
- id: b
  content: |-
    In the same positions
  feedback: |-
    The fringe orders remain at the same angles, not the same screen coordinates. Because $y=L\tan\theta$, increasing the screen distance $L$ moves each noncentral fringe farther from the center.
- id: c
  content: |-
    Farther apart
  correct: true
  feedback: |-
    Double-slit fringe spacing is approximately $\Delta y=\lambda L/d$. With wavelength and slit separation fixed, increasing the screen distance $L$ increases $\Delta y$, so the fringes are farther apart.
```

---

```quiz
type: radio
id: m6-1lec-q2
shuffle: true
content: |-
  **Question 2**

  A laboratory experiment produces a double-slit interference pattern on a screen. The marked point is how much farther from the left slit than from the right slit?

  ![](<Images/double-slit-second-order-bright-fringe-dot.png>)
options:
- id: a
  content: |-
    $0.5\lambda$
  feedback: |-
    A path difference of $0.5\lambda$ produces the first dark fringe. The marked point lies on a bright fringe, so its path difference must be an integer multiple of $\lambda$.
- id: b
  content: |-
    $1.0\lambda$
  feedback: |-
    A path difference of $1.0\lambda$ identifies the first-order bright fringe. The marked point is on the second bright fringe from the central maximum.
- id: c
  content: |-
    $1.5\lambda$
  feedback: |-
    A path difference of $1.5\lambda$ produces the second dark fringe. The dot is centered on a bright band rather than a dark band.
- id: d
  content: |-
    $2.0\lambda$
  correct: true
  feedback: |-
    Bright fringes satisfy $\Delta r=m\lambda$. The dot marks the second-order bright fringe, so $m=2$ and the path from the left slit is $2.0\lambda$ longer than the path from the right slit.
- id: e
  content: |-
    $2.5\lambda$
  feedback: |-
    A half-integer path difference produces destructive interference. Thus $2.5\lambda$ corresponds to the third dark fringe, not the marked bright fringe.
- id: f
  content: |-
    $3.0\lambda$
  feedback: |-
    A path difference of $3.0\lambda$ identifies the third-order bright fringe. The marked point is one bright band closer to the central maximum, at second order.
```

---

```quiz
type: blank
id: m6-1lec-q3
require_exact: true
content: |-
  **Question 3**

  A laser incident on a double slit produces a pattern on a screen. The graph shows the intensity as a function of $x$ in centimeters. The distance between the slit centers is $0.062\ \mathrm{mm}$, and the slits are $0.85\ \mathrm{m}$ from the screen.

  ![](<Images/double-slit-intensity-position-graph.png>)

  What is the wavelength of the laser? Enter the wavelength in nanometers as a number only: ==730==
feedback: |-
  Adjacent central intensity peaks are separated by $\Delta y=1.0\ \mathrm{cm}$. For small-angle double-slit interference,

  $$
  \lambda
  =\frac{\Delta y\,d}{L}
  =\frac{(1.0\times10^{-2}\ \mathrm{m})(6.2\times10^{-5}\ \mathrm{m})}{0.85\ \mathrm{m}}
  =7.294\ldots\times10^{-7}\ \mathrm{m}.
  $$

  The measured values support two significant figures, so $\lambda=7.3\times10^2\ \mathrm{nm}$, entered as `730`.
```

---

```quiz
type: blank
id: m6-1lec-q4
require_exact: true
content: |-
  **Question 4**

  A laser illuminates a diffraction grating, producing a pattern on a screen $1.8\ \mathrm{m}$ away. The center of the third bright fringe is $120\ \mathrm{cm}$ above the central maximum. The spacing between the grating lines is $3.0\ \mu\mathrm{m}$.

  What is the wavelength of the laser? Enter the wavelength in nanometers as a number only: ==550==
feedback: |-
  The angle is not small, so first use the screen geometry:

  $$
  \theta_3
  =\tan^{-1}\left(\frac{1.20\ \mathrm{m}}{1.8\ \mathrm{m}}\right)
  =33.690\ldots^\circ.
  $$

  For the third grating maximum, $d\sin\theta_3=3\lambda$. Therefore,

  $$
  \lambda
  =\frac{(3.0\times10^{-6}\ \mathrm{m})\sin(33.690\ldots^\circ)}{3}
  =5.547\ldots\times10^{-7}\ \mathrm{m}.
  $$

  The measured values support two significant figures, so $\lambda=5.5\times10^2\ \mathrm{nm}$, entered as `550`.
```
