# Ranking Index of Refraction From Wavelength

<!--
lesson-id: 212-M5-012
topic-code: MTH212.M5.12
-->

## Table of Contents

- [Introduction](#introduction)
- [Use Constant Frequency to Rank Wave Speeds](#use-constant-frequency-to-rank-wave-speeds)
- [Reverse the Speed Order to Rank Refractive Index](#reverse-the-speed-order-to-rank-refractive-index)
- [Combine the Two Relationships](#combine-the-two-relationships)
- [Read Wavelength From a Snapshot](#read-wavelength-from-a-snapshot)
- [Apply the Chain to Media A, B, and C](#apply-the-chain-to-media-a-b-and-c)
- [Variant: A Different Medium Order](#variant-a-different-medium-order)
- [Summary](#summary)

## Prerequisites

- Compare wavelengths by the spacing between repeating wave features.
- Use $v=f\lambda$ to relate wave speed, frequency, and wavelength.
- Use $n=c/v$ to relate light speed in a medium to its index of refraction.

---

<a id="introduction"></a>
## Introduction

When the same-frequency light wave travels through several media, rank the wavelengths first and then carry that order through two relationships:

$$
v=f\lambda
\qquad\text{and}\qquad
n=\frac{c}{v}.
$$

Because $f$ is the same in every medium, speed $v$ changes in the **same** direction as wavelength $\lambda$. Because $n=c/v$, refractive index $n$ changes in the **opposite** direction from speed.

Therefore, for the same frequency,

$$
\text{shortest }\lambda
\longrightarrow
\text{smallest }v
\longrightarrow
\text{largest }n.
$$

The recognition cue is a snapshot or description that compares wavelength across media while explicitly keeping frequency fixed.

| Role in the problem | Quantity |
|---|---|
| Held fixed across the media | Frequency $f$ |
| Read from the snapshot | Wavelength $\lambda$ |
| Inferred with $v=f\lambda$ | Wave speed $v$ |
| Requested comparison | Refractive index $n$ |

---

<a id="use-constant-frequency-to-rank-wave-speeds"></a>
## Use Constant Frequency to Rank Wave Speeds

**Example:** The same-frequency wave has wavelength $2\ \mathrm{cm}$ in medium $P$ and $5\ \mathrm{cm}$ in medium $Q$. In which medium is the wave speed smaller?

**Explanation**

Since the frequency is the same,

$$
\frac{v_P}{v_Q}
=\frac{f\lambda_P}{f\lambda_Q}
=\frac{\lambda_P}{\lambda_Q}
=\frac{2}{5}.
$$

Thus $v_P<v_Q$. At fixed frequency, the shorter wavelength belongs to the smaller wave speed.

```quiz
type: radio
id: problem-5-speed-q1
content: |-
  A same-frequency wave has a shorter wavelength in medium $X$ than in medium $Y$. How do the wave speeds compare?
options:
- id: a
  content: |-
    $v_X<v_Y$
  correct: true
  feedback: |-
    With frequency fixed, $v=f\lambda$, so the shorter wavelength gives the smaller speed.
- id: b
  content: |-
    $v_X>v_Y$
  feedback: |-
    At the same frequency, speed and wavelength change in the same direction.
- id: c
  content: |-
    $v_X=v_Y$
  feedback: |-
    Equal frequencies do not imply equal speeds when the wavelengths differ.
```

---

<a id="reverse-the-speed-order-to-rank-refractive-index"></a>
## Reverse the Speed Order to Rank Refractive Index

**Example:** Light travels more slowly in medium $R$ than in medium $S$. Which medium has the larger index of refraction?

**Explanation**

The index of refraction is

$$
n=\frac{c}{v}.
$$

The vacuum speed $c$ is fixed, so a smaller medium speed $v$ gives a larger index $n$. Because $v_R<v_S$, the index order reverses:

$$
n_R>n_S.
$$

```quiz
type: radio
id: problem-5-index-q1
content: |-
  Light travels faster in medium $M$ than in medium $N$. Which comparison of refractive indices is correct?
options:
- id: a
  content: |-
    $n_M>n_N$
  feedback: |-
    Refractive index varies inversely with speed.
- id: b
  content: |-
    $n_M<n_N$
  correct: true
  feedback: |-
    Since $n=c/v$, the medium with the greater speed has the smaller index.
- id: c
  content: |-
    $n_M=n_N$
  feedback: |-
    Different light speeds correspond to different refractive indices.
```

---

<a id="combine-the-two-relationships"></a>
## Combine the Two Relationships

**Example:** A same-frequency wave has the shortest wavelength in medium $R$, an intermediate wavelength in medium $P$, and the longest wavelength in medium $Q$. Rank the indices of refraction.

**Explanation**

At fixed frequency,

$$
\lambda_R<\lambda_P<\lambda_Q
\quad\Longrightarrow\quad
v_R<v_P<v_Q.
$$

The index relation reverses the speed order:

$$
n_R>n_P>n_Q.
$$

Equivalently, substitute $v=f\lambda$ into $n=c/v$:

$$
n=\frac{c}{f\lambda}.
$$

When $c$ and $f$ are fixed, $n$ is inversely proportional to $\lambda$.

**Watch Out!** Do not use $n\propto1/\lambda$ without the same-frequency condition. The general chain uses both $v=f\lambda$ and $n=c/v$.

```quiz
type: radio
id: problem-5-ranking-q1
content: |-
  A same-frequency wave has wavelengths ordered as $\lambda_U>\lambda_V>\lambda_W$. Which index ordering is correct?
options:
- id: a
  content: |-
    $n_U>n_V>n_W$
  feedback: |-
    Index and wavelength have opposite orders when frequency is fixed.
- id: b
  content: |-
    $n_U<n_V<n_W$
  correct: true
  feedback: |-
    The shortest wavelength in $W$ gives the smallest speed and largest index.
- id: c
  content: |-
    $n_U=n_V=n_W$
  feedback: |-
    Equal frequency does not produce equal index when wavelengths differ.
```

---

<a id="read-wavelength-from-a-snapshot"></a>
## Read Wavelength From a Snapshot

**Example:** In a wave snapshot, the repeating crests are packed closest together in medium $D$ and farthest apart in medium $E$. Which medium has the larger refractive index?

**Explanation**

Wavelength is the distance between matching neighboring features such as crest to crest. Closest spacing means $\lambda_D<\lambda_E$.

For the same-frequency wave,

$$
\lambda_D<\lambda_E
\longrightarrow
v_D<v_E
\longrightarrow
n_D>n_E.
$$

Therefore, medium $D$ has the larger refractive index.

```quiz
type: radio
id: problem-5-snapshot-q1
content: |-
  A snapshot of the same-frequency wave shows the most widely spaced crests in medium $J$. What does that imply about medium $J$ compared with media having shorter wavelengths?
options:
- id: a
  content: |-
    It has the greatest wave speed and the smallest refractive index.
  correct: true
  feedback: |-
    At fixed frequency, the longest wavelength gives the greatest speed; $n=c/v$ then gives the smallest index.
- id: b
  content: |-
    It has the smallest wave speed and the largest refractive index.
  feedback: |-
    This reverses both relationships.
- id: c
  content: |-
    It has the greatest wave speed and the largest refractive index.
  feedback: |-
    Greater speed corresponds to smaller, not larger, refractive index.
```

---

<a id="apply-the-chain-to-media-a-b-and-c"></a>
## Apply the Chain to Media A, B, and C

**Example:** A snapshot shows the same-frequency wave traveling through media $A$, $B$, and $C$. The wavelength is shortest in medium $B$ and longest in medium $C$. Which medium has the largest index of refraction? Explain your reasoning.

**Explanation**

The wavelength order is

| Medium | Wavelength | Wave speed | Refractive index |
|---|---|---|---|
| $B$ | Shortest | Smallest | Largest |
| $A$ | Intermediate | Intermediate | Intermediate |
| $C$ | Longest | Greatest | Smallest |

In symbols, the wavelength order is

$$
\lambda_B<\lambda_A<\lambda_C.
$$

Frequency remains constant across the boundaries. Since $v=f\lambda$, the speed order matches the wavelength order:

$$
v_B<v_A<v_C.
$$

Since $n=c/v$, the index order reverses:

$$
n_B>n_A>n_C.
$$

Therefore, medium $B$ has the largest index of refraction.

```quiz
type: radio
id: m5-2lec-q4
content: |-
  **Question 4**

  A snapshot shows the same-frequency wave traveling through media $A$, $B$, and $C$. The wavelength is shortest in medium $B$ and longest in medium $C$. Which medium has the largest index of refraction? Explain your reasoning.
options:
- id: a
  content: Medium $A$
  feedback: Medium $A$ has an intermediate wavelength, so its index is smaller than $n_B$ and larger than $n_C$.
- id: b
  content: Medium $B$
  correct: true
  feedback: Frequency remains constant across the boundaries. Since $v=f\lambda$ and $n=c/v$, the shortest wavelength corresponds to the smallest wave speed and largest index of refraction. Therefore, $n_B>n_A>n_C$.
- id: c
  content: Medium $C$
  feedback: Medium $C$ has the longest wavelength, so it has the greatest wave speed and the smallest index of refraction.
```

---

<a id="variant-a-different-medium-order"></a>
## Variant: A Different Medium Order

The letter attached to the shortest wavelength can change from diagram to diagram. Re-read the spacing instead of memorizing the answer from the preceding example.

```quiz
type: radio
id: khadley-light-waves-q1
shuffle: true
content: |-
  The same-frequency light wave travels through three media. Which medium has the largest index of refraction?

  ![](<../../2026-07-23-M5-1/Source/Images/figure-stt20-5.jpg>)
options:
- id: a
  content: Medium $a$
  feedback: |-
    Frequency remains constant across the boundaries. Medium $a$ has an intermediate wavelength, so it also has an intermediate speed and index.
- id: b
  content: Medium $b$
  feedback: |-
    Medium $b$ has the longest wavelength. Since $v=f\lambda$ and $n=c/v$, that corresponds to the highest speed and smallest index.
- id: c
  content: Medium $c$
  correct: true
  feedback: |-
    Medium $c$ has the shortest wavelength. With constant frequency, it has the smallest wave speed and therefore the largest index of refraction.
```

---

<a id="summary"></a>
## Summary

For a same-frequency wave crossing several media:

1. Read the wavelength order from the spacing in the snapshot.
2. Use $v=f\lambda$: speed has the same order as wavelength.
3. Use $n=c/v$: index has the opposite order from speed.
4. Therefore, the shortest wavelength identifies the largest refractive index.

The main trap is reversing only one link. At fixed frequency, wavelength and speed change together, while speed and refractive index change oppositely.

<!-- lesson-nav:start -->
---

```update-progress
```

[[212/Home|Home]]
[[212/0. Table of Contents/TOC|Table of Contents]]

---
<!-- lesson-nav:end -->
