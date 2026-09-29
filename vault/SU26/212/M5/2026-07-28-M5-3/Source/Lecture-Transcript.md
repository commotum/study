# Physics 212: Sound Intensity, Decibels, and the Doppler Effect

Welcome back to Physics 212.
[View Notes](Lecture-Notes.md)

## Announcements

Quiz 2 has finished being graded, and the scores will be posted this afternoon. The optional Quiz 2X assignment will open at the same time.

Because Quiz 3 is approaching, Quiz 2X will be due Tuesday at 6:00 p.m., after Quiz 3 has been completed. This provides additional time to complete the assignment without interfering as much with Quiz 3 preparation.

Quiz 3 will open Saturday and close Monday for the Proctorio version. The Zoom-proctored versions will be administered on Monday using the same format as the previous quizzes.

You should be completing your Quiz 3 note sheet. Remember to submit it to Gradescope with your photo ID visible before beginning the quiz.

# Review: Energy Transported by a Wave

We previously discussed the energy, power, intensity, and intensity level associated with waves.

Consider a particle in a medium undergoing sinusoidal motion. Its kinetic energy is

$$
K=\frac{1}{2}mu^2.
$$

For simple harmonic motion, the maximum particle speed is

$$
u_{\max}=\omega A,
$$

where $A$ is the amplitude and $\omega$ is the angular frequency.

Because

$$
\omega=2\pi f,
$$

we can also write

$$
u_{\max}=2\pi fA.
$$

The characteristic particle speed is therefore proportional to both the frequency and amplitude:

$$
u\propto fA.
$$

Because kinetic energy depends on the square of the speed,

$$
K\propto u^2,
$$

so

$$
K\propto f^2A^2.
$$

For a sinusoidal wave traveling through a fixed linear medium, the average power transported by the wave has the same frequency and amplitude dependence:

$$
\boxed{
P_{\mathrm{avg}}\propto f^2A^2
}.
$$

Thus:

- Doubling the frequency increases the transported power by a factor of four.
- Doubling the amplitude increases the transported power by a factor of four.
- Doubling both the frequency and amplitude increases the transported power by a factor of sixteen.

The proportionality constant depends on the type of wave and the properties of the medium.

# Intensity

Intensity is the average power transmitted per unit area:

$$
\boxed{
I=\frac{P}{A_s}
},
$$

where $A_s$ is the surface area through which the wave’s power passes.

The SI unit of intensity is

$$
\boxed{
[I]=\mathrm{W}/\mathrm{m}^2
}.
$$

We use $A_s$ for surface area so that it is not confused with the wave amplitude $A$.

Because intensity is proportional to power, a sinusoidal wave in a fixed medium also satisfies

$$
\boxed{
I\propto f^2A^2
}.
$$

# Intensity from an Isotropic Point Source

Consider an ideal point source radiating power uniformly in every direction.

At a distance $r$ from the source, the power is spread over the surface of a sphere. The area of that sphere is

$$
A_s=4\pi r^2.
$$

The intensity is therefore

$$
\boxed{
I(r)=\frac{P}{4\pi r^2}
}.
$$

This is an inverse-square relationship:

$$
I\propto\frac{1}{r^2}.
$$

The total power emitted by the source remains constant, but it is distributed over a progressively larger spherical surface as the wave moves outward.

This expression assumes:

- An ideal point source
- Uniform radiation in every direction
- No absorption by the medium
- No reflections or interference
- Constant source power

## Worked Example: Doubling the Distance from a Speaker

Suppose the sound intensity measured at a distance $r_1$ from a speaker is

$$
I_1=240\ \mathrm{W}/\mathrm{m}^2.
$$

The listener then moves to a distance

$$
r_2=2r_1.
$$

The intensities at the two positions are

$$
I_1=\frac{P}{4\pi r_1^2}
$$

and

$$
I_2=\frac{P}{4\pi r_2^2}.
$$

Taking the ratio eliminates the source power and the factor $4\pi$:

$$
\frac{I_2}{I_1}
=
\frac{
P/(4\pi r_2^2)
}{
P/(4\pi r_1^2)
}.
$$

Therefore,

$$
\frac{I_2}{I_1}
=
\frac{r_1^2}{r_2^2}.
$$

Using $r_2=2r_1$,

