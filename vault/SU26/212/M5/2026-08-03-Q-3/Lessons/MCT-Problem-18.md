# Chain String Material Data into a Resonant Mode

<!--
lesson-id: 212-M5-076
topic-code: MTH212.M5.76
-->

## Table of Contents

- [Introduction](#introduction)
- [Recover Length and Tension from One Mode](#source-length-tension)
- [Carry Material Data into a Selected Mode](#source-material-mode)
- [Transfer the Chain to a Wire Fundamental](#lecture-fundamental)
- [Let a Hanging Mass Supply the Tension](#lecture-hanging-mass)
- [Summary](#summary)

## Prerequisites

- Use $v=f\lambda$ for a traveling wave.
- Recognize that a fixed-fixed string in mode $n$ contains $n$ half-wavelength loops.
- Rearrange equations containing several variables.
- Convert grams to kilograms.

---

<a id="introduction"></a>
## Introduction

These problems join two descriptions of the same vibrating string. Its material data determine the wave speed, and its fixed ends determine which wavelengths fit. Keep the links in one chain:

$$
\boxed{\mu=\frac{m_{\text{string}}}{L}}
\quad\longrightarrow\quad
\boxed{v=\sqrt{\frac{F_T}{\mu}}}
\quad\longrightarrow\quad
\boxed{\lambda_n=\frac{2L}{n}}
\quad\longrightarrow\quad
\boxed{f_n=\frac{v}{\lambda_n}=\frac{nv}{2L}}.
$$

For a string fixed at both ends, the number of loops is the harmonic number $n$. Identify $n$ before using the boundary equation. Then isolate the requested quantity and substitute. The chain can be followed forward to a frequency or backward to a length or tension.

Two masses can appear in the same problem, but they do different jobs:

| Quantity | Meaning | Where it enters |
|---|---|---|
| $m_{\text{string}}$ | mass of the vibrating length of string | $\mu=m_{\text{string}}/L$ |
| $M$ | a separate hanging mass | $F_T=Mg$ |

Linear density must use kilograms per meter. For example,

$$
40\ \mathrm g\left(\frac{1\ \mathrm{kg}}{1000\ \mathrm g}\right)
=0.040\ \mathrm{kg}.
$$

Use proportionality only as a direction check. At fixed $L$ and $n$, $f_n$ rises like $\sqrt{F_T}$ when $\mu$ is fixed and falls like $1/\sqrt{\mu}$ when $F_T$ is fixed. These trends can reject an impossible result, but the boxed chain remains the calculation route.

[[MCT-Problem-17|Problem 17]] develops the full fixed-end harmonic catalog. Here, harmonic facts are used only to complete the material-data chain.

**Transcript correction.** In `-8nn8hb0H8o`, the automatic captions say “standard wave”; the equations and loop diagrams show that the intended term is **standing wave**.

---

<a id="source-length-tension"></a>
## Recover Length and Tension from One Mode

### Source-video worked case 1 — `-8nn8hb0H8o`, 00:24:56–00:29:49

Waves on a string travel at $v=30\ \mathrm{m/s}$. The string forms a five-loop standing wave at $f_5=250\ \mathrm{Hz}$ and has mass $40\ \mathrm g$. Find its length and tension.

Five loops means $n=5$. First pair the given frequency with its matching wavelength:

$$
\lambda_5=\frac{v}{f_5}
=\frac{30}{250}
=0.12\ \mathrm m.
$$

Five half-wavelengths fit in the string:

$$
L=\frac{n\lambda_n}{2}
=\frac{5(0.12)}{2}
=0.30\ \mathrm m=30\ \mathrm{cm}.
$$

Now convert the string mass and form its linear density:

$$
m_{\text{string}}=0.040\ \mathrm{kg},
\qquad
\mu=\frac{0.040}{0.30}
=0.133\overline3\ \mathrm{kg/m}.
$$

Isolate the tension before substituting:

$$
v^2=\frac{F_T}{\mu}
\quad\Longrightarrow\quad
F_T=\mu v^2.
$$

Therefore,

$$
F_T=(0.133\overline3)(30)^2
=120\ \mathrm N.
$$

```quiz
type: radio
id: mct-p18-recover-tension
shuffle: true
content: |-
  Waves on a string travel at $40\ \mathrm{m/s}$ and form a four-loop standing wave at $200\ \mathrm{Hz}$. The vibrating string has mass $0.050\ \mathrm{kg}$. What is the tension?
options:
- id: mct-p18-recover-tension-a
  content: |-
    $200\ \mathrm N$
  correct: true
  feedback: |-
    Four loops mean $n=4$. Thus $\lambda_4=v/f_4=0.20\ \mathrm m$, $L=4\lambda_4/2=0.40\ \mathrm m$, and $\mu=0.050/0.40=0.125\ \mathrm{kg/m}$. Then $F_T=\mu v^2=(0.125)(40)^2=200\ \mathrm N$.
- id: mct-p18-recover-tension-b
  content: |-
    $80\ \mathrm N$
  feedback: |-
    This comes from using the total string mass as though it were linear density: $(0.050)(40)^2=80$. Divide the string mass by the vibrating length first, so $\mu=0.125\ \mathrm{kg/m}$.
- id: mct-p18-recover-tension-c
  content: |-
    $100\ \mathrm N$
  feedback: |-
    This treats each loop as one full wavelength and makes $L=4\lambda_4=0.80\ \mathrm m$. A loop is half a wavelength, so $L=4\lambda_4/2=0.40\ \mathrm m$ and the tension is $200\ \mathrm N$.
- id: mct-p18-recover-tension-d
  content: |-
    $400\ \mathrm N$
  feedback: |-
    This effectively sets $L=\lambda_4=0.20\ \mathrm m$ and ignores that four half-wavelengths fit on the string. Use $L=n\lambda_n/2$ before computing $\mu$.
- id: mct-p18-recover-tension-e
  content: |-
    $2000\ \mathrm N$
  feedback: |-
    This is a tenfold mass-conversion error. The given mass is already $0.050\ \mathrm{kg}$; it is not $0.50\ \mathrm{kg}$. With $\mu=0.125\ \mathrm{kg/m}$, the tension is $200\ \mathrm N$.
```

---

<a id="source-material-mode"></a>
## Carry Material Data into a Selected Mode

### Source-video worked case 2 — `-8nn8hb0H8o`, 00:29:57–00:36:35

A $5.0\ \mathrm m$ string has mass $0.75\ \mathrm{kg}$ and tension $300\ \mathrm N$. It vibrates with five loops. Find its speed, fifth-mode wavelength and frequency, fundamental frequency, and first three overtone frequencies.

Again, five loops means $n=5$. Move through the material links first:

$$
\mu=\frac{m_{\text{string}}}{L}
=\frac{0.75}{5.0}
=0.15\ \mathrm{kg/m},
$$

$$
v=\sqrt{\frac{F_T}{\mu}}
=\sqrt{\frac{300}{0.15}}
=44.72\ \mathrm{m/s}.
$$

Then impose mode $5$:

$$
\lambda_5=\frac{2L}{5}
=\frac{2(5.0)}{5}
=2.0\ \mathrm m,
$$

$$
f_5=\frac{v}{\lambda_5}
=\frac{44.72}{2.0}
=22.36\ \mathrm{Hz}.
$$

Use $f_n=nf_1$ for the four remaining frequencies requested in the source:

| Requested quantity | Calculation | Result |
|---|---:|---:|
| fundamental | $f_1=f_5/5$ | $4.472\ \mathrm{Hz}$ |
| first overtone, $n=2$ | $f_2=2f_1$ | $8.944\ \mathrm{Hz}$ |
| second overtone, $n=3$ | $f_3=3f_1$ | $13.42\ \mathrm{Hz}$ |
| third overtone, $n=4$ | $f_4=4f_1$ | $17.89\ \mathrm{Hz}$ |

**Rounding correction.** The video reports $13.41\ \mathrm{Hz}$ and $17.88\ \mathrm{Hz}$. Carrying $v=\sqrt{2000}\ \mathrm{m/s}$ as a guard-digit value gives $13.416\ldots\ \mathrm{Hz}$ and $17.888\ldots\ \mathrm{Hz}$, which round to $13.42\ \mathrm{Hz}$ and $17.89\ \mathrm{Hz}$ to the nearest hundredth.

```quiz
type: radio
id: mct-p18-material-to-mode
shuffle: true
content: |-
  A $3.0\ \mathrm m$ string has mass $0.60\ \mathrm{kg}$ and tension $180\ \mathrm N$. It vibrates with three loops. What is its mode frequency?
options:
- id: mct-p18-material-to-mode-a
  content: |-
    $15\ \mathrm{Hz}$
  correct: true
  feedback: |-
    The linear density is $\mu=0.60/3.0=0.20\ \mathrm{kg/m}$, so $v=\sqrt{180/0.20}=30\ \mathrm{m/s}$. Three loops mean $n=3$ and $\lambda_3=2L/3=2.0\ \mathrm m$, giving $f_3=v/\lambda_3=15\ \mathrm{Hz}$.
- id: mct-p18-material-to-mode-b
  content: |-
    $5\ \mathrm{Hz}$
  feedback: |-
    This is the fundamental frequency $f_1=v/(2L)=5\ \mathrm{Hz}$. The string has three loops, so the requested mode is $n=3$ and $f_3=3f_1=15\ \mathrm{Hz}$.
- id: mct-p18-material-to-mode-c
  content: |-
    $10\ \mathrm{Hz}$
  feedback: |-
    This divides the speed by $L$ as though the full string length were the third-mode wavelength. For three loops, $\lambda_3=2L/3=2.0\ \mathrm m$, not $3.0\ \mathrm m$.
- id: mct-p18-material-to-mode-d
  content: |-
    $30\ \mathrm{Hz}$
  feedback: |-
    This uses $\lambda_3=L/3=1.0\ \mathrm m$. Each loop is a half-wavelength, so the fixed-end condition is $\lambda_3=2L/3=2.0\ \mathrm m$.
- id: mct-p18-material-to-mode-e
  content: |-
    $450\ \mathrm{Hz}$
  feedback: |-
    This omits the square root in $v=\sqrt{F_T/\mu}$ and treats $180/0.20=900$ as a speed. The actual speed is $30\ \mathrm{m/s}$, leading to $15\ \mathrm{Hz}$.
```

---

<a id="lecture-fundamental"></a>
## Transfer the Chain to a Wire Fundamental

### M5-4 lecture worked case — wire fundamental

A wire has length $0.85\ \mathrm m$, mass $0.0022\ \mathrm{kg}$, and tension $52\ \mathrm N$. Find its fundamental frequency.

The material part of the chain gives

$$
\mu=\frac{0.0022}{0.85}
=0.002588\ \mathrm{kg/m},
$$

$$
v=\sqrt{\frac{52}{0.002588}}
=141.7\ \mathrm{m/s}.
$$

The fundamental has $n=1$ and $\lambda_1=2L$, so

$$
f_1=\frac{v}{2L}
=\frac{141.7}{2(0.85)}
=83.4\ \mathrm{Hz}.
$$

```quiz
type: radio
id: mct-p18-wire-fundamental
shuffle: true
content: |-
  A wire has length $0.80\ \mathrm m$, mass $0.0080\ \mathrm{kg}$, and tension $50\ \mathrm N$. What is its fundamental frequency?
options:
- id: mct-p18-wire-fundamental-a
  content: |-
    $44.2\ \mathrm{Hz}$
  correct: true
  feedback: |-
    The linear density is $\mu=0.0080/0.80=0.010\ \mathrm{kg/m}$, so $v=\sqrt{50/0.010}=70.71\ \mathrm{m/s}$. The fundamental wavelength is $2L=1.60\ \mathrm m$, giving $f_1=70.71/1.60=44.2\ \mathrm{Hz}$.
- id: mct-p18-wire-fundamental-b
  content: |-
    $88.4\ \mathrm{Hz}$
  feedback: |-
    This uses $L$ as the fundamental wavelength. A string fixed at both ends has $\lambda_1=2L$, so divide the speed by $1.60\ \mathrm m$, not $0.80\ \mathrm m$.
- id: mct-p18-wire-fundamental-c
  content: |-
    $49.4\ \mathrm{Hz}$
  feedback: |-
    This uses the total mass $0.0080\ \mathrm{kg}$ in the speed formula as though it were $\mu$. First divide by the wire length to get $\mu=0.010\ \mathrm{kg/m}$.
- id: mct-p18-wire-fundamental-d
  content: |-
    $55.2\ \mathrm{Hz}$
  feedback: |-
    This multiplies mass by length when forming linear density. Linear density is mass per length, $\mu=m_{\text{string}}/L$, so here it is $0.010\ \mathrm{kg/m}$.
- id: mct-p18-wire-fundamental-e
  content: |-
    $70.7\ \mathrm{Hz}$
  feedback: |-
    This is the wave speed in meters per second, not the frequency. Complete the resonance link by dividing $v$ by the fundamental wavelength $2L=1.60\ \mathrm m$.
```

---

<a id="lecture-hanging-mass"></a>
## Let a Hanging Mass Supply the Tension

### M5-4 lecture worked case — hanging-mass third harmonic

The lecture uses a $3.1\ \mathrm m$ vibrating string with mass $0.0035\ \mathrm{kg}$. A separate $8.2\ \mathrm{kg}$ mass hangs over a pulley and supplies the tension. Find the third-harmonic frequency using $g=9.81\ \mathrm{m/s^2}$.

Keep the two masses in their assigned formulas:

$$
F_T=Mg=(8.2)(9.81)=80.442\ \mathrm N,
$$

$$
\mu=\frac{m_{\text{string}}}{L}
=\frac{0.0035}{3.1}
=0.001129\ \mathrm{kg/m}.
$$

Then

$$
v=\sqrt{\frac{80.442}{0.001129}}
=266.9\ \mathrm{m/s}.
$$

The third harmonic has $n=3$, so

$$
f_3=\frac{3v}{2L}
=\frac{3(266.9)}{2(3.1)}
=129.2\ \mathrm{Hz}
\approx130\ \mathrm{Hz}.
$$

Do not put the string's $0.0035\ \mathrm{kg}$ mass into $F_T=mg$. That mass sets $\mu$; the separate $8.2\ \mathrm{kg}$ mass sets $F_T$.

```quiz
type: radio
id: mct-p18-hanging-mass
shuffle: true
content: |-
  A $5.0\ \mathrm{kg}$ mass hangs from a $2.0\ \mathrm m$ vibrating string whose mass is $0.0040\ \mathrm{kg}$. Using $g=9.8\ \mathrm{m/s^2}$, what is the string's third-harmonic frequency?
options:
- id: mct-p18-hanging-mass-a
  content: |-
    $117\ \mathrm{Hz}$
  correct: true
  feedback: |-
    The hanging mass gives $F_T=Mg=49\ \mathrm N$, while the string gives $\mu=0.0040/2.0=0.0020\ \mathrm{kg/m}$. Thus $v=\sqrt{49/0.0020}=156.5\ \mathrm{m/s}$ and $f_3=3v/(2L)=117\ \mathrm{Hz}$.
- id: mct-p18-hanging-mass-b
  content: |-
    $39.1\ \mathrm{Hz}$
  feedback: |-
    This is the fundamental frequency $v/(2L)$. The question asks for the third harmonic, so multiply the fundamental by $3$.
- id: mct-p18-hanging-mass-c
  content: |-
    $156.5\ \mathrm{Hz}$
  feedback: |-
    This number is the wave speed $v=156.5\ \mathrm{m/s}$ with frequency units attached. Complete the mode step: $f_3=3v/(2L)$.
- id: mct-p18-hanging-mass-d
  content: |-
    $235\ \mathrm{Hz}$
  feedback: |-
    This uses $f_3=3v/L$ and misses the factor of $2$ in the fixed-end wavelength condition. Since $\lambda_3=2L/3$, the frequency is $3v/(2L)$.
- id: mct-p18-hanging-mass-e
  content: |-
    $3.3\ \mathrm{Hz}$
  feedback: |-
    This uses the vibrating string's weight for the tension. The separate $5.0\ \mathrm{kg}$ hanging mass supplies $F_T=49\ \mathrm N$; the $0.0040\ \mathrm{kg}$ string mass belongs in $\mu=m_{\text{string}}/L$.
```

---

<a id="summary"></a>
## Summary

For a string fixed at both ends, use one linked move:

1. Translate the picture or wording into harmonic number $n$; $n$ loops means mode $n$.
2. Put the vibrating string's mass into $\mu=m_{\text{string}}/L$.
3. Put a separate hanging mass, if present, into $F_T=Mg$.
4. Connect the material data to wave speed with $v=\sqrt{F_T/\mu}$.
5. Impose the selected mode with $\lambda_n=2L/n$ and $f_n=v/\lambda_n=nv/(2L)$.

A quick unit check should produce $\mu$ in $\mathrm{kg/m}$, $v$ in $\mathrm{m/s}$, and $f_n$ in hertz. A direction check should also agree: more tension raises the frequency, while greater linear density lowers it. The main traps are using total string mass as linear density, swapping the string and hanging masses, or treating each loop as a full wavelength.

<!-- lesson-nav:start -->
---

```update-progress
```

[[212/Home|Home]]
[[212/0. Table of Contents/TOC|Table of Contents]]

---
<!-- lesson-nav:end -->
