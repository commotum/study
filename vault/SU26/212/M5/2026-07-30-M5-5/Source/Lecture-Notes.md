## Lecture Outline (Phase Difference and Two-Source Interference)

### 1. Course Logistics

- Quiz 2 scores have been posted.
- Quiz 2X is open and is due:
  $$ \text{Tuesday at }6{:}00\text{ PM} $$
- Quiz 3 covers the wave material presented since Quiz 2, including this lecture.
- The Proctorio version of Quiz 3:
  - opens Saturday at $5{:}00\text{ PM}$
  - closes Monday at $5{:}00\text{ PM}$
- Zoom-proctored sessions will be held Monday at:
  $$ 11{:}00\text{ AM}\quad\text{and}\quad6{:}00\text{ PM} $$
- Students should continue preparing their Quiz 3 note sheet.

---

### 2. Scope Note: Beating

- Beating was briefly mentioned but will not be covered in class.
- Questions about beating will not appear on the quiz.

---

## Two-Source Interference

### 3. Two In-Phase Sound Sources

- The simulation uses two speakers oscillating in phase.
- Both speakers produce compressions and rarefactions at the same time.
- In the simulation:
  - light rings represent compressions
  - dark rings represent rarefactions
  - gray nodal regions represent complete cancellation
- The two sound waves interfere wherever they overlap.

---

### 4. Constructive Interference

- Complete constructive interference occurs where equal waves arrive with the same phase:
  - compression meets compression
  - rarefaction meets rarefaction
  - crest meets crest
  - trough meets trough
- Their displacements add:
  $$ y_{\mathrm{net}}=y_1+y_2 $$
- For two waves with equal amplitude $A$:
  $$ A_{\mathrm{net}}=2A $$
- A location of constructive interference is not permanently a crest or trough.
- Instead, it oscillates with the maximum possible amplitude.

---

### 5. Destructive Interference

- Complete destructive interference occurs where equal waves arrive completely out of phase:
  - compression meets rarefaction
  - crest meets trough
- For equal amplitudes:
  $$ A_{\mathrm{net}}=A-A=0 $$
- At most other locations, the waves undergo partial interference rather than complete constructive or destructive interference.

---

### 6. Effect of Frequency on the Pattern

- Wave speed, frequency, and wavelength are related by:
  $$ v_{\mathrm{wave}}=f\lambda $$
- For a fixed wave speed, increasing the frequency decreases the wavelength.
- More wavefronts then fit within the same region, producing more alternating lines of constructive and destructive interference.

---

## Graphical Interference Example

### 7. Interpreting the Wavefront Diagram

- The blue circles in the diagram represent crests.
- Troughs lie halfway between successive crest circles.
- The interference at a point depends on which portions of the two waves arrive there simultaneously.

---

### 8. Classification of the Labeled Points

- Point $P$ is a position of complete constructive interference because two crests meet there.
- Point $R$ is also a position of complete constructive interference because two troughs meet there.
- Point $Q$ is a position of complete destructive interference because a crest meets a trough.

---

## Phase of a Sinusoidal Wave

### 9. Traveling-Wave Equation

- A sinusoidal wave traveling in the positive $x$-direction may be written:
  $$ y(x,t)=A\sin(kx-\omega t+\phi_0) $$
- The phase of the wave is the argument of the sine function:
  $$ \phi(x,t)=kx-\omega t+\phi_0 $$
- Here:
  - $A$ is the amplitude
  - $k$ is the wave number
  - $\omega$ is the angular frequency
  - $\phi_0$ is the initial phase

---

### 10. Wavelength and Wave Number

- The wavelength $\lambda$ may be measured between:
  - successive crests
  - successive troughs
  - equivalent zero crossings with the same crossing direction
- Adjacent zero crossings are separated by only:
  $$ \frac{\lambda}{2} $$
- The wave number is:
  $$ \boxed{k=\frac{2\pi}{\lambda}} $$
