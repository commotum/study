## Lecture Outline (Center of Mass Continued and Introduction to Moment of Inertia)

### 1. Review of Center of Mass
- The center of mass is a **position**, not a point that divides an object into equal masses.
- An object supported at its center of mass will balance, assuming a uniform gravitational field.
- A freely rotating object naturally rotates about its center of mass.
- The center of mass depends on both:
  - the amount of mass
  - where that mass is located

---

### 2. Connection Between Balance and Torque
- Torque is defined as:
  $$ \vec{\tau}=\vec{r}\times\vec{F} $$
- Its magnitude is:
  $$ \tau=rF\sin\theta $$
- A balanced object has equal-magnitude clockwise and counterclockwise torques:
  $$ \sum\tau=0 $$
- The masses on opposite sides do not need to be equal because their distances from the support point may differ.

---

### 3. Center of Mass for Discrete Masses
- For a collection of point masses:
  $$ \vec{r}_{\mathrm{cm}}
  =
  \frac{\displaystyle\sum_i m_i\vec{r}_i}
       {\displaystyle\sum_i m_i} $$
- In one dimension:
  $$ x_{\mathrm{cm}}
  =
  \frac{\displaystyle\sum_i m_ix_i}
       {\displaystyle\sum_i m_i} $$

---

### 4. Center of Mass for a Continuous Object
- For a continuous mass distribution:
  $$ x_{\mathrm{cm}}=\frac{1}{M}\int x\,dm $$
- Here:
  - $M$ is the total mass
  - $dm$ is an infinitesimal mass element
  - $x$ is the position of that element

---

## Variable-Density Rod: Center of Mass

### 5. Linear Mass Density
- Consider a rod of length $L$ whose linear mass density varies with position:
  $$ \lambda(x)=Cx $$
- Linear mass density is:
  $$ \lambda(x)=\frac{dm}{dx} $$
- Therefore:
  $$ dm=\lambda(x)\,dx=Cx\,dx $$

---

### 6. Determine the Density Constant $C$
- The total mass is:
  $$ M=\int_0^L dm $$
- Substitute $dm=Cx\,dx$:
  $$ M=\int_0^L Cx\,dx $$
- Evaluate:
  $$ M=C\left[\frac{x^2}{2}\right]_0^L $$
  $$ M=\frac{CL^2}{2} $$
- Solve for $C$:
  $$ C=\frac{2M}{L^2} $$

---

### 7. Center of Mass of the Variable-Density Rod
- Start with:
  $$ x_{\mathrm{cm}}=\frac{1}{M}\int_0^L x\,dm $$
- Substitute:
  $$ dm=Cx\,dx $$
- Then:
  $$ x_{\mathrm{cm}}
  =
  \frac{1}{M}\int_0^L x(Cx)\,dx $$
  $$ x_{\mathrm{cm}}
  =
  \frac{C}{M}\int_0^L x^2\,dx $$

---

### 8. Evaluate the Center-of-Mass Integral
- Integrate:
  $$ x_{\mathrm{cm}}
  =
  \frac{C}{M}
  \left[\frac{x^3}{3}\right]_0^L $$
- Therefore:
  $$ x_{\mathrm{cm}}=\frac{CL^3}{3M} $$
- Substitute:
  $$ C=\frac{2M}{L^2} $$
- Result:
  $$ x_{\mathrm{cm}}=\frac{2L}{3} $$

---

### 9. Numerical Center-of-Mass Result
- For:
  $$ L=1.8\ \mathrm{m} $$
- The center of mass is:
  $$ x_{\mathrm{cm}}=\frac{2}{3}(1.8\ \mathrm{m}) $$
  $$ x_{\mathrm{cm}}=1.2\ \mathrm{m} $$
- This is physically reasonable because the rod has more mass toward the right side.

---

### 10. Physical-Reasoning Check
- The center of mass should lie:
  - within the rod
  - to the right of the midpoint
- Since:
  $$ \lambda(x)=Cx $$
  increases with $x$, the right side has greater mass density.
- Therefore:
  $$ \frac{L}{2}<x_{\mathrm{cm}}<L $$

---

## Introduction to Moment of Inertia

### 11. Rotational Kinetic Energy of Point Masses
- Consider a rigid object made from many small masses $m_i$.
- Its rotational kinetic energy is:
  $$ K_{\mathrm{rot}}
  =
  \sum_i \frac{1}{2}m_iv_i^2 $$
- For rigid rotation:
  $$ v_i=\omega r_{\perp,i} $$
- Therefore:
  $$ K_{\mathrm{rot}}
  =
  \sum_i \frac{1}{2}m_i(\omega r_{\perp,i})^2 $$

---

### 12. Define Moment of Inertia
- Factor out $\omega^2$:
  $$ K_{\mathrm{rot}}
  =
  \frac{1}{2}
  \left(\sum_i m_ir_{\perp,i}^2\right)\omega^2 $$
- Define the moment of inertia:
  $$ I=\sum_i m_ir_{\perp,i}^2 $$
