## Lecture Outline (Simple and Physical Pendulums)

### 1. Course Logistics
- Quiz 2 and Quiz 1X are being graded.
- Quiz 3 will cover:
  - oscillations
  - waves
- Students should begin preparing their Quiz 3 note sheet.
- Damping and driven oscillations will not appear on Quiz 3 or the final exam.
- Damping is addressed only through the homework in this shortened summer course.

---

## Pendulum Motion

### 2. Simple Pendulum Setup
- A simple pendulum consists of:
  - a point mass $m$
  - a massless string of length $L$
  - a fixed pivot
- The angular displacement from equilibrium is:
  $$ \theta $$
- The equilibrium position is directly below the pivot.

---

### 3. Forces on the Pendulum Bob
- Forces acting on the point mass:
  - tension force $F_T$ along the string
  - gravitational force:
    $$ F_g=mg $$
- The tension force $F_T$ points radially and therefore produces no torque about the pivot.
- The tangential component of gravity provides the restoring torque.

---

### 4. Restoring Torque
- The torque due to gravity is:
  $$ \tau_p=-mgL\sin\theta $$
- The negative sign indicates that the torque acts opposite the angular displacement and pulls the pendulum toward equilibrium.

---

### 5. Small-Angle Approximation
- For sufficiently small angles measured in radians:
  $$ \sin\theta\approx\theta $$
- Therefore:
  $$ \tau_p\approx-mgL\theta $$
- This approximation converts the pendulum equation into the equation of simple harmonic motion.

---

### 6. Rotational Equation of Motion
- Rotational dynamics gives:
  $$ \sum\tau_p=I_p\alpha $$
- Since:
  $$ \alpha=\frac{d^2\theta}{dt^2} $$
- The pendulum equation becomes:
  $$ I_p\frac{d^2\theta}{dt^2}=-mgL\theta $$

---

### 7. Connection to Simple Harmonic Motion
- Linear simple harmonic motion satisfies:
  $$ a(t)=-\omega^2x(t) $$
- The rotational analogue is:
  $$ \alpha(t)=-\omega^2\theta(t) $$
- Comparing with:
  $$ \alpha=-\frac{mgL}{I_p}\theta $$
- We obtain:
  $$ \omega^2=\frac{mgL}{I_p} $$

---

## General Physical-Pendulum Formula

### 8. Physical Pendulum
- A physical pendulum is an extended rigid object that oscillates about a pivot.
- Let:
  - $M$ be the total mass
  - $I_p$ be the moment of inertia about the pivot
  - $\ell$ be the distance from the pivot to the center of mass
- The restoring torque is:
  $$ \tau_p=-Mg\ell\sin\theta $$

---

### 9. Small-Angle Equation for a Physical Pendulum
- Using:
  $$ \sin\theta\approx\theta $$
- The equation of motion is:
  $$ I_p\frac{d^2\theta}{dt^2}=-Mg\ell\theta $$
- Rearranging:
  $$ \frac{d^2\theta}{dt^2}
     +\frac{Mg\ell}{I_p}\theta=0 $$

---

### 10. Angular Frequency
- Comparing with the standard SHM equation gives:
  $$ \omega=\sqrt{\frac{Mg\ell}{I_p}} $$

---

### 11. Period of a Physical Pendulum
- Since:
  $$ T=\frac{2\pi}{\omega} $$
- The general physical-pendulum period is:
  $$ T=2\pi\sqrt{\frac{I_p}{Mg\ell}} $$
- This result is valid under the small-angle approximation.

---

### 12. Important Notation
- In these problems:
  - $T$ represents the oscillation period
  - $\tau$ represents torque
  - $F_T$ represents tension force
  - $I_p$ represents moment of inertia about the pivot
  - $L$ may represent an object’s length
  - $\ell$ represents the distance from the pivot to the center of mass
- The meaning of a symbol must be determined from its context.

---

## Example 1: Simple Pendulum

### 13. Moment of Inertia
- For a point mass $m$ located a distance $L$ from the pivot:
  $$ I_p=mL^2 $$
- The center-of-mass distance is:
  $$ \ell=L $$

---

### 14. Simple-Pendulum Period
- Substitute into the physical-pendulum formula:
  $$ T=2\pi\sqrt{\frac{mL^2}{mgL}} $$
- Cancel $m$ and one factor of $L$:
  $$ T=2\pi\sqrt{\frac{L}{g}} $$

