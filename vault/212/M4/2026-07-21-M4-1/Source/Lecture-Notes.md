## Lecture Outline (Simple Harmonic Motion, Oscillations, and Spring Energy)

### 1. Course Logistics
- Quiz 2 is being graded.
- Quiz 1 extra credit is also being graded.
- The course is beginning Quiz 3 material:
  - oscillations
  - simple harmonic motion
  - waves
- Students should begin preparing their Quiz 3 note sheet.
- Students must submit their Quiz 2 note sheet with a photo ID to receive full Quiz 2 credit.

---

## Oscillations and Waves

### 2. Introduction to Simple Harmonic Motion
- Simple harmonic motion is motion described by a sine or cosine function.
- Examples include:
  - a mass oscillating on a spring
  - a pendulum moving back and forth
  - the projection of uniform circular motion onto one dimension

---

### 3. Circular-Motion Interpretation
- Consider a point moving around a circle at constant speed.
- The velocity is not constant because its direction changes.
- Projecting the circular motion onto a one-dimensional axis produces sinusoidal motion.
- This provides a geometric interpretation of simple harmonic motion.

---

### 4. Oscillation vs. Wave
- An **oscillation** is repeated motion occurring at a particular location.
- Examples:
  - a pendulum
  - a mass on a spring
- A **wave** is an oscillation that propagates through space.
- A wave can be viewed as a collection of many coupled oscillators.
- For a wave on a string, each point on the string oscillates while the disturbance travels along the string.

---

### 5. Oscillating Sources and Waves
- Waves are commonly produced by oscillating sources.
- The source and the resulting wave have the same frequency.
- The course first studies individual oscillators and then extends the ideas to wave propagation.

---

## Sinusoidal Description of Motion

### 6. General Position Function
- A general sinusoidal position function is:
  $$ x(t)=A\cos(\omega t+\phi) $$
- Here:
  - $A$ is the amplitude
  - $\omega$ is the angular frequency
  - $\phi$ is the phase constant
  - $t$ is time

---

### 7. Cosine as the Standard Starting Form
- If a mass is pulled to its maximum displacement and released at $t=0$, then:
  $$ \phi=0 $$
- The position can then be written as:
  $$ x(t)=A\cos(\omega t) $$
- A sine and cosine describe the same type of motion, differing only by a phase shift.

---

### 8. Amplitude
- The amplitude is the maximum displacement from equilibrium:
  $$ A=|x|_{\max} $$
- The oscillator moves between:
  $$ x=-A $$
  and:
  $$ x=+A $$

---

### 9. Period
- The period $T$ is the time required for one complete oscillation.
- It may be measured:
  - peak to peak
  - trough to trough
  - or between any two equivalent points in consecutive cycles

---

### 10. Frequency
- Frequency is the number of oscillations per unit time:
  $$ f=\frac{1}{T} $$
- Its SI unit is hertz:
  $$ 1\ \mathrm{Hz}=1\ \mathrm{cycle}/\mathrm{s} $$

---

### 11. Angular Frequency
- Angular frequency is related to ordinary frequency by:
  $$ \omega=2\pi f $$
- Since:
  $$ f=\frac{1}{T} $$
- We also have:
  $$ \omega=\frac{2\pi}{T} $$
- Angular frequency has units:
  $$ \mathrm{rad}/\mathrm{s} $$

---

## Velocity and Acceleration in Simple Harmonic Motion

### 12. Velocity Function
- Begin with:
  $$ x(t)=A\cos(\omega t) $$
- Velocity is the derivative of position:
  $$ v(t)=\frac{dx}{dt} $$
- Applying the chain rule:
  $$ v(t)=-A\omega\sin(\omega t) $$

---

### 13. Maximum Speed
- Since the largest possible magnitude of $\sin(\omega t)$ is $1$:
  $$ v_{\max}=A\omega $$
- The oscillator reaches maximum speed when passing through equilibrium:
  $$ x=0 $$

---

### 14. Acceleration Function
- Acceleration is the derivative of velocity:
  $$ a(t)=\frac{dv}{dt} $$
- Therefore:
  $$ a(t)=-A\omega^2\cos(\omega t) $$
- Since:
  $$ x(t)=A\cos(\omega t) $$
- Acceleration can also be written as:
  $$ a(t)=-\omega^2x(t) $$

---

### 15. Restoring Acceleration
- The negative sign in:
  $$ a(t)=-\omega^2x(t) $$
  means the acceleration always points opposite the displacement.
- Therefore, acceleration always points toward equilibrium.
- This restoring behavior is a defining property of simple harmonic motion.

