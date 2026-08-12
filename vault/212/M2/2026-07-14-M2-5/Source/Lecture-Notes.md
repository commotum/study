
## Lecture Outline (Rolling Motion, Angular Momentum, and Rotational Collisions)

### 1. Course and Quiz Logistics
- Quiz 1 scores have been posted.
- The optional Quiz 1X assignment asks students to address the quiz problem on which they lost the most points.
- Quiz 1X includes:
  - explaining the original reasoning
  - identifying what should have been done differently
  - providing a correct solution
  - completing unit analysis and covariational reasoning
  - discussing the problem with the instructor, a TA, or a Wormhole tutor
- Quiz 1X is due Friday at:
  $$ 6{:}00\text{ PM} $$
- Late submissions are not accepted.

---

### 2. Quiz 2 Schedule
- Proctorio version:
  $$ \text{Saturday at }5{:}00\text{ PM}
  \quad \text{to} \quad
  \text{Monday at }5{:}00\text{ PM} $$
- Zoom-proctored sessions on Monday:
  $$ 11{:}00\text{ AM} $$
  and:
  $$ 6{:}00\text{ PM} $$
- Students should begin preparing their handwritten Quiz 2 note sheet.

---

## Rolling Motion

### 3. Motion of a Point on a Rolling Wheel
- A point on the rim of a rolling wheel traces a **cycloid**.
- After one complete wheel revolution, the center of mass moves forward by one circumference:
  $$ \Delta x=2\pi R $$
- Here, $R$ is the wheel radius.

---

### 4. Period and Angular Speed
- The period $T$ is the time required for one complete revolution.
- Angular speed is related to period by:
  $$ \omega=\frac{2\pi}{T} $$
- Equivalently:
  $$ T=\frac{2\pi}{\omega} $$

---

### 5. Rolling-Without-Slipping Condition
- The center-of-mass speed is:
  $$ v_{\mathrm{cm}}=\frac{\Delta x}{T} $$
- Using:
  $$ \Delta x=2\pi R $$
  and:
  $$ T=\frac{2\pi}{\omega} $$
- We obtain:
  $$ v_{\mathrm{cm}}
  =
  \frac{2\pi R}{2\pi/\omega}
  =
  \omega R $$
- Therefore, for rolling without slipping:
  $$ v_{\mathrm{cm}}=\omega R $$

---

### 6. Acceleration Relation for Rolling
- Differentiate:
  $$ v_{\mathrm{cm}}=\omega R $$
- If $R$ is constant:
  $$ a_{\mathrm{cm}}=\alpha R $$
- Thus:
  - translational speed relates to angular speed through $R$
  - translational acceleration relates to angular acceleration through $R$

---

## Hollow Sphere Rolling Down a Ramp

### 7. Problem Setup
- A hollow sphere has:
  - mass $m$
  - radius $R$
- It starts from rest and rolls without slipping down a ramp.
- Ramp information:
  - distance along ramp:
    $$ d $$
  - incline angle:
    $$ \theta $$
- Goal: find the speed of its center of mass at the bottom:
  $$ v_f $$

---

### 8. Modeling Assumptions
- The sphere starts from rest.
- The sphere rolls without slipping.
- Air resistance is neglected.
- Rolling resistance is assumed small enough that mechanical energy is approximately conserved.
- Static friction may enforce rolling, but it does not dissipate mechanical energy in the ideal no-slip model.

---

### 9. Conservation of Energy
- Begin with:
  $$ U_0+K_0=U_f+K_f+\Delta E_{\mathrm{th}} $$
- Under the idealized assumptions:
  $$ \Delta E_{\mathrm{th}}\approx0 $$
- Taking the bottom of the ramp as zero gravitational potential:
  $$ mgh
  =
  \frac{1}{2}mv_f^2
  +
  \frac{1}{2}I\omega_f^2 $$

---

### 10. Ramp Height
- From the ramp geometry:
  $$ \sin\theta=\frac{h}{d} $$
- Therefore:
  $$ h=d\sin\theta $$

---

### 11. Moment of Inertia of a Hollow Sphere
- For a thin spherical shell:
  $$ I=\frac{2}{3}mR^2 $$

---

### 12. Apply the Rolling Constraint
- Since the sphere rolls without slipping:
  $$ v_f=\omega_f R $$
- Therefore:
  $$ \omega_f=\frac{v_f}{R} $$
- Substitute into the rotational kinetic energy:
  $$
  \frac{1}{2}I\omega_f^2
  =
  \frac{1}{2}
  \left(\frac{2}{3}mR^2\right)
  \left(\frac{v_f}{R}\right)^2
  $$
- Simplify:
  $$ \frac{1}{2}I\omega_f^2=\frac{1}{3}mv_f^2 $$

---

### 13. Solve for the Final Speed
- Conservation of energy becomes:
  $$ mgd\sin\theta
  =
  \frac{1}{2}mv_f^2+\frac{1}{3}mv_f^2 $$
