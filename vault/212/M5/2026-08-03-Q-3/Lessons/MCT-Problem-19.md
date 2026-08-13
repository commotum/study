# Map Pipe Boundaries, Harmonics, and Overtones

<!--
lesson-id: 212-M5-077
topic-code: MTH212.M5.77
-->

## Table of Contents

- [Introduction](#introduction)
- [Boundary Conditions and Allowed Harmonics](#pipe-boundaries)
- [Source-Video Worked Problem: Open-Open Pipe](#source-open-open)
- [Source-Video Worked Problem: Closed-Open Pipe](#source-closed-open)
- [Source-Video Worked Problem: Infer the Pipe from Successive Resonances](#source-successive-resonances)
- [Paired-Lecture Worked Example: Harmonic Ratios](#lecture-harmonic-ratios)
- [Summary](#summary)

## Prerequisites

- Use $v=f\lambda$ and rearrange it as $f=v/\lambda$ or $\lambda=v/f$.
- Substitute into a formula and track units.
- Recognize an arithmetic sequence and its constant spacing.
- Distinguish an item’s ordinal position from its numerical label.

---

<a id="introduction"></a>
## Introduction

An organ-pipe problem must be classified by its ends before any harmonic number is used. The boundary type decides both the length factor and the allowed values of $n$:

| Pipe type | Displacement at ends | Allowed $n$ | Wavelength | Frequency |
|---|---|---|---|---|
| open-open | antinode, antinode | $1,2,3,\ldots$ | $\lambda_n=2L/n$ | $f_n=nv/(2L)$ |
| closed-closed | node, node | $1,2,3,\ldots$ | $\lambda_n=2L/n$ | $f_n=nv/(2L)$ |
| closed-open | node, antinode | $1,3,5,\ldots$ | $\lambda_n=4L/n$ | $f_n=nv/(4L)$ |

These are air-displacement boundaries. Pressure uses the opposite labels:

- a closed end is a pressure antinode;
- an open end is approximately a pressure node.

The calculation follows one route:

1. Classify the pipe by its ends.
2. Translate “overtone” into the allowed harmonic number $n$.
3. Use the corresponding $2L$ or $4L$ formula.
4. Check that $n$ belongs to the pipe’s allowed sequence.

An overtone counts resonances above the fundamental; it is not automatically the same as a harmonic number. If $q$ is the overtone number, then

$$
\boxed{\text{open-open or closed-closed: }n=q+1}
$$

and

$$
\boxed{\text{closed-open: }n=2q+1}.
$$

For example, the third overtone is $n=4$ in an open-open pipe but $n=7$ in a closed-open pipe.

| Resonance position | fundamental | first overtone | second overtone | third overtone |
|---|---:|---:|---:|---:|
| equal-end harmonic $n$ | $1$ | $2$ | $3$ | $4$ |
| closed-open harmonic $n$ | $1$ | $3$ | $5$ | $7$ |

---

<a id="pipe-boundaries"></a>
## Boundary Conditions and Allowed Harmonics

The fundamental standing-wave pattern must fit the displacement conditions at both ends:

- Equal end types fit half a wavelength:
  $$
  L=\frac{\lambda_1}{2},
  \qquad
  f_1=\frac{v}{2L}.
  $$
- One closed and one open end fit one quarter of a wavelength:
  $$
  L=\frac{\lambda_1}{4},
  \qquad
  f_1=\frac{v}{4L}.
  $$

For an open-open or closed-closed pipe, every positive-integer multiple of $f_1$ remains compatible with the equal end conditions:

$$
f_1,\ 2f_1,\ 3f_1,\ 4f_1,\ldots
$$

For a closed-open pipe, only odd multiples preserve a node at one end and an antinode at the other:

$$
f_1,\ 3f_1,\ 5f_1,\ 7f_1,\ldots
$$

Thus the next resonance after $f_1$ in a closed-open pipe is $f_3$, not $f_2$.

```quiz
type: radio
id: mct-p19-classify-and-map
shuffle: true
content: |-
  A pipe is closed at one end and open at the other. Which formula and harmonic number describe its third overtone?
options:
- id: mct-p19-classify-and-map-a
  content: |-
    $f_n=\dfrac{nv}{2L}$ with $n=4$
  feedback: |-
    This is the equal-end formula and overtone map. A closed-open pipe uses $4L$ and supports only odd harmonics.
- id: mct-p19-classify-and-map-b
  content: |-
    $f_n=\dfrac{nv}{4L}$ with $n=3$
  feedback: |-
    The third harmonic is only the first overtone of a closed-open pipe. Counting allowed resonances gives $n=1,3,5,7$, so the third overtone has $n=7$.
- id: mct-p19-classify-and-map-c
  content: |-
    $f_n=\dfrac{nv}{4L}$ with $n=7$
  correct: true
  feedback: |-
    A closed-open pipe uses the quarter-wave formula and odd $n$. The third resonance above the fundamental follows $n=1,3,5,7$, so the third overtone is $n=7$.
- id: mct-p19-classify-and-map-d
  content: |-
    $f_n=\dfrac{nv}{2L}$ with $n=7$
  feedback: |-
    The odd harmonic label is right, but $2L$ belongs to pipes with equal end types. One closed and one open end require the $4L$ denominator.
- id: mct-p19-classify-and-map-e
  content: |-
    $f_n=\dfrac{nv}{4L}$ with $n=4$
  feedback: |-
    A fourth harmonic is not allowed in an ideal closed-open pipe. Translate overtone position through the odd sequence rather than using $q+1$.
```

---

<a id="source-open-open"></a>
## Source-Video Worked Problem: Open-Open Pipe

The first problem in `7eyYNNUojEc` at 0:00:00-0:04:23 gives an open-open pipe with

$$
L=0.85\,\mathrm m,
\qquad
T=15^\circ\mathrm C.
$$

The source approximates sound speed by

$$
v=331+0.6T,
$$

so

$$
v=331+0.6(15)
=\boxed{340\,\mathrm{m/s}}.
$$

Because both ends are open, use $f_n=nv/(2L)$ with every positive integer $n$.

### Fundamental and fourth harmonic

$$
\begin{aligned}
f_1
&=\frac{340}{2(0.85)}
=\boxed{200\,\mathrm{Hz}},\\
f_4
&=4f_1
=\boxed{800\,\mathrm{Hz}}.
\end{aligned}
$$

### Fifth overtone

For equal-end pipes, $n=q+1$. The fifth overtone therefore has $n=6$:

$$
f_6=6f_1
=6(200)
=\boxed{1200\,\mathrm{Hz}}.
$$

### Second-overtone wavelength

The second overtone has $n=3$:

$$
\begin{aligned}
\lambda_3
&=\frac{2L}{3}\\
&=\frac{2(0.85\,\mathrm m)}{3}\\
&=\boxed{0.567\,\mathrm m}.
\end{aligned}
$$

The wave relation confirms the same value because $f_3=3f_1=600\,\mathrm{Hz}$:

$$
\lambda_3=\frac{v}{f_3}
=\frac{340\,\mathrm{m/s}}{600\,\mathrm{Hz}}
=0.567\,\mathrm m.
$$

```quiz
type: radio
id: mct-p19-open-open
shuffle: true
content: |-
  An open-open pipe has length $1.00\,\mathrm m$ at $20^\circ\mathrm C$. Using $v=331+0.6T$, what is the frequency of its third overtone?
options:
- id: mct-p19-open-open-a
  content: |-
    $171.5\,\mathrm{Hz}$
  feedback: |-
    This is the fundamental, $v/(2L)$. The third overtone of an open-open pipe is the fourth harmonic, so multiply the fundamental by $4$.
- id: mct-p19-open-open-b
  content: |-
    $514.5\,\mathrm{Hz}$
  feedback: |-
    This uses $n=3$, which is the second overtone in an open-open pipe. The third overtone maps to $n=4$.
- id: mct-p19-open-open-c
  content: |-
    $686\,\mathrm{Hz}$
  correct: true
  feedback: |-
    At $20^\circ\mathrm C$, $v=331+0.6(20)=343\,\mathrm{m/s}$. An open-open third overtone has $n=4$, so $f_4=4(343)/[2(1.00)]=686\,\mathrm{Hz}$.
- id: mct-p19-open-open-d
  content: |-
    $343\,\mathrm{Hz}$
  feedback: |-
    This divides by the pipe length but omits the $2$ required by equal-end boundary conditions. It also does not apply the fourth-harmonic multiplier.
- id: mct-p19-open-open-e
  content: |-
    $1372\,\mathrm{Hz}$
  feedback: |-
    This multiplies the sound speed by the fourth-harmonic label but omits the equal-end denominator $2L$. Use $f_4=4v/(2L)$, not $4v/L$.
```

---

<a id="source-closed-open"></a>
## Source-Video Worked Problem: Closed-Open Pipe

The second problem in `7eyYNNUojEc` at 0:04:26-0:09:01 gives a pipe closed at one end and open at the other:

$$
L=0.50\,\mathrm m,
\qquad
T=15^\circ\mathrm C,
\qquad
v=340\,\mathrm{m/s}.
$$

Use $f_n=nv/(4L)$ and only $n=1,3,5,\ldots$.

### Fundamental and third overtone

$$
f_1
=\frac{340}{4(0.50)}
=\boxed{170\,\mathrm{Hz}}.
$$

The third overtone is the fourth allowed resonance:

$$
n=2q+1=2(3)+1=7.
$$

Therefore,

$$
f_7=7f_1
=7(170)
=\boxed{1190\,\mathrm{Hz}}.
$$

It is not $4f_1=680\,\mathrm{Hz}$; $n=4$ is not an allowed closed-open harmonic.

### Second-overtone wavelength and frequency

The second overtone has

$$
n=2(2)+1=5.
$$

Its wavelength is

$$
\lambda_5
=\frac{4L}{5}
=\frac{4(0.50\,\mathrm m)}{5}
=\boxed{0.40\,\mathrm m},
$$

and its frequency is

$$
f_5=5f_1
=5(170)
=\boxed{850\,\mathrm{Hz}}.
$$

The check must divide speed by frequency:

$$
\lambda_5=\frac{v}{f_5}
=\frac{340\,\mathrm{m/s}}{850\,\mathrm{s^{-1}}}
=0.40\,\mathrm m.
$$

**Source correction.** At 0:08:14 the narration says that wavelength is speed “times” frequency. The written relation is $v=\lambda f$, and the displayed numbers reach $0.40\,\mathrm m$ only by using $\lambda=v/f$. Multiplying would produce $\mathrm{m/s^2}$, not a wavelength.

```quiz
type: radio
id: mct-p19-closed-open
shuffle: true
content: |-
  A closed-open pipe has $L=0.70\,\mathrm m$ and $v=343\,\mathrm{m/s}$. What is the frequency of its third overtone?
options:
- id: mct-p19-closed-open-a
  content: |-
    $490\,\mathrm{Hz}$
  feedback: |-
    This uses $n=4$, as though overtone number were one less than harmonic number for every pipe. A closed-open pipe skips even harmonics, so its third overtone has $n=7$.
- id: mct-p19-closed-open-b
  content: |-
    $857.5\,\mathrm{Hz}$
  correct: true
  feedback: |-
    A closed-open pipe uses $f_n=nv/(4L)$ and the third overtone has $n=7$. Thus $f_7=7(343)/[4(0.70)]=857.5\,\mathrm{Hz}$.
- id: mct-p19-closed-open-c
  content: |-
    $122.5\,\mathrm{Hz}$
  feedback: |-
    This is the fundamental $v/(4L)$. The question asks for the third overtone, which is seven times the fundamental in a closed-open pipe.
- id: mct-p19-closed-open-d
  content: |-
    $1715\,\mathrm{Hz}$
  feedback: |-
    This uses the odd label $n=7$ but divides by $2L$. The $2L$ denominator requires equal end types; one closed and one open end require $4L$.
- id: mct-p19-closed-open-e
  content: |-
    $367.5\,\mathrm{Hz}$
  feedback: |-
    This uses $n=3$, the first overtone of a closed-open pipe. The allowed overtone sequence is $n=3,5,7,\ldots$, so the third overtone uses $n=7$.
```

---

<a id="source-successive-resonances"></a>
## Source-Video Worked Problem: Infer the Pipe from Successive Resonances

The final source problem in `7eyYNNUojEc` at 0:09:03-0:11:43 gives successive resonances

$$
750\,\mathrm{Hz}
\qquad\text{and}\qquad
1050\,\mathrm{Hz}.
$$

Their spacing is

$$
\Delta f=1050-750
=\boxed{300\,\mathrm{Hz}}.
$$

Step backward through the same spacing:

$$
1050,\ 750,\ 450,\ 150\,\mathrm{Hz}.
$$

The lowest positive term is $150\,\mathrm{Hz}$, so

$$
\boxed{f_1=150\,\mathrm{Hz}}.
$$

These resonances are

$$
f_1,\ f_3,\ f_5,\ f_7
=150,\ 450,\ 750,\ 1050\,\mathrm{Hz}.
$$

Test both pipe sequences against the spacing:

- For an equal-end pipe, successive resonances differ by $f_1$. That would give $f_1=300\,\mathrm{Hz}$, but $750/300=2.5$ is not an integer harmonic number.
- For a closed-open pipe, successive resonances differ by two harmonic numbers. Therefore $300=2f_1$, so $f_1=150\,\mathrm{Hz}$; then $750=5f_1$ and $1050=7f_1$, both allowed.

Only the odd-harmonic sequence fits, so the pipe is closed-open:

$$
\boxed{\Delta f=2f_1}.
$$

With the source’s $v=340\,\mathrm{m/s}$,

$$
\begin{aligned}
L
&=\frac{v}{4f_1}\\
&=\frac{340}{4(150)}\,\mathrm m\\
&=\boxed{0.567\,\mathrm m}.
\end{aligned}
$$

For an open-open or closed-closed pipe, consecutive allowed harmonics are separated by $f_1$, not $2f_1$.

```quiz
type: radio
id: mct-p19-successive-resonances
shuffle: true
content: |-
  Two successive resonances of a pipe are $600\,\mathrm{Hz}$ and $840\,\mathrm{Hz}$. The resonance sequence has no even harmonics, and $v=336\,\mathrm{m/s}$. What are the pipe type, fundamental frequency, and length?
options:
- id: mct-p19-successive-resonances-a
  content: |-
    closed-open; $f_1=120\,\mathrm{Hz}$; $L=0.700\,\mathrm m$
  correct: true
  feedback: |-
    Odd-only harmonics identify a closed-open pipe. Its successive allowed modes are separated by $2f_1$, so $f_1=(840-600)/2=120\,\mathrm{Hz}$ and $L=v/(4f_1)=336/480=0.700\,\mathrm m$.
- id: mct-p19-successive-resonances-b
  content: |-
    open-open; $f_1=240\,\mathrm{Hz}$; $L=0.700\,\mathrm m$
  feedback: |-
    A $240\,\mathrm{Hz}$ spacing would equal $f_1$ for an equal-end pipe, but the prompt says even harmonics are absent. That absence identifies a closed-open pipe, where the spacing is $2f_1$.
- id: mct-p19-successive-resonances-c
  content: |-
    closed-open; $f_1=240\,\mathrm{Hz}$; $L=0.350\,\mathrm m$
  feedback: |-
    This treats the full $240\,\mathrm{Hz}$ spacing as the fundamental. Closed-open successive resonances jump from one odd harmonic to the next, so the spacing is twice the fundamental.
- id: mct-p19-successive-resonances-d
  content: |-
    closed-open; $f_1=120\,\mathrm{Hz}$; $L=1.40\,\mathrm m$
  feedback: |-
    The pipe type and fundamental are right, but this uses the equal-end relation $L=v/(2f_1)$. A closed-open fundamental satisfies $f_1=v/(4L)$.
- id: mct-p19-successive-resonances-e
  content: |-
    closed-closed; $f_1=120\,\mathrm{Hz}$; $L=1.40\,\mathrm m$
  feedback: |-
    A closed-closed pipe has equal end types and allows all positive-integer harmonics. The stated odd-only sequence requires one closed and one open end.
```

---

<a id="lecture-harmonic-ratios"></a>
## Paired-Lecture Worked Example: Harmonic Ratios

The M5-4 lecture notes use a closed-open pipe with

$$
L=0.85\,\mathrm m,
\qquad
v=343\,\mathrm{m/s}.
$$

The third harmonic is

$$
\begin{aligned}
f_3
&=\frac{3v}{4L}\\
&=\frac{3(343)}{4(0.85)}\,\mathrm{Hz}\\
&=302.65\,\mathrm{Hz}\\
&\approx\boxed{303\,\mathrm{Hz}}.
\end{aligned}
$$

The lecture rounds this to about $300\,\mathrm{Hz}$ before using the ratio

$$
\frac{f_5}{f_3}=\frac{5}{3}.
$$

Thus

$$
f_5\approx\frac53(300\,\mathrm{Hz})
=\boxed{500\,\mathrm{Hz}}.
$$

Using unrounded values gives $f_5=504.41\,\mathrm{Hz}$. The $500\,\mathrm{Hz}$ result is consistent with the lecture’s rounded $f_3$; do not mix the rounded and unrounded inputs while claiming extra precision.

```quiz
type: radio
id: mct-p19-harmonic-ratio
shuffle: true
content: |-
  In one closed-open pipe, the third harmonic is $270\,\mathrm{Hz}$. What is the fifth-harmonic frequency?
options:
- id: mct-p19-harmonic-ratio-a
  content: |-
    $450\,\mathrm{Hz}$
  correct: true
  feedback: |-
    For one pipe, allowed harmonic frequencies scale with their harmonic numbers. Therefore $f_5/f_3=5/3$ and $f_5=(5/3)(270)=450\,\mathrm{Hz}$.
- id: mct-p19-harmonic-ratio-b
  content: |-
    $162\,\mathrm{Hz}$
  feedback: |-
    This reverses the ratio and computes $(3/5)f_3$. The fifth harmonic has the larger harmonic number, so it must have the higher frequency.
- id: mct-p19-harmonic-ratio-c
  content: |-
    $540\,\mathrm{Hz}$
  feedback: |-
    This doubles the third harmonic. Doubling would map $n=3$ to $n=6$, but the target is $n=5$, so use the ratio $5/3$.
- id: mct-p19-harmonic-ratio-d
  content: |-
    $810\,\mathrm{Hz}$
  feedback: |-
    This multiplies the third-harmonic frequency by $3$ again. The given $270\,\mathrm{Hz}$ already corresponds to $n=3$; convert between modes with $5/3$.
- id: mct-p19-harmonic-ratio-e
  content: |-
    $90\,\mathrm{Hz}$
  feedback: |-
    This is the fundamental, $f_1=f_3/3$. The question asks for the fifth harmonic, so continue to $f_5=5f_1$.
```

---

<a id="summary"></a>
## Summary

- Classify the pipe before choosing a formula or harmonic number.
- Open-open and closed-closed pipes use
  $$
  f_n=\frac{nv}{2L},
  \qquad
  n=1,2,3,\ldots
  $$
- Closed-open pipes use
  $$
  f_n=\frac{nv}{4L},
  \qquad
  n=1,3,5,\ldots
  $$
- For displacement, a closed end is a node and an open end is an antinode; pressure conditions are reversed.
- Map overtone $q$ to $n=q+1$ for equal-end pipes and to $n=2q+1$ for closed-open pipes.
- Use $\lambda=v/f$, not $vf$, when frequency and wave speed are known.
- Successive closed-open resonances differ by $2f_1$ because adjacent allowed harmonic numbers differ by $2$.
- Check that the chosen $n$ is allowed and that $v=f\lambda$ holds with consistent units.

<!-- lesson-nav:start -->
---

```update-progress
```

[[212/Home|Home]]
[[212/0. Table of Contents/TOC|Table of Contents]]

---
<!-- lesson-nav:end -->
