## Lecture Outline (Circular Motion Review, Angular Direction, and Right-Hand Rule)

### 1. Opening Review
- The lecture begins by reviewing circular motion from the previous class.
- Main idea:
  - rotational motion is closely related to translational motion
  - many rotational equations have direct translational analogues

---

### 2. Translational Motion Review
- Position:
  $$ x(t) $$
- Velocity:
  $$ v(t)=\frac{dx(t)}{dt} $$
- Acceleration:
  $$ a(t)=\frac{dv(t)}{dt}=\frac{d^2x(t)}{dt^2} $$

---

### 3. Rotational Motion Variables
- Angular position:
  $$ \theta(t) $$
- Angular velocity:
  $$ \omega(t)=\frac{d\theta(t)}{dt} $$
- Angular acceleration:
  $$ \alpha(t)=\frac{d\omega(t)}{dt} $$

---

### 4. Arc Length Relationship
- Translational distance around a circle is related to angular displacement by:
  $$ s=r\theta $$
- Here:
  - $s$ is arc length
  - $r$ is radius
  - $\theta$ is angular displacement in radians

---

### 5. Integral Relationships
- Translational motion:
  $$ v(t)=\int a(t)\,dt $$
  $$ x(t)=\int v(t)\,dt $$
- Rotational motion:
  $$ \omega(t)=\int \alpha(t)\,dt $$
  $$ \theta(t)=\int \omega(t)\,dt $$

---

### 6. Constant-Acceleration Kinematics
- For translational motion with constant acceleration:
  $$ x_f=x_0+v_0t+\frac{1}{2}at^2 $$
  $$ v_f=v_0+at $$
  $$ v_f^2=v_0^2+2a\Delta x $$

---

### 7. Constant-Angular-Acceleration Kinematics
- Rotational analogues:
  $$ \theta_f=\theta_0+\omega_0t+\frac{1}{2}\alpha t^2 $$
  $$ \omega_f=\omega_0+\alpha t $$
  $$ \omega_f^2=\omega_0^2+2\alpha\Delta\theta $$

---

### 8. Course Resource Note
- The instructor reminds students that Physics 211 materials are available through the course information pages.
- These materials can be used to review:
  - translational kinematics
  - constant-acceleration equations
  - earlier physics concepts needed for Physics 212

---

### 9. Vector Nature of Acceleration
- Acceleration can be written in Cartesian components:
  $$ \vec{a}=a_x\hat{x}+a_y\hat{y}+a_z\hat{z} $$
- Magnitude:
  $$ |\vec{a}|=\sqrt{a_x^2+a_y^2+a_z^2} $$

---

### 10. Radial and Tangential Acceleration
- For circular motion, it is often useful to break acceleration into:
  - radial acceleration
  - tangential acceleration
- Write:
  $$ \vec{a}=a_r\hat{r}+a_t\hat{t} $$
- Magnitude:
  $$ |\vec{a}|=\sqrt{a_r^2+a_t^2} $$

---

### 11. Meaning of Each Acceleration Component
- Tangential acceleration:
  - describes how the tangential speed changes
  - related to angular acceleration by:
    $$ a_t=r\alpha $$
- Radial acceleration:
  - points along the radius
  - associated with changing the direction of velocity
- Angular acceleration:
  $$ \alpha=\frac{d\omega}{dt} $$
  is different from both $a_t$ and $a_r$.

---

### 12. Direction of Radial Acceleration
- For circular motion, the particle does not move inward or outward along the radius.
- However, the direction of velocity changes continuously.
- Radial acceleration points along the radius, typically chosen positive inward toward the center of the circle.

---

### 13. Course Logistics: Poll Everywhere
- Poll Everywhere questions are only visible when the instructor activates them.
- Students may need to register the first time they use Poll Everywhere.
- If Poll Everywhere does not record an answer, students should:
  - send a message in Zoom chat during or right after the poll
  - email the instructor after class

---

### 14. Course Logistics: Lab Group Discussion
- Students are reminded to post in the course introductions discussion.
- Students also need to reply to others to help form lab groups.
- The lab discussion assignment is tied to:
  - finding a group
  - choosing a meeting time
  - coordinating with a TA

---

## Poll Everywhere Example 1: Disk Coming to a Stop

### 15. Problem Statement
- A disk is spinning initially at:
  $$ \omega_0=12\ \mathrm{rad}/\mathrm{s} $$
