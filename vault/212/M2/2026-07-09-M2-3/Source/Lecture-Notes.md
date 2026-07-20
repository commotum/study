## Lecture Outline (Torque, Moment Arms, the Right-Hand Rule, and Rotational Dynamics)

### 1. Course and Quiz Logistics
- Quiz 1 is still being graded.
- Scores are expected to be returned by Monday.
- After grading is complete, the Quiz 1 extra-credit assignment:
  $$ \text{Quiz 1X} $$
  will open.

---

### 2. Quiz 1 Extra Credit
- Quiz 1X must address the quiz problem where the student lost the most points.
- The course drops the lowest:
  - Quiz Part A score
  - Quiz Part B score
- Extra-credit points are retained even if the corresponding quiz score is later dropped.

---

### 3. Lab Participation
- Students must actively participate in their scheduled lab TA meeting.
- Half of the lab discussion grade is based on participation in the TA meeting.
- If a student cannot attend the normal meeting, they should contact the TA ahead of time and arrange to attend another available meeting.

---

### 4. Group Lab Report
- Each lab group submits one group report.
- Only students who actively contributed should:
  - have their names on the report
  - be added to the submission
- If a group member is not communicating or contributing, the group should contact the lab TA.

---

## Torque and Rotational Dynamics

### 5. Definition of Torque
- Torque is defined by the cross product:
  $$ \vec{\tau}=\vec{r}\times\vec{F} $$
- Here:
  - $\vec{r}$ points from the pivot to the point where the force is applied
  - $\vec{F}$ is the applied force
  - $\vec{\tau}$ is perpendicular to the plane containing $\vec{r}$ and $\vec{F}$

---

### 6. Magnitude of Torque
- The magnitude of torque is:
  $$ \tau=rF\sin\theta $$
- Here, $\theta$ is the angle between:
  $$ \vec{r} \quad \text{and} \quad \vec{F} $$

---

### 7. Rotational Version of Newton’s Second Law
- Translational dynamics:
  $$ \sum \vec{F}=m\vec{a} $$
- Rotational dynamics for a fixed-axis rigid body:
  $$ \sum \vec{\tau}=I\vec{\alpha} $$
- Here:
  - $I$ is the moment of inertia
  - $\vec{\alpha}$ is the angular acceleration

---

### 8. What Determines the Rotational Effect of a Force?
- Torque depends on:
  - the force magnitude $F$
  - the distance $r$ from the pivot
  - the angle $\theta$ between $\vec{r}$ and $\vec{F}$
- A force produces more torque when:
  - it is applied farther from the pivot
  - it is directed more nearly perpendicular to $\vec{r}$

---

### 9. Tangential Component of Force
- Only the component of force perpendicular to $\vec{r}$ produces torque.
- Tangential force component:
  $$ F_t=F\sin\theta $$
- Therefore:
  $$ \tau=rF_t $$
- Equivalently:
  $$ \tau=rF\sin\theta $$

---

### 10. Line of Action and Moment Arm
- The **line of action** is the line extending in the direction of the applied force.
- The **moment arm** $d$ is the shortest perpendicular distance from the pivot to the line of action.
- Geometrically:
  $$ d=r\sin\theta $$
- Therefore, torque can also be written as:
  $$ \tau=Fd $$

---

## Door Concept Question

### 11. Opening a Door
- Several forces of equal magnitude are applied to a door.
- The greatest torque is produced by the force that is:
  - applied farthest from the hinge
  - most nearly perpendicular to the door
- Pushing near the hinge produces less torque because $r$ is smaller.

---

### 12. Maximum and Zero Torque
- Maximum torque occurs when:
  $$ \theta=90^\circ $$
- Then:
  $$ \tau_{\max}=rF $$
- Zero torque occurs if:
  - the force is applied at the pivot:
    $$ r=0 $$
  - or the force is parallel to the position vector:
    $$ \theta=0^\circ \text{ or }180^\circ $$

---

## Wrench Example

