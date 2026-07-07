# Physics 212 Lecture Notes

Compiled from the local `Lecture-Notes.md` files in `vault/212/M1`. Administrative and course-organization material has been removed, so this file keeps the physics content only.

---

## 2026-06-23 - Circular Motion and Rotational Kinematics

Source: [[M1/2026-06-23-M1-00/Source/Lecture-Notes|Lecture Notes]]

### Circular Motion and Rotational Kinematics

#### Translational Motion Review
- Position:
  $$ x(t) $$
- Velocity:
  $$ v(t)=\frac{dx(t)}{dt} $$
- Acceleration:
  $$ a(t)=\frac{dv(t)}{dt} $$
- Equivalently:
  $$ a(t)=\frac{d^2x(t)}{dt^2} $$

#### Integral Relationships for Translational Motion
- Velocity from acceleration:
  $$ v(t)=\int a(t)\,dt $$
- Position from velocity:
  $$ x(t)=\int v(t)\,dt $$
- These relationships reverse the derivative chain:
  $$ x(t) \rightarrow v(t) \rightarrow a(t) $$

#### Arc Length and Angle
- For circular motion, arc length is related to radius and angle by:
  $$ s=r\theta $$
- Here:
  - $s$ is arc length
  - $r$ is radius
  - $\theta$ is angular position in radians

#### Radians
- One radian is the angle subtended when the arc length equals the radius.
- A full revolution is:
  $$ 2\pi \text{ rad} $$
- Equivalent angle measures:
  $$ 1\text{ revolution}=360^\circ=2\pi\text{ rad} $$

#### Angular Velocity
- Angular velocity is:
  $$ \omega(t)=\frac{d\theta(t)}{dt} $$
- Units may be:
  $$ \text{rad/s} $$
  or:
  $$ \text{rev/s}, \quad \text{deg/s}, \quad \text{s}^{-1} $$

#### Angular Acceleration
- Angular acceleration is:
  $$ \alpha(t)=\frac{d\omega(t)}{dt} $$
- This describes how fast angular velocity changes with time.

#### Translational–Rotational Connections
- From:
  $$ s=r\theta $$
- Differentiate with respect to time:
  $$ v=r\omega $$
- Differentiate again for tangential acceleration:
  $$ a_t=r\alpha $$

#### Integral Relationships for Rotational Motion
- Angular velocity from angular acceleration:
  $$ \omega(t)=\int \alpha(t)\,dt $$
- Angular position from angular velocity:
  $$ \theta(t)=\int \omega(t)\,dt $$

#### Constant-Acceleration Translational Kinematics
- For constant acceleration:
  $$ x_f=x_0+v_0t+\frac{1}{2}at^2 $$
  $$ v_f=v_0+at $$
  $$ v_f^2=v_0^2+2a\Delta x $$

#### Constant-Angular-Acceleration Kinematics
- Direct rotational analogues:
  $$ \theta_f=\theta_0+\omega_0t+\frac{1}{2}\alpha t^2 $$
  $$ \omega_f=\omega_0+\alpha t $$
  $$ \omega_f^2=\omega_0^2+2\alpha\Delta\theta $$

#### Direction and Sign Conventions
- For translational motion, choosing a positive direction defines signs for:
  - position
  - velocity
  - acceleration
- For rotational motion, choosing a positive rotational direction defines signs for:
  - angular position
  - angular velocity
  - angular acceleration
- The lecture notes that directionality for rotation will require more care later, including the right-hand rule.

### Vector Notation and Circular Coordinates

#### Cartesian Vector Components
- A vector can be written in component form:
  $$ \vec{a}=a_x\hat{x}+a_y\hat{y} $$
- Magnitude:
  $$ |\vec{a}|=\sqrt{a_x^2+a_y^2} $$

#### Radial and Tangential Components
- For circular motion, it is often more useful to use:
  - radial direction
  - tangential direction
- Acceleration can be written as:
  $$ \vec{a}=a_r\hat{r}+a_t\hat{t} $$
- Magnitude:
  $$ |\vec{a}|=\sqrt{a_r^2+a_t^2} $$

#### Radial vs. Tangential Acceleration
- Tangential acceleration describes how the **speed** around the circle changes:
  $$ a_t=r\alpha $$
- Radial acceleration points along the radius and is associated with changing direction of motion.
- Angular acceleration $\alpha$ is different from $a_r$ and $a_t$:
  $$ \alpha=\frac{d\omega}{dt} $$

### Concept Example 1: Reversing Direction

#### Given Angular Velocity
- The example gives:
  $$ \omega(t)=a-bt^2 $$
- With:
  $$ a=18\ \text{s}^{-1} $$
  $$ b=0.50\ \text{s}^{-3} $$

#### When Does the Disk Reverse Direction?
- A disk reverses direction when angular velocity becomes zero:
  $$ \omega(t)=0 $$
- Set:
  $$ 0=a-bt^2 $$
- Solve:
  $$ bt^2=a $$
  $$ t^2=\frac{a}{b} $$
  $$ t=\sqrt{\frac{a}{b}} $$

#### Numerical Result
- Substitute:
  $$ t=\sqrt{\frac{18}{0.50}} $$
- Therefore:
  $$ t=\sqrt{36}=6.0\text{ s} $$
- The disk reverses direction at:
  $$ t=6.0\text{ s} $$

#### Why Constant-Acceleration Equations Do Not Apply
- Since:
  $$ \omega(t)=a-bt^2 $$
- Angular acceleration is:
  $$ \alpha(t)=\frac{d\omega}{dt}=-2bt $$
- Because $\alpha(t)$ depends on time, angular acceleration is not constant.
- Therefore, constant-angular-acceleration kinematic equations should not be used.

### Concept Example 2: Angular Displacement

#### Angular Displacement Before Reversal
- The question asks for angular displacement from:
  $$ t=0 $$
  to the reversal time:
  $$ t=6.0\text{ s} $$

#### Start from Angular Velocity
- Since:
  $$ \omega(t)=\frac{d\theta}{dt} $$
- Then:
  $$ d\theta=\omega(t)\,dt $$
- Integrate:
  $$ \Delta\theta=\int_0^{t_f}\omega(t)\,dt $$

#### Substitute $\omega(t)$
- Use:
  $$ \omega(t)=a-bt^2 $$
- Then:
  $$ \Delta\theta=\int_0^{t_f}(a-bt^2)\,dt $$

#### Evaluate the Integral
- Integrate:
  $$ \Delta\theta=\left[at-\frac{b}{3}t^3\right]_0^{t_f} $$
- With:
  $$ t_f=\sqrt{\frac{a}{b}} $$

#### Numerical Result
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

#### Units Note
- Angular velocity may be reported in:
  $$ \text{rad/s},\quad \text{rev/s},\quad \text{deg/s} $$
- The unit choice determines whether the final angle is in:
  $$ \text{radians},\quad \text{revolutions},\quad \text{degrees} $$
- The lecture notes that unit conversions must be handled carefully.

#### Main Physics Takeaways
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

## 2026-06-24 - Circular Motion Review and Angular Direction

Source: [[M1/2026-06-24-M1-1/Source/Lecture-Notes|Lecture Notes]]

#### Opening Review
- The lecture begins by reviewing circular motion from the previous class.
- Main idea:
  - rotational motion is closely related to translational motion
  - many rotational equations have direct translational analogues

