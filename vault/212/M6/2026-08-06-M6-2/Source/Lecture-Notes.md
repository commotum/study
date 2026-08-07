## Lecture Outline (Diffraction Gratings, Spectroscopy, and Single-Slit Diffraction)

### 1. End-of-Term Deadline

- This is the next-to-last week of the term.
- The final day of the course is next Friday.
- No coursework will be accepted after that deadline.
- Students should verify that all assignments, especially all lab reports, have been submitted.

---

### 2. Lab Requirements

- Every lab must be submitted.
- Students must also earn an average lab score of at least:
  $$ 70\% $$
- Students with missing labs should email their lab TA immediately and explain that the reports are being completed.
- No lab score is dropped.

---

### 3. Final-Exam Schedule

- The Proctorio version of the final exam:
  - opens Tuesday at $5{:}00\text{ PM}$
  - closes Thursday at $5{:}00\text{ PM}$
- Zoom-proctored sessions will be offered Thursday at:
  $$ 11{:}00\text{ AM}\quad\text{and}\quad6{:}00\text{ PM} $$

---

### 4. Final Exam Is Required

- The final exam does not replace the lowest quiz score.
- The final is cumulative and is separate from the quiz category.
- The lowest quiz score has already been dropped.
- Students must still complete the final exam.

---

### 5. Dropped Scores

- The instructor has already dropped:
  - the lowest quiz score
  - three pre-lecture scores
  - three participation scores
  - one homework score
- No lab score is dropped.

---

### 6. Check the Canvas Gradebook

- Students should inspect the Canvas gradebook for missing scores.
- If a submitted lab report does not have a posted score, the student should email the lab TA.
- The email should identify the report and ask the TA to grade it or post its score as soon as possible.

---

## Review of Double-Slit Interference and Diffraction Gratings

### 7. Coherent Illumination

- A laser beam may be modeled as a coherent plane wave.
- Coherent light has:
  - a common frequency
  - a common wavelength in the same medium
  - a stable relative phase
- For a plane wave normally incident on the slits, the openings are illuminated in phase.
- Each opening then acts approximately as a coherent secondary wave source.

---

### 8. Governing Equations

- The condition for a bright interference maximum is:
  $$ \boxed{d\sin\theta_m=m\lambda} $$
- Equivalently:
  $$ \boxed{\sin\theta_m=\frac{m\lambda}{d}} $$
- The screen geometry is:
  $$ \boxed{\tan\theta_m=\frac{y_m}{L}} $$
- Here:
  - $d$ is the center-to-center spacing between neighboring slits
  - $\theta_m$ is the angle of the $m$th bright fringe
  - $m$ is the interference order
  - $\lambda$ is the wavelength
  - $y_m$ is the fringe’s position relative to the central maximum
  - $L$ is the distance from the slits or grating to the screen

---

### 9. Exact Screen Position

- Solve the interference condition for the angle:
  $$ \theta_m=\sin^{-1}\left(\frac{m\lambda}{d}\right) $$
- Then use:
  $$ y_m=L\tan\theta_m $$
- Therefore:
  $$
  \boxed{
  y_m
  =
  L\tan\left[
  \sin^{-1}\left(\frac{m\lambda}{d}\right)
  \right]
  }
  $$

---

### 10. Small-Angle Approximation

- For sufficiently small angles:
  $$ \sin\theta_m\approx\tan\theta_m\approx\theta_m $$
- The fringe-position equation then becomes:
  $$ \boxed{y_m\approx\frac{m\lambda L}{d}} $$
- Under this approximation, the bright fringes are evenly spaced.
- The approximation is valid when:
  $$ \frac{m\lambda}{d}\ll1 $$
- Its validity depends on the angle, not simply on whether the device is a double slit or a diffraction grating.
- Diffraction gratings often produce large angles, so the exact trigonometric equations are frequently required.

---

## Example 1: Lines per Millimeter in a Diffraction Grating

### 11. Given Information

- A helium–neon laser has wavelength:
  $$ \lambda=633\text{ nm} $$
