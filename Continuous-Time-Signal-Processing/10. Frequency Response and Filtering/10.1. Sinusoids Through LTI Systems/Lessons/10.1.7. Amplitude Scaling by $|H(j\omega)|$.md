# Amplitude Scaling by $|H(j\omega)|$

<!--
lesson-id: EE01-M10-01-L07
-->

## Table of Contents

- [Introduction to Amplitude Scaling by $|H(j\omega)|$](#introduction-to-amplitude-scaling-by-hjomega)
- [Scaling an Amplitude Using a Given $|H(j\omega_0)|$](#scaling-an-amplitude-using-a-given-hjomega0)
- [Evaluating $|H(j\omega)|$ at the Input Frequency](#evaluating-hjomega-at-the-input-frequency)
- [Computing $|H(j\omega_0)|$ from a Complex Frequency Response Value](#computing-hjomega0-from-a-complex-frequency-response-value)
- [Identifying Attenuation, Unity Gain, and Amplification from $|H(j\omega_0)|$](#identifying-attenuation-unity-gain-and-amplification-from-hjomega0)

---

<a id="introduction-to-amplitude-scaling-by-hjomega"></a>
## Introduction to Amplitude Scaling by $|H(j\omega)|$

In sinusoidal steady state through an LTI system, the output sinusoid keeps the same angular frequency $\omega_0$. The change to watch is the amplitude.

For the base case $x(t)=A\cos(\omega_0 t)$, track the input amplitude $A_{\text{in}}$ and the gain magnitude $|H(j\omega_0)|$ at that same frequency.

$$
A_{\text{out}}=A_{\text{in}}\,|H(j\omega_0)|
$$

So the output amplitude is the input amplitude multiplied by the magnitude of the frequency response at $\omega_0$. The output frequency stays fixed at $\omega_0$.

$$
x(t)=A\cos(\omega_0 t)\;\Longrightarrow\;A_{\text{out}}=A\,|H(j\omega_0)|
$$

Read the size of $|H(j\omega_0)|$ this way: values less than $1$ mean attenuation, values equal to $1$ mean unity gain, and values greater than $1$ mean amplification.

$$
|H(j\omega_0)|<1,\quad |H(j\omega_0)|=1,\quad |H(j\omega_0)|>1
$$

---

<a id="scaling-an-amplitude-using-a-given-hjomega0"></a>
## Scaling an Amplitude Using a Given $|H(j\omega_0)|$

**Example:** A sinusoid with amplitude $A_{\text{in}}=8$ enters an LTI system whose magnitude at the input frequency is $|H(j\omega_0)|=0.5$. Find the output amplitude.

**Explanation**

This is the cleanest numerical case: the gain magnitude is already given, so the only job is to scale the input amplitude.

Read off $A_{\text{in}}=8$ and $|H(j\omega_0)|=0.5$ from the prompt. Then apply the amplitude rule by multiplying those two numbers.

$$
A_{\text{out}}=A_{\text{in}}\,|H(j\omega_0)|=8(0.5)=4
$$

So the output amplitude is $4$.

**Question 1:**

```quiz
type: radio
id: EE01-M10-01-L07-q001
content: |-
  A sinusoid with amplitude $A_{\text{in}}=12$ enters an LTI system whose magnitude at the input frequency is $|H(j\omega_0)|=0.25$. What is the output amplitude?

options:
- id: a
  content: |-
    $12$

- id: b
  content: |-
    $48$

- id: c
  content: |-
    $0.25$

- id: d
  content: |-
    $12.25$

- id: e
  content: |-
    $3$
  correct: true
  feedback: |-
    Use the amplitude rule $A_{\text{out}}=A_{\text{in}}\,|H(j\omega_0)|$.

    Substitute $A_{\text{in}}=12$ and $|H(j\omega_0)|=0.25$ to get $A_{\text{out}}=12(0.25)=3$.
```

---

**Question 2:**

```quiz
type: radio
id: EE01-M10-01-L07-q002
content: |-
  A sinusoid with amplitude $A_{\text{in}}=15$ enters an LTI system whose magnitude at the input frequency is $|H(j\omega_0)|=1.2$. What is the output amplitude?

options:
- id: a
  content: |-
    $15$

- id: b
  content: |-
    $12.5$

- id: c
  content: |-
    $18$
  correct: true
  feedback: |-
    Use the same amplitude rule: multiply the input amplitude by the gain magnitude at the input frequency.

    Here $A_{\text{out}}=A_{\text{in}}\,|H(j\omega_0)|=15(1.2)=18$, so the output amplitude is amplified to $18$.

- id: d
  content: |-
    $16.2$

- id: e
  content: |-
    $1.2$
```

---

<a id="evaluating-hjomega-at-the-input-frequency"></a>
## Evaluating $|H(j\omega)|$ at the Input Frequency

**Example:** A sinusoid $x(t)=5\cos(4t)$ enters an LTI system with $H(j\omega)=\frac{10}{3+j\omega}$. Find the output amplitude.

**Explanation**

This example adds one new wrinkle: the gain factor is not given directly, so first evaluate the frequency response at the input frequency $\omega_0=4$.

Read the input amplitude as $A_{\text{in}}=5$. Then substitute $\omega_0=4$ into $H(j\omega)$ and take the magnitude.

$$
|H(j4)|=\left|\frac{10}{3+j4}\right|=\frac{10}{\sqrt{3^2+4^2}}=\frac{10}{5}=2
$$

Now apply the amplitude rule with that magnitude: multiply the input amplitude by $2$.

$$
A_{\text{out}}=A_{\text{in}}\,|H(j\omega_0)|=5(2)=10
$$

So the output amplitude is $10$.

**Question 3:**

```quiz
type: radio
id: EE01-M10-01-L07-q003
content: |-
  A sinusoid $x(t)=5\cos(4t)$ enters an LTI system with $H(j\omega)=\frac{12}{3+j\omega}$. Find the output amplitude after evaluating $|H(j4)|$.

options:
- id: a
  content: |-
    $12$
  correct: true
  feedback: |-
    Substitute the input frequency $\omega_0=4$ into the frequency response, then take the magnitude before multiplying by the input amplitude.

    $$
    |H(j4)|=\left|\frac{12}{3+j4}\right|=\frac{12}{\sqrt{3^2+4^2}}=\frac{12}{5}
    $$

    Now scale the input amplitude by that magnitude.

    $$
    A_{\text{out}}=A_{\text{in}}\,|H(j\omega_0)|=5\left(\frac{12}{5}\right)=12
    $$

    So the output amplitude is $12$.

- id: b
  content: |-
    $5$

- id: c
  content: |-
    $\frac{12}{5}$

- id: d
  content: |-
    $20$

- id: e
  content: |-
    $25$
```

---

**Question 4:**

```quiz
type: radio
id: EE01-M10-01-L07-q004
content: |-
  A sinusoid $x(t)=5\cos(t)$ enters an LTI system with $H(j\omega)=\frac{10}{3+j\omega}$. Find the output amplitude after evaluating $|H(j1)|$.

options:
- id: a
  content: |-
    $5$

- id: b
  content: |-
    $\sqrt{10}$

- id: c
  content: |-
    $10$

- id: d
  content: |-
    $5\sqrt{10}$
  correct: true
  feedback: |-
    This time the input frequency is $\omega_0=1$, so first evaluate the frequency response at $j1$ and take its magnitude.

    $$
    |H(j1)|=\left|\frac{10}{3+j}\right|=\frac{10}{\sqrt{3^2+1^2}}=\frac{10}{\sqrt{10}}=\sqrt{10}
    $$

    Then multiply the input amplitude by that gain magnitude.

    $$
    A_{\text{out}}=A_{\text{in}}\,|H(j\omega_0)|=5\sqrt{10}
    $$

    So the output amplitude is $5\sqrt{10}$.

- id: e
  content: |-
    $\frac{50}{3}$
```

---

<a id="computing-hjomega0-from-a-complex-frequency-response-value"></a>
## Computing $|H(j\omega_0)|$ from a Complex Frequency Response Value

**Example:** For an input amplitude $5$, the system response at the input frequency is $H(j\omega_0)=3-4j$. Find the output amplitude.

**Explanation**

This example keeps the same amplitude rule, but the frequency-response value is given in rectangular form. The first job is to extract its magnitude.

Read the input amplitude as $A_{\text{in}}=5$ and recognize that the system response at the same input frequency is $H(j\omega_0)=3-4j$. For a complex number $a+bj$, use $|a+bj|=\sqrt{a^2+b^2}$.

$$
|H(j\omega_0)|=|3-4j|=\sqrt{3^2+(-4)^2}=5
$$

Now use that magnitude as the amplitude gain and multiply it by the input amplitude.

$$
A_{\text{out}}=A_{\text{in}}\,|H(j\omega_0)|=5(5)=25
$$

So the output amplitude is $25$.

**Question 5:**

```quiz
type: radio
id: EE01-M10-01-L07-q005
content: |-
  An input sinusoid has amplitude $8$, and the system response at the input frequency is $H(j\omega_0)=3+4j$. What output amplitude do you get after taking the magnitude of the response?

options:
- id: a
  content: |-
    $24$

- id: b
  content: |-
    $32$

- id: c
  content: |-
    $56$

- id: d
  content: |-
    $24+32j$

- id: e
  content: |-
    $40$
  correct: true
  feedback: |-
    Use the magnitude of the complex response, not just its real or imaginary part.

    $$
    |H(j\omega_0)|=|3+4j|=\sqrt{3^2+4^2}=5
    $$

    Then scale the input amplitude: $A_{\text{out}}=8\cdot 5=40$.
```

---

**Question 6:**

```quiz
type: radio
id: EE01-M10-01-L07-q006
content: |-
  An input sinusoid has amplitude $4$, and the system response at the input frequency is $H(j\omega_0)=1-2j$. What output amplitude do you get after taking the magnitude of the response?

options:
- id: a
  content: |-
    $4$

- id: b
  content: |-
    $8$

- id: c
  content: |-
    $12$

- id: d
  content: |-
    $4+8j$

- id: e
  content: |-
    $4\sqrt{5}$
  correct: true
  feedback: |-
    First take the magnitude of the complex response.

    $$
    |H(j\omega_0)|=|1-2j|=\sqrt{1^2+(-2)^2}=\sqrt{5}
    $$

    Then scale the input amplitude: $A_{\text{out}}=4\cdot\sqrt{5}=4\sqrt{5}$.
```

---

<a id="identifying-attenuation-unity-gain-and-amplification-from-hjomega0"></a>
## Identifying Attenuation, Unity Gain, and Amplification from $|H(j\omega_0)|$

**Example:** A system has $|H(j\omega_0)|=0.4$ at the input frequency. Decide whether the output amplitude is attenuated, unchanged, or amplified.

**Explanation**

This example keeps the same amplitude rule, but the new job is to classify the gain factor by comparing it with $1$.

Read the gain factor as $|H(j\omega_0)|=0.4$. Since $0.4<1$, the output amplitude is smaller than the input amplitude.

$$
|H(j\omega_0)|<1 \Rightarrow \text{attenuation},\quad |H(j\omega_0)|=1 \Rightarrow \text{unity gain},\quad |H(j\omega_0)|>1 \Rightarrow \text{amplification}
$$

So this system produces attenuation.

**Question 7:**

```quiz
type: radio
id: EE01-M10-01-L07-q007
content: |-
  A system has $|H(j\omega_0)|=1$ at the input frequency. Which classification best describes the amplitude effect?

options:
- id: a
  content: |-
    attenuation

- id: b
  content: |-
    unity gain
  correct: true
  feedback: |-
    Because $|H(j\omega_0)|=1$, the output amplitude is unchanged. That classification is unity gain.

- id: c
  content: |-
    amplification

- id: d
  content: |-
    phase shift

- id: e
  content: |-
    frequency shift
```

---

**Question 8:**

```quiz
type: radio
id: EE01-M10-01-L07-q008
content: |-
  A system has $|H(j\omega_0)|=2.5$ at the input frequency. Which classification best describes the amplitude effect?

options:
- id: a
  content: |-
    attenuation

- id: b
  content: |-
    unity gain

- id: c
  content: |-
    amplification
  correct: true
  feedback: |-
    Because $|H(j\omega_0)|=2.5>1$, the output amplitude is larger than the input amplitude. That classification is amplification.

- id: d
  content: |-
    phase shift

- id: e
  content: |-
    frequency shift
```
