## Lecture Outline (Newtonian Gravitation, Orbits, Kepler’s Laws, and Geostationary Satellites)

### 1. Course Logistics
- Quiz 1 extra-credit assignment:
  $$ \text{Quiz 1X} $$
  is optional and closes Friday at:
  $$ 6{:}00\text{ PM} $$
- Quiz 2:
  - Proctorio version opens Saturday
  - Proctorio version closes Monday
  - Zoom-proctored versions are held Monday
- Students should begin preparing their Quiz 2 note sheet.

---

## Newtonian Gravitation

### 2. Gravity as a Central Force
- Gravity is a **central force**:
  - it acts along the line connecting two masses
  - it depends only on the distance between the masses
  - it is always attractive in Newtonian mechanics
- The lecture uses Newtonian gravity rather than general relativity.

---

### 3. Newton’s Law of Universal Gravitation
- The gravitational force between two point masses is:
  $$
  \vec{F}_g
  =
  -\frac{Gm_1m_2}{r^2}\hat{r}
  $$
- Here:
  - $G$ is the universal gravitational constant
  - $m_1$ and $m_2$ are the two masses
  - $r$ is the distance between their centers
  - $\hat{r}$ points radially outward
- The negative sign indicates that gravity points inward and is attractive.

---

### 4. Universal Gravitational Constant
- The gravitational constant is:
  $$
  G=6.67\times10^{-11}
  \mathrm{N}\,\mathrm{m}^2/\mathrm{kg}^2
  $$
- Unlike the local gravitational acceleration $g$, the value of $G$ is the same everywhere.

---

### 5. Weight Near the Surface of Earth
- Near Earth’s surface, gravitational force is often written as:
  $$
  F_g=mg
  $$
- The general gravitational-force magnitude is:
  $$
  F_g=\frac{GM_Em}{r^2}
  $$
- Equating these:
  $$
  mg=\frac{GM_Em}{r^2}
  $$
- Cancel the object’s mass $m$:
  $$
  g(r)=\frac{GM_E}{r^2}
  $$
- Therefore, gravitational acceleration does not depend on the falling object’s mass.

---

### 6. Earth Data
- Approximate mass of Earth:
  $$
  M_E=5.97\times10^{24}\ \mathrm{kg}
  $$
- Approximate mean radius of Earth:
  $$
  R_E=6.37\times10^6\ \mathrm{m}
  $$
- Equivalently:
  $$
  R_E\approx6370\ \mathrm{km}
  $$

---

### 7. Gravitational Acceleration at Earth’s Surface
- At Earth’s surface:
  $$
  g=\frac{GM_E}{R_E^2}
  $$
- Substituting the Earth data gives:
  $$
  g\approx9.81\ \mathrm{m}/\mathrm{s}^2
  $$

---

### 8. Dependence of Gravity on Altitude
- At altitude $h$ above Earth’s surface, the distance from Earth’s center is:
  $$
  r=R_E+h
  $$
- The gravitational acceleration there is:
  $$
  g_h=\frac{GM_E}{(R_E+h)^2}
  $$
- Gravity decreases with the inverse square of the distance from Earth’s center.

---

## Example: Satellite at an Altitude of $R_E/3$

### 9. Problem Setup
- A satellite is at altitude:
  $$
  h=\frac{R_E}{3}
  $$
- Find its gravitational acceleration as a fraction of the surface value:
  $$
  \frac{g_h}{g_0}
  $$

---

### 10. Form the Acceleration Ratio
- Use:
  $$
  g_h=\frac{GM_E}{(R_E+h)^2}
  $$
  and:
  $$
  g_0=\frac{GM_E}{R_E^2}
  $$
- Divide:
  $$
  \frac{g_h}{g_0}
  =
  \frac{GM_E/(R_E+h)^2}{GM_E/R_E^2}
  $$
- Cancel $GM_E$:
  $$
  \frac{g_h}{g_0}
  =
  \frac{R_E^2}{(R_E+h)^2}
  $$

---

### 11. Substitute the Altitude
- Since:
  $$
  h=\frac{R_E}{3}
  $$
- The orbital radius is:
  $$
  R_E+h
  =
  R_E+\frac{R_E}{3}
  =
  \frac{4R_E}{3}
  $$