- The screen is:
  $$ L=2.4\text{ m} $$
  from the grating.
- The separation between the two first-order bright fringes is:
  $$ 2y_1=1.70\text{ m} $$
- Therefore:
  $$ y_1=0.85\text{ m} $$
- Find the grating’s number of lines per millimeter.

---

### 12. Grating Spacing and Line Density

- Let $\rho$ be the number of grating lines per unit width.
- If $d$ is the distance between neighboring lines:
  $$ \boxed{\rho=\frac{1}{d}} $$
- If a width $W$ contains $N$ lines:
  $$ \rho=\frac{N}{W} $$
- Therefore:
  $$ N=\rho W=\frac{W}{d} $$

---

### 13. Determine the First-Order Angle

- From the screen geometry:
  $$ \tan\theta_1=\frac{y_1}{L} $$
- Therefore:
  $$
  \theta_1
  =
  \tan^{-1}\left(\frac{0.85\text{ m}}{2.4\text{ m}}\right)
  $$
- This gives:
  $$ \boxed{\theta_1\approx19.5^\circ} $$

---

### 14. Solve for the Line Density

- Begin with:
  $$ d\sin\theta_m=m\lambda $$
- Solve for:
  $$ \frac{1}{d} $$
- This gives:
  $$ \frac{1}{d}=\frac{\sin\theta_m}{m\lambda} $$
- Therefore:
  $$ \boxed{\rho=\frac{\sin\theta_m}{m\lambda}} $$
- Combining this with the screen geometry:
  $$
  \boxed{
  \rho
  =
  \frac{
  \sin\left[
  \tan^{-1}\left(\frac{y_m}{L}\right)
  \right]
  }
  {m\lambda}
  }
  $$

---

### 15. Numerical Calculation

- For the first-order maximum:
  $$ m=1 $$
- Substitute:
  $$
  \rho
  =
  \frac{
  \sin\left[
  \tan^{-1}\left(\frac{0.85}{2.4}\right)
  \right]
  }
  {(1)(633\times10^{-9}\text{ m})}
  $$
- Therefore:
  $$ \rho\approx5.27\times10^5\frac{\text{lines}}{\text{m}} $$
- Since:
  $$ 1\text{ m}=1000\text{ mm} $$
- The line density is:
  $$ \rho\approx527\frac{\text{lines}}{\text{mm}} $$

---

### 16. Final Result

- To two significant figures:
  $$ \boxed{\rho\approx5.3\times10^2\frac{\text{lines}}{\text{mm}}} $$
- Therefore, the grating contains approximately:
  $$ \boxed{530\text{ lines/mm}} $$

---

### 17. Significant Figures

- The wavelength:
  $$ 633\text{ nm} $$
  has three significant figures.
- The distances:
  $$ 2.4\text{ m}\quad\text{and}\quad1.70\text{ m} $$
  limit the final answer to approximately two or three significant figures.
- Scientific notation makes the intended precision clear:
  $$ 5.3\times10^2\text{ lines/mm} $$

---

## Example 2: Maximum Number of Diffraction-Grating Maxima

### 18. Given Information

- Grating spacing:
  $$ d=1.8\times10^{-6}\text{ m} $$
- Laser wavelength:
  $$ \lambda=633\times10^{-9}\text{ m} $$
- Find the possible bright-fringe orders and the total number of principal maxima.

---

### 19. Physical Restriction on the Order

- The grating equation is:
  $$ \sin\theta_m=\frac{m\lambda}{d} $$
- A real diffraction angle requires:
  $$ |\sin\theta_m|\leq1 $$
- Therefore:
  $$ \left|\frac{m\lambda}{d}\right|\leq1 $$
- Thus:
  $$ \boxed{|m|\leq\frac{d}{\lambda}} $$

---

### 20. Determine the Maximum Order

- Substitute:
  $$
  \frac{d}{\lambda}
  =
  \frac{1.8\times10^{-6}}
  {633\times10^{-9}}
  $$
