## Lecture Outline (Static Equilibrium, Tipping, Ladder Friction, and Massive Pulley Dynamics)

### 1. Quiz 1 Grading
- Quiz 1 scores are posted in Canvas.
- For students who took the asynchronous quiz:
  - Gradescope contains the submitted written work
  - the corresponding Canvas quiz score is the score used in the course-grade calculation
  - the separate Gradescope assignment column does not add extra weight
- Students can inspect the grading rubric by opening the question in Gradescope.

---

### 2. Regrade Requests
- Regrade requests are submitted through Gradescope.
- Regrade requests remain available for:
  $$ 15\text{ days} $$
- A request should clearly identify:
  - the part being disputed
  - the relevant physics concepts
  - why the existing grading should be reconsidered

---

### 3. Quiz 1 Extra Credit
- The Quiz 1X assignment focuses on the single question where the student lost the most points.
- The assignment asks students to explain:
  - why they used their original approach
  - what they should have done instead
  - the correct solution
  - covariational reasoning
  - explicit unit analysis
- Students must also discuss the problem with:
  - the instructor
  - a TA
  - or a Wormhole tutor

---

### 4. Quiz 2 Logistics
- The Proctorio version opens:
  $$ 5{:}00\text{ PM Saturday} $$
- It closes:
  $$ 5{:}00\text{ PM Monday} $$
- Zoom quiz sessions are held Monday at:
  $$ 11{:}00\text{ AM} $$
  and:
  $$ 6{:}00\text{ PM} $$
- Students should begin preparing their handwritten Quiz 2 note sheet.
- Useful items include:
  - standard moments of inertia
  - parallel-axis theorem
  - torque equations
  - rotational dynamics equations

---

## Review of Rotational Mechanics

### 5. Center of Mass
- For discrete masses:
  $$ x_{\text{cm}}=\frac{\sum_i m_ix_i}{\sum_i m_i} $$
- For a continuous object:
  $$ x_{\text{cm}}=\frac{1}{M}\int x\,dm $$

---

### 6. Rotational Kinetic Energy
- Rotational kinetic energy:
  $$ K_{\text{rot}}=\frac{1}{2}I\omega^2 $$
- The moment of inertia $I$ describes how mass is distributed relative to the rotation axis.

---

### 7. Parallel-Axis Theorem
- If the rotation axis is a distance $d$ from a parallel axis through the center of mass:
  $$ I=I_{\text{cm}}+Md^2 $$

---

### 8. Torque
- Vector definition:
  $$ \vec{\tau}=\vec{r}\times\vec{F} $$
- Magnitude:
  $$ \tau=rF\sin\theta $$
- Rotational equation of motion:
  $$ \sum\tau=I\alpha $$

---

### 9. Extended Free-Body Diagrams
- An extended free-body diagram shows:
  - every force acting on the object
  - where each force acts
  - the pivot point
  - the distance from the pivot to each force
  - the angle between $\vec{r}$ and $\vec{F}$
- These details are needed to calculate torque.

---

### 10. Contact Forces vs. Weight
- If an object rests on a plank, the force it exerts on the plank is a **normal force**, not its gravitational force.
- For an object in vertical equilibrium, the normal-force magnitude may equal its weight:
  $$ N=mg $$
- Even when the magnitudes are equal, they are different forces acting on different objects.

---

## Example 1: Plank Just Beginning to Tip

### 11. Problem Setup
- A uniform plank has:
  - length $L$
  - mass $M$
- It rests on two supports:
  - support $A$ at:
    $$ \frac{L}{5} $$
    from the left end
  - support $B$ at:
    $$ \frac{2L}{3} $$
    from the left end
- A box of mass $m$ is placed a distance $x$ to the right of support $B$.
- Goal: find $x$ when the plank just begins to tip.

---

### 12. Tipping Condition
- As the plank begins to tip about support $B$, it loses contact with support $A$.
- Therefore:
  $$ N_A=0 $$
- The pivot point is support $B$.
- The angular acceleration is zero at the threshold:
  $$ \alpha=0 $$
- Therefore:
  $$ \sum\tau_B=0 $$

---

### 13. Box Free-Body Diagram
- Forces on the box:
  - weight downward:
    $$ mg $$
  - normal force from the plank upward:
    $$ N_{M\to m} $$
- Since the box is in vertical equilibrium:
  $$ N_{M\to m}-mg=0 $$
- Therefore:
  $$ N_{M\to m}=mg $$

---

### 14. Force Exerted by the Box on the Plank
- By Newton’s third law, the box pushes downward on the plank with equal magnitude:
  $$ N_{m\to M}=mg $$

