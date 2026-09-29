## Lecture Outline (Wave Intensity, Decibel Levels, and the Doppler Effect)

### 1. Course Logistics
- Quiz 2 scores and the Quiz 2X extra-credit assignment will be posted after grading is completed.
- Quiz 2X will be due:
  $$ \text{Tuesday at }6{:}00\text{ PM} $$
- Quiz 3:
  - Proctorio version opens Saturday
  - Proctorio version closes Monday
  - Zoom-proctored sessions occur Monday during class and at $6{:}00\text{ PM}$
- Students should prepare their handwritten Quiz 3 note sheet and submit it to Gradescope with a photo ID before beginning the quiz.

---

## Wave Power and Intensity

### 2. Energy of an Oscillating Particle
- The kinetic energy of a particle is:
  $$ K=\frac{1}{2}mu^2 $$
- For sinusoidal motion, the maximum particle speed is:
  $$ u_{\max}=\omega A=2\pi fA $$
- Therefore, the energy scale is proportional to:
  $$ K\propto f^2A^2 $$

---

### 3. Wave Power
- Power is energy transferred per unit time:
  $$ P=\frac{\Delta E}{\Delta t} $$
- For fixed properties of the medium:
  $$ P\propto f^2A^2 $$
- Increasing either the frequency or amplitude increases the power carried by the wave.

---

### 4. Intensity
- Intensity is power divided by the area through which the power travels:
  $$ I=\frac{P}{A_s} $$
- SI units:
  $$ [I]=\mathrm{W}/\mathrm{m}^2 $$

---

### 5. Intensity from an Isotropic Point Source
- A point source produces approximately spherical wavefronts.
- The surface area of a sphere is:
  $$ A_s=4\pi r^2 $$
- Therefore:
  $$ I=\frac{P}{4\pi r^2} $$

---

### 6. Inverse-Square Dependence
- For a source with constant power:
  $$ I\propto\frac{1}{r^2} $$
- If the distance is multiplied by a factor $n$:
  $$ r_2=nr_1 $$
- Then:
  $$ I_2=\frac{I_1}{n^2} $$

---

## Example 1: Doubling the Distance from a Speaker

### 7. Given Relationship
- The listener moves twice as far from the same speaker:
  $$ r_2=2r_1 $$
- Since the source power does not change:
  $$ P_2=P_1 $$

---

### 8. Use an Intensity Ratio
- Write:
  $$ I_1=\frac{P}{4\pi r_1^2} $$
  $$ I_2=\frac{P}{4\pi r_2^2} $$
- Divide:
  $$ \frac{I_2}{I_1}
  =
  \frac{r_1^2}{r_2^2} $$
- Substitute $r_2=2r_1$:
  $$ \frac{I_2}{I_1}
  =
  \frac{r_1^2}{(2r_1)^2}
  =
  \frac{1}{4} $$

---

### 9. Result
- Therefore:
  $$ I_2=\frac{I_1}{4} $$
- Using the value applied in the lecture solution:
  $$ I_1=240\ \mathrm{W}/\mathrm{m}^2 $$
- Then:
  $$ I_2=60\ \mathrm{W}/\mathrm{m}^2 $$
- Doubling the distance reduces the intensity to one-fourth of its original value.

---

## Sound Intensity Level

### 10. Decibel Definition
- Sound intensity level is:
  $$ \beta
  =
  10\log_{10}\left(\frac{I}{I_0}\right)\ \mathrm{dB} $$
- Here:
  - $\beta$ is the intensity level in decibels
  - $I$ is the sound intensity
  - $I_0$ is the reference intensity

---

### 11. Reference Intensity
- The standard reference intensity is approximately the threshold of human hearing:
  $$ I_0=10^{-12}\ \mathrm{W}/\mathrm{m}^2 $$

---

### 12. Why Decibels Use a Logarithmic Scale
- Human hearing covers an extremely large range of intensities.
- The logarithmic decibel scale compresses that range into more manageable values.
- Other phenomena with large dynamic ranges, such as earthquake magnitudes, also use logarithmic scales.

---

## Example 2: Intensity of Normal Conversation

### 13. Given Intensity Level
- Normal conversation has an intensity level of approximately:
  $$ \beta=60\ \mathrm{dB} $$
- Find the corresponding intensity $I$.

---

### 14. Solve the Decibel Equation for Intensity
- Begin with:
  $$ \beta
  =
  10\log_{10}\left(\frac{I}{I_0}\right)\ \mathrm{dB} $$
- Divide by $10\ \mathrm{dB}$:
  $$ \frac{\beta}{10\ \mathrm{dB}}
  =
  \log_{10}\left(\frac{I}{I_0}\right) $$
- Raise $10$ to both sides:
  $$ 10^{\beta/(10\ \mathrm{dB})}
  =
  \frac{I}{I_0} $$