- This gives:
  $$ \frac{d}{\lambda}\approx2.84 $$
- Because $m$ must be an integer:
  $$ \boxed{m_{\max}=2} $$

---

### 21. Brute-Force Check of the Angles

- For the first order:
  $$
  \theta_1
  =
  \sin^{-1}\left(\frac{\lambda}{d}\right)
  $$
- Therefore:
  $$ \boxed{\theta_1\approx20.6^\circ} $$
- For the second order:
  $$
  \theta_2
  =
  \sin^{-1}\left(\frac{2\lambda}{d}\right)
  $$
- Therefore:
  $$ \boxed{\theta_2\approx44.7^\circ} $$

---

### 22. Why the Third Order Does Not Exist

- For:
  $$ m=3 $$
- The inverse-sine argument would be:
  $$
  \frac{3\lambda}{d}
  =
  \frac{3(633\times10^{-9})}
  {1.8\times10^{-6}}
  \approx1.055
  $$
- Since:
  $$ 1.055>1 $$
- The expression:
  $$ \sin^{-1}(1.055) $$
  has no real value.
- Therefore, no real forward angle can produce an $m=3$ principal maximum.

---

### 23. Total Number of Bright Fringes

- The allowed orders are:
  $$ m=-2,-1,0,1,2 $$
- The total number of possible principal maxima is:
  $$ N_{\text{maxima}}=2m_{\max}+1 $$
- Therefore:
  $$ N_{\text{maxima}}=2(2)+1 $$
- Thus:
  $$ \boxed{N_{\text{maxima}}=5} $$

---

### 24. Physical Interpretation

- The absence of the third-order maximum is not caused by the screen being too narrow.
- The third-order beam cannot exist because no real angle satisfies the grating equation.
- Making the screen arbitrarily large would not create an $m=3$ maximum.
- Assuming the screen intercepts all the physically allowed orders, five principal maxima appear.

---

## Spectroscopy

### 25. Wavelength-Dependent Diffraction

- From:
  $$ d\sin\theta_m=m\lambda $$
- Different wavelengths produce different diffraction angles.
- A diffraction grating therefore separates incoming light into its component wavelengths.
- The resulting distribution of intensity versus wavelength is called a spectrum.

---

### 26. Atomic Spectral Fingerprints

- Electrons in atoms occupy discrete energy levels.
- A photon can be absorbed when its energy matches an allowed upward transition:
  $$ E_\gamma=hf=\frac{hc}{\lambda} $$
- When an excited electron drops to a lower energy level, it can emit a photon satisfying:
  $$ \Delta E=hf=\frac{hc}{\lambda} $$
- Each element has a unique set of allowed energy differences.
- Its absorption and emission wavelengths therefore form a distinctive spectral fingerprint.

---

### 27. Stellar Absorption Spectra

- A hot, dense stellar interior produces an approximately continuous spectrum.
- This light passes through cooler material in the star’s outer atmosphere.
- Atoms in the atmosphere absorb specific wavelengths corresponding to their allowed electronic transitions.
- Re-emitted photons travel in many directions, leaving reduced intensity along the original line of sight.
- The observed spectrum therefore contains dark absorption lines.
- Comparing these lines with laboratory spectra reveals which elements are present in the star.

---

### 28. Emission Spectra

- A low-density excited gas can produce bright emission lines.
- These lines occur when excited electrons transition to lower energy levels and emit photons.
- Absorption and emission lines occur at characteristic wavelengths determined by the same atomic energy-level structure.

---

### 29. Astronomical Applications

- Spectroscopy can reveal the composition of:
  - stars
  - galaxies
  - interstellar gas
- Light from increasingly distant objects has traveled for increasingly long periods.
- Looking farther into space also means looking farther into the past.
- Spectra from objects at different distances help reveal how the universe has changed over time.

---

## Single-Slit Diffraction

### 30. Why One Slit Produces Interference