#### Translational Motion Review
- Position:
  $$ x(t) $$
- Velocity:
  $$ v(t)=\frac{dx(t)}{dt} $$
- Acceleration:
  $$ a(t)=\frac{dv(t)}{dt}=\frac{d^2x(t)}{dt^2} $$

#### Rotational Motion Variables
- Angular position:
  $$ \theta(t) $$
- Angular velocity:
  $$ \omega(t)=\frac{d\theta(t)}{dt} $$
- Angular acceleration:
  $$ \alpha(t)=\frac{d\omega(t)}{dt} $$

#### Arc Length Relationship
- Translational distance around a circle is related to angular displacement by:
  $$ s=r\theta $$
- Here:
  - $s$ is arc length
  - $r$ is radius
  - $\theta$ is angular displacement in radians

#### Integral Relationships
- Translational motion:
  $$ v(t)=\int a(t)\,dt $$
  $$ x(t)=\int v(t)\,dt $$
- Rotational motion:
  $$ \omega(t)=\int \alpha(t)\,dt $$
  $$ \theta(t)=\int \omega(t)\,dt $$

#### Constant-Acceleration Kinematics
- For translational motion with constant acceleration:
  $$ x_f=x_0+v_0t+\frac{1}{2}at^2 $$
  $$ v_f=v_0+at $$
  $$ v_f^2=v_0^2+2a\Delta x $$

#### Constant-Angular-Acceleration Kinematics
- Rotational analogues:
  $$ \theta_f=\theta_0+\omega_0t+\frac{1}{2}\alpha t^2 $$
  $$ \omega_f=\omega_0+\alpha t $$
  $$ \omega_f^2=\omega_0^2+2\alpha\Delta\theta $$

#### Vector Nature of Acceleration
- Acceleration can be written in Cartesian components:
  $$ \vec{a}=a_x\hat{x}+a_y\hat{y}+a_z\hat{z} $$
- Magnitude:
  $$ |\vec{a}|=\sqrt{a_x^2+a_y^2+a_z^2} $$

#### Radial and Tangential Acceleration
- For circular motion, it is often useful to break acceleration into:
  - radial acceleration
  - tangential acceleration
- Write:
  $$ \vec{a}=a_r\hat{r}+a_t\hat{t} $$
- Magnitude:
  $$ |\vec{a}|=\sqrt{a_r^2+a_t^2} $$

#### Meaning of Each Acceleration Component
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

#### Direction of Radial Acceleration
- For circular motion, the particle does not move inward or outward along the radius.
- However, the direction of velocity changes continuously.
- Radial acceleration points along the radius, typically chosen positive inward toward the center of the circle.

### Concept Example 1: Disk Coming to a Stop

#### Problem Statement
- A disk is spinning initially at:
  $$ \omega_0=12\ \mathrm{rad/s} $$
- It comes to a stop in:
  $$ \Delta t=26\ \mathrm{s} $$
- The angular acceleration is constant.
- Find the magnitude of the angular acceleration:
  $$ |\alpha| $$

#### Known Quantities
- Initial angular velocity:
  $$ \omega_0=12\ \mathrm{rad/s} $$
- Final angular velocity:
  $$ \omega_f=0 $$
- Time interval:
  $$ \Delta t=26\ \mathrm{s} $$
- Angular acceleration is constant:
  $$ \alpha=\text{constant} $$

#### Kinematic Graphs
- The instructor emphasizes drawing kinematic plots:
  - $\alpha$ vs. $t$
  - $\omega$ vs. $t$
  - $\theta$ vs. $t$
- Since angular acceleration is constant and the disk slows down:
  - $\alpha$ is a constant negative value
  - $\omega$ decreases linearly to zero
  - $\theta$ increases but with decreasing slope

#### Choosing the Correct Equation
- Use:
  $$ \omega_f=\omega_0+\alpha t $$
- Since the disk stops:
  $$ 0=\omega_0+\alpha t $$
- If solving for the magnitude:
  $$ |\alpha|=\frac{\omega_0}{t} $$

#### Angular Acceleration Calculation
- Substitute:
  $$ |\alpha|=\frac{12}{26} $$
- Result:
  $$ |\alpha|=0.46\ \mathrm{rad/s^2} $$
- With one extra digit:
  $$ |\alpha|=0.461\ \mathrm{rad/s^2} $$

#### Why the Sign Is Negative
- If the initial direction of rotation is chosen as positive, then:
  $$ \omega_0>0 $$
- Since the disk slows down:
  $$ \alpha<0 $$
- The magnitude is still positive:
  $$ |\alpha|=0.46\ \mathrm{rad/s^2} $$

### Direction of Angular Quantities

#### Translational Sign Convention Review
- In one-dimensional translational motion, choosing $+x$ determines:
  - positive velocity
  - positive acceleration
- If an object moves in the positive direction and speeds up:
  $$ a>0 $$
- If an object moves in the positive direction and slows down:
  $$ a<0 $$

#### Rotational Direction Is More Subtle
- Clockwise and counterclockwise depend on the observer’s viewpoint.
- A disk viewed from above may appear counterclockwise.
- The same disk viewed from below appears clockwise.
- Therefore, rotational direction is better defined with vectors and the right-hand rule.

#### Angular Velocity as a Vector
- Angular velocity is a vector:
  $$ \vec{\omega} $$
- Its direction is along the axis of rotation.
- For a disk rotating in the $xy$-plane, $\vec{\omega}$ points along the $z$-axis.

#### Relationship Between $\vec{v}$, $\vec{\omega}$, and $\vec{r}$
- The velocity vector is tangent to the circle.
- The radius vector points from the center to the particle.
- The vector relationship is:
  $$ \vec{v}=\vec{\omega}\times\vec{r} $$
- This cross product defines the direction of $\vec{\omega}$.

#### Magnitude of Tangential Velocity
- From the cross product:
  $$ |\vec{v}|=|\vec{\omega}||\vec{r}|\sin(\beta) $$
- Since $\vec{\omega}$ is perpendicular to $\vec{r}$:
  $$ \beta=90^\circ $$
- Therefore:
  $$ v=\omega r $$

#### Right-Hand Rule for Cross Products
- The right-hand rule is used to determine the direction of a cross product.
- For:
  $$ \hat{x}\times\hat{y}=\hat{z} $$
- Point fingers in the direction of $\hat{x}$, curl toward $\hat{y}$, and the thumb points in the direction of $\hat{z}$.

#### Right-Handed Coordinate System
- In a right-handed coordinate system:
  $$ \hat{x}\times\hat{y}=\hat{z} $$
- The $z$-axis direction is defined by the right-hand rule.
- If $z$ were defined in the opposite direction, the system would be left-handed.

#### Direction of Angular Acceleration
- Angular acceleration points in the same direction as $\vec{\omega}$ if the object is speeding up.
- Angular acceleration points opposite $\vec{\omega}$ if the object is slowing down.
- Summary:
  - positive $\omega$ and speeding up $\Rightarrow$ positive $\alpha$
  - positive $\omega$ and slowing down $\Rightarrow$ negative $\alpha$
  - negative $\omega$ and speeding up $\Rightarrow$ negative $\alpha$
  - negative $\omega$ and slowing down $\Rightarrow$ positive $\alpha$

