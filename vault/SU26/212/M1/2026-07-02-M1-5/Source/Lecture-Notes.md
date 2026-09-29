## Lecture Outline (Nonuniform Circular Motion, Acceleration Components, and Ball-on-String Dynamics)

### 1. Opening Course Logistics
- There is no class tomorrow.
- The next class meeting is Monday, and it will be Quiz 1.
- Quiz 1 covers material from:
  $$ \text{Chapter 4} $$
  and
  $$ \text{Chapter 8} $$
- The quiz includes:
  - rotational kinematics
  - circular forces
  - circular motion concepts

---

### 2. Quiz 1 Proctoring Options
- Students may take Quiz 1 using:
  - Zoom proctoring at:
    $$ 11{:}00\text{ AM} $$
  - Zoom proctoring at:
    $$ 6{:}00\text{ PM} $$
  - Proctorio asynchronously
- Proctorio opens:
  $$ \text{Saturday at }5{:}00\text{ PM} $$
- Proctorio closes:
  $$ \text{Monday at }5{:}00\text{ PM} $$

---

### 3. Zoom-Proctored Quiz Requirements
- Students must:
  - have a working webcam
  - keep the webcam on the entire time
  - keep microphones muted unless asking a question
- The entire class period will be used for the quiz.
- No new course content will be covered during the quiz session.

---

### 4. Quiz Format
- Quiz 1 has two parts:
  $$ \text{Part A} $$
  and
  $$ \text{Part B} $$
- Part A includes:
  - three multiple-choice questions
  - one short written question
- Part B includes:
  - one longer written question
- Each part is:
  $$ 20\text{ minutes} $$
  plus:
  $$ 5\text{ minutes} $$
  for upload.

---

### 5. Quiz Notes Requirement
- Students must upload a handwritten note sheet.
- Requirements:
  - at least half a page
  - no more than one full page
  - handwritten on paper
  - student’s own work
  - photo ID placed on top when scanned or photographed
- Submit through:
  $$ \text{Gradescope} $$

---

### 6. Calculator and Upload Notes
- Handheld calculators are allowed.
- For Proctorio, students should not switch tabs to use an online calculator.
- Proctorio includes a calculator, but students may use their own physical calculator.
- Written work is uploaded separately to Gradescope after each quiz part.

---

## Circular Motion Review

### 7. Translational Motion Review
- Velocity:
  $$ v(t)=\frac{dx(t)}{dt} $$
- Acceleration:
  $$ a(t)=\frac{dv(t)}{dt} $$
- Position can be recovered by integration:
  $$ x(t)=\int v(t)\,dt $$
- Velocity can be recovered by integration:
  $$ v(t)=\int a(t)\,dt $$

---

### 8. Rotational Motion Review
- Angular position:
  $$ \theta(t) $$
- Angular velocity:
  $$ \omega(t)=\frac{d\theta(t)}{dt} $$
- Angular acceleration:
  $$ \alpha(t)=\frac{d\omega(t)}{dt} $$

---

### 9. Constant Angular Acceleration
- If angular acceleration is constant, rotational kinematics can be used:
  $$ \omega_f=\omega_0+\alpha t $$
  $$ \theta_f=\theta_0+\omega_0t+\frac{1}{2}\alpha t^2 $$
  $$ \omega_f^2=\omega_0^2+2\alpha\Delta\theta $$

---

### 10. Acceleration as a Vector
- Acceleration can be resolved in Cartesian components:
  $$ \vec{a}=a_x\hat{x}+a_y\hat{y} $$
- It can also be resolved into radial and tangential components:
  $$ \vec{a}=a_r\hat{r}+a_t\hat{t} $$
- The magnitude is:
  $$ |\vec{a}|=\sqrt{a_r^2+a_t^2} $$

---

### 11. Radial, Tangential, and Angular Acceleration
- Radial acceleration:
  - units:
    $$ \mathrm{m}/\mathrm{s}^2 $$
  - points toward the center of circular motion
- Tangential acceleration:
  - units:
    $$ \mathrm{m}/\mathrm{s}^2 $$
  - changes the speed of the object
- Angular acceleration:
  - units:
    $$ \mathrm{rad}/\mathrm{s}^2 $$
  - describes how fast angular velocity changes:
    $$ \alpha=\frac{d\omega}{dt} $$

---

## Uniform vs. Nonuniform Circular Motion

### 12. Uniform Circular Motion
- Uniform circular motion means constant speed:
  $$ v=\text{constant} $$
- Velocity is still changing because its direction changes.
- Acceleration is purely radial:
  $$ \vec{a}=a_r\hat{r} $$

---

### 13. Nonuniform Circular Motion
- Nonuniform circular motion means:
  - the object moves in a circle
  - the speed changes