- A single slit contains only one physical opening, but it still produces an interference pattern.
- According to the Huygens–Fresnel principle, every point across the illuminated slit acts as a secondary wave source.
- Contributions from different parts of the slit travel slightly different distances to a point on the screen.
- Their superposition produces:
  - constructive interference at some angles
  - destructive interference at other angles

---

### 31. Appearance of the Pattern

- A single-slit diffraction pattern contains:
  - a broad, bright central maximum
  - dark minima on both sides
  - weaker secondary bright fringes between successive minima
- The secondary maxima become progressively dimmer away from the center.
- The central maximum is approximately twice as wide as each secondary bright region.

---

### 32. Single-Slit Variables

- Let:
  - $a$ be the width of the slit
  - $L$ be the distance from the slit to the screen
  - $\theta_p$ be the angle to the $p$th dark minimum
  - $y_p$ be the position of that minimum relative to the center
- The screen geometry is:
  $$ \boxed{\tan\theta_p=\frac{y_p}{L}} $$

---

### 33. Meaning of the Integer $p$

- For single-slit diffraction, $p$ labels dark minima:
  $$ p=\pm1,\pm2,\pm3,\ldots $$
- On one side of the pattern:
  $$ p=1,2,3,\ldots $$
- There is no $p=0$ dark fringe.
- At:
  $$ \theta=0 $$
  all contributions arrive in phase and form the central maximum.

---

## Derivation of the Single-Slit Minimum Condition

### 34. First Dark Minimum

- For the first minimum, divide the slit into two equal halves.
- Pair each point in the upper half with a corresponding point in the lower half.
- The paired points are separated by:
  $$ \frac{a}{2} $$
- Their path-length difference is:
  $$ \Delta r=\frac{a}{2}\sin\theta_1 $$
- Pairwise cancellation occurs when:
  $$ \Delta r=\frac{\lambda}{2} $$
- Therefore:
  $$ \frac{a}{2}\sin\theta_1=\frac{\lambda}{2} $$
- Canceling the factor of $\frac{1}{2}$ gives:
  $$ \boxed{a\sin\theta_1=\lambda} $$

---

### 35. General Dark-Minimum Condition

- For the $p$th minimum, divide the slit into $2p$ equal regions.
- Pair contributions from regions separated by:
  $$ \frac{a}{2p} $$
- Their path-length difference is:
  $$ \Delta r=\frac{a}{2p}\sin\theta_p $$
- For pairwise destructive interference:
  $$ \Delta r=\frac{\lambda}{2} $$
- Therefore:
  $$ \frac{a}{2p}\sin\theta_p=\frac{\lambda}{2} $$
- Multiply by $2p$:
  $$ \boxed{a\sin\theta_p=p\lambda} $$
- Equivalently:
  $$ \boxed{\sin\theta_p=\frac{p\lambda}{a}} $$

---

### 36. Exact Position of a Dark Minimum

- Solve for the angle:
  $$ \theta_p=\sin^{-1}\left(\frac{p\lambda}{a}\right) $$
- Use:
  $$ y_p=L\tan\theta_p $$
- Therefore:
  $$
  \boxed{
  y_p
  =
  L\tan\left[
  \sin^{-1}\left(\frac{p\lambda}{a}\right)
  \right]
  }
  $$

---

### 37. Small-Angle Minimum Position

- For sufficiently small angles:
  $$ \sin\theta_p\approx\tan\theta_p $$
- Since:
  $$ \sin\theta_p=\frac{p\lambda}{a} $$
  and:
  $$ \tan\theta_p=\frac{y_p}{L} $$
- We obtain:
  $$ \frac{y_p}{L}\approx\frac{p\lambda}{a} $$
- Therefore:
  $$ \boxed{y_p\approx\frac{p\lambda L}{a}} $$

---

### 38. Spacing of the Dark Minima

- On the positive side of the pattern:
  $$ y_1\approx\frac{\lambda L}{a} $$
  $$ y_2\approx\frac{2\lambda L}{a} $$
  $$ y_3\approx\frac{3\lambda L}{a} $$
- Adjacent dark minima are approximately separated by:
  $$ \boxed{\Delta y_{\text{dark}}\approx\frac{\lambda L}{a}} $$

