# Read a Wave Graph Before Using $v=f\lambda$

<!--
lesson-id: 212-M5-065
topic-code: MTH212.M5.65
-->

## Table of Contents

- [Introduction](#introduction)
- [Source-Video Worked Problem: Read a Spatial Graph](#source-spatial-graph)
- [Source-Video Worked Problem: Read a Time Graph](#source-time-graph)
- [Source-Video Worked Problem: Read an Offset Time Graph](#source-offset-graph)
- [Source-Video Worked Problem: Use the Wave-Speed Relation](#source-wave-speed)
- [Source-Video Worked Problem: Combine Crest Timing and Spacing](#source-crest-data)
- [Lecture Recognition Aid: Snapshot or Particle History?](#lecture-two-views)
- [Summary](#summary)

## Prerequisites

- Identify crests, troughs, and the equilibrium line on a periodic graph.
- Recognize one complete cycle between equivalent neighboring points.
- Use frequency as cycles per second and period as seconds per cycle.
- Rearrange a one-step equation and track units.

---

<a id="introduction"></a>
## Introduction

Before reading a horizontal interval from a wave graph, inspect the horizontal axis:

| Graph | What it holds fixed | Meaning of one horizontal cycle |
|---|---|---|
| $y$ versus position $x$ | one instant in time | one wavelength $\lambda$ |
| $y$ versus time $t$ | one position in the medium | one period $T$ |

A spatial snapshot answers, “How far apart are repeated features?” A time history answers, “How long apart are repeated events?” The curves may have the same sinusoidal shape, so the axis label and units—not the shape—decide what the interval means.

For a graph whose highest and lowest values are $y_{\max}$ and $y_{\min}$,

$$
y_{\text{mid}}=\frac{y_{\max}+y_{\min}}{2},
\qquad
A=\frac{y_{\max}-y_{\min}}{2}.
$$

If $N$ complete cycles occupy a horizontal span, then

$$
\lambda=\frac{\Delta x}{N}
\quad\text{on a spatial graph},
\qquad
T=\frac{\Delta t}{N}
\quad\text{on a time graph}.
$$

Use same-phase landmarks to recognize a complete repeat:

| Horizontal interval | Cycle fraction |
|---|---:|
| crest to next crest | $1$ |
| trough to next trough | $1$ |
| crest to next trough | $\tfrac12$ |
| midline crossing to adjacent crest or trough | $\tfrac14$ |

Wavelength and period use the smallest positive full repeat. Two points can have the same displacement without being in the same phase, so matching height alone is not enough; the curve must also be moving through the pattern in the same direction.

Only after identifying a spatial scale and a time scale should you connect them:

$$
f=\frac1T,
\qquad
v=\frac{\lambda}{T}=f\lambda.
$$

Use this order:

1. Read the horizontal variable and its units.
2. Mark two same-phase points, such as crest to next crest, or count complete cycles over a longer span.
3. Convert the span into $\lambda$ if the axis is position or $T$ if the axis is time.
4. Find the midline and amplitude from the vertical extremes when requested.
5. Use $f=1/T$ and $v=f\lambda$ only after the graph quantities have been classified.

---

<a id="source-spatial-graph"></a>
## Source-Video Worked Problem: Read a Spatial Graph

The first graph in `qm1hDJrIYwE` at 0:00:00-0:01:18 is a wave displacement plotted against position. Its midline is $0$, its crests reach $+3\,\mathrm m$, and the graph contains three complete spatial cycles across $10\,\mathrm m$.

The amplitude is the vertical distance from the midline to a crest:

$$
A=3-0=\boxed{3\,\mathrm m}.
$$

Because the horizontal axis measures position, the repeated horizontal length is wavelength. Three wavelengths fit in $10\,\mathrm m$:

$$
3\lambda=10\,\mathrm m,
$$

so

$$
\lambda=\frac{10\,\mathrm m}{3}
=\boxed{3.33\,\mathrm m}.
$$

**Source wording correction.** The narration describes the wave as having “traveled” $10\,\mathrm m$. A snapshot does not provide an elapsed time, so the graph directly shows a $10\,\mathrm m$ spatial span containing three wavelengths. The numerical calculation is unchanged, but no propagation distance over time has been measured.

```quiz
type: radio
id: mct-p7-spatial-cycles
shuffle: true
content: |-
  A graph of displacement $y$ versus position $x$ has a midline at $0$, a high point of $+2.5\,\mathrm m$, and a low point of $-2.5\,\mathrm m$. Four complete cycles occupy the interval from $x=0$ to $x=12\,\mathrm m$. What are the amplitude and wavelength?
options:
- id: mct-p7-spatial-cycles-a
  content: |-
    $A=2.5\,\mathrm m$ and $\lambda=3.0\,\mathrm m$
  correct: true
  feedback: |-
    Amplitude is the crest-to-midline distance, so $A=2.5\,\mathrm m$. The horizontal axis is position, and four spatial cycles fit in $12\,\mathrm m$, so $\lambda=12/4=3.0\,\mathrm m$.
- id: mct-p7-spatial-cycles-b
  content: |-
    $A=5.0\,\mathrm m$ and $\lambda=3.0\,\mathrm m$
  feedback: |-
    The $5.0\,\mathrm m$ peak-to-trough span is twice the amplitude. Amplitude is half that span, while $\lambda=12/4=3.0\,\mathrm m$ comes from the spatial cycle count.
- id: mct-p7-spatial-cycles-c
  content: |-
    $A=2.5\,\mathrm m$ and $\lambda=48\,\mathrm m$
  feedback: |-
    Four cycles share the $12\,\mathrm m$ span; they do not each occupy the entire span four times. Divide the total distance by the number of complete cycles: $\lambda=12/4$.
- id: mct-p7-spatial-cycles-d
  content: |-
    $A=2.5\,\mathrm m$ and $T=3.0\,\mathrm s$
  feedback: |-
    The numerical division is right, but the horizontal axis is position in meters. A repeated horizontal interval on this graph is a wavelength in meters, not a period in seconds.
- id: mct-p7-spatial-cycles-e
  content: |-
    $A=0$ and $\lambda=4.0\,\mathrm m$
  feedback: |-
    A midline of zero locates equilibrium; it does not make the amplitude zero. Also, $4$ is the number of cycles, while wavelength is distance per cycle: $12/4=3.0\,\mathrm m$.
```

---

<a id="source-time-graph"></a>
## Source-Video Worked Problem: Read a Time Graph

The second graph in `qm1hDJrIYwE` at 0:01:19-0:02:31 plots displacement against time. The vertical distance from the midline to the crest is $10\,\mathrm m$, so

$$
A=\boxed{10\,\mathrm m}.
$$

On this graph, the first $5\,\mathrm s$ covers one quarter of a cycle. Scale that partial cycle to one complete cycle:

$$
\frac{T}{4}=5\,\mathrm s
\quad\Longrightarrow\quad
T=4(5\,\mathrm s)=\boxed{20\,\mathrm s}.
$$

Then

$$
f=\frac1T
=\frac1{20\,\mathrm s}
=\boxed{0.05\,\mathrm{Hz}}.
$$

The $5\,\mathrm s$ horizontal interval is not a wavelength: its unit is seconds. This time graph alone also does not supply $\lambda$ or wave speed.

```quiz
type: radio
id: mct-p7-quarter-cycle-time
shuffle: true
content: |-
  On a displacement-versus-time graph, a particle moves from a midline crossing to the next crest in $1.5\,\mathrm s$. This interval is one quarter of a cycle. What are the period and frequency?
options:
- id: mct-p7-quarter-cycle-time-a
  content: |-
    $T=6.0\,\mathrm s$ and $f=0.17\,\mathrm{Hz}$
  correct: true
  feedback: |-
    A midline-to-adjacent-crest interval is one quarter-cycle, so $T=4(1.5)=6.0\,\mathrm s$. Frequency is the reciprocal: $f=1/6.0\approx0.17\,\mathrm{Hz}$.
- id: mct-p7-quarter-cycle-time-b
  content: |-
    $T=1.5\,\mathrm s$ and $f=0.667\,\mathrm{Hz}$
  feedback: |-
    The $1.5\,\mathrm s$ interval covers only a quarter-cycle, not a full repeat. Multiply by four before taking the reciprocal.
- id: mct-p7-quarter-cycle-time-c
  content: |-
    $T=0.375\,\mathrm s$ and $f=2.67\,\mathrm{Hz}$
  feedback: |-
    Dividing $1.5\,\mathrm s$ by four makes a quarter-cycle shorter still. A complete cycle contains four such intervals, so the period is $4(1.5)=6.0\,\mathrm s$.
- id: mct-p7-quarter-cycle-time-d
  content: |-
    $T=6.0\,\mathrm s$ and $f=6.0\,\mathrm{Hz}$
  feedback: |-
    Period and frequency are reciprocals, not numerically identical in general. With $T=6.0\,\mathrm s$, the frequency is $1/(6.0\,\mathrm s)\approx0.17\,\mathrm{Hz}$.
- id: mct-p7-quarter-cycle-time-e
  content: |-
    $\lambda=6.0\,\mathrm m$ and $f=0.17\,\mathrm{Hz}$
  feedback: |-
    The frequency is correct, but the graph's horizontal axis is time. Scaling its quarter-cycle yields a period in seconds; no spatial distance is given from which to infer wavelength.
```

---

<a id="source-offset-graph"></a>
## Source-Video Worked Problem: Read an Offset Time Graph

The third graph in `qm1hDJrIYwE` at 0:02:33-0:04:30 has a high value of $12\,\mathrm m$ and a low value of $4\,\mathrm m$. Because the oscillation is vertically offset, neither $12\,\mathrm m$ nor $8\,\mathrm m$ is its amplitude.

First find the midline:

$$
y_{\text{mid}}
=\frac{12+4}{2}
=\boxed{8\,\mathrm m}.
$$

Then find the amplitude:

$$
A
=\frac{12-4}{2}
=\boxed{4\,\mathrm m}.
$$

The time graph covers three quarters of a cycle in $6\,\mathrm s$. Thus one quarter-cycle takes $2\,\mathrm s$, and a full cycle takes

$$
T=4(2\,\mathrm s)=\boxed{8\,\mathrm s}.
$$

Therefore,

$$
f=\frac1T
=\boxed{0.125\,\mathrm{Hz}}.
$$

```quiz
type: radio
id: mct-p7-offset-time-graph
shuffle: true
content: |-
  A displacement-versus-time graph has a high value of $17\,\mathrm{cm}$ and a low value of $5\,\mathrm{cm}$. The graph shows $1.25$ cycles during $7.5\,\mathrm s$. Which set of values is correct?
options:
- id: mct-p7-offset-time-graph-a
  content: |-
    Midline $11\,\mathrm{cm}$, amplitude $6\,\mathrm{cm}$, $T=6.0\,\mathrm s$, and $f=0.17\,\mathrm{Hz}$
  correct: true
  feedback: |-
    The midline is $(17+5)/2=11\,\mathrm{cm}$ and the amplitude is $(17-5)/2=6\,\mathrm{cm}$. On a time graph, $1.25$ cycles in $7.5\,\mathrm s$ gives $T=7.5/1.25=6.0\,\mathrm s$ and $f=1/T\approx0.17\,\mathrm{Hz}$.
- id: mct-p7-offset-time-graph-b
  content: |-
    Midline $11\,\mathrm{cm}$, amplitude $12\,\mathrm{cm}$, $T=6.0\,\mathrm s$, and $f=0.17\,\mathrm{Hz}$
  feedback: |-
    The $12\,\mathrm{cm}$ difference from low to high is the full peak-to-trough span. Amplitude is half that span, so $A=6\,\mathrm{cm}$.
- id: mct-p7-offset-time-graph-c
  content: |-
    Midline $6\,\mathrm{cm}$, amplitude $11\,\mathrm{cm}$, $T=6.0\,\mathrm s$, and $f=0.17\,\mathrm{Hz}$
  feedback: |-
    This swaps the vertical roles. The average of the extremes locates the midline, $11\,\mathrm{cm}$; half their difference gives the amplitude, $6\,\mathrm{cm}$.
- id: mct-p7-offset-time-graph-d
  content: |-
    Midline $11\,\mathrm{cm}$, amplitude $6\,\mathrm{cm}$, $T=9.375\,\mathrm s$, and $f=0.107\,\mathrm{Hz}$
  feedback: |-
    Multiplying $7.5$ by $1.25$ treats the cycle count as a scale factor in the wrong direction. Period is time per cycle, so divide: $T=7.5/1.25=6.0\,\mathrm s$.
- id: mct-p7-offset-time-graph-e
  content: |-
    Midline $11\,\mathrm{cm}$, amplitude $6\,\mathrm{cm}$, $\lambda=6.0\,\mathrm m$, and $f=0.17\,\mathrm{Hz}$
  feedback: |-
    The graph's horizontal span is measured in seconds, so $7.5/1.25$ is a period, not a wavelength. A wavelength requires a spatial graph or a separate distance measurement.
```

---

<a id="source-wave-speed"></a>
## Source-Video Worked Problem: Use the Wave-Speed Relation

The source problem in `qm1hDJrIYwE` at 0:04:31-0:05:18 gives

$$
v=125\,\mathrm{m/s},
\qquad
f=250\,\mathrm{Hz}.
$$

Once speed and frequency are known, rearrange $v=f\lambda$:

$$
\lambda=\frac{v}{f}
=\frac{125\,\mathrm{m/s}}{250\,\mathrm{s^{-1}}}
=\boxed{0.50\,\mathrm m}.
$$

The unit cancellation matches the target: $(\mathrm{m/s})/(1/\mathrm s)=\mathrm m$.

```quiz
type: radio
id: mct-p7-speed-to-wavelength
shuffle: true
content: |-
  A wave travels at $72\,\mathrm{m/s}$ and has frequency $18\,\mathrm{Hz}$. What is its wavelength?
options:
- id: mct-p7-speed-to-wavelength-a
  content: |-
    $4.0\,\mathrm m$
  correct: true
  feedback: |-
    The wave-speed relation is $v=f\lambda$, so wavelength is speed divided by frequency: $\lambda=72/18=4.0\,\mathrm m$.
- id: mct-p7-speed-to-wavelength-b
  content: |-
    $1296\,\mathrm m$
  feedback: |-
    Multiplying $v$ by $f$ does not isolate wavelength and produces incompatible units. From $v=f\lambda$, divide by frequency: $\lambda=v/f$.
- id: mct-p7-speed-to-wavelength-c
  content: |-
    $0.25\,\mathrm m$
  feedback: |-
    This reverses the quotient as $f/v$. Wavelength is the distance traveled during one cycle, so it is speed divided by cycles per second: $72/18=4.0\,\mathrm m$.
- id: mct-p7-speed-to-wavelength-d
  content: |-
    $4.0\,\mathrm s$
  feedback: |-
    The arithmetic is correct but the quantity and unit are not. Dividing meters per second by inverse seconds leaves meters, so the result is wavelength, $4.0\,\mathrm m$.
- id: mct-p7-speed-to-wavelength-e
  content: |-
    $0.0556\,\mathrm s$
  feedback: |-
    This is the period $T=1/f$, not the wavelength. To find wavelength, include the wave speed: $\lambda=v/f=72/18$.
```

---

<a id="source-crest-data"></a>
## Source-Video Worked Problem: Combine Crest Timing and Spacing

The water-wave problem in `vEzftaDL7fM` at 0:12:56-0:14:47 gives two different kinds of repeat data:

- a crest passes a fixed boat every $2.5\,\mathrm s$;
- adjacent crests are $10\,\mathrm m$ apart.

The repeat at one fixed location is temporal, so

$$
T=\boxed{2.5\,\mathrm s},
\qquad
f=\frac1T
=\frac1{2.5\,\mathrm s}
=\boxed{0.40\,\mathrm{Hz}}.
$$

The crest-to-crest spacing is spatial, so

$$
\lambda=\boxed{10\,\mathrm m}.
$$

Now the wave speed is

$$
v=f\lambda
=(0.40\,\mathrm{Hz})(10\,\mathrm m)
=\boxed{4.0\,\mathrm{m/s}}.
$$

Equivalently, one wavelength passes the boat in one period:

$$
v=\frac{\lambda}{T}
=\frac{10\,\mathrm m}{2.5\,\mathrm s}
=4.0\,\mathrm{m/s}.
$$

```quiz
type: radio
id: mct-p7-crest-timing-spacing
shuffle: true
content: |-
  At a fixed buoy, successive crests arrive $1.2\,\mathrm s$ apart. At one instant, neighboring crests are $6.0\,\mathrm m$ apart. Which set of wave quantities is correct?
options:
- id: mct-p7-crest-timing-spacing-a
  content: |-
    $T=1.2\,\mathrm s$, $f=0.83\,\mathrm{Hz}$, $\lambda=6.0\,\mathrm m$, and $v=5.0\,\mathrm{m/s}$
  correct: true
  feedback: |-
    Arrival time between crests is the period, while crest spacing is wavelength. Thus $f=1/1.2\approx0.83\,\mathrm{Hz}$ and $v=\lambda/T=6.0/1.2=5.0\,\mathrm{m/s}$.
- id: mct-p7-crest-timing-spacing-b
  content: |-
    $T=6.0\,\mathrm s$, $f=0.17\,\mathrm{Hz}$, $\lambda=1.2\,\mathrm m$, and $v=0.20\,\mathrm{m/s}$
  feedback: |-
    This swaps the temporal and spatial data. Seconds between arrivals give $T=1.2\,\mathrm s$, while meters between adjacent crests give $\lambda=6.0\,\mathrm m$.
- id: mct-p7-crest-timing-spacing-c
  content: |-
    $T=1.2\,\mathrm s$, $f=1.2\,\mathrm{Hz}$, $\lambda=6.0\,\mathrm m$, and $v=7.2\,\mathrm{m/s}$
  feedback: |-
    Frequency is cycles per second, the reciprocal of seconds per cycle. With $T=1.2\,\mathrm s$, $f=1/1.2\approx0.83\,\mathrm{Hz}$ rather than $1.2\,\mathrm{Hz}$.
- id: mct-p7-crest-timing-spacing-d
  content: |-
    $T=1.2\,\mathrm s$, $f=0.83\,\mathrm{Hz}$, $\lambda=6.0\,\mathrm m$, and $v=0.20\,\mathrm{m/s}$
  feedback: |-
    The period, frequency, and wavelength are right, but speed is distance per time. One $6.0\,\mathrm m$ wavelength passes in $1.2\,\mathrm s$, so $v=6.0/1.2=5.0\,\mathrm{m/s}$.
- id: mct-p7-crest-timing-spacing-e
  content: |-
    $T=0.83\,\mathrm s$, $f=1.2\,\mathrm{Hz}$, $\lambda=6.0\,\mathrm m$, and $v=7.2\,\mathrm{m/s}$
  feedback: |-
    The observed $1.2\,\mathrm s$ is already the time from one crest to the next, so it is the period. Taking its reciprocal gives frequency; it does not replace the measured period.
```

---

<a id="lecture-two-views"></a>
## Lecture Recognition Aid: Snapshot or Particle History?

The M5-1 lecture notes separate two views of the same traveling wave:

- $y(x)$ at a fixed time is a snapshot of many particles.
- $y(t)$ at a fixed position is the time history of one particle.

This distinction also prevents a common motion error. For a right-moving wave, shift the entire spatial profile slightly to the right, then compare the old and shifted heights at the same fixed $x$. The particle moves vertically to the new height; it does not slide horizontally along the drawn curve.

```quiz
type: radio
id: mct-p7-snapshot-history
shuffle: true
content: |-
  Which interpretation of two sinusoidal wave graphs is correct?
options:
- id: mct-p7-snapshot-history-a
  content: |-
    A $y$-versus-$x$ graph shows many particles at one instant, while a $y$-versus-$t$ graph at fixed $x$ follows one particle through time.
  correct: true
  feedback: |-
    Position on the horizontal axis samples the medium across space at one instant; time on the horizontal axis follows the displacement at one fixed location. Therefore their repeated horizontal intervals are $\lambda$ and $T$, respectively.
- id: mct-p7-snapshot-history-b
  content: |-
    Both graphs show the path traveled by one particle through space.
  feedback: |-
    A wave curve is not a particle trajectory. A spatial snapshot records the simultaneous displacements of many particles, while a time graph records one particle's local oscillation.
- id: mct-p7-snapshot-history-c
  content: |-
    A $y$-versus-$x$ graph gives period, while a $y$-versus-$t$ graph gives wavelength.
  feedback: |-
    The assignments follow the horizontal units. Spatial repetition in meters is wavelength; temporal repetition in seconds is period.
- id: mct-p7-snapshot-history-d
  content: |-
    A $y$-versus-$x$ graph follows one particle, while a $y$-versus-$t$ graph shows all particles at one instant.
  feedback: |-
    This reverses the two views. Varying $x$ at fixed time scans many locations; varying $t$ at fixed position tracks one location.
- id: mct-p7-snapshot-history-e
  content: |-
    The graph's shape alone determines whether its horizontal cycle is $\lambda$ or $T$.
  feedback: |-
    Sinusoidal spatial and temporal graphs can have the same shape. The horizontal label and units—not the curve alone—determine whether a cycle is a distance or a time.
```

---

<a id="summary"></a>
## Summary

- Read the horizontal axis before reading a cycle: $x$ means a spatial snapshot and $t$ means a particle's time history.
- Use equivalent points with the same phase, or divide a longer span by its number of complete cycles:
  $$
  \lambda=\frac{\Delta x}{N},
  \qquad
  T=\frac{\Delta t}{N}.
  $$
- For a partial cycle, divide the observed span by the observed fraction of a cycle.
- With an offset midline,
  $$
  y_{\text{mid}}=\frac{y_{\max}+y_{\min}}2,
  \qquad
  A=\frac{y_{\max}-y_{\min}}2.
  $$
- Convert period to frequency with $f=1/T$.
- Connect the spatial and temporal scales only after classifying them:
  $$
  v=\frac{\lambda}{T}=f\lambda.
  $$
- Do not call a horizontal interval a wavelength or period from the curve's shape alone; its variable and units decide.

<!-- lesson-nav:start -->
---

```update-progress
```

[[212/Home|Home]]
[[212/0. Table of Contents/TOC|Table of Contents]]

---
<!-- lesson-nav:end -->
