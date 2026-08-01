
```quiz
type: checkbox
id: m5-5lec-q1
shuffle: true
content: |-
  **Question 1**

  Assume the blue circles in the diagram represent wave crests. Which labeled points are positions of complete constructive interference? Select all correct answers and explain.

  ![](<Images/two-source-wave-crests-interference.png>)
options:
- id: p
  content: P
  correct: true
  feedback: P lies at a crest–crest intersection, so the two waves arrive in phase and interfere constructively.
- id: q
  content: Q
  feedback: Q lies on only one crest line, so it is not a point of complete constructive interference.
- id: r
  content: R
  feedback: R lies between crest lines, so it is not a point of complete constructive interference.
```

---

```quiz
type: radio
id: m5-5lec-q2
shuffle: true
content: |-
  **Question 2**

  Two completely out-of-phase radio antennas at $x=+300\ \mathrm{m}$ and $x=-300\ \mathrm{m}$ emit $3.0\ \mathrm{MHz}$ waves. At the point $(x,y)=(300\ \mathrm{m},800\ \mathrm{m})$, is the interference completely constructive, completely destructive, or neither? Show all work.

  ![](<Images/out-of-phase-antennas-path-difference.png>)
options:
- id: a
  content: Completely constructive interference
- id: b
  content: Completely destructive interference
  correct: true
  feedback: The wavelength is $100\ \mathrm{m}$. The path lengths are $800\ \mathrm{m}$ and $1000\ \mathrm{m}$, so $\Delta r=200\ \mathrm{m}=2\lambda$. A whole-number path difference preserves the antennas' initial $\pi$ phase difference, so the waves arrive completely out of phase.
- id: c
  content: Neither
```

---

```quiz
type: blank
id: m5-5lec-q3
require_exact: false
content: |-
  **Question 3**

  Flute A is at $x=-13\ \mathrm{m}$ and flute B is at $x=+27\ \mathrm{m}$. They emit an $830\ \mathrm{Hz}$ note and begin $\pi$ radians out of phase. Find the phase difference of the waves detected at point P, located at $(0,61\ \mathrm{m})$. Use $343\ \mathrm{m/s}$ for the speed of sound.

  ![](<Images/two-flute-source-geometry.png>)

  The unreduced phase difference in radians is approximately ==69==.
feedback: |-
  The path lengths are

  $$
  r_A=\sqrt{13^2+61^2}=62.3699\ldots\ \mathrm{m},
  \qquad
  r_B=\sqrt{27^2+61^2}=66.7083\ldots\ \mathrm{m},
  $$

  so $\Delta r=4.33846\ldots\ \mathrm{m}$. Including the initial phase difference,

  $$
  \Delta\phi
  =\pi+\frac{2\pi f\Delta r}{v}
  =69.1044\ldots\ \mathrm{rad}.
  $$

  The coordinate data support about two significant figures, so the unreduced result is $69\ \mathrm{rad}$. Equivalent one-cycle representations are $6.27\ \mathrm{rad}$ modulo $2\pi$, or a smallest angular separation of $0.0107\ \mathrm{rad}$ in the opposite orientation. Exact string grading is disabled because the prompt does not specify which phase convention to enter.
```

---

```quiz
type: blank
id: m5-5lec-q4
require_exact: true
content: |-
  **Question 4**

  Two speakers are in phase and emit a $686\ \mathrm{Hz}$ tone. Speaker A is at the origin, and speaker B is at $(0,-2.2\ \mathrm{m})$. Where is the first point on the positive $x$-axis where you hear maximum sound intensity? Use $343\ \mathrm{m/s}$ for the speed of sound.

  Enter the $x$-coordinate in meters as a number only: ==0.21==
feedback: |-
  The wavelength is

  $$
  \lambda=\frac{343\ \mathrm{m/s}}{686\ \mathrm{Hz}}=0.500\ \mathrm{m}.
  $$

  At $(x,0)$, the path difference is

  $$
  \Delta r=\sqrt{x^2+(2.2\ \mathrm{m})^2}-x.
  $$

  At the origin, $\Delta r=2.2\ \mathrm{m}=4.4\lambda$. Moving right, the first constructive value reached is $4\lambda=2.0\ \mathrm{m}$, so

  $$
  \sqrt{x^2+2.2^2}-x=2.0,
  $$

  which gives $x=0.21\ \mathrm{m}$ to two significant figures.
```
