## Lecture Outline (Circular Motion Dynamics: Flat Curves, Banked Curves, and Conical Pendulum)

### 1. Opening Course Logistics
- Quiz 1 is coming up soon.
- Proctorio version:
  $$ \text{opens Saturday at }5:00\text{ PM} $$
  $$ \text{closes Monday at }5:00\text{ PM} $$
- Zoom-proctored quiz options:
  $$ 11:00\text{ AM Monday} $$
  $$ 6:00\text{ PM Monday} $$
- Different quiz versions may be used, but they are intended to have the same difficulty level.
- Students need:
  - working webcam
  - visible face during the quiz
  - handwritten note sheet submitted before starting the quiz

---

### 2. Quiz 1 Notes Assignment
- A handwritten note sheet is required.
- It should be:
  - in the student’s own handwriting
  - at least half a page
  - no more than one full page
  - related to the quiz material
- The assignment deadline is listed as the first quiz opening time:
  $$ 5:00\text{ PM Saturday} $$
- However, as long as notes are submitted before the quiz begins, they will not be marked late.

---

## Circular Motion on a Flat Curve

### 3. Physical Setup: Car on a Level Circular Curve
- A car travels around a level circular curve.
- The curve is flat:
  - no banking
  - no hill
  - no slope
- The car moves in a circle, so it must have radial acceleration:
  $$ a_r=\frac{v^2}{r} $$

---

### 4. Free-Body Diagram for the Flat Curve
- Forces on the car:
  - gravitational force downward:
    $$ mg $$
  - normal force upward:
    $$ N $$
  - static friction toward the center of the circle:
    $$ f_s $$

---

### 5. Why Friction Points Toward the Center
- The car needs an inward radial force to move in a circle.
- On a flat road, the only horizontal force available is friction.
- Therefore, static friction provides the net inward force:
  $$ f_s=m a_r=m\frac{v^2}{r} $$
- Friction points toward the center of the circle, not outward.

---

### 6. Static vs. Kinetic Friction
- The car is not sliding sideways if it is successfully making the turn.
- Therefore, the friction is static friction.
- At the maximum speed before slipping:
  $$ f_s=f_{s,\max} $$
- Maximum static friction:
  $$ f_{s,\max}=\mu_s N $$

---

### 7. Vertical Force Balance
- The car has no vertical acceleration:
  $$ \sum F_y=0 $$
- Therefore:
  $$ N-mg=0 $$
- So:
  $$ N=mg $$

---

### 8. Radial Force Equation
- In the radial direction:
  $$ \sum F_r=m a_r $$
- Since friction is the radial force:
  $$ f_s=m a_r=m\frac{v^2}{r} $$
- At the slipping threshold:
  $$ f_s=f_{s,\max}=\mu_s N=m a_r=m\frac{v^2}{r} $$

---

### 9. Solving for the Coefficient of Static Friction
- Substitute:
  $$ N=mg $$
- Then:
  $$ \mu_s mg=m\frac{v^2}{r} $$
- Cancel mass:
  $$ \mu_s g=\frac{v^2}{r} $$
- Solve:
  $$ \mu_s=\frac{v^2}{rg} $$

---

### 10. Numerical Result for the Flat Curve
- Given:
  $$ v=16\ \mathrm{m}/\mathrm{s} $$
  $$ r=49\ \mathrm{m} $$
  $$ g=9.81\ \mathrm{m}/\mathrm{s}^2 $$
- Compute:
  $$ \mu_s=\frac{16^2}{(49)(9.81)} $$
- Result:
  $$ \mu_s\approx 0.53 $$
- The car’s mass cancels out, so the required friction coefficient does not depend on mass.

---

## Banked Curve Without Friction

### 11. Physical Setup: Icy Banked Curve
- A car travels around a banked curve.
- The road is icy, so friction is neglected.
- The banking angle is:
  $$ \theta $$
- The curve radius is:
  $$ r $$
- Goal:
  - find the speed $v$ needed to navigate the curve without friction

---

### 12. Free-Body Diagram for the Icy Banked Curve
- Forces on the car:
  - gravitational force downward:
    $$ mg $$
  - normal force perpendicular to the road:
    $$ N $$
- There is no friction force.

---

