## Lecture Outline (Center of Mass, Torque Balance, and Mass Density)

### 1. Course and Quiz Logistics
- Quiz 1 has ended, and the course is beginning Quiz 2 material.
- Quiz 2 focuses on:
  - rigid-body rotational motion
  - center of mass
  - torque
  - moment of inertia

---

### 2. Quiz Note Sheets
- Each quiz and the final exam require a handwritten note sheet.
- Quiz 2 note-sheet requirements:
  - between half a page and one full page
  - handwritten in the student’s own handwriting
  - no photocopied or printed material
  - photo ID placed on top when scanned and submitted
- The Quiz 1 note sheet may also be used during Quiz 2, so Quiz 2 notes do not need to repeat all earlier material.

---

### 3. Quiz 1 Extra Credit
- The Quiz 1 extra-credit assignment opens after Quiz 1 is graded.
- Students choose the problem where they lost the most points and discuss:
  - why they used their original approach
  - which physics concepts led to their mistakes
  - what they should have done
  - the correct solution
- Students must also meet with the instructor or a TA to discuss the problem.
- Up to $12$ points may be recovered:
  - up to $8$ points from the written reflection, capped by points lost
  - up to $4$ points for meeting with someone

---

## Center of Mass and Balance

### 4. Teeter-Totter Motivation
- A small person and a larger person can balance on opposite sides of a teeter-totter.
- The larger person must sit closer to the fulcrum.
- The masses on the two sides do not need to be equal.
- What must balance are the clockwise and counterclockwise torques.

---

### 5. Torque
- Torque is defined by:
  $$ \vec{\tau}=\vec{r}\times\vec{F} $$
- Its magnitude is:
  $$ \tau=rF\sin\theta $$
- Here:
  - $\vec{r}$ points from the rotation axis to the force application point
  - $\vec{F}$ is the applied force
  - $\theta$ is the angle between $\vec{r}$ and $\vec{F}$

---

### 6. Torque from Weight
- For a mass supported on a horizontal teeter-totter:
  $$ F=mg $$
- Since the position vector and weight are perpendicular:
  $$ \theta=90^\circ $$
- Therefore:
  $$ \tau=rmg $$

---

### 7. Balance Condition
- For two masses on opposite sides of a fulcrum, equilibrium requires:
  $$ |\tau_1|=|\tau_2| $$
- Therefore:
  $$ m_1gr_1=m_2gr_2 $$
- Canceling $g$:
  $$ m_1r_1=m_2r_2 $$
- A larger mass must be placed at a smaller distance from the fulcrum.

---

### 8. Center of Mass Interpretation
- A system can balance when supported at its center of mass.
- A freely rotating object rotates about its center of mass.
- The center of mass is a position, not an amount of mass.
- Its units are units of length, such as:
  $$ \mathrm{m},\quad \mathrm{cm} $$

---

### 9. Center of Mass for Discrete Masses
- For point masses:
  $$ \vec{r}_{\mathrm{cm}}
  =
  \frac{\displaystyle\sum_i m_i\vec{r}_i}
       {\displaystyle\sum_i m_i} $$
- In one dimension:
  $$ x_{\mathrm{cm}}
  =
  \frac{\displaystyle\sum_i m_ix_i}
       {\displaystyle\sum_i m_i} $$
- Expanded for two masses:
  $$ x_{\mathrm{cm}}
  =
  \frac{m_1x_1+m_2x_2}{m_1+m_2} $$

---

### 10. Center of Mass for a Continuous Object
- For a continuously distributed mass:
  $$ x_{\mathrm{cm}}=\frac{1}{M}\int x\,dm $$
- Here:
  - $M$ is the total mass
  - $dm$ is a small mass element
  - $x$ is the position of that mass element

---

## Example 1: Two Point Masses

### 11. Problem Setup
- Two point masses are separated by distance $L$.
- The origin is placed at $m_1$:
  $$ x_1=0,\qquad x_2=L $$
- Their masses satisfy:
  $$ m_1=3m_2 $$

---

### 12. Center of Mass Calculation
- Use:
  $$ x_{\mathrm{cm}}
  =
  \frac{m_1x_1+m_2x_2}{m_1+m_2} $$
- Substitute:
  $$ x_{\mathrm{cm}}
  =
  \frac{m_1(0)+m_2L}{m_1+m_2} $$
- Since $m_1=3m_2$:
  $$ x_{\mathrm{cm}}
  =
  \frac{m_2L}{3m_2+m_2} $$
- Therefore:
  $$ x_{\mathrm{cm}}=\frac{L}{4} $$

---

### 13. Numerical Result
- For:
  $$ L=0.88\ \mathrm{m} $$
- The center of mass is:
  $$ x_{\mathrm{cm}}=\frac{0.88}{4}=0.22\ \mathrm{m} $$
- It lies closer to the larger mass $m_1$.

---

### 14. Equivalent Torque Method
- If the support is at $x=x_{\mathrm{cm}}$, the lever arms are:
  $$ r_1=x_{\mathrm{cm}} $$
  $$ r_2=L-x_{\mathrm{cm}} $$
- Torque balance gives:
  $$ m_1g x_{\mathrm{cm}}
  =
  m_2g(L-x_{\mathrm{cm}}) $$
- Cancel $g$ and solve:
  $$ (m_1+m_2)x_{\mathrm{cm}}=m_2L $$
- Therefore:
  $$ x_{\mathrm{cm}}=\frac{m_2L}{m_1+m_2} $$
- This matches the center-of-mass formula.

---

## Example 2: Arrangement of Identical Blocks

### 15. Treating Groups as Point Masses
- The system contains $10$ identical blocks, each of mass $m$.
- Because the blocks have uniform density, each group may be represented by:
  - its total mass
  - its own center position