- It comes to a stop in:
  $$ \Delta t=26\ \mathrm{s} $$
- The angular acceleration is constant.
- Find the magnitude of the angular acceleration:
  $$ |\alpha| $$

---

### 16. Known Quantities
- Initial angular velocity:
  $$ \omega_0=12\ \mathrm{rad}/\mathrm{s} $$
- Final angular velocity:
  $$ \omega_f=0 $$
- Time interval:
  $$ \Delta t=26\ \mathrm{s} $$
- Angular acceleration is constant:
  $$ \alpha=\text{constant} $$

---

### 17. Kinematic Graphs
- The instructor emphasizes drawing kinematic plots:
  - $\alpha$ vs. $t$
  - $\omega$ vs. $t$
  - $\theta$ vs. $t$
- Since angular acceleration is constant and the disk slows down:
  - $\alpha$ is a constant negative value
  - $\omega$ decreases linearly to zero
  - $\theta$ increases but with decreasing slope

---

### 18. Choosing the Correct Equation
- Use:
  $$ \omega_f=\omega_0+\alpha t $$
- Since the disk stops:
  $$ 0=\omega_0+\alpha t $$
- If solving for the magnitude:
  $$ |\alpha|=\frac{\omega_0}{t} $$

---

### 19. Angular Acceleration Calculation
- Substitute:
  $$ |\alpha|=\frac{12}{26} $$
- Result:
  $$ |\alpha|=0.46\ \mathrm{rad}/\mathrm{s}^2 $$
- With one extra digit:
  $$ |\alpha|=0.461\ \mathrm{rad}/\mathrm{s}^2 $$

---

### 20. Why the Sign Is Negative
- If the initial direction of rotation is chosen as positive, then:
  $$ \omega_0>0 $$
- Since the disk slows down:
  $$ \alpha<0 $$
- The magnitude is still positive:
  $$ |\alpha|=0.46\ \mathrm{rad}/\mathrm{s}^2 $$

---

## Direction of Angular Quantities

### 21. Translational Sign Convention Review
- In one-dimensional translational motion, choosing $+x$ determines:
  - positive velocity
  - positive acceleration
- If an object moves in the positive direction and speeds up:
  $$ a>0 $$
- If an object moves in the positive direction and slows down:
  $$ a<0 $$

---

### 22. Rotational Direction Is More Subtle
- Clockwise and counterclockwise depend on the observer’s viewpoint.
- A disk viewed from above may appear counterclockwise.
- The same disk viewed from below appears clockwise.
- Therefore, rotational direction is better defined with vectors and the right-hand rule.

---

### 23. Angular Velocity as a Vector
- Angular velocity is a vector:
  $$ \vec{\omega} $$
- Its direction is along the axis of rotation.
- For a disk rotating in the $xy$-plane, $\vec{\omega}$ points along the $z$-axis.

---

### 24. Relationship Between $\vec{v}$, $\vec{\omega}$, and $\vec{r}$
- The velocity vector is tangent to the circle.
- The radius vector points from the center to the particle.
- The vector relationship is:
  $$ \vec{v}=\vec{\omega}\times\vec{r} $$
- This cross product defines the direction of $\vec{\omega}$.

---

### 25. Tangential Speed
- From the cross-product magnitude:
  $$ v=r\omega\sin\theta $$
- Since $\vec{\omega}$ is perpendicular to $\vec{r}$:
  $$ \theta=90^\circ $$
- Therefore:
  $$ v=r\omega $$

---

### 26. Right-Hand Rule for Cross Products
- The right-hand rule is used to determine the direction of a cross product.
- For:
  $$ \hat{x}\times\hat{y}=\hat{z} $$
- Point fingers in the direction of $\hat{x}$, curl toward $\hat{y}$, and the thumb points in the direction of $\hat{z}$.

---

### 27. Right-Handed Coordinate System
- In a right-handed coordinate system:
  $$ \hat{x}\times\hat{y}=\hat{z} $$
- The $z$-axis direction is defined by the right-hand rule.
- If $z$ were defined in the opposite direction, the system would be left-handed.

---

### 28. Direction of Angular Acceleration
- Angular acceleration points in the same direction as $\vec{\omega}$ if the object is speeding up.
- Angular acceleration points opposite $\vec{\omega}$ if the object is slowing down.
- Summary:
  - positive $\omega$ and speeding up $\Rightarrow$ positive $\alpha$
  - positive $\omega$ and slowing down $\Rightarrow$ negative $\alpha$
  - negative $\omega$ and speeding up $\Rightarrow$ negative $\alpha$
  - negative $\omega$ and slowing down $\Rightarrow$ positive $\alpha$

