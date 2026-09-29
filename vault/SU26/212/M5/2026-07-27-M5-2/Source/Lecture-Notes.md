## Lecture Outline (Wave Functions, Wave Speed, Refraction, and Intensity)

### 1. Course Logistics
- Quiz 2 grading is nearly complete.
- Quiz 2 scores and the Quiz 2X extra-credit assignment are expected to be posted soon.
- Quiz 2X will close on Thursday rather than Friday because the Physics Wormhole is not open on Fridays during the summer.
- Students seeking TA help should use the sign-up sheet in the TA Information module.
- Students should sign up approximately:
  $$ 24\text{ hours in advance} $$

---

## Review of Wave Concepts

### 2. Definition of a Wave
- A wave is a disturbance that propagates through space.
- A mechanical wave can be viewed as a collection of coupled oscillators.
- The individual particles oscillate about equilibrium while the disturbance moves through the medium.

---

### 3. Transverse Waves
- In a transverse wave, particle motion is perpendicular to the direction of wave propagation:
  $$ \text{particle motion}\perp\text{wave propagation} $$
- Example:
  - a wave traveling along a stretched string

---

### 4. Longitudinal Waves
- In a longitudinal wave, particle motion is parallel or antiparallel to the direction of wave propagation:
  $$ \text{particle motion}\parallel\text{wave propagation} $$
- Example:
  - a sound wave in air

---

### 5. Oscillator vs. Wave Function
- A single oscillator varies only with time:
  $$ x(t)=A\cos(\omega t+\phi_0) $$
- A traveling wave varies with both position and time:
  $$ y(x,t)=A\sin(kx-\omega t+\phi_0) $$
- Sine and cosine describe the same type of motion with an appropriate phase shift.

---

## Mathematical Description of a Sinusoidal Wave

### 6. Wave Amplitude
- The amplitude $A$ is the maximum displacement of a particle from equilibrium:
  $$ A=|y|_{\max} $$

---

### 7. Angular Frequency
- Angular frequency is:
  $$ \omega=2\pi f $$
- Since:
  $$ f=\frac{1}{T} $$
- We may also write:
  $$ \omega=\frac{2\pi}{T} $$

---

### 8. Wave Number
- The wave number is:
  $$ k=\frac{2\pi}{\lambda} $$
- Here:
  - $k$ describes the spatial repetition rate
  - $\lambda$ is the wavelength
- The wave number may be viewed as a type of spatial frequency.

---

### 9. Phase
- The complete phase of the wave is:
  $$ \phi(x,t)=kx-\omega t+\phi_0 $$
- The initial phase is:
  $$ \phi_0 $$
- At:
  $$ x=0,\qquad t=0 $$
  the phase is $\phi_0$.

---

### 10. Wave-Speed Relations
- In one period, the wave travels one wavelength:
  $$ v_{\mathrm{wave}}=\frac{\lambda}{T} $$
- Since:
  $$ f=\frac{1}{T} $$
- Then:
  $$ v_{\mathrm{wave}}=f\lambda $$
- Using $k$ and $\omega$:
  $$ v_{\mathrm{wave}}=\frac{\omega}{k} $$

---

## Direction of Wave Propagation

### 11. Right-Moving Wave
- Consider:
  $$ y(x,t)=A\sin(kx-\omega t+\phi_0) $$
- Follow a point of constant phase:
  $$ kx-\omega t=C $$
- Solve for position:
  $$ x=\frac{\omega}{k}t+\frac{C}{k} $$
- As $t$ increases, $x$ increases.
- Therefore:
  $$ kx-\omega t $$
  represents a wave traveling in the positive $x$-direction.

---

### 12. Left-Moving Wave
- For:
  $$ y(x,t)=A\sin(kx+\omega t+\phi_0) $$
- Constant phase gives:
  $$ x=-\frac{\omega}{k}t+\frac{C}{k} $$
- As $t$ increases, $x$ decreases.
- Therefore:
  $$ kx+\omega t $$
  represents a wave traveling in the negative $x$-direction.

---

### 13. Direction Summary
- Right-moving:
  $$ y(x,t)=A\sin(kx-\omega t+\phi_0) $$
- Left-moving:
  $$ y(x,t)=A\sin(kx+\omega t+\phi_0) $$

---

## Wave Speed vs. Particle Speed

### 14. Particle Motion in an Oscillator
- For:
  $$ x(t)=A\cos(\omega t) $$
- Particle velocity is:
  $$ u(t)=-\omega A\sin(\omega t) $$
- Maximum particle speed:
  $$ u_{\max}=\omega A $$

---

