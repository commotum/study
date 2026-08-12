# Connecting Angular and Linear Motion at a Radius

<!--
lesson-id: 212-M1-076
topic-code: M1.76
-->

## Table of Contents

- [Introduction](#introduction)
- [Turn Radians Into Arc Length](#turn-radians-into-arc-length)
- [Turn Angular Speed Into Tangential Speed](#turn-angular-speed-into-tangential-speed)
- [Work Backward From Tangential Speed](#work-backward-from-tangential-speed)
- [Prepare Diameter and Centimeter Data](#prepare-diameter-and-centimeter-data)
- [Compare Points on One Rigid Body](#compare-points-on-one-rigid-body)
- [Summary](#summary)

## Prerequisites

- Multiply and divide decimal numbers.
- Rearrange a one-step multiplication equation.
- Use \(d=2r\) and \(100\,\mathrm{cm}=1\,\mathrm{m}\).

---

<a id="introduction"></a>
## Introduction

For a point at radius \(r\), first identify whether the problem gives an **angular amount** or an **angular rate**:

- angle \(\theta\) and arc length \(s\): use \(s=r\theta\);
- angular speed \(\omega\) and tangential speed \(v\): use \(v=r\omega\).

The angle in \(s=r\theta\) must be measured in radians. For SI calculations, measure the radius in meters. Because a radian is dimensionless, multiplying \(r\) by radians gives a length, and multiplying \(r\) by radians per second gives a length per second. Writing \(r\) as a temporary “meters per radian” conversion factor can help track cancellation, but that is not an intrinsic unit of radius.

First name the requested linear or angular quantity. Then prepare the radius and angle units, choose the bridge containing the target, and check the final unit.

---

<a id="turn-radians-into-arc-length"></a>
## Turn Radians Into Arc Length

The radian measure of a central angle is defined by

$$
\theta=\frac{s}{r}.
$$

Solving this definition for the arc length gives

$$
s=r\theta.
$$

**Source-video example:** During a five-minute interval, a wheel of radius \(2\,\mathrm{m}\) accumulates an angular displacement of \(7200\,\mathrm{rad}\). If it rolls without slipping, how far does it travel along the ground?

**Explanation**

The problem asks for linear distance and supplies angular displacement, so use \(s=r\theta\). For rolling without slipping, the distance along the ground equals the arc length unrolled by the rim. The angular displacement is already in radians, so substitute it with the radius:

$$
s=(2\,\mathrm{m})(7200)=14{,}400\,\mathrm{m}.
$$

The wheel travels \(14{,}400\,\mathrm{m}\) along the ground. Without the no-slip condition, \(r\theta\) still gives the rim arc length but need not equal the wheel's ground displacement. If an angle is supplied in degrees or revolutions, convert it to radians before using this equation.

```quiz
type: radio
id: mct-p2-q1
content: |-
  A point is \(0.45\,\mathrm{m}\) from an axis and sweeps through \(1.6\,\mathrm{rad}\). What arc length does it travel?
options:
- id: mct-p2-q1-a
  content: |-
    \(0.72\,\mathrm{m}\)
  correct: true
  feedback: |-
    Radian measure satisfies \(\theta=s/r\), so the arc length is \(s=r\theta=(0.45\,\mathrm{m})(1.6)=0.72\,\mathrm{m}\).
- id: mct-p2-q1-b
  content: |-
    \(3.56\,\mathrm{m}\)
  feedback: |-
    This comes from dividing \(\theta\) by \(r\). Solving \(\theta=s/r\) for the requested arc length requires multiplication, not division: \(s=r\theta\).
- id: mct-p2-q1-c
  content: |-
    \(0.281\,\mathrm{m}\)
  feedback: |-
    This reverses the ratio and calculates \(r/\theta\). A larger swept angle at fixed radius must produce a longer arc, so multiply \(0.45\) by \(1.6\).
- id: mct-p2-q1-d
  content: |-
    \(2.05\,\mathrm{m}\)
  feedback: |-
    This adds the numerical values of radius and angle. Radius and angle play different roles and cannot be added; the radian definition connects them by \(s=r\theta\).
- id: mct-p2-q1-e
  content: |-
    \(0.45\,\mathrm{m}\)
  feedback: |-
    An arc length equals the radius only when the swept angle is exactly \(1\,\mathrm{rad}\). Here \(\theta=1.6\,\mathrm{rad}\), so the arc is \(1.6\) times the radius.
```

---

<a id="turn-angular-speed-into-tangential-speed"></a>
## Turn Angular Speed Into Tangential Speed

For a point at fixed radius, divide \(s=r\theta\) by the same elapsed time:

$$
\frac{s}{\Delta t}=r\frac{\theta}{\Delta t}.
$$

The two rates are \(v=s/\Delta t\) and \(\omega=\theta/\Delta t\), so

$$
v=r\omega.
$$

**Source-video example:** A wheel has radius \(30\,\mathrm{cm}\) and rotates at \(25\,\mathrm{rad/s}\). Find the tangential speed at its rim.

**Explanation**

Use the angular-rate-to-linear-rate bridge \(v=r\omega\), but convert the radius to meters first:

$$
r=30\,\mathrm{cm}\left(\frac{1\,\mathrm{m}}{100\,\mathrm{cm}}\right)=0.30\,\mathrm{m}.
$$

Then

$$
v=(0.30\,\mathrm{m})(25\,\mathrm{rad/s})=7.5\,\mathrm{m/s}.
$$

The answer is tangential speed, so its unit is \(\mathrm{m/s}\), not \(\mathrm{rad/s}\). Because radians are dimensionless, the unit check reduces to meters per second; radius itself is still a length.

```quiz
type: radio
id: mct-p2-q2
content: |-
  A bead fixed \(0.24\,\mathrm{m}\) from a turntable's axis rotates with angular speed \(9.0\,\mathrm{rad/s}\). What is its tangential speed?
options:
- id: mct-p2-q2-a
  content: |-
    \(2.16\,\mathrm{m/s}\)
  correct: true
  feedback: |-
    Tangential speed is the angular rate scaled by radius: \(v=r\omega=(0.24\,\mathrm{m})(9.0\,\mathrm{rad/s})=2.16\,\mathrm{m/s}\).
- id: mct-p2-q2-b
  content: |-
    \(37.5\,\mathrm{m/s}\)
  feedback: |-
    This divides \(\omega\) by \(r\), which does not produce a linear-speed unit. The radius multiplies the common angular rate, so use \(v=r\omega\).
- id: mct-p2-q2-c
  content: |-
    \(0.0267\,\mathrm{m/s}\)
  feedback: |-
    This divides \(r\) by \(\omega\). That ratio is not distance traveled per time; each radian sweeps an arc proportional to \(r\), so multiply \(r\) and \(\omega\).
- id: mct-p2-q2-d
  content: |-
    \(9.24\,\mathrm{m/s}\)
  feedback: |-
    This adds \(r\) and \(\omega\), quantities with incompatible roles and units. The geometry supplies the product \(v=r\omega\), not a sum.
- id: mct-p2-q2-e
  content: |-
    \(2.16\,\mathrm{rad/s}\)
  feedback: |-
    The numerical product is right, but the unit names the wrong quantity. Angular speed is measured in \(\mathrm{rad/s}\); the requested tangential speed is \(2.16\,\mathrm{m/s}\).
```

---

<a id="work-backward-from-tangential-speed"></a>
## Work Backward From Tangential Speed

The same relationship can be rearranged to recover either missing input:

$$
\omega=\frac{v}{r},
\qquad
r=\frac{v}{\omega}.
$$

Choose the form whose left side is the requested quantity.

**Example:** The rim of a grinding wheel moves at \(6.3\,\mathrm{m/s}\) and is \(0.35\,\mathrm{m}\) from the axis. What is the wheel's angular speed?

**Explanation**

Angular speed is requested, so divide the tangential speed by the radius:

$$
\omega=\frac{v}{r}
=\frac{6.3\,\mathrm{m/s}}{0.35\,\mathrm{m}}
=18\,\mathrm{rad/s}.
$$

The length units cancel, leaving an inverse-second rate conventionally reported as radians per second.

```quiz
type: radio
id: mct-p2-q3
content: |-
  A point has tangential speed \(5.6\,\mathrm{m/s}\) while rotating at \(14\,\mathrm{rad/s}\). How far is it from the axis?
options:
- id: mct-p2-q3-a
  content: |-
    \(0.40\,\mathrm{m}\)
  correct: true
  feedback: |-
    Radius is the missing factor in \(v=r\omega\), so \(r=v/\omega=(5.6\,\mathrm{m/s})/(14\,\mathrm{rad/s})=0.40\,\mathrm{m}\).
- id: mct-p2-q3-b
  content: |-
    \(78.4\,\mathrm{m}\)
  feedback: |-
    This multiplies \(v\) and \(\omega\). Because \(v\) is already the product \(r\omega\), isolate the radius by dividing \(v\) by \(\omega\).
- id: mct-p2-q3-c
  content: |-
    \(2.5\,\mathrm{m}\)
  feedback: |-
    This calculates the reciprocal ratio \(\omega/v\). The equation \(v=r\omega\) requires \(r=v/\omega\), and its units reduce to meters.
- id: mct-p2-q3-d
  content: |-
    \(19.6\,\mathrm{m}\)
  feedback: |-
    This adds a linear speed to an angular speed, which cannot produce a radius. Rearrange the product relationship before inserting the values.
- id: mct-p2-q3-e
  content: |-
    \(0.0286\,\mathrm{m}\)
  feedback: |-
    This divides by \(\omega\) twice. Only one angular-speed factor appears in \(v=r\omega\), so a single division gives \(r=0.40\,\mathrm{m}\).
```

---

<a id="prepare-diameter-and-centimeter-data"></a>
## Prepare Diameter and Centimeter Data

The \(r\) in either bridge equation is the **radius**, not the diameter. For an SI speed calculation, prepare the geometry first:

$$
r=\frac{d}{2},
\qquad
r(\mathrm{m})=\frac{r(\mathrm{cm})}{100}.
$$

**Source-video example:** A disk has diameter \(20\,\mathrm{cm}\) and angular speed \(8.33\,\mathrm{rad/s}\). Find the tangential speed at its rim.

**Explanation**

First convert diameter to radius, then centimeters to meters:

$$
r=\frac{20\,\mathrm{cm}}{2}=10\,\mathrm{cm},
\qquad
10\,\mathrm{cm}\left(\frac{1\,\mathrm{m}}{100\,\mathrm{cm}}\right)=0.10\,\mathrm{m}.
$$

Now substitute the prepared radius:

$$
v=r\omega=(0.10\,\mathrm{m})(8.33\,\mathrm{rad/s})
=0.833\,\mathrm{m/s}.
$$

The units reduce to \(\mathrm{m/s}\), as required for tangential speed.

```quiz
type: radio
id: mct-p2-q4
content: |-
  A rotor has diameter \(64\,\mathrm{cm}\) and angular speed \(7.5\,\mathrm{rad/s}\). What is the tangential speed of a point on its rim?
options:
- id: mct-p2-q4-a
  content: |-
    \(2.40\,\mathrm{m/s}\)
  correct: true
  feedback: |-
    The radius is half the diameter: \(r=32\,\mathrm{cm}=0.32\,\mathrm{m}\). Therefore \(v=r\omega=(0.32)(7.5)=2.40\,\mathrm{m/s}\).
- id: mct-p2-q4-b
  content: |-
    \(4.80\,\mathrm{m/s}\)
  feedback: |-
    This uses the \(64\,\mathrm{cm}\) diameter as though it were the radius. The rim is \(32\,\mathrm{cm}=0.32\,\mathrm{m}\) from the axis, so the correct product is half as large.
- id: mct-p2-q4-c
  content: |-
    \(240\,\mathrm{m/s}\)
  feedback: |-
    This treats \(32\,\mathrm{cm}\) as \(32\,\mathrm{m}\). Convert centimeters to meters by dividing by \(100\) before multiplying by \(\omega\).
- id: mct-p2-q4-d
  content: |-
    \(0.024\,\mathrm{m/s}\)
  feedback: |-
    This converts \(32\,\mathrm{cm}\) as though \(1000\,\mathrm{cm}=1\,\mathrm{m}\). Since \(100\,\mathrm{cm}=1\,\mathrm{m}\), the radius is \(0.32\,\mathrm{m}\), not \(0.0032\,\mathrm{m}\).
- id: mct-p2-q4-e
  content: |-
    \(1.20\,\mathrm{m/s}\)
  feedback: |-
    This halves the given diameter twice. Halve \(64\,\mathrm{cm}\) once to obtain the radius \(32\,\mathrm{cm}\), then use that full radius in \(v=r\omega\).
```

---

<a id="compare-points-on-one-rigid-body"></a>
## Compare Points on One Rigid Body

Points fixed to the same rigid rotating body sweep the same angle in the same time. Therefore, they share one angular speed \(\omega\). Their tangential speeds differ because

$$
v=r\omega.
$$

At fixed \(\omega\), tangential speed varies directly with radius:

$$
\frac{v_B}{v_A}=\frac{r_B}{r_A}.
$$

**Source-video example:** Points \(A\) and \(B\) are fixed to one rigid wheel rotating at \(5\,\mathrm{rad/s}\). Point \(B\) is farther from the axis. Compare their angular and tangential speeds.

**Explanation**

Both points complete each turn together, so

$$
\omega_A=\omega_B=5\,\mathrm{rad/s}.
$$

Point \(B\) must cover a longer arc in the same time. Since \(v=r\omega\), the shared \(\omega\) makes the point at the larger radius faster, so \(v_B>v_A\). If the radius ratio were known, the same ratio would give the tangential-speed ratio.

```quiz
type: radio
id: mct-p2-q5
content: |-
  Points \(P\) and \(Q\) are fixed to the same rigid disk at radii \(r_P=0.15\,\mathrm{m}\) and \(r_Q=0.45\,\mathrm{m}\). Which comparison is correct?
options:
- id: mct-p2-q5-a
  content: |-
    \(\omega_P=\omega_Q\) and \(v_Q=3v_P\)
  correct: true
  feedback: |-
    A rigid disk gives both points the same angular speed. Since \(r_Q/r_P=0.45/0.15=3\) and \(v=r\omega\), the outer point has \(v_Q=3v_P\).
- id: mct-p2-q5-b
  content: |-
    \(\omega_Q=3\omega_P\) and \(v_Q=v_P\)
  feedback: |-
    This assigns the radius factor to angular speed. Fixed points on one rigid disk sweep the same angle per time, so their \(\omega\) values are equal; radius instead scales tangential speed.
- id: mct-p2-q5-c
  content: |-
    \(\omega_P=\omega_Q\) and \(v_P=v_Q\)
  feedback: |-
    The equal-angular-speed part is correct, but equal \(\omega\) does not mean equal tangential speed. Point \(Q\) traces a circle three times as large in radius during the same time, so it moves three times as fast.
- id: mct-p2-q5-d
  content: |-
    \(\omega_P=3\omega_Q\) and \(v_P=3v_Q\)
  feedback: |-
    This reverses both comparisons. The rigid body fixes \(\omega_P=\omega_Q\), and the larger radius belongs to \(Q\), so \(Q\), not \(P\), has the larger tangential speed.
- id: mct-p2-q5-e
  content: |-
    \(\omega_P=\omega_Q\) and \(v_P=3v_Q\)
  feedback: |-
    The points do share angular speed, but the speed ratio is reversed. With \(v\) directly proportional to \(r\), the point at \(0.45\,\mathrm{m}\) moves three times as fast as the point at \(0.15\,\mathrm{m}\).
```

---

<a id="summary"></a>
## Summary

- If the prompt connects an angle to an arc length, convert the angle to radians and use \(s=r\theta\).
- If it connects angular speed to tangential speed, use \(v=r\omega\), rearranging only after naming the target.
- Prepare the radius before substitution: halve a diameter once and convert centimeters to meters for an SI result.
- On one rigid rotating body, every fixed point has the same \(\omega\), while \(s\) and \(v\) increase in direct proportion to \(r\).
- Check the result's kind and units: \(s\) is a length and \(v\) is a length per time. Radius itself remains a length; “length per radian” is only optional unit bookkeeping.

<!-- lesson-nav:start -->

---

```update-progress
```

[[212/Home|Home]]
[[212/0. Table of Contents/TOC|Table of Contents]]

---

<!-- lesson-nav:end -->