---

## Poll Everywhere Example 2: Direction of Angular Acceleration

### 29. Problem Setup
- The disk is initially spinning in the direction shown in the diagram.
- It is slowing down.
- Determine the direction of angular acceleration:
  - into the page
  - out of the page
  - zero

---

### 30. Reasoning
- The disk’s initial rotation direction defines:
  $$ \vec{\omega}_0 $$
- Using the right-hand rule, the initial angular velocity points out of the page for the chosen positive direction.
- Since the disk is slowing down, angular acceleration points opposite $\vec{\omega}$.

---

### 31. Result
- Therefore:
  $$ \vec{\alpha} \text{ points into the page} $$
- The lecture notes that this is analogous to translational motion:
  - moving in the positive direction while slowing down means negative acceleration.

---

### 32. Why $\vec{\omega}$ Points Along the Axis
- A student asks why angular velocity points along the $z$-axis instead of along the direction of motion.
- The instructor explains:
  - velocity $\vec{v}$ is tangent to the circle
  - radius $\vec{r}$ points outward from the center
  - angular velocity $\vec{\omega}$ completes the three-dimensional basis through:
    $$ \vec{v}=\vec{\omega}\times\vec{r} $$
- For circular motion, $\vec{\omega}$ can be understood as pointing along the axis about which the object rotates.

---

## Poll Everywhere Example 3: Number of Revolutions Before Stopping

### 33. Problem Statement
- Same disk:
  $$ \omega_0=12\ \mathrm{rad}/\mathrm{s} $$
- It stops in:
  $$ t=26\ \mathrm{s} $$
- Find how many revolutions it makes before stopping.

---

### 34. Choose a Rotational Kinematic Equation
- Use:
  $$ \omega_f^2=\omega_0^2+2\alpha\Delta\theta $$
- Since the disk stops:
  $$ \omega_f=0 $$
- Since the disk is slowing down, use the magnitude of $\alpha$ with a negative sign:
  $$ 0=\omega_0^2-2|\alpha|\Delta\theta $$

---

### 35. Solve for Angular Displacement
- Rearrange:
  $$ \omega_0^2=2|\alpha|\Delta\theta $$
- Therefore:
  $$ \Delta\theta=\frac{\omega_0^2}{2|\alpha|} $$

---

### 36. Substitute the Earlier Result for $\alpha$
- From the first example:
  $$ |\alpha|=\frac{\omega_0}{t} $$
- Substitute:
  $$ \Delta\theta=\frac{\omega_0^2}{2(\omega_0/t)} $$
- Simplify:
  $$ \Delta\theta=\frac{\omega_0 t}{2} $$

---

### 37. Compute Angular Displacement in Radians
- Substitute values:
  $$ \Delta\theta=\frac{(12)(26)}{2} $$
- Result:
  $$ \Delta\theta=156\ \mathrm{rad} $$

---

### 38. Convert Radians to Revolutions
- Use:
  $$ 1\ \mathrm{rev}=2\pi\ \mathrm{rad} $$
- Number of revolutions:
  $$ n_{\mathrm{rev}}=\frac{156}{2\pi} $$
- Result:
  $$ n_{\mathrm{rev}}\approx 25\ \mathrm{rev} $$

---

### 39. Main Physics Takeaways
- Rotational kinematics parallels translational kinematics:
  $$ x \leftrightarrow \theta $$
  $$ v \leftrightarrow \omega $$
  $$ a \leftrightarrow \alpha $$
- Constant-angular-acceleration equations can be used only when:
  $$ \alpha=\text{constant} $$
- Direction of angular velocity and angular acceleration must be handled using vectors.
- The right-hand rule defines the direction of angular velocity:
  $$ \vec{v}=\vec{\omega}\times\vec{r} $$
- If an object is rotating in the positive direction but slowing down, angular acceleration is negative.

---

### 40. Main Problem-Solving Takeaways
- Start by listing known quantities.
- Draw kinematic plots when helpful:
  - $\alpha(t)$
  - $\omega(t)$
  - $\theta(t)$
- Choose the equation based on what is known and what is being asked.
- Keep signs separate from magnitudes when needed.
- Convert final angular displacement into the requested units:
  $$ \mathrm{rad} \to \mathrm{rev} $$
