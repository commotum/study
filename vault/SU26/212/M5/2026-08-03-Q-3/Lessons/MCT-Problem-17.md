# Translate a Fixed-End Standing-Wave Mode

<!--
lesson-id: 212-M5-075
topic-code: MTH212.M5.75
-->

## Table of Contents

- [Introduction](#introduction)
- [Build the Mode Ledger](#mode-ledger)
- [Use the Frequency Ladder](#frequency-ladder)
- [Use the Wavelength Ladder](#wavelength-ladder)
- [Carry One Mode Through Length, Wavelength, and Frequency](#one-mode-chain)
- [Align Subscripts Before Multiplying](#align-subscripts)
- [Summary](#summary)

## Prerequisites

- Use $v=f\lambda$ for a traveling wave.
- Work with ratios of positive integers.
- Recognize a node as a point of zero displacement and an antinode as a point of maximum displacement.
- Use $1\ \mathrm{Hz}=1\ \mathrm{s^{-1}}$.

---

<a id="introduction"></a>
## Introduction

For a string fixed at both ends, first translate the picture or mode name into its harmonic number $n$. Then keep that same subscript attached to every quantity from that mode:

$$
\boxed{L=n\frac{\lambda_n}{2}},
\qquad
\boxed{\lambda_n=\frac{2L}{n}},
\qquad
\boxed{f_n=nf_1=\frac{nv}{2L}}.
$$

The harmonic number supplies a compact ledger:

| Description of mode $n$ | Count or relation |
|---|---:|
| half-wavelength segments, or loops | $n$ |
| antinodes | $n$ |
| total nodes, including both fixed ends | $n+1$ |
| overtone number | $n-1$ |

Thus, overtone number $q$ means harmonic number $n=q+1$ for a fixed-fixed string. One loop is one half-wavelength, not one full wavelength.

When a problem gives mode $k$ and asks about mode $n$, normalize to mode $1$ before changing the index:

| Given | Recover the fundamental | Move to mode $n$ |
|---|---:|---:|
| $f_k$ | $f_1=f_k/k$ | $f_n=nf_1$ |
| $\lambda_k$ | $\lambda_1=k\lambda_k$ | $\lambda_n=\lambda_1/n$ |

The same string has one wave speed $v$ in every mode. The product $f_n\lambda_n$ equals that speed only when the subscripts match. Do not multiply $f_n$ by $\lambda_m$ when $n\ne m$.

These rules apply to a string fixed at both ends. A pipe with one closed and one open end has a different allowed-mode and overtone map.

**Transcript correction.** The automatic captions for `qm1hDJrIYwE` and `-8nn8hb0H8o` use “standard wave” for **standing wave**; the latter also uses “knife harmonic” for **ninth harmonic**. The equations and surrounding examples identify the intended terms.

---

<a id="mode-ledger"></a>
## Build the Mode Ledger

Start by counting loops. Each loop runs from one node to the next and contains $\lambda_n/2$, so $n$ loops fit into the string as

$$
L=n\frac{\lambda_n}{2}.
$$

The two fixed endpoints count as nodes. That is why a mode with $n$ loops has $n+1$ total nodes rather than $n-1$.

### Source-video worked case — `-8nn8hb0H8o`, 00:13:38–00:14:37

The source shows five loops. Therefore,

$$
n=5,
\qquad
N_{\text{nodes}}=n+1=6,
\qquad
N_{\text{antinodes}}=n=5.
$$

```quiz
type: radio
id: mct-p17-mode-ledger
shuffle: true
content: |-
  A string fixed at both ends vibrates in its third overtone. Which description of the pattern is correct?
options:
- id: mct-p17-mode-ledger-a
  content: |-
    $n=4$, with $4$ loops, $5$ total nodes, and $4$ antinodes
  correct: true
  feedback: |-
    For a fixed-fixed string, overtone number $q$ maps to $n=q+1$. The third overtone is therefore $n=4$, and mode $4$ has four loops, four antinodes, and $4+1=5$ total nodes.
- id: mct-p17-mode-ledger-b
  content: |-
    $n=3$, with $3$ loops, $4$ total nodes, and $3$ antinodes
  feedback: |-
    This describes the third harmonic, which is the second overtone. Overtone counting starts above the fundamental, so the third overtone is harmonic $n=4$.
- id: mct-p17-mode-ledger-c
  content: |-
    $n=4$, with $4$ loops, $3$ total nodes, and $4$ antinodes
  feedback: |-
    The count $n-1=3$ gives interior nodes only. The question asks for total nodes, so include the two fixed endpoints: $3+2=5$.
- id: mct-p17-mode-ledger-d
  content: |-
    $n=4$, with $2$ loops, $5$ total nodes, and $2$ antinodes
  feedback: |-
    Four half-wavelength segments fit in mode $4$. Pairing two half-wavelengths into one full wavelength does not turn the pattern into two loops; each half-wavelength segment is one loop.
- id: mct-p17-mode-ledger-e
  content: |-
    $n=4$, with $4$ loops, $4$ total nodes, and $5$ antinodes
  feedback: |-
    This reverses the node and antinode counts. Mode $n$ has $n$ antinodes but $n+1$ total nodes because both fixed ends are nodes.
```

---

<a id="frequency-ladder"></a>
## Use the Frequency Ladder

For one fixed-fixed string, frequency varies directly with harmonic number:

$$
f_n=nf_1,
\qquad
\frac{f_n}{n}=f_1.
$$

If any harmonic frequency is known, divide by its subscript to recover $f_1$. Then multiply $f_1$ by the new subscript.

### Source-video worked case — `qm1hDJrIYwE`, 00:07:34–00:12:23

The source uses $v=130\ \mathrm{m/s}$ and $L=2.5\ \mathrm m$. The fundamental is

$$
f_1=\frac{v}{2L}
=\frac{130}{2(2.5)}
=26\ \mathrm{Hz}.
$$

The remaining requested quantities all follow from the mode ledger:

| Request | Mode translation | Result |
|---|---:|---:|
| third harmonic frequency | $n=3$ | $f_3=3(26)=78\ \mathrm{Hz}$ |
| nodes and antinodes in the third mode | $n=3$ | $4$ nodes and $3$ antinodes |
| fifth overtone frequency | $n=6$ | $f_6=6(26)=156\ \mathrm{Hz}$ |
| third overtone wavelength | $n=4$ | $\lambda_4=2(2.5)/4=1.25\ \mathrm m$ |

### Source-video worked cases — `-8nn8hb0H8o`, 00:14:46–00:17:28

With $f_1=175\ \mathrm{Hz}$, the first four harmonics are

$$
f_1=175,
\quad
f_2=350,
\quad
f_3=525,
\quad
f_4=700\ \mathrm{Hz}.
$$

In the next source case, $f_7=280\ \mathrm{Hz}$. Normalize to the fundamental first:

$$
f_1=\frac{f_7}{7}=40\ \mathrm{Hz}.
$$

Then

$$
f_4=4f_1=160\ \mathrm{Hz},
\qquad
f_9=9f_1=360\ \mathrm{Hz}.
$$

### M5-4 lecture ratio check

The lecture simulation gives

$$
f_1\approx0.44\ \mathrm{Hz},
\qquad
f_2\approx0.88\ \mathrm{Hz},
\qquad
f_3\approx1.32\ \mathrm{Hz}.
$$

The values obey $f_2=2f_1$ and $f_3=3f_1=\tfrac32f_2$, as the mode ratios require.

```quiz
type: radio
id: mct-p17-frequency-ladder
shuffle: true
content: |-
  A fixed-fixed string has $f_6=270\ \mathrm{Hz}$. What is its fourth-harmonic frequency?
options:
- id: mct-p17-frequency-ladder-a
  content: |-
    $180\ \mathrm{Hz}$
  correct: true
  feedback: |-
    Harmonic frequencies share the same base value $f_1$. Since $f_1=f_6/6=45\ \mathrm{Hz}$, the fourth harmonic is $f_4=4f_1=180\ \mathrm{Hz}$.
- id: mct-p17-frequency-ladder-b
  content: |-
    $45\ \mathrm{Hz}$
  feedback: |-
    Dividing $f_6$ by $6$ correctly finds the fundamental frequency $f_1=45\ \mathrm{Hz}$, but the question asks for $f_4$. Multiply that base value by $4$.
- id: mct-p17-frequency-ladder-c
  content: |-
    $1080\ \mathrm{Hz}$
  feedback: |-
    This treats the given $f_6$ as though it were $f_1$ and multiplies it by $4$. First remove the given subscript by dividing $270$ by $6$, then apply the new subscript $4$.
- id: mct-p17-frequency-ladder-d
  content: |-
    $405\ \mathrm{Hz}$
  feedback: |-
    The frequency ratio is $f_4/f_6=4/6$, not $6/4$. A lower harmonic number must have a lower frequency on the same string, so $f_4$ must be below $270\ \mathrm{Hz}$.
- id: mct-p17-frequency-ladder-e
  content: |-
    $67.5\ \mathrm{Hz}$
  feedback: |-
    Dividing the sixth-harmonic frequency by $4$ uses the requested index in the wrong step. Divide by the given index $6$ to find $f_1$, then multiply by the requested index $4$.
```

---

<a id="wavelength-ladder"></a>
## Use the Wavelength Ladder

Wavelength varies inversely with harmonic number:

$$
\lambda_n=\frac{\lambda_1}{n}=\frac{2L}{n},
\qquad
n\lambda_n=\lambda_1=2L.
$$

As $n$ rises, $f_n$ rises but $\lambda_n$ falls. The invariant $n\lambda_n=\lambda_1$ is the wavelength counterpart of $f_n/n=f_1$.

### Source-video worked cases — `-8nn8hb0H8o`, 00:22:37–00:24:50

For $\lambda_1=12\ \mathrm m$, division by the harmonic number gives

| Harmonic | $\lambda_n=\lambda_1/n$ |
|---:|---:|
| $1$ | $12\ \mathrm m$ |
| $2$ | $6\ \mathrm m$ |
| $3$ | $4\ \mathrm m$ |
| $4$ | $3\ \mathrm m$ |
| $5$ | $2.4\ \mathrm m$ |

In the next case, $\lambda_5=1.8\ \mathrm m$. Recover the fundamental wavelength and then change the subscript:

$$
\lambda_1=5\lambda_5=5(1.8)=9.0\ \mathrm m,
$$

$$
\lambda_9=\frac{\lambda_1}{9}=\frac{9.0}{9}=1.0\ \mathrm m.
$$

```quiz
type: radio
id: mct-p17-wavelength-ladder
shuffle: true
content: |-
  On one fixed-fixed string, $\lambda_4=1.5\ \mathrm m$. What is $\lambda_{10}$?
options:
- id: mct-p17-wavelength-ladder-a
  content: |-
    $0.60\ \mathrm m$
  correct: true
  feedback: |-
    The wavelength invariant is $n\lambda_n=\lambda_1$. Thus $\lambda_1=4(1.5)=6.0\ \mathrm m$, and $\lambda_{10}=6.0/10=0.60\ \mathrm m$.
- id: mct-p17-wavelength-ladder-b
  content: |-
    $3.75\ \mathrm m$
  feedback: |-
    This scales wavelength directly with harmonic number. Wavelength varies inversely with $n$, so moving from $n=4$ to $n=10$ must make the wavelength smaller, by a factor of $4/10$.
- id: mct-p17-wavelength-ladder-c
  content: |-
    $0.15\ \mathrm m$
  feedback: |-
    Dividing $\lambda_4$ directly by $10$ ignores that $1.5\ \mathrm m$ belongs to mode $4$, not mode $1$. First form $\lambda_1=4\lambda_4$, then divide by $10$.
- id: mct-p17-wavelength-ladder-d
  content: |-
    $6.0\ \mathrm m$
  feedback: |-
    This correctly finds the fundamental wavelength $\lambda_1=4\lambda_4$ but stops there. The tenth-harmonic wavelength is one tenth of that value.
- id: mct-p17-wavelength-ladder-e
  content: |-
    $15\ \mathrm m$
  feedback: |-
    Multiplying $\lambda_4$ by the requested index $10$ does not preserve $n\lambda_n$. The invariant requires $4\lambda_4=10\lambda_{10}$, which makes $\lambda_{10}$ smaller than $\lambda_4$.
```

---

<a id="one-mode-chain"></a>
## Carry One Mode Through Length, Wavelength, and Frequency

When the picture gives $n$ loops, keep $n$ attached through the chain

$$
n
\longrightarrow
\lambda_n=\frac{2L}{n}
\longrightarrow
f_n=\frac{v}{\lambda_n}
\longrightarrow
f_1=\frac{f_n}{n}.
$$

### Source-video worked case — `-8nn8hb0H8o`, 00:17:36–00:22:25

A $2.0\ \mathrm m$ string has three loops, and the wave speed is $45\ \mathrm{m/s}$. Three loops mean $n=3$, so

$$
\lambda_3=\frac{2L}{3}
=\frac{2(2.0)}{3}
=\frac43\ \mathrm m.
$$

Use the matching third-mode frequency:

$$
f_3=\frac{v}{\lambda_3}
=\frac{45}{4/3}
=33.75\ \mathrm{Hz}.
$$

Now normalize both mode quantities:

$$
f_1=\frac{f_3}{3}=11.25\ \mathrm{Hz},
\qquad
\lambda_1=3\lambda_3=4.0\ \mathrm m.
$$

The speed check agrees in either mode:

$$
f_3\lambda_3
=(33.75)\left(\frac43\right)
=45\ \mathrm{m/s},
$$

$$
f_1\lambda_1
=(11.25)(4.0)
=45\ \mathrm{m/s}.
$$

```quiz
type: radio
id: mct-p17-one-mode-chain
shuffle: true
content: |-
  A $1.8\ \mathrm m$ string fixed at both ends has four loops. Its wave speed is $72\ \mathrm{m/s}$. Which line gives the correct $\lambda_4$, $f_4$, and $f_1$?
options:
- id: mct-p17-one-mode-chain-a
  content: |-
    $\lambda_4=0.90\ \mathrm m$, $f_4=80\ \mathrm{Hz}$, and $f_1=20\ \mathrm{Hz}$
  correct: true
  feedback: |-
    Four loops mean $n=4$, and each loop is half a wavelength. Thus $\lambda_4=2L/4=0.90\ \mathrm m$, $f_4=v/\lambda_4=80\ \mathrm{Hz}$, and $f_1=f_4/4=20\ \mathrm{Hz}$.
- id: mct-p17-one-mode-chain-b
  content: |-
    $\lambda_4=0.90\ \mathrm m$, $f_4=20\ \mathrm{Hz}$, and $f_1=80\ \mathrm{Hz}$
  feedback: |-
    This swaps the mode frequency and the fundamental. The fourth harmonic is four times the fundamental, so $f_4$ must be the larger value: $80\ \mathrm{Hz}$ versus $20\ \mathrm{Hz}$.
- id: mct-p17-one-mode-chain-c
  content: |-
    $\lambda_4=0.45\ \mathrm m$, $f_4=160\ \mathrm{Hz}$, and $f_1=40\ \mathrm{Hz}$
  feedback: |-
    This treats each loop as a full wavelength. A loop is half a wavelength, so four loops satisfy $L=4\lambda_4/2$ and give $\lambda_4=0.90\ \mathrm m$, not $0.45\ \mathrm m$.
- id: mct-p17-one-mode-chain-d
  content: |-
    $\lambda_4=3.6\ \mathrm m$, $f_4=20\ \mathrm{Hz}$, and $f_1=5.0\ \mathrm{Hz}$
  feedback: |-
    The value $2L=3.6\ \mathrm m$ is $\lambda_1$, so $72/3.6=20\ \mathrm{Hz}$ is $f_1$, not $f_4$. For mode $4$, use $\lambda_4=\lambda_1/4=0.90\ \mathrm m$ and $f_4=4f_1=80\ \mathrm{Hz}$.
- id: mct-p17-one-mode-chain-e
  content: |-
    $\lambda_4=0.90\ \mathrm m$, $f_4=80\ \mathrm{Hz}$, and $f_1=320\ \mathrm{Hz}$
  feedback: |-
    The first two entries are correct, but this multiplies by $4$ when moving from $f_4$ to $f_1$. Since $f_4=4f_1$, recover the fundamental by dividing $80\ \mathrm{Hz}$ by $4$.
```

---

<a id="align-subscripts"></a>
## Align Subscripts Before Multiplying

The wave-speed equation applies within one mode:

$$
\boxed{v=f_n\lambda_n}.
$$

If the supplied subscripts differ, translate one or both quantities to a common harmonic before multiplying. The fundamental is often the simplest common mode.

### Source-video worked case — `-8nn8hb0H8o`, 00:36:39–00:40:05

The source gives

$$
f_4=300\ \mathrm{Hz},
\qquad
\lambda_2=2.3\ \mathrm m.
$$

The product $f_4\lambda_2$ is invalid because the subscripts do not match. Translate both quantities to mode $1$:

$$
f_1=\frac{f_4}{4}=75\ \mathrm{Hz},
\qquad
\lambda_1=2\lambda_2=4.6\ \mathrm m.
$$

Now the subscripts match, so

$$
v=f_1\lambda_1
=(75\ \mathrm{s^{-1}})(4.6\ \mathrm m)
=345\ \mathrm{m/s}.
$$

The same result follows in mode $4$: $\lambda_4=\lambda_1/4=1.15\ \mathrm m$, so $f_4\lambda_4=(300)(1.15)=345\ \mathrm{m/s}$.

```quiz
type: radio
id: mct-p17-align-subscripts
shuffle: true
content: |-
  On one fixed-fixed string, $f_3=240\ \mathrm{Hz}$ and $\lambda_6=0.80\ \mathrm m$. What is the wave speed?
options:
- id: mct-p17-align-subscripts-a
  content: |-
    $384\ \mathrm{m/s}$
  correct: true
  feedback: |-
    Match the mode labels before using $v=f\lambda$. Since $\lambda_3=(6/3)\lambda_6=1.60\ \mathrm m$, the speed is $v=f_3\lambda_3=(240)(1.60)=384\ \mathrm{m/s}$.
- id: mct-p17-align-subscripts-b
  content: |-
    $192\ \mathrm{m/s}$
  feedback: |-
    This is the mismatched product $f_3\lambda_6=(240)(0.80)$. Frequency $f_3$ must be paired with $\lambda_3$; converting the sixth-mode wavelength gives $\lambda_3=1.60\ \mathrm m$.
- id: mct-p17-align-subscripts-c
  content: |-
    $1152\ \mathrm{m/s}$
  feedback: |-
    This converts $\lambda_6$ to $\lambda_1=6(0.80)=4.8\ \mathrm m$ but still multiplies by $f_3$. Pair $\lambda_1$ with $f_1=240/3=80\ \mathrm{Hz}$, or pair $f_3$ with $\lambda_3$.
- id: mct-p17-align-subscripts-d
  content: |-
    $96\ \mathrm{m/s}$
  feedback: |-
    This makes wavelength decrease when moving from mode $6$ down to mode $3$. Lower harmonics have longer wavelengths, so $\lambda_3=(6/3)(0.80)=1.60\ \mathrm m$, not $0.40\ \mathrm m$.
- id: mct-p17-align-subscripts-e
  content: |-
    $80\ \mathrm{m/s}$
  feedback: |-
    The value $240/3=80$ is the fundamental frequency in hertz, not a speed. Multiply $f_1=80\ \mathrm{Hz}$ by the matching $\lambda_1=6(0.80)=4.8\ \mathrm m$ to obtain meters per second.
```

---

<a id="summary"></a>
## Summary

For a string fixed at both ends:

1. Translate the picture or wording into harmonic number $n$.
2. Use one loop $=\lambda_n/2$, so mode $n$ has $n$ loops, $n$ antinodes, and $n+1$ total nodes.
3. Convert overtone $q$ to harmonic $n=q+1$.
4. Use
   $$
   \lambda_n=\frac{2L}{n}=\frac{\lambda_1}{n},
   \qquad
   f_n=nf_1=\frac{nv}{2L}.
   $$
5. Before using $v=f\lambda$, make the subscripts match: $v=f_n\lambda_n$.

Quick direction check: higher $n$ means higher frequency and shorter wavelength, while the wave speed stays fixed for the same string. The main trap is combining quantities from different modes or treating overtone number as harmonic number.

<!-- lesson-nav:start -->
---

```update-progress
```

[[212/Home|Home]]
[[212/0. Table of Contents/TOC|Table of Contents]]

---
<!-- lesson-nav:end -->