- Combine the kinetic-energy terms:
  $$ mgd\sin\theta=\frac{5}{6}mv_f^2 $$
- Cancel $m$:
  $$ gd\sin\theta=\frac{5}{6}v_f^2 $$
- Therefore:
  $$ v_f^2=\frac{6}{5}gd\sin\theta $$
- Final result:
  $$ v_f=\sqrt{\frac{6}{5}gd\sin\theta} $$

---

### 14. Numerical Result
- Substituting the values from the lecture gives approximately:
  $$ v_f\approx2.5\ \mathrm{m}/\mathrm{s} $$

---

### 15. Important Rolling-Energy Lesson
- A rolling object has two kinds of kinetic energy:
  $$ K_{\mathrm{total}}
  =
  K_{\mathrm{trans}}+K_{\mathrm{rot}} $$
- Specifically:
  $$ K_{\mathrm{total}}
  =
  \frac{1}{2}mv_{\mathrm{cm}}^2
  +
  \frac{1}{2}I\omega^2 $$
- Neglecting rotational kinetic energy would give an incorrect final speed.

---

## Angular Momentum

### 16. Translational Momentum Review
- Linear momentum is:
  $$ \vec{p}=m\vec{v} $$
- Newton’s second law can be written as:
  $$ \sum\vec{F}_{\mathrm{ext}}=\frac{d\vec{p}}{dt} $$

---

### 17. Angular Momentum of a Particle
- Angular momentum is defined as:
  $$ \vec{L}=\vec{r}\times\vec{p} $$
- Since:
  $$ \vec{p}=m\vec{v} $$
- We may write:
  $$ \vec{L}=m\vec{r}\times\vec{v} $$
- Magnitude:
  $$ L=mrv\sin\phi $$
- If $\vec{r}$ and $\vec{v}$ are perpendicular:
  $$ L=mrv $$

---

### 18. Torque and Angular Momentum
- The rotational analogue of:
  $$ \sum\vec{F}=\frac{d\vec{p}}{dt} $$
  is:
  $$ \sum\vec{\tau}_{\mathrm{ext}}
  =
  \frac{d\vec{L}}{dt} $$

---

### 19. Angular Momentum of a Rigid Body
- For a rigid body rotating about a fixed axis:
  $$ L=I\omega $$
- Here:
  - $I$ is the moment of inertia about the rotation axis
  - $\omega$ is the angular velocity

---

### 20. Conservation of Angular Momentum
- If the net external torque about the chosen axis is zero:
  $$ \sum\vec{\tau}_{\mathrm{ext}}=0 $$
- Then:
  $$ \frac{d\vec{L}}{dt}=0 $$
- Therefore:
  $$ \vec{L}_i=\vec{L}_f $$
- For fixed-axis rotation:
  $$ I_i\omega_i=I_f\omega_f $$

---

## Rain Falling into Rotating Cups

### 21. Problem Setup
- Two identical cups rotate about a central axis.
- Initially:
  - each cup has mass $m$
  - the cups are separated by distance $d$
  - each cup is a distance:
    $$ \frac{d}{2} $$
    from the axis
  - angular speed is:
    $$ \omega_0 $$
- Rain enters each cup, doubling each cup’s mass:
  $$ m\to2m $$
- Goal: find the final angular speed:
  $$ \omega_f $$

---

### 22. Why Angular Momentum Is Conserved
- There is no significant external torque about the central rotation axis.
- The incoming rain is assumed to add no initial angular momentum about that axis.
- Therefore:
  $$ L_0=L_f $$

---

### 23. Initial Moment of Inertia
- Treat both cups as point masses:
  $$
  I_0
  =
  m\left(\frac{d}{2}\right)^2
  +
  m\left(\frac{d}{2}\right)^2
  $$
- Simplify:
  $$ I_0=\frac{1}{2}md^2 $$

---

### 24. Final Moment of Inertia
- Each cup now has mass $2m$:
  $$
  I_f
  =
  2m\left(\frac{d}{2}\right)^2
  +
  2m\left(\frac{d}{2}\right)^2
  $$
- Simplify:
  $$ I_f=md^2 $$

---

### 25. Final Angular Speed
- Apply conservation of angular momentum:
  $$ I_0\omega_0=I_f\omega_f $$
- Substitute:
  $$ \left(\frac{1}{2}md^2\right)\omega_0
  =
  (md^2)\omega_f $$
- Cancel $m$ and $d^2$:
  $$ \omega_f=\frac{\omega_0}{2} $$

---

### 26. Numerical Result
- If:
  $$ \omega_0=4.2\ \mathrm{rad}/\mathrm{s} $$
- Then:
  $$ \omega_f=2.1\ \mathrm{rad}/\mathrm{s} $$

---

### 27. Covariational Interpretation
- The moment of inertia increases when additional mass is added at the same radius.
- Since angular momentum is conserved:
  $$ I\omega=\text{constant} $$
- Increasing $I$ causes $\omega$ to decrease.

---

## Mechanical Energy Lost in the Rain-Cup Collision

