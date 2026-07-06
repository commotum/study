## Lecture Outline (Physics 212: Course Logistics, Problem-Solving Strategy, and Circular Motion)

### 1. Opening Course Logistics
- The lecture begins with a short check-in about course structure and questions from the previous class.
- Students are encouraged to:
  - talk with classmates in breakout rooms
  - ask questions in Zoom or chat
  - email the instructor when course setup questions come up
  - stay for office hour after class

---

### 2. Lab TA Meetings During Week 1
- Lab TA meetings generally begin during the second week.
- During the first week, students automatically receive credit for the TA meeting because lab groups and meeting times are still being arranged.
- Students may meet with a TA during the first week if their group has already arranged a meeting.

---

### 3. Canvas Announcements and Notifications
- The instructor emphasizes turning on Canvas notifications for course announcements.
- Recommended action:
  - go to Canvas account settings
  - select notifications
  - enable announcements for this course
- Announcements are used for information about:
  - lecture videos
  - participation assignments
  - due dates
  - course corrections or updates

---

### 4. Participation Grades in Canvas
- If students participate live through Poll Everywhere, the participation score appears after the instructor syncs the grades.
- If students complete asynchronous participation instead, Canvas may temporarily show a zero.
- That zero is replaced after the asynchronous assignment is graded.
- Early in the term, Canvas grades may look misleading because there are very few grade entries.

---

### 5. Participation Category Weight
- Participation counts as:
  $$ 5\% $$
  of the overall course grade.
- Missing one early participation assignment may make the Canvas grade look artificially low.
- The instructor drops three participation scores near the end of the term.

---

### 6. Due Date Clarification
- The PDF syllabus has the correct quiz and assignment dates.
- The Canvas syllabus/calendar may show placeholder or outdated dates for unpublished assignments.
- Students should use the posted PDF syllabus as the reliable source for dates.
- If due dates appear inconsistent later in the term, students should email the instructor.

---

### 7. Course Content Overview
- The course begins with rotational motion.
- Major topic sequence:
  - rotational kinematics
  - rotational dynamics
  - torque and moment of inertia
  - angular momentum
  - rotational energy
  - oscillations
  - waves
  - wave optics
  - ray optics

---

### 8. Translational vs. Rotational Motion
- Rotational motion is presented as translational motion rewritten in a more convenient form for circular motion.
- Translational dynamics:
  $$ \sum F = ma $$
- Rotational dynamics:
  $$ \sum \tau = I\alpha $$
- Translational momentum relation:
  $$ \sum F = \frac{dp}{dt} $$
- Rotational analogue:
  $$ \sum \tau = \frac{dL}{dt} $$

---

### 9. Problem-Solving Strategy in Physics
- Physics is not just applied math.
- The math is usually the final step.
- Recommended process:
  1. understand the physical situation
  2. identify the system
  3. state assumptions
  4. create visual representations
  5. choose general equations
  6. specialize equations to the system
  7. solve the math

---

### 10. Importance of Assumptions
- Assumptions simplify the physical system so the analysis is possible.
- Example:
  - modeling a golf ball’s flight without every microscopic interaction
- Knowing which assumptions to make is a major part of physics problem solving.

---

### 11. Visual Representations
- Useful representations include:
  - diagrams
  - graphs
  - coordinate systems
  - vectors
  - free-body diagrams
- These help connect the physical situation to equations.

---

### 12. Studying for Physics Quizzes
- The instructor recommends practicing setup more than algebra.
- Many students understand the math but struggle with:
  - where to start
  - what equation to use
  - how to represent the system
- The focus should be on building the problem from the physical situation upward.

---

### 13. Equation Sheets
- Students write their own equation sheets.
- The equation sheet can include:
  - equations
  - diagrams
  - labels
  - notes to self
- The goal is not just memorization, but understanding how to apply the equations.

---

### 14. Bloom’s Taxonomy and Physics Learning
- The lecture references Bloom’s taxonomy:
  - remembering
  - understanding
  - applying
  - analyzing
  - evaluating
  - creating / synthesizing
- Physics emphasizes higher-level skills:
  - analyzing systems
  - choosing assumptions
  - applying ideas to new situations
  - recognizing similarities between different problems

