## Lecture Outline (Circular Motion, Covariational Reasoning, and Radial Acceleration)

### 1. Opening Logistics
- Lab 1 discussion is due today.
- Students should:
  - post in the course introduction discussion
  - find potential lab partners
  - choose or join a group in the People section
  - post availability in the shared Google Doc
- The shared availability document helps the instructors and TAs arrange groups if students have trouble finding compatible schedules.

---

### 2. Lab Group Formation Advice
- To find compatible lab partners, students can use:
  $$ \text{Ctrl+F} $$
  in the course introductions thread.
- Useful search terms might include:
  - time zone
  - availability
  - major
  - program
  - schedule constraints
- If students cannot find a group, they should still try to choose a group and get others to join afterward.

---

### 3. Course Schedule Note
- There is no class tomorrow.
- After today’s lecture, there is a long weekend.
- The next class meeting is Monday.

---

## Rotating Disk / Bullet Problem

### 4. Physical Setup
- A bullet passes through two rotating disks or plates.
- The disks are separated by distance:
  $$ D $$
- The system rotates with period:
  $$ T $$
- The holes in the two disks are separated by angular displacement:
  $$ \theta $$
- The bullet travels with speed:
  $$ v $$

---

### 5. Assumptions for the Bullet Problem
- The bullet is moving fast enough that gravity can be neglected.
- The bullet is treated as a particle.
- The bullet fits through the holes.
- The rotating disks are rigid.
- Air resistance is neglected.
- Therefore, the bullet speed is constant:
  $$ v=\text{constant} $$

---

### 6. Covariational Reasoning
- Before solving, the lecture uses **covariational reasoning**.
- This means asking how changing one variable affects another.
- Goal:
  - predict whether each variable should appear in the numerator or denominator of the final expression for $v$

---

### 7. Effect of Disk Separation $D$
- If the disk separation $D$ increases while everything else stays the same, the bullet must travel farther in the same timing condition.
- Therefore, the bullet must move faster.
- So $D$ should appear in the numerator:
  $$ v \propto D $$

---

### 8. Effect of Period $T$
- The period $T$ is the time for one full rotation.
- If $T$ increases, the system rotates more slowly.
- A slower rotation means the bullet can move more slowly and still pass through both holes.
- Therefore, $T$ should appear in the denominator:
  $$ v \propto \frac{1}{T} $$

---

### 9. Effect of Angular Separation $\theta$
- If the angular separation $\theta$ increases, the second hole takes longer to rotate into alignment.
- That means the bullet can travel more slowly and still meet the second hole.
- Therefore, $\theta$ should appear in the denominator:
  $$ v \propto \frac{1}{\theta} $$

---

### 10. Expected Form from Reasoning
- Covariational reasoning suggests:
  $$ v \sim \frac{D}{T\theta} $$
- A unit check confirms the basic form:
  $$ \mathrm{m}/(\mathrm{s}\cdot\mathrm{rad}) $$
- Since radians are dimensionless:
  $$ \mathrm{m}/\mathrm{s} $$
- The missing factor will come from rotational motion:
  $$ 2\pi $$

---

### 11. Translational Motion of the Bullet
- The bullet travels distance $D$ between the two disks.
- Since velocity is constant:
  $$ D=v\Delta t $$
- Therefore:
  $$ \Delta t=\frac{D}{v} $$

---

### 12. Rotational Motion of the Disks
- The disks rotate through angle $\theta$ while the bullet travels between disks.
- With constant angular speed:
  $$ \theta=\omega\Delta t $$

---

### 13. Relating Angular Speed to Period
- Angular speed is related to frequency by:
  $$ \omega=2\pi f $$
- Period and frequency are related by:
  $$ T=\frac{1}{f} $$
- Therefore:
  $$ \omega=\frac{2\pi}{T} $$

---

### 14. Solve for Bullet Speed
- From:
  $$ D=v\Delta t $$
  and
  $$ \theta=\omega\Delta t $$
- Divide the first equation by the second:
  $$ \frac{D}{\theta}=\frac{v\Delta t}{\omega\Delta t} $$
- Cancel $\Delta t$:
  $$ \frac{D}{\theta}=\frac{v}{\omega} $$
- Solve for $v$:
  $$ v=\frac{D\omega}{\theta} $$
- Substitute:
  $$ \omega=\frac{2\pi}{T} $$
- Final expression:
  $$ v=\frac{2\pi D}{T\theta} $$

---

### 15. Numerical Example
- Given:
  $$ D=0.86\ \mathrm{m} $$
  $$ \theta=\frac{\pi}{6}\ \mathrm{rad} $$
  $$ T=0.22\ \mathrm{s} $$
- Substitute:
  $$ v=\frac{2\pi(0.86)}{(0.22)(\pi/6)} $$
- Result:
  $$ v\approx 47\ \mathrm{m}/\mathrm{s} $$

---

### 16. Main Problem-Solving Lesson
- The instructor emphasizes solving symbolically first.
- Good workflow:
  1. start with general equations
  2. specify them for the system
  3. solve symbolically
  4. substitute numbers only at the end

---

## Radial Acceleration in Uniform Circular Motion

### 17. Uniform Circular Motion
- Uniform circular motion means constant speed:
  $$ |\vec{v}_1|=|\vec{v}_2|=v $$
- The velocity direction changes, so velocity is not constant.
- Since velocity changes direction, there is acceleration even when speed is constant.

---

### 18. Arc Length and Angular Displacement
- Arc length is related to radius and angular displacement by:
  $$ \Delta s=r\Delta\theta $$
- Here:
  - $\Delta s$ is a small arc length
  - $r$ is radius
  - $\Delta\theta$ is the angular displacement

---