---

### 15. Plank’s Center of Mass
- Since the plank is uniform, its center of mass is at:
  $$ \frac{L}{2} $$
  from the left end.
- Support $B$ is at:
  $$ \frac{2L}{3} $$
- The distance between support $B$ and the plank’s center is:
  $$ \frac{2L}{3}-\frac{L}{2}=\frac{L}{6} $$

---

### 16. Torque Balance About Support $B$
- Choose clockwise torque as positive.
- The box produces clockwise torque:
  $$ \tau_{\text{box}}=mgx $$
- The plank’s weight produces counterclockwise torque:
  $$ \tau_{\text{plank}}=Mg\frac{L}{6} $$
- At the tipping threshold:
  $$ mgx-Mg\frac{L}{6}=0 $$

---

### 17. Solve for the Box Position
- Rearrange:
  $$ mgx=Mg\frac{L}{6} $$
- Cancel $g$:
  $$ mx=M\frac{L}{6} $$
- Therefore:
  $$ x=\frac{ML}{6m} $$

---

### 18. Numerical Result
- Given:
  $$ M=2.4\text{ kg} $$
  $$ m=1.6\text{ kg} $$
  $$ L=1.4\text{ m} $$
- Then:
  $$ x=\frac{(2.4)(1.4)}{6(1.6)} $$
- Result:
  $$ x=0.35\text{ m} $$

---

### 19. Physical Check
- The box must be:
  - to the right of support $B$
  - still located on the plank
- The result:
  $$ x=0.35\text{ m} $$
  satisfies those physical conditions.

---

## Example 2: Ladder Against a Frictionless Wall

### 20. Problem Setup
- A uniform ladder has:
  - length $L$
  - mass $m$
  - angle $\theta$ above the floor
- The wall is frictionless.
- The floor has coefficient of static friction $\mu_s$.
- The ladder is just at the threshold of slipping.
- Goal: find $\mu_s$.

---

### 21. Forces on the Ladder
- Gravitational force at the center:
  $$ mg $$
- Normal force from the floor:
  $$ N_F $$
- Static friction from the floor:
  $$ f_s $$
- Normal force from the wall:
  $$ N_W $$
- Since the wall is frictionless, no wall-friction force acts.

---

### 22. Vertical Equilibrium
- The ladder has no vertical acceleration:
  $$ \sum F_y=0 $$
- Therefore:
  $$ N_F-mg=0 $$
- So:
  $$ N_F=mg $$

---

### 23. Horizontal Equilibrium
- The floor friction balances the wall’s normal force:
  $$ N_W=f_s $$
- At the threshold of slipping:
  $$ f_s=f_{s,\max}=\mu_sN_F $$
- Since $N_F=mg$:
  $$ N_W=\mu_smg $$

---

### 24. Choose the Pivot
- Choose the bottom of the ladder as the pivot.
- The floor normal force and floor friction act at the pivot, so they produce no torque about that point.

---

### 25. Torque from the Wall
- The wall normal force acts at the top of the ladder.
- Its torque magnitude is:
  $$ \tau_W=N_WL\sin\theta $$

---

### 26. Torque from the Ladder’s Weight
- The weight acts at the ladder’s center:
  $$ r=\frac{L}{2} $$
- The relevant angle gives:
  $$ \sin(90^\circ-\theta)=\cos\theta $$
- Therefore:
  $$ \tau_g=mg\frac{L}{2}\cos\theta $$

---

### 27. Torque Equilibrium
- Set clockwise and counterclockwise torques equal:
  $$ N_WL\sin\theta
     =
     mg\frac{L}{2}\cos\theta $$
- Substitute:
  $$ N_W=\mu_smg $$
- Then:
  $$ \mu_smgL\sin\theta
     =
     mg\frac{L}{2}\cos\theta $$

---

### 28. Solve for the Static-Friction Coefficient
- Cancel $mgL$:
  $$ \mu_s\sin\theta=\frac{1}{2}\cos\theta $$
- Therefore:
  $$ \mu_s=\frac{1}{2}\frac{\cos\theta}{\sin\theta} $$
- Equivalent forms:
  $$ \mu_s=\frac{1}{2}\cot\theta $$
  $$ \mu_s=\frac{1}{2\tan\theta} $$

---

### 29. Numerical Result
- Substituting the angle given in the lecture problem gives:
  $$ \mu_s\approx0.34 $$

---

