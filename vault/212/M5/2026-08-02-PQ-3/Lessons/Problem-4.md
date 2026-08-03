# Deriving Wave Speed on a Load-Bearing Wire

<!--
lesson-id: 212-M5-048
topic-code: MTH212.M5.48
-->

## Table of Contents

- [Introduction](#introduction)
- [Core Move 1: Read "Static" for Each Object](#read-static)
- [Core Move 2: Transfer the Hanging Load to the Shelf](#transfer-the-hanging-load-to-the-shelf)
- [Core Move 3: Build the Shelf's Extended Free-Body Diagram](#build-the-shelf-fbd)
- [Core Move 4: Turn the Diagram Into a Torque Equation](#write-the-torque-equation)
- [Core Move 5: Solve Symbolically for the Support-Wire Tension](#solve-for-support-wire-tension)
- [Optional: Recover the Single Hinge Force](#recover-the-hinge-force)
- [Core Move 6: Find the Support Wire's Actual Length](#find-the-wire-length)
- [Core Move 7: Convert Wire Mass Into Linear Density](#find-linear-density)
- [Core Move 8: Combine the Static and Wave Models](#combine-the-static-and-wave-models)
- [Separate Medium Data from Wave Data](#separate-medium-data-from-wave-data)
- [Complete Exam-Style Walkthrough](#exam-style-walkthrough)
- [Summary](#summary)

## Prerequisites

- Identify weight and tension forces.
- Know that $a=0$ means velocity is not changing and $\alpha=0$ means angular velocity is not changing.
- Use $\tau=rF\sin\phi$ and place the center of mass of a uniform shelf at $L/2$.
- Use $\cos\theta=(\text{adjacent})/(\text{hypotenuse})$.
- Divide by a fraction by multiplying by its reciprocal.
- Recognize $\mu=(\text{mass})/(\text{length})$ and $v=\sqrt{T/\mu}$.

---

<a id="introduction"></a>
## Introduction

This problem is not one formula substitution. It joins a statics problem, a geometry problem, and a traveling-wave problem.

A block of mass $m_2$ hangs from the end of a uniform shelf of mass $m_1$ and length $L$. A support wire of mass $m_w$ holds the shelf at angle $\theta$ and also carries a traveling wave.

![](<../Source/PQ3/Images/shelf-block-support-wire.png>)

The final wave model is familiar:

$$
v=\sqrt{\frac{T}{\mu}}.
$$

The difficulty is that neither input is given directly:

- The two static objects determine the support-wire tension $T$.
- The right-triangle geometry determines the support-wire length $L_w$.
- The wire mass and actual wire length determine $\mu$.

The complete dependency chain is

$$
\boxed{
\text{block equilibrium}
\longrightarrow T_s
\longrightarrow
\text{shelf torque balance}
\longrightarrow T
}
$$

$$
\boxed{
\text{wire geometry}
\longrightarrow L_w
\longrightarrow \mu
\longrightarrow
v=\sqrt{T/\mu}
}.
$$

There are also two different tensions:

| Symbol | Meaning |
| --- | --- |
| $T_s$ | Tension in the vertical string holding the block |
| $T$ | Tension in the diagonal support wire carrying the wave |

Do not set these equal. The block determines $T_s$; the shelf's torque balance determines $T$.

This lesson follows the supplied idealized model: the support wire is straight, has one uniform tension $T$, and contributes its mass only through $\mu$. Modeling the wire's distributed weight would require a different analysis with tension varying along the wire.

---

<a id="read-static"></a>
## Core Move 1: Read "Static" for Each Object

The word **static** does not mean that no forces act. It means the motion is not changing.

For any object whose center of mass is not accelerating,

$$
\sum\vec F_{\mathrm{ext}}
=M\vec a_{\mathrm{cm}}
=0.
$$

For an extended rigid object that is not angularly accelerating,

$$
\sum\tau_{\mathrm{ext}}
=I\alpha
=0.
$$

Apply those statements separately:

| Object | What static tells us | Equation used here |
| --- | --- | --- |
| Hanging block | $\vec a=0$ | $\sum F_y=0$ |
| Shelf | $\vec a_{\mathrm{cm}}=0$ and $\alpha=0$ | $\sum\vec F=0$ and $\sum\tau=0$ |

Both shelf equations are true. To find $T$, however, torque balance is the useful one: choosing the hinge as the pivot makes the unknown hinge forces contribute zero torque. Shelf force balance would instead be useful if the hinge reactions were requested.

These are equations for **different systems**. The block's force equation comes from the block's FBD; the shelf's torque equation comes from the shelf's extended FBD.

```quiz
type: radio
id: pq3-p4-static-meaning
content: |-
  The hanging block and shelf are both stationary. Which statement correctly translates that information into Newton's laws?
options:
- id: pq3-p4-static-meaning-a
  content: |-
    No forces act on either object.
  feedback: |-
    Static means the net force and net torque vanish, not that every individual force vanishes. Weight, tension, and hinge forces can all be nonzero while balancing one another.
- id: pq3-p4-static-meaning-b
  content: |-
    The block satisfies $\sum F_y=0$, while the shelf satisfies both $\sum\vec F=0$ and $\sum\tau=0$.
  correct: true
  feedback: |-
    The block has zero translational acceleration, so its forces balance. The rigid shelf has zero translational and angular acceleration, so both its net force and net torque are zero.
- id: pq3-p4-static-meaning-c
  content: |-
    Only the shelf's forces must balance; its torques can be nonzero because it is attached to a hinge.
  feedback: |-
    A hinge permits rotation but does not require it. Because the shelf remains at a fixed angle, $\alpha=0$ and its external torques must balance as well as its forces.
- id: pq3-p4-static-meaning-d
  content: |-
    The single equation $\sum F_y=0$ describes the block and the shelf together.
  feedback: |-
    The block and shelf must first be isolated as separate systems. The block needs its own force balance, while the extended shelf also needs rotational equilibrium, $\sum\tau=0$.
```

---

<a id="transfer-the-hanging-load-to-the-shelf"></a>
## Core Move 2: Transfer the Hanging Load to the Shelf

**Example:** A stationary block of mass $m_2$ hangs from a massless vertical string attached to the end of a shelf. What downward force does that string exert on the shelf?

**Explanation**

This is the first isolated system. Work only with the hanging block:

1. Choose upward as positive.
2. Draw the two forces on the block: upward $T_s$ and downward $m_2g$.
3. Use the block's zero acceleration.

Newton's second law gives

$$
\sum F_y=m_2a_y.
$$

Because the block is static, $a_y=0$, so

$$
0=T_s-m_2g.
$$

Add $m_2g$ to both sides:

$$
\boxed{T_s=m_2g}.
$$

This is the first equation you asked about. It belongs only to the hanging block and means that two nonzero forces balance; it does not mean the block has no forces.

Now transfer the result to the shelf. A massless string has the same tension throughout. At its upper attachment, the vertical string pulls **downward** on the shelf with magnitude

$$
T_s=m_2g.
$$

The corresponding Newton's-third-law partner is the shelf's upward force on the string.

Keep $T_s$ distinct from the diagonal support-wire tension $T$.

```quiz
type: radio
id: pq3-p4-q1
content: |-
  A stationary block of mass $m$ hangs from a massless vertical string attached to the end of a shelf. Which force from the string belongs on the shelf's extended free-body diagram?
options:
- id: q1-a
  content: |-
    An upward force $mg$ at the shelf's end
  feedback: |-
    This uses the direction of the string's force on the block. A taut vertical string pulls each attached object toward the string: upward on the block but downward on the shelf.
- id: q1-b
  content: |-
    A downward force $mg$ at the shelf's end
  correct: true
  feedback: |-
    Because the block is stationary, the massless-string tension is $T_s=mg$. At the upper attachment, that string pulls downward on the shelf at its end with the same tension magnitude.
- id: q1-c
  content: |-
    A downward force $mg/2$ at the shelf's center
  feedback: |-
    The block's full weight is transmitted as string tension, not halved. This force acts where the string attaches at the end; the force at the shelf's center is the shelf's own weight.
- id: q1-d
  content: |-
    No force, because the block is stationary
  feedback: |-
    Stationary means the block's net force is zero, not that each force is zero. Its weight is balanced by a nonzero string tension, and the string therefore exerts a downward force on the shelf.
```

---

<a id="build-the-shelf-fbd"></a>
## Core Move 3: Build the Shelf's Extended Free-Body Diagram

Now isolate the shelf as the second system. An ordinary FBD records force directions. An **extended** FBD must also record where each force acts, because torque depends on distance from the pivot.

![700](<../Source/PQ3/Images/shelf-block-free-body-diagrams-labeled.svg>)

The solid blue arrows are forces. The dashed blue arrows at the outer end show the parallel and perpendicular components of the same support-wire tension $T$; they are not additional forces.

The image follows the supplied solution by drawing the hinge reaction as one resultant force $F_p$. Its magnitude and its angle $\gamma$ above the shelf are initially unknown. The optional section after Core Move 5 shows how to recover both. The graded diagram should show the following information:

| Force on the shelf | Point of application | Direction |
| --- | --- | --- |
| Hinge reaction, $F_p$ | Wall hinge, $r=0$ | Up and right at an initially unknown angle $\gamma$ |
| Shelf weight, $m_1g$ | Shelf's center of mass, $r=L/2$ | Downward |
| Vertical-string force, $T_s=m_2g$ | Outer end, $r=L$ | Downward |
| Support-wire tension, $T$ | Outer end, $r=L$ | Along the wire, angle $\theta$ above the shelf |

Two distinctions matter:

- The downward end force is a **string force on the shelf**. Its magnitude happens to equal $m_2g$ because the separate block is static.
- The uniform shelf's own weight acts at $L/2$, not at the outer end.

On an exam, label the hinge as the chosen pivot, the distances $L/2$ and $L$, and the angle $\theta$. Those labels are what let you translate the picture into a torque equation.

```quiz
type: radio
id: pq3-p4-shelf-fbd
content: |-
  Which description gives the essential forces and locations for the shelf's extended free-body diagram?
options:
- id: pq3-p4-shelf-fbd-a
  content: |-
    Hinge reaction at $r=0$; $m_1g$ downward at $L/2$; $T_s=m_2g$ downward at $L$; and $T$ along the support wire at $L$.
  correct: true
  feedback: |-
    An extended FBD records both forces and application points. The uniform shelf's weight acts at its center, both string forces act at the outer end, and the hinge reaction acts at the pivot.
- id: pq3-p4-shelf-fbd-b
  content: |-
    Hinge reaction at $r=0$; both $m_1g$ and $m_2g$ downward at $L/2$; and $T$ vertically upward at $L$.
  feedback: |-
    This moves the hanging load to the shelf's center and changes the direction of the diagonal tension. The block's string pulls at the outer end, while $T$ must point along the support wire.
- id: pq3-p4-shelf-fbd-c
  content: |-
    $m_1g$ downward at $L$; $T_s=m_2g$ upward at $L$; and $T$ along the support wire at $L$.
  feedback: |-
    The shelf's weight belongs at its center, $L/2$, and the vertical string pulls downward on the shelf. The upward string force belongs on the block's FBD, not the shelf's.
- id: pq3-p4-shelf-fbd-d
  content: |-
    Only $m_1g$, $m_2g$, and $T$ should be shown because the hinge force produces no torque.
  feedback: |-
    The hinge reaction still acts on the shelf and belongs on a complete FBD. Choosing the hinge as the torque pivot later makes its torque zero; that does not make the force itself disappear.
```

---

<a id="write-the-torque-equation"></a>
## Core Move 4: Turn the Diagram Into a Torque Equation

The shelf is not rotating, so

$$
\sum\tau_{\text{hinge}}=I\alpha=0.
$$

Choose the hinge as the pivot. This is strategic: the unknown hinge reaction acts at $r=0$, so its torque is automatically zero.

Let counterclockwise torque be positive. For this horizontal shelf, it is easiest to use

$$
\tau=rF_{\perp},
$$

where $F_{\perp}$ is the force component perpendicular to the shelf.

The diagonal tension has a component parallel to the shelf and a component perpendicular to it:

$$
T_{\parallel}=T\cos\theta,
\qquad
T_{\perp}=T\sin\theta.
$$

$T_{\parallel}$ points toward the hinge, so its line of action passes through the pivot and it produces no torque. $T_{\perp}$ points upward and turns the shelf counterclockwise.

| Force | Lever arm and perpendicular component | Rotation | Torque term |
| --- | --- | --- | ---: |
| Hinge reaction | $r=0$ | None | $0$ |
| Support wire | $r=L$, $F_\perp=T\sin\theta$ | Counterclockwise | $+LT\sin\theta$ |
| Shelf weight | $r=L/2$, $F_\perp=m_1g$ | Clockwise | $-m_1g(L/2)$ |
| Vertical string | $r=L$, $F_\perp=T_s$ | Clockwise | $-T_sL$ |

Write one term for every force in the table:

$$
0
=LT\sin\theta
-m_1g\frac{L}{2}
-T_sL.
$$

Now substitute the result from the block, $T_s=m_2g$:

$$
\boxed{
0
=LT\sin\theta
-m_1g\frac{L}{2}
-m_2gL
}.
$$

This is the second equation you asked about. It is not another equation for the block: it is the shelf's rotational form of Newton's second law, $\sum\tau=I\alpha=0$.

If clockwise is chosen as positive instead, every sign reverses:

$$
0
=m_1g\frac{L}{2}
+m_2gL
-TL\sin\theta.
$$

These are the same physical equation multiplied by $-1$.

The other form you encountered,

$$
0=m_1g+2m_2g-2T\sin\theta,
$$

comes from multiplying the clockwise-positive equation by $2/L$. No new force or new physics has been introduced; the equation has only been rescaled.

```quiz
type: radio
id: pq3-p4-torque-equation
content: |-
  Counterclockwise torque is positive. Which equation correctly represents rotational equilibrium of the shelf about the hinge?
options:
- id: pq3-p4-torque-equation-a
  content: |-
    $0=LT\sin\theta-m_1g\dfrac{L}{2}-m_2gL$
  correct: true
  feedback: |-
    The wire's vertical component $T\sin\theta$ acts at $L$ and turns counterclockwise. The shelf weight acts at $L/2$ and the hanging load acts at $L$; both turn clockwise.
- id: pq3-p4-torque-equation-b
  content: |-
    $0=LT\cos\theta-m_1g\dfrac{L}{2}-m_2gL$
  feedback: |-
    $T\cos\theta$ is parallel to the shelf, so its line of action produces no torque about the hinge. The perpendicular component is $T\sin\theta$.
- id: pq3-p4-torque-equation-c
  content: |-
    $0=LT\sin\theta-m_1gL-m_2gL$
  feedback: |-
    This assigns the full lever arm $L$ to the shelf's weight. A uniform shelf's center of mass is at $L/2$, so its torque magnitude is $m_1g(L/2)$.
- id: pq3-p4-torque-equation-d
  content: |-
    $0=T\sin\theta-m_1g\dfrac{L}{2}-m_2gL$
  feedback: |-
    Every term in a torque equation must have force-times-distance units. The tension term is missing its lever arm $L$, so it has force units and cannot be added to the two torque terms.
```

---

<a id="solve-for-support-wire-tension"></a>
## Core Move 5: Solve Symbolically for the Support-Wire Tension

The target in this stage is the diagonal tension $T$. Treat $m_1$, $m_2$, $g$, $L$, and $\theta$ as known while isolating it.

Start from the torque equation:

$$
LT\sin\theta
-m_1g\frac{L}{2}
-m_2gL
=0.
$$

Move the two clockwise terms to the other side:

$$
LT\sin\theta
=m_1g\frac{L}{2}+m_2gL.
$$

Every term contains $L$, so divide by $L$:

$$
T\sin\theta
=\frac{m_1g}{2}+m_2g.
$$

Factor out $g$:

$$
T\sin\theta
=\left(\frac{m_1}{2}+m_2\right)g.
$$

Put the two mass terms over a common denominator:

$$
\frac{m_1}{2}+m_2
=\frac{m_1}{2}+\frac{2m_2}{2}
=\frac{m_1+2m_2}{2}.
$$

Finally, divide by $\sin\theta$:

$$
\boxed{
T
=\frac{\left(\dfrac{m_1}{2}+m_2\right)g}{\sin\theta}
=\frac{(m_1+2m_2)g}{2\sin\theta}
}.
$$

The factor $2m_2$ does **not** mean that there are two blocks. It appears only because the shelf's weight acts at half the block's lever arm. Algebraically, it comes from clearing the denominator in $m_1/2+m_2$.

A physical check supports the result: as $\theta$ becomes smaller, the support wire becomes more horizontal, $\sin\theta$ becomes smaller, and a larger total tension is required to supply the same upward component.

```quiz
type: radio
id: pq3-p4-q2
content: |-
  Torque balance for a shelf and hanging load has been simplified to $T\sin\alpha=\left(\dfrac{M}{2}+m\right)g$. Which expression correctly isolates $T$?
options:
- id: q2-a
  content: |-
    $\dfrac{(M+2m)g}{2\sin\alpha}$
  correct: true
  feedback: |-
    Divide both sides by $\sin\alpha$, then combine $M/2+m=(M+2m)/2$. This gives $T=(M+2m)g/(2\sin\alpha)$.
- id: q2-b
  content: |-
    $\dfrac{(M+m)g}{\sin\alpha}$
  feedback: |-
    This replaces $M/2+m$ with $M+m$. The shelf term still carries the factor $1/2$; using a common denominator gives $(M+2m)/2$, not $M+m$.
- id: q2-c
  content: |-
    $\dfrac{(M+2m)g}{2\cos\alpha}$
  feedback: |-
    The equation being solved contains $T\sin\alpha$, so isolating $T$ requires division by $\sin\alpha$. Replacing it with cosine changes the given equation rather than solving it.
- id: q2-d
  content: |-
    $\dfrac{(2M+m)g}{2\sin\alpha}$
  feedback: |-
    This combines the mass terms incorrectly. Writing $M/2+m$ over a common denominator gives $(M+2m)/2$; the factor of $2$ belongs with $m$, not with $M$.
```

---

<a id="recover-the-hinge-force"></a>
## Optional: Recover the Single Hinge Force

Choosing the hinge as the torque pivot made the torque from $F_p$ vanish because its lever arm is zero. It did **not** make the hinge force itself zero. Once torque balance has determined $T$, the shelf's two force-balance equations can determine the magnitude and direction of $F_p$.

Choose $+x$ to the right and $+y$ upward. Let $\gamma$ be the angle that the single hinge force $F_p$ makes above the horizontal shelf. Its projections are

$$
F_{p,x}=F_p\cos\gamma,
\qquad
F_{p,y}=F_p\sin\gamma.
$$

These are components of the **one** force $F_p$, not additional forces on the FBD.

### Step 1: Find the Horizontal Component

The support wire pulls left with horizontal component $T\cos\theta$, while the hinge pushes right. Horizontal equilibrium gives

$$
\sum F_x=0,
$$

$$
0=F_p\cos\gamma-T\cos\theta.
$$

Therefore,

$$
F_{p,x}=F_p\cos\gamma=T\cos\theta.
$$

Substitute the tension already found from torque balance:

$$
\begin{aligned}
F_{p,x}
&=\frac{(m_1+2m_2)g}{2\sin\theta}\cos\theta\\
&=\boxed{\frac{(m_1+2m_2)g}{2}\cot\theta}.
\end{aligned}
$$

### Step 2: Find the Vertical Component

The upward forces on the shelf are $F_p\sin\gamma$ and $T\sin\theta$. The downward forces are the shelf's weight $m_1g$ and the vertical-string force $T_s=m_2g$. Thus,

$$
\sum F_y=0,
$$

$$
0
=F_p\sin\gamma
+T\sin\theta
-m_1g
-m_2g.
$$

Solve for the vertical hinge-force component:

$$
F_{p,y}=F_p\sin\gamma
=(m_1+m_2)g-T\sin\theta.
$$

The torque calculation already established that

$$
T\sin\theta
=\left(\frac{m_1}{2}+m_2\right)g.
$$

Substitute this result:

$$
\begin{aligned}
F_{p,y}
&=(m_1+m_2)g
-\left(\frac{m_1}{2}+m_2\right)g\\
&=\boxed{\frac{m_1g}{2}}.
\end{aligned}
$$

The support wire supplies the upward force needed for the entire hanging load and half of the uniform shelf's weight. The hinge supplies the remaining half of the shelf's weight.

### Step 3: Reconstruct the Magnitude

The perpendicular components form a right triangle whose hypotenuse is $F_p$:

$$
F_p=\sqrt{F_{p,x}^2+F_{p,y}^2}.
$$

Substitute the two component results:

$$
\begin{aligned}
F_p
&=\sqrt{
\left[
\frac{(m_1+2m_2)g}{2}\cot\theta
\right]^2
+\left(\frac{m_1g}{2}\right)^2
}\\
&=\boxed{
\frac{g}{2}
\sqrt{(m_1+2m_2)^2\cot^2\theta+m_1^2}
}.
\end{aligned}
$$

### Step 4: Reconstruct the Direction

Because $\gamma$ is measured above the horizontal,

$$
\tan\gamma
=\frac{F_{p,y}}{F_{p,x}}.
$$

Substitute the components and simplify:

$$
\begin{aligned}
\tan\gamma
&=
\frac{m_1g/2}
{[(m_1+2m_2)g/2]\cot\theta}\\
&=\frac{m_1}{m_1+2m_2}\tan\theta.
\end{aligned}
$$

Therefore, the direction of the hinge force is

$$
\boxed{
\gamma
=\tan^{-1}\!\left(
\frac{m_1}{m_1+2m_2}\tan\theta
\right)
}
$$

above the horizontal shelf. For the acute angle shown, both components are positive, so $F_p$ points up and right as drawn. The magnitude has units of force, and neither $F_p$ nor $\gamma$ is needed to find the requested wave speed; this calculation is only required if the hinge reaction is requested.

---

<a id="find-the-wire-length"></a>
## Core Move 6: Find the Support Wire's Actual Length

The symbol $L$ labels the horizontal shelf length, not the slanted wire length. Let the actual wire length be $L_w$.

Relative to the angle $\theta$:

- the shelf length $L$ is the adjacent side;
- the wire length $L_w$ is the hypotenuse.

Cosine is the ratio that connects those two sides:

$$
\cos\theta
=\frac{\text{adjacent}}{\text{hypotenuse}}
=\frac{L}{L_w}.
$$

Now solve for $L_w$. Multiply both sides by $L_w$:

$$
L_w\cos\theta=L.
$$

Divide by $\cos\theta$:

$$
\boxed{L_w=\frac{L}{\cos\theta}}.
$$

This passes a geometric check. For an acute nonzero angle, $0<\cos\theta<1$, so

$$
L_w=\frac{L}{\cos\theta}>L.
$$

The slanted hypotenuse must be longer than its horizontal projection.

```quiz
type: radio
id: pq3-p4-wire-length
content: |-
  A support wire makes angle $\beta$ with a horizontal shelf of length $d$. The shelf is the adjacent side and the wire is the hypotenuse. What is the wire's actual length $L_w$?
options:
- id: pq3-p4-wire-length-a
  content: |-
    $L_w=d\cos\beta$
  feedback: |-
    Multiplying by $\cos\beta<1$ would make the hypotenuse shorter than the adjacent side. Since $\cos\beta=d/L_w$, solving gives $L_w=d/\cos\beta$.
- id: pq3-p4-wire-length-b
  content: |-
    $L_w=\dfrac{d}{\cos\beta}$
  correct: true
  feedback: |-
    Cosine relates the adjacent shelf length to the wire hypotenuse: $\cos\beta=d/L_w$. Isolating the hypotenuse gives $L_w=d/\cos\beta>d$.
- id: pq3-p4-wire-length-c
  content: |-
    $L_w=d\sin\beta$
  feedback: |-
    Sine relates the opposite side to the hypotenuse, but the known shelf length is adjacent to $\beta$. Use cosine, then divide $d$ by $\cos\beta$.
- id: pq3-p4-wire-length-d
  content: |-
    $L_w=\dfrac{\cos\beta}{d}$
  feedback: |-
    This has inverse-length units and cannot represent a length. Solving the dimensionless ratio $\cos\beta=d/L_w$ gives $L_w=d/\cos\beta$.
```

---

<a id="find-linear-density"></a>
## Core Move 7: Convert Wire Mass Into Linear Density

Linear mass density means mass per **actual wire length**:

$$
\mu=\frac{m_w}{L_w}.
$$

Substitute $L_w=L/\cos\theta$:

$$
\mu
=\frac{m_w}{L/\cos\theta}.
$$

Dividing by $L/\cos\theta$ means multiplying by its reciprocal, $\cos\theta/L$:

$$
\mu
=m_w\left(\frac{\cos\theta}{L}\right).
$$

Therefore,

$$
\boxed{\mu=\frac{m_w\cos\theta}{L}}.
$$

The units are $\mathrm{kg/m}$. The geometry also gives a useful check: because $L_w>L$, the actual density $m_w/L_w$ must be smaller than the incorrect value $m_w/L$ obtained by treating the shelf as the wire.

```quiz
type: radio
id: pq3-p4-q3
content: |-
  A straight wire of mass $m$ spans a horizontal distance $d$ while making angle $\beta$ with the horizontal. What is its linear mass density?
options:
- id: q3-a
  content: |-
    $\dfrac{m}{d}$
  feedback: |-
    This treats the horizontal span $d$ as the wire's full length. The slanted wire is the hypotenuse, $L_w=d/\cos\beta>d$, so its density is smaller than $m/d$.
- id: q3-b
  content: |-
    $\dfrac{m}{d\cos\beta}$
  feedback: |-
    This divides by $d\cos\beta$, which would make the wire shorter than its horizontal span. The wire length is $d/\cos\beta$, so dividing $m$ by that length multiplies by $\cos\beta$.
- id: q3-c
  content: |-
    $\dfrac{m\cos\beta}{d}$
  correct: true
  feedback: |-
    The wire is the hypotenuse, so its length is $L_w=d/\cos\beta$. Linear density is mass per actual wire length; therefore $\mu=m/L_w=m\cos\beta/d$.
- id: q3-d
  content: |-
    $\dfrac{m\sin\beta}{d}$
  feedback: |-
    The known horizontal span $d$ is adjacent to $\beta$, so it is related to the hypotenuse by cosine. Sine would be appropriate if the vertical rise, rather than the horizontal span, were given.
```

---

<a id="combine-the-static-and-wave-models"></a>
## Core Move 8: Combine the Static and Wave Models

**Example:** A block of mass $m_2$ hangs from the end of a uniform shelf of mass $m_1$ and length $L$. A uniform support wire of mass $m_w$ makes angle $\theta$ with the shelf. Find the speed of a traveling transverse wave on the wire.

![](<../Source/PQ3/Images/shelf-block-support-wire.png>)

**Explanation**

At this stage, the wave equation has two input slots:

$$
v=\sqrt{\frac{\boxed{T}}{\boxed{\mu}}}.
$$

Earlier stages produced one expression for each slot:

$$
T=\frac{(m_1+2m_2)g}{2\sin\theta},
$$

$$
\mu=\frac{m_w\cos\theta}{L}.
$$

Substitute both expressions without skipping the compound fraction:

$$
v
=\sqrt{
\frac{
\dfrac{(m_1+2m_2)g}{2\sin\theta}
}{
\dfrac{m_w\cos\theta}{L}
}
}.
$$

Dividing by $m_w\cos\theta/L$ means multiplying by its reciprocal:

$$
v
=\sqrt{
\frac{(m_1+2m_2)g}{2\sin\theta}
\left(\frac{L}{m_w\cos\theta}\right)
}.
$$

Now multiply the numerators and denominators:

$$
\boxed{
v=\sqrt{
\frac{(m_1+2m_2)gL}
{2m_w\sin\theta\cos\theta}
}
}.
$$

Every factor has a traceable source:

| Factor | Origin |
| --- | --- |
| $m_1+2m_2$ and $\sin\theta$ | Shelf torque balance |
| $L$ and $\cos\theta$ | Actual wire length and linear density |
| $m_w$ | Wire mass in $\mu$ |
| Square root | Traveling-wave model $v=\sqrt{T/\mu}$ |

For the unit check, the trigonometric factors and $2$ are dimensionless:

$$
\frac{
(\mathrm{kg})(\mathrm{m/s^2})(\mathrm{m})
}{
\mathrm{kg}
}
=\frac{\mathrm{m^2}}{\mathrm{s^2}}.
$$

Taking the square root gives $\mathrm{m/s}$, as required for speed.

```quiz
type: radio
id: pq3-p4-substitute-t-mu
content: |-
  After deriving $T=\dfrac{(m_1+2m_2)g}{2\sin\theta}$ and $\mu=\dfrac{m_w\cos\theta}{L}$, which is the correct unsimplified substitution into $v=\sqrt{T/\mu}$?
options:
- id: pq3-p4-substitute-t-mu-a
  content: |-
    $\displaystyle v=\sqrt{\frac{\dfrac{(m_1+2m_2)g}{2\sin\theta}}{\dfrac{m_w\cos\theta}{L}}}$
  correct: true
  feedback: |-
    The entire derived tension belongs in the numerator and the entire linear density belongs in the denominator. Dividing by $m_w\cos\theta/L$ then introduces its reciprocal, $L/(m_w\cos\theta)$.
- id: pq3-p4-substitute-t-mu-b
  content: |-
    $\displaystyle v=\sqrt{\frac{(m_1+2m_2)g}{2\sin\theta}\frac{m_w\cos\theta}{L}}$
  feedback: |-
    This multiplies by $\mu$ instead of dividing by it. Because $v=\sqrt{T/\mu}$, the density factor must be inverted to $L/(m_w\cos\theta)$.
- id: pq3-p4-substitute-t-mu-c
  content: |-
    $\displaystyle v=\sqrt{\frac{\dfrac{m_w\cos\theta}{L}}{\dfrac{(m_1+2m_2)g}{2\sin\theta}}}$
  feedback: |-
    This reverses the wave-speed ratio and computes $\sqrt{\mu/T}$. Tension belongs above density in $v=\sqrt{T/\mu}$.
- id: pq3-p4-substitute-t-mu-d
  content: |-
    $\displaystyle v=\sqrt{\frac{\dfrac{(m_1+2m_2)g}{2\sin\theta}}{\dfrac{m_wL}{\cos\theta}}}$
  feedback: |-
    This uses the wrong linear density. Since the actual wire length is $L/\cos\theta$, $\mu=m_w/(L/\cos\theta)=m_w\cos\theta/L$.
```

### Optional Numerical Transfer

The original practice-quiz problem itself asks for a symbolic result. Use this numerical variant only after you can reproduce the symbolic chain, and substitute numbers only at the end.

```quiz
type: radio
id: pq3-p4-q4
content: |-
  A $4.00\ \mathrm{kg}$ uniform shelf is $3.00\ \mathrm{m}$ long and supports a $2.00\ \mathrm{kg}$ block at its end. A $1.50\ \mathrm{kg}$ support wire makes a $30.0^\circ$ angle with the shelf. Using $g=9.80\ \mathrm{m/s^2}$, what is the traveling-wave speed on the wire?
options:
- id: q4-a
  content: |-
    $6.73\ \mathrm{m/s}$
  feedback: |-
    This results if the support-wire tension is replaced by the hanging block's weight, $19.6\ \mathrm{N}$. That is the tension in the block's vertical string, not in the diagonal wire; shelf torque balance gives $T=78.4\ \mathrm{N}$ and hence $v=13.5\ \mathrm{m/s}$.
- id: q4-b
  content: |-
    $9.80\ \mathrm{m/s}$
  feedback: |-
    This reuses the numerical value of $g$, but acceleration due to gravity is not the wave speed. Gravity helps determine the wire tension; the requested speed is then $v=\sqrt{T/\mu}=13.5\ \mathrm{m/s}$.
- id: q4-c
  content: |-
    $13.5\ \mathrm{m/s}$
  correct: true
  feedback: |-
    The shelf and block set the support tension: $T=78.4\ \mathrm{N}$. The wire's actual slanted length sets $\mu=(1.5\cos30^\circ)/3.0=0.433\ \mathrm{kg/m}$, so $v=\sqrt{T/\mu}=13.5\ \mathrm{m/s}$.
- id: q4-d
  content: |-
    $19.6\ \mathrm{m/s}$
  feedback: |-
    This copies the numerical value of the block's weight, $mg=19.6\ \mathrm{N}$, into a speed answer. A force is not a wave speed; use the diagonal-wire tension $78.4\ \mathrm{N}$ and density $0.433\ \mathrm{kg/m}$ in $\sqrt{T/\mu}$ to get $13.5\ \mathrm{m/s}$.
```

---

<a id="separate-medium-data-from-wave-data"></a>
## Separate Medium Data from Wave Data

**Example:** The support wire is plucked with amplitude $A$ and wavelength $\lambda$. Are either needed to determine the speed once $T$ and $\mu$ are known?

**Explanation**

The problem gives amplitude $A$ and wavelength $\lambda$, but the requested propagation speed is already determined by the medium:

$$
v=\sqrt{\frac{T}{\mu}}.
$$

- Amplitude $A$ describes the size of the wire's transverse displacement. It does not change $T$ or $\mu$ in the ideal linear model.
- Wavelength $\lambda$ could be paired with frequency through $v=f\lambda$, but $f$ is not given and is unnecessary once $T$ and $\mu$ are known.
- "No reflections" means the problem describes one traveling wave. Do not impose a standing-wave condition such as $L_w=n\lambda/2$.

The data are not meaningless in every possible question. For example, $A$ would matter for wave energy or maximum transverse particle speed, and $\lambda$ would matter if frequency were requested. They simply do not control the propagation speed asked for here.

```quiz
type: radio
id: pq3-p4-q5
content: |-
  The support wire carries a sinusoidal wave of amplitude $A$ and wavelength $\lambda$, and the problem says there are no reflections. How should these facts be used when finding the propagation speed?
options:
- id: q5-a
  content: |-
    Use $A$ to increase the tension, then calculate $v=\sqrt{T/\mu}$.
  feedback: |-
    In the ideal linear-wave model, amplitude describes transverse displacement and does not change the wire's static support tension. The speed is determined by the separately derived $T$ and $\mu$.
- id: q5-b
  content: |-
    Use $L_w=n\lambda/2$ because the endpoints fix a standing-wave pattern.
  feedback: |-
    The problem explicitly removes reflections, so no standing wave is formed and no harmonic condition applies. Use the traveling-wave relation $v=\sqrt{T/\mu}$ instead.
- id: q5-c
  content: |-
    Neither $A$ nor $\lambda$ is needed; "no reflections" rules out standing-wave conditions, so use $v=\sqrt{T/\mu}$.
  correct: true
  feedback: |-
    Propagation speed on the ideal wire is fixed by its tension and linear density. Amplitude and wavelength describe the wave, while "no reflections" confirms that no standing-wave boundary condition should be imposed.
- id: q5-d
  content: |-
    First calculate $f=v/\lambda$, then use that frequency to determine $v$.
  feedback: |-
    This is circular because it uses the unknown speed to calculate a frequency and then tries to recover the same speed. The medium properties $T$ and $\mu$ determine $v$ directly; $f$ would adjust to satisfy $v=f\lambda$.
```

---

<a id="exam-style-walkthrough"></a>
## Complete Exam-Style Walkthrough

The original task is a written derivation problem. A final memorized formula is not a substitute for the diagrams and equations that produce it.

Use the two parts below as a closed-notes rehearsal. Complete each one on paper before reading its model response.

### Part A — Draw the Diagrams

A block of mass $m_2$ hangs from a massless string at the end of a uniform shelf of mass $m_1$ and length $L$. The shelf is pivoted at the wall and supported at its outer end by a uniform wire of mass $m_w$ that makes an angle $\theta$ with the shelf.

Draw a free-body diagram of the hanging block and a completely labeled extended free-body diagram of the shelf.

![](<../Source/PQ3/Images/shelf-block-support-wire.png>)

> [!answer]- Model response
>
> ![](<../Source/PQ3/Images/shelf-block-free-body-diagrams-labeled.svg>)
>
> The block FBD must show $T_s$ upward and $m_2g$ downward.
>
> The shelf's extended FBD must show the hinge or pivot; the single hinge reaction $F_p$ at $r=0$, directed up and right at an initially unknown angle $\gamma$; $m_1g$ downward at $L/2$; $T_s=m_2g$ downward at $L$; and $T$ at $L$, directed along the support wire at angle $\theta$ above the shelf.
>
> Label the lever arms $L/2$ and $L$ and state a torque-sign convention. Do not omit the hinge reaction merely because its torque about the hinge will later be zero.

### Part B — Derive the Wave Speed

The support wire is plucked, producing a traveling sinusoidal wave of amplitude $A$ and wavelength $\lambda$. Assume there are no reflections.

Starting from Newton's laws, derive the wave speed completely symbolically in terms of $m_1$, $m_2$, $m_w$, $g$, $L$, and $\theta$. Show the equations that would need to appear on a graded solution.

> [!answer]- Model response
>
> For the static hanging block,
>
> $$
> \sum F_y=0
> \quad\Longrightarrow\quad
> 0=T_s-m_2g
> \quad\Longrightarrow\quad
> T_s=m_2g.
> $$
>
> For the static shelf, take counterclockwise torque as positive and choose the hinge as the pivot:
>
> $$
> \sum\tau_{\mathrm{hinge}}=0.
> $$
>
> Therefore,
>
> $$
> 0
> =LT\sin\theta
> -m_1g\frac{L}{2}
> -T_sL.
> $$
>
> Substitute $T_s=m_2g$ and solve for $T$:
>
> $$
> LT\sin\theta
> =m_1g\frac{L}{2}+m_2gL,
> $$
>
> $$
> T
> =\frac{\left(\dfrac{m_1}{2}+m_2\right)g}{\sin\theta}
> =\frac{(m_1+2m_2)g}{2\sin\theta}.
> $$
>
> The wire is the hypotenuse of the right triangle:
>
> $$
> \cos\theta=\frac{L}{L_w}
> \quad\Longrightarrow\quad
> L_w=\frac{L}{\cos\theta}.
> $$
>
> Therefore,
>
> $$
> \mu
> =\frac{m_w}{L_w}
> =\frac{m_w}{L/\cos\theta}
> =\frac{m_w\cos\theta}{L}.
> $$
>
> Substitute both derived inputs into the traveling-wave equation:
>
> $$
> \begin{aligned}
> v
> &=\sqrt{\frac{T}{\mu}}\\
> &=\sqrt{
> \frac{
> \dfrac{(m_1+2m_2)g}{2\sin\theta}
> }{
> \dfrac{m_w\cos\theta}{L}
> }
> }\\
> &=\boxed{
> \sqrt{
> \frac{(m_1+2m_2)gL}
> {2m_w\sin\theta\cos\theta}
> }
> }.
> \end{aligned}
> $$
>
> The result has units $\mathrm{m/s}$. Neither $A$ nor $\lambda$ is required, and "no reflections" rules out standing-wave boundary conditions.

---

<a id="summary"></a>
## Summary

This synthesis contains eight core moves:

1. Translate static into $\sum\vec F=0$ and, for the shelf, $\sum\tau=0$.
2. Isolate the block and derive $T_s=m_2g$.
3. Transfer the downward force $T_s$ to the shelf's extended FBD.
4. Choose the hinge as pivot and build every signed torque term.
5. Solve the torque equation for
   $$
   T=\frac{(m_1+2m_2)g}{2\sin\theta}.
   $$
   If the hinge reaction is requested, return to $\sum F_x=0$ and $\sum F_y=0$ after finding $T$; these give the components needed to reconstruct the single force $F_p$ and its direction.
6. Use the right triangle to derive
   $$
   L_w=\frac{L}{\cos\theta}.
   $$
7. Convert wire mass to
   $$
   \mu=\frac{m_w\cos\theta}{L}.
   $$
8. Substitute both derived inputs into $v=\sqrt{T/\mu}$.

The final result is

$$
\boxed{
v=\sqrt{
\frac{(m_1+2m_2)gL}
{2m_w\sin\theta\cos\theta}
}
}.
$$

On a graded page, show the following rather than writing only the boxed result:

- the block FBD and the shelf's labeled extended FBD;
- $0=T_s-m_2g$;
- the complete hinge-torque equation;
- the symbolic algebra leading to $T$;
- $\cos\theta=L/L_w$ and the derivation of $\mu$;
- the unsimplified substitution into $v=\sqrt{T/\mu}$;
- a unit check and numbers only at the end.

The main traps are confusing $T_s$ with $T$, forgetting that static means both force and torque balance for the shelf, putting $m_1g$ at $L$ instead of $L/2$, using $T\cos\theta$ instead of $T\sin\theta$ in the torque, and using shelf length instead of actual wire length in $\mu$.

<!-- lesson-nav:start -->
---

```update-progress
```

[[212/Home|Home]]
[[212/0. Table of Contents/TOC|Table of Contents]]

[Quiz 3 Study Guide](../../2026-08-03-Q-3/Study-Guide.md)
Next: [Locate a Listener on a Circular Wavefront](../../2026-07-27-M5-2/Lessons/Problem-4.md)

Study guide index: 13/28

---
<!-- lesson-nav:end -->