### 15. Particle Acceleration
- Particle acceleration is:
  $$ a_{\mathrm{particle}}(t)=-\omega^2A\cos(\omega t) $$
- Equivalently:
  $$ a_{\mathrm{particle}}(t)=-\omega^2x(t) $$

---

### 16. Important Distinction
- Wave speed:
  $$ v_{\mathrm{wave}}=f\lambda=\frac{\omega}{k} $$
  describes how fast the disturbance propagates.
- Particle speed:
  $$ u_{\max}=\omega A $$
  describes how fast a particle in the medium moves around equilibrium.
- These are different physical quantities and need not have the same value.

---

## Waves on a String

### 17. Linear Mass Density
- Linear mass density is:
  $$ \mu=\frac{m_{\mathrm{string}}}{L} $$
- Units:
  $$ [\mu]=\mathrm{kg}/\mathrm{m} $$

---

### 18. Wave Speed on a String
- The wave speed is:
  $$ v_{\mathrm{wave}}=\sqrt{\frac{F_T}{\mu}} $$
- Here:
  - $F_T$ is the string tension
  - $\mu$ is the linear mass density

---

### 19. Effect of String Tension
- Increasing tension increases the wave speed:
  $$ v_{\mathrm{wave}}\propto\sqrt{F_T} $$
- Greater tension produces a stronger restoring force.

---

### 20. Effect of Linear Density
- Increasing linear density decreases the wave speed:
  $$ v_{\mathrm{wave}}\propto\frac{1}{\sqrt{\mu}} $$
- A more massive string has greater inertia per unit length.

---

## Example 1: Hanging Mass and String Wave Speed

### 21. System Setup
- A block of mass $M$ hangs from a string or wire.
- The wire has:
  - mass $m_w$
  - length $L$
- The block is stationary, so the string tension is:
  $$ F_T=Mg $$

---

### 22. Substitute the Linear Density
- Since:
  $$ \mu=\frac{m_w}{L} $$
- The wave speed becomes:
  $$ v_{\mathrm{wave}}
  =
  \sqrt{
  \frac{Mg}{m_w/L}
  } $$

---

### 23. Final Wave-Speed Formula
- Simplify:
  $$ v_{\mathrm{wave}}
  =
  \sqrt{\frac{MgL}{m_w}} $$
- The lecture’s numerical result is:
  $$ v_{\mathrm{wave}}\approx25\ \mathrm{m}/\mathrm{s} $$

---

### 24. Mass-Notation Warning
- The hanging-block mass and wire mass are different:
  $$ M\ne m_w $$
- The hanging mass determines the tension.
- The wire mass determines the linear density.

---

## Example 2: Maximum Speed of a String Particle

### 25. Given Wave Properties
- The system also specifies:
  - amplitude $A$
  - wavelength $\lambda$
  - wave speed $v_{\mathrm{wave}}$
- Goal:
  - find the maximum speed of a particle oscillating in the wire

---

### 26. Relate Frequency to Wave Speed
- Use:
  $$ v_{\mathrm{wave}}=f\lambda $$
- Therefore:
  $$ f=\frac{v_{\mathrm{wave}}}{\lambda} $$

---

### 27. Maximum Particle Speed
- Start with:
  $$ u_{\max}=\omega A $$
- Since:
  $$ \omega=2\pi f $$
- Then:
  $$ u_{\max}=2\pi fA $$

---

### 28. Substitute the Wave Frequency
- Using:
  $$ f=\frac{v_{\mathrm{wave}}}{\lambda} $$
- We obtain:
  $$ u_{\max}
  =
  \frac{2\pi A}{\lambda}v_{\mathrm{wave}} $$

---

### 29. Complete Formula for the Hanging-Mass System
- Substitute:
  $$ v_{\mathrm{wave}}=\sqrt{\frac{MgL}{m_w}} $$
- Then:
  $$
  u_{\max}
  =
  \frac{2\pi A}{\lambda}
  \sqrt{\frac{MgL}{m_w}}
  $$
- The lecture’s numerical result is approximately:
  $$ u_{\max}\approx200\ \mathrm{m}/\mathrm{s} $$

---

## Spherical Sound Wavefronts

### 30. Wavefront Geometry
- A point sound source produces approximately spherical wavefronts.
- In a two-dimensional diagram, a spherical wavefront appears as a circle.
- Points detecting the same wavefront simultaneously are the same distance from the source.

---

### 31. Locate the Sound Source
- Two listeners lie on the $x$-axis at:
  $$ x_1=-7\ \mathrm{m} $$
  $$ x_2=3\ \mathrm{m} $$
- The source is also on the $x$-axis.
- Its position is the midpoint:
  $$ x_s=\frac{x_1+x_2}{2} $$