---

### 15. Simple-Pendulum Frequency
- Frequency is:
  $$ f=\frac{1}{T} $$
- Therefore:
  $$ f=\frac{1}{2\pi}\sqrt{\frac{g}{L}} $$
- The lecture’s numerical result is:
  $$ f\approx0.83\ \mathrm{Hz} $$

---

### 16. Effect of the Initial Angle
- The pendulum is released from an angle of approximately:
  $$ 11^\circ $$
- This value is used only to establish that the angle is small enough for:
  $$ \sin\theta\approx\theta $$
- Under the small-angle approximation, the period does not depend on the release angle.

---

## Example 2: Uniform Rod Pivoted at One End

### 17. Rod Properties
- Consider a uniform rod with:
  - mass $M$
  - length $L$
  - pivot at one end
- Moment of inertia about one end:
  $$ I_p=\frac{1}{3}ML^2 $$
- Center of mass is at the midpoint:
  $$ \ell=\frac{L}{2} $$

---

### 18. Period of the End-Pivoted Rod
- Substitute:
  $$ T
  =
  2\pi
  \sqrt{
  \frac{\frac{1}{3}ML^2}
       {Mg(L/2)}
  } $$
- Simplify:
  $$ T=2\pi\sqrt{\frac{2L}{3g}} $$
- The lecture’s numerical result is:
  $$ T\approx1.6\ \mathrm{s} $$

---

## Example 3: Uniform Rod Pivoted at $L/6$ from One End

### 19. Distance from the Pivot to the Center of Mass
- The rod’s center of mass is at:
  $$ \frac{L}{2} $$
- The pivot is at:
  $$ \frac{L}{6} $$
- Therefore:
  $$ \ell=\frac{L}{2}-\frac{L}{6}=\frac{L}{3} $$

---

### 20. Parallel-Axis Theorem
- Moment of inertia about the center of mass:
  $$ I_{\mathrm{cm}}=\frac{1}{12}ML^2 $$
- Parallel-axis theorem:
  $$ I_p=I_{\mathrm{cm}}+M\ell^2 $$
- Substitute:
  $$ I_p=\frac{1}{12}ML^2+M\left(\frac{L}{3}\right)^2 $$

---

### 21. Simplify the Moment of Inertia
- Therefore:
  $$ I_p
  =
  \left(\frac{1}{12}+\frac{1}{9}\right)ML^2 $$
- Using a common denominator:
  $$ I_p=\frac{7}{36}ML^2 $$

---

### 22. Period of the Offset-Pivot Rod
- Substitute into:
  $$ T=2\pi\sqrt{\frac{I_p}{Mg\ell}} $$
- Then:
  $$ T
  =
  2\pi
  \sqrt{
  \frac{\frac{7}{36}ML^2}
       {Mg(L/3)}
  } $$
- Simplify:
  $$ T=2\pi\sqrt{\frac{7L}{12g}} $$
- The lecture’s numerical result is:
  $$ T\approx1.3\ \mathrm{s} $$

---

## Example 4: Uniform Rod with a Point Mass

### 23. Composite Pendulum Setup
- A uniform rod has:
  - mass $m_r$
  - length $L$
- A point mass $m_p$ is attached to the rod’s lower end.
- The assembly pivots about the rod’s upper end.

---

### 24. Total Moment of Inertia
- Rod contribution:
  $$ I_r=\frac{1}{3}m_rL^2 $$
- Point-mass contribution:
  $$ I_p^{(\mathrm{point})}=m_pL^2 $$
- Total:
  $$ I_{\mathrm{total}}=I_r+I_p^{(\mathrm{point})} $$
- Therefore:
  $$ I_{\mathrm{total}}
  =
  \frac{1}{3}m_rL^2+m_pL^2
  =
  \frac{m_r+3m_p}{3}L^2 $$

---

### 25. Composite Center of Mass
- The rod’s center is at $L/2$, and the point mass is at $L$:
  $$
  \ell
  =
  \frac{m_r(L/2)+m_pL}{m_r+m_p}
  $$
- Simplify:
  $$
  \ell
  =
  \frac{m_r+2m_p}{2(m_r+m_p)}L
  $$

---

### 26. Period of the Rod–Point-Mass System
- The total mass is:
  $$ M=m_r+m_p $$
