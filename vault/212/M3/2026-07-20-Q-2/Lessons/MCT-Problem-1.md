# Calculate Signed Torque from a Force's Line of Action

<!--
lesson-id: 212-M3-037
topic-code: MTH212.M3.37
-->

## Table of Contents

- [Introduction](#introduction)
- [Mark the Pivot and Line of Action](#mark-the-pivot-and-line-of-action)
- [Source-Video Geometry: Door Comparison](#source-video-door-comparison)
- [Source-Video Worked Problem: Two-Force Bar](#source-video-two-force-bar)
- [Source-Video Worked Problem: Three-Force Propeller](#source-video-three-force-propeller)
- [Zero Torque and Plausibility Checks](#zero-torque-and-plausibility-checks)
- [Summary](#summary)

## Prerequisites

- Identify clockwise and counterclockwise rotation about a marked pivot.
- Use $\sin\theta=\text{opposite}/\text{hypotenuse}$ in a right triangle.
- Resolve a force into components parallel and perpendicular to a chosen direction.
- Add positive and negative quantities with their signs intact.

---

<a id="introduction"></a>
## Introduction

Torque measures how strongly a force tends to turn an object about a chosen pivot. A force is effective only through its perpendicular separation from the pivot:

$$
\tau=F d_\perp=rF\sin\theta.
$$

Here $\mathbf r$ points from the pivot to the point where the force is applied, $\theta$ is the angle **between $\mathbf r$ and $\mathbf F$**, and $d_\perp$ is the perpendicular distance from the pivot to the force's line of action.

This lesson uses one sign convention throughout:

$$
\text{counterclockwise }(+),\qquad \text{clockwise }(-).
$$

The operational move is:

1. Mark the pivot.
2. Draw or extend each force's line of action.
3. Find either $d_\perp$ or the perpendicular force component $F_\perp$.
4. Attach a sign from the force's turning tendency.
5. Add the signed torques.

The paired lecture note motivates the idea with a teeter-totter: a larger rider can sit closer to the fulcrum while a smaller rider sits farther away. Their forces need not match because turning effect depends on both force and perpendicular lever arm. Solving an unknown balance force or distance belongs to the next lesson; here the task is to calculate and sign the torques already given.

---

<a id="mark-the-pivot-and-line-of-action"></a>
## Mark the Pivot and Line of Action

A force's **line of action** is the infinite line through its application point, parallel to the force. Drop a perpendicular from the pivot to this line:

```text
                            ↑ F
                            │ line of action
                            ● application point
                         r /│
                          / │
                         /  │
              pivot O ●─────┘  ⟂
                      d_perp
```

The triangle has hypotenuse $r$ and side opposite $\theta$ equal to $d_\perp$. Therefore,

$$
\sin\theta=\frac{d_\perp}{r}
\quad\Longrightarrow\quad
d_\perp=r\sin\theta.
$$

This gives the moment-arm route:

$$
|\tau|=F d_\perp=Fr\sin\theta.
$$

Alternatively, keep the full distance $r$ and use only the force component perpendicular to $\mathbf r$:

$$
F_\perp=F\sin\theta,
\qquad
|\tau|=rF_\perp=rF\sin\theta.
$$

These are the same calculation. Do not use both adjustments at once; multiplying $d_\perp$ by $F_\perp$ would insert the sine factor twice.

**Example:** A $50\,\mathrm N$ force is applied $0.80\,\mathrm m$ from a pivot. The angle between $\mathbf r$ and $\mathbf F$ is $30^\circ$, and the force tends to turn the object counterclockwise.

Using the perpendicular force component,

$$
F_\perp=(50)\sin 30^\circ=25\,\mathrm N,
$$

so

$$
\tau=+(0.80)(25)=+20\,\mathrm{N\cdot m}.
$$

The plus sign records counterclockwise tendency. The unit is newton-meter, $\mathrm{N\cdot m}$.

```quiz
type: radio
id: mct-p1-angled-force
content: |-
  A $40\,\mathrm N$ force is applied $0.60\,\mathrm m$ from a pivot. The angle between $\mathbf r$ and $\mathbf F$ is $30^\circ$, and the force tends to rotate the object clockwise. What is its signed torque if counterclockwise is positive?
options:
- id: mct-p1-angled-force-a
  content: |-
    $-12\,\mathrm{N\cdot m}$
  correct: true
  feedback: |-
    The perpendicular factor is $\sin 30^\circ$. Thus $\tau=-(0.60)(40)\sin 30^\circ=-12\,\mathrm{N\cdot m}$, with a negative sign for clockwise tendency.
- id: mct-p1-angled-force-b
  content: |-
    $+12\,\mathrm{N\cdot m}$
  feedback: |-
    The magnitude uses the correct sine factor, but the sign is reversed. A clockwise tendency is negative under the stated convention.
- id: mct-p1-angled-force-c
  content: |-
    $-24\,\mathrm{N\cdot m}$
  feedback: |-
    This uses the full product $rF$ as though the force were perpendicular to $\mathbf r$. At $30^\circ$, only $F\sin30^\circ$ is perpendicular, so the torque magnitude is $12\,\mathrm{N\cdot m}$.
- id: mct-p1-angled-force-d
  content: |-
    $-20.8\,\mathrm{N\cdot m}$
  feedback: |-
    This comes from using $\cos30^\circ$, which selects the force component parallel to $\mathbf r$. The parallel component does not turn the object; use $F\sin30^\circ$.
- id: mct-p1-angled-force-e
  content: |-
    $0\,\mathrm{N\cdot m}$
  feedback: |-
    The line of action is not through the pivot because the angle is neither $0^\circ$ nor $180^\circ$. The nonzero perpendicular component produces a $12\,\mathrm{N\cdot m}$ torque.
```

---

<a id="source-video-door-comparison"></a>
## Source-Video Geometry: Door Comparison

**Source-video example (0:01–6:18):** Equal forces are applied to a door at positions A, B, and C. Position A is farthest from the hinge, B is intermediate, and C is closest.

The hinge is the pivot. For equal forces applied in the same direction, the farther position has the larger perpendicular moment arm:

$$
d_{\perp,A}>d_{\perp,B}>d_{\perp,C}.
$$

Consequently,

$$
|\tau_A|>|\tau_B|>|\tau_C|.
$$

This is why pushing near the outer edge of a door is more effective than pushing near its hinge. The comparison is about perpendicular moment arm, not distance alone; changing the force angle can change the ranking.

```quiz
type: radio
id: mct-p1-door-mirror
content: |-
  A door is mirrored so that its hinge is on the right. Equal forces act perpendicular to the door at points $P$, $Q$, and $R$, located $0.20\,\mathrm m$, $0.55\,\mathrm m$, and $0.90\,\mathrm m$ from the hinge, respectively. Which torque-magnitude ranking is correct?
options:
- id: mct-p1-door-mirror-a
  content: |-
    $|\tau_R|>|\tau_Q|>|\tau_P|$
  correct: true
  feedback: |-
    Each force is equal and perpendicular, so $|\tau|=rF$. Point $R$ has the largest moment arm, followed by $Q$ and then $P$; moving the hinge to the other side does not change that distance ranking.
- id: mct-p1-door-mirror-b
  content: |-
    $|\tau_P|>|\tau_Q|>|\tau_R|$
  feedback: |-
    This reverses the lever-arm effect. With equal perpendicular forces, the point farthest from the hinge produces the largest torque magnitude.
- id: mct-p1-door-mirror-c
  content: |-
    $|\tau_P|=|\tau_Q|=|\tau_R|$
  feedback: |-
    Equal forces do not guarantee equal torques. Their perpendicular moment arms are $0.20$, $0.55$, and $0.90\,\mathrm m$, so the torque magnitudes differ.
- id: mct-p1-door-mirror-d
  content: |-
    $|\tau_Q|>|\tau_R|>|\tau_P|$
  feedback: |-
    Point $Q$ is not farthest from the hinge. Since the forces are perpendicular and equal, the $0.90\,\mathrm m$ arm at $R$ must produce more torque than the $0.55\,\mathrm m$ arm at $Q$.
- id: mct-p1-door-mirror-e
  content: |-
    $|\tau_R|>|\tau_P|>|\tau_Q|$
  feedback: |-
    The first comparison is right, but $Q$ has a larger moment arm than $P$. Thus $Q$ must rank above $P$ for equal perpendicular forces.
```

---

<a id="source-video-two-force-bar"></a>
## Source-Video Worked Problem: Two-Force Bar

**Source-video worked problem (6:24–9:04):** A $200\,\mathrm N$ force acts with a $3\,\mathrm m$ perpendicular moment arm and tends to rotate a bar counterclockwise. A $400\,\mathrm N$ force acts with a $1.5\,\mathrm m$ perpendicular moment arm and tends to rotate it clockwise.

Record each contribution before adding:

| Force | Magnitude calculation | Turning sense | Signed torque |
|---|---:|---|---:|
| $200\,\mathrm N$ | $(200)(3)$ | Counterclockwise | $+600\,\mathrm{N\cdot m}$ |
| $400\,\mathrm N$ | $(400)(1.5)$ | Clockwise | $-600\,\mathrm{N\cdot m}$ |

Then

$$
\tau_{\mathrm{net}}
=+600-600
=0\,\mathrm{N\cdot m}.
$$

The two turning effects cancel even though the forces have different magnitudes. This result establishes torque balance about the chosen pivot; it does not, by itself, describe every aspect of the bar's motion.

```quiz
type: radio
id: mct-p1-two-force-mirror
content: |-
  A $120\,\mathrm N$ force has a $2.5\,\mathrm m$ perpendicular moment arm and tends to turn a bar counterclockwise. A $250\,\mathrm N$ force has a $0.80\,\mathrm m$ perpendicular moment arm and tends to turn it clockwise. With counterclockwise positive, what is the net torque and its direction?
options:
- id: mct-p1-two-force-mirror-a
  content: |-
    $+100\,\mathrm{N\cdot m}$, counterclockwise
  correct: true
  feedback: |-
    The signed contributions are $+(120)(2.5)=+300$ and $-(250)(0.80)=-200\,\mathrm{N\cdot m}$. Their sum is $+100\,\mathrm{N\cdot m}$, so the net tendency is counterclockwise.
- id: mct-p1-two-force-mirror-b
  content: |-
    $-100\,\mathrm{N\cdot m}$, clockwise
  feedback: |-
    The magnitude difference is $100\,\mathrm{N\cdot m}$, but the larger contribution is the $+300\,\mathrm{N\cdot m}$ counterclockwise torque. The net sign is therefore positive, not negative.
- id: mct-p1-two-force-mirror-c
  content: |-
    $+500\,\mathrm{N\cdot m}$, counterclockwise
  feedback: |-
    This adds the two torque magnitudes. Because the forces tend to turn the bar in opposite directions, the signed ledger is $+300-200$, not $300+200$.
- id: mct-p1-two-force-mirror-d
  content: |-
    $0\,\mathrm{N\cdot m}$
  feedback: |-
    The torques would cancel only if their magnitudes matched. Here they are $300$ and $200\,\mathrm{N\cdot m}$, leaving a $100\,\mathrm{N\cdot m}$ counterclockwise torque.
- id: mct-p1-two-force-mirror-e
  content: |-
    $-500\,\mathrm{N\cdot m}$, clockwise
  feedback: |-
    This both adds the magnitudes and gives the sum the clockwise sign. Opposing turning tendencies require signed addition: $+300+(-200)=+100\,\mathrm{N\cdot m}$.
```

---

<a id="source-video-three-force-propeller"></a>
## Source-Video Worked Problem: Three-Force Propeller

**Source-video worked problem (9:11–13:04):** Three forces act on a propeller about its center:

- A $300\,\mathrm N$ force acts $4\,\mathrm m$ from the pivot and tends clockwise.
- A $600\,\mathrm N$ force acts $3\,\mathrm m$ from the pivot at $60^\circ$ to $\mathbf r$ and tends counterclockwise.
- A $500\,\mathrm N$ force acts $5\,\mathrm m$ from the pivot at $50^\circ$ to $\mathbf r$ and tends counterclockwise.

Before calculating, inspect the diagram information. The first torque is negative. The other two are positive, and each angled torque must be smaller in magnitude than its corresponding maximum $rF$. These observations give a sign and size check for the arithmetic.

Now build the signed ledger:

$$
\begin{aligned}
\tau_1&=-(300)(4)=-1200\,\mathrm{N\cdot m},\\
\tau_2&=+(600)(3)\sin60^\circ
\approx+1558.8\,\mathrm{N\cdot m},\\
\tau_3&=+(500)(5)\sin50^\circ
\approx+1915.1\,\mathrm{N\cdot m}.
\end{aligned}
$$

Therefore,

$$
\begin{aligned}
\tau_{\mathrm{net}}
&=-1200+1558.8+1915.1\\
&\approx+2274\,\mathrm{N\cdot m}.
\end{aligned}
$$

The positive result means the net turning tendency is counterclockwise.

```quiz
type: radio
id: mct-p1-three-force-control
content: |-
  Three forces act about one pivot. Force A is $90\,\mathrm N$ at $2.0\,\mathrm m$, perpendicular to $\mathbf r$, and clockwise. Force B is $100\,\mathrm N$ at $1.5\,\mathrm m$, perpendicular to $\mathbf r$, and counterclockwise. Force C is $80\,\mathrm N$ at $1.0\,\mathrm m$ and $30^\circ$ to $\mathbf r$, counterclockwise. What is the net torque if counterclockwise is positive?
options:
- id: mct-p1-three-force-control-a
  content: |-
    $+10\,\mathrm{N\cdot m}$, counterclockwise
  correct: true
  feedback: |-
    The ledger is $-(90)(2.0)+(100)(1.5)+(80)(1.0)\sin30^\circ=-180+150+40=+10\,\mathrm{N\cdot m}$. Its positive sign indicates counterclockwise tendency.
- id: mct-p1-three-force-control-b
  content: |-
    $-10\,\mathrm{N\cdot m}$, clockwise
  feedback: |-
    The three magnitudes are handled correctly, but the final sign is reversed. The two counterclockwise contributions total $190\,\mathrm{N\cdot m}$, which exceeds the $180\,\mathrm{N\cdot m}$ clockwise contribution.
- id: mct-p1-three-force-control-c
  content: |-
    $+370\,\mathrm{N\cdot m}$, counterclockwise
  feedback: |-
    This adds all three torque magnitudes. Force A is clockwise and must enter as $-180\,\mathrm{N\cdot m}$ before the contributions are summed.
- id: mct-p1-three-force-control-d
  content: |-
    $+50\,\mathrm{N\cdot m}$, counterclockwise
  feedback: |-
    This treats force C as perpendicular and uses $rF=80\,\mathrm{N\cdot m}$. Its angle is $30^\circ$, so its torque is only $(80)(1)\sin30^\circ=40\,\mathrm{N\cdot m}$.
- id: mct-p1-three-force-control-e
  content: |-
    $-70\,\mathrm{N\cdot m}$, clockwise
  feedback: |-
    This omits force C's $+40\,\mathrm{N\cdot m}$ contribution and also misstates the remaining sum: $-180+150=-30\,\mathrm{N\cdot m}$. Including all three gives $+10\,\mathrm{N\cdot m}$.
```

---

<a id="zero-torque-and-plausibility-checks"></a>
## Zero Torque and Plausibility Checks

Run these checks from the diagram before entering numbers:

1. **Line through the pivot:** If the line of action passes through the pivot, then $d_\perp=0$ and $\tau=0$. Equivalently, $\theta=0^\circ$ or $180^\circ$, so $\sin\theta=0$.
2. **Perpendicular force:** If $\theta=90^\circ$, then $|\tau|=rF$, the largest possible torque magnitude for the given $r$ and $F$.
3. **Magnitude bound:** Since $0\leq\sin\theta\leq1$, every contribution must satisfy $|\tau|\leq rF$.
4. **Turning sense:** Imagine the object free to rotate. Label counterclockwise contributions positive and clockwise contributions negative before adding them.
5. **Units:** Torque is reported in $\mathrm{N\cdot m}$. Keep the unit written this way even though it has the same base dimensions as a joule; torque is a turning effect, not energy.

```quiz
type: radio
id: mct-p1-zero-line-action
content: |-
  Which force produces zero torque about the pivot $O$?
options:
- id: mct-p1-zero-line-action-a
  content: |-
    A nonzero force applied away from $O$ whose line of action passes directly through $O$
  correct: true
  feedback: |-
    The perpendicular distance from $O$ to this line of action is zero. Thus $\tau=F d_\perp=0$ even though both the force and the distance to its application point are nonzero.
- id: mct-p1-zero-line-action-b
  content: |-
    A nonzero force perpendicular to $\mathbf r$ at a point away from $O$
  feedback: |-
    A perpendicular force has $\theta=90^\circ$, so $|\tau|=rF$. For fixed nonzero $r$ and $F$, this is the maximum torque magnitude rather than zero.
- id: mct-p1-zero-line-action-c
  content: |-
    A nonzero force at $45^\circ$ to $\mathbf r$ at a point away from $O$
  feedback: |-
    Since $\sin45^\circ$ is nonzero, the force has a perpendicular component and produces torque of magnitude $rF\sin45^\circ$.
- id: mct-p1-zero-line-action-d
  content: |-
    Two forces whose torque magnitudes are unequal and whose turning senses oppose
  feedback: |-
    Opposing signs do not guarantee cancellation. Unequal torque magnitudes leave a nonzero net torque equal to their signed difference.
- id: mct-p1-zero-line-action-e
  content: |-
    A force whose line of action is farther from $O$ than another equal force's line of action
  feedback: |-
    A larger perpendicular distance increases $|\tau|=F d_\perp$. It cannot make the torque zero unless the force itself is zero.
```

---

<a id="summary"></a>
## Summary

- Mark the pivot and each force's line of action before calculating.
- Use either $\tau=F d_\perp$ with $d_\perp=r\sin\theta$, or $\tau=rF_\perp$ with $F_\perp=F\sin\theta$.
- The angle $\theta$ is the angle between $\mathbf r$ and $\mathbf F$.
- Assign the sign from turning sense: counterclockwise positive, clockwise negative.
- Add signed contributions rather than adding torque magnitudes.
- A line of action through the pivot gives zero torque; a perpendicular force gives the maximum magnitude $rF$.
- Check $|\tau|\leq rF$, the expected rotation direction, and units of $\mathrm{N\cdot m}$ before accepting a result.

<!-- lesson-nav:start -->
---

```update-progress
```

[[212/Home|Home]]
[[212/0. Table of Contents/TOC|Table of Contents]]

---
<!-- lesson-nav:end -->