- Therefore:
  $$
  \frac{g_h}{g_0}
  =
  \frac{R_E^2}{(4R_E/3)^2}
  =
  \left(\frac{3}{4}\right)^2
  $$
- Result:
  $$
  \frac{g_h}{g_0}
  =
  \frac{9}{16}
  \approx0.56
  $$
- The satellite experiences about:
  $$ 56\% $$
  of the surface gravitational acceleration.

---

## Gravitational Force Compared with Electric Force

### 12. Two Electrons
- For two electrons separated by distance $r$, the electric-force magnitude is:
  $$
  F_e=\frac{k_e e^2}{r^2}
  $$
- Their gravitational-force magnitude is:
  $$
  F_g=\frac{Gm_e^2}{r^2}
  $$
- The ratio is:
  $$
  \frac{F_e}{F_g}
  =
  \frac{k_e e^2}{Gm_e^2}
  $$

---

### 13. Relative Strength
- The lecture gives approximately:
  $$
  \frac{F_e}{F_g}\approx4\times10^{42}
  $$
- The electric force between two electrons is enormously stronger than their gravitational attraction.
- Gravity dominates astronomical systems because:
  - positive and negative electric charges tend to cancel
  - ordinary matter is approximately electrically neutral
  - gravitational mass has only one ordinary sign, so gravitational attraction accumulates

---

## Gravitational Potential Energy

### 14. Force and Potential Energy
- In general, a conservative force is related to potential energy by:
  $$
  \vec{F}=-\nabla U
  $$
- For radial motion:
  $$
  F_r=-\frac{dU}{dr}
  $$

---

### 15. Gravitational Potential-Energy Derivation
- Gravitational force is:
  $$
  \vec{F}_g
  =
  -\frac{GMm}{r^2}\hat{r}
  $$
- Choosing:
  $$
  U(\infty)=0
  $$
- The potential energy is:
  $$
  U(r)
  =
  -\int_{\infty}^{r}\vec{F}_g\cdot d\vec{r}
  $$
- Evaluating the integral gives:
  $$
  U(r)=-\frac{GMm}{r}
  $$

---

### 16. Meaning of Negative Potential Energy
- The gravitational potential energy is negative because the two masses form a bound attractive system.
- Energy must be added to separate the masses to infinite distance, where:
  $$
  U(\infty)=0
  $$

---

## Circular Orbits

### 17. Force Balance for a Circular Orbit
- For a satellite of mass $m$ orbiting a much larger mass $M$, take inward as positive. Gravity provides the radial net force:
  $$
  \sum F_r=m a_r=m\frac{v^2}{r}=F_g=\frac{GMm}{r^2}
  $$
- Cancel $m$ and one factor of $r$:
  $$
  v^2=\frac{GM}{r}
  $$

---

### 18. Circular-Orbit Speed
- The orbital speed is:
  $$
  v=\sqrt{\frac{GM}{r}}
  $$
- A larger orbital radius corresponds to a smaller circular-orbit speed.

---

### 19. Orbital Kinetic Energy
- Kinetic energy is:
  $$
  K=\frac{1}{2}mv^2
  $$
- Substitute:
  $$
  v^2=\frac{GM}{r}
  $$
- Then:
  $$
  K=\frac{GMm}{2r}
  $$

---

### 20. Total Mechanical Energy of a Circular Orbit
- Gravitational potential energy:
  $$
  U=-\frac{GMm}{r}
  $$
- Kinetic energy:
  $$
  K=\frac{GMm}{2r}
  $$
- Total energy:
  $$
  E=K+U
  $$
- Therefore:
  $$
  E=-\frac{GMm}{2r}
  $$
- The negative total energy indicates a gravitationally bound orbit.

---

## Newton’s Cannon Thought Experiment

### 21. Basic Idea
- Imagine firing a cannonball horizontally from a very high mountain.
- With a small launch speed, it travels forward and falls to Earth.
- With a greater launch speed, it travels farther before reaching Earth.
- At the correct speed, Earth’s surface curves away at the same rate that the cannonball falls.

---

### 22. Orbit as Continuous Free Fall
- An orbiting object is continuously falling toward Earth.
- It keeps missing Earth because of its horizontal velocity.
- An orbiting object is not force-free.
- It still has inward acceleration:
  $$
  a_r=\frac{v^2}{r}
  $$
