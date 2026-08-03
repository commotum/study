# Extreme Doppler Frequencies from a Rotating Source

<!--
lesson-id: 212-M5-049
topic-code: MTH212.M5.49
-->

## Table of Contents

- [Introduction](#introduction)
- [Convert Rotation Rate to Source Speed](#convert-rotation-rate-to-source-speed)
- [Match Toward and Away Motion to the Signs](#match-toward-and-away-motion-to-the-signs)
- [Calculate the Two Extreme Frequencies](#calculate-the-two-extreme-frequencies)
- [Complete the Rotating-Whistle Problem](#complete-the-rotating-whistle-problem)
- [Summary](#summary)

## Prerequisites

- Convert revolutions per minute to revolutions per second.
- Use circumference $2\pi L$ to find tangential speed.
- Evaluate a fraction and round a frequency in hertz.

---

<a id="introduction"></a>
## Introduction

When a sound source moves in a circle and a stationary listener hears changing pitch, use this chain:

$$
\text{rotation rate}
\longrightarrow
\text{source speed}
\longrightarrow
\text{toward or away}
\longrightarrow
\text{Doppler frequency}.
$$

For a source at radius $L$ rotating with frequency $f_{\mathrm{rot}}$,

$$
v_s=2\pi Lf_{\mathrm{rot}}.
$$

For a stationary listener and a moving source,

$$
f'=f_0\frac{v}{v\mp v_s},
$$

where $f_0$ is the emitted frequency and $v$ is the speed of sound. Use the minus sign when the source moves toward the listener and the plus sign when it moves away. This model assumes $v_s<v$ and that the air is at rest.

---

<a id="convert-rotation-rate-to-source-speed"></a>
## Convert Rotation Rate to Source Speed

**Example:** A source moves on a circle of radius $0.80\ \mathrm{m}$ at $90\ \mathrm{rpm}$. Find its tangential speed.

**Explanation**

First convert the rotation rate:

$$
f_{\mathrm{rot}}
=90\ \frac{\mathrm{rev}}{\mathrm{min}}
\left(\frac{1\ \mathrm{min}}{60\ \mathrm{s}}\right)
=1.5\ \frac{\mathrm{rev}}{\mathrm{s}}
=1.5\ \mathrm{Hz}.
$$

The orbit radius is the string length $L$, so one revolution covers

$$
C=2\pi L.
$$

Speed is distance per time. Multiplying the distance per revolution by the revolutions per second makes the revolution units cancel:

$$
v_s
=2\pi Lf_{\mathrm{rot}}
=\left(\frac{2\pi(0.80\ \mathrm{m})}{1\ \mathrm{rev}}\right)
\left(1.5\ \frac{\mathrm{rev}}{\mathrm{s}}\right)
=7.54\ \mathrm{m/s}.
$$

```quiz
type: radio
id: pq3-p5-source-speed
content: |-
  A sound source moves on a circle of radius $0.50\ \mathrm{m}$ at $180\ \mathrm{rpm}$. What is its tangential speed?
options:
- id: pq3-p5-source-speed-a
  content: |-
    $1.5\ \mathrm{m/s}$
  feedback: |-
    This treats the radius $L$ as the distance traveled per revolution. One revolution covers the full circumference $2\pi L$, so omitting $2\pi$ gives too small a speed; the correct value is $9.4\ \mathrm{m/s}$.
- id: pq3-p5-source-speed-b
  content: |-
    $3.0\ \mathrm{m/s}$
  feedback: |-
    This is the rotation rate $180/60=3.0\ \mathrm{rev/s}$, not a tangential speed. Multiplying by the circumference $2\pi(0.50\ \mathrm{m})$ converts revolutions per second to $9.4\ \mathrm{m/s}$.
- id: pq3-p5-source-speed-c
  content: |-
    $9.4\ \mathrm{m/s}$
  correct: true
  feedback: |-
    Tangential speed is circumference traveled per revolution times revolutions per second. Since $180\ \mathrm{rpm}=3.0\ \mathrm{Hz}$, $v_s=2\pi(0.50\ \mathrm{m})(3.0\ \mathrm{s^{-1}})=9.4\ \mathrm{m/s}$.
- id: pq3-p5-source-speed-d
  content: |-
    $19\ \mathrm{m/s}$
  feedback: |-
    This doubles the radius that was already given. In $v_s=2\pi rf_{\mathrm{rot}}$, $0.50\ \mathrm m$ is already $r$, so use it directly: $v_s=2\pi(0.50)(3.0)=9.4\ \mathrm{m/s}$.
- id: pq3-p5-source-speed-e
  content: |-
    $570\ \mathrm{m/s}$
  feedback: |-
    This treats $180\ \mathrm{rev/min}$ as $180\ \mathrm{rev/s}$ and makes the speed $60$ times too large. Convert first: $180\ \mathrm{rpm}=3.0\ \mathrm{Hz}$, then obtain $v_s=9.4\ \mathrm{m/s}$.
```

---

<a id="match-toward-and-away-motion-to-the-signs"></a>
## Match Toward and Away Motion to the Signs

**Example:** A rotating source reaches one instant when its velocity points directly toward a stationary listener and another when its velocity points directly away. Decide which instant produces the highest frequency.

**Explanation**

The source moving toward the listener compresses the wavefronts. Its denominator is $v-v_s$, which is smaller than $v$, so the observed frequency is greater than $f_0$.

The source moving away spreads the wavefronts. Its denominator is $v+v_s$, which is larger than $v$, so the observed frequency is less than $f_0$.

![](<../Source/PQ3/Images/rotating-whistle-doppler-wavefronts.png>)

Thus,

$$
f_{\mathrm{high}}=f_0\frac{v}{v-v_s},
\qquad
f_{\mathrm{low}}=f_0\frac{v}{v+v_s}.
$$

```quiz
type: radio
id: pq3-p5-sign-choice
content: |-
  Which pair correctly gives the highest and lowest frequencies heard by a stationary listener from a moving source of speed $v_s$?
options:
- id: pq3-p5-sign-choice-a
  content: |-
    $f_{\mathrm{high}}=f_0\dfrac{v+v_s}{v}$ and $f_{\mathrm{low}}=f_0\dfrac{v-v_s}{v}$
  feedback: |-
    This uses the moving-observer structure. A moving source changes the spacing between emitted wavefronts, so $v_s$ belongs in the denominator: $v-v_s$ for the compressed, high-frequency side and $v+v_s$ for the stretched, low-frequency side.
- id: pq3-p5-sign-choice-b
  content: |-
    $f_{\mathrm{high}}=f_0\dfrac{v}{v+v_s}$ and $f_{\mathrm{low}}=f_0\dfrac{v}{v-v_s}$
  feedback: |-
    This swaps the two source directions. Toward motion compresses wavefront spacing, so the high frequency uses the smaller denominator $v-v_s$; away motion uses the larger $v+v_s$.
- id: pq3-p5-sign-choice-c
  content: |-
    $f_{\mathrm{high}}=f_0\dfrac{v}{v-v_s}$ and $f_{\mathrm{low}}=f_0\dfrac{v}{v+v_s}$
  correct: true
  feedback: |-
    Toward motion compresses the wavefronts, so the smaller denominator $v-v_s$ raises the observed frequency. Away motion spreads them out, so the larger denominator $v+v_s$ lowers it.
- id: pq3-p5-sign-choice-d
  content: |-
    $f_{\mathrm{high}}=f_0\dfrac{v}{v-v_s}$ and $f_{\mathrm{low}}=f_0\dfrac{v}{v-v_s}$
  feedback: |-
    This uses compressed wavefront spacing at both extremes. At the away point the source stretches the spacing, so the low-frequency denominator must switch to $v+v_s$.
- id: pq3-p5-sign-choice-e
  content: |-
    $f_{\mathrm{high}}=f_{\mathrm{low}}=f_0$
  feedback: |-
    Equality with $f_0$ occurs when the source has no radial velocity relative to the listener. At the toward and away points its radial speed has maximum magnitude, so the wavefronts are compressed or stretched and the two frequencies differ from $f_0$.
```

---

<a id="calculate-the-two-extreme-frequencies"></a>
## Calculate the Two Extreme Frequencies

**Example:** A source emits $680\ \mathrm{Hz}$ and moves at $20\ \mathrm{m/s}$. Use $340\ \mathrm{m/s}$ for the speed of sound. Find the highest and lowest frequencies heard by a stationary listener.

**Explanation**

Evaluate the two denominators first:

$$
v-v_s=340-20=320\ \mathrm{m/s},
\qquad
v+v_s=340+20=360\ \mathrm{m/s}.
$$

Then apply the two source-motion formulas:

$$
f_{\mathrm{high}}
=680\frac{340}{340-20}
=722.5\ \mathrm{Hz},
$$

$$
f_{\mathrm{low}}
=680\frac{340}{340+20}
=642.2\ \mathrm{Hz}.
$$

The order check is

$$
f_{\mathrm{high}}>f_0>f_{\mathrm{low}}.
$$

```quiz
type: radio
id: pq3-p5-numerical-extremes
content: |-
  A source emits $500\ \mathrm{Hz}$ and moves at $14\ \mathrm{m/s}$. Using $350\ \mathrm{m/s}$ for the speed of sound, which pair gives the highest and lowest frequencies heard by a stationary listener, rounded to the nearest hertz?
options:
- id: pq3-p5-numerical-extremes-a
  content: |-
    $f_{\mathrm{high}}=481\ \mathrm{Hz}$ and $f_{\mathrm{low}}=521\ \mathrm{Hz}$
  feedback: |-
    The numerical values are reversed. Toward motion compresses wavefronts and must give the value above $500\ \mathrm{Hz}$, $521\ \mathrm{Hz}$; away motion gives the value below it, $481\ \mathrm{Hz}$.
- id: pq3-p5-numerical-extremes-b
  content: |-
    $f_{\mathrm{high}}=500\ \mathrm{Hz}$ and $f_{\mathrm{low}}=500\ \mathrm{Hz}$
  feedback: |-
    This assumes zero radial source speed at both extremes. At the toward and away points, the moving source produces one frequency above and one below $500\ \mathrm{Hz}$: $521\ \mathrm{Hz}$ and $481\ \mathrm{Hz}$.
- id: pq3-p5-numerical-extremes-c
  content: |-
    $f_{\mathrm{high}}=520\ \mathrm{Hz}$ and $f_{\mathrm{low}}=480\ \mathrm{Hz}$
  feedback: |-
    These are truncated rather than rounded to the nearest hertz. The unrounded extremes are $520.8\ldots\ \mathrm{Hz}$ and $480.8\ldots\ \mathrm{Hz}$, so both ones digits round up to $521\ \mathrm{Hz}$ and $481\ \mathrm{Hz}$.
- id: pq3-p5-numerical-extremes-d
  content: |-
    $f_{\mathrm{high}}=521\ \mathrm{Hz}$ and $f_{\mathrm{low}}=481\ \mathrm{Hz}$
  correct: true
  feedback: |-
    Toward motion uses $v-v_s$ and must raise the frequency; away motion uses $v+v_s$ and must lower it. The results are $500(350)/(350-14)=520.8\ldots\ \mathrm{Hz}$ and $500(350)/(350+14)=480.8\ldots\ \mathrm{Hz}$, which round to $521\ \mathrm{Hz}$ and $481\ \mathrm{Hz}$.
- id: pq3-p5-numerical-extremes-e
  content: |-
    $f_{\mathrm{high}}=514\ \mathrm{Hz}$ and $f_{\mathrm{low}}=486\ \mathrm{Hz}$
  feedback: |-
    This adds and subtracts $14\ \mathrm{m/s}$ directly from $500\ \mathrm{Hz}$, combining unlike units. Source speed must instead modify the wavefront-spacing denominator, yielding $521\ \mathrm{Hz}$ and $481\ \mathrm{Hz}$.
```

---

<a id="complete-the-rotating-whistle-problem"></a>
## Complete the Rotating-Whistle Problem

**Example:** Giorgio swings a whistle on a $1.2\ \mathrm{m}$ string in a horizontal circle at $120\ \mathrm{rpm}$. The whistle emits a $740\ \mathrm{Hz}$ sound when at rest. Using $343\ \mathrm{m/s}$ for the speed of sound, find the highest and lowest Doppler-shifted frequencies heard by a stationary bystander.

![](<../Source/PQ3/Images/rotating-whistle-path.png>)

**Explanation**

Convert the rotation rate and find the source speed:

$$
f_{\mathrm{rot}}=\frac{120}{60}=2.0\ \mathrm{Hz},
\qquad
v_s=2\pi(1.2)(2.0)=15.08\ldots\ \mathrm{m/s}.
$$

Then

$$
f_{\mathrm{high}}
=740\frac{343}{343-15.08\ldots}
=774.0\ldots\ \mathrm{Hz},
$$

$$
f_{\mathrm{low}}
=740\frac{343}{343+15.08\ldots}
=709.0\ldots\ \mathrm{Hz}.
$$

```quiz
type: radio
id: pq3-p5-original-check
content: |-
  Giorgio swings a whistle on a $1.2\ \mathrm{m}$ string in a horizontal circle at $120\ \mathrm{rpm}$. The whistle emits a $740\ \mathrm{Hz}$ sound when at rest. Using $343\ \mathrm{m/s}$ for the speed of sound, find the highest and lowest Doppler-shifted frequencies heard by a stationary bystander.

  Which pair gives the highest frequency followed by the lowest frequency, rounded to the nearest hertz?
options:
- id: pq3-p5-original-check-a
  content: |-
    $774\ \mathrm{Hz},\ 709\ \mathrm{Hz}$
  correct: true
  feedback: |-
    The rotation rate gives the source speed: $120\ \mathrm{rpm}=2.0\ \mathrm{Hz}$ and $v_s=2\pi(1.2)(2.0)=15.08\ldots\ \mathrm{m/s}$. Compressed wavefronts use $v-v_s$ and stretched wavefronts use $v+v_s$, giving $774\ \mathrm{Hz}$ and $709\ \mathrm{Hz}$.
- id: pq3-p5-original-check-b
  content: |-
    $709\ \mathrm{Hz},\ 774\ \mathrm{Hz}$
  feedback: |-
    This lists the extremes in reverse order. Toward motion compresses wavefronts and produces the larger $774\ \mathrm{Hz}$ value; away motion produces $709\ \mathrm{Hz}$.
- id: pq3-p5-original-check-c
  content: |-
    $740\ \mathrm{Hz},\ 740\ \mathrm{Hz}$
  feedback: |-
    This treats the source as radially stationary at both extremes. Its $15.08\ldots\ \mathrm{m/s}$ tangential speed points toward or away at the extreme-pitch points, shifting the frequencies to $774\ \mathrm{Hz}$ and $709\ \mathrm{Hz}$.
- id: pq3-p5-original-check-d
  content: |-
    $745\ \mathrm{Hz},\ 735\ \mathrm{Hz}$
  feedback: |-
    This uses $Lf_{\mathrm{rot}}$ as the source speed and omits the distance $2\pi L$ traveled each revolution. Including the circumference gives $v_s=15.08\ldots\ \mathrm{m/s}$ and the wider pair $774\ \mathrm{Hz},\ 709\ \mathrm{Hz}$.
- id: pq3-p5-original-check-e
  content: |-
    $773\ \mathrm{Hz},\ 707\ \mathrm{Hz}$
  feedback: |-
    This uses the moving-observer numerator structure. Here the source moves, changing wavefront spacing through the denominators $v-v_s$ and $v+v_s$; those give $774\ \mathrm{Hz}$ and $709\ \mathrm{Hz}$.
```

---

<a id="summary"></a>
## Summary

For a rotating sound source and a stationary listener:

1. Convert rpm to hertz: $f_{\mathrm{rot}}=\mathrm{rpm}/60$.
2. Find source speed: $v_s=2\pi Lf_{\mathrm{rot}}$.
3. Use toward motion for the highest frequency: $f_{\mathrm{high}}=f_0v/(v-v_s)$.
4. Use away motion for the lowest frequency: $f_{\mathrm{low}}=f_0v/(v+v_s)$.
5. Check that $f_{\mathrm{high}}>f_0>f_{\mathrm{low}}$.

The main traps are treating rpm as hertz, omitting $2\pi$, and swapping the Doppler signs.

<!-- lesson-nav:start -->
---

```update-progress
```

[[212/Home|Home]]
[[212/0. Table of Contents/TOC|Table of Contents]]

[Quiz 3 Study Guide](../../2026-08-03-Q-3/Study-Guide.md)
Next: [Largest Displacement When Two Pulses Overlap](../../2026-07-30-M5-5/Lessons/Problem-1.md)

Study guide index: 20/28

---
<!-- lesson-nav:end -->