- It represents the spatial phase change per unit distance.

---

## Phase Difference Along One Wave

### 11. Phases at Two Positions

- Consider positions $x_1$ and $x_2$ at the same time:
  $$ \phi_1=kx_1-\omega t+\phi_0 $$
  $$ \phi_2=kx_2-\omega t+\phi_0 $$
- Define the separation:
  $$ \Delta x=x_2-x_1 $$

---

### 12. Derive the Spatial Phase Difference

- The phase difference is:
  $$ \Delta\phi=\phi_2-\phi_1 $$
- Therefore:
  $$
  \Delta\phi
  =
  \left(kx_2-\omega t+\phi_0\right)
  -
  \left(kx_1-\omega t+\phi_0\right)
  $$
- Because both phases are evaluated at the same time, the time terms cancel.
- The initial-phase terms also cancel:
  $$ \Delta\phi=k(x_2-x_1)=k\Delta x $$
- Using:
  $$ k=\frac{2\pi}{\lambda} $$
- The spatial phase difference is:
  $$ \boxed{\Delta\phi=\frac{2\pi\Delta x}{\lambda}} $$

---

### 13. Physical Interpretation

- A separation of one complete wavelength gives:
  $$ \Delta x=\lambda $$
  $$ \Delta\phi=2\pi $$
- A separation of half a wavelength gives:
  $$ \Delta x=\frac{\lambda}{2} $$
  $$ \Delta\phi=\pi $$
- A separation of one-quarter wavelength gives:
  $$ \Delta x=\frac{\lambda}{4} $$
  $$ \Delta\phi=\frac{\pi}{2} $$

---

## Phase Difference Between Two Waves

### 14. Two Coherent Sources

- Consider two waves with the same frequency and wavelength but possibly different initial phases:
  $$ y_1=A\sin(kr_1-\omega t+\phi_{1,0}) $$
  $$ y_2=A\sin(kr_2-\omega t+\phi_{2,0}) $$
- Here:
  - $r_1$ is the path length from source 1
  - $r_2$ is the path length from source 2
- Define:
  $$ \Delta r=r_2-r_1 $$
  $$ \Delta\phi_0=\phi_{2,0}-\phi_{1,0} $$

---

### 15. General Phase-Difference Equation

- Subtracting the two phases gives:
  $$
  \Delta\phi
  =
  k(r_2-r_1)
  +
  \left(\phi_{2,0}-\phi_{1,0}\right)
  $$
- Therefore:
  $$ \Delta\phi=k\Delta r+\Delta\phi_0 $$
- Using:
  $$ k=\frac{2\pi}{\lambda} $$
- The general result is:
  $$ \boxed{\Delta\phi=\frac{2\pi\Delta r}{\lambda}+\Delta\phi_0} $$

---

### 16. Initial Phase of the Sources

- Sources that begin in phase have:
  $$ \Delta\phi_0=0\pmod{2\pi} $$
- Sources that begin completely out of phase have:
  $$ \Delta\phi_0=\pi\pmod{2\pi} $$
- The interference at an observation point depends on both:
  - the initial phase difference of the sources
  - the difference between the distances traveled

---

## Conditions for Complete Interference

### 17. Complete Constructive Interference

- Complete constructive interference occurs when the arriving waves differ by a whole number of cycles:
  $$ \boxed{\Delta\phi=2\pi m} $$
- Here:
  $$ m\in\mathbb{Z} $$
- Equivalently, the phase difference is an even multiple of $\pi$.

---

### 18. Complete Destructive Interference

- Complete destructive interference occurs when the arriving waves differ by an odd multiple of $\pi$:
  $$ \boxed{\Delta\phi=(2m+1)\pi} $$
- An equivalent form is:
  $$ \boxed{\Delta\phi=2\pi\left(m+\frac{1}{2}\right)} $$
- Here:
  $$ m\in\mathbb{Z} $$

---

### 19. Path-Difference Rules for In-Phase Sources