---

### 39. Width of the Central Maximum

- The central maximum lies between:
  $$ y=-y_1 $$
  and:
  $$ y=+y_1 $$
- Therefore:
  $$ w_{\text{central}}=2y_1 $$
- Under the small-angle approximation:
  $$ \boxed{w_{\text{central}}\approx\frac{2\lambda L}{a}} $$

---

## Double-Slit and Single-Slit Comparison

### 40. Similar Equations with Different Meanings

| System | Labeled feature | Exact condition | Small-angle position |
|---|---|---|---|
| Double slit or grating | Bright maximum $m$ | $d\sin\theta_m=m\lambda$ | $y_m\approx\dfrac{m\lambda L}{d}$ |
| Single slit | Dark minimum $p$ | $a\sin\theta_p=p\lambda$ | $y_p\approx\dfrac{p\lambda L}{a}$ |

- For the double slit:
  - $d$ is the separation between the two slits
  - $m$ identifies bright fringes
- For the single slit:
  - $a$ is the width of the one slit
  - $p$ identifies dark minima
- The mathematical forms are similar, but they locate different features of the patterns.

---

## Example 3: Distance from a Single Slit to the Screen

### 41. Given Information

- Laser wavelength:
  $$ \lambda\approx633\text{ nm} $$
- Single-slit width:
  $$ a=0.15\text{ mm} $$
- Convert the slit width:
  $$ a=1.5\times10^{-4}\text{ m} $$
- The center of the central maximum appears at the $6\text{ cm}$ coordinate on the graph.
- The first dark minimum is $2\text{ cm}$ from the center:
  $$ y_1=2.0\text{ cm}=2.0\times10^{-2}\text{ m} $$
- Find the slit-to-screen distance:
  $$ L $$

---

### 42. Solve for the Screen Distance

- For the first dark minimum:
  $$ y_1\approx\frac{\lambda L}{a} $$
- Solve for $L$:
  $$ \boxed{L\approx\frac{y_1a}{\lambda}} $$

---

### 43. Numerical Result

- Substitute:
  $$
  L
  \approx
  \frac{
  (2.0\times10^{-2}\text{ m})
  (1.5\times10^{-4}\text{ m})
  }
  {633\times10^{-9}\text{ m}}
  $$
- Therefore:
  $$ L\approx4.74\text{ m} $$
- Rounded appropriately:
  $$ \boxed{L\approx4.7\text{ m}} $$

---

## Secondary Bright Fringes

### 44. Approximate Positions

- Secondary bright fringes lie between consecutive dark minima.
- In the approximation used during the lecture, each secondary maximum is placed halfway between the neighboring minima.
- The first secondary bright fringe lies between:
  $$ p=1\quad\text{and}\quad p=2 $$
- Its approximate position is:
  $$
  y_{\text{bright},1}
  \approx
  \frac{y_1+y_2}{2}
  =
  \frac{3\lambda L}{2a}
  $$
- The second secondary bright fringe lies between:
  $$ p=2\quad\text{and}\quad p=3 $$
- Its approximate position is:
  $$
  \boxed{
  y_{\text{bright},2}
  \approx
  \frac{y_2+y_3}{2}
  =
  \frac{5\lambda L}{2a}
  }
  $$

---

### 45. Accuracy of the Midpoint Approximation

- The dark-minimum positions:
  $$ a\sin\theta_p=p\lambda $$
  are exact within the ideal Fraunhofer single-slit model.
- The secondary bright maxima are not located exactly halfway between adjacent minima.
- The midpoint method is a convenient introductory approximation.
- A more exact treatment uses:
  $$
  I(\theta)
  =
  I(0)
  \left(
  \frac{\sin\beta}{\beta}
  \right)^2
  $$
- Here:
  $$ \beta=\frac{\pi a\sin\theta}{\lambda} $$
- The noncentral maxima satisfy:
  $$ \tan\beta=\beta $$
