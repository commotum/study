## Lecture Outline (Circular Motion Dynamics: Ferris Wheel Forces and Turntable Friction)

### 1. Opening Course Logistics
- The lecture begins with Week 2 course updates.
- Current course topic:
  $$ \text{Chapter 8: Circular Motion} $$
- Upcoming topic:
  $$ \text{Chapter 12} $$
- Homework 2 covers Chapter 8 and is due:
  $$ \text{July 3} $$

---

### 2. Proctorio Practice Quiz
- Students only need to complete the Proctorio practice quiz if they plan to take quizzes asynchronously using Proctorio.
- Students taking quizzes live in Zoom do **not** need to complete the Proctorio practice quiz.
- Students using Proctorio should first read:
  $$ \text{Proctorio Setup and Troubleshooting} $$

---

### 3. Quiz 1 Notes Requirement
- Students must submit a handwritten note sheet before taking Quiz 1.
- The note sheet should be:
  - handwritten
  - between half a page and one full page
  - the student’s own work
  - submitted to Gradescope
- A photo ID should be placed on top of the notes when scanning/uploading.
- The note sheet may include:
  - equations
  - diagrams
  - notes
  - reminders

---

### 4. Quiz 1 Format
- Quiz 1 has two parts:
  $$ \text{Quiz 1A} $$
  $$ \text{Quiz 1B} $$
- Quiz 1A contains:
  - three multiple-choice questions
  - one short written question
- Quiz 1B contains:
  - one longer written question
- Students must complete both parts.

---

### 5. Quiz Timing
- Each quiz part is open for:
  $$ 20\ \mathrm{min} $$
- Students then have:
  $$ 5\ \mathrm{min} $$
  to upload written work to Gradescope.
- If written work is not uploaded within the upload window, credit for that written question may be lost.

---

### 6. Quiz Options
- Students may take quizzes:
  - asynchronously with Proctorio
  - live in Zoom at the scheduled lecture time
  - live in the evening Zoom session
- For live Zoom quizzes:
  - webcam must be on
  - student must be visible
  - quiz must be taken during the Zoom session

---

### 7. Quiz Practice Problems
- A practice quiz will be posted before Quiz 1.
- It will have the same format:
  - three multiple choice
  - one short written
  - one longer written
- It will be a document, not a Canvas quiz.
- Solutions will be posted separately.

---

### 8. Quiz Extra Credit
- After quizzes are graded, a quiz extra credit assignment opens.
- Students choose the question where they lost the most points.
- The extra credit asks students to explain:
  - why they did what they did
  - what they should have done
  - the correct solution
  - covariational reasoning
  - explicit unit analysis
- Students also meet with someone to discuss the problem, such as:
  - the instructor
  - a Wormhole tutor
  - a lab TA

---

### 9. Dropped Scores
- The course drops:
  - one quiz Part A score
  - one quiz Part B score
  - three pre-lecture scores
  - three participation scores
  - one homework score
- Labs are not dropped.

---

## Circular Motion Review

### 10. Uniform Circular Motion
- Uniform circular motion means motion in a circle at constant speed.
- Constant speed does **not** mean constant velocity because velocity direction changes.
- Since velocity changes direction, there is acceleration.

---

### 11. Nonuniform Circular Motion
- Nonuniform circular motion means:
  - motion is circular
  - speed is not constant
- In this case, acceleration has both:
  - radial component
  - tangential component

---

### 12. Radial Acceleration
- Radial acceleration points inward, toward the center of the circle.
- Magnitude:
  $$ a_r=\frac{v^2}{r} $$
- Since:
  $$ v=r\omega $$
- Radial acceleration can also be written as:
  $$ a_r=r\omega^2 $$

---

### 13. Tangential and Radial Components
- Choose $\hat{r}$ inward and $\hat{t}$ along the motion. Acceleration can then be resolved into:
  $$ \vec{a}=a_r\hat{r}+a_t\hat{t} $$
- Radial acceleration changes the direction of velocity.
- Tangential acceleration changes the speed.

---

### 14. Period and Speed
- For uniform circular motion, speed can be written as:
  $$ v=\frac{2\pi r}{T} $$
- Here:
  - $r$ is radius
  - $T$ is period

---

### 15. Angular Kinematics Review
- For constant angular acceleration:
  $$ \omega_f=\omega_0+\alpha\Delta t $$
  $$ \theta_f=\theta_0+\omega_0\Delta t+\frac{1}{2}\alpha(\Delta t)^2 $$
  $$ \omega_f^2=\omega_0^2+2\alpha(\theta_f-\theta_0) $$

---

## Ferris Wheel Example 1: Speed from Angular Velocity

### 16. Problem Setup
- A Ferris wheel has:
  $$ r=42\ \mathrm{m} $$
  $$ \omega=0.16\ \mathrm{rad}/\mathrm{s} $$