- In a circular orbit, the object can have constant **speed**, but its velocity changes direction continuously.

---

## Kepler’s Laws

### 23. Kepler’s First Law
- Planetary orbits are ellipses.
- The Sun is located at one focus of each planetary ellipse.
- A circular orbit is a special case of an ellipse.

---

### 24. Kepler’s Second Law
- A line from the Sun to a planet sweeps out equal areas in equal time intervals.
- Therefore:
  - a planet moves faster when it is closer to the Sun
  - a planet moves slower when it is farther from the Sun

---

### 25. Energy Interpretation of the Second Law
- As a planet moves closer to the Sun:
  - gravitational potential energy decreases
  - kinetic energy increases
  - speed increases
- As it moves farther away:
  - gravitational potential energy increases
  - kinetic energy decreases
  - speed decreases

---

### 26. Kepler’s Third Law
- The square of the orbital period is proportional to the cube of the semi-major axis:
  $$
  T^2\propto a^3
  $$
- For a circular orbit, the semi-major axis $a$ is simply the orbital radius $r$:
  $$
  T^2\propto r^3
  $$

---

## Derivation of Kepler’s Third Law for a Circular Orbit

### 27. Begin with Radial Force Balance
- Take inward as positive. Gravity supplies the radial net force:
  $$
  \sum F_r=m a_r=m\frac{v^2}{r}=F_g=\frac{GMm}{r^2}
  $$
- Cancel $m$:
  $$
  v^2=\frac{GM}{r}
  $$

---

### 28. Express Speed in Terms of Orbital Period
- For one circular orbit, the distance traveled is:
  $$
  2\pi r
  $$
- Therefore:
  $$
  v=\frac{2\pi r}{T}
  $$
- Square:
  $$
  v^2=\frac{4\pi^2r^2}{T^2}
  $$

---

### 29. Substitute into the Force Result
- Set:
  $$
  \frac{4\pi^2r^2}{T^2}
  =
  \frac{GM}{r}
  $$
- Multiply by $rT^2$:
  $$
  4\pi^2r^3=GMT^2
  $$
- Therefore:
  $$
  r^3=\frac{GMT^2}{4\pi^2}
  $$
- Equivalently:
  $$
  T^2=\frac{4\pi^2}{GM}r^3
  $$

---

### 30. More General Two-Body Form
- If neither orbiting mass is negligible, the more general relation is:
  $$
  T^2
  =
  \frac{4\pi^2a^3}{G(M+m)}
  $$
- If $M\gg m$, this reduces to:
  $$
  T^2\approx\frac{4\pi^2a^3}{GM}
  $$

---

## Example: Planet with an Eight-Year Period

### 31. Problem Setup
- A planet orbits the same star as Earth.
- Its orbital period is:
  $$
  T_p=8T_E
  $$
- Find its orbital radius relative to Earth’s:
  $$
  \frac{r_p}{r_E}
  $$

---

### 32. Use Kepler’s Third Law as a Ratio
- For both planets orbiting the same star:
  $$
  \frac{r_p^3}{r_E^3}
  =
  \frac{T_p^2}{T_E^2}
  $$
- Substitute:
  $$
  T_p=8T_E
  $$
- Then:
  $$
  \frac{r_p^3}{r_E^3}
  =
  \frac{(8T_E)^2}{T_E^2}
  =
  64
  $$

---

### 33. Solve for the Radius Ratio
- Take the cube root:
  $$
  \frac{r_p}{r_E}
  =
  \sqrt[3]{64}
  =
  4
  $$
- Therefore:
  $$
  r_p=4r_E
  $$
- If Earth’s orbital radius is $1\ \mathrm{AU}$:
  $$
  r_p=4.0\ \mathrm{AU}
  $$

---

## Geostationary Satellites

### 34. Definition
- A geostationary satellite remains above the same point on Earth’s surface.
- To do this, it must:
  - have a circular orbit
  - orbit in Earth’s equatorial plane
  - travel in the same direction as Earth’s rotation
  - have an orbital period equal to Earth’s rotational period

---

### 35. Geostationary Period
- The lecture uses:
  $$
  T=24\ \mathrm{h}
  $$