- Therefore:
  $$ x_s=\frac{-7+3}{2}=-2\ \mathrm{m} $$

---

### 32. Radius of the Wavefront
- The wavefront radius is:
  $$ r=|-7-(-2)| $$
- Therefore:
  $$ r=5\ \mathrm{m} $$

---

### 33. Position of a Third Listener
- For a third listener shown at $x=0$, its horizontal distance from the source is:
  $$ \Delta x=0-(-2)=2\ \mathrm{m} $$
- Apply the circle equation:
  $$ (\Delta x)^2+y^2=r^2 $$

---

### 34. Solve for the Vertical Coordinate
- Rearranging:
  $$ y=\sqrt{r^2-(\Delta x)^2} $$
- Substitute:
  $$ y=\sqrt{(5\ \mathrm{m})^2-(2\ \mathrm{m})^2} $$
- Therefore:
  $$ y=\sqrt{21}\ \mathrm{m} $$
- Numerical result:
  $$ y\approx4.58\ \mathrm{m} $$

---

## Index of Refraction

### 35. Definition
- The index of refraction is:
  $$ n=\frac{c}{v} $$
- Here:
  - $c$ is the speed of light in vacuum
  - $v$ is the effective speed of light in the material

---

### 36. Physical Meaning
- Light interacts with atoms and molecules while traveling through a material.
- These interactions reduce its effective propagation speed.
- Since:
  $$ v<c $$
  for an ordinary transparent material:
  $$ n>1 $$

---

### 37. Frequency Across a Boundary
- When light passes from one medium into another, its frequency remains unchanged:
  $$ f_1=f_2 $$
- The source determines the frequency.

---

### 38. Wavelength Across a Boundary
- Since:
  $$ v=f\lambda $$
- A change in speed with constant frequency requires a change in wavelength:
  $$ \lambda=\frac{v}{f} $$
- Slower light speed means shorter wavelength.

---

### 39. Index–Wavelength Relationship
- Substitute:
  $$ v=f\lambda $$
  into:
  $$ n=\frac{c}{v} $$
- Then:
  $$ n=\frac{c}{f\lambda} $$
- For the same light:
  $$ n\lambda=\frac{c}{f}=\text{constant} $$

---

### 40. Comparing Different Media
- For the same light passing through several materials:
  $$ n_1\lambda_1=n_2\lambda_2=n_3\lambda_3 $$
- Therefore:
  - shorter wavelength $\Rightarrow$ larger index of refraction
  - longer wavelength $\Rightarrow$ smaller index of refraction

---

### 41. Wavelength-Ranking Example
- From the wave snapshot in the lecture:
  - medium $B$ has the shortest wavelength
  - medium $C$ has the longest wavelength
- Therefore:
  $$ n_B>n_A>n_C $$

---

## Example: Number of Wavelengths Inside Glass

### 42. Given Information
- Light in air has wavelength:
  $$ \lambda_{\mathrm{air}}=650\ \mathrm{nm} $$
- Indices of refraction:
  $$ n_{\mathrm{air}}=1.0 $$
  $$ n_{\mathrm{glass}}=1.5 $$
- The glass slide has width $w$.
- Goal:
  - find the number of wavelengths contained within the slide

---

### 43. Wavelength in Glass
- Use:
  $$ n_{\mathrm{air}}\lambda_{\mathrm{air}}=n_{\mathrm{glass}}\lambda_{\mathrm{glass}} $$
- Therefore:
  $$ \lambda_{\mathrm{glass}}=\frac{n_{\mathrm{air}}}{n_{\mathrm{glass}}}\lambda_{\mathrm{air}} $$

---

### 44. Number of Wavelengths
- The number of wavelengths in a width $w$ is:
  $$ N=\frac{w}{\lambda_{\mathrm{glass}}} $$
- Substitute the expression for $\lambda_{\mathrm{glass}}$:
  $$
  N
  =
  \frac{w}{(n_{\mathrm{air}}/n_{\mathrm{glass}})\lambda_{\mathrm{air}}}
  $$
- Therefore:
  $$ N=\frac{wn_{\mathrm{glass}}}{n_{\mathrm{air}}\lambda_{\mathrm{air}}} $$

---

### 45. Numerical Result
- Using the slide width supplied in the problem:
  $$ N\approx3.23\times10^3 $$
- So approximately:
  $$ N\approx3230\text{ wavelengths} $$

---

## Wave Energy and Power

### 46. Kinetic Energy of an Oscillating Particle
- The kinetic energy of a particle is:
  $$ K=\frac{1}{2}mu^2 $$
- For simple harmonic motion:
  $$ u_{\max}=\omega A $$