### 13. Problem Setup
- A force is applied to a wrench.
- Given:
  $$ r=52\text{ cm}=0.52\text{ m} $$
  $$ F=120\text{ N} $$
  $$ \phi=33^\circ $$
- Goal:
  - calculate the torque about the pivot

---

### 14. Identify the Correct Angle
- The angle in:
  $$ \tau=rF\sin\theta $$
  must be the angle between $\vec{r}$ and $\vec{F}$.
- The labeled $33^\circ$ angle is not directly the required angle.
- From the geometry:
  $$ \theta=90^\circ-\phi $$
- Therefore:
  $$ \theta=90^\circ-33^\circ=57^\circ $$

---

### 15. Calculate the Wrench Torque
- Use:
  $$ \tau=rF\sin\theta $$
- Substitute:
  $$ \tau=(0.52)(120)\sin(57^\circ) $$
- Result:
  $$ \tau\approx52\text{ N}\cdot\text{m} $$

---

### 16. Units of Torque
- Torque units are:
  $$ \text{N}\cdot\text{m} $$
- From the formula:
  $$ \tau=rF $$
- The units are:
  $$ (\text{m})(\text{N})=\text{N}\cdot\text{m} $$

---

### 17. Direction of the Wrench Torque
- Direction is found using:
  $$ \vec{\tau}=\vec{r}\times\vec{F} $$
- The vectors $\vec{r}$ and $\vec{F}$ lie in the plane of the page.
- Therefore, the torque must point:
  - into the page
  - or out of the page
- Applying the right-hand rule gives:
  $$ \vec{\tau}\text{ points into the page} $$

---

### 18. Right-Hand Rule
- To determine the direction of:
  $$ \vec{A}\times\vec{B} $$
- Point the fingers of the right hand along $\vec{A}$.
- Curl them toward $\vec{B}$.
- The thumb points in the direction of the cross product.

---

### 19. Page-Direction Notation
- Into the page is represented by:
  $$ \otimes $$
- Out of the page is represented by:
  $$ \odot $$
- These directions are perpendicular to the plane of the diagram.

---

## Spool Pulled by a Cord

### 20. Physical Setup
- A cord is wrapped around a freely rotating solid cylindrical spool.
- Given:
  - tension $T$
  - spool mass $m$
  - spool radius $r$
- The tension is constant and tangential to the spool.
- Goal:
  - find the angular acceleration $\alpha$

---

### 21. Translational Free-Body Diagram
- Forces on the spool include:
  - weight:
    $$ mg $$
  - upward normal force:
    $$ N_1 $$
  - tension:
    $$ T $$
  - horizontal support force at the spindle:
    $$ N_2 $$
- The center of the spool does not translate, so:
  $$ \sum F_x=0 $$
  $$ \sum F_y=0 $$

---

### 22. Translational Equilibrium Equations
- Horizontal direction:
  $$ T-N_2=0 $$
- Vertical direction:
  $$ N_1-mg=0 $$
- Therefore:
  $$ N_2=T $$
  $$ N_1=mg $$

---

### 23. Extended Free-Body Diagram
- The rotation axis is through the center of the spool.
- Tension is applied tangentially at radius $r$.
- The spindle force acts at the pivot and therefore has zero moment arm.

---

### 24. Torque About the Spool Axis
- Torque from tension:
  $$ \tau_T=Tr $$
- The angle between $\vec{r}$ and $\vec{T}$ is:
  $$ 90^\circ $$
- Therefore:
  $$ \tau_T=Tr\sin90^\circ=Tr $$

---

### 25. Why the Spindle Force Produces No Torque
- The spindle force acts at the rotation axis.
- Its position relative to the pivot is:
  $$ r=0 $$
- Therefore:
  $$ \tau_{\text{spindle}}=0 $$
- The force itself is not zero; only its torque about that pivot is zero.

---

### 26. Moment of Inertia of the Spool
- For a solid cylinder rotating about its central axis:
  $$ I=\frac{1}{2}mr^2 $$

---

### 27. Angular Acceleration of the Spool
- Apply:
  $$ \sum\tau=I\alpha $$
