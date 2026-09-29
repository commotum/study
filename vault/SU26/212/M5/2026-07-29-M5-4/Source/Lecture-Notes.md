## Lecture Outline (Superposition, Standing Waves, and Harmonics)

### 1. Course Logistics
- Quiz 2 scores are posted.
- Quiz 2X is available and is due:
  $$ \text{Tuesday at }6{:}00\text{ PM} $$
- The Proctorio version of Quiz 3 opens:
  $$ \text{Saturday at }5{:}00\text{ PM} $$
- Zoom-proctored Quiz 3 sessions occur Monday:
  - during class
  - at $6{:}00\text{ PM}$
- Students should prepare their Quiz 3 note sheet.

---

## Principle of Superposition

### 2. Definition
- Superposition means adding the displacements of overlapping waves.
- If two waves occupy the same location:
  $$ y_{\mathrm{net}}(x,t)=y_1(x,t)+y_2(x,t) $$
- The addition is performed point by point.

---

### 3. Waves Passing Through One Another
- In a linear medium, waves pass through one another without permanently altering each other.
- While they overlap, the observed displacement is their sum.
- Afterward, each wave continues traveling with its original shape.
- Circular ripples produced by raindrops on a pond provide a familiar example.

---

### 4. Completely Constructive Interference
- Consider two identical waves with the same:
  - amplitude
  - frequency
  - wavelength
- If they are in phase, each crest overlaps a crest and each trough overlaps a trough.
- Their amplitudes add:
  $$ A_{\mathrm{net}}=A+A=2A $$
- Frequency and wavelength remain unchanged.

---

### 5. Completely Destructive Interference
- Two identical waves are completely out of phase when:
  - the crest of one overlaps the trough of the other
  - their phase difference is $180^\circ$ or $\pi$ radians
- Their displacements cancel:
  $$ A_{\mathrm{net}}=A-A=0 $$

---

### 6. Partial Interference
- Waves are not always perfectly in phase or perfectly out of phase.
- At different positions and times, their interference may be:
  - partly constructive
  - partly destructive
- The total displacement still follows:
  $$ y_{\mathrm{net}}=y_1+y_2 $$

---

### 7. Beating
- Waves with similar but unequal frequencies repeatedly move into and out of phase.
- Their superposition alternates between:
  - constructive interference
  - destructive interference
- This produces a varying-amplitude envelope called a **beat pattern**.

---

## Wave Reflection

### 8. Reflection at a Fixed End
- A fixed boundary produces a hard reflection.
- The reflected wave is inverted:
  - an upward pulse reflects downward
  - a downward pulse reflects upward
- This corresponds to a phase change of:
  $$ \pi\ \mathrm{rad} $$

---

### 9. Reflection at a Free End
- A free boundary produces a soft reflection.
- The reflected pulse is not inverted.
- It returns with the same displacement orientation as the incident pulse.

---

### 10. Changes in the Medium
- At a boundary between different media, a wave may be divided into:
  - a reflected wave
  - a transmitted wave
- The relative amounts depend on the difference between the two media.
- A sufficiently well-matched boundary can produce little or no reflection.
- Detailed calculations for discontinuities were omitted from this lecture.

---

## Formation of Standing Waves

### 11. Oppositely Traveling Waves
- A standing wave can form from:
  - one wave traveling to the right
  - an equivalent wave traveling to the left
- The two waves travel through the same medium with the same wave speed.
- A stable standing pattern occurs only when the frequency is compatible with the system’s length and boundary conditions.

---

### 12. Nodes
- A **node** is a location that remains stationary:
  $$ A_{\mathrm{node}}=0 $$
- The oppositely traveling waves always interfere destructively at a node.

---

### 13. Antinodes
- An **antinode** is a location where the medium has its maximum oscillation amplitude.
- The oppositely traveling waves interfere constructively at an antinode.

---