- Therefore:
  $$ I=I_0\,10^{\beta/(10\ \mathrm{dB})} $$

---

### 15. Numerical Result
- Substitute:
  $$ I_0=10^{-12}\ \mathrm{W}/\mathrm{m}^2 $$
  $$ \beta=60\ \mathrm{dB} $$
- Then:
  $$
  I
  =
  10^{-12}
  10^{60/10}
  \mathrm{W}/\mathrm{m}^2
  $$
- Therefore:
  $$ I=10^{-6}\ \mathrm{W}/\mathrm{m}^2 $$
- In milliwatts per square meter:
  $$ I=0.0010\ \mathrm{mW}/\mathrm{m}^2 $$

---

## Example 3: Two People Talking

### 16. Intensity Addition
- Suppose one person produces a sound level:
  $$ \beta_1=60\ \mathrm{dB} $$
- If two similar people speak simultaneously, their powers add:
  $$ P_2=2P_1 $$
- At the same distance, their intensities also add:
  $$ I_2=2I_1 $$

---

### 17. Compare the Two Intensity Levels
- Write:
  $$ \beta_2-\beta_1
  =
  10\log_{10}\left(\frac{I_2}{I_0}\right)
  -
  10\log_{10}\left(\frac{I_1}{I_0}\right) $$
- Use:
  $$ \log B-\log A=\log\left(\frac{B}{A}\right) $$
- Then:
  $$ \beta_2-\beta_1
  =
  10\log_{10}\left(\frac{I_2}{I_1}\right)\ \mathrm{dB} $$

---

### 18. Substitute the Intensity Ratio
- Since:
  $$ I_2=2I_1 $$
- We get:
  $$ \beta_2-\beta_1
  =
  10\log_{10}(2)\ \mathrm{dB} $$
- Since:
  $$ \log_{10}(2)\approx0.301 $$
- The increase is:
  $$ \Delta\beta\approx3.0\ \mathrm{dB} $$

---

### 19. Final Sound Level
- Therefore:
  $$ \beta_2=\beta_1+3.0\ \mathrm{dB} $$
- With $\beta_1=60\ \mathrm{dB}$:
  $$ \beta_2\approx63\ \mathrm{dB} $$

---

### 20. Important Decibel Lesson
- Two equal sound sources do not produce twice the decibel level.
- The intensities add:
  $$ I_{\mathrm{total}}=I_1+I_2 $$
- Doubling intensity increases the sound level by only:
  $$ 3\ \mathrm{dB} $$

---

## Doppler Effect

### 21. Definition
- The Doppler effect is a change in the observed frequency caused by relative motion between:
  - the source
  - the observer
- The effect applies to sound and other waves, although this lecture focuses on sound.

---

### 22. Source Moving Toward the Observer
- When a source moves toward an observer, it moves into the wavefronts it emits.
- The wavefronts are compressed.
- The observed wavelength decreases.
- Therefore, the observed frequency increases.

---

### 23. Source Moving Away from the Observer
- When a source moves away, the emitted wavefronts are spread farther apart.
- The observed wavelength increases.
- Therefore, the observed frequency decreases.

---

### 24. Observer Moving Toward the Source
- A moving observer encounters incoming wavefronts more frequently.
- Therefore, the observer detects a higher frequency.

---

### 25. Observer Moving Away from the Source
- A moving observer encounters incoming wavefronts less frequently.
- Therefore, the observer detects a lower frequency.

---

### 26. Doppler-Effect Notation
- Let:
  - $f_0$ be the frequency emitted in the source’s rest frame
  - $f_{\mathrm{obs}}$ be the frequency measured by the observer
  - $v_o$ be the observer’s speed
  - $v_s$ be the source’s speed
  - $v$ be the wave speed in the medium
- For sound in air near ordinary conditions:
  $$ v\approx343\ \mathrm{m}/\mathrm{s} $$

---

## Moving Observer Equations

### 27. Observer Moving Toward a Stationary Source
- The observed frequency is:
  $$ f_{\mathrm{obs}}
  =
  f_0\left(1+\frac{v_o}{v}\right) $$
- This produces a higher frequency:
  $$ f_{\mathrm{obs}}>f_0 $$

---

### 28. Observer Moving Away from a Stationary Source
- The observed frequency is:
  $$ f_{\mathrm{obs}}
  =
  f_0\left(1-\frac{v_o}{v}\right) $$
- This produces a lower frequency:
  $$ f_{\mathrm{obs}}<f_0 $$

---

## Moving Source Equations

### 29. Source Moving Toward a Stationary Observer
- The observed frequency is:
  $$ f_{\mathrm{obs}}
  =
  \frac{f_0}{1-\frac{v_s}{v}} $$
- The denominator becomes smaller, so:
  $$ f_{\mathrm{obs}}>f_0 $$

---