$$
\frac{I_2}{I_1}
=
\frac{r_1^2}{(2r_1)^2}.
$$

Thus,

$$
\frac{I_2}{I_1}
=
\frac{1}{4}.
$$

Therefore,

$$
I_2=\frac{1}{4}I_1.
$$

Substituting the original intensity,

$$
I_2
=
\frac{1}{4}
\left(
240\ \mathrm{W}/\mathrm{m}^2
\right).
$$

The resulting intensity is

$$
\boxed{
I_2=60\ \mathrm{W}/\mathrm{m}^2
}.
$$

Doubling the distance from an isotropic point source reduces the intensity to one-fourth of its original value.

# Sound Intensity Level

The human ear can respond to sound intensities covering an enormous numerical range. A logarithmic scale is therefore more convenient than a linear scale.

The **sound intensity level** is defined as

$$
\boxed{
\beta
=
10\log_{10}
\left(
\frac{I}{I_0}
\right)
\ \mathrm{dB}
},
$$

where:

- $\beta$ is the sound intensity level,
- $I$ is the measured sound intensity, and
- $I_0$ is the reference intensity.

The standard reference intensity is

$$
\boxed{
I_0=1.0\times10^{-12}\ \mathrm{W}/\mathrm{m}^2
}.
$$

This is approximately the threshold of human hearing under standard reference conditions.

The unit of intensity level is the decibel:

$$
10\ \mathrm{dB}=1\ \mathrm{bel}.
$$

Because the scale is logarithmic, multiplying the physical intensity corresponds to adding to the intensity level.

## Solving for Intensity

Starting with

$$
\beta
=
10\log_{10}
\left(
\frac{I}{I_0}
\right)
\ \mathrm{dB},
$$

divide by $10\ \mathrm{dB}$:

$$
\frac{\beta}{10\ \mathrm{dB}}
=
\log_{10}
\left(
\frac{I}{I_0}
\right).
$$

Raise $10$ to the power of each side:

$$
10^{\beta/(10\ \mathrm{dB})}
=
\frac{I}{I_0}.
$$

Therefore,

$$
\boxed{
I
=
I_0
10^{\beta/(10\ \mathrm{dB})}
}.
$$

## Worked Example: Intensity of Normal Conversation

A normal conversation has an approximate sound intensity level of

$$
\beta=60\ \mathrm{dB}.
$$

The corresponding intensity is

$$
I
=
I_0
10^{\beta/(10\ \mathrm{dB})}.
$$

Substituting the reference intensity,

$$
I
=
\left(
1.0\times10^{-12}\ \mathrm{W}/\mathrm{m}^2
\right)
10^{60/10}.
$$

Because

$$
\frac{60}{10}=6,
$$

we obtain

$$
I
=
\left(
1.0\times10^{-12}\ \mathrm{W}/\mathrm{m}^2
\right)
10^6.
$$

Therefore,

$$
\boxed{
I=1.0\times10^{-6}\ \mathrm{W}/\mathrm{m}^2
}.
$$

Because

$$
1\ \mathrm{mW}=10^{-3}\ \mathrm{W},
$$

this may also be written as

$$
\boxed{
I=1.0\times10^{-3}\ \mathrm{mW}/\mathrm{m}^2
}
$$

or

$$
\boxed{
I=0.0010\ \mathrm{mW}/\mathrm{m}^2
}.
$$

# Comparing Two Intensity Levels

Suppose two sound intensities $I_1$ and $I_2$ have intensity levels $\beta_1$ and $\beta_2$.

Their definitions are

$$
\beta_1
=
10\log_{10}
\left(
\frac{I_1}{I_0}
\right)
\ \mathrm{dB}
$$

and

$$
\beta_2
=
10\log_{10}
\left(
\frac{I_2}{I_0}
\right)
\ \mathrm{dB}.
$$

Subtracting gives

$$
\beta_2-\beta_1
=
10
\left[
\log_{10}
\left(
\frac{I_2}{I_0}
\right)
-
\log_{10}
\left(
\frac{I_1}{I_0}
\right)
\right]
\mathrm{dB}.
$$

Using the logarithm identity

$$
\log_{10}B-\log_{10}A
=
\log_{10}
\left(
\frac{B}{A}
\right),
$$