- Acceleration has both radial and tangential components:
  $$ \vec{a}=a_r\hat{r}+a_t\hat{t} $$
- Radial acceleration changes direction of velocity.
- Tangential acceleration changes speed.

---

### 14. Radial Acceleration
- Radial acceleration magnitude:
  $$ a_r=\frac{v^2}{r} $$
- It points toward the center of the circle.

---

### 15. Tangential Acceleration
- Tangential acceleration is related to changing speed:
  $$ a_t=\frac{dv}{dt} $$
- In rotational variables:
  $$ a_t=r\alpha $$

---

## Poll Everywhere Concept Question: Net Force Direction

### 16. Problem Setup
- A particle moves in a circle.
- The question asks which diagram represents a particle moving:
  - clockwise
  - while speeding up
- Since:
  $$ \vec{F}_{\mathrm{net}}=m\vec{a} $$
- The net force points in the same direction as the acceleration.

---

### 17. Acceleration Components for Clockwise Speeding Up
- Because the particle moves in a circle, it has radial acceleration:
  $$ a_r\hat{r}\ \text{points toward the center} $$
- Because it is speeding up, it also has tangential acceleration in the direction of motion:
  $$ a_t\hat{t}\ \text{points tangent to the path} $$
- Total acceleration:
  $$ \vec{a}=a_r\hat{r}+a_t\hat{t} $$

---

### 18. Resultant Acceleration Direction
- If the object were moving at constant speed, acceleration would point directly toward the center.
- Since the object is speeding up, the tangential component shifts the total acceleration away from the center direction.
- For clockwise motion while speeding up, the correct resultant acceleration direction is the inward-plus-forward direction.

---

### 19. Conceptual Warning
- A diagram showing only inward acceleration corresponds to uniform circular motion.
- A diagram with the opposite tangential component could represent:
  - counterclockwise speeding up
  - or clockwise slowing down
- Direction of tangential acceleration depends on whether the object is speeding up or slowing down.

---

## Ball on a String: Force-Based Circular Motion

### 20. Physical Setup
- A ball of mass $m$ is attached to a string of length $L$.
- The string has tension:
  $$ T_{\mathrm{tens}} $$
- The ball is at an angle:
  $$ \theta $$
- The goal is to find:
  - radial acceleration
  - tangential acceleration
  - total acceleration
  - later, the maximum height if the string is cut

---

### 21. Modeling Assumptions
- The ball is treated as a particle.
- Rotation of the ball itself is ignored.
- The motion is analyzed using radial and tangential axes.
- The radial direction is chosen inward along the string.

---

### 22. Free-Body Diagram
- Forces on the ball:
  - tension along the string:
    $$ T_{\mathrm{tens}} $$
  - weight downward:
    $$ mg $$
- The radial axis points inward.
- The tangential axis is perpendicular to the string.

---

### 23. Radial Force Equation
- Newton’s second law in the radial direction:
  $$ \sum F_r=m a_r $$
- Radial forces:
  - tension contributes positively:
    $$ T_{\mathrm{tens}} $$
  - the radial component of weight contributes:
    $$ mg\cos\theta $$
- Therefore:
  $$ T_{\mathrm{tens}}+mg\cos\theta=m a_r $$

---

### 24. Radial Acceleration
- Solve for radial acceleration:
  $$ a_r=\frac{T_{\mathrm{tens}}}{m}+g\cos\theta $$
- The numerical result from the lecture is:
  $$ a_r=11.7\ \mathrm{m}/\mathrm{s}^2 $$
- Rounded to two significant figures:
  $$ a_r\approx 12\ \mathrm{m}/\mathrm{s}^2 $$

---

### 25. Tangential Force Equation
- Newton’s second law in the tangential direction:
  $$ \sum F_t=m a_t $$
- Tension is radial, so it has no tangential component.
- The tangential component comes from gravity:
  $$ mg\sin\theta $$

---

### 26. Tangential Acceleration
- From:
  $$ m a_t=mg\sin\theta $$
- Solve:
  $$ a_t=g\sin\theta $$
- Numerical result:
  $$ a_t=2.4\ \mathrm{m}/\mathrm{s}^2 $$

---

### 27. Resolving Gravity into Components
- The gravitational force can be decomposed into:
  - radial component:
    $$ mg\cos\theta $$
  - tangential component:
    $$ mg\sin\theta $$
- The component used depends on which axis is parallel to the side of the triangle.
- The lecture emphasizes drawing the right triangle so that the components align with the chosen axes.

---

### 28. Total Acceleration Magnitude
- Since radial and tangential directions are perpendicular:
  $$ |\vec{a}|=\sqrt{a_r^2+a_t^2} $$
- Substitute:
  $$ |\vec{a}|=\sqrt{\left(\frac{T_{\mathrm{tens}}}{m}+g\cos\theta\right)^2+\left(g\sin\theta\right)^2} $$