### 30. Source Moving Away from a Stationary Observer
- The observed frequency is:
  $$ f_{\mathrm{obs}}
  =
  \frac{f_0}{1+\frac{v_s}{v}} $$
- The denominator becomes larger, so:
  $$ f_{\mathrm{obs}}<f_0 $$

---

### 31. Source Motion vs. Observer Motion
- Source motion and observer motion use different formulas.
- A moving observer changes the rate at which wavefronts are encountered.
- A moving source changes the spacing between the emitted wavefronts.
- Therefore, the two effects are physically different and are not simple inverses of one another.

---

## Example 4: Bat Flying Toward a Singer

### 32. Problem Setup
- A singer emits:
  $$ f_0=880\ \mathrm{Hz} $$
- A bat flies toward the singer at:
  $$ v_o=35\ \mathrm{m}/\mathrm{s} $$
- The bat is the moving observer.
- Find the frequency heard by the bat.

---

### 33. Select the Correct Equation
- Since the observer moves toward the stationary source:
  $$ f_{\mathrm{obs}}
  =
  f_0\left(1+\frac{v_o}{v}\right) $$

---

### 34. Numerical Calculation
- Substitute:
  $$ f_{\mathrm{obs}}
  =
  880
  \left(
  1+\frac{35}{343}
  \right)\ \mathrm{Hz} $$
- Result:
  $$ f_{\mathrm{obs}}\approx970\ \mathrm{Hz} $$
- The bat hears a higher frequency because it moves toward the singer.

---

## Example 5: Can a Bat’s Chirp Become Audible?

### 35. Problem Setup
- A bat emits an echolocation chirp at:
  $$ f_0=25\ \mathrm{kHz} $$
- The approximate upper limit of human hearing is:
  $$ f_{\mathrm{obs}}=20\ \mathrm{kHz} $$
- Find how fast the bat would need to fly for the chirp to be shifted into the audible range.

---

### 36. Determine the Direction of Motion
- The emitted frequency must decrease from:
  $$ 25\ \mathrm{kHz} $$
  to:
  $$ 20\ \mathrm{kHz} $$
- Therefore, the bat must move **away** from the observer.
- The bat is the moving source.

---

### 37. Use the Moving-Source Equation
- For a source moving away:
  $$ f_{\mathrm{obs}}
  =
  \frac{f_0}{1+\frac{v_s}{v}} $$
- Rearrange:
  $$ 1+\frac{v_s}{v}
  =
  \frac{f_0}{f_{\mathrm{obs}}} $$
- Therefore:
  $$ \frac{v_s}{v}
  =
  \frac{f_0}{f_{\mathrm{obs}}}-1 $$
- Solve:
  $$ v_s
  =
  v\left(\frac{f_0}{f_{\mathrm{obs}}}-1\right) $$

---

### 38. Numerical Calculation
- Substitute:
  $$ v=343\ \mathrm{m}/\mathrm{s} $$
  $$ f_0=25\ \mathrm{kHz} $$
  $$ f_{\mathrm{obs}}=20\ \mathrm{kHz} $$
- Then:
  $$
  v_s
  =
  343
  \left(
  \frac{25}{20}-1
  \right)\ \mathrm{m}/\mathrm{s}
  $$
- Since:
  $$ \frac{25}{20}-1=\frac{1}{4} $$
- We get:
  $$ v_s\approx86\ \mathrm{m}/\mathrm{s} $$

---

### 39. Interpretation of the Bat Result
- The required speed is approximately:
  $$ 86\ \mathrm{m}/\mathrm{s} $$
- This is about:
  $$ 190\ \mathrm{mph} $$
- That is too fast for an ordinary bat.
- Therefore, a bat cannot normally make a $25\ \mathrm{kHz}$ chirp audible to humans simply by flying away.

---

### 40. Main Physics Takeaways
- Point-source intensity:
  $$ I=\frac{P}{4\pi r^2} $$
- Sound intensity level:
  $$ \beta
  =
  10\log_{10}\left(\frac{I}{I_0}\right)\ \mathrm{dB} $$
- Reference intensity:
  $$ I_0=10^{-12}\ \mathrm{W}/\mathrm{m}^2 $$
- Doubling distance reduces intensity by:
  $$ \frac{1}{4} $$
- Doubling intensity increases sound level by:
  $$ 3\ \mathrm{dB} $$
- Motion toward the other object increases observed frequency.
- Motion away decreases observed frequency.

---

### 41. Main Problem-Solving Strategy
1. Determine whether the moving object is the source or observer.
2. Determine whether it moves toward or away from the other object.
3. Decide whether the observed frequency should be higher or lower.
4. Select the matching Doppler equation.
5. Distinguish:
   $$ v_s,\quad v_o,\quad v $$
6. Solve symbolically before substituting values.
7. Check whether the result is physically reasonable.