---

## Circular Motion and Rotational Kinematics

### 15. Translational Motion Review
- Position:
  $$ x(t) $$
- Velocity:
  $$ v(t)=\frac{dx(t)}{dt} $$
- Acceleration:
  $$ a(t)=\frac{dv(t)}{dt} $$
- Equivalently:
  $$ a(t)=\frac{d^2x(t)}{dt^2} $$

---

### 16. Integral Relationships for Translational Motion
- Velocity from acceleration:
  $$ v(t)=\int a(t)\,dt $$
- Position from velocity:
  $$ x(t)=\int v(t)\,dt $$
- These relationships reverse the derivative chain:
  $$ x(t) \rightarrow v(t) \rightarrow a(t) $$

---

### 17. Arc Length and Angle
- For circular motion, arc length is related to radius and angle by:
  $$ s=r\theta $$
- Here:
  - $s$ is arc length
  - $r$ is radius
  - $\theta$ is angular position in radians

---

### 18. Radians
- One radian is the angle subtended when the arc length equals the radius.
- A full revolution is:
  $$ 2\pi \text{ rad} $$
- Equivalent angle measures:
  $$ 1\text{ revolution}=360^\circ=2\pi\text{ rad} $$

---

### 19. Angular Velocity
- Angular velocity is:
  $$ \omega(t)=\frac{d\theta(t)}{dt} $$
- Units may be:
  $$ \text{rad/s} $$
  or:
  $$ \text{rev/s}, \quad \text{deg/s}, \quad \text{s}^{-1} $$

---

### 20. Angular Acceleration
- Angular acceleration is:
  $$ \alpha(t)=\frac{d\omega(t)}{dt} $$
- This describes how fast angular velocity changes with time.

---

### 21. Translational–Rotational Connections
- From:
  $$ s=r\theta $$
- Differentiate with respect to time:
  $$ v=r\omega $$
- Differentiate again for tangential acceleration:
  $$ a_t=r\alpha $$

---

### 22. Integral Relationships for Rotational Motion
- Angular velocity from angular acceleration:
  $$ \omega(t)=\int \alpha(t)\,dt $$
- Angular position from angular velocity:
  $$ \theta(t)=\int \omega(t)\,dt $$

---

### 23. Constant-Acceleration Translational Kinematics
- For constant acceleration:
  $$ x_f=x_0+v_0t+\frac{1}{2}at^2 $$
  $$ v_f=v_0+at $$
  $$ v_f^2=v_0^2+2a\Delta x $$

---

### 24. Constant-Angular-Acceleration Kinematics
- Direct rotational analogues:
  $$ \theta_f=\theta_0+\omega_0t+\frac{1}{2}\alpha t^2 $$
  $$ \omega_f=\omega_0+\alpha t $$
  $$ \omega_f^2=\omega_0^2+2\alpha\Delta\theta $$

---

### 25. Direction and Sign Conventions
- For translational motion, choosing a positive direction defines signs for:
  - position
  - velocity
  - acceleration
- For rotational motion, choosing a positive rotational direction defines signs for:
  - angular position
  - angular velocity
  - angular acceleration
- The lecture notes that directionality for rotation will require more care later, including the right-hand rule.

---

## Vector Notation and Circular Coordinates

### 26. Cartesian Vector Components
- A vector can be written in component form:
  $$ \vec{a}=a_x\hat{x}+a_y\hat{y} $$
- Magnitude:
  $$ |\vec{a}|=\sqrt{a_x^2+a_y^2} $$

---

### 27. Radial and Tangential Components
- For circular motion, it is often more useful to use:
  - radial direction
  - tangential direction
- Acceleration can be written as:
  $$ \vec{a}=a_r\hat{r}+a_t\hat{t} $$
- Magnitude:
  $$ |\vec{a}|=\sqrt{a_r^2+a_t^2} $$

---

### 28. Radial vs. Tangential Acceleration
- Tangential acceleration describes how the **speed** around the circle changes:
  $$ a_t=r\alpha $$