### Concept Example 2: Direction of Angular Acceleration

#### Problem Setup
- The disk is initially spinning in the direction shown in the diagram.
- It is slowing down.
- Determine the direction of angular acceleration:
  - into the page
  - out of the page
  - zero

#### Reasoning
- The disk’s initial rotation direction defines:
  $$ \vec{\omega}_0 $$
- Using the right-hand rule, the initial angular velocity points out of the page for the chosen positive direction.
- Since the disk is slowing down, angular acceleration points opposite $\vec{\omega}$.

#### Result
- Therefore:
  $$ \vec{\alpha} \text{ points into the page} $$
- The lecture notes that this is analogous to translational motion:
  - moving in the positive direction while slowing down means negative acceleration.

#### Why $\vec{\omega}$ Points Along the Axis
- A student asks why angular velocity points along the $z$-axis instead of along the direction of motion.
- The instructor explains:
  - velocity $\vec{v}$ is tangent to the circle
  - radius $\vec{r}$ points outward from the center
  - angular velocity $\vec{\omega}$ completes the three-dimensional basis through:
    $$ \vec{v}=\vec{\omega}\times\vec{r} $$
- For circular motion, $\vec{\omega}$ can be understood as pointing along the axis about which the object rotates.

### Concept Example 3: Number of Revolutions Before Stopping

#### Problem Statement
- Same disk:
  $$ \omega_0=12\ \mathrm{rad/s} $$
- It stops in:
  $$ t=26\ \mathrm{s} $$
- Find how many revolutions it makes before stopping.

#### Choose a Rotational Kinematic Equation
- Use:
  $$ \omega_f^2=\omega_0^2+2\alpha\Delta\theta $$
- Since the disk stops:
  $$ \omega_f=0 $$
- Since the disk is slowing down, use the magnitude of $\alpha$ with a negative sign:
  $$ 0=\omega_0^2-2|\alpha|\Delta\theta $$

#### Solve for Angular Displacement
- Rearrange:
  $$ \omega_0^2=2|\alpha|\Delta\theta $$
- Therefore:
  $$ \Delta\theta=\frac{\omega_0^2}{2|\alpha|} $$

#### Substitute the Earlier Result for $\alpha$
- From the first example:
  $$ |\alpha|=\frac{\omega_0}{t} $$
- Substitute:
  $$ \Delta\theta=\frac{\omega_0^2}{2(\omega_0/t)} $$
- Simplify:
  $$ \Delta\theta=\frac{\omega_0 t}{2} $$

#### Compute Angular Displacement in Radians
- Substitute values:
  $$ \Delta\theta=\frac{(12)(26)}{2} $$
- Result:
  $$ \Delta\theta=156\ \mathrm{rad} $$

#### Convert Radians to Revolutions
- Use:
  $$ 1\ \text{rev}=2\pi\ \text{rad} $$
- Number of revolutions:
  $$ N=\frac{156}{2\pi} $$
- Result:
  $$ N\approx 25\ \text{rev} $$

#### Main Physics Takeaways
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

#### Main Problem-Solving Takeaways
- Start by listing known quantities.
- Draw kinematic plots when helpful:
  - $\alpha(t)$
  - $\omega(t)$
  - $\theta(t)$
- Choose the equation based on what is known and what is being asked.
- Keep signs separate from magnitudes when needed.
- Convert final angular displacement into the requested units:
  $$ \text{radians} \to \text{revolutions} $$

---

## 2026-06-25 - Circular Motion and Radial Acceleration

Source: [[M1/2026-06-25-M1-2/Source/Lecture-Notes|Lecture Notes]]

### Rotating Disk / Bullet Problem

#### Physical Setup
- A bullet passes through two rotating disks or plates.
- The disks are separated by distance:
  $$ d $$
- The system rotates with period:
  $$ T $$
- The holes in the two disks are separated by angular displacement:
  $$ \theta $$
- The bullet travels with speed:
  $$ v $$

#### Assumptions for the Bullet Problem
- The bullet is moving fast enough that gravity can be neglected.
- The bullet is treated as a particle.
- The bullet fits through the holes.
- The rotating disks are rigid.
- Air resistance is neglected.
- Therefore, the bullet speed is constant:
  $$ v=\text{constant} $$

#### Covariational Reasoning
- Before solving, the lecture uses **covariational reasoning**.
- This means asking how changing one variable affects another.
- Goal:
  - predict whether each variable should appear in the numerator or denominator of the final expression for $v$

#### Effect of Disk Separation $d$
- If the disk separation $d$ increases while everything else stays the same, the bullet must travel farther in the same timing condition.
- Therefore, the bullet must move faster.
- So $d$ should appear in the numerator:
  $$ v \propto d $$

#### Effect of Period $T$
- The period $T$ is the time for one full rotation.
- If $T$ increases, the system rotates more slowly.
- A slower rotation means the bullet can move more slowly and still pass through both holes.
- Therefore, $T$ should appear in the denominator:
  $$ v \propto \frac{1}{T} $$

#### Effect of Angular Separation $\theta$
- If the angular separation $\theta$ increases, the second hole takes longer to rotate into alignment.
- That means the bullet can travel more slowly and still meet the second hole.
- Therefore, $\theta$ should appear in the denominator:
  $$ v \propto \frac{1}{\theta} $$

#### Expected Form from Reasoning
- Covariational reasoning suggests:
  $$ v \sim \frac{d}{T\theta} $$
- A unit check confirms the basic form:
  $$ \frac{\text{m}}{\text{s}\cdot \text{rad}} $$
- Since radians are dimensionless:
  $$ \frac{\text{m}}{\text{s}} $$
- The missing factor will come from rotational motion:
  $$ 2\pi $$

#### Translational Motion of the Bullet
- The bullet travels distance $d$ between the two disks.
- Since velocity is constant:
  $$ d=v\Delta t $$
- Therefore:
  $$ \Delta t=\frac{d}{v} $$

#### Rotational Motion of the Disks
- The disks rotate through angle $\theta$ while the bullet travels between disks.
- With constant angular speed:
  $$ \theta=\omega\Delta t $$

#### Relating Angular Speed to Period
- Angular speed is related to frequency by:
  $$ \omega=2\pi f $$
- Period and frequency are related by:
  $$ T=\frac{1}{f} $$
- Therefore:
  $$ \omega=\frac{2\pi}{T} $$

#### Solve for Bullet Speed
- From:
  $$ d=v\Delta t $$
  and
  $$ \theta=\omega\Delta t $$
- Divide the first equation by the second:
  $$ \frac{d}{\theta}=\frac{v\Delta t}{\omega\Delta t} $$
- Cancel $\Delta t$:
  $$ \frac{d}{\theta}=\frac{v}{\omega} $$
- Solve for $v$:
  $$ v=\frac{d\omega}{\theta} $$
- Substitute:
  $$ \omega=\frac{2\pi}{T} $$
- Final expression:
  $$ v=\frac{2\pi d}{T\theta} $$

#### Numerical Example
- Given:
  $$ d=0.86\ \text{m} $$
  $$ \theta=\frac{\pi}{6} $$
  $$ T=0.22\ \text{s} $$
- Substitute:
  $$ v=\frac{2\pi(0.86)}{(0.22)(\pi/6)} $$