### 13. Coordinate Choice
- Use:
  - vertical axis $y$
  - radial axis $r$ pointing inward toward the center of the circle
- This is important because radial acceleration points toward the center:
  $$ a_r=\frac{v^2}{r} $$
- Do not choose axes parallel and perpendicular to the ramp if you want to directly use:
  $$ \frac{v^2}{r} $$

---

### 14. Components of the Normal Force
- The normal force has:
  - vertical component:
    $$ N\cos\theta $$
  - radial inward component:
    $$ N\sin\theta $$

---

### 15. Vertical Force Equation
- No vertical acceleration:
  $$ \sum F_y=0 $$
- Therefore:
  $$ N\cos\theta - mg=0 $$
- So:
  $$ N\cos\theta=mg $$
- Solve for $N$:
  $$ N=\frac{mg}{\cos\theta} $$

---

### 16. Radial Force Equation
- Radial acceleration:
  $$ a_r=\frac{v^2}{r} $$
- Radial force equation:
  $$ \sum F_r=m a_r $$
- The inward component of the normal force provides the radial force:
  $$ N\sin\theta=m a_r=m\frac{v^2}{r} $$

---

### 17. Solve for the Speed on a Frictionless Banked Curve
- Substitute:
  $$ N=\frac{mg}{\cos\theta} $$
- Then:
  $$ \frac{mg}{\cos\theta}\sin\theta=m\frac{v^2}{r} $$
- Cancel mass:
  $$ g\tan\theta=\frac{v^2}{r} $$
- Solve:
  $$ v=\sqrt{rg\tan\theta} $$

---

### 18. Numerical Result for the Icy Banked Curve
- Given:
  $$ r=48\ \mathrm{m} $$
  $$ \theta=6.2^\circ $$
  $$ g=9.81\ \mathrm{m}/\mathrm{s}^2 $$
- Compute:
  $$ v=\sqrt{(48)(9.81)\tan(6.2^\circ)} $$
- Result:
  $$ v\approx 7.2\ \mathrm{m}/\mathrm{s} $$

---

### 19. Key Observation
- The car’s mass cancels out.
- The no-friction banked-curve speed depends only on:
  $$ r,\quad g,\quad \theta $$

---

## Banked Curve With Friction

### 20. Adding Static Friction
- If the ice melts, static friction can act between the tires and road.
- This means the car can travel:
  - slower than the no-friction speed
  - or faster than the no-friction speed
- Friction adjusts direction depending on which way the car would tend to slide.

---

### 21. Direction of Friction if the Car Is Going Too Slowly
- If the car is stopped or moving too slowly, it tends to slide down the bank.
- Static friction points up the slope to oppose that tendency.

---

### 22. Direction of Friction if the Car Is Going Faster Than the No-Friction Speed
- If the car is going faster than:
  $$ v=\sqrt{rg\tan\theta} $$
- It tends to slide up the bank, outward from the curve.
- Therefore, static friction points down the slope.

---

### 23. Free-Body Diagram for Maximum Speed
- For the maximum speed before sliding:
  - friction points down the slope
  - friction is at its maximum value
- Forces:
  - weight:
    $$ mg $$
  - normal force:
    $$ N $$
  - static friction:
    $$ f_s=f_{s,\max}=\mu_s N $$

---

### 24. Components for Maximum-Speed Case
- With friction down the slope:
  - vertical component of friction points downward:
    $$ f_s\sin\theta $$
  - radial component of friction points inward:
    $$ f_s\cos\theta $$

---

### 25. Vertical Force Equation With Friction
- No vertical acceleration:
  $$ \sum F_y=0 $$
- Therefore:
  $$ N\cos\theta - f_s\sin\theta - mg=0 $$
- Substitute:
  $$ f_s=f_{s,\max}=\mu_s N $$
- Then:
  $$ N\cos\theta-\mu_s N\sin\theta=mg $$
- Factor:
  $$ N(\cos\theta-\mu_s\sin\theta)=mg $$

---

### 26. Radial Force Equation With Friction
- Radial equation:
  $$ \sum F_r=m a_r $$
- Inward components:
  $$ N\sin\theta+f_s\cos\theta=m a_r=m\frac{v^2}{r} $$