### 14. Standing-Wave Appearance
- A standing wave does not appear to propagate along the medium.
- The nodes remain fixed.
- The antinodes repeatedly move between their maximum positive and negative displacements.

---

### 15. Resonant Frequencies
- Only particular frequencies produce stable standing waves.
- These are the system’s:
  - resonant frequencies
  - natural frequencies
  - harmonics
- At a nonresonant frequency, the reflections do not consistently reinforce one another, so no stable node-and-antinode pattern forms.

---

### 16. Roles of the Medium and Source
- For a string, the medium determines the wave speed:
  $$ v_{\mathrm{wave}}=\sqrt{\frac{F_T}{\mu}} $$
- The oscillator determines the frequency:
  $$ f=f_{\mathrm{oscillator}} $$
- The wavelength must then satisfy:
  $$ v_{\mathrm{wave}}=f\lambda $$
- A standing wave appears when this wavelength fits the available length and boundary conditions.

---

### 17. Simulation Demonstration
- Driving the string at approximately the second-harmonic frequency produced one node near its center.
- The approximate resonant frequencies demonstrated were:
  $$ f_1\approx0.44\ \mathrm{Hz} $$
  $$ f_2\approx0.88\ \mathrm{Hz} $$
  $$ f_3\approx1.32\ \mathrm{Hz} $$
- These obey:
  $$ f_2=2f_1 $$
  $$ f_3=3f_1=\frac{3}{2}f_2 $$

---

## Standing Waves on a String

### 18. Fixed-End Boundary Conditions
- A string fixed at both ends must have a node at each end.
- The allowed wavelengths must fit an integer number of half-wavelengths into the string:
  $$ L=m\frac{\lambda_m}{2} $$
- Here:
  $$ m=1,2,3,\ldots $$

---

### 19. Fundamental Mode
- The lowest-frequency standing wave is called:
  - the fundamental
  - the first harmonic
- It contains:
  - nodes at both ends
  - one antinode at the center
- The string length contains half of a wavelength:
  $$ L=\frac{\lambda_1}{2} $$
- Therefore:
  $$ \lambda_1=2L $$

---

### 20. Fundamental Frequency
- Using:
  $$ f=\frac{v}{\lambda} $$
- The fundamental frequency is:
  $$ f_1=\frac{v}{2L} $$

---

### 21. Second Harmonic
- The second harmonic has:
  - nodes at both ends
  - one interior node
  - two antinodes
- One complete wavelength fits into the string:
  $$ \lambda_2=L $$
- Therefore:
  $$ f_2=\frac{v}{L}=2f_1 $$

---

### 22. Third Harmonic
- The third harmonic has:
  - nodes at both ends
  - two interior nodes
  - three antinodes
- Three half-wavelengths fit into the string:
  $$ L=3\frac{\lambda_3}{2} $$
- Therefore:
  $$ \lambda_3=\frac{2L}{3} $$
- Its frequency is:
  $$ f_3=\frac{v}{\lambda_3}
  =\frac{3v_{\mathrm{wave}}}{2L}
  =3f_1 $$

---

### 23. General String Wavelength
- For harmonic number $m$:
  $$ \boxed{\lambda_m=\frac{2L}{m}} $$
- Higher harmonics have shorter wavelengths.

---

### 24. General String Frequency
- Substitute the allowed wavelength into:
  $$ f_m=\frac{v}{\lambda_m} $$
- This gives:
  $$ \boxed{f_m=\frac{mv}{2L}} $$
- Since:
  $$ f_1=\frac{v}{2L} $$
- The harmonic frequencies satisfy:
  $$ \boxed{f_m=mf_1} $$

---

### 25. Harmonic Ratios
- The first several frequencies are:
  $$ f_1=f_1 $$
  $$ f_2=2f_1 $$
  $$ f_3=3f_1 $$
- For example:
  $$ \frac{f_3}{f_2}
  =
  \frac{3f_1}{2f_1}
  =
  \frac{3}{2} $$

---

## Wave Speed on a String