- If:
  $$ \Delta\phi_0=0 $$
- Constructive interference requires:
  $$ \boxed{\Delta r=m\lambda} $$
- Destructive interference requires:
  $$ \boxed{\Delta r=\left(m+\frac{1}{2}\right)\lambda} $$

---

### 20. Phase Is Periodic

- Phase differences separated by an integer multiple of $2\pi$ describe the same relative phase:
  $$ \Delta\phi\equiv\Delta\phi+2\pi m $$
- A large phase difference may therefore be reduced modulo $2\pi$ when only the relative phase is needed.

---

## Example 1: Two Out-of-Phase Radio Antennas

### 21. Given Information

- Two radio antennas are separated by:
  $$ d=600\ \mathrm{m} $$
- The nearer antenna is:
  $$ r_1=800\ \mathrm{m} $$
  from observation point $P$.
- The antennas emit at:
  $$ f=3.0\times10^6\ \mathrm{Hz} $$
- Radio waves travel at approximately:
  $$ c=3.0\times10^8\ \mathrm{m}/\mathrm{s} $$
- The sources are completely out of phase:
  $$ \Delta\phi_0=\pi $$

---

### 22. Radio Wavelength

- Use:
  $$ c=f\lambda $$
- Therefore:
  $$ \lambda=\frac{c}{f} $$
- Substitute:
  $$
  \lambda
  =
  \frac{3.0\times10^8\ \mathrm{m}/\mathrm{s}}
  {3.0\times10^6\ \mathrm{Hz}}
  $$
- Thus:
  $$ \boxed{\lambda=100\ \mathrm{m}} $$

---

### 23. Determine the Second Path Length

- The geometry forms a right triangle:
  $$ r_2=\sqrt{r_1^2+d^2} $$
- Substitute:
  $$
  r_2
  =
  \sqrt{(800\ \mathrm{m})^2+(600\ \mathrm{m})^2}
  $$
- Therefore:
  $$ r_2=1000\ \mathrm{m} $$

---

### 24. Path-Length Difference

- The difference between the two paths is:
  $$ \Delta r=r_2-r_1 $$
- Therefore:
  $$ \Delta r=1000\ \mathrm{m}-800\ \mathrm{m} $$
- Thus:
  $$ \boxed{\Delta r=200\ \mathrm{m}=2\lambda} $$

---

### 25. Phase Difference at Point $P$

- Use:
  $$ \Delta\phi=\frac{2\pi\Delta r}{\lambda}+\Delta\phi_0 $$
- Substitute:
  $$
  \Delta\phi
  =
  2\pi
  \left(
  \frac{200\ \mathrm{m}}{100\ \mathrm{m}}
  \right)
  +
  \pi
  $$
- Therefore:
  $$ \Delta\phi=4\pi+\pi $$
  $$ \boxed{\Delta\phi=5\pi} $$

---

### 26. Interference Classification

- Since $5\pi$ is an odd multiple of $\pi$, point $P$ is a location of:
  $$ \boxed{\text{complete destructive interference}} $$
- Although the path-length difference alone contributes $4\pi$, the sources begin with an additional phase difference of $\pi$.

---

### 27. Common Error

- If the initial phase difference were omitted, the calculation would incorrectly give:
  $$ \Delta\phi=4\pi $$
- That would incorrectly predict constructive interference.
- The initial source phase must always be included when it is not zero.

---

## Example 2: Phase Difference from Two Flutes

### 28. Problem Setup

- Two flutes lie on opposite sides of the $y$-axis.
- Point $P$ lies on the $y$-axis.
- Both flutes emit:
  $$ f=830\ \mathrm{Hz} $$
- Use the speed of sound:
  $$ v_{\mathrm{wave}}=343\ \mathrm{m}/\mathrm{s} $$
- The flutes emit in phase:
  $$ \Delta\phi_0=0 $$