---

### 16. Grouped Masses and Positions
- First group:
  $$ 6m \text{ at } x=1.5\ \mathrm{cm} $$
- Second group:
  $$ 2m \text{ at } x=4.0\ \mathrm{cm} $$
- Third group:
  $$ 2m \text{ at } x=5.5\ \mathrm{cm} $$

---

### 17. Center of Mass Calculation
- Use:
  $$
  x_{\mathrm{cm}}
  =
  \frac{
  6m(1.5)+2m(4.0)+2m(5.5)
  }{10m}
  $$
- Cancel $m$:
  $$
  x_{\mathrm{cm}}
  =
  \frac{9+8+11}{10}\ \mathrm{cm}
  $$
- Therefore:
  $$ x_{\mathrm{cm}}=2.8\ \mathrm{cm} $$

---

### 18. Main Lesson from the Block Example
- Identical objects may be grouped together to simplify the calculation.
- Each group is represented by a point mass at that group’s center of mass.
- This avoids summing every individual block separately.

---

## Example 3: Two Attached Cubes

### 19. Composite Object Setup
- The object consists of:
  - a large cube with side length $2L$
  - a smaller cube with side length $L$
- Both cubes have uniform volume mass density:
  $$ \rho=\frac{m}{V} $$
- Therefore:
  $$ m=\rho V $$

---

### 20. Expected Center-of-Mass Location
- The origin is at the left side of the large cube.
- The center of mass should lie between:
  $$ L<x_{\mathrm{cm}}<2L $$
- It must be to the right of the large cube’s center because the smaller cube adds mass on the right.

---

### 21. Mass of the Large Cube
- The volume is:
  $$ V_1=(2L)^3=8L^3 $$
- Therefore:
  $$ m_1=8\rho L^3 $$

---

### 22. Mass of the Small Cube
- The volume is:
  $$ V_2=L^3 $$
- Therefore:
  $$ m_2=\rho L^3 $$

---

### 23. Positions of the Individual Centers
- Center of the large cube:
  $$ x_1=L $$
- The small cube begins at $x=2L$, so its center is:
  $$ x_2=2L+\frac{L}{2}=\frac{5L}{2} $$

---

### 24. Composite Center of Mass
- Use:
  $$ x_{\mathrm{cm}}
  =
  \frac{m_1x_1+m_2x_2}{m_1+m_2} $$
- Substitute:
  $$
  x_{\mathrm{cm}}
  =
  \frac{
  (8\rho L^3)(L)
  +
  (\rho L^3)\left(\frac{5L}{2}\right)
  }{
  8\rho L^3+\rho L^3
  }
  $$

---

### 25. Simplify the Result
- Cancel $\rho L^3$:
  $$
  x_{\mathrm{cm}}
  =
  \frac{8L+\frac{5L}{2}}{9}
  $$
- Combine:
  $$
  x_{\mathrm{cm}}
  =
  \frac{\frac{16L}{2}+\frac{5L}{2}}{9}
  =
  \frac{21L}{18}
  $$
- Therefore:
  $$ x_{\mathrm{cm}}=\frac{7L}{6} $$
- The lecture’s numerical value is approximately:
  $$ x_{\mathrm{cm}}\approx0.875\ \mathrm{m} $$

---

## Variable Linear Mass Density

### 26. Linear Mass Density
- Linear mass density is mass per unit length:
  $$ \lambda(x)=\frac{dm}{dx} $$
- Therefore:
  $$ dm=\lambda(x)\,dx $$

---

### 27. Rod with Position-Dependent Density
- A rod has:
  - total length $L$
  - total mass $M$
  - linear mass density:
    $$ \lambda(x)=Cx $$
- The rod becomes more massive per unit length as $x$ increases.
- Goal:
  - determine the constant $C$

---

### 28. Total Mass from the Density
- Add all mass elements:
  $$ M=\int dm $$
- Substitute:
  $$ dm=\lambda(x)\,dx $$
- Therefore:
  $$ M=\int_0^L\lambda(x)\,dx $$

---

### 29. Substitute the Density Function
- Since:
  $$ \lambda(x)=Cx $$
- Then:
  $$ M=\int_0^L Cx\,dx $$

---

### 30. Evaluate the Integral
- Integrate:
  $$ M=C\left[\frac{x^2}{2}\right]_0^L $$
- Therefore:
  $$ M=\frac{CL^2}{2} $$

---

### 31. Solve for $C$
- Rearranging:
  $$ C=\frac{2M}{L^2} $$
- The units of $C$ are:
  $$ [C]=\mathrm{kg}/\mathrm{m}^2 $$
- The lecture’s numerical substitution gives:
  $$ C=0.40\ \mathrm{kg}/\mathrm{m}^2 $$

---

### 32. Main Physics Takeaways
- Center of mass is a weighted average of position:
  $$ x_{\mathrm{cm}}
  =
  \frac{\sum_i m_ix_i}{\sum_i m_i} $$
- For continuous distributions:
  $$ x_{\mathrm{cm}}=\frac{1}{M}\int x\,dm $$
- A balanced system has zero net torque:
  $$ \sum\tau=0 $$
- Equal torque does not require equal masses.
- The center of mass has units of position.
- Density functions connect small mass elements to geometry:
  $$ dm=\lambda(x)\,dx $$

---

### 33. Main Problem-Solving Takeaways
- Choose and clearly identify an origin.
- Measure every position from the same origin.
- Use symmetry or grouping when possible.
- Check whether the answer lies in a physically reasonable region.
- For continuous mass distributions:
  1. identify the density
  2. write $dm$ in terms of the spatial variable
  3. set the correct integration limits
  4. evaluate the integral
- The next lecture continues center-of-mass problems and introduces moment of inertia.
