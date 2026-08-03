# Matching Fundamental Frequencies of Open and Closed Tubes

<!--
lesson-id: 212-M5-042
topic-code: MTH212.M5.42
-->

## Table of Contents

- [Introduction](#introduction)
- [Read the Fundamental Pattern](#read-the-fundamental-pattern)
- [Match the Frequencies](#match-the-frequencies)
- [Compress the Result to a Length Ratio](#compress-the-result-to-a-length-ratio)
- [Reverse the Comparison](#reverse-the-comparison)
- [Reject the Equal-Length Trap](#reject-the-equal-length-trap)
- [Summary](#summary)

## Prerequisites

- Use $v=f\lambda$ to relate wave speed, frequency, and wavelength.
- Solve a one-step equation containing fractions.

---

<a id="introduction"></a>
## Introduction

The recognition cue is a pair of tubes with **different end conditions** but the **same fundamental frequency**. In the ideal-tube model, use one short chain:

$$
\text{end conditions}
\longrightarrow
\text{fundamental formulas}
\longrightarrow
\text{equal frequencies}
\longrightarrow
\text{length ratio}.
$$

For sound traveling through the same air, both tubes have the same wave speed $v$:

| Tube | Fundamental pattern | Fundamental frequency |
| --- | --- | --- |
| Open at both ends | $\ell_{\mathrm{oo}}=\lambda/2$ | $f_{\mathrm{oo}}=\dfrac{v}{2\ell_{\mathrm{oo}}}$ |
| Closed at one end | $\ell_{\mathrm{co}}=\lambda/4$ | $f_{\mathrm{co}}=\dfrac{v}{4\ell_{\mathrm{co}}}$ |

The factors $2$ and $4$ come from the standing-wave patterns. Keep them attached to the correct tube. Because the tubes contain the same air, equal $f$ also means equal $\lambda$; their physical lengths differ because the two patterns fit different fractions of that common wavelength.

---

<a id="read-the-fundamental-pattern"></a>
## Read the Fundamental Pattern

**Example:** Find the fundamental wavelength in an open-open tube of length $0.80\ \mathrm{m}$ and in a closed-open tube of length $0.30\ \mathrm{m}$.

**Explanation**

An open-open tube contains half a wavelength in its fundamental:

$$
\ell_{\mathrm{oo}}=\frac{\lambda_{\mathrm{oo}}}{2}
\quad\Longrightarrow\quad
\lambda_{\mathrm{oo}}=2\ell_{\mathrm{oo}}
=2(0.80\ \mathrm{m})
=1.60\ \mathrm{m}.
$$

A closed-open tube contains one quarter of a wavelength:

$$
\ell_{\mathrm{co}}=\frac{\lambda_{\mathrm{co}}}{4}
\quad\Longrightarrow\quad
\lambda_{\mathrm{co}}=4\ell_{\mathrm{co}}
=4(0.30\ \mathrm{m})
=1.20\ \mathrm{m}.
$$

```quiz
type: radio
id: p2-pattern-check
content: |-
  An open-open tube is $0.60\ \mathrm{m}$ long, and a closed-open tube is $0.25\ \mathrm{m}$ long. What are their fundamental wavelengths, in that order?
options:
- id: p2-pattern-a
  content: |-
    $1.20\ \mathrm{m}$ and $1.00\ \mathrm{m}$
  correct: true
  feedback: |-
    An open-open fundamental fits half a wavelength, while a closed-open fundamental fits one quarter. Therefore $\lambda_{oo}=2(0.60)=1.20\ \mathrm{m}$ and $\lambda_{co}=4(0.25)=1.00\ \mathrm{m}$.
- id: p2-pattern-b
  content: |-
    $0.60\ \mathrm{m}$ and $0.25\ \mathrm{m}$
  feedback: |-
    A tube's length is only a fraction of its fundamental wavelength, not the whole wavelength. Here the open-open tube holds $\lambda/2$ and the closed-open tube holds $\lambda/4$, giving $1.20\ \mathrm{m}$ and $1.00\ \mathrm{m}$.
- id: p2-pattern-c
  content: |-
    $1.20\ \mathrm{m}$ and $0.50\ \mathrm{m}$
  feedback: |-
    $1.20\ \mathrm{m}$ correctly uses the half-wave pattern for the open-open tube. The closed-open tube instead holds a quarter wavelength, so its wavelength is $4(0.25)=1.00\ \mathrm{m}$, not $0.50\ \mathrm{m}$.
- id: p2-pattern-d
  content: |-
    $2.40\ \mathrm{m}$ and $1.00\ \mathrm{m}$
  feedback: |-
    $2.40\ \mathrm{m}$ treats the open-open tube as a quarter-wave resonator. Both ends are open, so its fundamental contains half a wavelength and $\lambda=2(0.60)=1.20\ \mathrm{m}$; the second value is correct.
- id: p2-pattern-e
  content: |-
    $0.30\ \mathrm{m}$ and $1.00\ \mathrm{m}$
  feedback: |-
    The closed-open value correctly uses $\lambda=4L$. For the open-open tube, $L=\lambda/2$ means $\lambda=2L=1.20\ \mathrm{m}$, not $L/2=0.30\ \mathrm{m}$.
```

---

<a id="match-the-frequencies"></a>
## Match the Frequencies

**Example:** An open-open tube is $1.20\ \mathrm{m}$ long. How long must a closed-open tube be to have the same fundamental frequency in the same air?

**Explanation**

Let the closed-open tube's length be $x$. Equal fundamental frequencies give

$$
\frac{v}{2(1.20\ \mathrm{m})}
=
\frac{v}{4x}.
$$

Cancel the common nonzero wave speed $v$:

$$
\frac{1}{2(1.20\ \mathrm{m})}
=
\frac{1}{4x}.
$$

Cross-multiply and isolate $x$:

$$
\begin{aligned}
4x&=2(1.20\ \mathrm{m}),\\
4x&=2.40\ \mathrm{m},\\
x&=0.60\ \mathrm{m}.
\end{aligned}
$$

The closed-open tube must be $0.60\ \mathrm{m}$ long.

```quiz
type: radio
id: p2-frequency-match
content: |-
  An open-open tube is $0.90\ \mathrm{m}$ long. A closed-open tube in the same air has the same fundamental frequency. What is the closed-open tube's length?
options:
- id: p2-match-a
  content: |-
    $0.225\ \mathrm{m}$
  feedback: |-
    The quarter-wave label describes the closed tube's fraction of the common wavelength, not its fraction of the open tube's length. Since $2L_{oo}=4L_{co}$, the matching closed-open length is $0.45\ \mathrm{m}$, not $0.225\ \mathrm{m}$.
- id: p2-match-b
  content: |-
    $0.45\ \mathrm{m}$
  correct: true
  feedback: |-
    Both tubes share the same sound speed, so equal frequency means equal wavelength. The patterns give $2L_{oo}=4L_{co}$, hence $L_{co}=0.90/2=0.45\ \mathrm{m}$.
- id: p2-match-c
  content: |-
    $0.90\ \mathrm{m}$
  feedback: |-
    Equal frequency in the same air fixes a common wavelength, not equal tube lengths. The open-open tube holds half that wavelength and the closed-open tube holds one quarter, so the latter must be $0.45\ \mathrm{m}$ long.
- id: p2-match-d
  content: |-
    $1.80\ \mathrm{m}$
  feedback: |-
    $1.80\ \mathrm{m}=2L_{oo}$ is the common wavelength. A closed-open fundamental occupies only one quarter of it, so its tube length is $1.80/4=0.45\ \mathrm{m}$.
- id: p2-match-e
  content: |-
    $3.60\ \mathrm{m}$
  feedback: |-
    The factor $4$ connects a closed tube's length to wavelength; it is not a multiplier between the two tube lengths. Equating the common wavelength gives $2(0.90)=4L_{co}$ and $L_{co}=0.45\ \mathrm{m}$.
```

---

<a id="compress-the-result-to-a-length-ratio"></a>
## Compress the Result to a Length Ratio

**Example:** An open-open tube has length $A$. Express the length $C$ of a closed-open tube with the same fundamental frequency.

**Explanation**

Start from the two fundamental-frequency formulas:

$$
\frac{v}{2A}=\frac{v}{4C}.
$$

Cancel $v$ and cross-multiply:

$$
\begin{aligned}
\frac{1}{2A}&=\frac{1}{4C},\\
4C&=2A,\\
C&=\frac{A}{2}.
\end{aligned}
$$

Thus, for equal fundamental frequencies in the same medium,

$$
\boxed{\ell_{\mathrm{co}}=\frac{\ell_{\mathrm{oo}}}{2}}.
$$

Equivalently,

$$
\boxed{\ell_{\mathrm{co}}:\ell_{\mathrm{oo}}=1:2}.
$$

This labeled ratio is a quick direction check: the closed-open tube must be the shorter one.

```quiz
type: radio
id: p2-original-check
shuffle: true
content: |-
  A tube of length $L$ is open at both ends.

  A second tube is closed at one end and open at the other.

  The second tube has the same fundamental frequency as the first tube.

  What is the length of the second tube?
options:
- id: p2-original-a
  content: |-
    $L/4$
  feedback: |-
    $L/4$ treats the open tube's physical length as though it were the common wavelength. The open-open pattern gives $\lambda=2L$, so the closed-open length is $\lambda/4=L/2$.
- id: p2-original-b
  content: |-
    $L/2$
  correct: true
  feedback: |-
    Equal frequency in the same medium means both tubes use the same wavelength. Since the open-open tube has $L=\lambda/2$ and the closed-open tube has $L_{co}=\lambda/4$, the second tube is $L/2$ long.
- id: p2-original-c
  content: |-
    $L$
  feedback: |-
    The two end conditions fit different fractions of a wavelength into a tube. If their lengths were both $L$, the closed-open fundamental would be half the open-open frequency; matching frequencies instead requires $L_{co}=L/2$.
- id: p2-original-d
  content: |-
    $2L$
  feedback: |-
    A closed-open fundamental needs only a quarter wavelength, whereas the open-open tube needs a half wavelength. For the same wavelength, the closed-open tube is half as long, $L/2$, not twice as long.
- id: p2-original-e
  content: |-
    $4L$
  feedback: |-
    The $4$ in $f_{co}=v/(4L_{co})$ is tied to the quarter-wave pattern; it does not make the closed tube four times longer. Equal frequencies give $4L_{co}=2L$, so $L_{co}=L/2$.
```

---

<a id="reverse-the-comparison"></a>
## Reverse the Comparison

**Example:** A closed-open tube is $0.35\ \mathrm{m}$ long. Find the length of an open-open tube with the same fundamental frequency.

**Explanation**

Keep the tube labels attached to the ratio:

$$
\ell_{\mathrm{co}}:\ell_{\mathrm{oo}}=1:2.
$$

This time the open-open length is unknown, so the second part of the ratio is twice the first:

$$
\begin{aligned}
\ell_{\mathrm{oo}}&=2\ell_{\mathrm{co}},\\
\ell_{\mathrm{oo}}&=2(0.35\ \mathrm{m}),\\
\ell_{\mathrm{oo}}&=0.70\ \mathrm{m}.
\end{aligned}
$$

```quiz
type: radio
id: p2-reverse-check
content: |-
  A closed-open tube is $0.48\ \mathrm{m}$ long. How long must an open-open tube be to have the same fundamental frequency in the same air?
options:
- id: p2-reverse-a
  content: |-
    $0.12\ \mathrm{m}$
  feedback: |-
    Dividing by $4$ reverses the quarter-wave relationship. The closed-open tube's common wavelength is $4(0.48)=1.92\ \mathrm{m}$, so the matching open-open length is half of that, $0.96\ \mathrm{m}$.
- id: p2-reverse-b
  content: |-
    $0.24\ \mathrm{m}$
  feedback: |-
    For a common wavelength, the open-open tube holds $\lambda/2$ while the closed-open tube holds only $\lambda/4$. The open-open tube must therefore be twice, not half, the closed tube's length: $0.96\ \mathrm{m}$.
- id: p2-reverse-c
  content: |-
    $0.48\ \mathrm{m}$
  feedback: |-
    Equal frequency fixes the wavelength, but different endpoint patterns require different lengths. A matching open-open tube must be twice the $0.48\ \mathrm{m}$ closed-open length, so it is $0.96\ \mathrm{m}$.
- id: p2-reverse-d
  content: |-
    $0.96\ \mathrm{m}$
  correct: true
  feedback: |-
    The closed-open fundamental sets the common wavelength to $\lambda=4(0.48)=1.92\ \mathrm{m}$. The open-open tube holds half that wavelength, so its length is $0.96\ \mathrm{m}$.
- id: p2-reverse-e
  content: |-
    $1.92\ \mathrm{m}$
  feedback: |-
    $1.92\ \mathrm{m}$ is the wavelength obtained from the closed-open tube. An open-open fundamental fits half of that wavelength inside the tube, giving a length of $0.96\ \mathrm{m}$.
```

---

<a id="reject-the-equal-length-trap"></a>
## Reject the Equal-Length Trap

**Example:** An open-open tube and a closed-open tube both have length $L$. Do they have the same fundamental frequency?

**Explanation**

Their fundamental frequencies are

$$
f_{\mathrm{oo}}=\frac{v}{2L}
\qquad\text{and}\qquad
f_{\mathrm{co}}=\frac{v}{4L}.
$$

Therefore,

$$
f_{\mathrm{co}}=\frac{1}{2}f_{\mathrm{oo}}.
$$

Equal physical lengths do **not** produce equal fundamentals when the end conditions differ. For equal frequencies in the same air, the wavelength is the same, but the open-open tube holds half of it while the closed-open tube holds only one quarter of it.

```quiz
type: radio
id: p2-trap-check
content: |-
  Why is a closed-open tube half as long as an open-open tube when their fundamental frequencies are equal in the same air?
options:
- id: p2-trap-a
  content: |-
    Sound travels twice as fast in the closed-open tube.
  feedback: |-
    Sound speed is set by the medium, and both tubes contain the same air. Their lengths differ because the open-open fundamental fits $\lambda/2$ while the closed-open fundamental fits $\lambda/4$.
- id: p2-trap-b
  content: |-
    Equal frequencies require equal physical tube lengths.
  feedback: |-
    Equal frequency and equal sound speed do not force equal lengths; they force equal wavelengths through $v=f\lambda$. The endpoint conditions then make the open tube contain $\lambda/2$ and the closed tube $\lambda/4$.
- id: p2-trap-c
  content: |-
    The open-open tube holds half of the common wavelength, while the closed-open tube holds one quarter.
  correct: true
  feedback: |-
    Equal frequency in the same air gives a common wavelength. The open-open fundamental contains half of it and the closed-open fundamental contains one quarter, so $L_{co}=L_{oo}/2$.
- id: p2-trap-d
  content: |-
    The open-open tube holds one quarter of the wavelength, while the closed-open tube holds one half.
  feedback: |-
    The fractions are reversed. Antinodes at both open ends produce the half-wave fundamental, while one closed end and one open end produce the quarter-wave fundamental; therefore the closed-open tube is shorter.
- id: p2-trap-e
  content: |-
    Closing one end doubles the wavelength without changing either tube's length.
  feedback: |-
    Closing one end of a fixed-length tube does change its fundamental wavelength, but this question instead adjusts the second tube's length to keep $f$ and $\lambda$ unchanged. The required length ratio comes from $\lambda/4$ versus $\lambda/2$.
```

---

<a id="summary"></a>
## Summary

When two tubes in the same medium have equal fundamental frequencies:

1. Identify the end conditions.
2. Write $f_{\mathrm{oo}}=v/(2\ell_{\mathrm{oo}})$ and $f_{\mathrm{co}}=v/(4\ell_{\mathrm{co}})$.
3. Set the frequencies equal and cancel the common wave speed.
4. Solve to get

$$
\boxed{\ell_{\mathrm{co}}=\frac{\ell_{\mathrm{oo}}}{2}}.
$$

In ratio form, $\ell_{\mathrm{co}}:\ell_{\mathrm{oo}}=1:2$. The main trap is setting the physical lengths equal. Equal frequency and equal wave speed give the same wavelength, but the two boundary conditions fit different fractions of that wavelength into the tubes.

<!-- lesson-nav:start -->
---

```update-progress
```

[[212/Home|Home]]
[[212/0. Table of Contents/TOC|Table of Contents]]

[Quiz 3 Study Guide](../../2026-08-03-Q-3/Study-Guide.md)
Next: [Third Harmonic of an Open–Closed Pipe](../../2026-07-29-M5-4/Lessons/Problem-4.md)

Study guide index: 24/28

---
<!-- lesson-nav:end -->
