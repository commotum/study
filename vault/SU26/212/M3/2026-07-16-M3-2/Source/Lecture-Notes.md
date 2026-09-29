## Lecture Outline (Binary Star Systems and Three-Body Gravitational Orbits)

### 1. Course Logistics
- Quiz 1 extra credit, Quiz 1X, is due:
  $$ \text{Friday at }6{:}00\text{ PM} $$
- Part D requires discussing the selected quiz problem with:
  - the instructor
  - a TA
  - or a Physics Wormhole tutor
- Quiz 2:
  - Proctorio version opens Saturday
  - Proctorio version closes Monday
  - Zoom-proctored versions are held Monday
- Students must submit the required handwritten quiz note sheet with a photo ID.

---

## Gravitation Review

### 2. Newton’s Law of Universal Gravitation
- The gravitational-force magnitude between two masses is:
  $$ F_g=\frac{Gm_1m_2}{r^2} $$
- In vector form:
  $$ \vec{F}_g=-\frac{Gm_1m_2}{r^2}\hat{r} $$
- The negative sign indicates that gravity is attractive.

---

### 3. Gravitational Potential Energy
- Taking the potential energy to be zero at infinite separation:
  $$ U(r)=-\frac{Gm_1m_2}{r} $$
- A negative gravitational potential energy indicates an attractive, potentially bound system.

---

### 4. Kepler’s Laws Review
- **First law:** planetary orbits are ellipses with the central body at one focus.
- **Second law:** a line between the orbiting body and central body sweeps out equal areas in equal times.
- **Third law:**
  $$ T^2\propto a^3 $$
- For circular orbits:
  $$ T^2\propto r^3 $$

---

## Binary Star System

### 5. Physical Description
- Two stars with masses $M$ and $m$ are separated by distance $d$.
- Both stars orbit their common center of mass.
- The stars:
  - have different orbital radii
  - have the same orbital period
  - remain on opposite sides of the center of mass

---

### 6. Center of Mass of the Binary System
- Choose the larger star $M$ as the origin:
  $$ x_M=0,\qquad x_m=d $$
- The center-of-mass position is:
  $$ x_{\mathrm{cm}}
  =
  \frac{Mx_M+mx_m}{M+m} $$
- Therefore:
  $$ x_{\mathrm{cm}}=\frac{md}{M+m} $$

---

### 7. Numerical Binary-Star Masses
- The lecture uses:
  $$ M=5.0\times10^{30}\ \mathrm{kg} $$
  $$ m=2.5\times10^{30}\ \mathrm{kg} $$
- Thus:
  $$ M=2m $$

---

### 8. Center-of-Mass Position for $M=2m$
- Substitute $M=2m$:
  $$ x_{\mathrm{cm}}
  =
  \frac{md}{2m+m} $$
- Therefore:
  $$ x_{\mathrm{cm}}=\frac{d}{3} $$
- As a fraction of the star separation:
  $$ \frac{x_{\mathrm{cm}}}{d}=\frac{1}{3} $$
- The center of mass lies closer to the more massive star.

---

### 9. Orbital Radii of the Two Stars
- Radius of the larger star’s orbit:
  $$ r_M=\frac{md}{M+m} $$
- Radius of the smaller star’s orbit:
  $$ r_m=\frac{Md}{M+m} $$
- Their orbital radii add to the separation:
  $$ r_M+r_m=d $$

---

### 10. Gravitational Force as the Radial Force
- For either star, take inward as positive. Gravity supplies the inward radial net force.
- Using the larger star:
  $$ \sum F_r=M a_r=M\frac{v_M^2}{r_M}=F_g=\frac{GMm}{d^2} $$
- The relevant gravitational distance is:
  $$ d $$
- The relevant orbital radius is:
  $$ r_M $$
- These are not the same distance.

---

### 11. Relating Orbital Speed and Period
- The larger star travels one circular circumference in one period:
  $$ v_M=\frac{2\pi r_M}{T} $$

---

### 12. General Binary-Orbit Period
- Substituting the center-of-mass radius and orbital speed into the force equation gives:
  $$ T^2=\frac{4\pi^2d^3}{G(M+m)} $$
- Therefore:
  $$ T=2\pi\sqrt{\frac{d^3}{G(M+m)}} $$

---

### 13. Special Form for $M=2m$
- Since:
  $$ M+m=3m $$
- The period becomes:
  $$ T=2\pi\sqrt{\frac{d^3}{3Gm}} $$

---

### 14. Numerical Binary-Orbit Period
- Using:
  $$ d=3.0\times10^{12}\ \mathrm{m} $$
  $$ m=2.5\times10^{30}\ \mathrm{kg} $$
- The lecture obtains:
  $$ T\approx46\ \mathrm{yr} $$

---

### 15. Main Binary-System Lessons
- Both stars orbit the common center of mass.
- The more massive star has the smaller orbital radius.
- Both stars complete each orbit in the same period.
- The period depends on:
  $$ d^3 $$
  and the total mass:
  $$ M+m $$

---

## Three Equal Masses in an Equilateral Triangle

### 16. Three-Body Configuration
- Three identical masses $m$ are located at the vertices of an equilateral triangle.
- Each side has length:
  $$ L $$
- The three masses orbit their common center of mass.
- By symmetry, the common center of mass is at the center of the triangle.

---

### 17. Gravitational Forces on One Mass
- Select the mass at the top of the triangle.
- The other two masses exert equal gravitational forces on it.
- Each individual force has magnitude:
  $$ F_g=\frac{Gm^2}{L^2} $$

---

