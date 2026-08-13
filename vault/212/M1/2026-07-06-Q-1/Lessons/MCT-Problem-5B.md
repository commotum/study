# Constant Angular Acceleration When Time Is Missing

<!--
lesson-id: 212-M1-080
topic-code: M1.80
-->

## Table of Contents

- [Introduction](#introduction)
- [Select the No-Time Equation](#select-the-no-time-equation)
- [Recover Angular Acceleration From Rim Data](#recover-angular-acceleration-from-rim-data)
- [Keep the Signs Consistent While Slowing](#keep-the-signs-consistent-while-slowing)
- [Track a Negative Rotation Direction](#track-a-negative-rotation-direction)
- [Summary](#summary)

## Prerequisites

- Distinguish signed angular velocity $\omega$ from angular acceleration $\alpha$; angular speed is the magnitude $|\omega|$.
- Convert a diameter to a radius and centimeters to meters.
- Use $a_t=r\alpha$ for the **tangential** acceleration of a point at radius $r$.
- Use $1\,\mathrm{rev}=2\pi\,\mathrm{rad}$.

---

<a id="introduction"></a>
## Introduction

Part A handled constant-angular-acceleration problems in which the elapsed time was known. Sometimes a wheel is described instead by its initial and final angular velocities and its angular acceleration, but not by how long the change takes. When \(\alpha\) is constant, the same kinematics family can eliminate time.

The recognition cue is a request for angular displacement with **no time given**, together with \(\omega_i\), \(\omega_f\), and \(\alpha\) or enough information to find them. Under those conditions, use the rotational counterpart of the familiar linear no-time equation \(v_f^2=v_i^2+2a\Delta x\):

$$
\omega_f^2=\omega_i^2+2\alpha\Delta\theta.
$$

This equation connects exactly four quantities: $\omega_i$, $\omega_f$, $\alpha$, and $\Delta\theta$. Isolate the target before inserting numbers:

$$
\begin{aligned}
\omega_f^2&=\omega_i^2+2\alpha\Delta\theta \\
\omega_f^2-\omega_i^2&=2\alpha\Delta\theta \\
\boxed{\Delta\theta&=\frac{\omega_f^2-\omega_i^2}{2\alpha}}.
\end{aligned}
$$

The division step assumes $\alpha\ne0$. If $\alpha=0$, angular velocity is constant, so different endpoint angular velocities are impossible. Equal nonzero endpoint angular velocities still require the elapsed time to determine $\Delta\theta$; if both endpoint angular velocities are zero, then $\Delta\theta=0$.

Work in this order:

1. Confirm that $\alpha$ is constant and time is absent.
2. List $\omega_i$, $\omega_f$, and $\alpha$, and identify any quantity that must be recovered first.
3. Choose a positive rotation direction and attach signs to both angular velocities and $\alpha$.
4. Substitute into the isolated expression, keeping each angular velocity inside its square.
5. Check the sign, units, and scale of $\Delta\theta$; convert radians to revolutions only if requested.

---

<a id="select-the-no-time-equation"></a>
## Select the No-Time Equation

Keep the structure $\omega_f^2-\omega_i^2$: it is the difference of two squared endpoint velocities, not $(\omega_f-\omega_i)^2$.

**Example:** A rotor speeds up with constant angular acceleration from $4.0\,\mathrm{rad/s}$ to $10.0\,\mathrm{rad/s}$. If $\alpha=3.0\,\mathrm{rad/s^2}$ and no time is given, find the angular displacement.

**Explanation**

The known quantities are $\omega_i$, $\omega_f$, and $\alpha$; the target is $\Delta\theta$. Because time is absent, use the equation that eliminates time:

$$
\begin{aligned}
\Delta\theta
&=\frac{\omega_f^2-\omega_i^2}{2\alpha} \\
&=\frac{(10.0\,\mathrm{rad/s})^2-(4.0\,\mathrm{rad/s})^2}
        {2(3.0\,\mathrm{rad/s^2})} \\
&=\frac{100-16}{6}\,\mathrm{rad} \\
&=14\,\mathrm{rad}.
\end{aligned}
$$

Both the numerator and denominator are positive, so the positive displacement agrees with a rotor speeding up in the chosen positive direction.

```quiz
type: radio
id: mct-p5b-direct-no-time
content: |-
  A turntable speeds up with constant angular acceleration from $6.0\,\mathrm{rad/s}$ to $14.0\,\mathrm{rad/s}$. If $\alpha=5.0\,\mathrm{rad/s^2}$ and no time is given, what is its angular displacement?
options:
- id: mct-p5b-direct-no-time-a
  content: |-
    $16\,\mathrm{rad}$
  correct: true
  feedback: |-
    With constant $\alpha$ and no time, isolate displacement as $\Delta\theta=(\omega_f^2-\omega_i^2)/(2\alpha)$. Here $(14^2-6^2)/(2\cdot5)=(196-36)/10=16\,\mathrm{rad}$, positive as expected for positive rotation with positive angular acceleration.
- id: mct-p5b-direct-no-time-b
  content: |-
    $-16\,\mathrm{rad}$
  feedback: |-
    This reverses the squared-speed subtraction. The equation gives final squared minus initial squared, $14^2-6^2>0$; because $\alpha>0$, the displacement must also be positive.
- id: mct-p5b-direct-no-time-c
  content: |-
    $32\,\mathrm{rad}$
  feedback: |-
    This omits the factor of $2$ multiplying $\alpha$. The governing term is $2\alpha\Delta\theta$, so the denominator is $2(5.0)=10$, not $5.0$.
- id: mct-p5b-direct-no-time-d
  content: |-
    $23.2\,\mathrm{rad}$
  feedback: |-
    This adds the squared angular speeds. Rearranging $\omega_f^2=\omega_i^2+2\alpha\Delta\theta$ requires subtracting $\omega_i^2$ from both sides, so the numerator is $196-36$, not $196+36$.
- id: mct-p5b-direct-no-time-e
  content: |-
    $0.80\,\mathrm{rad}$
  feedback: |-
    This uses the unsquared change $\omega_f-\omega_i$ in a relationship built from squared angular speeds. Keep both velocities squared: the numerator is $14^2-6^2=160\,\mathrm{rad^2/s^2}$.
```

---

<a id="recover-angular-acceleration-from-rim-data"></a>
## Recover Angular Acceleration From Rim Data

If a problem gives acceleration at the rim instead of $\alpha$, use $a_t=r\alpha$ only when the supplied acceleration is the tangential component. Radial acceleration or total acceleration cannot be substituted for $a_t$ without first resolving its tangential component.

**Source-video example:** A wheel has diameter $80\,\mathrm{cm}$ and speeds up from $30\,\mathrm{rad/s}$ to $80\,\mathrm{rad/s}$. The tangential acceleration at its rim is $15\,\mathrm{m/s^2}$. How many revolutions does the wheel turn through? Assume constant angular acceleration.

**Explanation**

The target is angular displacement, but time is absent and angular acceleration is not given directly. Recover the angular acceleration from the rim data before using the no-time equation.

First convert diameter to radius and orient the length conversion so centimeters cancel:

$$
r=\frac{80\,\mathrm{cm}}{2}
\left(\frac{1\,\mathrm{m}}{100\,\mathrm{cm}}\right)
=0.400\,\mathrm{m}.
$$

Because the given rim acceleration is tangential, recover angular acceleration:

$$
\alpha=\frac{a_t}{r}
=\frac{15\,\mathrm{m/s^2}}{0.400\,\mathrm{m}}
=37.5\,\mathrm{rad/s^2}.
$$

Now isolate and calculate the angular displacement:

$$
\begin{aligned}
\Delta\theta
&=\frac{\omega_f^2-\omega_i^2}{2\alpha} \\
&=\frac{(80\,\mathrm{rad/s})^2-(30\,\mathrm{rad/s})^2}
        {2(37.5\,\mathrm{rad/s^2})} \\
&=\frac{6400-900}{75}\,\mathrm{rad} \\
&=73.33\,\mathrm{rad}.
\end{aligned}
$$

Only now convert the requested result to revolutions:

$$
73.33\,\mathrm{rad}
\left(\frac{1\,\mathrm{rev}}{2\pi\,\mathrm{rad}}\right)
=11.67\,\mathrm{rev}.
$$

Since $\omega_f^2-\omega_i^2>0$ and $\alpha>0$, $\Delta\theta>0$. A quick estimate gives the same scale: $5500/75$ is tens of radians, and dividing by about $6.28$ gives roughly a dozen revolutions.

The units also reduce to radians:

$$
[\Delta\theta]
=\frac{(\mathrm{rad/s})^2}{\mathrm{rad/s^2}}
=\mathrm{rad},
$$

where radians are dimensionless but retained to label the angular result.

```quiz
type: radio
id: mct-p5b-linked-rim-data
content: |-
  A wheel has diameter $0.600\,\mathrm{m}$ and speeds up from $12.0\,\mathrm{rad/s}$ to $30.0\,\mathrm{rad/s}$. Its rim has constant tangential acceleration $9.00\,\mathrm{m/s^2}$. Through how many revolutions does the wheel turn?
options:
- id: mct-p5b-linked-rim-data-a
  content: |-
    $2.01\,\mathrm{rev}$
  correct: true
  feedback: |-
    The radius is $0.300\,\mathrm{m}$, so $\alpha=a_t/r=9.00/0.300=30.0\,\mathrm{rad/s^2}$. Then $\Delta\theta=(30.0^2-12.0^2)/(2\cdot30.0)=12.6\,\mathrm{rad}$, and $12.6/(2\pi)=2.01\,\mathrm{rev}$.
- id: mct-p5b-linked-rim-data-b
  content: |-
    $4.01\,\mathrm{rev}$
  feedback: |-
    This is twice the correct displacement. That factor-of-two error results from using the $0.600\,\mathrm{m}$ diameter as the radius or from omitting the $2$ in $2\alpha\Delta\theta$. Use $r=0.300\,\mathrm{m}$ and the full denominator $2\alpha$.
- id: mct-p5b-linked-rim-data-c
  content: |-
    $12.6\,\mathrm{rev}$
  feedback: |-
    The value $12.6$ is the displacement in radians, not revolutions. Because one revolution is $2\pi$ radians, divide $12.6\,\mathrm{rad}$ by $2\pi\,\mathrm{rad/rev}$ to obtain $2.01\,\mathrm{rev}$.
- id: mct-p5b-linked-rim-data-d
  content: |-
    $0.319\,\mathrm{rev}$
  feedback: |-
    This divides by $2\pi$ twice. The no-time equation already gives $12.6\,\mathrm{rad}$; a single factor $1\,\mathrm{rev}/(2\pi\,\mathrm{rad})$ converts it to $2.01\,\mathrm{rev}$.
- id: mct-p5b-linked-rim-data-e
  content: |-
    $-2.01\,\mathrm{rev}$
  feedback: |-
    The wheel is speeding up in the stated positive direction, so $\omega_f^2-\omega_i^2$ and $\alpha$ are both positive. Their quotient must give a positive angular displacement, not a negative one.
```

---

<a id="keep-the-signs-consistent-while-slowing"></a>
## Keep the Signs Consistent While Slowing

**Example:** A flywheel rotates in the positive direction and slows from $18\,\mathrm{rad/s}$ to $6.0\,\mathrm{rad/s}$ with constant angular acceleration $-4.0\,\mathrm{rad/s^2}$. Find its angular displacement while slowing.

**Explanation**

Slowing positive rotation means $\omega_i>0$, $\omega_f>0$, and $\alpha<0$. Apply the same isolated equation without discarding the sign of $\alpha$:

$$
\begin{aligned}
\Delta\theta
&=\frac{\omega_f^2-\omega_i^2}{2\alpha} \\
&=\frac{6.0^2-18^2}{2(-4.0)} \\
&=\frac{-288}{-8} \\
&=36\,\mathrm{rad}.
\end{aligned}
$$

The displacement is positive because the wheel continues rotating in the positive direction while its positive angular speed decreases. A negative numerator divided by a negative angular acceleration gives the physically consistent positive result.

```quiz
type: radio
id: mct-p5b-slowing-signs
content: |-
  A flywheel rotates in the positive direction and slows from $20\,\mathrm{rad/s}$ to $8.0\,\mathrm{rad/s}$ with constant angular acceleration $-6.0\,\mathrm{rad/s^2}$. What is its angular displacement during the slowdown?
options:
- id: mct-p5b-slowing-signs-a
  content: |-
    $28\,\mathrm{rad}$
  correct: true
  feedback: |-
    For positive rotation that slows, $\omega_f^2-\omega_i^2<0$ and $\alpha<0$, so the displacement is positive. Numerically, $(8^2-20^2)/(2\cdot-6)=(-336)/(-12)=28\,\mathrm{rad}$.
- id: mct-p5b-slowing-signs-b
  content: |-
    $-28\,\mathrm{rad}$
  feedback: |-
    Negative angular acceleration describes the decrease in positive angular velocity; it does not by itself make displacement negative. The wheel is still turning positively, and the two negative signs in $(-336)/(-12)$ produce $+28\,\mathrm{rad}$.
- id: mct-p5b-slowing-signs-c
  content: |-
    $56\,\mathrm{rad}$
  feedback: |-
    This omits the factor $2$ in the denominator. The no-time equation contains $2\alpha\Delta\theta$, so divide the squared-speed difference by $2(-6.0)=-12$, not by $-6.0$.
- id: mct-p5b-slowing-signs-d
  content: |-
    $38.7\,\mathrm{rad}$
  feedback: |-
    This uses the sum of the squared speeds. Rearranging the governing equation requires the difference $\omega_f^2-\omega_i^2=8^2-20^2$, which is negative for a slowdown.
- id: mct-p5b-slowing-signs-e
  content: |-
    $1.0\,\mathrm{rad}$
  feedback: |-
    This substitutes the unsquared change $\omega_f-\omega_i$. The no-time relationship compares squared angular speeds, so the numerator must be $8^2-20^2=-336$, not $8-20=-12$.
```

---

<a id="track-a-negative-rotation-direction"></a>
## Track a Negative Rotation Direction

When an angular velocity is negative, put the entire signed value in parentheses before squaring: $(-5)^2=25$. Squaring removes the velocity signs, but the sign of $\alpha$ remains.

**Example:** With counterclockwise chosen positive, a rotor spins clockwise and speeds up from $\omega_i=-5.0\,\mathrm{rad/s}$ to $\omega_f=-13\,\mathrm{rad/s}$. Its constant angular acceleration is $\alpha=-4.0\,\mathrm{rad/s^2}$. Find $\Delta\theta$.

**Explanation**

Substitute both signed angular velocities with parentheses and keep the sign of $\alpha$:

$$
\begin{aligned}
\Delta\theta
&=\frac{(-13)^2-(-5.0)^2}{2(-4.0)} \\
&=\frac{169-25}{-8} \\
&=-18\,\mathrm{rad}.
\end{aligned}
$$

The negative result matches the wheel's clockwise rotation, which is the defined negative direction. Angular **speed** increased even though the signed displacement is negative.

```quiz
type: radio
id: mct-p5b-negative-direction
content: |-
  Counterclockwise is positive. A rotor spins clockwise and speeds up from $\omega_i=-4.0\,\mathrm{rad/s}$ to $\omega_f=-10.0\,\mathrm{rad/s}$ with constant $\alpha=-3.0\,\mathrm{rad/s^2}$. What is its angular displacement?
options:
- id: mct-p5b-negative-direction-a
  content: |-
    $-14\,\mathrm{rad}$
  correct: true
  feedback: |-
    The squared-speed difference is $(-10)^2-(-4)^2=84$, while $2\alpha=-6.0\,\mathrm{rad/s^2}$. Thus $\Delta\theta=84/(-6)=-14\,\mathrm{rad}$, matching clockwise motion under the stated sign convention.
- id: mct-p5b-negative-direction-b
  content: |-
    $14\,\mathrm{rad}$
  feedback: |-
    Squaring the angular velocities makes the numerator positive, but the denominator still contains the negative angular acceleration. The quotient is negative, which agrees with the rotor's clockwise displacement.
- id: mct-p5b-negative-direction-c
  content: |-
    $-28\,\mathrm{rad}$
  feedback: |-
    This omits the factor $2$ attached to $\alpha$. Dividing $84$ by $-3.0$ gives $-28$, but the governing denominator is $2(-3.0)=-6.0$, giving $-14\,\mathrm{rad}$.
- id: mct-p5b-negative-direction-d
  content: |-
    $1.0\,\mathrm{rad}$
  feedback: |-
    This uses $\omega_f-\omega_i=-6$ instead of the required squared-speed difference. Substitute $(-10)^2-(-4)^2=84$ into the no-time equation; the negative acceleration then gives a negative displacement.
- id: mct-p5b-negative-direction-e
  content: |-
    $-19.3\,\mathrm{rad}$
  feedback: |-
    This uses the sum $(-10)^2+(-4)^2=116$. Rearranging $\omega_f^2=\omega_i^2+2\alpha\Delta\theta$ requires subtracting the initial squared speed, so the numerator is $100-16=84$.
```

---

<a id="summary"></a>
## Summary

When $\alpha$ is constant, angular displacement is requested, and time is missing:

1. Use $\omega_f^2=\omega_i^2+2\alpha\Delta\theta$.
2. Rearrange first: $\Delta\theta=(\omega_f^2-\omega_i^2)/(2\alpha)$.
3. If rim data are supplied, convert diameter to radius and use only the tangential component in $\alpha=a_t/r$.
4. Keep signed values through the calculation; compare the sign of $\Delta\theta$ with the actual rotation direction.
5. Expect radians from the equation, then divide by $2\pi$ once if revolutions are requested.

Check that both angular velocities were squared, the denominator includes $2\alpha$, and the units reduce to angle. Estimate the numerator divided by the denominator to catch a misplaced factor or exponent.

<!-- lesson-nav:start -->
---

```update-progress
```

[[212/Home|Home]]
[[212/0. Table of Contents/TOC|Table of Contents]]

---
<!-- lesson-nav:end -->
