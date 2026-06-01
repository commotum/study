# Finding the Support of $x(\tau)$

<!--
lesson-id: EE01-M07-01-L01
-->

## Table of Contents

- [Introduction to Finding the Support of $x(\tau)$](#introduction-to-finding-the-support-of-xtau)
- [Reading the Support of a Basic Signal in $\tau$](#reading-the-support-of-a-basic-signal-in-tau)
- [Finding Support from a Piecewise Definition in $\tau$](#finding-support-from-a-piecewise-definition-in-tau)
- [Finding Support from Unit Step Windows in $\tau$](#finding-support-from-unit-step-windows-in-tau)
- [Writing the Fixed Support Constraint for $x(\tau)$](#writing-the-fixed-support-constraint-for-xtau)

---

<a id="introduction-to-finding-the-support-of-xtau"></a>
## Introduction to Finding the Support of $x(\tau)$

In a convolution integral, $\tau$ is the integration variable. The value of $t$ is treated as fixed later, but the first support constraint comes only from the signal $x(\tau)$.

$$
y(t)=\int_{-\infty}^{\infty}x(\tau)h(t-\tau)\,d\tau
$$

The support of $x(\tau)$ means the set of $\tau$ values where $x(\tau)$ is nonzero. To find it, ignore $h(t-\tau)$ for now and read only where the input-side signal is active.

$$
\operatorname{supp} x=\{\tau: x(\tau)\ne 0\}
$$

For the cleanest case, suppose $x(\tau)$ is equal to $1$ on one interval and is $0$ everywhere else. The support is exactly the interval where the nonzero branch appears.

$$
x(\tau)=\begin{cases}1,&0\le \tau\le 2\\0,&\text{otherwise}\end{cases}\quad\Rightarrow\quad 0\le \tau\le 2
$$

So the fixed support constraint from $x(\tau)$ is $0\le \tau\le 2$. It is fixed because it depends only on $x(\tau)$ and contains no $t$; later overlap work will combine this fixed constraint with the moving support of $h(t-\tau)$.

---

<a id="reading-the-support-of-a-basic-signal-in-tau"></a>
## Reading the Support of a Basic Signal in $\tau$

**Example:** Find the support of $x(\tau)$ if $x(\tau)=2$ for $-1\le \tau\le 3$ and $x(\tau)=0$ otherwise.

**Explanation**

The cue is the phrase that tells us exactly when $x(\tau)$ is nonzero. Here, $x(\tau)=2$ on $-1\le \tau\le 3$, so the amplitude $2$ only tells us the signal is active on that interval.

$$
x(\tau)=2 \quad \text{for} \quad -1\le \tau\le 3
$$

Everywhere outside that interval, the signal is given as $0$, so those $\tau$ values are not part of the support. The support is the interval from the nonzero clause.

$$
\operatorname{supp} x=\{\tau:x(\tau)\ne0\}=[-1,3]
$$

So the fixed support constraint for this signal is $-1\le \tau\le 3$. This constraint comes only from $x(\tau)$; no comparison with $h(t-\tau)$ is needed in this step.

**Question 1:**

```quiz
type: free
id: EE01-M07-01-L01-q001
content: |-
  Find the support of $x(\tau)$ if $x(\tau)=5$ for $-2\le \tau\le 1$ and $x(\tau)=0$ otherwise.

correct: |-
  $-2\le \tau\le 1$

feedback: |-
  The signal is nonzero exactly on $-2\le \tau\le 1$. The amplitude $5$ does not change the support, so the support is $[-2,1]$.
```

---

**Question 2:**

```quiz
type: free
id: EE01-M07-01-L01-q002
content: |-
  Find the support of $x(\tau)$ if $x(\tau)=-3$ for $0\le \tau\le 4$ and $x(\tau)=0$ otherwise.

correct: |-
  $0\le \tau\le 4$

feedback: |-
  The support is the interval where $x(\tau)$ is nonzero. Since $x(\tau)=-3$ on $0\le \tau\le 4$ and is zero otherwise, the support is $[0,4]$.
```

---

<a id="finding-support-from-a-piecewise-definition-in-tau"></a>
## Finding Support from a Piecewise Definition in $\tau$

**Example:** Find the support of $x(\tau)=\begin{cases}0,&\tau<-1\\\tau+3,&-1\le \tau\le 2\\0,&\tau>2\end{cases}$.

**Explanation**

The cue is the piecewise definition. To find the support, scan the branches and separate the branches where $x(\tau)$ is exactly $0$ from the branch where $x(\tau)$ is nonzero.

$$
x(\tau)=\begin{cases}0,&\tau<-1\\\tau+3,&-1\le \tau\le 2\\0,&\tau>2\end{cases}
$$

The first branch is zero for $\tau<-1$, and the last branch is zero for $\tau>2$. Those intervals are not part of the support.

The remaining branch is $x(\tau)=\tau+3$ on $-1\le \tau\le 2$. This is the active branch, so its condition gives the support interval.

$$
\operatorname{supp} x=\{\tau:x(\tau)\ne0\}=[-1,2]
$$

So the fixed support constraint for this signal is $-1\le \tau\le 2$. This step uses only the branches of $x(\tau)$; it does not involve $h(t-\tau)$ or any overlap calculation.

**Question 3:**

```quiz
type: free
id: EE01-M07-01-L01-q003
content: |-
  Find the support of $x(\tau)$.

  $$
  x(\tau)=\begin{cases}0,&\tau<-3\\4-\tau,&-3\le \tau\le 0\\0,&\tau>0\end{cases}
  $$

correct: |-
  $-3\le \tau\le 0$

feedback: |-
  The zero branches cover $\tau<-3$ and $\tau>0$. The only active branch is $4-\tau$ on $-3\le \tau\le 0$, so that branch condition is the support.
```

---

**Question 4:**

```quiz
type: free
id: EE01-M07-01-L01-q004
content: |-
  Find the support of $x(\tau)$.

  $$
  x(\tau)=\begin{cases}0,&\tau<-4\\\tau+6,&-4\le \tau\le -1\\0,&\tau>-1\end{cases}
  $$

correct: |-
  $-4\le \tau\le -1$

feedback: |-
  The first and last branches are exactly zero, so they are outside the support. The nonzero branch is $\tau+6$ on $-4\le \tau\le -1$, which gives the support interval.
```

---

<a id="finding-support-from-unit-step-windows-in-tau"></a>
## Finding Support from Unit Step Windows in $\tau$

**Example:** Find the support of $x(\tau)=(u(\tau-1)-u(\tau-4))e^{-\tau}$.

**Explanation**

The cue is the unit-step difference $u(\tau-1)-u(\tau-4)$. This factor acts like a window: it turns the signal on at one $\tau$ value and turns it off at another.

$$
x(\tau)=(u(\tau-1)-u(\tau-4))e^{-\tau}
$$

The term $u(\tau-1)$ turns on at $\tau=1$. The subtracted term $u(\tau-4)$ turns on at $\tau=4$, which turns the window off after that point.

$$
u(\tau-1)-u(\tau-4) \quad \text{selects the window} \quad 1\le \tau\le 4
$$

The multiplier $e^{-\tau}$ does not create a new cutoff because it is nonzero for every $\tau$. So the support comes from the unit-step window.

$$
\operatorname{supp} x=\{\tau:x(\tau)\ne0\}=[1,4]
$$

So the fixed support constraint for this signal is $1\le \tau\le 4$. This is still a constraint from $x(\tau)$ only; no overlap with $h(t-\tau)$ is being formed yet.

**Question 5:**

```quiz
type: free
id: EE01-M07-01-L01-q005
content: |-
  Find the support of $x(\tau)$.

  $$
  x(\tau)=(u(\tau+2)-u(\tau-1))(\tau^2+1)
  $$

correct: |-
  $-2\le \tau\le 1$

feedback: |-
  The unit step $u(\tau+2)$ turns on at $\tau=-2$, and subtracting $u(\tau-1)$ turns the window off at $\tau=1$. The factor $\tau^2+1$ is nonzero on that window, so the support is $-2\le \tau\le 1$.
```

---

**Question 6:**

```quiz
type: free
id: EE01-M07-01-L01-q006
content: |-
  Find the support of $x(\tau)$.

  $$
  x(\tau)=(u(\tau+4)-u(\tau+1))e^{2\tau}
  $$

correct: |-
  $-4\le \tau\le -1$

feedback: |-
  The window starts when $u(\tau+4)$ turns on at $\tau=-4$ and ends when the subtracted step $u(\tau+1)$ turns on at $\tau=-1$. Since $e^{2\tau}$ is nonzero for every $\tau$, the support is $-4\le \tau\le -1$.
```

---

<a id="writing-the-fixed-support-constraint-for-xtau"></a>
## Writing the Fixed Support Constraint for $x(\tau)$

**Example:** Given that $x(\tau)$ is nonzero only for $-2\le \tau\le 1$, write the fixed support constraint for $x(\tau)$ that will be used later when finding overlap with $h(t-\tau)$.

**Explanation**

The cue is that the nonzero interval for $x(\tau)$ has already been identified. Since $x(\tau)$ is nonzero only for $-2\le \tau\le 1$, that interval is the support of $x$.

$$
\operatorname{supp} x=[-2,1]
$$

To write this as a support constraint, keep the convolution variable $\tau$ in the inequality and copy the support endpoints in increasing order.

$$
-2\le \tau\le 1
$$

This constraint is fixed because it contains no $t$. It comes only from $x(\tau)$, so it does not move as the output time changes.

$$
\text{fixed support constraint from }x(\tau):\quad -2\le \tau\le 1
$$

Later overlap work will combine this fixed constraint with the support of $h(t-\tau)$. For this step, stop here and do not form an intersection.

**Question 7:**

```quiz
type: free
id: EE01-M07-01-L01-q007
content: |-
  If $x(\tau)$ is nonzero only on $-1\le \tau\le 4$, write the fixed support constraint for $x(\tau)$ that will be used when finding overlap with $h(t-\tau)$.

correct: |-
  $-1\le \tau\le 4$

feedback: |-
  The support has already been identified. To write it as the fixed support constraint, keep the variable as $\tau$ and copy the endpoints: $-1\le \tau\le 4$. No $t$ appears, so this is the fixed constraint from $x(\tau)$.
```

---

**Question 8:**

```quiz
type: free
id: EE01-M07-01-L01-q008
content: |-
  Given that $\operatorname{supp} x=[-6,-2]$, write the fixed support constraint for $x(\tau)$.

correct: |-
  $-6\le \tau\le -2$

feedback: |-
  The interval $[-6,-2]$ means $x(\tau)$ is nonzero from $\tau=-6$ through $\tau=-2$. Written as the fixed support constraint, this is $-6\le \tau\le -2$.
```