### 30. Main Lesson from the Ladder Problem
- The key step is constructing the extended free-body diagram correctly.
- The torque equation depends on:
  - where each force acts
  - its distance from the pivot
  - the angle between the force and position vectors

---

## Example 3: Atwood Machine with a Massive Pulley

### 31. Problem Setup
- Two masses are connected by a string passing over a massive pulley:
  $$ m_1<m_2 $$
- Pulley:
  - mass $M_p$
  - radius $r$
  - modeled as a solid disk
- The heavier mass $m_2$ moves downward.
- The lighter mass $m_1$ moves upward.
- Goal: find the acceleration magnitude $a$.

---

### 32. Unequal String Tensions
- Because the pulley has rotational inertia, the tensions are not equal:
  $$ T_2>T_1 $$
- The tension difference produces the pulley’s angular acceleration.
- For a massless pulley:
  $$ T_1=T_2 $$
- For a massive pulley:
  $$ T_1\ne T_2 $$

---

### 33. Force Equation for $m_1$
- Choose upward as positive for $m_1$:
  $$ \sum F_y=m_1a $$
- Therefore:
  $$ T_1-m_1g=m_1a $$
- Solve:
  $$ T_1=m_1g+m_1a $$

---

### 34. Force Equation for $m_2$
- Choose downward as positive for $m_2$:
  $$ \sum F_y=m_2a $$
- Therefore:
  $$ m_2g-T_2=m_2a $$
- Solve:
  $$ T_2=m_2g-m_2a $$

---

### 35. Pulley Torque Equation
- Choose clockwise rotation as positive.
- Torque from $T_2$:
  $$ +T_2r $$
- Torque from $T_1$:
  $$ -T_1r $$
- Therefore:
  $$ (T_2-T_1)r=I\alpha $$

---

### 36. Pulley Moment of Inertia
- For a solid-disk pulley:
  $$ I=\frac{1}{2}M_pr^2 $$

---

### 37. No-Slip Condition
- The string does not slip on the pulley:
  $$ a=\alpha r $$
- Therefore:
  $$ \alpha=\frac{a}{r} $$

---

### 38. Substitute into the Torque Equation
- Start with:
  $$ (T_2-T_1)r
     =
     \left(\frac{1}{2}M_pr^2\right)\frac{a}{r} $$
- Cancel $r$:
  $$ T_2-T_1=\frac{1}{2}M_pa $$

---

### 39. Substitute the Tensions
- Use:
  $$ T_2=m_2g-m_2a $$
  $$ T_1=m_1g+m_1a $$
- Then:
  $$
  (m_2g-m_2a)-(m_1g+m_1a)
  =
  \frac{1}{2}M_pa
  $$

---

### 40. Solve for the Acceleration
- Rearrange:
  $$ (m_2-m_1)g
     =
     \left(m_1+m_2+\frac{M_p}{2}\right)a $$
- Therefore:
  $$
  a=
  \frac{(m_2-m_1)g}
       {m_1+m_2+\frac{M_p}{2}}
  $$

---

### 41. Numerical Result
- Substituting the values from the lecture gives:
  $$ a\approx2.5\text{ m/s}^2 $$

---

### 42. Effect of Pulley Mass
- The term:
  $$ \frac{M_p}{2} $$
  appears in the denominator because some of the gravitational energy accelerates the rotating pulley.
- Increasing pulley mass decreases the system’s acceleration.

---

### 43. Massless-Pulley Limit
- If:
  $$ M_p\to0 $$
- Then:
  $$
  a\to
  \frac{(m_2-m_1)g}{m_1+m_2}
  $$
- This is the standard Atwood-machine result for a massless pulley.

---

### 44. Main Physics Takeaways
- At the tipping threshold:
  $$ \sum\tau=0 $$
  and the unused support force becomes zero.
- Static-equilibrium problems require both:
  $$ \sum\vec{F}=0 $$
  and:
  $$ \sum\tau=0 $$
- A force acting at the pivot produces no torque about that pivot.
- For a massive pulley:
  $$ T_1\ne T_2 $$
- Translational and rotational motion are connected through:
  $$ a=\alpha r $$

---

### 45. Main Problem-Solving Strategy
1. Identify the object or system being analyzed.
2. Draw point free-body diagrams for translating objects.
3. Draw an extended free-body diagram for rotating objects.
4. Select a useful pivot point.
5. Write:
   $$ \sum\vec{F}=m\vec{a} $$
6. Write:
   $$ \sum\tau=I\alpha $$
7. Apply geometric constraints such as:
   $$ a=\alpha r $$
8. Solve symbolically before substituting numbers.
9. Check the result using units and physical reasoning.
