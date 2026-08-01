# Fifth Harmonic of an Open–Closed Pipe

## Table of Contents

- [Introduction](#introduction)
- [Anchor the Boundary Conditions](#anchor-the-boundary-conditions)
- [Count Quarter-Wavelength Segments](#count-quarter-wavelength-segments)
- [Convert Wavelength to Frequency](#convert-wavelength-to-frequency)
- [Complete the Given Pipe Problem](#complete-the-given-pipe-problem)
- [Summary](#summary)

## Prerequisites

- Recognize displacement nodes and antinodes in a standing wave.
- Use the wave-speed relation $v=f\lambda$.
- Substitute measured quantities with units into a formula.
- Round a calculated result to the significant figures of the least precise given measurement.

---

<a id="introduction"></a>
## Introduction

When a pipe is closed at one end and open at the other, its displacement standing wave must have a **node** at the closed end and an **antinode** at the open end. This unequal pair of boundary conditions allows only the odd harmonics.

For the $n$th allowed harmonic, where $n=1,3,5,\ldots$,

$$
L=\frac{n\lambda_n}{4}
\qquad\text{and}\qquad
f_n=\frac{v}{\lambda_n}=\frac{nv}{4L}.
$$

Here, $L$ is the pipe length, $v$ is the sound speed, $\lambda_n$ is the wavelength of the $n$th harmonic, and $f_n$ is its frequency.

The key is to translate the harmonic label into $n$ quarter-wavelength segments, draw the alternating node–antinode pattern, and then use the same value of $n$ in the frequency calculation.

Two direction checks help catch setup errors: with $v$ and $L$ fixed, $f_n$ varies directly with $n$; with $v$ and $n$ fixed, $f_n$ varies inversely with $L$.

---

<a id="anchor-the-boundary-conditions"></a>
## Anchor the Boundary Conditions

**Example:** Describe the displacement pattern for the third harmonic of an open–closed pipe of length $L$.

**Explanation**

Start at the closed end with a node and finish at the open end with an antinode. The third harmonic contains three quarter-wavelength segments, so the turning points are equally spaced by $L/3$:

$$
\underbrace{N}_{x=0}
\;\longrightarrow\;
\underbrace{A}_{x=L/3}
\;\longrightarrow\;
\underbrace{N}_{x=2L/3}
\;\longrightarrow\;
\underbrace{A}_{x=L}.
$$

The labels must alternate. A drawing that begins with an antinode or ends with a node violates the pipe's boundary conditions.

```quiz
type: radio
id: problem-5-boundaries
content: |-
  Which sequence correctly describes the displacement pattern of the fifth harmonic of an open–closed pipe from the closed end to the open end?
options:
- id: a
  content: |-
    $A-N-A-N-A-N$
- id: b
  content: |-
    $N-A-N-A-N-A$
  correct: true
- id: c
  content: |-
    $N-A-N-A-N$
- id: d
  content: |-
    $N-N-A-A-N-A$
- id: e
  content: |-
    $A-N-A-N-A$
```

---

<a id="count-quarter-wavelength-segments"></a>
## Count Quarter-Wavelength Segments

**Example:** Relate the pipe length $L$ to the wavelength $\lambda_5$ for the fifth harmonic.

**Explanation**

The fifth harmonic places five quarter-wavelength segments inside the pipe. Therefore,

$$
L=5\left(\frac{\lambda_5}{4}\right)=\frac{5\lambda_5}{4}.
$$

Solving for wavelength gives

$$
\lambda_5=\frac{4L}{5}.
$$

The common trap is to use $L=5\lambda_5/2$, which counts half-wavelengths and fits equal end conditions, not one closed end and one open end.

```quiz
type: radio
id: problem-5-quarter-segments
content: |-
  Which equation relates $L$ and $\lambda_7$ for the seventh harmonic of an open–closed pipe?
options:
- id: a
  content: |-
    $L=\dfrac{7\lambda_7}{4}$
  correct: true
- id: b
  content: |-
    $L=\dfrac{7\lambda_7}{2}$
- id: c
  content: |-
    $L=\dfrac{4\lambda_7}{7}$
- id: d
  content: |-
    $L=7\lambda_7$
- id: e
  content: |-
    $L=\dfrac{\lambda_7}{4}$
```

---

<a id="convert-wavelength-to-frequency"></a>
## Convert Wavelength to Frequency

**Example:** An open–closed pipe has length $0.60\ \mathrm{m}$, and sound travels at $336\ \mathrm{m/s}$. Find its third-harmonic frequency.

**Explanation**

For the third harmonic, $n=3$. Substitute into the open–closed frequency formula:

$$
\begin{aligned}
f_3
&=\frac{3v}{4L} \\
&=\frac{3(336\ \mathrm{m/s})}{4(0.60\ \mathrm{m})} \\
&=420\ \mathrm{s}^{-1} \\
&=420\ \mathrm{Hz}.
\end{aligned}
$$

The meter units cancel, leaving inverse seconds, or hertz. The harmonic number multiplies the numerator; it does not multiply the pipe length.

This result also follows from the two linked relationships

$$
\lambda_3=\frac{4L}{3}
\qquad\text{and}\qquad
v=f_3\lambda_3.
$$

Thus the open–closed pipe condition selects the wavelength first, and the wave-speed relation converts that wavelength to frequency.

```quiz
type: radio
id: problem-5-frequency
content: |-
  An open–closed pipe has length $0.75\ \mathrm{m}$, and sound travels at $330\ \mathrm{m/s}$. What is its fifth-harmonic frequency?
options:
- id: a
  content: |-
    $110\ \mathrm{Hz}$
- id: b
  content: |-
    $220\ \mathrm{Hz}$
- id: c
  content: |-
    $440\ \mathrm{Hz}$
- id: d
  content: |-
    $550\ \mathrm{Hz}$
  correct: true
- id: e
  content: |-
    $1{,}100\ \mathrm{Hz}$
```

---

<a id="complete-the-given-pipe-problem"></a>
## Complete the Given Pipe Problem

**Example:** For the same $0.85\ \mathrm{m}$ open–closed pipe and sound speed of $343\ \mathrm{m/s}$, what is its fifth-harmonic frequency? Draw the corresponding displacement standing-wave pattern, and enter the frequency in hertz as a number only.

**Explanation**

The drawing starts with a displacement node at the closed end. It then alternates through an antinode at $x=L/5$, a node at $x=2L/5$, an antinode at $x=3L/5$, a node at $x=4L/5$, and a displacement antinode at the open end:

$$
\begin{array}{c|cccccc}
x & 0 & L/5 & 2L/5 & 3L/5 & 4L/5 & L \\
\hline
\text{displacement} & N & A & N & A & N & A
\end{array}
$$

When checking a schematic, verify both endpoints and the spacing: it must begin $N$, end $A$, and contain exactly five quarter-wavelength intervals, consistent with $L=5\lambda_5/4$.

This is five quarter-wavelength segments, so

$$
L=\frac{5\lambda_5}{4}
\qquad\Longrightarrow\qquad
\lambda_5=\frac{4L}{5}.
$$

Now compute the frequency:

$$
\begin{aligned}
f_5
&=\frac{v}{\lambda_5} \\
&=\frac{5v}{4L} \\
&=\frac{5(343\ \mathrm{m/s})}{4(0.85\ \mathrm{m})} \\
&=504.411\ldots\ \mathrm{Hz}.
\end{aligned}
$$

The pipe length $0.85\ \mathrm{m}$ has two significant figures, so the frequency is

$$
f_5=5.0\times10^2\ \mathrm{Hz}.
$$

As a reasonableness check, the fundamental frequency would be

$$
f_1=\frac{343}{4(0.85)}\approx101\ \mathrm{Hz},
$$

so the fifth harmonic should be five times that value, about $505\ \mathrm{Hz}$. The unrounded result $504.411\ldots\ \mathrm{Hz}$ is consistent with that prediction.

Because the requested entry is a number only, enter **500**.

```quiz
type: radio
id: problem-5-final-check
content: |-
  A fifth-harmonic calculation gives $497.8\ \mathrm{Hz}$. If the least precise given measurement has two significant figures and the answer box requests hertz as a number only, what should be entered?
options:
- id: a
  content: |-
    $497.8$
- id: b
  content: |-
    $498$
- id: c
  content: |-
    $5.0\times10^2\ \mathrm{Hz}$
- id: d
  content: |-
    $500$
  correct: true
- id: e
  content: |-
    $50$
```

---

<a id="summary"></a>
## Summary

For an open–closed pipe:

1. Put a displacement node at the closed end and an antinode at the open end.
2. For odd $n$, count $n$ quarter-wavelength segments: $L=n\lambda_n/4$.
3. Use $f_n=v/\lambda_n=nv/(4L)$.
4. Keep units through the calculation, round only at the end, and format the final entry exactly as requested.

Useful checks: increasing the odd harmonic number raises the frequency, while increasing the pipe length lowers it. The main trap is using a half-wavelength condition instead of the open–closed quarter-wavelength condition.

For the given fifth-harmonic problem, the pattern is $N-A-N-A-N-A$ and the numeric-only frequency entry is **500**.