- Find the speed of a particle on the rim.

---

### 17. Use the Tangential Speed Formula
- Tangential speed:
  $$ v=r\omega $$
- Substitute:
  $$ v=(0.16)(42) $$
- Result:
  $$ v=6.72\ \mathrm{m}/\mathrm{s} $$
- Rounded appropriately:
  $$ v\approx 6.7\ \mathrm{m}/\mathrm{s} $$

---

### 18. Units Note
- Angular velocity has units:
  $$ \mathrm{rad}/\mathrm{s} $$
- Radians are treated as dimensionless, so:
  $$ (\mathrm{rad}/\mathrm{s})(\mathrm{m})=\mathrm{m}/\mathrm{s} $$

---

## Ferris Wheel Example 2: Comparing Normal Force at Top and Bottom

### 19. Physical Setup
- A person rides on a Ferris wheel.
- Compare the normal force from the seat:
  - at the top of the wheel
  - at the bottom of the wheel

---

### 20. Intuitive Result
- At the bottom, the rider feels pushed harder into the seat.
- At the top, the rider feels lighter.
- Therefore:
  $$ N_{\mathrm{bottom}}>N_{\mathrm{top}} $$

---

### 21. Free-Body Diagram at the Top
- Forces on the rider:
  - weight downward:
    $$ mg $$
  - normal force upward:
    $$ N_{\mathrm{top}} $$
- At the top, radial acceleration points downward toward the center.
- Choose downward as positive.
- Force equation:
  $$ \sum F_r=m a_r $$
  $$ mg-N_{\mathrm{top}}=m a_r=m\frac{v^2}{r} $$

---

### 22. Normal Force at the Top
- Solve for normal force:
  $$ N_{\mathrm{top}}=mg-m\frac{v^2}{r} $$
- Since:
  $$ v=r\omega $$
- Then:
  $$ \frac{v^2}{r}=r\omega^2 $$
- So:
  $$ N_{\mathrm{top}}=m(g-\omega^2 r) $$

---

### 23. Free-Body Diagram at the Bottom
- Forces on the rider:
  - weight downward:
    $$ mg $$
  - normal force upward:
    $$ N_{\mathrm{bottom}} $$
- At the bottom, radial acceleration points upward toward the center.
- Choose upward as positive.
- Force equation:
  $$ \sum F_r=m a_r=m\frac{v^2}{r}=N_{\mathrm{bottom}}-mg $$

---

### 24. Normal Force at the Bottom
- Solve for normal force:
  $$ N_{\mathrm{bottom}}=mg+m\frac{v^2}{r} $$
- Using:
  $$ \frac{v^2}{r}=r\omega^2 $$
- Then:
  $$ N_{\mathrm{bottom}}=m(g+\omega^2 r) $$

---

### 25. Numerical Values for Ferris Wheel Normal Forces
- Given:
  $$ m=68\ \mathrm{kg} $$
  $$ r=42\ \mathrm{m} $$
  $$ \omega=0.16\ \mathrm{rad}/\mathrm{s} $$
  $$ g=9.81\ \mathrm{m}/\mathrm{s}^2 $$

---

### 26. Normal Force at the Bottom
- Use:
  $$ N_{\mathrm{bottom}}=m(g+\omega^2 r) $$
- Substitute:
  $$ N_{\mathrm{bottom}}=68\left(9.81+(0.16)^2(42)\right) $$
- Result:
  $$ N_{\mathrm{bottom}}\approx740\ \mathrm{N} $$

---

### 27. Normal Force at the Top
- Use:
  $$ N_{\mathrm{top}}=m(g-\omega^2 r) $$
- Substitute:
  $$ N_{\mathrm{top}}=68\left(9.81-(0.16)^2(42)\right) $$
- Result:
  $$ N_{\mathrm{top}}\approx590\ \mathrm{N} $$

---

### 28. Comparison
- The bottom normal force is larger:
  $$ N_{\mathrm{bottom}}\approx740\ \mathrm{N} $$
- The top normal force is smaller:
  $$ N_{\mathrm{top}}\approx590\ \mathrm{N} $$
- Therefore:
  $$ N_{\mathrm{bottom}}>N_{\mathrm{top}} $$

---

### 29. Why the Normal Force Changes
- At the bottom, the normal force must both:
  - balance weight
  - provide inward radial acceleration
- At the top, gravity already points inward, so the seat provides less normal force.

---

## Sign Convention for Circular Motion Forces

### 30. Choosing the Positive Radial Direction
- The instructor chooses the positive radial direction toward the center of the circle.
- At the top:
  $$ +r \text{ is downward} $$
- At the bottom:
  $$ +r \text{ is upward} $$