- Result:
  $$ v\approx 47\ \text{m/s} $$

#### Main Problem-Solving Lesson
- The instructor emphasizes solving symbolically first.
- Good workflow:
  1. start with general equations
  2. specify them for the system
  3. solve symbolically
  4. substitute numbers only at the end

### Radial Acceleration in Uniform Circular Motion

#### Uniform Circular Motion
- Uniform circular motion means constant speed:
  $$ |\vec{v}_1|=|\vec{v}_2|=v $$
- The velocity direction changes, so velocity is not constant.
- Since velocity changes direction, there is acceleration even when speed is constant.

#### Arc Length and Angular Displacement
- Arc length is related to radius and angular displacement by:
  $$ \Delta L = r\Delta\theta $$
- Here:
  - $\Delta L$ is a small arc length
  - $r$ is radius
  - $\Delta\theta$ is the angular displacement

#### Velocity Vectors in Circular Motion
- The velocity vector is tangent to the circle.
- At two nearby points:
  $$ \vec{v}_1 $$
  and
  $$ \vec{v}_2 $$
  have the same magnitude but different directions.
- The change in velocity is:
  $$ \Delta \vec{v}=\vec{v}_2-\vec{v}_1 $$

#### Similar-Triangle Argument
- The triangle formed by:
  $$ r,\ r,\ \Delta L $$
  is similar to the triangle formed by:
  $$ v,\ v,\ \Delta v $$
- Therefore:
  $$ \frac{\Delta v}{v}=\frac{\Delta L}{r} $$

#### Solve for $\Delta v$
- From:
  $$ \frac{\Delta v}{v}=\frac{\Delta L}{r} $$
- Rearranging:
  $$ \Delta v=\frac{v\Delta L}{r} $$

#### Radial Acceleration Definition
- Radial acceleration is:
  $$ a_r=\lim_{\Delta t\to 0}\frac{\Delta v}{\Delta t} $$
- Substitute:
  $$ \Delta v=\frac{v\Delta L}{r} $$
- Then:
  $$ a_r=\lim_{\Delta t\to 0}\frac{v\Delta L}{r\Delta t} $$

#### Derive the Magnitude of Radial Acceleration
- Since:
  $$ \lim_{\Delta t\to 0}\frac{\Delta L}{\Delta t}=v $$
- We get:
  $$ a_r=\frac{v}{r}v $$
- Therefore:
  $$ a_r=\frac{v^2}{r} $$

#### Direction of Radial Acceleration
- The direction of $\Delta\vec{v}$ points toward the center of the circle.
- Therefore, for uniform circular motion:
  $$ \vec{a}_r \text{ points toward the center} $$
- Radial acceleration is also called centripetal acceleration.

#### Radial Acceleration in Terms of Angular Speed
- Since:
  $$ v=r\omega $$
- Substitute into:
  $$ a_r=\frac{v^2}{r} $$
- Then:
  $$ a_r=\frac{(r\omega)^2}{r} $$
- So:
  $$ a_r=r\omega^2 $$

#### Uniform vs. Nonuniform Circular Motion
- In uniform circular motion:
  - speed is constant
  - radial acceleration points toward the center
  - tangential acceleration is zero
- In nonuniform circular motion:
  - speed changes
  - tangential acceleration is nonzero
  - total acceleration is the vector sum of radial and tangential components

#### Total Acceleration in Nonuniform Circular Motion
- For nonuniform circular motion:
  $$ \vec{a}=\vec{a}_r+\vec{a}_t $$
- The total acceleration generally does not point directly toward the center.
- Its magnitude is:
  $$ |\vec{a}|=\sqrt{a_r^2+a_t^2} $$

### Concept Example: Ranking Radial Accelerations

#### Ranking Setup
- Four circular-motion cases are compared.
- Use:
  $$ a_r=\frac{v^2}{r} $$
- The goal is to rank the radial accelerations from smallest to largest.

#### Given Values
- Case A:
  $$ v=1\ \text{m/s}, \quad r=1\ \text{m} $$
- Case B:
  $$ v=2\ \text{m/s}, \quad r=1\ \text{m} $$
- Case C:
  $$ v=2\ \text{m/s}, \quad r=2\ \text{m} $$
- Case D:
  $$ v=1\ \text{m/s}, \quad r=2\ \text{m} $$

#### Compute Each Radial Acceleration
- Case A:
  $$ a_{r,A}=\frac{1^2}{1}=1\ \text{m/s}^2 $$
- Case B:
  $$ a_{r,B}=\frac{2^2}{1}=4\ \text{m/s}^2 $$
- Case C:
  $$ a_{r,C}=\frac{2^2}{2}=2\ \text{m/s}^2 $$
- Case D:
  $$ a_{r,D}=\frac{1^2}{2}=0.5\ \text{m/s}^2 $$

#### Ranking Result
- From smallest to largest:
  $$ D < A < C < B $$

#### Interpretation of the Ranking
- Radial acceleration increases with the square of speed:
  $$ a_r\propto v^2 $$
- Radial acceleration decreases as radius increases:
  $$ a_r\propto \frac{1}{r} $$
- Speed has a strong effect because it is squared.

#### Main Physics Takeaways
- Uniform circular motion has constant speed but changing velocity.
- Changing velocity direction produces radial acceleration.
- Radial acceleration magnitude is:
  $$ a_r=\frac{v^2}{r} $$
- Equivalent form:
  $$ a_r=r\omega^2 $$
- The direction of radial acceleration is toward the center of the circle.
- For nonuniform circular motion, total acceleration includes both radial and tangential components:
  $$ \vec{a}=\vec{a}_r+\vec{a}_t $$
- Ranking radial accelerations requires careful attention to both speed and radius.

---

## 2026-06-29 - Circular Motion Dynamics

Source: [[M1/2026-06-29-M1-3/Source/Lecture-Notes|Lecture Notes]]

### Circular Motion Review

#### Uniform Circular Motion
- Uniform circular motion means motion in a circle at constant speed.
- Constant speed does **not** mean constant velocity because velocity direction changes.
- Since velocity changes direction, there is acceleration.

#### Nonuniform Circular Motion
- Nonuniform circular motion means:
  - motion is circular
  - speed is not constant
- In this case, acceleration has both:
  - radial component
  - tangential component

#### Radial Acceleration
- Radial acceleration points inward, toward the center of the circle.
- Magnitude:
  $$ a_r=\frac{v^2}{r} $$
- Since:
  $$ v=\omega r $$
- Radial acceleration can also be written as:
  $$ a_r=\omega^2 r $$

#### Tangential and Radial Components
- Acceleration can be resolved into:
  $$ \vec{a}=a_r\hat{r}+a_t\hat{t} $$
- Radial acceleration changes the direction of velocity.
- Tangential acceleration changes the speed.

#### Period and Speed
- For uniform circular motion, speed can be written as:
  $$ v=\frac{2\pi r}{T} $$
- Here:
  - $r$ is radius
  - $T$ is period

#### Angular Kinematics Review
- For constant angular acceleration:
  $$ \omega_f=\omega_0+\alpha t $$
  $$ \theta_f=\theta_0+\omega_0t+\frac{1}{2}\alpha t^2 $$
  $$ \omega_f^2=\omega_0^2+2\alpha\Delta\theta $$

### Ferris Wheel Example 1: Speed from Angular Velocity