### 26. Linear Mass Density
- The linear mass density is:
  $$ \mu=\frac{m_{\mathrm{wire}}}{L} $$
- Here:
  - $m_{\mathrm{wire}}$ is the total mass of the vibrating wire
  - $L$ is its length
- Units:
  $$ [\mu]=\mathrm{kg}/\mathrm{m} $$

---

### 27. String-Wave Speed
- The wave speed is:
  $$ v_{\mathrm{wave}}=\sqrt{\frac{F_T}{\mu}} $$
- Substituting:
  $$ \mu=\frac{m_{\mathrm{wire}}}{L} $$
- Gives:
  $$ v_{\mathrm{wave}}=\sqrt{\frac{F_TL}{m_{\mathrm{wire}}}} $$

---

### 28. General String-Harmonic Formula
- Combining:
  $$ f_m=\frac{mv}{2L} $$
  with:
  $$ v_{\mathrm{wave}}=\sqrt{\frac{F_TL}{m_{\mathrm{wire}}}} $$
- Gives:
  $$ f_m
  =
  \frac{m}{2L}
  \sqrt{\frac{F_TL}{m_{\mathrm{wire}}}} $$
- Equivalently:
  $$ \boxed{
  f_m
  =
  \frac{m}{2}
  \sqrt{\frac{F_T}{m_{\mathrm{wire}}L}}
  } $$

---

## Example 1: Fundamental Frequency of a Wire

### 29. Given Information
- Wire length:
  $$ L=0.85\ \mathrm{m} $$
- Wire mass:
  $$ m_{\mathrm{wire}}=0.0022\ \mathrm{kg} $$
- Tension:
  $$ F_T=52\ \mathrm{N} $$
- Find:
  $$ f_1 $$

---

### 30. Fundamental Wavelength
- For a string fixed at both ends:
  $$ \lambda_1=2L $$
- Therefore:
  $$ f_1=\frac{v}{2L} $$

---

### 31. Substitute the Wave Speed
- Use:
  $$ v_{\mathrm{wave}}=\sqrt{\frac{F_TL}{m_{\mathrm{wire}}}} $$
- Then:
  $$ f_1
  =
  \frac{1}{2L}
  \sqrt{\frac{F_TL}{m_{\mathrm{wire}}}} $$
- Simplifying:
  $$ f_1
  =
  \frac{1}{2}
  \sqrt{\frac{F_T}{m_{\mathrm{wire}}L}} $$

---

### 32. Numerical Result
- Substitute the given values:
  $$
  f_1
  =
  \frac{1}{2}
  \sqrt{
  \frac{52}
  {(0.0022)(0.85)}
  }
  \ \mathrm{Hz}
  $$
- Therefore:
  $$ \boxed{f_1\approx83.4\ \mathrm{Hz}} $$

---

## Example 2: Third Harmonic with a Hanging Mass

### 33. System Setup
- A hanging mass $M$ supplies the tension in a wire.
- The vibrating wire has:
  - length $L$
  - mass $m_{\mathrm{wire}}$
- The goal is to find the third-harmonic frequency.

---

### 34. Determine the Tension
- For a stationary hanging mass:
  $$ \sum F_y=0 $$
- Therefore:
  $$ F_T=Mg $$

---

### 35. Determine the Wave Speed
- The string-wave speed is:
  $$ v_{\mathrm{wave}}=\sqrt{\frac{F_T}{\mu}} $$
- Using:
  $$ F_T=Mg $$
  and:
  $$ \mu=\frac{m_{\mathrm{wire}}}{L} $$
- Gives:
  $$ v_{\mathrm{wave}}=\sqrt{\frac{MgL}{m_{\mathrm{wire}}}} $$

---

### 36. Third-Harmonic Wavelength
- For the third harmonic:
  $$ \lambda_3=\frac{2L}{3} $$

---

### 37. Third-Harmonic Frequency
- Begin with:
  $$ f_3=\frac{v}{\lambda_3} $$