- Substitute:
  $$ f_s=f_{s,\max}=\mu_s N $$
- Then:
  $$ N\sin\theta+\mu_s N\cos\theta=m\frac{v^2}{r} $$
- Factor:
  $$ N(\sin\theta+\mu_s\cos\theta)=m\frac{v^2}{r} $$

---

### 27. Solve for Maximum Speed
- From vertical force balance:
  $$ N=\frac{mg}{\cos\theta-\mu_s\sin\theta} $$
- Substitute into the radial equation:
  $$ \frac{mg}{\cos\theta-\mu_s\sin\theta}(\sin\theta+\mu_s\cos\theta)
     =m\frac{v^2}{r} $$
- Cancel mass:
  $$ \frac{g(\sin\theta+\mu_s\cos\theta)}
     {\cos\theta-\mu_s\sin\theta}
     =
     \frac{v^2}{r} $$
- Solve:
  $$
  v_{\max,\mathrm{banked}}
  =
  \sqrt{
  rg
  \frac{\sin\theta+\mu_s\cos\theta}
       {\cos\theta-\mu_s\sin\theta}
  }
  $$

---

### 28. Numerical Result for Maximum Speed
- Using the values from the lecture, the result is:
  $$ v_{\max,\mathrm{banked}}\approx 25\ \mathrm{m}/\mathrm{s} $$
- This is approximately:
  $$ 55\ \mathrm{mi}/\mathrm{h} $$

---

### 29. Key Observations for Banked Curves
- For no friction:
  $$ v=\sqrt{rg\tan\theta} $$
- With friction, there is a range of possible speeds.
- The friction direction depends on whether the car tends to slide:
  - down the bank
  - or up the bank

---

## Conical Pendulum

### 30. Physical Setup
- A key or object is tied to a string and moves in a horizontal circle.
- This is called a **conical pendulum**.
- The object moves in a circle while the string makes an angle with the vertical.

---

### 31. Free-Body Diagram for the Conical Pendulum
- Forces on the object:
  - gravitational force downward:
    $$ mg $$
  - tension along the string:
    $$ T_{\mathrm{tens}} $$
- There is no separate “centripetal force” vector.

---

### 32. No Separate Inward Force
- Some students may be tempted to draw an additional force pointing toward the center.
- That is not a real force.
- The inward radial force is the horizontal component of tension.

---

### 33. Radial Force Comes From Tension
- The tension force can be broken into:
  - vertical component balancing weight
  - horizontal component providing radial acceleration
- Vertical:
  $$ T_{\mathrm{tens}}\cos\theta=mg $$
- Radial:
  $$ T_{\mathrm{tens}}\sin\theta=m a_r=m\frac{v^2}{r} $$

---

### 34. Connection to the Banked Curve
- The conical pendulum has the same mathematical structure as the frictionless banked curve.
- In both cases:
  - one angled force provides a vertical component
  - and a radial inward component
- For the banked curve:
  $$ N $$
  plays the role of the angled force.
- For the conical pendulum:
  $$ T_{\mathrm{tens}} $$
  plays the role of the angled force.

---

### 35. Main Conceptual Warning
- “Centripetal force” is not an extra force.
- It is the name for the net inward radial force:
  $$ \sum F_r=m a_r $$
- Real forces such as tension, friction, gravity, or normal force may contribute to this net radial force.

---

### 36. Main Physics Takeaways
- For a flat curve, static friction provides the radial force:
  $$ f_s=m a_r=m\frac{v^2}{r} $$
- For a frictionless banked curve, the inward component of the normal force provides the radial force:
  $$ N\sin\theta=m a_r=m\frac{v^2}{r} $$
- For a banked curve with friction, both normal force and friction can contribute to radial force.
- For a conical pendulum, the horizontal component of tension provides the radial force.
- Always identify the real forces first, then determine which components point radially inward.

---

### 37. Main Problem-Solving Takeaways
- Start with a free-body diagram.
- Choose axes carefully:
  - vertical direction
  - radial direction toward the center
- Do not add a fake centripetal force.
- Use:
  $$ \sum F_y=0 $$
  when there is no vertical acceleration.
- Use:
  $$ \sum F_r=m a_r $$
  for circular motion.
- Solve symbolically before substituting numbers.