we obtain

$$
\beta_2-\beta_1
=
10\log_{10}
\left[
\frac{
I_2/I_0
}{
I_1/I_0
}
\right]
\mathrm{dB}.
$$

The reference intensity cancels:

$$
\boxed{
\beta_2-\beta_1
=
10\log_{10}
\left(
\frac{I_2}{I_1}
\right)
\ \mathrm{dB}
}.
$$

This equation allows us to compare sound levels without explicitly using $I_0$.

## Worked Example: Two People Talking

Suppose one person produces an intensity level of

$$
\beta_1=60\ \mathrm{dB}
$$

at a listener’s position.

Now suppose a second person speaks with the same power at the same distance. If the two speakers are independent, their intensities add.

The total intensity is therefore

$$
I_2=2I_1.
$$

The change in intensity level is

$$
\beta_2-\beta_1
=
10\log_{10}
\left(
\frac{I_2}{I_1}
\right)
\ \mathrm{dB}.
$$

Substituting $I_2=2I_1$,

$$
\beta_2-\beta_1
=
10\log_{10}(2)
\ \mathrm{dB}.
$$

Because

$$
\log_{10}(2)\approx0.301,
$$

we obtain

$$
\beta_2-\beta_1
\approx
3.01\ \mathrm{dB}.
$$

Therefore,

$$
\beta_2
=
\beta_1+3.01\ \mathrm{dB}.
$$

Using $\beta_1=60\ \mathrm{dB}$,

$$
\boxed{
\beta_2\approx63\ \mathrm{dB}
}.
$$

Doubling the physical intensity does not double the decibel level. It increases the intensity level by approximately $3\ \mathrm{dB}$.

More generally:

$$
\boxed{
I_2=2I_1
\quad\Longrightarrow\quad
\beta_2=\beta_1+3.0\ \mathrm{dB}
}.
$$

# The Doppler Effect

The **Doppler effect** is the change in observed frequency caused by relative motion between a wave source and an observer.

A familiar example is the sound of a siren on a moving vehicle:

- As the vehicle approaches, the observed frequency is higher.
- After it passes and moves away, the observed frequency is lower.

The same qualitative phenomenon occurs for light, although the equations developed here are specifically for sound waves propagating through a material medium.

We will use the following notation:

- $f_0$ is the frequency emitted in the source’s rest frame.
- $f_{\mathrm{obs}}$ is the frequency measured by the observer.
- $v_o$ is the observer’s speed relative to the medium.
- $v_s$ is the source’s speed relative to the medium.
- $v$ is the speed of sound through the medium.

For sound in air under the conditions used in these examples,

$$
\boxed{
v=343\ \mathrm{m}/\mathrm{s}
}.
$$

The speeds $v_o$ and $v_s$ will be treated as positive magnitudes. The appropriate sign is built into each of the following case-specific formulas.

# Moving Observer and Stationary Source

When the source is stationary and the observer moves through the wave, the wavelength in the medium remains unchanged. The observer simply encounters the wavefronts at a different rate.

## Observer Moving Toward the Source

An observer moving toward the source encounters wavefronts more frequently. The observed frequency is

$$
\boxed{
f_{\mathrm{obs}}
=
f_0
\left(
1+\frac{v_o}{v}
\right)
}.
$$

Because the factor in parentheses is greater than one,

$$
f_{\mathrm{obs}}>f_0.
$$

## Observer Moving Away from the Source

An observer moving away from the source encounters wavefronts less frequently:

$$
\boxed{
f_{\mathrm{obs}}
=
f_0
\left(
1-\frac{v_o}{v}
\right)
}.
$$

In this case,

$$
f_{\mathrm{obs}}<f_0.
$$

# Moving Source and Stationary Observer

When the source moves through the medium, the source changes the spacing between the wavefronts.

Wavefronts are compressed in front of an approaching source and spread farther apart behind a receding source. The wavelength in the medium therefore changes.

## Source Moving Toward the Observer

For a source moving toward a stationary observer,

$$
\boxed{
f_{\mathrm{obs}}
=
\frac{f_0}{
1-\frac{v_s}{v}
}
}.
$$

The denominator is less than one, so

$$
f_{\mathrm{obs}}>f_0.
$$

## Source Moving Away from the Observer