- Then:
  $$ K_{\mathrm{rot}}=\frac{1}{2}I\omega^2 $$

---

### 13. Continuous Form of Moment of Inertia
- For a continuous mass distribution:
  $$ I=\int r_\perp^2\,dm $$
- Moment of inertia depends on:
  - total mass
  - how far each mass element is from the rotation axis
- Distance is weighted by:
  $$ r_\perp^2 $$

---

### 14. Units of Moment of Inertia
- From:
  $$ I=\int r_\perp^2\,dm $$
- The units are:
  $$ [I]=\mathrm{kg}\,\mathrm{m}^2 $$
- Moment of inertia has no special named SI unit.

---

### 15. Physical Meaning of Moment of Inertia
- Moment of inertia measures how difficult it is to change an object’s rotational motion.
- A larger moment of inertia means:
  - more energy is stored for the same angular speed
  - more torque is required to produce the same angular acceleration
- Moving mass farther from the rotation axis increases $I$ significantly because of the $r^2$ dependence.

---

## Uniform Thin Rod About Its Center

### 16. Rod Setup
- Consider a uniform thin rod:
  - mass $M$
  - length $L$
  - rotation axis through its center and perpendicular to the rod
- Linear density:
  $$ \lambda=\frac{M}{L} $$
- Mass element:
  $$ dm=\lambda\,dx=\frac{M}{L}\,dx $$

---

### 17. Moment-of-Inertia Integral About the Center
- Choose the origin at the center:
  $$ -\frac{L}{2}\le x\le\frac{L}{2} $$
- Then:
  $$ I_{\mathrm{cm}}
  =
  \int_{-L/2}^{L/2}x^2\,dm $$
- Substitute $dm$:
  $$ I_{\mathrm{cm}}
  =
  \frac{M}{L}
  \int_{-L/2}^{L/2}x^2\,dx $$

---

### 18. Evaluate the Integral
- Integrate:
  $$ I_{\mathrm{cm}}
  =
  \frac{M}{L}
  \left[\frac{x^3}{3}\right]_{-L/2}^{L/2} $$
- Result:
  $$ I_{\mathrm{cm}}=\frac{1}{12}ML^2 $$

---

## Uniform Thin Rod About One End

### 19. Moment-of-Inertia Integral About the End
- Move the rotation axis to one end of the rod:
  $$ 0\le x\le L $$
- Then:
  $$ I_{\mathrm{end}}
  =
  \frac{M}{L}\int_0^Lx^2\,dx $$

---

### 20. Evaluate the End-Axis Integral
- Integrate:
  $$ I_{\mathrm{end}}
  =
  \frac{M}{L}
  \left[\frac{x^3}{3}\right]_0^L $$
- Result:
  $$ I_{\mathrm{end}}=\frac{1}{3}ML^2 $$

---

### 21. Comparing the Two Rotation Axes
- About the center:
  $$ I_{\mathrm{cm}}=\frac{1}{12}ML^2 $$
- About the end:
  $$ I_{\mathrm{end}}=\frac{1}{3}ML^2 $$
- Therefore:
  $$ I_{\mathrm{end}}=4I_{\mathrm{cm}} $$
- Rotating the rod about its end is more difficult because more of its mass lies farther from the axis.

---

## Parallel-Axis Theorem

### 22. General Formula
- The parallel-axis theorem is:
  $$ I=I_{\mathrm{cm}}+Md^2 $$
- Here:
  - $I_{\mathrm{cm}}$ is the moment of inertia about a parallel axis through the center of mass
  - $M$ is total mass
  - $d$ is the distance between the two parallel axes

---

### 23. Apply the Theorem to the Rod About Its End
- For a rod, the center-to-end distance is:
  $$ d=\frac{L}{2} $$
- Therefore:
  $$ I_{\mathrm{end}}
  =
  \frac{1}{12}ML^2
  +
  M\left(\frac{L}{2}\right)^2 $$
- Simplify:
  $$ I_{\mathrm{end}}
  =
  \frac{1}{12}ML^2+\frac{1}{4}ML^2 $$
  $$ I_{\mathrm{end}}
  =
  \frac{4}{12}ML^2 $$
- Result:
  $$ I_{\mathrm{end}}=\frac{1}{3}ML^2 $$

---

## Variable-Density Rod: Moment of Inertia

### 24. Moment of Inertia About the Left End
- Return to the rod with:
  $$ \lambda(x)=Cx $$
- Moment of inertia about the origin at the left end:
  $$ I=\int_0^Lx^2\,dm $$
- Substitute:
  $$ dm=Cx\,dx $$
- Then:
  $$ I=\int_0^Lx^2(Cx)\,dx $$
  $$ I=C\int_0^Lx^3\,dx $$

---

### 25. Evaluate the Integral
- Integrate:
  $$ I=C\left[\frac{x^4}{4}\right]_0^L $$
- Therefore:
  $$ I=\frac{CL^4}{4} $$
- Substitute:
  $$ C=\frac{2M}{L^2} $$
