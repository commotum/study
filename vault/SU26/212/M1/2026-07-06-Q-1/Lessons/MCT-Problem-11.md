# Writing Tension Equations at the Top, Bottom, and Side of a Vertical Circle

<!--
lesson-id: 212-M1-085
topic-code: MTH212.M1.85
-->

## Table of Contents

- [Introduction](#introduction)
- [Aim Inward at Each Location](#aim-inward-at-each-location)
- [Source-Video Problem 1: Top](#source-video-problem-1-top)
- [Source-Video Problem 1: Bottom](#source-video-problem-1-bottom)
- [Source-Video Problem 1: Side](#source-video-problem-1-side)
- [Rank the Tensions at Equal Speed](#rank-the-tensions-at-equal-speed)
- [Summary](#summary)

## Prerequisites

- Draw only real forces on a free-body diagram.
- Know that tension in a taut rope points along the rope toward its anchor.
- Use $a_r=v^2/r$ and write Newton's second law in the radial direction as $\sum F_r=mv^2/r$.
- Distinguish the inward radial direction from the perpendicular tangential direction.

---

<a id="introduction"></a>
## Introduction

When a mass on a rope moves in a **vertical circle** and the question asks for tension at the top, bottom, or side, first project every force onto the inward radial direction. The location determines whether weight helps, opposes, or has no component along the radius.

Follow this sequence:

1. Locate the circle's center and point $+r$ inward from the mass.
2. Draw tension toward the anchor and weight straight down.
3. Assign signs to the radial components only.
4. Write $\sum F_r=mv^2/r$ and isolate $T$ before inserting numbers.

For a fixed vertical circle, the three equations are:

| Location | Radial role of weight | Inward-positive equation | Tension |
|---|---|---|---|
| Top | Inward | $T+mg=mv^2/r$ | $T=mv^2/r-mg$ |
| Bottom | Outward | $T-mg=mv^2/r$ | $T=mv^2/r+mg$ |
| Side | Perpendicular to radius | $T=mv^2/r$ | $T=mv^2/r$ |

The speed $v$ in each row is the speed at that location. Do not assume those speeds are equal unless the problem says so.

At the side, gravity is tangential. Without another tangential force, gravity changes the mass's speed. A claim of constant speed all the way around the vertical circle therefore requires an external tangential agent to cancel gravity's tangential component away from the top and bottom.

---

<a id="aim-inward-at-each-location"></a>
## Aim Inward at Each Location

**Example:** Write the radial force equation for a mass at the top, bottom, and right side of a vertical circle without using a memorized location formula.

**Explanation**

The inward direction changes as the mass moves, but tension always points inward along the taut rope:

```text
Top:                    ● mass
                        ↓ T, mg, +r
                        ⊙ center

Right side:   ⊙ center ← T, +r — ● mass
                                    ↓ mg (tangential)

Bottom:                 ⊙ center
                        ↑ T, +r
                        ● mass
                        ↓ mg
```

- At the top, $T$ and $mg$ both point inward: $T+mg=mv^2/r$.
- At the bottom, $T$ points inward and $mg$ points outward: $T-mg=mv^2/r$.
- At the side, $T$ is inward while $mg$ is perpendicular to the radius: $T=mv^2/r$.

The quantity $mv^2/r$ is the required inward net force. It is not a separate force arrow.

```quiz
type: radio
id: mct-p11-location-equations
content: |-
  Which set of inward-positive radial equations is correct for a mass on a taut rope at the top, bottom, and side of a fixed vertical circle?
options:
- id: mct-p11-location-equations-a
  content: |-
    Top: $T+mg=\dfrac{mv^2}{r}$; bottom: $T-mg=\dfrac{mv^2}{r}$; side: $T=\dfrac{mv^2}{r}$
  correct: true
  feedback: |-
    Tension points inward at all three locations. Weight is inward at the top, outward at the bottom, and perpendicular to the radius at the side, giving the three stated equations.
- id: mct-p11-location-equations-b
  content: |-
    Top: $T-mg=\dfrac{mv^2}{r}$; bottom: $T+mg=\dfrac{mv^2}{r}$; side: $T=\dfrac{mv^2}{r}$
  feedback: |-
    This reverses gravity's radial sign at the top and bottom. Gravity points toward the center at the top but away from the center at the bottom.
- id: mct-p11-location-equations-c
  content: |-
    Top, bottom, and side: $T=\dfrac{mv^2}{r}$
  feedback: |-
    This omits gravity's radial component at the top and bottom. Only at the exact side is gravity perpendicular to the radius and absent from the radial equation.
- id: mct-p11-location-equations-d
  content: |-
    Top: $T+mg=\dfrac{mv^2}{r}$; bottom: $T-mg=\dfrac{mv^2}{r}$; side: $T+mg=\dfrac{mv^2}{r}$
  feedback: |-
    At the side, weight is vertical while the radius is horizontal, so gravity's radial projection is zero. Weight belongs in the tangential equation there, not the radial equation.
- id: mct-p11-location-equations-e
  content: |-
    Top: $T+mg+\dfrac{mv^2}{r}=0$; bottom: $T-mg+\dfrac{mv^2}{r}=0$; side: $T+\dfrac{mv^2}{r}=0$
  feedback: |-
    This treats $mv^2/r$ as another force. It is the inward net-force value from Newton's second law, so the real radial forces must equal it rather than be added to it.
```

---

<a id="source-video-problem-1-top"></a>
## Source-Video Problem 1: Top

**Example:** In the source video's top case (4:03–6:15), a $0.25\,\mathrm{kg}$ mass moves at $15\,\mathrm{m/s}$ on a $1.5\,\mathrm m$ rope. Find the tension at the top of its vertical circle.

**Explanation**

At the top, inward is downward. Both tension and weight point toward the center:

```text
             ● mass
             ↓ T
             ↓ mg
             ↓ +r
             ⊙ center
```

Calculate the shared radial-force scale and the weight:

$$
\frac{mv^2}{r}
=\frac{(0.25)(15^2)}{1.5}
=37.5\,\mathrm N,
\qquad
mg=(0.25)(9.8)=2.45\,\mathrm N.
$$

Now solve the top equation:

$$
\begin{aligned}
T_{\mathrm{top}}+mg&=\frac{mv^2}{r},\\
T_{\mathrm{top}}&=\frac{mv^2}{r}-mg\\
&=37.5-2.45\\
&=35.05\,\mathrm N\approx35\,\mathrm N.
\end{aligned}
$$

Gravity supplies part of the required inward force, so the rope supplies the remainder.

```quiz
type: radio
id: mct-p11-top-mirror
content: |-
  A $0.40\,\mathrm{kg}$ mass moves at $8.0\,\mathrm{m/s}$ at the top of a vertical circle of radius $2.0\,\mathrm m$. What is the rope tension? Use $g=9.8\,\mathrm{m/s^2}$.
options:
- id: mct-p11-top-mirror-a
  content: |-
    $8.88\,\mathrm N$
  correct: true
  feedback: |-
    At the top, tension and weight are both inward, so $T=mv^2/r-mg$. Here $mv^2/r=12.8\,\mathrm N$ and $mg=3.92\,\mathrm N$, giving $T=8.88\,\mathrm N$.
- id: mct-p11-top-mirror-b
  content: |-
    $16.72\,\mathrm N$
  feedback: |-
    Adding weight to $mv^2/r$ gives the bottom tension. At the top, gravity helps provide the inward net force, so it is subtracted when tension is isolated.
- id: mct-p11-top-mirror-c
  content: |-
    $12.8\,\mathrm N$
  feedback: |-
    This sets tension equal to the entire required inward net force and ignores gravity. At the top, gravity already supplies $3.92\,\mathrm N$ inward, leaving $8.88\,\mathrm N$ for the rope.
- id: mct-p11-top-mirror-d
  content: |-
    $3.92\,\mathrm N$
  feedback: |-
    This is the weight, not the tension. The two inward forces must add to $12.8\,\mathrm N$, so tension is the difference $12.8-3.92$.
- id: mct-p11-top-mirror-e
  content: |-
    $0\,\mathrm N$
  feedback: |-
    Zero tension would mean gravity alone supplies the required radial force, which would require $v^2/r=g$. Here $v^2/r=32\,\mathrm{m/s^2}$, so a positive tension is required.
```

---

<a id="source-video-problem-1-bottom"></a>
## Source-Video Problem 1: Bottom

**Example:** For the same source-video mass, rope, and speed, find the tension at the bottom (6:35–8:15).

**Explanation**

At the bottom, inward is upward. Tension points inward, while weight points outward:

```text
             ⊙ center
             ↑ +r
             ↑ T
             ● mass
             ↓ mg
```

The values $mv^2/r=37.5\,\mathrm N$ and $mg=2.45\,\mathrm N$ have not changed. The radial signs have:

$$
\begin{aligned}
T_{\mathrm{bottom}}-mg&=\frac{mv^2}{r},\\
T_{\mathrm{bottom}}&=\frac{mv^2}{r}+mg\\
&=37.5+2.45\\
&=39.95\,\mathrm N.
\end{aligned}
$$

The rope must overcome the outward contribution of weight and still provide the required upward net force.

```quiz
type: radio
id: mct-p11-bottom-mirror
content: |-
  The same $0.40\,\mathrm{kg}$ mass moves at $8.0\,\mathrm{m/s}$ at the bottom of the circle of radius $2.0\,\mathrm m$. What is the rope tension? Use $g=9.8\,\mathrm{m/s^2}$.
options:
- id: mct-p11-bottom-mirror-a
  content: |-
    $16.72\,\mathrm N$
  correct: true
  feedback: |-
    At the bottom, tension is inward and weight is outward, so $T=mv^2/r+mg$. Adding $12.8\,\mathrm N$ and $3.92\,\mathrm N$ gives $16.72\,\mathrm N$.
- id: mct-p11-bottom-mirror-b
  content: |-
    $8.88\,\mathrm N$
  feedback: |-
    Subtracting weight produces the top tension. At the bottom, tension must both oppose the downward weight and leave an upward net force, so $mg$ is added to $mv^2/r$.
- id: mct-p11-bottom-mirror-c
  content: |-
    $12.8\,\mathrm N$
  feedback: |-
    This omits the outward radial contribution of weight. If $T$ were $12.8\,\mathrm N$, subtracting $mg$ would leave less than the required $12.8\,\mathrm N$ inward.
- id: mct-p11-bottom-mirror-d
  content: |-
    $3.92\,\mathrm N$
  feedback: |-
    This is only the weight. Equal tension and weight would give zero radial net force, but the moving mass requires $mv^2/r=12.8\,\mathrm N$ upward.
- id: mct-p11-bottom-mirror-e
  content: |-
    $25.6\,\mathrm N$
  feedback: |-
    This doubles $mv^2/r$ without accounting for the actual weight. The correct addition is $12.8+3.92$, because $mg=3.92\,\mathrm N$ for this mass.
```

---

<a id="source-video-problem-1-side"></a>
## Source-Video Problem 1: Side

**Example:** For the same source-video mass, rope, and speed, find the tension at the side of the fixed vertical circle (8:23–11:28).

**Explanation**

At the exact side, the taut rope is a horizontal radius. Tension is horizontal and inward; weight is vertical and tangential:

```text
⊙ center ← T, +r — ● mass
                    ↓ mg
                    ↓ tangential
```

Because gravity is perpendicular to the radius, its radial projection is zero. Therefore,

$$
\boxed{T_{\mathrm{side}}=\frac{mv^2}{r}=37.5\,\mathrm N}.
$$

This is exact for the stated fixed-circle geometry, not a high-speed approximation.

The source next tilts the rope, assigns $T_x=37.5\,\mathrm N$ and $T_y=mg=2.45\,\mathrm N$, and reports

$$
\sqrt{37.5^2+2.45^2}=37.58\,\mathrm N
$$

as an “exact” side tension. That construction does not describe a mass at the side of a fixed vertical circle. A taut rope is the radius; if the rope tilts, the mass is no longer at the side, the inward direction tilts with the rope, and gravity must be projected onto that new radial direction. The conical-pendulum rule $T_y=mg$ also cannot be imported: a conical pendulum follows a horizontal circle and has no vertical acceleration, while this mass follows a vertical circle.

At the side, gravity instead supplies a tangential force of magnitude $mg$. If the mass moves freely, its speed changes. If an external drive keeps the speed constant, that drive must supply an equal upward tangential force at this instant; it does not change the radial result $T=mv^2/r$.

```quiz
type: radio
id: mct-p11-side-controlled
content: |-
  A $0.30\,\mathrm{kg}$ mass moves at $5.0\,\mathrm{m/s}$ at the right side of a fixed vertical circle of radius $0.75\,\mathrm m$. An external drive keeps the speed constant. Which statement correctly separates the radial and tangential equations? Use $g=9.8\,\mathrm{m/s^2}$.
options:
- id: mct-p11-side-controlled-a
  content: |-
    $T=10.0\,\mathrm N$ inward, and the drive supplies $2.94\,\mathrm N$ upward to cancel gravity tangentially.
  correct: true
  feedback: |-
    At the side, tension alone is radial: $T=mv^2/r=(0.30)(5.0^2)/(0.75)=10.0\,\mathrm N$. Gravity is tangential with magnitude $mg=2.94\,\mathrm N$, so constant speed requires an equal upward drive force.
- id: mct-p11-side-controlled-b
  content: |-
    $T=\sqrt{10.0^2+2.94^2}=10.42\,\mathrm N$, with no external drive needed.
  feedback: |-
    This repeats the tilted-rope construction. At the side of a fixed circle, the rope and its tension are horizontal; gravity is a separate tangential force and cannot be turned into a vertical component of tension.
- id: mct-p11-side-controlled-c
  content: |-
    $T=12.94\,\mathrm N$ because gravity is added to the radial-force requirement.
  feedback: |-
    Gravity is perpendicular to the radius at the side, so its radial component is zero. Adding $mg$ belongs to the bottom equation, not the side equation.
- id: mct-p11-side-controlled-d
  content: |-
    $T=7.06\,\mathrm N$ because gravity helps provide the inward force.
  feedback: |-
    Gravity points vertically at the side and provides no horizontal inward component. Subtracting $mg$ belongs to the top equation, where gravity actually points inward.
- id: mct-p11-side-controlled-e
  content: |-
    $T=10.0\,\mathrm N$, and no tangential force is needed because radial acceleration accounts for all acceleration.
  feedback: |-
    The radial tension value is correct, but constant speed also requires zero tangential acceleration. Gravity supplies $2.94\,\mathrm N$ downward tangentially, so an external agent must cancel it.
```

---

<a id="rank-the-tensions-at-equal-speed"></a>
## Rank the Tensions at Equal Speed

**Example:** Rank the source-video tensions when the mass has the same $15\,\mathrm{m/s}$ speed at the top, side, and bottom.

**Explanation**

Let

$$
C=\frac{mv^2}{r}.
$$

At equal speed, $C$ is the same at all three locations:

$$
T_{\mathrm{top}}=C-mg,
\qquad
T_{\mathrm{side}}=C,
\qquad
T_{\mathrm{bottom}}=C+mg.
$$

Thus,

$$
\boxed{T_{\mathrm{bottom}}>T_{\mathrm{side}}>T_{\mathrm{top}}}
$$

and the source values show the spacing:

$$
39.95\,\mathrm N>37.5\,\mathrm N>35.05\,\mathrm N.
$$

The side tension is halfway between the top and bottom tensions when the speeds are equal. If the motion is not externally driven, energy changes the speed with height, so compare the local values of $mv^2/r$ before ranking.

A rope can pull but cannot push. If the top equation produces $T<0$, the rope goes slack and the assumed circular path is no longer valid. That is a consistency check, not a new tension formula.

```quiz
type: radio
id: mct-p11-rank-controlled
content: |-
  The same mass has equal speed at the top, side, and bottom of a vertical circle. Measurements give $T_{\mathrm{top}}=18\,\mathrm N$ and $T_{\mathrm{bottom}}=28\,\mathrm N$. What is $T_{\mathrm{side}}$?
options:
- id: mct-p11-rank-controlled-a
  content: |-
    $23\,\mathrm N$
  correct: true
  feedback: |-
    At equal speed, $T_{\mathrm{top}}=C-mg$ and $T_{\mathrm{bottom}}=C+mg$. Their average isolates $C$: $(18+28)/2=23\,\mathrm N$, and the side tension equals $C$.
- id: mct-p11-rank-controlled-b
  content: |-
    $18\,\mathrm N$
  feedback: |-
    This would make side and top tension equal even though gravity helps radially only at the top. With equal speed, the side value is $mg$ above the top value.
- id: mct-p11-rank-controlled-c
  content: |-
    $28\,\mathrm N$
  feedback: |-
    This would make side and bottom tension equal even though gravity opposes the inward direction only at the bottom. With equal speed, the side value is $mg$ below the bottom value.
- id: mct-p11-rank-controlled-d
  content: |-
    $10\,\mathrm N$
  feedback: |-
    The difference $28-18=10\,\mathrm N$ equals $2mg$, not the radial-force scale $C$. Half that difference is $mg=5\,\mathrm N$, placing the side tension at $18+5=23\,\mathrm N$.
- id: mct-p11-rank-controlled-e
  content: |-
    $46\,\mathrm N$
  feedback: |-
    Adding the top and bottom tensions gives $2C$ because the $-mg$ and $+mg$ terms cancel. Divide the sum by two to obtain the side tension, $C=23\,\mathrm N$.
```

---

<a id="summary"></a>
## Summary

For a mass on a taut rope moving in a fixed vertical circle:

1. Point $+r$ from the mass toward the center at the location of interest.
2. Project tension and weight onto that inward direction.
3. Set their signed radial sum equal to $mv^2/r$.
4. Isolate tension before substituting the local speed.

At the top, $T=mv^2/r-mg$. At the bottom, $T=mv^2/r+mg$. At the side, gravity is tangential, so $T=mv^2/r$ exactly. For equal speeds, $T_{\mathrm{bottom}}>T_{\mathrm{side}}>T_{\mathrm{top}}$.

Do not add a separate “centripetal force,” set $T=mv^2/r$ at every position, or tilt the rope at the side of a fixed circle to give tension a vertical component. If constant speed is specified away from the top and bottom, account for the external tangential force required to cancel gravity's tangential component.

<!-- lesson-nav:start -->

---

```update-progress
```

[[212/Home|Home]]
[[212/0. Table of Contents/TOC|Table of Contents]]

---

<!-- lesson-nav:end -->