- Let:
  - $x_1$ be the horizontal distance from flute 1 to the $y$-axis
  - $x_2$ be the horizontal distance from flute 2 to the $y$-axis
  - $y$ be the vertical coordinate of point $P$

---

### 29. Determine the Path Lengths

- The distance from flute 1 to point $P$ is:
  $$ r_1=\sqrt{x_1^2+y^2} $$
- The distance from flute 2 to point $P$ is:
  $$ r_2=\sqrt{x_2^2+y^2} $$
- Therefore:
  $$
  \Delta r
  =
  \sqrt{x_2^2+y^2}
  -
  \sqrt{x_1^2+y^2}
  $$

---

### 30. Phase-Difference Equation

- Begin with:
  $$ \Delta\phi=\frac{2\pi\Delta r}{\lambda}+\Delta\phi_0 $$
- Since:
  $$ \lambda=\frac{v_{\mathrm{wave}}}{f} $$
- Then:
  $$ \frac{1}{\lambda}=\frac{f}{v_{\mathrm{wave}}} $$
- Because the sources are in phase:
  $$
  \boxed{
  \Delta\phi
  =
  \frac{2\pi f}{v_{\mathrm{wave}}}
  \left(
  \sqrt{x_2^2+y^2}
  -
  \sqrt{x_1^2+y^2}
  \right)
  }
  $$

---

### 31. Numerical Result

- Substitution of the coordinates shown in the lecture diagram gives:
  $$ \boxed{\Delta\phi\approx66\ \mathrm{rad}} $$
- Using the rounded value:
  $$ 66\ \mathrm{rad}\bmod 2\pi\approx3.17\ \mathrm{rad} $$
- The unrounded phase should be used if the interference must be classified precisely.

---

## Example 3: First Maximum-Intensity Point on the Positive $x$-Axis

### 32. Speaker Geometry

- Speaker $A$ is at the origin:
  $$ A=(0,0) $$
- Speaker $B$ is a distance $y$ below the origin:
  $$ B=(0,-y) $$
- The observation point lies on the positive $x$-axis:
  $$ P=(x,0) $$
- The speakers emit coherent, in-phase sound waves.
- The given values are:
  $$ y=2.20\ \mathrm{m} $$
  $$ \lambda=0.50\ \mathrm{m} $$
- Goal: find the first maximum-intensity position to the right of the origin.

---

### 33. Distances to the Observation Point

- For $x>0$, the distance from speaker $A$ is:
  $$ r_1=x $$
- The distance from speaker $B$ is:
  $$ r_2=\sqrt{x^2+y^2} $$
- Therefore:
  $$ \boxed{\Delta r=\sqrt{x^2+y^2}-x} $$

---

### 34. Condition for Maximum Intensity

- Maximum intensity occurs at complete constructive interference.
- For in-phase sources:
  $$ \Delta r=m\lambda $$
- Therefore:
  $$ \sqrt{x^2+y^2}-x=m\lambda $$
- The integer $m$ should be retained until the possible positions have been evaluated.

---

### 35. Solve for $x$

- Begin with:
  $$ \sqrt{x^2+y^2}-x=m\lambda $$
- Add $x$:
  $$ \sqrt{x^2+y^2}=x+m\lambda $$
- Square both sides:
  $$ x^2+y^2=x^2+2m\lambda x+m^2\lambda^2 $$
- Cancel $x^2$:
  $$ y^2=2m\lambda x+m^2\lambda^2 $$
- Solve for $x$:
  $$
  \boxed{
  x
  =
  \frac{y^2}{2m\lambda}
  -
  \frac{m\lambda}{2}
  }
  $$

---

### 36. The Case $m=0$

- The algebraic formula for $x$ cannot be used with:
  $$ m=0 $$
- Physically, $m=0$ requires:
  $$ \Delta r=0 $$
- For the two separated speakers, the path-length difference approaches zero only as:
  $$ x\rightarrow\infty $$
- There is no finite positive-$x$ solution for $m=0$.

