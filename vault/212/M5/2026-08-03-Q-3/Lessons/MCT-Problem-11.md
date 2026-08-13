# Convert Light Speed and Wavelength with Refractive Index

<!--
lesson-id: 212-M5-069
topic-code: MTH212.M5.69
-->

## Table of Contents

- [Introduction](#introduction)
- [Choose the Form of the Invariant](#choose-form)
- [Source-Video Speed and Index Cases](#source-speed-index)
- [Source-Video Vacuum-to-Glass Wavelength](#source-vacuum-glass)
- [Source-Video Glass-to-Diamond Wavelength](#source-glass-diamond)
- [Lecture Wavelength Ranking](#lecture-ranking)
- [Lecture Count Wavelengths in a Slide](#lecture-slide)
- [Summary](#summary)

## Prerequisites

- Use $v=f\lambda$ for a wave.
- Rearrange a one-step equation to isolate the requested variable.
- Divide numbers in scientific notation.
- Convert between nanometers and millimeters.

---

<a id="introduction"></a>
## Introduction

When the same light crosses from one medium into another, its frequency remains fixed by the source:

$$
f_1=f_2.
$$

The medium changes the light's speed. Because $v=f\lambda$, the wavelength changes with that speed. Refractive index records the speed change:

$$
n=\frac{c}{v},
$$

where $c=3.00\times10^8\ \mathrm{m/s}$ is the speed of light in vacuum. Combining these relations gives two constant products for the same light:

$$
\boxed{nv=c},
\qquad
\boxed{n\lambda=\frac{c}{f}}.
$$

Across a boundary, therefore,

$$
\boxed{n_1\lambda_1=n_2\lambda_2}.
$$

The comparison should be predicted before calculating:

| If refractive index... | Speed... | Wavelength... | Frequency... |
|---|---|---|---|
| increases | decreases | decreases | stays fixed |
| decreases | increases | increases | stays fixed |

Use these relations to convert speed, refractive index, and wavelength. Ray angles require Snell's law and are outside this lesson.

---

<a id="choose-form"></a>
## Choose the Form of the Invariant

Match the equation to the requested quantity before inserting numbers.

| Requested quantity | Use | Quick check |
|---|---|---|
| speed $v$ in one medium | $v=c/n$ | $n>1$ gives $v<c$ |
| refractive index $n$ | $n=c/v$ | the speed units cancel, so $n$ has no units |
| wavelength in medium 2 | $\lambda_2=(n_1/n_2)\lambda_1$ | larger $n_2$ gives shorter $\lambda_2$ |

The wavelength ratio is dimensionless. If $\lambda_1$ is entered in nanometers, $\lambda_2$ comes out in nanometers without converting to meters. Keep the medium labels attached to each index and wavelength; reversing one ratio reverses the physical trend.

For a two-medium wavelength problem, write one row per medium before solving:

| Medium | Index | Wavelength | Constant product |
|---|---:|---:|---:|
| 1 | $n_1$ | $\lambda_1$ | $n_1\lambda_1$ |
| 2 | $n_2$ | $\lambda_2$ | $n_2\lambda_2$ |

Set the last-column entries equal, then isolate the requested wavelength. This layout prevents an index from being paired with the other medium's wavelength.

---

<a id="source-speed-index"></a>
## Source-Video Speed and Index Cases

### Source-video worked case — `ohQheheySDw`, 00:00:12–00:01:13

Water has refractive index $n=1.33$. Since the unknown is speed, use $v=c/n$:

$$
\begin{aligned}
v_{\mathrm{water}}
&=\frac{3.00\times10^8\ \mathrm{m/s}}{1.33}\\
&=2.256\times10^8\ \mathrm{m/s}.
\end{aligned}
$$

The result is below $c$, as a value $n>1$ requires.

**Wording correction.** Near the end of this segment, the value “one” refers to the refractive index of vacuum, not to a speed. The correct statements are $n_{\mathrm{vac}}=1$ and $c=3.00\times10^8\ \mathrm{m/s}$.

### Source-video worked case — `ohQheheySDw`, 00:01:16–00:02:20

Light travels through diamond at

$$
v_{\mathrm{diamond}}=1.24\times10^8\ \mathrm{m/s}.
$$

Now the unknown is the index, so isolate $n$:

$$
\begin{aligned}
n_{\mathrm{diamond}}
&=\frac{c}{v_{\mathrm{diamond}}}\\
&=\frac{3.00\times10^8}{1.24\times10^8}\\
&=2.419\ldots\approx2.42.
\end{aligned}
$$

The matching powers of ten and speed units cancel. Refractive index is dimensionless.

```quiz
type: radio
id: mct-p11-speed-index
shuffle: true
content: |-
  Light travels at $2.00\times10^8\ \mathrm{m/s}$ in a transparent medium. Using $c=3.00\times10^8\ \mathrm{m/s}$, what is the medium's refractive index?
options:
- id: mct-p11-speed-index-a
  content: |-
    $n=1.50$
  correct: true
  feedback: |-
    Refractive index compares vacuum speed with material speed, so $n=c/v=(3.00\times10^8)/(2.00\times10^8)=1.50$. The speed units and matching powers of ten cancel, leaving a dimensionless index.
- id: mct-p11-speed-index-b
  content: |-
    $n=0.667$
  feedback: |-
    This reverses the ratio and computes $v/c$. The definition is $n=c/v$; here $v<c$, so $c/v$ must be greater than $1$, not $0.667$.
- id: mct-p11-speed-index-c
  content: |-
    $n=6.00\times10^{16}$
  feedback: |-
    This multiplies the two speeds. Refractive index is a speed ratio, $c/v$, so the units must cancel rather than multiply to $\mathrm{m^2/s^2}$.
- id: mct-p11-speed-index-d
  content: |-
    $n=1.50\ \mathrm{m/s}$
  feedback: |-
    The numerical ratio is right, but refractive index has no units because it divides one speed by another. The result is $n=1.50$, not a speed.
- id: mct-p11-speed-index-e
  content: |-
    $n=2.00$
  feedback: |-
    The coefficient $2.00$ belongs to the given material speed; it is not the index. Divide the vacuum-speed coefficient by it: $3.00/2.00=1.50$.
```

---

<a id="source-vacuum-glass"></a>
## Source-Video Vacuum-to-Glass Wavelength

### Source-video worked case — `ohQheheySDw`, 00:02:23–00:03:14

Light with vacuum wavelength $600\ \mathrm{nm}$ enters glass with $n_{\mathrm{glass}}=1.5$. Use $n_{\mathrm{vac}}=1$ and the constant product $n\lambda$:

$$
n_{\mathrm{vac}}\lambda_{\mathrm{vac}}
=n_{\mathrm{glass}}\lambda_{\mathrm{glass}}.
$$

Therefore,

$$
\begin{aligned}
\lambda_{\mathrm{glass}}
&=\frac{n_{\mathrm{vac}}}{n_{\mathrm{glass}}}\lambda_{\mathrm{vac}}\\
&=\frac{1}{1.5}(600\ \mathrm{nm})\\
&=400\ \mathrm{nm}.
\end{aligned}
$$

The index increased from $1$ to $1.5$, so the shorter wavelength is the expected direction. The frequency, not the wavelength, remains unchanged at the boundary.

```quiz
type: radio
id: mct-p11-vacuum-medium
shuffle: true
content: |-
  Light has wavelength $540\ \mathrm{nm}$ in vacuum and enters a medium with $n=1.80$. What is its wavelength in the medium?
options:
- id: mct-p11-vacuum-medium-a
  content: |-
    $300\ \mathrm{nm}$
  correct: true
  feedback: |-
    The same light keeps its frequency, so $n\lambda$ is constant. With $n_{\mathrm{vac}}=1$, $\lambda=(1/1.80)(540\ \mathrm{nm})=300\ \mathrm{nm}$, shorter than the vacuum wavelength as the larger index requires.
- id: mct-p11-vacuum-medium-b
  content: |-
    $972\ \mathrm{nm}$
  feedback: |-
    This multiplies the vacuum wavelength by $1.80$. A higher index means lower speed, and fixed frequency then means a shorter wavelength; divide by $1.80$ instead of multiplying.
- id: mct-p11-vacuum-medium-c
  content: |-
    $540\ \mathrm{nm}$
  feedback: |-
    Frequency stays fixed at the interface, but wavelength does not. Since the speed falls by the factor $1/1.80$, the wavelength also falls to $300\ \mathrm{nm}$.
- id: mct-p11-vacuum-medium-d
  content: |-
    $167\ \mathrm{nm}$
  feedback: |-
    This applies the index reduction twice by dividing by $1.80^2$. The single invariant $n_{\mathrm{vac}}\lambda_{\mathrm{vac}}=n\lambda$ requires only one factor of $1/1.80$.
- id: mct-p11-vacuum-medium-e
  content: |-
    $1.80\ \mathrm{nm}$
  feedback: |-
    The refractive index is a dimensionless scale factor, not a wavelength. It must act on the given $540\ \mathrm{nm}$ through $\lambda=540/1.80=300\ \mathrm{nm}$.
```

---

<a id="source-glass-diamond"></a>
## Source-Video Glass-to-Diamond Wavelength

### Source-video worked case — `ohQheheySDw`, 00:03:18–00:05:04

The same light has wavelength $450\ \mathrm{nm}$ in glass, where $n_g=1.5$, and then enters diamond, where $n_d=2.42$. Both starting and ending media matter:

$$
n_g\lambda_g=n_d\lambda_d.
$$

Solve symbolically before substituting:

$$
\begin{aligned}
\lambda_d
&=\frac{n_g}{n_d}\lambda_g\\
&=\frac{1.5}{2.42}(450\ \mathrm{nm})\\
&=278.9\ldots\ \mathrm{nm}\\
&\approx279\ \mathrm{nm}.
\end{aligned}
$$

Because $n_d>n_g$, the result must be below $450\ \mathrm{nm}$. Dividing only by $n_d$ would incorrectly treat the given glass wavelength as though it were a vacuum wavelength.

```quiz
type: radio
id: mct-p11-medium-medium
shuffle: true
content: |-
  The wavelength of light in medium $A$ is $520\ \mathrm{nm}$. The indices are $n_A=1.30$ and $n_B=2.00$. What is the wavelength of the same light in medium $B$?
options:
- id: mct-p11-medium-medium-a
  content: |-
    $338\ \mathrm{nm}$
  correct: true
  feedback: |-
    Frequency stays fixed, so $n_A\lambda_A=n_B\lambda_B$. Thus $\lambda_B=(1.30/2.00)(520\ \mathrm{nm})=338\ \mathrm{nm}$, shorter because medium $B$ has the larger index.
- id: mct-p11-medium-medium-b
  content: |-
    $800\ \mathrm{nm}$
  feedback: |-
    This reverses the index ratio and uses $n_B/n_A$. Since $n_B>n_A$, the wavelength must decrease, so use $n_A/n_B$ to obtain $338\ \mathrm{nm}$.
- id: mct-p11-medium-medium-c
  content: |-
    $260\ \mathrm{nm}$
  feedback: |-
    This divides $520\ \mathrm{nm}$ by $n_B$ and silently treats the starting wavelength as a vacuum value. It is already the wavelength in medium $A$, so the numerator must include $n_A=1.30$.
- id: mct-p11-medium-medium-d
  content: |-
    $400\ \mathrm{nm}$
  feedback: |-
    This divides by the starting index $n_A$ but never uses the destination index $n_B$. A two-medium conversion must keep the paired products equal: $n_A\lambda_A=n_B\lambda_B$.
- id: mct-p11-medium-medium-e
  content: |-
    $520\ \mathrm{nm}$
  feedback: |-
    The light source fixes frequency, not wavelength. The larger index lowers the speed in medium $B$, so $v=f\lambda$ requires the wavelength to fall from $520\ \mathrm{nm}$ to $338\ \mathrm{nm}$.
```

---

<a id="lecture-ranking"></a>
## Lecture Wavelength Ranking

### M5-2 lecture worked case

The lecture shows a snapshot of the same-frequency light in media $A$, $B$, and $C$. Medium $B$ has the shortest wavelength, medium $A$ has the intermediate wavelength, and medium $C$ has the longest:

$$
\lambda_B<\lambda_A<\lambda_C.
$$

For the same light, $n\lambda$ is constant. The index order is therefore reversed:

$$
\boxed{n_B>n_A>n_C}.
$$

Medium $B$ also has the lowest speed, while medium $C$ has the highest. No numerical wavelength is needed to rank the indices.

```quiz
type: radio
id: mct-p11-rank-media
shuffle: true
content: |-
  A snapshot shows the same light in three media. The wavelengths are $\lambda_P=420\ \mathrm{nm}$, $\lambda_Q=310\ \mathrm{nm}$, and $\lambda_R=570\ \mathrm{nm}$. Which index ranking is correct?
options:
- id: mct-p11-rank-media-a
  content: |-
    $n_Q>n_P>n_R$
  correct: true
  feedback: |-
    For the same frequency, $n\lambda$ is constant, so index order is the reverse of wavelength order. Since $310<420<570$, the indices satisfy $n_Q>n_P>n_R$.
- id: mct-p11-rank-media-b
  content: |-
    $n_R>n_P>n_Q$
  feedback: |-
    This copies the wavelength order into the index order. Index and wavelength vary inversely for the same light, so the longest wavelength in $R$ corresponds to the smallest index.
- id: mct-p11-rank-media-c
  content: |-
    $n_P>n_Q>n_R$
  feedback: |-
    This correctly places $R$ last but swaps $P$ and $Q$. Medium $Q$ has the shorter wavelength, so it must have the larger index: $n_Q>n_P$.
- id: mct-p11-rank-media-d
  content: |-
    $n_Q>n_R>n_P$
  feedback: |-
    This correctly places $Q$ first but reverses the remaining pair. Since $\lambda_P<\lambda_R$, inverse ordering gives $n_P>n_R$.
- id: mct-p11-rank-media-e
  content: |-
    $n_P=n_Q=n_R$
  feedback: |-
    The frequency is common to all three media, but their wavelengths differ. With $n\lambda=c/f$, different wavelengths require different indices.
```

---

<a id="lecture-slide"></a>
## Lecture Count Wavelengths in a Slide

### Original M5-2 lecture worked case

Orange light has $\lambda_{\mathrm{air}}=650\ \mathrm{nm}$, with $n_{\mathrm{air}}=1.0$ and $n_{\mathrm{glass}}=1.5$. Its wavelength inside the glass is

$$
\lambda_{\mathrm{glass}}
=\frac{n_{\mathrm{air}}}{n_{\mathrm{glass}}}\lambda_{\mathrm{air}}
=\frac{1.0}{1.5}(650\ \mathrm{nm})
=433.3\ldots\ \mathrm{nm}.
$$

The original lecture slide uses a width of $1.4\ \mathrm{mm}$. Convert that width to the same unit as the wavelength:

$$
1.4\ \mathrm{mm}=1.4\times10^6\ \mathrm{nm}.
$$

Using capital $N$ for the number of wavelengths, so it is not confused with refractive index $n$,

$$
\begin{aligned}
N
&=\frac{w}{\lambda_{\mathrm{glass}}}\\
&=\frac{1.4\times10^6\ \mathrm{nm}}{433.3\ldots\ \mathrm{nm}}\\
&=3230.8\ldots\\
&\approx3.23\times10^3.
\end{aligned}
$$

Thus about $3230$ wavelengths fit across the original slide width.

**Source reconciliation.** The cleaned `M5-2-LEC.md` variant uses a slide thickness of $1.2\ \mathrm{mm}$ instead. With the same $433.3\ldots\ \mathrm{nm}$ glass wavelength, that version gives

$$
N=2769.2\ldots\approx2.8\times10^3,
$$

entered as `2800`. The values $3230$ and $2800$ belong to different slide widths; neither should be paired with the other's thickness.

```quiz
type: radio
id: mct-p11-count-wavelengths
shuffle: true
content: |-
  Light has wavelength $500\ \mathrm{nm}$ in air. It enters glass with $n=1.25$. How many wavelengths fit across a $0.80\ \mathrm{mm}$ thickness of glass?
options:
- id: mct-p11-count-wavelengths-a
  content: |-
    $2000$ wavelengths
  correct: true
  feedback: |-
    The fixed frequency gives $\lambda_{\mathrm{glass}}=500/1.25=400\ \mathrm{nm}$. Since $0.80\ \mathrm{mm}=8.0\times10^5\ \mathrm{nm}$, the count is $N=(8.0\times10^5)/400=2000$ wavelengths.
- id: mct-p11-count-wavelengths-b
  content: |-
    $1600$ wavelengths
  feedback: |-
    This divides the width by the air wavelength and ignores the wavelength compression in glass. The glass wavelength is $400\ \mathrm{nm}$, so more than $1600$ cycles fit in the same width.
- id: mct-p11-count-wavelengths-c
  content: |-
    $1280$ wavelengths
  feedback: |-
    This lengthens the wavelength to $625\ \mathrm{nm}$ by multiplying by the index. A higher index lowers speed and shortens wavelength; divide $500\ \mathrm{nm}$ by $1.25$ before counting.
- id: mct-p11-count-wavelengths-d
  content: |-
    $400$ wavelengths
  feedback: |-
    The number $400$ is the wavelength in glass measured in nanometers, not the number of wavelengths. Divide the slide width, in nanometers, by that wavelength to obtain the dimensionless count.
- id: mct-p11-count-wavelengths-e
  content: |-
    $2.0$ wavelengths
  feedback: |-
    This divides $0.80$ by $0.400$ while leaving the numerator in millimeters and the denominator in micrometers. Convert both lengths to the same unit; $0.80\ \mathrm{mm}=800\ \mathrm{\mu m}$, not $0.80\ \mathrm{\mu m}$.
```

---

<a id="summary"></a>
## Summary

For the same light crossing a boundary:

1. Hold frequency fixed: $f_1=f_2$.
2. Identify the unknown before choosing a form:
   $$
   v=\frac{c}{n},
   \qquad
   n=\frac{c}{v},
   \qquad
   n_1\lambda_1=n_2\lambda_2.
   $$
3. Predict the direction: larger $n$ means lower $v$ and shorter $\lambda$.
4. Keep every index paired with its medium and isolate the unknown symbolically before substituting.
5. Check units: $n$ and wavelength counts are dimensionless; wavelength units survive an index ratio; lengths must share a unit before counting cycles.

The main trap is holding wavelength fixed because frequency is fixed. The correct chain is that the medium changes speed, fixed frequency then changes wavelength, and $n\lambda$ remains constant.

<!-- lesson-nav:start -->
---

```update-progress
```

[[212/Home|Home]]
[[212/0. Table of Contents/TOC|Table of Contents]]

---
<!-- lesson-nav:end -->