- Radial acceleration points along the radius and is associated with changing direction of motion.
- Angular acceleration $\alpha$ is different from $a_r$ and $a_t$:
  $$ \alpha=\frac{d\omega}{dt} $$

---

## Poll Everywhere Example 1: Reversing Direction

### 29. Given Angular Velocity
- The example gives:
  $$ \omega(t)=a-bt^2 $$
- With:
  $$ a=18\ \text{s}^{-1} $$
  $$ b=0.50\ \text{s}^{-3} $$

---

### 30. When Does the Disk Reverse Direction?
- A disk reverses direction when angular velocity becomes zero:
  $$ \omega(t)=0 $$
- Set:
  $$ 0=a-bt^2 $$
- Solve:
  $$ bt^2=a $$
  $$ t^2=\frac{a}{b} $$
  $$ t=\sqrt{\frac{a}{b}} $$

---

### 31. Numerical Result
- Substitute:
  $$ t=\sqrt{\frac{18}{0.50}} $$
- Therefore:
  $$ t=\sqrt{36}=6.0\text{ s} $$
- The disk reverses direction at:
  $$ t=6.0\text{ s} $$

---

### 32. Why Constant-Acceleration Equations Do Not Apply
- Since:
  $$ \omega(t)=a-bt^2 $$
- Angular acceleration is:
  $$ \alpha(t)=\frac{d\omega}{dt}=-2bt $$
- Because $\alpha(t)$ depends on time, angular acceleration is not constant.
- Therefore, constant-angular-acceleration kinematic equations should not be used.

---

## Poll Everywhere Example 2: Angular Displacement

### 33. Angular Displacement Before Reversal
- The question asks for angular displacement from:
  $$ t=0 $$
  to the reversal time:
  $$ t=6.0\text{ s} $$

---

### 34. Start from Angular Velocity
- Since:
  $$ \omega(t)=\frac{d\theta}{dt} $$
- Then:
  $$ d\theta=\omega(t)\,dt $$
- Integrate:
  $$ \Delta\theta=\int_0^{t_f}\omega(t)\,dt $$

---

### 35. Substitute $\omega(t)$
- Use:
  $$ \omega(t)=a-bt^2 $$
- Then:
  $$ \Delta\theta=\int_0^{t_f}(a-bt^2)\,dt $$

---

### 36. Evaluate the Integral
- Integrate:
  $$ \Delta\theta=\left[at-\frac{b}{3}t^3\right]_0^{t_f} $$
- With:
  $$ t_f=\sqrt{\frac{a}{b}} $$

---

### 37. Numerical Result
- Using:
  $$ a=18 $$
  $$ b=0.50 $$
  $$ t_f=6.0\text{ s} $$
- Compute:
  $$ \Delta\theta=18(6.0)-\frac{0.50}{3}(6.0)^3 $$
- So:
  $$ \Delta\theta=108-36=72 $$
- If $\omega$ is interpreted in radians per second, then:
  $$ \Delta\theta=72\text{ rad} $$

---

### 38. Units Note
- Angular velocity may be reported in:
  $$ \text{rad/s},\quad \text{rev/s},\quad \text{deg/s} $$
- The unit choice determines whether the final angle is in:
  $$ \text{radians},\quad \text{revolutions},\quad \text{degrees} $$
- The lecture notes that unit conversions must be handled carefully.

---

### 39. Main Physics Takeaways
- Rotational motion parallels translational motion:
  $$ x \leftrightarrow \theta $$
  $$ v \leftrightarrow \omega $$
  $$ a \leftrightarrow \alpha $$
- Arc length and angular position are related by:
  $$ s=r\theta $$
- Tangential quantities relate to angular quantities by:
  $$ v=r\omega $$
  $$ a_t=r\alpha $$
- If angular acceleration is not constant, use calculus rather than constant-acceleration kinematic equations.
- A reversal of rotational direction occurs when:
  $$ \omega(t)=0 $$

---

### 40. Main Course-Skill Takeaways
- Focus on setting up physics problems correctly.
- Identify what is known and what is being asked.
- Translate the physical statement into equations.
- Use calculus when the motion is not constant-acceleration.
- Practice the setup process, not just algebraic manipulation.