---

### 37. Substitute the Given Values

- Using:
  $$ y=2.20\ \mathrm{m} $$
  $$ \lambda=0.50\ \mathrm{m} $$
- The position becomes:
  $$
  x_m
  =
  \frac{(2.20\ \mathrm{m})^2}
  {2m(0.50\ \mathrm{m})}
  -
  \frac{m(0.50\ \mathrm{m})}{2}
  $$
- Therefore:
  $$ \boxed{x_m=\frac{4.84\ \mathrm{m}}{m}-(0.25\ \mathrm{m})m} $$

---

### 38. Evaluate the Interference Orders

| $m$ | Calculated $x_m$ |
|---:|---:|
| $1$ | $4.59\ \mathrm{m}$ |
| $2$ | $1.92\ \mathrm{m}$ |
| $3$ | $0.86\ \mathrm{m}$ |
| $4$ | $0.21\ \mathrm{m}$ |
| $5$ | $-0.28\ \mathrm{m}$ |
| $6$ | $-0.69\ \mathrm{m}$ |

- The negative results lie outside the assumed positive-$x$ region.
- Thus, the permitted positive-$x$ interference orders are:
  $$ m=1,2,3,4 $$

---

### 39. First Maximum to the Right of the Origin

- The maximum closest to the origin corresponds to the smallest positive value of $x$.
- From the table, this occurs at:
  $$ m=4 $$
- Therefore:
  $$ \boxed{x\approx0.21\ \mathrm{m}} $$

---

### 40. Physical Check on the Allowed Values

- Along the positive $x$-axis:
  $$ \Delta r=\sqrt{x^2+y^2}-x $$
- Near the origin:
  $$ \Delta r\rightarrow y=2.20\ \mathrm{m}=4.4\lambda $$
- Far from the speakers:
  $$ \Delta r\rightarrow0 $$
- Therefore, the positive integer multiples of $\lambda$ that occur are:
  $$ \lambda,\quad2\lambda,\quad3\lambda,\quad4\lambda $$
- This confirms that:
  $$ m_{\max}=4 $$

---

### 41. Main Physics Takeaways

- Phase of a sinusoidal wave:
  $$ \phi=kx-\omega t+\phi_0 $$
- Wave number:
  $$ k=\frac{2\pi}{\lambda} $$
- Spatial phase difference along one wave:
  $$ \Delta\phi=\frac{2\pi\Delta x}{\lambda} $$
- Phase difference from two coherent sources:
  $$ \boxed{\Delta\phi=\frac{2\pi\Delta r}{\lambda}+\Delta\phi_0} $$
- Using:
  $$ v_{\mathrm{wave}}=f\lambda $$
- The same equation may be written:
  $$ \boxed{\Delta\phi=\frac{2\pi f}{v}\Delta r+\Delta\phi_0} $$
- Complete constructive interference:
  $$ \Delta\phi=2\pi m $$
- Complete destructive interference:
  $$ \Delta\phi=(2m+1)\pi $$
- For in-phase sources:
  $$ \Delta r=m\lambda $$
  gives constructive interference.
- The initial source phase and the path-length difference must both be included.

---

### 42. Main Problem-Solving Strategy

1. Identify the two sources and determine whether they begin in phase or out of phase.
2. Write the initial phase difference:
   $$ \Delta\phi_0 $$
3. Calculate the two path lengths:
   $$ r_1\quad\text{and}\quad r_2 $$
4. Determine:
   $$ \Delta r=r_2-r_1 $$
5. Find the wavelength using the correct wave speed:
   $$ \lambda=\frac{v}{f} $$
6. Use:
   $$ \Delta\phi=\frac{2\pi\Delta r}{\lambda}+\Delta\phi_0 $$
7. Classify the result as constructive, destructive, or partial interference.
8. When solving for a location, retain the integer $m$ until all geometrically allowed values have been tested.
9. Check that the final position lies in the region specified by the problem.
