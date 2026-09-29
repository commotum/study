# Solving Static-Friction Thresholds in Circular Motion

<!--
lesson-id: 212-M1-083
topic-code: MTH212.M1.83
-->

## Table of Contents

- [Introduction](#introduction)
- [Identify the Threshold Before Using Mu N](#identify-the-threshold-before-using-mu-n)
- [Find a Level Turn's Maximum Safe Speed](#find-a-level-turns-maximum-safe-speed)
- [Find the Required Coefficient on a Level Turn](#find-the-required-coefficient-on-a-level-turn)
- [Switch a Turntable Threshold to Angular Speed](#switch-a-turntable-threshold-to-angular-speed)
- [Rebuild the Force Equations for a Rotor](#rebuild-the-force-equations-for-a-rotor)
- [Summary](#summary)

## Prerequisites

- Draw a free-body diagram and resolve forces along radial and vertical axes.
- Use $a_r=v^2/r=\omega^2r$ and $v=\omega r$.
- Rearrange equations and take the positive square root of a positive physical quantity.

---

<a id="introduction"></a>
## Introduction

The cue is a circular-motion phrase such as “maximum safe speed,” “minimum rotation rate,” “just starts to slip,” or “prevent sliding when the floor drops.” These phrases place the object at an **impending-slip threshold**.

At any instant before slipping, static friction adjusts to the amount needed:

$$
f_s\leq \mu_sN.
$$

Use $f_s=\mu_sN$ only when the prompt puts the object at the threshold. Below the threshold, the actual friction can be smaller. After sliding begins, the contact uses kinetic rather than static friction.

For every threshold problem, use the same routine:

1. Draw only the real forces and mark the center of the circular path.
2. Decide which way the object would slip relative to the surface; static friction opposes that tendency.
3. Choose inward as radial-positive and write $\sum F_r=mv^2/r$ or $m\omega^2r$.
4. Write the independent nonradial force equation.
5. Apply $f_s=\mu_sN$ at the threshold, circle the requested symbol, and isolate it before substituting numbers.

Do not add an outward “centrifugal force” to an inertial-frame free-body diagram. The inward net force is the force sum required by the inward acceleration, not a separate interaction.

---

<a id="identify-the-threshold-before-using-mu-n"></a>
## Identify the Threshold Before Using Mu N

**Source-video recognition case:** A car follows a level, unbanked circular road. Weight $mg$ points down, the road's normal force $N$ points up, and static friction points horizontally inward. The vertical forces balance, while friction alone supplies the radial net force:

$$
N=mg,
\qquad
f_s=\frac{mv^2}{r}.
$$

The car would otherwise fail to follow the curved road and skid outward relative to it, so static friction must point inward. Notice that this direction is perpendicular to the car's instantaneous velocity; static friction opposes impending relative slip, not necessarily the velocity.

At the maximum safe speed, the required inward friction reaches its available maximum:

$$
\frac{mv_{\max}^2}{r}=f_{s,\max}=\mu_sN.
$$

At a lower speed, the first two equations still hold, but $f_s<\mu_sN$.

```quiz
type: radio
id: mct-p9-threshold-role
content: |-
  A car rounds a level, unbanked curve below its maximum safe speed without skidding. Which force setup is correct?
options:
- id: mct-p9-threshold-role-a
  content: |-
    $N=mg$, $f_s=mv^2/r$, and $f_s<\mu_sN$
  correct: true
  feedback: |-
    Vertical balance gives $N=mg$, while the required inward force is the actual static friction $f_s=mv^2/r$. Because the car is below the slipping threshold, that required friction is less than the available maximum $\mu_sN$.
- id: mct-p9-threshold-role-b
  content: |-
    $N=mg$ and $f_s=\mu_sN$ at every speed
  feedback: |-
    The vertical equation is right, but static friction is not automatically at its maximum. Equality $f_s=\mu_sN$ applies only at impending slip; below the maximum safe speed, friction adjusts to $mv^2/r<\mu_sN$.
- id: mct-p9-threshold-role-c
  content: |-
    $N=mv^2/r$ and $f_s=mg$
  feedback: |-
    These force roles belong to a rider against a vertical rotor wall, not a car on a horizontal road. Here the road's normal force balances weight, and friction supplies the horizontal inward force.
- id: mct-p9-threshold-role-d
  content: |-
    Static friction points outward and balances an inward centripetal force
  feedback: |-
    “Centripetal force” is the inward net force requirement, not an extra force arrow. The only horizontal real force in this level-turn model is static friction, so it points inward and produces the radial acceleration.
- id: mct-p9-threshold-role-e
  content: |-
    Kinetic friction points inward because the tires are moving along the road
  feedback: |-
    Rolling without skidding leaves the tire contact patch instantaneously at rest relative to the road, so the relevant contact force is static friction. Kinetic friction would apply only after relative sliding began.
```

---

<a id="find-a-level-turns-maximum-safe-speed"></a>
## Find a Level Turn's Maximum Safe Speed

**Source-video Problem 1:** A car rounds a level turn of radius $r=90\,\mathrm m$. The coefficient of static friction between the tires and road is $\mu_s=0.75$. Find the maximum safe speed.

**Explanation**

The word “maximum” signals impending outward slip, so friction points inward and is at its limiting value. Use the level-turn equations:

$$
N=mg,
\qquad
f_{s,\max}=\mu_sN,
\qquad
f_s=\frac{mv^2}{r}.
$$

Couple them and cancel the mass:

$$
\begin{aligned}
\frac{mv_{\max}^2}{r}&=\mu_smg,\\
v_{\max}^2&=\mu_srg,\\
v_{\max}&=\sqrt{\mu_srg}.
\end{aligned}
$$

The algebraic equation for $v^2$ has two square roots, but speed is a nonnegative magnitude. The physical threshold therefore uses the positive root:

$$
v_{\max}
=\sqrt{(0.75)(90\,\mathrm m)(9.8\,\mathrm{m/s^2})}
=25.7\,\mathrm{m/s}.
$$

The mass cancellation means that this idealized threshold does not depend on vehicle mass. The formula also shows that more static friction or a larger turn radius permits a higher speed.

```quiz
type: radio
id: mct-p9-level-speed
content: |-
  A car rounds a level, unbanked turn of radius $50\,\mathrm m$. If $\mu_s=0.60$, what is its maximum safe speed? Use $g=9.8\,\mathrm{m/s^2}$.
options:
- id: mct-p9-level-speed-a
  content: |-
    $17.1\,\mathrm{m/s}$
  correct: true
  feedback: |-
    At impending slip, inward static friction reaches $\mu_sN$ and $N=mg$. Thus $v_{\max}=\sqrt{\mu_srg}=\sqrt{(0.60)(50)(9.8)}=17.1\,\mathrm{m/s}$.
- id: mct-p9-level-speed-b
  content: |-
    $294\,\mathrm{m/s}$
  feedback: |-
    The product $\mu_srg=294\,\mathrm{m^2/s^2}$ is $v_{\max}^2$, not the speed. Taking the positive square root supplies the requested units of meters per second.
- id: mct-p9-level-speed-c
  content: |-
    $5.48\,\mathrm{m/s}$
  feedback: |-
    This is $\sqrt{\mu_sr}$ and omits gravity. Friction's limit is $\mu_sN=\mu_smg$, so $g$ must remain in $v_{\max}=\sqrt{\mu_srg}$.
- id: mct-p9-level-speed-d
  content: |-
    $0.343\,\mathrm{m/s}$
  feedback: |-
    This uses $\sqrt{\mu_sg/r}$, the angular-speed form for a coin on a turntable. The prompt requests linear speed, whose level-turn threshold grows with radius: $v_{\max}=\sqrt{\mu_srg}$.
- id: mct-p9-level-speed-e
  content: |-
    $28.6\,\mathrm{m/s}$
  feedback: |-
    This places $\mu_s$ in the denominator. A larger friction coefficient should raise, not lower, the safe speed; the radial and friction equations give $v_{\max}^2=\mu_srg$.
```

---

<a id="find-the-required-coefficient-on-a-level-turn"></a>
## Find the Required Coefficient on a Level Turn

**Source-video Problem 2:** A car rounds a level turn of radius $70\,\mathrm m$ at $24\,\mathrm{m/s}$. Find the minimum coefficient of static friction that permits this motion.

**Explanation**

“Minimum coefficient” again places the contact at its threshold. The force diagram is unchanged from Problem 1, so reuse the same coupled equation and isolate the new target:

$$
\begin{aligned}
\frac{mv^2}{r}&=\mu_smg,\\
\mu_{s,\min}&=\frac{v^2}{rg}.
\end{aligned}
$$

Substitute only after isolating $\mu_s$:

$$
\mu_{s,\min}
=\frac{(24\,\mathrm{m/s})^2}
{(70\,\mathrm m)(9.8\,\mathrm{m/s^2})}
=\frac{576}{686}
=0.84.
$$

The coefficient is dimensionless. At any smaller $\mu_s$, the available static friction would be too small to bend the car's path at $24\,\mathrm{m/s}$.

```quiz
type: radio
id: mct-p9-level-mu
content: |-
  A car is just at the no-skid threshold while traveling at $20\,\mathrm{m/s}$ around a level turn of radius $80\,\mathrm m$. What is $\mu_s$? Use $g=9.8\,\mathrm{m/s^2}$.
options:
- id: mct-p9-level-mu-a
  content: |-
    $0.51$
  correct: true
  feedback: |-
    At the level-turn threshold, $mv^2/r=\mu_smg$, so $\mu_s=v^2/(rg)=20^2/[(80)(9.8)]=0.51$.
- id: mct-p9-level-mu-b
  content: |-
    $0.0255$
  feedback: |-
    This uses $v/(rg)$ and drops the square on speed. Radial acceleration depends on $v^2$, so the required friction coefficient is $v^2/(rg)$.
- id: mct-p9-level-mu-c
  content: |-
    $1.96$
  feedback: |-
    This is the reciprocal $rg/v^2$. The required coefficient must increase when speed increases, so $v^2$ belongs in the numerator: $\mu_s=v^2/(rg)$.
- id: mct-p9-level-mu-d
  content: |-
    $5.0$
  feedback: |-
    The value $v^2/r=5.0\,\mathrm{m/s^2}$ is the radial acceleration, not a friction coefficient. Divide that acceleration by $g$ to compare the required friction with the normal force per unit mass.
- id: mct-p9-level-mu-e
  content: |-
    $40.8$
  feedback: |-
    Dividing $v^2$ by $g$ omits the turn radius and leaves units of length. The dimensionless coefficient requires $\mu_s=v^2/(rg)$.
```

---

<a id="switch-a-turntable-threshold-to-angular-speed"></a>
## Switch a Turntable Threshold to Angular Speed

**M1-3 lecture transfer:** A coin of mass $m$ rests at radius $r$ on a horizontal turntable. The coefficient of static friction is $\mu_s=0.24$. Find the maximum angular speed before the coin slips.

**Explanation**

The coin and the level-turn car have the same force geometry: $N=mg$, and inward static friction supplies the radial force. At the threshold,

$$
f_{s,\max}=\mu_smg.
$$

Use the angular form of radial acceleration rather than changing the force reasoning:

$$
\begin{aligned}
m\omega_{\max}^2r&=\mu_smg,\\
\omega_{\max}^2r&=\mu_sg,\\
\omega_{\max}&=\sqrt{\frac{\mu_sg}{r}}
=\sqrt{\frac{(0.24)g}{r}}.
\end{aligned}
$$

The mass cancels. At fixed $\mu_s$, a coin farther from the axis has a lower allowable angular speed because $a_r=\omega^2r$ grows with radius.

```quiz
type: radio
id: mct-p9-coin-omega
content: |-
  A coin rests $0.40\,\mathrm m$ from the center of a horizontal turntable. If $\mu_s=0.36$, what is the maximum angular speed before it slips? Use $g=9.8\,\mathrm{m/s^2}$.
options:
- id: mct-p9-coin-omega-a
  content: |-
    $2.97\,\mathrm{rad/s}$
  correct: true
  feedback: |-
    Static friction supplies $m\omega^2r$ and reaches $\mu_smg$ at slipping, so $\omega_{\max}=\sqrt{\mu_sg/r}=\sqrt{(0.36)(9.8)/0.40}=2.97\,\mathrm{rad/s}$.
- id: mct-p9-coin-omega-b
  content: |-
    $8.82\,\mathrm{rad/s}$
  feedback: |-
    The value $8.82\,\mathrm{s^{-2}}$ is $\omega_{\max}^2$. Take the positive square root to obtain an angular speed in radians per second.
- id: mct-p9-coin-omega-c
  content: |-
    $1.19\,\mathrm{rad/s}$
  feedback: |-
    This comes from multiplying by $r$ inside the square root. At fixed angular speed, radial acceleration is $\omega^2r$, so solving the threshold equation places $r$ in the denominator.
- id: mct-p9-coin-omega-d
  content: |-
    $8.25\,\mathrm{rad/s}$
  feedback: |-
    This uses $\sqrt{g/(\mu_sr)}$ and inverts the friction coefficient. More available static friction should permit a larger angular speed, so $\mu_s$ belongs in the numerator.
- id: mct-p9-coin-omega-e
  content: |-
    $4.20\,\mathrm{rad/s}$
  feedback: |-
    This result uses $0.20\,\mathrm m$ as though the stated $0.40\,\mathrm m$ were a diameter. The prompt already gives the radius, so substitute $r=0.40\,\mathrm m$ directly.
```

---

<a id="rebuild-the-force-equations-for-a-rotor"></a>
## Rebuild the Force Equations for a Rotor

A rotor ride changes which force occupies each axis:

| Geometry | Inward radial force | Nonradial balance | Impending-slip direction |
| --- | --- | --- | --- |
| Level car or horizontal turntable | $f_s=mv^2/r$ | $N=mg$ | outward relative to the surface |
| Rider against a vertical rotor wall | $N=mv^2/r$ | $f_s=mg$ | downward along the wall |

Importing $N=mg$ into the rotor would assign both force directions incorrectly and make the normal force independent of the spin rate.

**Source-video Problem 3:** A rotor has radius $r=8\,\mathrm m$ and rotates at $25\,\mathrm{rpm}$. Find the minimum coefficient of static friction that prevents a rider from sliding down when the floor drops.

**Explanation**

The impending slip is downward, so static friction points upward. The wall's normal force points inward and supplies the radial acceleration:

$$
N=\frac{mv^2}{r}.
$$

At the minimum-coefficient threshold, upward static friction just balances weight:

$$
f_s=mg,
\qquad
f_s=\mu_sN.
$$

Convert the supplied RPM to linear speed before substituting into $N=mv^2/r$. The two compact routes below review [[MCT-Problem-3#convert-rpm-before-using-si-units|Problem 3]]; the friction setup is unchanged.

**RPM route 1 — frequency and period:**

$$
f=25\,\frac{\mathrm{rev}}{\mathrm{min}}
\left(\frac{1\,\mathrm{min}}{60\,\mathrm s}\right)
=0.4167\,\mathrm{Hz},
\qquad
T=\frac1f=2.4\,\mathrm s.
$$

Then

$$
v=\frac{2\pi r}{T}
=\frac{2\pi(8\,\mathrm m)}{2.4\,\mathrm s}
=20.94\,\mathrm{m/s}.
$$

**RPM route 2 — direct unit-factor check:**

$$
\begin{aligned}
v={}&25\,\frac{\mathrm{rev}}{\mathrm{min}}
\left(\frac{1\,\mathrm{min}}{60\,\mathrm s}\right)
\left(\frac{2\pi\,\mathrm{rad}}{1\,\mathrm{rev}}\right)
\left(8\,\frac{\mathrm m}{\mathrm{rad}}\right)\\
={}&20.94\,\mathrm{m/s}.
\end{aligned}
$$

The two routes agree. In the direct check, $8\,\mathrm{m/rad}$ is only unit bookkeeping from $s=r\theta$. The radius remains the length $8\,\mathrm m$, and the radian is dimensionless.

Now return to the force equations:

$$
\begin{aligned}
\mu_sN&=mg,\\
\mu_s\left(\frac{mv^2}{r}\right)&=mg,\\
\mu_{s,\min}&=\frac{rg}{v^2}\\
&=\frac{(8)(9.8)}{(20.94)^2}\\
&=0.179.
\end{aligned}
$$

Equivalently, $N=m\omega^2r$ gives

$$
\mu_s\omega^2r\geq g.
$$

Equality marks the threshold. A larger coefficient or rotation rate satisfies the no-slip condition; a smaller one does not. Once the rider is stationary relative to the wall, the actual upward friction is $mg$. Above threshold, it remains below its larger available maximum $\mu_sN$.

```quiz
type: radio
id: mct-p9-rotor-mu
content: |-
  A rotor ride has radius $6.0\,\mathrm m$ and angular speed $3.0\,\mathrm{rad/s}$. What minimum coefficient of static friction prevents downward sliding? Use $g=9.8\,\mathrm{m/s^2}$.
options:
- id: mct-p9-rotor-mu-a
  content: |-
    $0.18$
  correct: true
  feedback: |-
    The wall's normal force is $N=m\omega^2r$, and threshold friction balances weight: $\mu_sN=mg$. Therefore $\mu_{s,\min}=g/(\omega^2r)=9.8/[(3.0)^2(6.0)]=0.18$.
- id: mct-p9-rotor-mu-b
  content: |-
    $5.5$
  feedback: |-
    This is the reciprocal $\omega^2r/g$. The rotor needs $\mu_sN\geq mg$, so isolate the coefficient as the weight-to-normal ratio $g/(\omega^2r)$.
- id: mct-p9-rotor-mu-c
  content: |-
    $0.54$
  feedback: |-
    This uses $g/(\omega r)$ and drops the square on angular speed. Radial acceleration is $\omega^2r$, so the normal force and available friction grow with $\omega^2$.
- id: mct-p9-rotor-mu-d
  content: |-
    $1.8$
  feedback: |-
    This is a decimal-place error in $9.8/54$. Since the radial acceleration $\omega^2r=54\,\mathrm{m/s^2}$ is several times $g$, the required coefficient should be well below $1$.
- id: mct-p9-rotor-mu-e
  content: |-
    $0.060$
  feedback: |-
    This divides by an extra factor of angular speed. Only one radial-acceleration factor $\omega^2r$ belongs in $N=m\omega^2r$, giving $\mu_s=g/(\omega^2r)$.
```

---

<a id="summary"></a>
## Summary

For any circular-motion static-friction threshold:

1. Draw the real forces, choose inward as radial-positive, and identify the impending relative slip.
2. Write the radial and nonradial equations before using a friction formula.
3. Keep $f_s\leq\mu_sN$ until the prompt specifies impending slip; only then use equality.
4. For a level car or horizontal turntable, use $N=mg$ and let friction supply the radial force.
5. For a vertical-wall rotor, let $N$ supply the radial force and let upward friction balance weight.

The resulting threshold forms are

$$
v_{\max}=\sqrt{\mu_srg},
\qquad
\omega_{\max}=\sqrt{\frac{\mu_sg}{r}},
\qquad
\mu_{s,\min}^{\mathrm{rotor}}=\frac{g}{\omega^2r}=\frac{rg}{v^2}.
$$

Read each dependency while holding the other displayed quantities fixed. On a level turn, more $\mu_s$ or a larger $r$ raises $v_{\max}$. On a turntable, increasing $r$ lowers $\omega_{\max}$. For a rotor, increasing $\omega$ at fixed $r$, or increasing $r$ at fixed $\omega$, strengthens the wall's normal force and lowers the required $\mu_s$. At fixed linear speed $v$, however, $\mu_{s,\min}=rg/v^2$ increases with $r$. The main trap is carrying $N=mg$ into a geometry where the normal force is radial.

<!-- lesson-nav:start -->

---

```update-progress
```

[[212/Home|Home]]
[[212/0. Table of Contents/TOC|Table of Contents]]

---

<!-- lesson-nav:end -->