For a source moving away from a stationary observer,

$$
\boxed{
f_{\mathrm{obs}}
=
\frac{f_0}{
1+\frac{v_s}{v}
}
}.
$$

The denominator is greater than one, so

$$
f_{\mathrm{obs}}<f_0.
$$

# Why the Observer and Source Formulas Differ

The effects of source motion and observer motion are not simply inverses of one another.

When the observer moves, the wave pattern in the medium remains unchanged. The observer merely crosses the existing wavefronts more or less rapidly.

When the source moves, it changes the spacing of the wavefronts in the medium itself:

- Motion toward the observer compresses the wavelength.
- Motion away from the observer stretches the wavelength.

Because these are physically different situations, the source speed and observer speed appear differently in the Doppler equations.

# Worked Example: A Bat Flying Toward a Singer

A singer produces a note with frequency

$$
f_0=880\ \mathrm{Hz}.
$$

A bat flies toward the singer at

$$
v_o=35\ \mathrm{m}/\mathrm{s}.
$$

The singer is the stationary source, while the bat is the moving observer. Because the observer moves toward the source, we use

$$
f_{\mathrm{obs}}
=
f_0
\left(
1+\frac{v_o}{v}
\right).
$$

Substituting the known values,

$$
f_{\mathrm{obs}}
=
(880\ \mathrm{Hz})
\left(
1+
\frac{
35\ \mathrm{m}/\mathrm{s}
}{
343\ \mathrm{m}/\mathrm{s}
}
\right).
$$

The speed units cancel inside the parentheses:

$$
f_{\mathrm{obs}}
=
(880\ \mathrm{Hz})(1.102).
$$

Therefore,

$$
f_{\mathrm{obs}}
\approx969.8\ \mathrm{Hz}.
$$

To the appropriate precision,

$$
\boxed{
f_{\mathrm{obs}}\approx970\ \mathrm{Hz}
}.
$$

The observed frequency is higher than the emitted frequency because the bat is moving into the approaching wavefronts.

# Worked Example: Can a Receding Bat Chirp Enter the Human Audible Range?

Suppose a bat emits an echolocation chirp at

$$
f_0=25\ \mathrm{kHz}.
$$

The approximate upper limit of human hearing is

$$
f_{\mathrm{obs}}=20\ \mathrm{kHz}.
$$

We want to determine how rapidly the bat would need to move for its chirp to be Doppler-shifted down to $20\ \mathrm{kHz}$.

Because the observed frequency must be lower than the emitted frequency, the bat must move **away** from the observer.

The bat is the moving source, and the observer is stationary. We therefore use

$$
f_{\mathrm{obs}}
=
\frac{f_0}{
1+\frac{v_s}{v}
}.
$$

Substituting the known frequencies,

$$
20\ \mathrm{kHz}
=
\frac{
25\ \mathrm{kHz}
}{
1+\frac{v_s}{343\ \mathrm{m}/\mathrm{s}}
}.
$$

Divide both sides by $25\ \mathrm{kHz}$:

$$
\frac{20}{25}
=
\frac{1}{
1+\frac{v_s}{343\ \mathrm{m}/\mathrm{s}}
}.
$$

Taking the reciprocal gives

$$
1+\frac{v_s}{343\ \mathrm{m}/\mathrm{s}}
=
\frac{25}{20}.
$$

Therefore,

$$
\frac{v_s}{343\ \mathrm{m}/\mathrm{s}}
=
\frac{25}{20}-1.
$$

Since

$$
\frac{25}{20}=1.25,
$$

we obtain

$$
\frac{v_s}{343\ \mathrm{m}/\mathrm{s}}
=
0.25.
$$

Thus,

$$
v_s
=
(343\ \mathrm{m}/\mathrm{s})(0.25).
$$

Therefore,

$$
\boxed{
v_s\approx86\ \mathrm{m}/\mathrm{s}
}.
$$

This is approximately

$$
\boxed{
v_s\approx190\ \mathrm{mph}
}.
$$

That speed is unrealistically high for a flying bat. A bat emitting a $25\ \mathrm{kHz}$ chirp therefore cannot ordinarily lower the frequency into the human audible range merely by flying away from the listener.

# General Strategy for Doppler-Effect Problems

## 1. Identify the Emitted and Observed Frequencies