- Substitute the wavelength:
  $$ f_3
  =
  \frac{3}{2L}
  \sqrt{\frac{MgL}{m_{\mathrm{wire}}}} $$
- Simplifying:
  $$ \boxed{
  f_3
  =
  \frac{3}{2}
  \sqrt{\frac{Mg}{m_{\mathrm{wire}}L}}
  } $$
- Substitution of the diagram’s values gives:
  $$ \boxed{f_3\approx130\ \mathrm{Hz}} $$

---

## Standing Sound Waves in Pipes

### 38. Sound as a Longitudinal Wave
- Sound waves in a pipe are longitudinal.
- Air particles oscillate parallel to the pipe while the disturbance travels through it.
- A transverse-looking curve is only a graph of:
  - particle displacement
  - pressure variation
- It does not mean that the air moves transversely.

---

### 39. Displacement Boundary Conditions
- When diagrams represent air-particle displacement:
  - a closed end is a displacement node
  - an open end is approximately a displacement antinode

---

### 40. Pressure Boundary Conditions
- Pressure boundaries are opposite to displacement boundaries:
  - a closed end is a pressure antinode
  - an open end is approximately a pressure node
- The lecture’s standing-wave diagrams primarily used particle displacement.

---

### 41. Speed of Sound
- For the problems in this lecture:
  $$ v_{\mathrm{wave}}\approx343\ \mathrm{m}/\mathrm{s} $$
- The precise speed depends on properties of the medium and conditions such as:
  - temperature
  - density
  - altitude
- These variations were neglected in the examples.

---

## Closed–Closed Pipes

### 42. Fundamental Mode
- A pipe closed at both ends has displacement nodes at both ends.
- Its fundamental contains half a wavelength:
  $$ L=\frac{\lambda_1}{2} $$
- Therefore:
  $$ \lambda_1=2L $$
  $$ f_1=\frac{v}{2L} $$

---

### 43. Higher Harmonics
- A closed–closed pipe supports the same harmonic sequence as a string fixed at both ends:
  $$ \lambda_m=\frac{2L}{m} $$
  $$ f_m=\frac{mv}{2L}=mf_1 $$
- All positive integer harmonics are allowed:
  $$ m=1,2,3,\ldots $$

---

## Open–Open Pipes

### 44. Fundamental Mode
- An open–open pipe has displacement antinodes at both ends.
- The fundamental still contains half a wavelength:
  $$ \lambda_1=2L $$
- Therefore:
  $$ f_1=\frac{v}{2L} $$

---

### 45. Higher Harmonics
- An open–open pipe has the same allowed harmonic frequencies as:
  - a closed–closed pipe
  - a string fixed at both ends
- Thus:
  $$ \lambda_m=\frac{2L}{m} $$
  $$ f_m=\frac{mv}{2L}=mf_1 $$
- All positive integer harmonics are allowed.

---

## Closed–Open Pipes

### 46. Fundamental Mode
- A closed–open pipe has:
  - a displacement node at the closed end
  - a displacement antinode at the open end
- Its fundamental contains one-quarter of a wavelength:
  $$ L=\frac{\lambda_1}{4} $$
- Therefore:
  $$ \boxed{\lambda_1=4L} $$
- The fundamental frequency is:
  $$ \boxed{f_1=\frac{v}{4L}} $$

---

### 47. Next Allowed Harmonic
- The next pattern satisfying the boundary conditions contains three-quarters of a wavelength:
  $$ L=\frac{3\lambda_3}{4} $$
- Therefore:
  $$ \lambda_3=\frac{4L}{3} $$
- Its frequency is:
  $$ f_3=\frac{v}{\lambda_3}
  =\frac{3v_{\mathrm{wave}}}{4L}
  =3f_1 $$

---

### 48. Odd Harmonics Only
- A closed–open pipe supports only odd harmonic numbers:
  $$ m=1,3,5,7,\ldots $$