### 19. Velocity Vectors in Circular Motion
- The velocity vector is tangent to the circle.
- At two nearby points:
  $$ \vec{v}_1 $$
  and
  $$ \vec{v}_2 $$
  have the same magnitude but different directions.
- The change in velocity is:
  $$ \Delta\vec{v}=\vec{v}_2-\vec{v}_1 $$

---

### 20. Similar-Triangle Argument
- The triangle formed by:
  $$ r,\ r,\ \Delta s $$
  is similar to the triangle formed by:
  $$ v,\ v,\ |\Delta\vec{v}| $$
- Therefore:
  $$ \frac{|\Delta\vec{v}|}{v}=\frac{\Delta s}{r} $$

---

### 21. Solve for $|\Delta\vec{v}|$
- From:
  $$ \frac{|\Delta\vec{v}|}{v}=\frac{\Delta s}{r} $$
- Rearranging:
  $$ |\Delta\vec{v}|=\frac{v\Delta s}{r} $$

---

### 22. Radial Acceleration Definition
- Radial acceleration is:
  $$ a_r=\lim_{\Delta t\to 0}\frac{|\Delta\vec{v}|}{\Delta t} $$
- Substitute:
  $$ |\Delta\vec{v}|=\frac{v\Delta s}{r} $$
- Then:
  $$ a_r=\lim_{\Delta t\to 0}\frac{v\Delta s}{r\Delta t} $$

---

### 23. Derive the Magnitude of Radial Acceleration
- Since:
  $$ \lim_{\Delta t\to 0}\frac{\Delta s}{\Delta t}=v $$
- We get:
  $$ a_r=\frac{v}{r}v $$
- Therefore:
  $$ a_r=\frac{v^2}{r} $$

---

### 24. Direction of Radial Acceleration
- The direction of $\Delta\vec{v}$ points toward the center of the circle.
- Therefore, for uniform circular motion, the radial component $a_r$ is directed toward the center.
- This inward acceleration is sometimes called centripetal acceleration; here it is denoted by $a_r$ and called radial acceleration.

---

### 25. Radial Acceleration in Terms of Angular Speed
- Since:
  $$ v=r\omega $$
- Substitute into:
  $$ a_r=\frac{v^2}{r} $$
- Then:
  $$ a_r=\frac{(r\omega)^2}{r} $$
- So:
  $$ a_r=r\omega^2 $$

---

### 26. Uniform vs. Nonuniform Circular Motion
- In uniform circular motion:
  - speed is constant
  - radial acceleration points toward the center
  - tangential acceleration is zero
- In nonuniform circular motion:
  - speed changes
  - tangential acceleration is nonzero
  - total acceleration is the vector sum of radial and tangential components

---

### 27. Total Acceleration in Nonuniform Circular Motion
- Choose $\hat{r}$ inward and $\hat{t}$ tangent to the path.
- For nonuniform circular motion:
  $$ \vec{a}=a_r\hat{r}+a_t\hat{t} $$
- The total acceleration generally does not point directly toward the center.
- Its magnitude is:
  $$ |\vec{a}|=\sqrt{a_r^2+a_t^2} $$

---

## Poll Everywhere Example: Ranking Radial Accelerations

### 28. Ranking Setup
- Four circular-motion cases are compared.
- Use:
  $$ a_r=\frac{v^2}{r} $$
- The goal is to rank the radial accelerations from smallest to largest.

---

### 29. Given Values
- Case A:
  $$ v=1\ \mathrm{m}/\mathrm{s}, \quad r=1\ \mathrm{m} $$
- Case B:
  $$ v=2\ \mathrm{m}/\mathrm{s}, \quad r=1\ \mathrm{m} $$
- Case C:
  $$ v=2\ \mathrm{m}/\mathrm{s}, \quad r=2\ \mathrm{m} $$
- Case D:
  $$ v=1\ \mathrm{m}/\mathrm{s}, \quad r=2\ \mathrm{m} $$

---

### 30. Compute Each Radial Acceleration
- Case A:
  $$ a_{r,A}=\frac{1^2}{1}=1\ \mathrm{m}/\mathrm{s}^2 $$
- Case B:
  $$ a_{r,B}=\frac{2^2}{1}=4\ \mathrm{m}/\mathrm{s}^2 $$
- Case C:
  $$ a_{r,C}=\frac{2^2}{2}=2\ \mathrm{m}/\mathrm{s}^2 $$
- Case D:
  $$ a_{r,D}=\frac{1^2}{2}=0.5\ \mathrm{m}/\mathrm{s}^2 $$

---

### 31. Ranking Result
- From smallest to largest:
  $$ D < A < C < B $$

---

### 32. Interpretation of the Ranking
- Radial acceleration increases with the square of speed:
  $$ a_r\propto v^2 $$
- Radial acceleration decreases as radius increases:
  $$ a_r\propto \frac{1}{r} $$
- Speed has a strong effect because it is squared.

---

### 33. Preview of Next Class
- The next lecture will apply radial acceleration to physical systems using forces.
- This means moving from kinematics to dynamics:
  $$ \sum \vec{F}=m\vec{a} $$
- For circular motion, radial acceleration will connect to the net inward force.

---

### 34. Main Physics Takeaways
- Uniform circular motion has constant speed but changing velocity.
- Changing velocity direction produces radial acceleration.
- Radial acceleration magnitude is:
  $$ a_r=\frac{v^2}{r} $$
- Equivalent form:
  $$ a_r=r\omega^2 $$
- The direction of radial acceleration is toward the center of the circle.
- For nonuniform circular motion, total acceleration includes both radial and tangential components:
  $$ \vec{a}=a_r\hat{r}+a_t\hat{t} $$
- Ranking radial accelerations requires careful attention to both speed and radius.