The emitted frequency is $f_0$.

The frequency measured by the listener or detector is $f_{\mathrm{obs}}$.

## 2. Identify What Is Moving

Determine whether the moving object is:

- The observer
- The source
- Both

The observer and source formulas are physically different.

## 3. Determine Whether the Frequency Should Increase or Decrease

Before choosing an equation, make a qualitative prediction:

- Motion toward produces a higher observed frequency.
- Motion away produces a lower observed frequency.

This provides an immediate check on the selected signs.

## 4. Distinguish Signal Speed from Source or Observer Speed

The sound speed $v$ describes the propagation of the wave through the medium.

The source speed $v_s$ describes the motion of the object producing the sound.

The observer speed $v_o$ describes the motion of the listener or detector.

These are different physical quantities.

## 5. Solve Symbolically Before Substituting Values

For example, for a receding source,

$$
f_{\mathrm{obs}}
=
\frac{f_0}{
1+\frac{v_s}{v}
}.
$$

Solving symbolically for the source speed gives

$$
1+\frac{v_s}{v}
=
\frac{f_0}{f_{\mathrm{obs}}},
$$

$$
\frac{v_s}{v}
=
\frac{f_0}{f_{\mathrm{obs}}}-1,
$$

and therefore

$$
\boxed{
v_s
=
v
\left(
\frac{f_0}{f_{\mathrm{obs}}}-1
\right)
}.
$$

The numerical values should be inserted only after this symbolic result has been obtained.

## 6. Check the Physical Meaning of the Result

Confirm that:

- An approaching source or observer gives $f_{\mathrm{obs}}>f_0$.
- A receding source or observer gives $f_{\mathrm{obs}}<f_0$.
- The units of the calculated speed are correct.
- The resulting speed is physically plausible.

# Summary

For a sinusoidal wave in a fixed linear medium,

$$
\boxed{
P_{\mathrm{avg}}\propto f^2A^2
}
$$

and

$$
\boxed{
I\propto f^2A^2
}.
$$

Intensity is power per unit area:

$$
\boxed{
I=\frac{P}{A_s}
}.
$$

For an isotropic point source,

$$
\boxed{
I=\frac{P}{4\pi r^2}
}.
$$

Therefore,

$$
I\propto\frac{1}{r^2}.
$$

Doubling the distance reduces the intensity to one-fourth of its original value.

Sound intensity level is

$$
\boxed{
\beta
=
10\log_{10}
\left(
\frac{I}{I_0}
\right)
\ \mathrm{dB}
}
$$

with

$$
\boxed{
I_0=1.0\times10^{-12}\ \mathrm{W}/\mathrm{m}^2
}.
$$

Solving for intensity gives

$$
\boxed{
I
=
I_0
10^{\beta/(10\ \mathrm{dB})}
}.
$$

The difference between two sound intensity levels is

$$
\boxed{
\beta_2-\beta_1
=
10\log_{10}
\left(
\frac{I_2}{I_1}
\right)
\ \mathrm{dB}
}.
$$

Doubling intensity increases the sound intensity level by approximately

$$
\boxed{
3.0\ \mathrm{dB}
}.
$$

For a stationary source and moving observer:

$$
\boxed{
f_{\mathrm{obs}}
=
f_0
\left(
1+\frac{v_o}{v}
\right)
}
$$

when the observer moves toward the source, and

$$
\boxed{
f_{\mathrm{obs}}
=
f_0
\left(
1-\frac{v_o}{v}
\right)
}
$$

when the observer moves away.

For a moving source and stationary observer:

$$
\boxed{
f_{\mathrm{obs}}
=
\frac{f_0}{
1-\frac{v_s}{v}
}
}
$$

when the source moves toward the observer, and

$$
\boxed{
f_{\mathrm{obs}}
=
\frac{f_0}{
1+\frac{v_s}{v}
}
}
$$

when the source moves away.

Approaching motion produces a higher observed frequency. Receding motion produces a lower observed frequency.

---

Up Next: [Superposition, Standing Waves, and Harmonics](../../2026-07-29-M5-4/Source/Lecture-Transcript.md)
Previous: [Traveling Waves, Refraction, and Intensity](../../2026-07-27-M5-2/Source/Lecture-Transcript.md)

---