#### Problem Setup
- A Ferris wheel has:
  $$ r=42\text{ m} $$
  $$ \omega=0.16\text{ rad/s} $$
- Find the speed of a particle on the rim.

#### Use the Tangential Speed Formula
- Tangential speed:
  $$ v=\omega r $$
- Substitute:
  $$ v=(0.16)(42) $$
- Result:
  $$ v=6.72\text{ m/s} $$
- Rounded appropriately:
  $$ v\approx 6.7\text{ m/s} $$

#### Units Note
- Angular velocity has units:
  $$ \text{rad/s} $$
- Radians are treated as dimensionless, so:
  $$ (\text{rad/s})(\text{m})=\text{m/s} $$

### Ferris Wheel Example 2: Comparing Normal Force at Top and Bottom

#### Physical Setup
- A person rides on a Ferris wheel.
- Compare the normal force from the seat:
  - at the top of the wheel
  - at the bottom of the wheel

#### Intuitive Result
- At the bottom, the rider feels pushed harder into the seat.
- At the top, the rider feels lighter.
- Therefore:
  $$ N_{\text{bottom}} > N_{\text{top}} $$

#### Free-Body Diagram at the Top
- Forces on the rider:
  - weight downward:
    $$ mg $$
  - normal force upward:
    $$ N_{\text{top}} $$
- At the top, radial acceleration points downward toward the center.
- Choose downward as positive.
- Force equation:
  $$ \sum F_r=ma_r $$
  $$ mg-N_{\text{top}}=m\frac{v^2}{r} $$

#### Normal Force at the Top
- Solve for normal force:
  $$ N_{\text{top}}=mg-m\frac{v^2}{r} $$
- Since:
  $$ v=\omega r $$
- Then:
  $$ \frac{v^2}{r}=\omega^2 r $$
- So:
  $$ N_{\text{top}}=m(g-\omega^2 r) $$

#### Free-Body Diagram at the Bottom
- Forces on the rider:
  - weight downward:
    $$ mg $$
  - normal force upward:
    $$ N_{\text{bottom}} $$
- At the bottom, radial acceleration points upward toward the center.
- Choose upward as positive.
- Force equation:
  $$ N_{\text{bottom}}-mg=m\frac{v^2}{r} $$

#### Normal Force at the Bottom
- Solve for normal force:
  $$ N_{\text{bottom}}=mg+m\frac{v^2}{r} $$
- Using:
  $$ \frac{v^2}{r}=\omega^2 r $$
- Then:
  $$ N_{\text{bottom}}=m(g+\omega^2 r) $$

#### Numerical Values for Ferris Wheel Normal Forces
- Given:
  $$ m=68\text{ kg} $$
  $$ r=42\text{ m} $$
  $$ \omega=0.16\text{ rad/s} $$
  $$ g=9.81\text{ m/s}^2 $$

#### Normal Force at the Bottom
- Use:
  $$ N_{\text{bottom}}=m(g+\omega^2 r) $$
- Substitute:
  $$ N_{\text{bottom}}=68\left(9.81+(0.16)^2(42)\right) $$
- Result:
  $$ N_{\text{bottom}}\approx 740\text{ N} $$

#### Normal Force at the Top
- Use:
  $$ N_{\text{top}}=m(g-\omega^2 r) $$
- Substitute:
  $$ N_{\text{top}}=68\left(9.81-(0.16)^2(42)\right) $$
- Result:
  $$ N_{\text{top}}\approx 590\text{ N} $$

#### Comparison
- The bottom normal force is larger:
  $$ N_{\text{bottom}}\approx 740\text{ N} $$
- The top normal force is smaller:
  $$ N_{\text{top}}\approx 590\text{ N} $$
- Therefore:
  $$ N_{\text{bottom}}>N_{\text{top}} $$

#### Why the Normal Force Changes
- At the bottom, the normal force must both:
  - balance weight
  - provide inward radial acceleration
- At the top, gravity already points inward, so the seat provides less normal force.

### Sign Convention for Circular Motion Forces

#### Choosing the Positive Radial Direction
- The instructor chooses the positive radial direction toward the center of the circle.
- At the top:
  $$ +r \text{ is downward} $$
- At the bottom:
  $$ +r \text{ is upward} $$
- This keeps:
  $$ a_r=\frac{v^2}{r} $$
  positive in the radial equation.

#### Importance of Free-Body Diagrams
- The lecture emphasizes starting with a free-body diagram.
- For circular motion:
  - draw all real forces
  - identify the radial direction
  - choose the positive direction toward the center
  - write Newton’s second law in the radial direction

#### Symbolic Solutions First
- Students are encouraged to solve symbolically before plugging in numbers.
- Example:
  $$ N_{\text{bottom}}=m(g+\omega^2 r) $$
- This is preferred over inserting numbers too early.
- Quiz problems may ask for symbolic answers without numbers.

### Turntable and Static Friction Example

#### Problem Setup
- A coin sits on a rotating turntable.
- Given:
  - mass:
    $$ m $$
  - radius:
    $$ r $$
  - coefficient of static friction:
    $$ \mu_s=0.24 $$
- Find the angular speed $\omega$ at which the coin just starts to slip.

#### Forces on the Coin
- Free-body diagram:
  - weight downward:
    $$ mg $$
  - normal force upward:
    $$ N $$
  - static friction inward:
    $$ f_s $$
- Static friction provides the radial force needed for circular motion.

#### Vertical Force Balance
- There is no vertical acceleration:
  $$ \sum F_y=0 $$
- So:
  $$ N-mg=0 $$
- Therefore:
  $$ N=mg $$

#### Radial Force Equation
- Radial acceleration:
  $$ a_r=\frac{v^2}{r} $$
- Newton’s second law in the radial direction:
  $$ \sum F_r=ma_r $$
- The only radial force is friction:
  $$ f_s=m\frac{v^2}{r} $$

#### Maximum Static Friction
- At the threshold of slipping:
  $$ f_s=f_{s,\max} $$
- Maximum static friction:
  $$ f_{s,\max}=\mu_s N $$
- Since:
  $$ N=mg $$
- Then:
  $$ f_{s,\max}=\mu_s mg $$

#### Solve for the Critical Speed
- Set centripetal force equal to maximum static friction:
  $$ m\frac{v^2}{r}=\mu_s mg $$
- Cancel mass:
  $$ \frac{v^2}{r}=\mu_s g $$

#### Solve for Critical Angular Speed
- Use:
  $$ v=\omega r $$
- Then:
  $$ \frac{(\omega r)^2}{r}=\mu_s g $$
- Simplify:
  $$ \omega^2 r=\mu_s g $$
- Solve:
  $$ \omega=\sqrt{\frac{\mu_s g}{r}} $$

#### Interpretation of the Turntable Result
- The mass cancels, so the slipping condition does not depend on the coin’s mass.
- If $\mu_s$ increases, the coin can rotate faster before slipping:
  $$ \omega \propto \sqrt{\mu_s} $$
- If $r$ increases, the coin slips at a lower angular speed:
  $$ \omega \propto \frac{1}{\sqrt{r}} $$

#### Main Physics Takeaways
- Circular motion requires an inward net force:
  $$ \sum F_r=m\frac{v^2}{r} $$