---

### 16. Maximum Acceleration
- At maximum displacement:
  $$ x=\pm A $$
- The acceleration magnitude is maximum:
  $$ a_{\max}=\omega^2A $$
- At equilibrium:
  $$ x=0 $$
  so:
  $$ a=0 $$

---

## Relationships Among the Graphs

### 17. Position and Velocity
- Velocity is the slope of the position graph.
- When position passes through equilibrium:
  $$ x=0 $$
  the slope of $x(t)$ is greatest in magnitude.
- Therefore:
  $$ |v|=v_{\max} $$

---

### 18. Position and Acceleration
- Acceleration is opposite in sign to position:
  $$ a(t)=-\omega^2x(t) $$
- When position is at a positive maximum, acceleration is at a negative maximum.
- When position is at a negative maximum, acceleration is at a positive maximum.

---

### 19. Velocity and Acceleration
- Acceleration is the slope of the velocity graph.
- When velocity is at a maximum or minimum, its slope is zero:
  $$ a=0 $$
- When velocity passes through zero, its slope has maximum magnitude:
  $$ |a|=a_{\max} $$

---

## Energy of a Mass–Spring Oscillator

### 20. Hooke’s Law
- The restoring force exerted by a spring is:
  $$ F=-kx $$
- Here:
  - $k$ is the spring constant
  - $x$ is displacement from equilibrium
- The negative sign indicates that the force points toward equilibrium.

---

### 21. Spring Potential Energy
- Force and potential energy are related by:
  $$ F=-\frac{dU}{dx} $$
- Using:
  $$ F=-kx $$
- We obtain:
  $$ \frac{dU}{dx}=kx $$
- Integrating:
  $$ U(x)=\frac{1}{2}kx^2 $$

---

### 22. Total Mechanical Energy
- For an ideal mass–spring oscillator:
  $$ E=K+U $$
- Therefore:
  $$ E=\frac{1}{2}mv^2+\frac{1}{2}kx^2 $$
- With no dissipative forces, the total energy remains constant.

---

### 23. Energy at Equilibrium
- At equilibrium:
  $$ x=0 $$
- Spring potential energy is zero:
  $$ U=0 $$
- Speed is maximum:
  $$ v=v_{\max} $$
- All the energy is kinetic:
  $$ E=\frac{1}{2}mv_{\max}^2 $$

---

### 24. Energy at Maximum Displacement
- At either turning point:
  $$ x=\pm A $$
- Velocity is zero:
  $$ v=0 $$
- All the energy is spring potential energy:
  $$ E=\frac{1}{2}kA^2 $$

---

### 25. Angular Frequency of a Mass–Spring System
- Equate the energy at equilibrium and at maximum displacement:
  $$ \frac{1}{2}mv_{\max}^2=\frac{1}{2}kA^2 $$
- Use:
  $$ v_{\max}=\omega A $$
- Then:
  $$ m(\omega A)^2=kA^2 $$
- Cancel $A^2$:
  $$ m\omega^2=k $$
- Therefore:
  $$ \omega=\sqrt{\frac{k}{m}} $$

---

### 26. Period and Frequency of a Mass–Spring System
- Since:
  $$ \omega=\frac{2\pi}{T} $$
- The period is:
  $$ T=2\pi\sqrt{\frac{m}{k}} $$
- The frequency is:
  $$ f=\frac{1}{2\pi}\sqrt{\frac{k}{m}} $$

---

## Graph-Reading Example

### 27. Amplitude from the Graph
- The plotted oscillator has amplitude:
  $$ A=2.5\ \mathrm{cm} $$

---

### 28. Period from the Graph
- One complete oscillation takes:
  $$ T=4.0\ \mathrm{s} $$

---

### 29. Frequency from the Graph
- Use:
  $$ f=\frac{1}{T} $$
- Therefore:
  $$ f=\frac{1}{4.0\ \mathrm{s}} $$
- Result:
  $$ f=0.25\ \mathrm{Hz} $$

---

### 30. Angular Frequency from the Graph
- Use:
  $$ \omega=2\pi f $$
- Therefore:
  $$ \omega=2\pi(0.25) $$
- Result:
  $$ \omega=\frac{\pi}{2}\ \mathrm{rad}/\mathrm{s} $$
- Numerically:
  $$ \omega\approx1.57\ \mathrm{rad}/\mathrm{s} $$

---

### 31. Maximum Speed from the Graph
- Use:
  $$ v_{\max}=\omega A $$
