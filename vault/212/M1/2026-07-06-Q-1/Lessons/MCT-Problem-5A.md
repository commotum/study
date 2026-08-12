# Constant Angular Acceleration When Time Is Known

<!--
lesson-id: 212-M1-079
topic-code: M1.79
-->

## Table of Contents

- [Introduction](#introduction)
- [Translate the Linear Equations](#translate-the-linear-equations)
- [Find Final Angular Velocity](#find-final-angular-velocity)
- [Find Displacement From Angular Acceleration](#find-displacement-from-angular-acceleration)
- [Use Endpoint Angular Velocities](#use-endpoint-angular-velocities)
- [Keep the Sign When Rotation Slows](#keep-the-sign-when-rotation-slows)
- [Summary](#summary)

## Prerequisites

- Choose and use a positive rotational direction.
- Rearrange one-step equations and evaluate squares.
- Use \(1\,\mathrm{rev}=2\pi\,\mathrm{rad}\).

---

<a id="introduction"></a>
## Introduction

Use the equations in this lesson only over an interval where angular acceleration \(\alpha\) is constant. The recognition cue is a constant \(\alpha\) together with a known or requested time \(t\).

Start every problem with a known/target list chosen from

$$
\omega_i,\quad \omega_f,\quad \alpha,\quad t,\quad \Delta\theta.
$$

Then choose the equation that contains the target and the known quantities without introducing an extra unknown:

| Target and useful givens | Equation |
| --- | --- |
| \(\omega_f\) from \(\omega_i,\alpha,t\) | \(\omega_f=\omega_i+\alpha t\) |
| \(\Delta\theta\) from \(\omega_i,\alpha,t\) | \(\Delta\theta=\omega_i t+\frac12\alpha t^2\) |
| \(\Delta\theta\) from \(\omega_i,\omega_f,t\) | \(\Delta\theta=\dfrac{\omega_i+\omega_f}{2}t\) |

Use a target-first routine:

1. Write the requested symbol as the target.
2. Translate each phrase into a signed value and unit.
3. Choose an equation containing the target and the supplied values.
4. Isolate the target before substituting if it is not already alone.

“Starts from rest” means \(\omega_i=0\). Keep signs during the calculation: with counterclockwise chosen positive, clockwise angular velocity is negative, and an angular acceleration opposing a positive angular velocity is negative. Solve in radians first and convert to revolutions only if the requested answer requires it.

---

<a id="translate-the-linear-equations"></a>
## Translate the Linear Equations

The constant-acceleration equations keep their structure when linear variables are replaced by angular variables:

$$
x\leftrightarrow\theta,\qquad
v\leftrightarrow\omega,\qquad
a\leftrightarrow\alpha.
$$

For changes over an interval, use \(\Delta x\leftrightarrow\Delta\theta\).

**Source-video example:** Translate the linear equation \(v_f=v_i+at\) into its rotational form.

**Explanation**

Replace each linear velocity \(v\) with angular velocity \(\omega\), and replace linear acceleration \(a\) with angular acceleration \(\alpha\). Time does not change:

$$
\omega_f=\omega_i+\alpha t.
$$

Like its linear counterpart, this equation requires constant acceleration over the interval.

```quiz
type: radio
id: mct-p5a-q1
content: |-
  Which rotational equation has the same structure as
  \(\Delta x=v_i t+\frac12at^2\)?
options:
- id: mct-p5a-q1-a
  content: |-
    \(\Delta\theta=\omega_i t+\frac12\alpha t^2\)
  correct: true
  feedback: |-
    Preserve the constant-acceleration structure while replacing \(\Delta x\) with \(\Delta\theta\), \(v_i\) with \(\omega_i\), and \(a\) with \(\alpha\). This gives \(\Delta\theta=\omega_i t+\frac12\alpha t^2\).
- id: mct-p5a-q1-b
  content: |-
    \(\Delta\theta=\omega_f t+\frac12\alpha t^2\)
  feedback: |-
    This changes the initial velocity term into a final velocity term. Direct translation preserves the subscript, so \(v_i t\) becomes \(\omega_i t\), not \(\omega_f t\).
- id: mct-p5a-q1-c
  content: |-
    \(\omega_f=\omega_i+\frac12\alpha t^2\)
  feedback: |-
    This mixes a displacement term with an angular-velocity target. The factor \(\frac12\alpha t^2\) belongs in the displacement equation; the final-velocity equation uses \(\alpha t\).
- id: mct-p5a-q1-d
  content: |-
    \(\Delta\theta=\omega_i t+\alpha t^2\)
  feedback: |-
    The variable replacements are right, but the constant-acceleration displacement contribution retains its factor of \(\frac12\). Dropping it doubles that contribution.
- id: mct-p5a-q1-e
  content: |-
    \(\Delta\theta=\omega_i t+\frac12\alpha t\)
  feedback: |-
    The acceleration contribution must contain \(t^2\) so its units become radians: \((\mathrm{rad/s^2})(\mathrm{s^2})\). Using only \(t\) leaves angular-velocity units.
```

---

<a id="find-final-angular-velocity"></a>
## Find Final Angular Velocity

When \(\omega_i\), \(\alpha\), and \(t\) are known and \(\omega_f\) is requested, use

$$
\omega_f=\omega_i+\alpha t.
$$

**Source-video example:** A disk starts from rest and speeds up at a constant \(2.5\,\mathrm{rad/s^2}\) for \(18\,\mathrm{s}\). Find its final angular velocity.

**Explanation**

“Starts from rest” supplies \(\omega_i=0\). The known/target list is

$$
\omega_i=0,\qquad
\alpha=2.5\,\mathrm{rad/s^2},\qquad
t=18\,\mathrm{s},\qquad
\omega_f=\text{target}.
$$

Substitute these values:

$$
\begin{aligned}
\omega_f
&=\omega_i+\alpha t\\
&=0+(2.5\,\mathrm{rad/s^2})(18\,\mathrm{s})\\
&=45\,\mathrm{rad/s}.
\end{aligned}
$$

```quiz
type: radio
id: mct-p5a-q2
content: |-
  A turntable starts from rest and has constant angular acceleration \(1.8\,\mathrm{rad/s^2}\) for \(12\,\mathrm{s}\). What is its final angular velocity?
options:
- id: mct-p5a-q2-a
  content: |-
    \(21.6\,\mathrm{rad/s}\)
  correct: true
  feedback: |-
    Starting from rest means \(\omega_i=0\). Constant acceleration gives \(\omega_f=\omega_i+\alpha t=0+(1.8)(12)=21.6\,\mathrm{rad/s}\).
- id: mct-p5a-q2-b
  content: |-
    \(13.8\,\mathrm{rad/s}\)
  feedback: |-
    This adds the numerical values of \(\alpha\) and \(t\), but acceleration must act for the full time. Multiply \(\alpha t\), then add the initial angular velocity.
- id: mct-p5a-q2-c
  content: |-
    \(10.8\,\mathrm{rad/s}\)
  feedback: |-
    This inserts a factor of \(\frac12\) from the displacement equation. Final angular velocity changes by the full amount \(\alpha t\); the half factor does not appear in \(\omega_f=\omega_i+\alpha t\).
- id: mct-p5a-q2-d
  content: |-
    \(0.15\,\mathrm{rad/s}\)
  feedback: |-
    This divides acceleration by time. Angular acceleration is angular-velocity change per time, so the change accumulated over \(12\,\mathrm{s}\) is found by multiplying by time.
- id: mct-p5a-q2-e
  content: |-
    \(21.6\,\mathrm{rad/s^2}\)
  feedback: |-
    The numerical calculation is right, but the unit still names angular acceleration. Multiplying \(\mathrm{rad/s^2}\) by seconds leaves \(\mathrm{rad/s}\), the unit of angular velocity.
```

---

<a id="find-displacement-from-angular-acceleration"></a>
## Find Displacement From Angular Acceleration

When \(\omega_i\), \(\alpha\), and \(t\) are known and angular displacement is requested, choose

$$
\Delta\theta=\omega_i t+\frac12\alpha t^2.
$$

**Source-video example, continued:** For the disk that starts from rest with \(\alpha=2.5\,\mathrm{rad/s^2}\), how many revolutions does it complete during the \(18\,\mathrm{s}\) interval?

**Explanation**

Use the same givens, but change the target to \(\Delta\theta\):

$$
\begin{aligned}
\Delta\theta
&=\omega_i t+\frac12\alpha t^2\\
&=(0)(18)+\frac12(2.5)(18)^2\\
&=405\,\mathrm{rad}.
\end{aligned}
$$

Convert the radian result to revolutions:

$$
405\,\mathrm{rad}
\left(\frac{1\,\mathrm{rev}}{2\pi\,\mathrm{rad}}\right)
\approx64.46\,\mathrm{rev}.
$$

```quiz
type: radio
id: mct-p5a-q3
content: |-
  A rotor starts from rest and maintains \(\alpha=1.2\,\mathrm{rad/s^2}\) for \(10\,\mathrm{s}\). Approximately how many revolutions does it complete?
options:
- id: mct-p5a-q3-a
  content: |-
    \(9.55\,\mathrm{rev}\)
  correct: true
  feedback: |-
    Starting from rest removes the \(\omega_i t\) term. Thus \(\Delta\theta=\frac12(1.2)(10)^2=60\,\mathrm{rad}\), and \(60/(2\pi)\approx9.55\,\mathrm{rev}\).
- id: mct-p5a-q3-b
  content: |-
    \(60\,\mathrm{rev}\)
  feedback: |-
    The value \(60\) is the angular displacement in radians, not revolutions. Divide radians by \(2\pi\,\mathrm{rad/rev}\) to obtain the requested number of revolutions.
- id: mct-p5a-q3-c
  content: |-
    \(19.10\,\mathrm{rev}\)
  feedback: |-
    This omits the factor of \(\frac12\), producing \(120\,\mathrm{rad}\) before conversion. Constant-acceleration displacement from rest is \(\frac12\alpha t^2\), so the correct radian result is \(60\).
- id: mct-p5a-q3-d
  content: |-
    \(4.77\,\mathrm{rev}\)
  feedback: |-
    This divides the \(60\,\mathrm{rad}\) result by \(4\pi\), adding an extra factor of two. One revolution is \(2\pi\) radians, so use \(60/(2\pi)\).
- id: mct-p5a-q3-e
  content: |-
    \(0\,\mathrm{rev}\)
  feedback: |-
    Rest describes only the initial angular velocity. A nonzero angular acceleration immediately changes \(\omega\), so the rotor accumulates angular displacement during the interval.
```

---

<a id="use-endpoint-angular-velocities"></a>
## Use Endpoint Angular Velocities

With constant angular acceleration, angular velocity changes linearly in time. If both endpoint angular velocities and the time are known, their average is

$$
\omega_{\mathrm{avg}}=\frac{\omega_i+\omega_f}{2},
$$

so

$$
\Delta\theta=\frac{\omega_i+\omega_f}{2}t.
$$

This is also the area under the straight segment on an angular-velocity-versus-time graph. The region is a trapezoid whose parallel sides are \(\omega_i\) and \(\omega_f\), and whose width is \(t\). That geometric view explains why the endpoint values are added and divided by two before multiplying by time.

**Source-video example:** A disk with diameter \(60\,\mathrm{cm}\) increases its angular velocity from \(20\,\mathrm{rad/s}\) to \(40\,\mathrm{rad/s}\) in \(5\,\mathrm{s}\). How many revolutions does it turn through?

**Explanation**

The diameter is extra information for this angular question. The endpoint angular velocities and time are enough:

$$
\begin{aligned}
\Delta\theta
&=\frac{\omega_i+\omega_f}{2}t\\
&=\frac{20+40}{2}(5)\\
&=150\,\mathrm{rad}.
\end{aligned}
$$

Convert only the final angular displacement:

$$
150\,\mathrm{rad}
\left(\frac{1\,\mathrm{rev}}{2\pi\,\mathrm{rad}}\right)
\approx23.87\,\mathrm{rev}.
$$

The radius would matter for a tangential quantity, but it is not needed for \(\Delta\theta\).

The source video next uses the same endpoint data to find the disk's constant angular acceleration. Isolate \(\alpha\) in \(\omega_f=\omega_i+\alpha t\), then substitute:

$$
\begin{aligned}
\alpha
&=\frac{\omega_f-\omega_i}{t}\\
&=\frac{40-20}{5}\\
&=4\,\mathrm{rad/s^2}.
\end{aligned}
$$

The supplied diameter remains irrelevant because neither angular displacement nor angular acceleration requires a radius.

```quiz
type: radio
id: mct-p5a-q4
content: |-
  A flywheel's angular velocity increases uniformly from \(12\,\mathrm{rad/s}\) to \(28\,\mathrm{rad/s}\) during \(6\,\mathrm{s}\). What is its angular displacement?
options:
- id: mct-p5a-q4-a
  content: |-
    \(120\,\mathrm{rad}\)
  correct: true
  feedback: |-
    Constant angular acceleration makes the time-average velocity the mean of the endpoints: \(\omega_{\mathrm{avg}}=(12+28)/2=20\,\mathrm{rad/s}\). Therefore \(\Delta\theta=(20)(6)=120\,\mathrm{rad}\).
- id: mct-p5a-q4-b
  content: |-
    \(240\,\mathrm{rad}\)
  feedback: |-
    This multiplies the sum of the endpoint velocities by time without dividing by two. The sum must first be converted to the average angular velocity.
- id: mct-p5a-q4-c
  content: |-
    \(96\,\mathrm{rad}\)
  feedback: |-
    This uses the change \(28-12=16\,\mathrm{rad/s}\) as though it were the average angular velocity. The change helps find \(\alpha\); displacement here uses the mean \((12+28)/2\).
- id: mct-p5a-q4-d
  content: |-
    \(20\,\mathrm{rad}\)
  feedback: |-
    The value \(20\,\mathrm{rad/s}\) is the average angular velocity, not the displacement. Multiply that rate by the \(6\,\mathrm{s}\) interval to obtain radians.
- id: mct-p5a-q4-e
  content: |-
    \(2.67\,\mathrm{rad}\)
  feedback: |-
    The value \((28-12)/6\approx2.67\) is the angular acceleration in \(\mathrm{rad/s^2}\), not angular displacement. The requested displacement follows from average angular velocity times time.
```

```quiz
type: radio
id: mct-p5a-q4b
content: |-
  A pulley's angular velocity increases uniformly from \(14\,\mathrm{rad/s}\) to \(32\,\mathrm{rad/s}\) in \(6.0\,\mathrm{s}\). What is its angular acceleration?
options:
- id: mct-p5a-q4b-a
  content: |-
    \(3.0\,\mathrm{rad/s^2}\)
  correct: true
  feedback: |-
    Angular acceleration is angular-velocity change per time. Here \(\alpha=(32-14)/6.0=3.0\,\mathrm{rad/s^2}\).
- id: mct-p5a-q4b-b
  content: |-
    \(18\,\mathrm{rad/s^2}\)
  feedback: |-
    The value \(18\,\mathrm{rad/s}\) is the change in angular velocity, not the acceleration. Divide that change by the \(6.0\,\mathrm{s}\) interval to obtain change per time.
- id: mct-p5a-q4b-c
  content: |-
    \(7.67\,\mathrm{rad/s^2}\)
  feedback: |-
    This adds the endpoint velocities and divides by time. Angular acceleration uses the endpoint difference \(\omega_f-\omega_i\); adding endpoints is part of finding their average for displacement.
- id: mct-p5a-q4b-d
  content: |-
    \(23\,\mathrm{rad/s^2}\)
  feedback: |-
    The value \(23\,\mathrm{rad/s}\) is the mean of the endpoint angular velocities. It describes the interval's average angular velocity, while angular acceleration is \((32-14)/6.0\).
- id: mct-p5a-q4b-e
  content: |-
    \(-3.0\,\mathrm{rad/s^2}\)
  feedback: |-
    The angular velocity grows from \(14\) to \(32\,\mathrm{rad/s}\) in the chosen positive direction, so \(\omega_f-\omega_i\) is positive. A negative acceleration would describe a decrease in positive angular velocity.
```

---

<a id="keep-the-sign-when-rotation-slows"></a>
## Keep the Sign When Rotation Slows

Choose a positive direction before assigning signs. If \(\omega_i>0\) and the object slows without reversing, then \(\alpha<0\), but \(\Delta\theta\) can remain positive.

**Example:** A rotor has \(\omega_i=18\,\mathrm{rad/s}\) and constant \(\alpha=-2.0\,\mathrm{rad/s^2}\) for \(6.0\,\mathrm{s}\). Find its angular displacement.

**Explanation**

Keep the negative sign on \(\alpha\):

$$
\begin{aligned}
\Delta\theta
&=\omega_i t+\frac12\alpha t^2\\
&=(18)(6)+\frac12(-2.0)(6)^2\\
&=108-36\\
&=72\,\mathrm{rad}.
\end{aligned}
$$

As a direction check,

$$
\omega_f=\omega_i+\alpha t=18+(-2.0)(6)=6\,\mathrm{rad/s}.
$$

The rotor is still moving in the positive direction at the end, so a positive displacement is consistent.

```quiz
type: radio
id: mct-p5a-q5
content: |-
  A wheel has \(\omega_i=24\,\mathrm{rad/s}\) and constant \(\alpha=-3.0\,\mathrm{rad/s^2}\) for \(5.0\,\mathrm{s}\). What is its angular displacement?
options:
- id: mct-p5a-q5-a
  content: |-
    \(82.5\,\mathrm{rad}\)
  correct: true
  feedback: |-
    The negative acceleration reduces the positive displacement: \(\Delta\theta=(24)(5)+\frac12(-3.0)(5)^2=120-37.5=82.5\,\mathrm{rad}\).
- id: mct-p5a-q5-b
  content: |-
    \(157.5\,\mathrm{rad}\)
  feedback: |-
    This treats the negative angular acceleration as positive and adds \(37.5\,\mathrm{rad}\). Because \(\alpha\) opposes the positive rotation, its displacement contribution must be subtracted.
- id: mct-p5a-q5-c
  content: |-
    \(120\,\mathrm{rad}\)
  feedback: |-
    This uses only \(\omega_i t\), which would require zero angular acceleration. The wheel slows throughout the interval, so include \(\frac12\alpha t^2=-37.5\,\mathrm{rad}\).
- id: mct-p5a-q5-d
  content: |-
    \(45\,\mathrm{rad}\)
  feedback: |-
    The final angular velocity is \(24+(-3)(5)=9\,\mathrm{rad/s}\), but multiplying that final rate by the entire time assumes it was \(9\,\mathrm{rad/s}\) throughout. Use the constant-acceleration displacement equation instead.
- id: mct-p5a-q5-e
  content: |-
    \(-82.5\,\mathrm{rad}\)
  feedback: |-
    A negative \(\alpha\) means the positive angular velocity is decreasing; it does not by itself make the displacement negative. Here \(\omega_f=9\,\mathrm{rad/s}>0\), so the wheel rotates positively for the whole interval.
```

---

<a id="summary"></a>
## Summary

1. Confirm that \(\alpha\) is constant and choose a positive rotational direction.
2. Translate the words: “starts from rest” means \(\omega_i=0\), and “slows” means \(\alpha\) opposes \(\omega\).
3. List the known quantities and target from \(\omega_i,\omega_f,\alpha,t,\Delta\theta\).
4. Select the time-containing equation that reaches the target without adding an extra unknown.
5. Keep signs through the calculation, solve angular displacement in radians, and convert to revolutions only at the end.

The main traps are using a constant-\(\alpha\) equation when acceleration is not constant, borrowing the factor \(\frac12\) from the wrong equation, dropping the square on \(t\), averaging endpoint velocities without dividing by two, and treating a negative acceleration as automatically meaning negative displacement.

<!-- lesson-nav:start -->

---

```update-progress
```

[[212/Home|Home]]
[[212/0. Table of Contents/TOC|Table of Contents]]

---

<!-- lesson-nav:end -->