- Result:
  $$ I=\frac{1}{2}ML^2 $$

---

### 26. Numerical Moment of Inertia
- Given:
  $$ M=0.65\ \mathrm{kg} $$
  $$ L=1.8\ \mathrm{m} $$
- Compute:
  $$ I=\frac{1}{2}(0.65)(1.8)^2 $$
- Result:
  $$ I\approx1.1\ \mathrm{kg}\,\mathrm{m}^2 $$

---

## Uniform Rod Rotating One-Third of the Way from an End

### 27. Problem Setup
- A uniform rod of mass $M$ and length $L$ rotates about an axis located:
  $$ \frac{L}{3} $$
  from the left end.
- Relative to the new axis, the rod extends from:
  $$ -\frac{L}{3} $$
  to:
  $$ \frac{2L}{3} $$

---

### 28. Direct Integration
- Use:
  $$ I=\frac{M}{L}\int_{-L/3}^{2L/3}x^2\,dx $$
- Evaluate:
  $$ I=
  \frac{M}{L}
  \left[\frac{x^3}{3}\right]_{-L/3}^{2L/3} $$
- Therefore:
  $$
  I=
  \frac{M}{3L}
  \left[
  \left(\frac{2L}{3}\right)^3
  -
  \left(-\frac{L}{3}\right)^3
  \right]
  $$

---

### 29. Simplify the Result
- Compute the powers:
  $$ \left(\frac{2L}{3}\right)^3=\frac{8L^3}{27} $$
  $$ \left(-\frac{L}{3}\right)^3=-\frac{L^3}{27} $$
- Then:
  $$ I=
  \frac{M}{3L}
  \left(\frac{9L^3}{27}\right) $$
- Result:
  $$ I=\frac{1}{9}ML^2 $$

---

### 30. Verify with the Parallel-Axis Theorem
- The rod’s center is at:
  $$ \frac{L}{2} $$
- The new axis is at:
  $$ \frac{L}{3} $$
- Their separation is:
  $$ d=\frac{L}{2}-\frac{L}{3}=\frac{L}{6} $$
- Apply:
  $$ I=I_{\mathrm{cm}}+Md^2 $$
- Therefore:
  $$ I=
  \frac{1}{12}ML^2
  +
  M\left(\frac{L}{6}\right)^2 $$
- Simplify:
  $$ I=\frac{1}{12}ML^2+\frac{1}{36}ML^2 $$
  $$ I=\frac{1}{9}ML^2 $$

---

## Composite Object: Rod and Point Mass

### 31. Problem Setup
- A uniform rod has:
  - mass $M$
  - length $L$
- A point mass of:
  $$ 3M $$
  is attached to the far end.
- The object rotates about the opposite end of the rod.

---

### 32. Add the Moments of Inertia
- The total moment of inertia is:
  $$ I_{\mathrm{total}}=I_{\mathrm{rod}}+I_{\mathrm{point}} $$
- Rod about one end:
  $$ I_{\mathrm{rod}}=\frac{1}{3}ML^2 $$
- Point mass at distance $L$:
  $$ I_{\mathrm{point}}=(3M)L^2 $$

---

### 33. Final Composite Moment of Inertia
- Add:
  $$ I_{\mathrm{total}}
  =
  \frac{1}{3}ML^2+3ML^2 $$
- Therefore:
  $$ I_{\mathrm{total}}=\frac{10}{3}ML^2 $$

---

### 34. Standard Moments of Inertia
- The lecture recommends knowing or recording standard results for common shapes.
- Examples introduced here:
  - thin rod about its center:
    $$ I=\frac{1}{12}ML^2 $$
  - thin rod about one end:
    $$ I=\frac{1}{3}ML^2 $$
- More common shapes will include:
  - disks
  - cylinders
  - hoops
  - solid spheres
  - spherical shells

---

### 35. Main Physics Takeaways
- Center of mass is a mass-weighted average position:
  $$ x_{\mathrm{cm}}=\frac{1}{M}\int x\,dm $$
- Moment of inertia is a mass-weighted average of squared distance from an axis:
  $$ I=\int r_\perp^2\,dm $$
- Rotational kinetic energy is:
  $$ K_{\mathrm{rot}}=\frac{1}{2}I\omega^2 $$
- Moving the rotation axis away from the center of mass increases the moment of inertia:
  $$ I=I_{\mathrm{cm}}+Md^2 $$
- Composite moments of inertia can be added:
  $$ I_{\mathrm{total}}=\sum_i I_i $$

---

### 36. Main Problem-Solving Takeaways
- Clearly identify the rotation axis before calculating $I$.
- Measure every $r_\perp$ from that axis.
- Convert mass density into a mass element:
  $$ dm=\lambda(x)\,dx $$
- Solve symbolically before inserting numerical values.
- Check the units:
  $$ [I]=\mathrm{kg}\,\mathrm{m}^2 $$
- Use the parallel-axis theorem when the axis is parallel to one through the center of mass.