- This keeps:
  $$ a_r=\frac{v^2}{r} $$
  positive in the radial equation.

---

### 31. Importance of Free-Body Diagrams
- The lecture emphasizes starting with a free-body diagram.
- For circular motion:
  - draw all real forces
  - identify the radial direction
  - choose the positive direction toward the center
  - write Newton’s second law in the radial direction

---

### 32. Symbolic Solutions First
- Students are encouraged to solve symbolically before plugging in numbers.
- Example:
  $$ N_{\mathrm{bottom}}=m(g+\omega^2 r) $$
- This is preferred over inserting numbers too early.
- Quiz problems may ask for symbolic answers without numbers.

---

### 33. Significant Figures Note
- In Canvas numerical questions, too many or too few significant figures may fall outside the accepted range.
- In written quiz work, significant-figure errors may cost a small amount, but the symbolic setup is usually worth more.

---

## Turntable and Static Friction Example

### 34. Problem Setup
- A coin sits on a rotating turntable.
- Given:
  - mass:
    $$ m $$
  - radius:
    $$ r $$
  - coefficient of static friction:
    $$ \mu_s=0.24 $$
- Find the maximum angular speed $\omega_{\max,\mathrm{turntable}}$ at which the coin just starts to slip.

---

### 35. Forces on the Coin
- Free-body diagram:
  - weight downward:
    $$ mg $$
  - normal force upward:
    $$ N $$
  - static friction inward:
    $$ f_s $$
- Static friction provides the radial force needed for circular motion.

---

### 36. Vertical Force Balance
- There is no vertical acceleration:
  $$ \sum F_y=0 $$
- So:
  $$ N-mg=0 $$
- Therefore:
  $$ N=mg $$

---

### 37. Radial Force Equation
- Radial acceleration:
  $$ a_r=\frac{v^2}{r} $$
- Newton’s second law in the radial direction:
  $$ \sum F_r=m a_r $$
- The only radial force is friction:
  $$ \sum F_r=m a_r=m\frac{v^2}{r}=f_s $$

---

### 38. Maximum Static Friction
- At the threshold of slipping:
  $$ f_s=f_{s,\max} $$
- Maximum static friction:
  $$ f_{s,\max}=\mu_s N $$
- Since:
  $$ N=mg $$
- Then:
  $$ f_{s,\max}=\mu_s mg $$

---

### 39. Solve for the Critical Speed
- Set the required net inward force equal to maximum static friction:
  $$ \sum F_r=m a_r=m\frac{v_{\max,\mathrm{turntable}}^2}{r}=f_{s,\max}=\mu_s mg $$
- Cancel mass:
  $$ \frac{v_{\max,\mathrm{turntable}}^2}{r}=\mu_s g $$

---

### 40. Solve for Critical Angular Speed
- Use:
  $$ v_{\max,\mathrm{turntable}}=\omega_{\max,\mathrm{turntable}}r $$
- Then:
  $$ \frac{(\omega_{\max,\mathrm{turntable}}r)^2}{r}=\mu_s g $$
- Simplify:
  $$ \omega_{\max,\mathrm{turntable}}^2 r=\mu_s g $$
- Solve:
  $$ \omega_{\max,\mathrm{turntable}}=\sqrt{\frac{\mu_s g}{r}} $$

---

### 41. Interpretation of the Turntable Result
- The mass cancels, so the slipping condition does not depend on the coin’s mass.
- If $\mu_s$ increases, the coin can rotate faster before slipping:
  $$ \omega_{\max,\mathrm{turntable}}\propto\sqrt{\mu_s} $$
- If $r$ increases, the coin slips at a lower angular speed:
  $$ \omega_{\max,\mathrm{turntable}}\propto\frac{1}{\sqrt{r}} $$

---

### 42. Main Physics Takeaways
- Circular motion requires an inward net force:
  $$ \sum F_r=m a_r=m\frac{v^2}{r} $$
- Radial acceleration can be written as:
  $$ a_r=\frac{v^2}{r}=r\omega^2 $$
- For Ferris wheel motion:
  $$ N_{\mathrm{bottom}}=m(g+\omega^2 r) $$
  $$ N_{\mathrm{top}}=m(g-\omega^2 r) $$
- For a coin on a turntable:
  $$ \omega_{\max,\mathrm{turntable}}=\sqrt{\frac{\mu_s g}{r}} $$
- Always identify which real force or combination of forces produces the inward net force associated with $a_r$.

---

### 43. Main Problem-Solving Takeaways
- Start with a free-body diagram.
- Choose the radial positive direction toward the center.
- Write:
  $$ \sum F_r=m a_r $$
- Use:
  $$ a_r=\frac{v^2}{r}=r\omega^2 $$
- Solve symbolically before substituting numbers.