### 18. Symmetry of the Force Components
- The tangential components of the two gravitational forces cancel.
- The inward radial components add.
- Each force makes an angle of:
  $$ 30^\circ $$
  with the inward radial direction.

---

### 19. Net Radial Force
- The net force is:
  $$ F_{\mathrm{net}}
  =
  2F_g\cos(30^\circ) $$
- Substitute:
  $$ F_{\mathrm{net}}
  =
  2\frac{Gm^2}{L^2}\cos(30^\circ) $$
- Since:
  $$ \cos(30^\circ)=\frac{\sqrt{3}}{2} $$
- Therefore:
  $$ F_{\mathrm{net}}
  =
  \sqrt{3}\frac{Gm^2}{L^2} $$

---

### 20. Numerical Net Force
- Using the values supplied in the lecture:
  $$ F_{\mathrm{net}}\approx2.2\times10^{26}\ \mathrm{N} $$
- This is approximately:
  $$ 220\ \mathrm{YN} $$

---

### 21. Orbital Radius of Each Mass
- Let $R$ be the distance from a vertex to the common center.
- From the triangle geometry:
  $$ \cos(30^\circ)=\frac{L/2}{R} $$
- Therefore:
  $$ R=\frac{L}{2\cos(30^\circ)} $$
- Simplify:
  $$ R=\frac{L}{\sqrt{3}} $$

---

### 22. Find the Orbital Speed
- Take inward as positive and set the net gravitational force equal to the radial-acceleration requirement:
  $$ \sum F_r=m a_r=m\frac{v^2}{R}=F_{\mathrm{net}}=\sqrt{3}\frac{Gm^2}{L^2} $$
- Substitute:
  $$ R=\frac{L}{\sqrt{3}} $$
- Then:
  $$ m\frac{v^2}{L/\sqrt{3}}
  =
  \sqrt{3}\frac{Gm^2}{L^2} $$

---

### 23. Simplify the Speed Expression
- Cancel the common factors:
  $$ v^2=\frac{Gm}{L} $$
- Therefore:
  $$ v=\sqrt{\frac{Gm}{L}} $$

---

### 24. Numerical Orbital Speed
- Using the lecture’s values:
  $$ v\approx9.7\times10^3\ \mathrm{m}/\mathrm{s} $$
- Equivalently:
  $$ v\approx9700\ \mathrm{m}/\mathrm{s} $$

---

## Total Energy of the Three-Mass System

### 25. Total Mechanical Energy
- The total mechanical energy is:
  $$ E_{\mathrm{total}}=K_{\mathrm{total}}+U_{\mathrm{total}} $$

---

### 26. Total Kinetic Energy
- Each of the three masses has kinetic energy:
  $$ K_i=\frac{1}{2}mv^2 $$
- Therefore:
  $$ K_{\mathrm{total}}
  =
  3\left(\frac{1}{2}mv^2\right) $$
- Using:
  $$ v^2=\frac{Gm}{L} $$
- We get:
  $$ K_{\mathrm{total}}
  =
  \frac{3}{2}\frac{Gm^2}{L} $$

---

### 27. Counting the Gravitational Pairs
- With three masses, there are three distinct pairs:
  $$ (1,2),\qquad(1,3),\qquad(2,3) $$
- Each pair is separated by $L$.
- Each pair contributes:
  $$ U_{\mathrm{pair}}=-\frac{Gm^2}{L} $$

---

### 28. Total Gravitational Potential Energy
- Add the three pair energies:
  $$ U_{\mathrm{total}}
  =
  -3\frac{Gm^2}{L} $$

---

### 29. Total Energy
- Combine kinetic and potential energy:
  $$ E_{\mathrm{total}}
  =
  \frac{3}{2}\frac{Gm^2}{L}
  -
  3\frac{Gm^2}{L} $$
- Therefore:
  $$ E_{\mathrm{total}}
  =
  -\frac{3}{2}\frac{Gm^2}{L} $$

---

### 30. Numerical Total Energy
- Using the values from the lecture:
  $$ E_{\mathrm{total}}
  \approx
  -3.5\times10^{38}\ \mathrm{J} $$

---

### 31. Meaning of the Negative Energy
- The potential-energy magnitude is larger than the kinetic energy:
  $$ |U_{\mathrm{total}}|>K_{\mathrm{total}} $$
- Therefore:
  $$ E_{\mathrm{total}}<0 $$
- A negative total mechanical energy indicates that the system is gravitationally bound.
- Energy must be added to separate all three masses to infinite distance.

---

### 32. Main Physics Takeaways
- Binary stars orbit their common center of mass.
- For a binary circular orbit:
  $$ T=2\pi\sqrt{\frac{d^3}{G(M+m)}} $$
- Symmetry can simplify multi-body gravitational-force calculations.
- For three identical masses at the vertices of an equilateral triangle:
  $$ F_{\mathrm{net}}
  =
  \sqrt{3}\frac{Gm^2}{L^2} $$
  $$ R=\frac{L}{\sqrt{3}} $$
  $$ v=\sqrt{\frac{Gm}{L}} $$
  $$ E_{\mathrm{total}}
  =
  -\frac{3}{2}\frac{Gm^2}{L} $$

---

### 33. Main Problem-Solving Strategy
1. Identify the common center of mass.
2. Distinguish the separation between objects from each object’s orbital radius.
3. Draw a free-body diagram for one object.
4. Resolve forces into radial and tangential components.
5. Use symmetry to cancel components when possible.
6. Set:
   $$ \sum F_r=m a_r=m\frac{v^2}{R} $$
7. Count every unique gravitational pair once when calculating potential energy.
8. Solve symbolically before substituting numerical values.
9. Use the sign of the total energy to determine whether the system is bound.
