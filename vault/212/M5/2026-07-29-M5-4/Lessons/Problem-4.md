# Third Harmonic of an Open–Closed Pipe

<!--
lesson-id: 212-M5-034
topic-code: MTH212.M5.34
-->

## Table of Contents

- [Introduction](#introduction)
- [Place the Displacement Nodes and Antinodes](#place-the-displacement-nodes-and-antinodes)
- [Convert the Pattern to a Wavelength](#convert-the-pattern-to-a-wavelength)
- [Convert Wavelength to Frequency](#convert-wavelength-to-frequency)
- [Apply the Method and Round](#apply-the-method-and-round)
- [Summary](#summary)

## Prerequisites

- Distinguishing a displacement node from a displacement antinode
- Using $v=f\lambda$
- Substituting values with units into a formula
- Rounding to the significant figures set by measured data

---

<a id="introduction"></a>
## Introduction

The cue is a pipe with one closed end and one open end. For displacement, the closed end must be a node and the open end must be an antinode. To find the third-harmonic frequency, draw the third-harmonic node–antinode pattern, turn its three quarter-wavelength segments into an equation for $\lambda_3$, and then use $f_3=v/\lambda_3$.

Only odd harmonics fit these endpoint conditions. The third harmonic is the next allowed pattern after the fundamental.

Use this short chain every time:

$$
\text{endpoints}
\;\longrightarrow\;
\text{quarter-wavelength count}
\;\longrightarrow\;
\lambda_3
\;\longrightarrow\;
f_3.
$$

---

<a id="place-the-displacement-nodes-and-antinodes"></a>
## Place the Displacement Nodes and Antinodes

**Example:** Describe the displacement standing-wave pattern for the third harmonic of an open–closed pipe of length $L$.

**Explanation**

Start with a displacement node at the closed end. Nodes and antinodes then alternate every quarter wavelength until the open end is reached:

$$
\text{node at }x=0
\;\longrightarrow\;
\text{antinode at }x=\frac{L}{3}
\;\longrightarrow\;
\text{node at }x=\frac{2L}{3}
\;\longrightarrow\;
\text{antinode at }x=L.
$$

This is an N–A–N–A pattern. Reversing the endpoint types would describe a pipe whose open and closed ends have been swapped.

Count the node-to-antinode intervals, not the visible humps of the curve. Each N-to-A or A-to-N interval contributes exactly $\lambda/4$.

```quiz
type: radio
id: p4-pattern
content: |-
  Which displacement pattern is the third harmonic of a pipe that is closed at $x=0$ and open at $x=L$?
options:
- id: a
  content: |-
    Node at $0$, antinode at $L/3$, node at $2L/3$, antinode at $L$
  correct: true
  feedback: |-
    Correct. Displacement is zero at the closed end and maximum at the open end, with alternating node and antinode points.
- id: b
  content: |-
    Antinode at $0$, node at $L/3$, antinode at $2L/3$, node at $L$
  feedback: |-
    This reverses the required displacement conditions at both ends.
- id: c
  content: |-
    Node at $0$, antinode at $L/2$, node at $L$
  feedback: |-
    This ends with a node, so it cannot satisfy the open-end displacement condition.
- id: d
  content: |-
    Antinode at $0$, node at $L/2$, antinode at $L$
  feedback: |-
    The closed end must be a displacement node, not an antinode.
```

---

<a id="convert-the-pattern-to-a-wavelength"></a>
## Convert the Pattern to a Wavelength

**Example:** An open–closed pipe has length $0.72\ \mathrm{m}$. What wavelength fits its third-harmonic displacement pattern?

**Explanation**

The N–A–N–A pattern contains three node-to-antinode intervals. Each interval is one quarter wavelength, so

$$
L=3\left(\frac{\lambda_3}{4}\right)=\frac{3\lambda_3}{4}.
$$

Solve for the wavelength before substituting:

$$
\lambda_3=\frac{4L}{3}
=\frac{4(0.72\ \mathrm{m})}{3}
=0.96\ \mathrm{m}.
$$

The factor $4/3$ comes from three quarter-wavelength segments; it is not the formula for every open–closed harmonic.

A useful check is that $\lambda_3$ must be longer than $L$: three quarters of the wavelength, rather than one full wavelength, occupies the pipe.

```quiz
type: radio
id: p4-wavelength
content: |-
  An open–closed pipe is $0.90\ \mathrm{m}$ long. What wavelength fits its third harmonic?
options:
- id: a
  content: |-
    $1.20\ \mathrm{m}$
  correct: true
  feedback: |-
    Correct. $\lambda_3=4L/3=4(0.90\ \mathrm{m})/3=1.20\ \mathrm{m}$.
- id: b
  content: |-
    $0.675\ \mathrm{m}$
  feedback: |-
    This multiplies by $3/4$ instead of solving $L=3\lambda_3/4$ for $\lambda_3$.
- id: c
  content: |-
    $0.30\ \mathrm{m}$
  feedback: |-
    This divides the pipe into three pieces but treats each quarter wavelength as a full wavelength.
- id: d
  content: |-
    $3.60\ \mathrm{m}$
  feedback: |-
    This treats the pipe length as one quarter wavelength, which describes the fundamental rather than the third harmonic.
```

---

<a id="convert-wavelength-to-frequency"></a>
## Convert Wavelength to Frequency

**Example:** An open–closed pipe is $0.60\ \mathrm{m}$ long, and sound travels at $340\ \mathrm{m/s}$. Find the third-harmonic frequency.

**Explanation**

First convert the pattern to a wavelength:

$$
\lambda_3=\frac{4L}{3}
=\frac{4(0.60\ \mathrm{m})}{3}
=0.80\ \mathrm{m}.
$$

Then use $v=f\lambda$:

$$
f_3=\frac{v}{\lambda_3}
=\frac{340\ \mathrm{m/s}}{0.80\ \mathrm{m}}
=425\ \mathrm{s^{-1}}
=425\ \mathrm{Hz}.
$$

Combining the two equations gives the useful third-harmonic formula

$$
f_3=\frac{3v}{4L}.
$$

This formula also gives a direction check: for a fixed sound speed, $f_3$ varies inversely with $L$. A longer pipe must have a lower third-harmonic frequency.

```quiz
type: radio
id: p4-frequency
content: |-
  An open–closed pipe is $0.75\ \mathrm{m}$ long, and the sound speed is $344\ \mathrm{m/s}$. What is its third-harmonic frequency?
options:
- id: a
  content: |-
    $344\ \mathrm{Hz}$
  correct: true
  feedback: |-
    Correct. $f_3=3v/(4L)=3(344)/(4(0.75))=344\ \mathrm{Hz}$.
- id: b
  content: |-
    $115\ \mathrm{Hz}$
  feedback: |-
    This is near the fundamental frequency; the question asks for the third harmonic.
- id: c
  content: |-
    $459\ \mathrm{Hz}$
  feedback: |-
    This uses $v/L$ and ignores the three-quarter-wavelength geometry.
- id: d
  content: |-
    $258\ \mathrm{Hz}$
  feedback: |-
    This multiplies by $3/4$ when the length belongs in the denominator of $3v/(4L)$.
```

---

<a id="apply-the-method-and-round"></a>
## Apply the Method and Round

**Example:** An open–closed pipe is $0.85\ \mathrm{m}$ long. Use a sound speed of $343\ \mathrm{m/s}$. What is its third-harmonic frequency? Be sure to draw the corresponding displacement standing-wave pattern.

**Explanation**

**1. Draw the endpoint pattern.** The corresponding displacement pattern has a node at the closed end, an antinode at $x=L/3$, a node at $x=2L/3$, and an antinode at the open end:

![](<../Source/Images/open-closed-pipe-third-harmonic.png>)

**2. Translate the picture into an equation.** The picture places three quarter-wavelength segments in the pipe, so

$$
L=\frac{3\lambda_3}{4}
\qquad\text{and}\qquad
f_3=\frac{v}{\lambda_3}=\frac{3v}{4L}.
$$

**3. Substitute with units.** Keep the unrounded value until the end:

$$
\begin{aligned}
f_3
&=\frac{3(343\ \mathrm{m/s})}{4(0.85\ \mathrm{m})}\\
&=302.647\ldots\ \mathrm{Hz}.
\end{aligned}
$$

The units also check: $(\mathrm{m/s})/\mathrm{m}=\mathrm{s^{-1}}=\mathrm{Hz}$.

**4. Report the requested precision.** The pipe length $0.85\ \mathrm{m}$ has two significant figures, so the final result is

$$
f_3=3.0\times10^2\ \mathrm{Hz}.
$$

For the requested number-only answer, enter $\boxed{300}$.

```quiz
type: radio
id: p4-precision
content: |-
  An open–closed pipe is $0.65\ \mathrm{m}$ long, and the sound speed is $343\ \mathrm{m/s}$. What number should be reported for its third-harmonic frequency if the measured length sets two significant figures?
options:
- id: a
  content: |-
    $400$
  correct: true
  feedback: |-
    Correct. The unrounded result is $395.769\ldots\ \mathrm{Hz}$, which is $4.0\times10^2\ \mathrm{Hz}$ to two significant figures.
- id: b
  content: |-
    $396$
  feedback: |-
    This keeps three significant figures even though the length supplies only two.
- id: c
  content: |-
    $132$
  feedback: |-
    This is close to the fundamental frequency rather than the third-harmonic frequency.
- id: d
  content: |-
    $528$
  feedback: |-
    This uses $v/L$ and omits the factor $3/4$ from the standing-wave geometry.
```

---

<a id="summary"></a>
## Summary

For an open–closed pipe, displacement is a node at the closed end and an antinode at the open end. The third-harmonic pattern is N–A–N–A, so three quarter wavelengths fit in the pipe:

$$
L=\frac{3\lambda_3}{4},
\qquad
\lambda_3=\frac{4L}{3},
\qquad
f_3=\frac{3v}{4L}.
$$

The reusable procedure is:

1. Mark a displacement node at the closed end and an antinode at the open end.
2. Draw N–A–N–A and count three quarter-wavelength intervals.
3. Write $L=3\lambda_3/4$, then use $f_3=v/\lambda_3=3v/(4L)$.
4. Check that the units reduce to hertz and that increasing $L$ would decrease $f_3$.
5. Keep full calculator precision and round only the reported answer.

The main trap is using the fundamental relation $L=\lambda/4$ for the third harmonic. For the assigned values, the unrounded result is $302.647\ldots\ \mathrm{Hz}$ and the required number-only answer is $300$.

<!-- lesson-nav:start -->
---

```update-progress
```

[[212/Home|Home]]
[[212/0. Table of Contents/TOC|Table of Contents]]

[Quiz 3 Study Guide](../../2026-08-03-Q-3/Study-Guide.md)
Next: [Finding Complete Constructive Interference in a Crest Diagram](../../2026-07-30-M5-5/Lessons/Problem-2.md)

Study guide index: 25/28

---
<!-- lesson-nav:end -->