---

### 47. Dependence on Frequency and Amplitude
- Since:
  $$ u_{\max}\propto\omega A $$
- The kinetic energy scale is:
  $$ K\propto\omega^2A^2 $$
- Since:
  $$ \omega=2\pi f $$
- We may also write:
  $$ K\propto f^2A^2 $$

---

### 48. Wave Power
- Power is energy transferred per unit time:
  $$ P=\frac{\Delta E}{\Delta t} $$
- For fixed properties of the medium, wave power scales as:
  $$ P\propto f^2A^2 $$
- Increasing either frequency or amplitude increases the transmitted power.

---

### 49. Amplitude Dependence
- Since:
  $$ P\propto A^2 $$
- Doubling the amplitude increases the power by:
  $$ 2^2=4 $$
- Tripling the amplitude increases the power by:
  $$ 3^2=9 $$

---

### 50. Frequency Dependence
- Since:
  $$ P\propto f^2 $$
- Doubling the frequency, with other relevant quantities fixed, increases the power scale by:
  $$ 2^2=4 $$

---

## Wave Intensity

### 51. Definition of Intensity
- Intensity is power per area:
  $$ I=\frac{P}{A_s} $$
- SI units:
  $$ [I]=\mathrm{W}/\mathrm{m}^2 $$

---

### 52. Point Source in Three Dimensions
- For an isotropic point source, power spreads uniformly over a sphere.
- Surface area of a sphere:
  $$ A_s=4\pi r^2 $$
- Therefore:
  $$ I=\frac{P}{4\pi r^2} $$

---

### 53. Inverse-Square Law
- From:
  $$ I=\frac{P}{4\pi r^2} $$
- Intensity varies as:
  $$ I\propto\frac{1}{r^2} $$
- Doubling the distance reduces intensity to:
  $$ \frac{1}{2^2}=\frac{1}{4} $$
  of its original value.

---

### 54. Assumptions for the Point-Source Formula
- The relation:
  $$ I=\frac{P}{4\pi r^2} $$
  assumes:
  - an isotropic point source
  - spherical spreading
  - negligible absorption
  - no significant reflections or obstacles

---

## Sound Intensity Level

### 55. Decibel Scale
- Because audible intensities span an enormous range, sound is commonly described using a logarithmic scale.
- Sound intensity level is:
  $$
  \beta
  =
  10\log_{10}\left(\frac{I}{I_0}\right)
  $$

---

### 56. Reference Intensity
- The reference intensity is approximately the threshold of human hearing:
  $$ I_0=10^{-12}\ \mathrm{W}/\mathrm{m}^2 $$

---

### 57. Units of Intensity Level
- Sound intensity level is measured in decibels:
  $$ [\beta]=\mathrm{dB} $$

---

### 58. Why a Logarithmic Scale Is Used
- Human hearing covers a very large range of intensities.
- A logarithmic scale compresses that range into manageable numerical values.
- Similar logarithmic scales are used for phenomena with large dynamic ranges, such as earthquakes.

---

### 59. Main Physics Takeaways
- Sinusoidal traveling wave:
  $$ y(x,t)=A\sin(kx-\omega t+\phi_0) $$
- Wave number:
  $$ k=\frac{2\pi}{\lambda} $$
- Angular frequency:
  $$ \omega=2\pi f $$
- Wave speed:
  $$ v_{\mathrm{wave}}=f\lambda=\frac{\omega}{k} $$
- String-wave speed:
  $$ v_{\mathrm{wave}}=\sqrt{\frac{F_T}{\mu}} $$
- Maximum particle speed:
  $$ u_{\max}=\omega A $$
- Index of refraction:
  $$ n=\frac{c}{v} $$
- For the same light:
  $$ n\lambda=\text{constant} $$
- Intensity:
  $$ I=\frac{P}{A_s} $$
- Isotropic point-source intensity:
  $$ I=\frac{P}{4\pi r^2} $$
- Sound intensity level:
  $$ \beta=10\log_{10}\left(\frac{I}{I_0}\right) $$

---

### 60. Main Problem-Solving Takeaways
1. Distinguish wave propagation speed from particle oscillation speed.
2. Use the sign in $kx\mp\omega t$ to determine wave direction.
3. For waves on strings, identify both tension and linear mass density.
4. Use geometric wavefronts to locate sources or listeners.
5. Remember that frequency remains constant when light enters a different medium.
6. Use:
   $$ n_1\lambda_1=n_2\lambda_2 $$
   when comparing wavelengths in different media.
7. Use the inverse-square law for an isotropic point source.
8. Distinguish intensity $I$ from intensity level $\beta$.