- The allowed wavelengths are:
  $$ \boxed{\lambda_m=\frac{4L}{m}} $$
- The allowed frequencies are:
  $$ \boxed{f_m=\frac{mv}{4L}=mf_1} $$
- There is no second harmonic in the ideal closed–open pipe.

---

### 49. Harmonic Number vs. Mode Number
- In a closed–open pipe:
  - $m=1$ is the first resonant mode
  - $m=3$ is the second resonant mode but the third harmonic
  - $m=5$ is the third resonant mode but the fifth harmonic
- This distinction occurs because the even harmonics are absent.

---

## Example 3: Third Harmonic of a Closed–Open Pipe

### 50. Given Information
- Pipe length:
  $$ L=0.85\ \mathrm{m} $$
- Speed of sound:
  $$ v_{\mathrm{wave}}=343\ \mathrm{m}/\mathrm{s} $$
- Find:
  $$ f_3 $$

---

### 51. Third-Harmonic Calculation
- For a closed–open pipe:
  $$ \lambda_3=\frac{4L}{3} $$
- Therefore:
  $$ f_3
  =
  \frac{v}{4L/3}
  =
  \frac{3v_{\mathrm{wave}}}{4L} $$
- Substitute:
  $$
  f_3
  =
  \frac{3(343)}
  {4(0.85)}
  \ \mathrm{Hz}
  $$
- Result:
  $$ f_3\approx303\ \mathrm{Hz} $$
- Rounded as in the lecture:
  $$ \boxed{f_3\approx300\ \mathrm{Hz}} $$

---

## Example 4: Fifth Harmonic of the Same Pipe

### 52. Use a Harmonic Ratio
- For the same closed–open pipe:
  $$ f_3=3f_1 $$
  $$ f_5=5f_1 $$
- Divide:
  $$ \frac{f_5}{f_3}=\frac{5}{3} $$
- Therefore:
  $$ f_5=\frac{5}{3}f_3 $$

---

### 53. Numerical Result
- Using:
  $$ f_3\approx300\ \mathrm{Hz} $$
- Then:
  $$ f_5
  =
  \frac{5}{3}(300\ \mathrm{Hz}) $$
- Therefore:
  $$ \boxed{f_5\approx500\ \mathrm{Hz}} $$

---

### 54. Main Physics Takeaways
- Superposition:
  $$ y_{\mathrm{net}}=y_1+y_2 $$
- Constructive interference increases the resultant amplitude.
- Destructive interference reduces or cancels the resultant amplitude.
- A fixed-end reflection is inverted.
- A free-end reflection is not inverted.
- Standing waves contain fixed nodes and antinodes.
- String-wave speed:
  $$ v_{\mathrm{wave}}=\sqrt{\frac{F_T}{\mu}} $$
- Fixed–fixed string:
  $$ \lambda_m=\frac{2L}{m} $$
  $$ f_m=\frac{mv}{2L}=mf_1 $$
- Closed–closed and open–open pipes obey the same harmonic sequence.
- Closed–open pipe:
  $$ \lambda_m=\frac{4L}{m} $$
  $$ f_m=\frac{mv}{4L}=mf_1 $$
  with:
  $$ m=1,3,5,\ldots $$

---

### 55. Main Problem-Solving Strategy
1. Identify the boundary conditions.
2. Determine whether each end must be a node or antinode.
3. Draw the standing-wave pattern.
4. Relate the system length to the wavelength.
5. Determine the wave speed from the medium:
   $$ v_{\mathrm{wave}}=\sqrt{\frac{F_T}{\mu}} $$
   for a string, or:
   $$ v_{\mathrm{wave}}\approx343\ \mathrm{m}/\mathrm{s} $$
   for sound in air.
6. Use:
   $$ f=\frac{v}{\lambda} $$
7. Check which harmonic numbers are permitted.
8. For closed–open pipes, remember that only odd harmonics occur.