- Radial acceleration can be written as:
  $$ a_r=\frac{v^2}{r}=\omega^2 r $$
- For Ferris wheel motion:
  $$ N_{\text{bottom}}=m(g+\omega^2 r) $$
  $$ N_{\text{top}}=m(g-\omega^2 r) $$
- For a coin on a turntable:
  $$ \omega_{\max}=\sqrt{\frac{\mu_s g}{r}} $$
- Always identify which force provides the centripetal acceleration.

#### Main Problem-Solving Takeaways
- Start with a free-body diagram.
- Choose the radial positive direction toward the center.
- Write:
  $$ \sum F_r=ma_r $$
- Use:
  $$ a_r=\frac{v^2}{r}=\omega^2 r $$
- Solve symbolically before substituting numbers.

---

## 2026-06-30 - Flat Curves, Banked Curves, and Conical Pendulum

Source: [[M1/2026-06-30-M1-4/Source/Lecture-Notes|Lecture Notes]]

### Circular Motion on a Flat Curve

#### Physical Setup: Car on a Level Circular Curve
- A car travels around a level circular curve.
- The curve is flat:
  - no banking
  - no hill
  - no slope
- The car moves in a circle, so it must have radial acceleration:
  $$ a_r=\frac{v^2}{r} $$

#### Free-Body Diagram for the Flat Curve
- Forces on the car:
  - gravitational force downward:
    $$ mg $$
  - normal force upward:
    $$ N $$
  - static friction toward the center of the circle:
    $$ f_s $$

#### Why Friction Points Toward the Center
- The car needs an inward radial force to move in a circle.
- On a flat road, the only horizontal force available is friction.
- Therefore, static friction provides the centripetal force:
  $$ f_s = m\frac{v^2}{r} $$
- Friction points toward the center of the circle, not outward.

#### Static vs. Kinetic Friction
- The car is not sliding sideways if it is successfully making the turn.
- Therefore, the friction is static friction.
- At the maximum speed before slipping:
  $$ f_s=f_{s,\max} $$
- Maximum static friction:
  $$ f_{s,\max}=\mu_s N $$

#### Vertical Force Balance
- The car has no vertical acceleration:
  $$ \sum F_y=0 $$
- Therefore:
  $$ N-mg=0 $$
- So:
  $$ N=mg $$

#### Radial Force Equation
- In the radial direction:
  $$ \sum F_r=ma_r $$
- Since friction is the radial force:
  $$ f_s=m\frac{v^2}{r} $$
- At the slipping threshold:
  $$ \mu_s N=m\frac{v^2}{r} $$

#### Solving for the Coefficient of Static Friction
- Substitute:
  $$ N=mg $$
- Then:
  $$ \mu_s mg=m\frac{v^2}{r} $$
- Cancel mass:
  $$ \mu_s g=\frac{v^2}{r} $$
- Solve:
  $$ \mu_s=\frac{v^2}{rg} $$

#### Numerical Result for the Flat Curve
- Given:
  $$ v=16\text{ m/s} $$
  $$ r=49\text{ m} $$
  $$ g=9.81\text{ m/s}^2 $$
- Compute:
  $$ \mu_s=\frac{16^2}{(49)(9.81)} $$
- Result:
  $$ \mu_s\approx 0.53 $$
- The car’s mass cancels out, so the required friction coefficient does not depend on mass.

### Banked Curve Without Friction

#### Physical Setup: Icy Banked Curve
- A car travels around a banked curve.
- The road is icy, so friction is neglected.
- The banking angle is:
  $$ \theta $$
- The curve radius is:
  $$ r $$
- Goal:
  - find the speed $v$ needed to navigate the curve without friction

#### Free-Body Diagram for the Icy Banked Curve
- Forces on the car:
  - gravitational force downward:
    $$ mg $$
  - normal force perpendicular to the road:
    $$ N $$
- There is no friction force.

#### Coordinate Choice
- Use:
  - vertical axis $y$
  - radial axis $r$ pointing inward toward the center of the circle
- This is important because radial acceleration points toward the center:
  $$ a_r=\frac{v^2}{r} $$
- Do not choose axes parallel and perpendicular to the ramp if you want to directly use:
  $$ \frac{v^2}{r} $$

#### Components of the Normal Force
- The normal force has:
  - vertical component:
    $$ N\cos\theta $$
  - radial inward component:
    $$ N\sin\theta $$

#### Vertical Force Equation
- No vertical acceleration:
  $$ \sum F_y=0 $$
- Therefore:
  $$ N\cos\theta - mg=0 $$
- So:
  $$ N\cos\theta=mg $$
- Solve for $N$:
  $$ N=\frac{mg}{\cos\theta} $$

#### Radial Force Equation
- Radial acceleration:
  $$ a_r=\frac{v^2}{r} $$
- Radial force equation:
  $$ \sum F_r=m\frac{v^2}{r} $$
- The inward component of the normal force provides the radial force:
  $$ N\sin\theta=m\frac{v^2}{r} $$

#### Solve for the Speed on a Frictionless Banked Curve
- Substitute:
  $$ N=\frac{mg}{\cos\theta} $$
- Then:
  $$ \frac{mg}{\cos\theta}\sin\theta=m\frac{v^2}{r} $$
- Cancel mass:
  $$ g\tan\theta=\frac{v^2}{r} $$
- Solve:
  $$ v=\sqrt{rg\tan\theta} $$

#### Numerical Result for the Icy Banked Curve
- Given:
  $$ r=48\text{ m} $$
  $$ \theta=6.2^\circ $$
  $$ g=9.81\text{ m/s}^2 $$
- Compute:
  $$ v=\sqrt{(48)(9.81)\tan(6.2^\circ)} $$
- Result:
  $$ v\approx 7.2\text{ m/s} $$

#### Key Observation
- The car’s mass cancels out.
- The no-friction banked-curve speed depends only on:
  $$ r,\quad g,\quad \theta $$

### Banked Curve With Friction

#### Adding Static Friction
- If the ice melts, static friction can act between the tires and road.
- This means the car can travel:
  - slower than the no-friction speed
  - or faster than the no-friction speed
- Friction adjusts direction depending on which way the car would tend to slide.

#### Direction of Friction if the Car Is Going Too Slowly
- If the car is stopped or moving too slowly, it tends to slide down the bank.
- Static friction points up the slope to oppose that tendency.

#### Direction of Friction if the Car Is Going Faster Than the No-Friction Speed
- If the car is going faster than:
  $$ v=\sqrt{rg\tan\theta} $$
- It tends to slide up the bank, outward from the curve.
- Therefore, static friction points down the slope.

#### Free-Body Diagram for Maximum Speed
- For the maximum speed before sliding:
  - friction points down the slope
  - friction is at its maximum value
- Forces:
  - weight:
    $$ mg $$
  - normal force:
    $$ N $$
  - static friction:
    $$ f_s=\mu_s N $$

#### Components for Maximum-Speed Case
- With friction down the slope:
  - vertical component of friction points downward:
    $$ f_s\sin\theta $$
  - radial component of friction points inward:
    $$ f_s\cos\theta $$

#### Vertical Force Equation With Friction
- No vertical acceleration:
  $$ \sum F_y=0 $$
- Therefore:
  $$ N\cos\theta - f_s\sin\theta - mg=0 $$
- Substitute:
  $$ f_s=\mu_s N $$