- Substitute into the physical-pendulum formula:
  $$
  T
  =
  2\pi
  \sqrt{
  \frac{I_{\mathrm{total}}}
       {(m_r+m_p)g\ell}
  }
  $$
- After simplification:
  $$
  T
  =
  2\pi
  \sqrt{
  \frac{2L(m_r+3m_p)}
       {3g(m_r+2m_p)}
  }
  $$
- The lecture’s numerical result is:
  $$ T\approx2.0\ \mathrm{s} $$

---

## Example 5: Uniform Rod with an Attached Disk

### 27. Composite Pendulum Setup
- A uniform rod has:
  - mass $m_r$
  - length $L$
- A solid disk has:
  - mass $m_d$
  - radius $R$
- The disk is attached to the lower end of the rod.
- The distance from the pivot to the disk’s center is:
  $$ L+R $$

---

### 28. Rod Moment of Inertia
- About the pivot at the rod’s upper end:
  $$ I_r=\frac{1}{3}m_rL^2 $$

---

### 29. Disk Moment of Inertia
- About the disk’s center:
  $$ I_{d,\mathrm{cm}}=\frac{1}{2}m_dR^2 $$
- Apply the parallel-axis theorem:
  $$ I_{d,p}=I_{d,\mathrm{cm}}+m_d(L+R)^2 $$
- Therefore:
  $$ I_{d,p}=\frac{1}{2}m_dR^2+m_d(L+R)^2 $$

---

### 30. Total Moment of Inertia
- Add the rod and disk contributions:
  $$
  I_{\mathrm{total}}
  =
  \frac{1}{3}m_rL^2
  +
  \frac{1}{2}m_dR^2
  +
  m_d(L+R)^2
  $$

---

### 31. Composite Center-of-Mass Distance
- The rod’s center is at $L/2$.
- The disk’s center is at $L+R$.
- Therefore:
  $$
  \ell
  =
  \frac{
  m_r(L/2)+m_d(L+R)
  }{
  m_r+m_d
  }
  $$

---

### 32. Period of the Rod–Disk System
- Substitute into:
  $$ T=2\pi\sqrt{\frac{I_{\mathrm{total}}}{(m_r+m_d)g\ell}} $$
- Since:
  $$
  (m_r+m_d)\ell
  =
  m_r\frac{L}{2}+m_d(L+R)
  $$
- The period can be written as:
  $$
  T
  =
  2\pi
  \sqrt{
  \frac{
  \frac{1}{3}m_rL^2
  +
  \frac{1}{2}m_dR^2
  +
  m_d(L+R)^2
  }{
  g\left[
  m_r(L/2)+m_d(L+R)
  \right]
  }
  }
  $$
- The lecture’s numerical result is:
  $$ T\approx2.5\ \mathrm{s} $$

---

### 33. Why the Disk’s Own Rotation Matters
- The disk is an extended object, not a point mass.
- Its moment of inertia has two contributions:
  - rotation about its own center:
    $$ \frac{1}{2}m_dR^2 $$
  - motion of its center around the pendulum pivot:
    $$ m_d(L+R)^2 $$
- Both contributions must be included.

---

### 34. Main Physics Takeaways
- A physical pendulum undergoes approximate simple harmonic motion when:
  $$ \sin\theta\approx\theta $$
- The general period is:
  $$ T=2\pi\sqrt{\frac{I_p}{Mg\ell}} $$
- The period depends on:
  - moment of inertia about the pivot
  - total mass
  - distance from the pivot to the center of mass
- The simple-pendulum result:
  $$ T=2\pi\sqrt{\frac{L}{g}} $$
  is a special case of the physical-pendulum formula.
- Moving the pivot changes both:
  $$ I_p $$
  and:
  $$ \ell $$
- For composite objects:
  $$ I_{\mathrm{total}}=\sum_i I_i $$
  and the combined center of mass must also be calculated.

---

### 35. Main Problem-Solving Strategy
1. Confirm that the small-angle approximation is appropriate.
2. Identify the pivot.
3. Calculate the total moment of inertia about that pivot.
4. Use the parallel-axis theorem when necessary:
   $$ I_p=I_{\mathrm{cm}}+Md^2 $$
5. Find the system’s combined center of mass.
6. Determine:
   $$ \ell=\text{distance from pivot to center of mass} $$
7. Substitute into:
   $$ T=2\pi\sqrt{\frac{I_p}{Mg\ell}} $$
8. Simplify symbolically before substituting numerical values.