- Therefore:
  $$ Tr=\frac{1}{2}mr^2\alpha $$
- Solve for $\alpha$:
  $$ \alpha=\frac{Tr}{\frac{1}{2}mr^2} $$
- Simplify:
  $$ \alpha=\frac{2T}{mr} $$

---

### 28. Numerical Result
- Substituting the values given in the lecture produces:
  $$ \alpha\approx2.7\text{ rad/s}^2 $$

---

## Two Rigidly Attached Solid Cylinders

### 29. Composite-Rotation Setup
- Two solid cylinders are rigidly attached and rotate together about the same central axis.
- Large cylinder:
  - mass $M$
  - radius $R$
- Small cylinder:
  - mass $m$
  - radius $r$
- A tangential force $F$ acts on the outer edge of the large cylinder.
- Angular acceleration $\alpha$ is known.
- Goal:
  - solve for the unknown mass $m$

---

### 30. Torque from the Applied Force
- Since the force is tangential at radius $R$:
  $$ \tau=FR $$

---

### 31. Total Moment of Inertia
- Because the cylinders are rigidly connected and rotate about the same axis, their moments of inertia add:
  $$ I_{\text{total}}=I_{\text{small}}+I_{\text{large}} $$
- For each solid cylinder:
  $$ I=\frac{1}{2}MR^2 $$
- Therefore:
  $$ I_{\text{total}}
  =
  \frac{1}{2}mr^2+\frac{1}{2}MR^2 $$

---

### 32. Rotational Equation of Motion
- Apply:
  $$ \sum\tau=I_{\text{total}}\alpha $$
- Therefore:
  $$ FR=
  \left(
  \frac{1}{2}mr^2+\frac{1}{2}MR^2
  \right)\alpha $$

---

### 33. Solve for the Unknown Mass
- Multiply both sides by $2/\alpha$:
  $$ \frac{2FR}{\alpha}=mr^2+MR^2 $$
- Rearrange:
  $$ mr^2=\frac{2FR}{\alpha}-MR^2 $$
- Divide by $r^2$:
  $$ m=
  \frac{2FR}{\alpha r^2}
  -
  \frac{MR^2}{r^2} $$

---

### 34. Numerical Result
- Substitution of the lecture’s numerical values gives:
  $$ m\approx2.5\text{ kg} $$

---

### 35. Explicit Unit Check
- First term:
  $$ \frac{FR}{\alpha r^2} $$
- Units:
  $$
  \frac{
  (\text{kg}\cdot\text{m/s}^2)(\text{m})
  }{
  (\text{s}^{-2})(\text{m}^2)
  }
  =\text{kg}
  $$
- Second term:
  $$ \frac{MR^2}{r^2} $$
- Units:
  $$ \frac{(\text{kg})(\text{m}^2)}{\text{m}^2}=\text{kg} $$
- Both terms have the correct units of mass.

---

### 36. Main Physics Takeaways
- Torque is:
  $$ \vec{\tau}=\vec{r}\times\vec{F} $$
- Torque magnitude is:
  $$ \tau=rF\sin\theta=Fd $$
- Rotational dynamics is governed by:
  $$ \sum\vec{\tau}=I\vec{\alpha} $$
- Forces applied farther from the pivot generally produce more torque.
- Forces applied at the pivot produce zero torque about that pivot.
- For composite rigid bodies rotating about the same axis:
  $$ I_{\text{total}}=\sum_i I_i $$

---

### 37. Main Problem-Solving Strategy
1. Identify the pivot or rotation axis.
2. Draw an extended free-body diagram.
3. Determine the correct position vector $\vec{r}$ for each force.
4. Determine the angle between $\vec{r}$ and $\vec{F}$.
5. Calculate each torque using:
   $$ \tau=rF\sin\theta $$
6. Assign torque directions using the right-hand rule.
7. Add moments of inertia for rigidly attached objects.
8. Apply:
   $$ \sum\tau=I\alpha $$
9. Solve symbolically before substituting numbers.
10. Perform an explicit unit check.