- Numerical result:
  $$ |\vec{a}|=11.9\ \mathrm{m}/\mathrm{s}^2 $$
- Rounded:
  $$ |\vec{a}|\approx 12\ \mathrm{m}/\mathrm{s}^2 $$

---

### 29. Finding the Speed from Radial Acceleration
- The lecture notes that the skipped velocity question could be solved using:
  $$ a_r=\frac{v^2}{r} $$
- In this string problem:
  $$ r=L $$
- So:
  $$ a_r=\frac{v^2}{L} $$
- Therefore:
  $$ v=\sqrt{a_rL} $$

---

## Cutting the String: Projectile Motion After Release

### 30. Physical Situation
- If the string is cut, the ball leaves the circular path.
- At the release instant, the velocity is tangent to the circle.
- After release, the ball follows projectile motion.

---

### 31. Initial Velocity Direction
- The velocity vector at release is tangential.
- If the tangent makes angle $\theta$ with the horizontal or vertical as drawn in the lecture, the vertical component is written as:
  $$ v_{0y}=v_0\sin\theta $$

---

### 32. Goal: Maximum Height Above Release Point
- Find:
  $$ \Delta y_{\max} $$
- At the maximum height:
  $$ v_{fy}=0 $$

---

### 33. Projectile Kinematics Equation
- Use:
  $$ v_{fy}^2=v_{0y}^2+2a_y\Delta y $$
- Since:
  $$ v_{fy}=0 $$
  and:
  $$ a_y=-g $$
- Then:
  $$ 0=v_{0y}^2-2g\Delta y $$

---

### 34. Solve for Maximum Height
- Rearranging:
  $$ \Delta y_{\max}=\frac{v_{0y}^2}{2g} $$
- With:
  $$ v_{0y}=v_0\sin\theta $$
- Then:
  $$ \Delta y_{\max}=\frac{v_0^2\sin^2\theta}{2g} $$

---

### 35. Express $v_0^2$ Using Radial Acceleration
- From radial acceleration:
  $$ a_r=\frac{v_0^2}{L} $$
- So:
  $$ v_0^2=a_rL $$
- Using:
  $$ a_r=\frac{T_{\mathrm{tens}}}{m}+g\cos\theta $$
- Therefore:
  $$ v_0^2=L\left(\frac{T_{\mathrm{tens}}}{m}+g\cos\theta\right) $$

---

### 36. Final Symbolic Expression for Maximum Height
- Substitute into the projectile expression:
  $$
  \Delta y_{\max}
  =
  \frac{
  L\left(\frac{T_{\mathrm{tens}}}{m}+g\cos\theta\right)\sin^2\theta
  }{2g}
  $$
- The lecture emphasizes that this is a complete symbolic solution in terms of given variables:
  $$ L,\quad T_{\mathrm{tens}},\quad m,\quad \theta,\quad g $$

---

### 37. Numerical Result for Maximum Height
- Using the values from the problem, the lecture gives:
  $$ \Delta y_{\max}=0.031\ \mathrm{m} $$

---

## Quiz Preparation Advice

### 38. Study Class Examples
- The instructor recommends reviewing:
  - multiple-choice questions done in class
  - written questions done in class
  - conceptual reasoning used in each solution
- Quiz questions are often similar to class problems but modified by “one step.”

---

### 39. Emphasis on Symbolic Solutions
- Students should show symbolic work before substituting numbers.
- Symbolic solutions should be written in terms of given variables.
- Example:
  $$
  \Delta y_{\max}
  =
  \frac{
  L\left(\frac{T_{\mathrm{tens}}}{m}+g\cos\theta\right)\sin^2\theta
  }{2g}
  $$

---

### 40. Main Physics Takeaways
- Nonuniform circular motion has both:
  $$ a_r $$
  and
  $$ a_t $$
- Radial acceleration points toward the center:
  $$ a_r=\frac{v^2}{r} $$
- Tangential acceleration changes the object’s speed:
  $$ a_t=\frac{dv}{dt} $$
- Net force direction matches total acceleration:
  $$ \vec{F}_{\mathrm{net}}=m\vec{a} $$
- For a ball on a string:
  $$ a_r=\frac{T_{\mathrm{tens}}}{m}+g\cos\theta $$
  $$ a_t=g\sin\theta $$
- If the string is cut, the ball becomes a projectile with initial velocity tangent to the circle.

---

### 41. Main Problem-Solving Takeaways
- Start with a clear free-body diagram.
- Choose radial and tangential axes carefully.
- Resolve forces along the chosen axes.
- Use:
  $$ \sum F_r=m a_r $$
  and:
  $$ \sum F_t=m a_t $$
- Use projectile kinematics after circular motion ends.
- Solve symbolically before using numerical values.