### 28. Angular Momentum vs. Mechanical Energy
- Angular momentum is conserved because the net external torque is zero.
- Mechanical energy is not conserved because the rain sticks to the cups.
- This is a completely inelastic rotational interaction.

---

### 29. Initial Rotational Kinetic Energy
- Initial kinetic energy:
  $$ K_0=\frac{1}{2}I_0\omega_0^2 $$
- Substitute:
  $$ I_0=\frac{1}{2}md^2 $$
- Therefore:
  $$ K_0=\frac{1}{4}md^2\omega_0^2 $$

---

### 30. Final Rotational Kinetic Energy
- Final kinetic energy:
  $$ K_f=\frac{1}{2}I_f\omega_f^2 $$
- Using:
  $$ I_f=md^2 $$
  and:
  $$ \omega_f=\frac{\omega_0}{2} $$
- Then:
  $$
  K_f
  =
  \frac{1}{2}(md^2)
  \left(\frac{\omega_0}{2}\right)^2
  $$
- Simplify:
  $$ K_f=\frac{1}{8}md^2\omega_0^2 $$

---

### 31. Thermal-Energy Increase
- The mechanical energy converted to thermal/internal energy is:
  $$ \Delta E_{\mathrm{th}}=K_0-K_f $$
- Substitute:
  $$ \Delta E_{\mathrm{th}}
  =
  \frac{1}{4}md^2\omega_0^2
  -
  \frac{1}{8}md^2\omega_0^2 $$
- Therefore:
  $$ \Delta E_{\mathrm{th}}
  =
  \frac{1}{8}md^2\omega_0^2 $$

---

### 32. Numerical Result
- Using the values from the lecture:
  $$ \Delta E_{\mathrm{th}}\approx0.47\ \mathrm{J} $$

---

## Bullet Embedding in a Solid Cylinder

### 33. Problem Setup
- A solid uniform cylinder has:
  - mass $M$
  - radius $R$
  - initial angular speed:
    $$ 0 $$
- A bullet has:
  - mass $m$
  - speed $v$
- The bullet strikes tangentially and embeds in the cylinder’s rim.
- Goal: find the final angular speed:
  $$ \omega_f $$

---

### 34. Conservation Principle
- During the short collision, the net external torque about the spindle axis is assumed negligible.
- Therefore:
  $$ L_i=L_f $$
- Mechanical energy is not conserved because the bullet embeds in the cylinder.

---

### 35. Initial Angular Momentum
- The cylinder is initially at rest.
- The bullet’s velocity is perpendicular to the radius at impact.
- Therefore:
  $$ L_i=mRv $$

---

### 36. Final Moment of Inertia
- The cylinder’s moment of inertia is:
  $$ I_{\mathrm{cyl}}=\frac{1}{2}MR^2 $$
- Treat the embedded bullet as a point mass at radius $R$:
  $$ I_{\mathrm{bullet}}=mR^2 $$
- Total final moment of inertia:
  $$ I_f=\frac{1}{2}MR^2+mR^2 $$

---

### 37. Solve for the Final Angular Speed
- Apply:
  $$ L_i=L_f $$
- Therefore:
  $$ mRv
  =
  \left(
  \frac{1}{2}MR^2+mR^2
  \right)\omega_f $$
- Solve:
  $$
  \omega_f
  =
  \frac{mRv}
  {\frac{1}{2}MR^2+mR^2}
  $$
- Factor $R^2$:
  $$
  \omega_f
  =
  \frac{mv}
  {R\left(\frac{M}{2}+m\right)}
  $$

---

### 38. Numerical Result
- Substituting the values from the lecture gives:
  $$ \omega_f\approx0.95\ \mathrm{rad}/\mathrm{s} $$

---

### 39. Main Physics Takeaways
- Rolling without slipping:
  $$ v_{\mathrm{cm}}=\omega R $$
  $$ a_{\mathrm{cm}}=\alpha R $$
- Total kinetic energy of a rolling object:
  $$ K=
  \frac{1}{2}mv_{\mathrm{cm}}^2
  +
  \frac{1}{2}I\omega^2 $$
- Angular momentum:
  $$ \vec{L}=\vec{r}\times\vec{p} $$
- For fixed-axis rigid-body rotation:
  $$ L=I\omega $$
- Angular momentum is conserved when:
  $$ \sum\vec{\tau}_{\mathrm{ext}}=0 $$
- Angular momentum may be conserved even when mechanical energy is not.

---

### 40. Main Problem-Solving Strategy
1. Identify the rotation axis.
2. Determine whether the net external torque about that axis is zero.
3. Choose the appropriate angular-momentum expression:
   $$ \vec{L}=\vec{r}\times\vec{p} $$
   or:
   $$ L=I\omega $$
4. Calculate the initial and final moments of inertia.
5. Apply:
   $$ L_i=L_f $$
6. Treat sticking collisions as mechanically inelastic.
7. Use energy conservation for ideal rolling problems, including both translational and rotational kinetic energy.
8. Solve symbolically before substituting numerical values.