- For the second secondary maximum, the exact dimensionless coefficient is approximately:
  $$ \frac{a\sin\theta}{\lambda}\approx2.459 $$
- The midpoint approximation uses:
  $$ 2.5 $$

---

## Example 4: Position of the Second Secondary Bright Fringe

### 46. Problem Setup

- The wavelength $\lambda$ and slit width $a$ are supplied in the problem.
- The screen is:
  $$ L=1.2\text{ m} $$
  from the slit.
- Find the distance from the central maximum to the second secondary bright fringe.

---

### 47. Identify the Surrounding Minima

- The integer $p$ labels dark minima.
- The second secondary bright fringe lies between:
  $$ p=2\quad\text{and}\quad p=3 $$
- Therefore:
  $$ y_{\text{bright},2}\approx\frac{y_2+y_3}{2} $$

---

### 48. Calculate the Position

- Use:
  $$ y_2\approx\frac{2\lambda L}{a} $$
  $$ y_3\approx\frac{3\lambda L}{a} $$
- Then:
  $$
  y_{\text{bright},2}
  \approx
  \frac{1}{2}
  \left(
  \frac{2\lambda L}{a}
  +
  \frac{3\lambda L}{a}
  \right)
  $$
- Therefore:
  $$ \boxed{y_{\text{bright},2}\approx\frac{5\lambda L}{2a}} $$
- Substitution of the problem’s values gives:
  $$ y_{\text{bright},2}\approx0.0139\text{ m} $$
- Rounded appropriately:
  $$ \boxed{y_{\text{bright},2}\approx0.014\text{ m}} $$
- Equivalently:
  $$ \boxed{y_{\text{bright},2}\approx1.4\text{ cm}} $$

---

### 49. Main Physics Takeaways

- Diffraction-grating maxima:
  $$ \boxed{d\sin\theta_m=m\lambda} $$
- Grating line density:
  $$ \boxed{\rho=\frac{1}{d}} $$
- Maximum possible grating order:
  $$ \boxed{|m|\leq\frac{d}{\lambda}} $$
- Total symmetric grating maxima:
  $$ \boxed{N_{\text{maxima}}=2m_{\max}+1} $$
- Single-slit dark minima:
  $$ \boxed{a\sin\theta_p=p\lambda} $$
- Exact single-slit minimum position:
  $$
  \boxed{
  y_p
  =
  L\tan\left[
  \sin^{-1}\left(\frac{p\lambda}{a}\right)
  \right]
  }
  $$
- Small-angle single-slit minimum position:
  $$ \boxed{y_p\approx\frac{p\lambda L}{a}} $$
- Central-maximum width:
  $$ \boxed{w_{\text{central}}\approx\frac{2\lambda L}{a}} $$
- In the lecture’s approximation, secondary bright fringes are located halfway between adjacent dark minima.

---

### 50. Main Problem-Solving Strategy

1. Determine whether the optical system uses:
   - two slits
   - a diffraction grating
   - one slit
2. For a double slit or grating, use:
   $$ d\sin\theta_m=m\lambda $$
3. For a single slit, use:
   $$ a\sin\theta_p=p\lambda $$
4. Remember:
   - $m$ labels bright grating or double-slit maxima
   - $p$ labels dark single-slit minima
5. Relate angle and screen position using:
   $$ \tan\theta=\frac{y}{L} $$
6. Use a small-angle formula only when the angle is sufficiently small.
7. For a grating-order problem, enforce:
   $$ \left|\frac{m\lambda}{d}\right|\leq1 $$
8. Include the central maximum and both sides when counting the total number of fringes.
9. Measure every screen position relative to the central maximum.
10. Keep the single-slit width $a$ distinct from:
    - the grating or double-slit spacing $d$
    - the screen distance $L$
11. Convert all lengths to consistent units before substituting.
12. If a problem asks for a secondary single-slit maximum, identify the neighboring dark minima and apply the stated approximation.

---

### 51. Closing

- The lecture ended after the second single-slit example.
- There is no class on Friday.
- The next class meeting will be Monday.