- Convert to seconds:
  $$
  T=(24)(60)(60)
  $$
  $$
  T=86{,}400\ \mathrm{s}
  $$

---

### 36. Orbital Radius of the Satellite
- Let the altitude above Earth’s surface be $h$.
- The distance from Earth’s center is:
  $$
  r=R_E+h
  $$
- Take inward as positive. Gravitational force supplies the radial net force:
  $$
  \sum F_r=m a_r=m\frac{v^2}{R_E+h}=F_g=\frac{GM_Em}{(R_E+h)^2}
  $$

---

### 37. Simplify the Force Equation
- Cancel $m$ and one power of $R_E+h$:
  $$
  v^2=\frac{GM_E}{R_E+h}
  $$

---

### 38. Express Speed Using the Period
- For a circular orbit:
  $$
  v=\frac{2\pi(R_E+h)}{T}
  $$
- Therefore:
  $$
  v^2=\frac{4\pi^2(R_E+h)^2}{T^2}
  $$

---

### 39. Solve for the Orbital Radius
- Set the two expressions for $v^2$ equal:
  $$
  \frac{4\pi^2(R_E+h)^2}{T^2}
  =
  \frac{GM_E}{R_E+h}
  $$
- Rearranging:
  $$
  (R_E+h)^3
  =
  \frac{GM_ET^2}{4\pi^2}
  $$
- Take the cube root:
  $$
  R_E+h
  =
  \left(
  \frac{GM_ET^2}{4\pi^2}
  \right)^{1/3}
  $$

---

### 40. Solve for the Altitude
- Therefore:
  $$
  h
  =
  \left(
  \frac{GM_ET^2}{4\pi^2}
  \right)^{1/3}
  -R_E
  $$

---

### 41. Numerical Result
- Using the Earth data and:
  $$
  T=86{,}400\ \mathrm{s}
  $$
- The geostationary altitude is approximately:
  $$
  h\approx3.58\times10^7\ \mathrm{m}
  $$
- Equivalently:
  $$
  h\approx35{,}800\ \mathrm{km}
  $$

---

### 42. Orbital Radius vs. Altitude
- The orbital radius from Earth’s center is approximately:
  $$
  r_{\mathrm{geo}}\approx4.22\times10^7\ \mathrm{m}
  $$
- Equivalently:
  $$
  r_{\mathrm{geo}}\approx42{,}200\ \mathrm{km}
  $$
- The altitude is found by subtracting Earth’s radius:
  $$
  h=r_{\mathrm{geo}}-R_E
  $$

---

### 43. Comparison with Low Earth Orbit
- The International Space Station orbits at an altitude of roughly:
  $$
  400\ \mathrm{km}
  $$
- A geostationary satellite is much farther away:
  $$
  h\approx35{,}800\ \mathrm{km}
  $$

---

### 44. Main Physics Takeaways
- Universal gravitational force:
  $$
  \vec{F}_g
  =
  -\frac{Gm_1m_2}{r^2}\hat{r}
  $$
- Gravitational acceleration:
  $$
  g(r)=\frac{GM}{r^2}
  $$
- Gravitational potential energy:
  $$
  U(r)=-\frac{GMm}{r}
  $$
- Circular-orbit speed:
  $$
  v=\sqrt{\frac{GM}{r}}
  $$
- Kepler’s third law:
  $$
  T^2=\frac{4\pi^2}{GM}r^3
  $$
- Geostationary altitude:
  $$
  h
  =
  \left(
  \frac{GM_ET^2}{4\pi^2}
  \right)^{1/3}
  -R_E
  $$

---

### 45. Main Problem-Solving Strategy
1. Draw the orbit and identify the distance from the central body’s center.
2. Distinguish altitude $h$ from orbital radius:
   $$ r=R_E+h $$
3. Draw a free-body diagram.
4. Take inward as positive and set the radial net force equal to the radial-acceleration requirement:
   $$ \sum F_r=m a_r=m\frac{v^2}{r}=F_g=\frac{GMm}{r^2} $$
5. Use:
   $$ v=\frac{2\pi r}{T} $$
   when the orbital period is known.
6. Solve symbolically before inserting numerical values.
7. Use ratios to cancel common constants when comparing two orbits.