- Then:
  $$ N\cos\theta-\mu_s N\sin\theta=mg $$
- Factor:
  $$ N(\cos\theta-\mu_s\sin\theta)=mg $$

#### Radial Force Equation With Friction
- Radial equation:
  $$ \sum F_r=m\frac{v^2}{r} $$
- Inward components:
  $$ N\sin\theta+f_s\cos\theta=m\frac{v^2}{r} $$
- Substitute:
  $$ f_s=\mu_s N $$
- Then:
  $$ N\sin\theta+\mu_s N\cos\theta=m\frac{v^2}{r} $$
- Factor:
  $$ N(\sin\theta+\mu_s\cos\theta)=m\frac{v^2}{r} $$

#### Solve for Maximum Speed
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
  v_{\max}
  =
  \sqrt{
  rg
  \frac{\sin\theta+\mu_s\cos\theta}
       {\cos\theta-\mu_s\sin\theta}
  }
  $$

#### Numerical Result for Maximum Speed
- Using the values from the lecture, the result is:
  $$ v_{\max}\approx 25\text{ m/s} $$
- This is approximately:
  $$ 55\text{ mph} $$

#### Key Observations for Banked Curves
- For no friction:
  $$ v=\sqrt{rg\tan\theta} $$
- With friction, there is a range of possible speeds.
- The friction direction depends on whether the car tends to slide:
  - down the bank
  - or up the bank

### Conical Pendulum

#### Physical Setup
- A key or object is tied to a string and moves in a horizontal circle.
- This is called a **conical pendulum**.
- The object moves in a circle while the string makes an angle with the vertical.

#### Free-Body Diagram for the Conical Pendulum
- Forces on the object:
  - gravitational force downward:
    $$ mg $$
  - tension along the string:
    $$ T $$
- There is no separate “centripetal force” vector.

#### No Separate Inward Force
- Some students may be tempted to draw an additional force pointing toward the center.
- That is not a real force.
- The inward radial force is the horizontal component of tension.

#### Radial Force Comes From Tension
- The tension force can be broken into:
  - vertical component balancing weight
  - horizontal component providing radial acceleration
- Vertical:
  $$ T\cos\theta=mg $$
- Radial:
  $$ T\sin\theta=m\frac{v^2}{r} $$

#### Connection to the Banked Curve
- The conical pendulum has the same mathematical structure as the frictionless banked curve.
- In both cases:
  - one angled force provides a vertical component
  - and a radial inward component
- For the banked curve:
  $$ N $$
  plays the role of the angled force.
- For the conical pendulum:
  $$ T $$
  plays the role of the angled force.

#### Main Conceptual Warning
- “Centripetal force” is not an extra force.
- It is the name for the net inward radial force:
  $$ \sum F_r=m\frac{v^2}{r} $$
- Real forces such as tension, friction, gravity, or normal force may contribute to this net radial force.

#### Main Physics Takeaways
- For a flat curve, static friction provides the radial force:
  $$ f_s=m\frac{v^2}{r} $$
- For a frictionless banked curve, the inward component of the normal force provides the radial force:
  $$ N\sin\theta=m\frac{v^2}{r} $$
- For a banked curve with friction, both normal force and friction can contribute to radial force.
- For a conical pendulum, the horizontal component of tension provides the radial force.
- Always identify the real forces first, then determine which components point radially inward.

#### Main Problem-Solving Takeaways
- Start with a free-body diagram.
- Choose axes carefully:
  - vertical direction
  - radial direction toward the center
- Do not add a fake centripetal force.
- Use:
  $$ \sum F_y=0 $$
  when there is no vertical acceleration.
- Use:
  $$ \sum F_r=m\frac{v^2}{r} $$
  for circular motion.
- Solve symbolically before substituting numbers.

---

## 2026-07-02 - Nonuniform Circular Motion and Ball-on-String Dynamics

Source: [[M1/2026-07-02-M1-5/Source/Lecture-Notes|Lecture Notes]]

### Circular Motion Review

#### Translational Motion Review
- Velocity:
  $$ v(t)=\frac{dx(t)}{dt} $$
- Acceleration:
  $$ a(t)=\frac{dv(t)}{dt} $$
- Position can be recovered by integration:
  $$ x(t)=\int v(t)\,dt $$
- Velocity can be recovered by integration:
  $$ v(t)=\int a(t)\,dt $$

#### Rotational Motion Review
- Angular position:
  $$ \theta(t) $$
- Angular velocity:
  $$ \omega(t)=\frac{d\theta(t)}{dt} $$
- Angular acceleration:
  $$ \alpha(t)=\frac{d\omega(t)}{dt} $$

#### Constant Angular Acceleration
- If angular acceleration is constant, rotational kinematics can be used:
  $$ \omega_f=\omega_0+\alpha t $$
  $$ \theta_f=\theta_0+\omega_0t+\frac{1}{2}\alpha t^2 $$
  $$ \omega_f^2=\omega_0^2+2\alpha\Delta\theta $$

#### Acceleration as a Vector
- Acceleration can be resolved in Cartesian components:
  $$ \vec{a}=a_x\hat{x}+a_y\hat{y} $$
- It can also be resolved into radial and tangential components:
  $$ \vec{a}=a_r\hat{r}+a_t\hat{t} $$
- The magnitude is:
  $$ |\vec{a}|=\sqrt{a_r^2+a_t^2} $$

#### Radial, Tangential, and Angular Acceleration
- Radial acceleration:
  - units:
    $$ \text{m/s}^2 $$
  - points toward the center of circular motion
- Tangential acceleration:
  - units:
    $$ \text{m/s}^2 $$
  - changes the speed of the object
- Angular acceleration:
  - units:
    $$ \text{rad/s}^2 $$
  - describes how fast angular velocity changes:
    $$ \alpha=\frac{d\omega}{dt} $$

### Uniform vs. Nonuniform Circular Motion

#### Uniform Circular Motion
- Uniform circular motion means constant speed:
  $$ v=\text{constant} $$
- Velocity is still changing because its direction changes.
- Acceleration is purely radial:
  $$ \vec{a}=a_r\hat{r} $$

#### Nonuniform Circular Motion
- Nonuniform circular motion means:
  - the object moves in a circle
  - the speed changes
- Acceleration has both radial and tangential components:
  $$ \vec{a}=a_r\hat{r}+a_t\hat{t} $$
- Radial acceleration changes direction of velocity.
- Tangential acceleration changes speed.

#### Radial Acceleration
- Radial acceleration magnitude:
  $$ a_r=\frac{v^2}{r} $$
- It points toward the center of the circle.

#### Tangential Acceleration
- Tangential acceleration is related to changing speed:
  $$ a_t=\frac{dv}{dt} $$
- In rotational variables:
  $$ a_t=r\alpha $$

### Concept Question: Net Force Direction

#### Problem Setup
- A particle moves in a circle.
- The question asks which diagram represents a particle moving:
  - clockwise
  - while speeding up
- Since:
  $$ \sum \vec{F}=m\vec{a} $$
- The net force points in the same direction as the acceleration.

#### Acceleration Components for Clockwise Speeding Up
- Because the particle moves in a circle, it has radial acceleration:
  $$ \vec{a}_r \text{ points toward the center} $$