- Substitute:
  $$ v_{\max}
  =
  \left(\frac{\pi}{2}\ \mathrm{rad}/\mathrm{s}\right)
  (2.5\ \mathrm{cm}) $$
- Result:
  $$ v_{\max}\approx3.9\ \mathrm{cm}/\mathrm{s} $$

---

## Mass–Spring Position and Velocity Example

### 32. Given Information
- Equilibrium position:
  $$ x_{\mathrm{eq}}=0.35\ \mathrm{m} $$
- Initial release position:
  $$ x_{\mathrm{release}}=0.48\ \mathrm{m} $$
- Number of oscillations:
  $$ 12 $$
- Elapsed time:
  $$ 7.0\ \mathrm{s} $$
- Evaluate the motion at:
  $$ t=3.9\ \mathrm{s} $$

---

### 33. Amplitude
- The amplitude relative to equilibrium is:
  $$ A=x_{\mathrm{release}}-x_{\mathrm{eq}} $$
- Therefore:
  $$ A=0.48-0.35 $$
- Result:
  $$ A=0.13\ \mathrm{m} $$

---

### 34. Frequency and Angular Frequency
- The frequency is:
  $$ f=\frac{12}{7.0\ \mathrm{s}} $$
- Therefore:
  $$ f\approx1.71\ \mathrm{Hz} $$
- Angular frequency:
  $$ \omega=2\pi f=\frac{24\pi}{7}\ \mathrm{rad}/\mathrm{s} $$

---

### 35. Position at $t=3.9\ \mathrm{s}$
- Position relative to equilibrium:
  $$ y(t)=A\cos(2\pi ft) $$
- Substitute:
  $$ y(3.9)
  =
  (0.13)
  \cos\left(
  2\pi\frac{12}{7}(3.9)
  \right) $$
- Result:
  $$ y(3.9)\approx-0.051\ \mathrm{m} $$
- The negative sign means the block is to the left of equilibrium.

---

### 36. Velocity at $t=3.9\ \mathrm{s}$
- Velocity:
  $$ v(t)=-2\pi fA\sin(2\pi ft) $$
- Substituting the values gives:
  $$ v(3.9)\approx+1.3\ \mathrm{m}/\mathrm{s} $$

---

### 37. Interpreting the Motion
- At $t=3.9\ \mathrm{s}$:
  $$ y<0 $$
  and:
  $$ v>0 $$
- Therefore, the block is:
  - to the left of equilibrium
  - moving toward the right
  - moving toward equilibrium
  - speeding up

---

## Maximum-Speed Energy Example

### 38. Energy Method
- At maximum displacement:
  $$ E=\frac{1}{2}kA^2 $$
- At equilibrium:
  $$ E=\frac{1}{2}mv_{\max}^2 $$
- Equate:
  $$ \frac{1}{2}mv_{\max}^2=\frac{1}{2}kA^2 $$

---

### 39. Solve for Maximum Speed
- Cancel $\frac{1}{2}$:
  $$ mv_{\max}^2=kA^2 $$
- Solve:
  $$ v_{\max}=A\sqrt{\frac{k}{m}} $$
- The numerical values in the lecture give:
  $$ v_{\max}\approx8.8\ \mathrm{m}/\mathrm{s} $$

---

### 40. Main Physics Takeaways
- Simple harmonic position:
  $$ x(t)=A\cos(\omega t+\phi) $$
- Velocity:
  $$ v(t)=-A\omega\sin(\omega t+\phi) $$
- Acceleration:
  $$ a(t)=-\omega^2x(t) $$
- Maximum speed:
  $$ v_{\max}=A\omega $$
- Spring potential energy:
  $$ U=\frac{1}{2}kx^2 $$
- Total spring-system energy:
  $$ E=\frac{1}{2}mv^2+\frac{1}{2}kx^2 $$
- Mass–spring angular frequency:
  $$ \omega=\sqrt{\frac{k}{m}} $$
- Mass–spring period:
  $$ T=2\pi\sqrt{\frac{m}{k}} $$

---

### 41. Main Problem-Solving Takeaways
1. Identify the equilibrium position.
2. Measure displacement relative to equilibrium.
3. Determine amplitude, period, and frequency from the graph or given data.
4. Use:
   $$ \omega=2\pi f=\frac{2\pi}{T} $$
5. Differentiate position to obtain velocity and acceleration.
6. Use graph slopes to relate $x(t)$, $v(t)$, and $a(t)$.
7. Use energy conservation to connect maximum displacement and maximum speed.
8. Keep units attached throughout the calculation.