- Because it is speeding up, it also has tangential acceleration in the direction of motion:
  $$ \vec{a}_t \text{ points tangent to the path} $$
- Total acceleration:
  $$ \vec{a}=\vec{a}_r+\vec{a}_t $$

#### Resultant Acceleration Direction
- If the object were moving at constant speed, acceleration would point directly toward the center.
- Since the object is speeding up, the tangential component shifts the total acceleration away from the center direction.
- For clockwise motion while speeding up, the correct resultant acceleration direction is the inward-plus-forward direction.

#### Conceptual Warning
- A diagram showing only inward acceleration corresponds to uniform circular motion.
- A diagram with the opposite tangential component could represent:
  - counterclockwise speeding up
  - or clockwise slowing down
- Direction of tangential acceleration depends on whether the object is speeding up or slowing down.

### Ball on a String: Force-Based Circular Motion

#### Physical Setup
- A ball of mass $m$ is attached to a string of length $L$.
- The string has tension:
  $$ T_{\text{tens}} $$
- The ball is at an angle:
  $$ \theta $$
- The goal is to find:
  - radial acceleration
  - tangential acceleration
  - total acceleration
  - later, the maximum height if the string is cut

#### Modeling Assumptions
- The ball is treated as a particle.
- Rotation of the ball itself is ignored.
- The motion is analyzed using radial and tangential axes.
- The radial direction is chosen inward along the string.

#### Free-Body Diagram
- Forces on the ball:
  - tension along the string:
    $$ T_{\text{tens}} $$
  - weight downward:
    $$ mg $$
- The radial axis points inward.
- The tangential axis is perpendicular to the string.

#### Radial Force Equation
- Newton’s second law in the radial direction:
  $$ \sum F_r=ma_r $$
- Radial forces:
  - tension contributes positively:
    $$ T_{\text{tens}} $$
  - the radial component of weight contributes:
    $$ mg\cos\theta $$
- Therefore:
  $$ T_{\text{tens}}+mg\cos\theta=ma_r $$

#### Radial Acceleration
- Solve for radial acceleration:
  $$ a_r=\frac{T_{\text{tens}}}{m}+g\cos\theta $$
- The numerical result from the lecture is:
  $$ a_r=11.7\text{ m/s}^2 $$
- Rounded to two significant figures:
  $$ a_r\approx 12\text{ m/s}^2 $$

#### Tangential Force Equation
- Newton’s second law in the tangential direction:
  $$ \sum F_t=ma_t $$
- Tension is radial, so it has no tangential component.
- The tangential component comes from gravity:
  $$ mg\sin\theta $$

#### Tangential Acceleration
- From:
  $$ ma_t=mg\sin\theta $$
- Solve:
  $$ a_t=g\sin\theta $$
- Numerical result:
  $$ a_t=2.4\text{ m/s}^2 $$

#### Resolving Gravity into Components
- The gravitational force can be decomposed into:
  - radial component:
    $$ mg\cos\theta $$
  - tangential component:
    $$ mg\sin\theta $$
- The component used depends on which axis is parallel to the side of the triangle.
- The lecture emphasizes drawing the right triangle so that the components align with the chosen axes.

#### Total Acceleration Magnitude
- Since radial and tangential directions are perpendicular:
  $$ |\vec{a}|=\sqrt{a_r^2+a_t^2} $$
- Substitute:
  $$ |\vec{a}|=\sqrt{\left(\frac{T_{\text{tens}}}{m}+g\cos\theta\right)^2+\left(g\sin\theta\right)^2} $$
- Numerical result:
  $$ |\vec{a}|=11.9\text{ m/s}^2 $$
- Rounded:
  $$ |\vec{a}|\approx 12\text{ m/s}^2 $$

#### Finding the Speed from Radial Acceleration
- The lecture notes that the skipped velocity question could be solved using:
  $$ a_r=\frac{v^2}{r} $$
- In this string problem:
  $$ r=L $$
- So:
  $$ a_r=\frac{v^2}{L} $$
- Therefore:
  $$ v=\sqrt{a_rL} $$

### Cutting the String: Projectile Motion After Release

#### Physical Situation
- If the string is cut, the ball leaves the circular path.
- At the release instant, the velocity is tangent to the circle.
- After release, the ball follows projectile motion.

#### Initial Velocity Direction
- The velocity vector at release is tangential.
- If the tangent makes angle $\theta$ with the horizontal or vertical as drawn in the lecture, the vertical component is written as:
  $$ v_{0y}=v_0\sin\theta $$

#### Goal: Maximum Height Above Release Point
- Find:
  $$ \Delta y_{\max} $$
- At the maximum height:
  $$ v_{yf}=0 $$

#### Projectile Kinematics Equation
- Use:
  $$ v_{yf}^2=v_{0y}^2+2a_y\Delta y $$
- Since:
  $$ v_{yf}=0 $$
  and:
  $$ a_y=-g $$
- Then:
  $$ 0=v_{0y}^2-2g\Delta y $$

#### Solve for Maximum Height
- Rearranging:
  $$ \Delta y_{\max}=\frac{v_{0y}^2}{2g} $$
- With:
  $$ v_{0y}=v_0\sin\theta $$
- Then:
  $$ \Delta y_{\max}=\frac{v_0^2\sin^2\theta}{2g} $$

#### Express $v_0^2$ Using Radial Acceleration
- From radial acceleration:
  $$ a_r=\frac{v_0^2}{L} $$
- So:
  $$ v_0^2=a_rL $$
- Using:
  $$ a_r=\frac{T_{\text{tens}}}{m}+g\cos\theta $$
- Therefore:
  $$ v_0^2=L\left(\frac{T_{\text{tens}}}{m}+g\cos\theta\right) $$

#### Final Symbolic Expression for Maximum Height
- Substitute into the projectile expression:
  $$
  \Delta y_{\max}
  =
  \frac{
  L\left(\frac{T_{\text{tens}}}{m}+g\cos\theta\right)\sin^2\theta
  }{2g}
  $$
- The lecture emphasizes that this is a complete symbolic solution in terms of given variables:
  $$ L,\quad T_{\text{tens}},\quad m,\quad \theta,\quad g $$

#### Numerical Result for Maximum Height
- Using the values from the problem, the lecture gives:
  $$ \Delta y_{\max}=0.031\text{ m} $$

#### Main Physics Takeaways
- Nonuniform circular motion has both:
  $$ a_r $$
  and
  $$ a_t $$
- Radial acceleration points toward the center:
  $$ a_r=\frac{v^2}{r} $$
- Tangential acceleration changes the object’s speed:
  $$ a_t=\frac{dv}{dt} $$
- Net force direction matches total acceleration:
  $$ \sum \vec{F}=m\vec{a} $$
- For a ball on a string:
  $$ a_r=\frac{T_{\text{tens}}}{m}+g\cos\theta $$
  $$ a_t=g\sin\theta $$
- If the string is cut, the ball becomes a projectile with initial velocity tangent to the circle.

#### Main Problem-Solving Takeaways
- Start with a clear free-body diagram.
- Choose radial and tangential axes carefully.
- Resolve forces along the chosen axes.
- Use:
  $$ \sum F_r=ma_r $$
  and:
  $$ \sum F_t=ma_t $$
- Use projectile kinematics after circular motion ends.
- Solve symbolically before using numerical values.
