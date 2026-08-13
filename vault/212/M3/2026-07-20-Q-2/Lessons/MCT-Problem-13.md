# Solve Ladder Equilibrium and the Static-Friction Threshold

<!--
lesson-id: 212-M3-049
topic-code: MTH212.M3.49
-->

## Table of Contents

- [Introduction](#introduction)
- [Draw the Contact Forces](#draw-the-contact-forces)
- [Measure Moment Arms From Lines of Action](#measure-moment-arms-from-lines-of-action)
- [Solve the Empty-Ladder Source Problem](#solve-the-empty-ladder-source-problem)
- [Solve the Person-on-Ladder Threshold Problem](#solve-the-person-on-ladder-threshold-problem)
- [Use the Threshold Condition Carefully](#use-the-threshold-condition-carefully)
- [Connect to the Empty-Ladder Lecture Formula](#connect-to-the-empty-ladder-lecture-formula)
- [Summary](#summary)

## Prerequisites

- Apply $\sum F_x=0$, $\sum F_y=0$, and $\sum\tau=0$ in static equilibrium.
- Use $\tau=Fd_\perp$, where $d_\perp$ is the perpendicular distance from the pivot to a force's line of action.
- Locate the center of mass of a uniform ladder at its midpoint.
- Use the Pythagorean theorem and right-triangle trigonometry.
- Add perpendicular force components to find a resultant.

---

<a id="introduction"></a>
## Introduction

A ladder leaning against a frictionless wall has a useful order of attack:

1. Draw the wall and floor contact forces.
2. Pivot at the foot, removing both floor forces from the torque equation.
3. Solve the torque equation for the wall force.
4. Return to horizontal and vertical force balance.
5. Use $f_s=\mu_sN$ only if the ladder is at impending slip.

The same sequence handles an empty ladder and a ladder supporting a person. The extra load changes the torque ledger, but not the move.

---

<a id="draw-the-contact-forces"></a>
## Draw the Contact Forces

Suppose the wall is to the right of the ladder. The extended free-body diagram is

```text
                         wall
                   ← N_w │
                        ●│
                       / │
                      /  │
             W_L ↓  /   │
                    /    │
             N ↑   /     │
               ●─────────┘ floor
               → f_s
              foot
```

- The frictionless wall supplies only the horizontal normal force $N_w$, directed away from the wall.
- The floor supplies an upward normal force $N$ and a horizontal static-friction force $f_s$.
- The foot would tend to slide away from the wall, so friction points toward the wall.
- The uniform ladder's weight $W_L=M_Lg$ acts downward at its midpoint.
- A person's weight acts downward through the person's location.

Horizontal and vertical equilibrium give

$$
f_s=N_w
$$

and, when a person of mass $m_p$ is present,

$$
N=(M_L+m_p)g.
$$

Do not try to finish with these equations yet; torque balance must supply $N_w$ first.

```quiz
type: radio
id: mct-p13-contact-ledger
shuffle: true
content: |-
  A uniform ladder leans against a frictionless wall on its right. Its foot is on a rough horizontal floor. The wall contact is a vertical height $h$ above the foot, and the horizontal wall-to-foot distance is $b$. Which force-and-moment-arm description is correct when torques are taken about the foot?
options:
- id: mct-p13-contact-ledger-a
  content: |-
    The wall force points left with arm $h$; floor friction points right; the floor normal points up; and the ladder's weight has arm $b/2$.
  correct: true
  feedback: |-
    The wall is frictionless, so it pushes horizontally away from itself. Its horizontal line of action is $h$ above the pivot. The floor forces act at the pivot, and the uniform ladder's vertical weight line is $b/2$ horizontally from the foot.
- id: mct-p13-contact-ledger-b
  content: |-
    The wall force points up with arm $b$; floor friction points left; and the ladder's weight has arm equal to the ladder length.
  feedback: |-
    A frictionless vertical wall cannot exert a vertical contact force. The wall normal is horizontal, and moment arms are perpendicular distances to lines of action rather than distances measured along the ladder.
- id: mct-p13-contact-ledger-c
  content: |-
    The wall force points right with arm $h$; floor friction points left; and the ladder's weight has arm $b/2$.
  feedback: |-
    The wall pushes the ladder away from the wall, which is leftward here. Horizontal balance then requires floor friction to point right, toward the wall.
- id: mct-p13-contact-ledger-d
  content: |-
    The wall force points left with arm equal to the ladder length; floor friction points right; and the ladder's weight has arm $b$.
  feedback: |-
    The force directions are right, but both moment arms are wrong. The wall force's perpendicular arm is the height $h$, and a uniform ladder's weight acts at the midpoint, giving horizontal arm $b/2$.
- id: mct-p13-contact-ledger-e
  content: |-
    The wall force points left with arm $h$; both floor forces also contribute torque; and the ladder's weight has arm $b/2$.
  feedback: |-
    Both floor forces act at the chosen pivot. Their moment arms about the foot are zero, even though the forces themselves are generally nonzero.
```

---

<a id="measure-moment-arms-from-lines-of-action"></a>
## Measure Moment Arms From Lines of Action

Let the top of the ladder be height $h$ above the floor and horizontal distance $b$ from the foot. Choose the foot as the pivot and take counterclockwise torque as positive.

The wall force is horizontal, so its perpendicular moment arm is the vertical height $h$. A downward force has a vertical line of action, so its moment arm is the horizontal distance from the foot to that line.

Finish the right-triangle geometry before writing torque. If the ladder length $L$ and height $h$ are known, then

$$
b=\sqrt{L^2-h^2},
$$

where the positive root is the physical length. If the ladder makes angle $\theta$ above the floor, then $h=L\sin\theta$ and $b=L\cos\theta$. For a uniform ladder, halve the completed base distance to get the weight's arm, $b/2$; do not halve the ladder length and use that as a perpendicular arm.

For an empty uniform ladder,

$$
N_wh-M_Lg\frac b2=0.
$$

If a person has horizontal coordinate $x_p$ measured from the foot, then

$$
N_wh-m_pg x_p-M_Lg\frac b2=0.
$$

Thus,

$$
\boxed{N_w=\frac{m_pg x_p+M_Lg(b/2)}{h}}.
$$

The quantity $x_p$ is the horizontal distance to the person's vertical weight line. It is not automatically the person's distance along the ladder.

---

<a id="solve-the-empty-ladder-source-problem"></a>
## Solve the Empty-Ladder Source Problem

**Source-video worked problem (`qGvFAl5CK_c`, 00:44:07–00:55:20):** A uniform $10\,\mathrm m$ ladder of mass $8\,\mathrm{kg}$ rests against a frictionless wall. Its top is $8\,\mathrm m$ above the floor. Find the floor's horizontal and vertical force components, then the resultant floor force and its direction.

**Frame check (44:55 and 47:00):** The wall is on the right and pushes the ladder left. The floor's horizontal force points right. The $10\,\mathrm m$ ladder and $8\,\mathrm m$ height form a $6$-$8$-$10$ triangle, so the foot is $6\,\mathrm m$ from the wall.

Vertical balance gives

$$
N=M_Lg=(8)(9.8)=78.4\,\mathrm N.
$$

The ladder's weight acts at its midpoint. Its vertical line of action is therefore $3\,\mathrm m$ horizontally from the foot. Pivoting at the foot gives

$$
N_w(8)-(78.4)(3)=0,
$$

so

$$
N_w=29.4\,\mathrm N.
$$

Horizontal balance requires

$$
\boxed{f_s=N_w=29.4\,\mathrm N\ \text{toward the wall}}.
$$

Only after finding the components do we combine them:

$$
F_{\mathrm{floor}}
=\sqrt{N^2+f_s^2}
=\sqrt{(78.4)^2+(29.4)^2}
=\boxed{83.7\,\mathrm N}.
$$

Its direction above the horizontal is

$$
\phi=\tan^{-1}\!\left(\frac{N}{f_s}\right)
=\tan^{-1}\!\left(\frac{78.4}{29.4}\right)
=\boxed{69.4^\circ}.
$$

This problem does not say that the ladder is about to slip, so no equation of the form $f_s=\mu_sN$ is needed.

```quiz
type: radio
id: mct-p13-empty-ladder-mirror
shuffle: true
content: |-
  A uniform $5.0\,\mathrm m$ ladder of mass $12\,\mathrm{kg}$ leans against a frictionless wall. Its top is $4.0\,\mathrm m$ above the floor, so its foot is $3.0\,\mathrm m$ from the wall. Using $g=9.8\,\mathrm{m/s^2}$, what is the magnitude of the floor's resultant force on the ladder?
options:
- id: mct-p13-empty-ladder-mirror-a
  content: |-
    $125.6\,\mathrm N$
  correct: true
  feedback: |-
    The weight is $117.6\,\mathrm N$ and has horizontal arm $1.5\,\mathrm m$. Torque balance gives $N_w(4.0)=(117.6)(1.5)$, so $f_s=N_w=44.1\,\mathrm N$. The floor resultant is $\sqrt{117.6^2+44.1^2}=125.6\,\mathrm N$.
- id: mct-p13-empty-ladder-mirror-b
  content: |-
    $117.6\,\mathrm N$
  feedback: |-
    This is only the floor's vertical component. The floor also supplies $44.1\,\mathrm N$ of horizontal friction, so the resultant is larger than $117.6\,\mathrm N$.
- id: mct-p13-empty-ladder-mirror-c
  content: |-
    $44.1\,\mathrm N$
  feedback: |-
    This is only the horizontal friction component found from torque and horizontal force balance. Combine it perpendicular to the $117.6\,\mathrm N$ normal force.
- id: mct-p13-empty-ladder-mirror-d
  content: |-
    $161.7\,\mathrm N$
  feedback: |-
    This adds perpendicular components directly. The magnitude of the vector sum is $\sqrt{117.6^2+44.1^2}$, not $117.6+44.1$.
- id: mct-p13-empty-ladder-mirror-e
  content: |-
    $147.0\,\mathrm N$
  feedback: |-
    Using the full $3.0\,\mathrm m$ base as the weight's arm gives $f_s=88.2\,\mathrm N$ and this $147.0\,\mathrm N$ resultant. A uniform ladder's weight acts at its midpoint, so the correct horizontal arm is $1.5\,\mathrm m$.
```

---

<a id="solve-the-person-on-ladder-threshold-problem"></a>
## Solve the Person-on-Ladder Threshold Problem

**Source-video worked problem (`qGvFAl5CK_c`, 00:55:20–01:04:51):** A uniform $15\,\mathrm m$, $10\,\mathrm{kg}$ ladder reaches $9\,\mathrm m$ up a frictionless wall, placing its foot $12\,\mathrm m$ from the wall. A $70\,\mathrm{kg}$ person stands so that the person's vertical weight line is $8\,\mathrm m$ horizontally from the foot. Find the minimum coefficient of static friction when the ladder just begins to slide.

**Frame check (57:15 and 59:30):** The $8\,\mathrm m$ label is drawn along the floor from the foot to the person's vertical weight line. It is a horizontal torque arm, not a distance along the ladder. The wall normal points left, while the floor friction points right.

Vertical balance gives

$$
N=(10+70)(9.8)=784\,\mathrm N.
$$

The ladder's midpoint is $6\,\mathrm m$ horizontally from the foot because the full base is $12\,\mathrm m$. Pivoting at the foot,

$$
N_w(9)-(686)(8)-(98)(6)=0.
$$

The clockwise torques add to

$$
(686)(8)+(98)(6)=5488+588=6076\,\mathrm{N\,m}.
$$

**Source correction:** The narration says “676” while adding these terms. The written terms and the video's final wall-force value require $6076\,\mathrm{N\,m}$.

Therefore,

$$
N_w=\frac{6076}{9}=675.1\,\mathrm N.
$$

Horizontal balance gives $f_s=N_w=675.1\,\mathrm N$. Because the ladder is just beginning to slide, static friction has reached its limiting value:

$$
f_s=\mu_sN.
$$

Hence,

$$
\boxed{\mu_{s,\min}=\frac{675.1}{784}=0.861}.
$$

```quiz
type: radio
id: mct-p13-person-threshold-mirror
shuffle: true
content: |-
  A uniform $10\,\mathrm m$, $10\,\mathrm{kg}$ ladder reaches $8.0\,\mathrm m$ up a frictionless wall and has a $6.0\,\mathrm m$ base. A $50\,\mathrm{kg}$ person stands where the person's vertical weight line is $4.5\,\mathrm m$ horizontally from the foot. Using $g=9.8\,\mathrm{m/s^2}$, what minimum coefficient of static friction prevents impending slip?
options:
- id: mct-p13-person-threshold-mirror-a
  content: |-
    $0.531$
  correct: true
  feedback: |-
    About the foot, $N_w(8)=(490)(4.5)+(98)(3)$, so $N_w=f_s=312.375\,\mathrm N$. Vertical balance gives $N=(50+10)(9.8)=588\,\mathrm N$. At impending slip, $\mu_{s,\min}=312.375/588=0.53125$.
- id: mct-p13-person-threshold-mirror-b
  content: |-
    $0.469$
  feedback: |-
    This includes the person's torque but omits the ladder's own weight. The $98\,\mathrm N$ ladder weight acts with a $3.0\,\mathrm m$ horizontal arm and must be included.
- id: mct-p13-person-threshold-mirror-c
  content: |-
    $0.344$
  feedback: |-
    This treats the given $4.5\,\mathrm m$ as distance along the ladder and projects it to $4.5(6/10)=2.7\,\mathrm m$. The $4.5\,\mathrm m$ is already the perpendicular horizontal distance to the person's vertical weight line, so it should enter the torque equation directly.
- id: mct-p13-person-threshold-mirror-d
  content: |-
    $0.266$
  feedback: |-
    This effectively doubles the wall force's $8.0\,\mathrm m$ moment arm. The wall normal is horizontal, so its perpendicular distance from the foot is exactly the $8.0\,\mathrm m$ height.
- id: mct-p13-person-threshold-mirror-e
  content: |-
    $3.19$
  feedback: |-
    This divides the required friction by the ladder's weight alone. The floor normal supports both the ladder and the person, so $N=(10+50)g=588\,\mathrm N$.
```

---

<a id="use-the-threshold-condition-carefully"></a>
## Use the Threshold Condition Carefully

Static friction adjusts to the value required for equilibrium, up to a maximum:

$$
|f_s|\leq \mu_sN.
$$

Use the equality

$$
|f_s|=\mu_sN
$$

only when the problem says “just begins to slide,” “impending slip,” or “minimum coefficient that prevents slipping.” Without such a cue, solve the required friction from equilibrium and leave it as a value below or at the unknown maximum.

```quiz
type: radio
id: mct-p13-threshold-language
shuffle: true
content: |-
  A ladder is motionless against a frictionless wall. The problem gives a coefficient of static friction $\mu_s$ but does not say the ladder is about to slip. Which statement is always valid?
options:
- id: mct-p13-threshold-language-a
  content: |-
    The required friction comes from equilibrium and must satisfy $|f_s|\leq\mu_sN$.
  correct: true
  feedback: |-
    Static friction takes whatever value equilibrium requires, provided that value does not exceed $\mu_sN$. Equality is guaranteed only at the slipping threshold.
- id: mct-p13-threshold-language-b
  content: |-
    The friction force must equal $\mu_sN$ because the ladder is at rest.
  feedback: |-
    Being at rest establishes static friction, not maximum static friction. The value equals $\mu_sN$ only when the contact is at impending slip.
- id: mct-p13-threshold-language-c
  content: |-
    The friction force is zero because the ladder is at rest.
  feedback: |-
    Zero acceleration does not imply zero force. Here floor friction generally balances the horizontal normal force from the wall.
- id: mct-p13-threshold-language-d
  content: |-
    The friction force can exceed $\mu_sN$ as long as the net torque is zero.
  feedback: |-
    Both force and torque equilibrium are required, and static friction cannot exceed its limiting magnitude $\mu_sN$.
- id: mct-p13-threshold-language-e
  content: |-
    The wall supplies vertical friction so the floor-friction condition is unnecessary.
  feedback: |-
    The wall is frictionless and therefore supplies no vertical force. The floor must provide the vertical normal and the horizontal friction required by equilibrium.
```

---

<a id="connect-to-the-empty-ladder-lecture-formula"></a>
## Connect to the Empty-Ladder Lecture Formula

**M2-4 lecture transfer:** For an empty uniform ladder of length $L$ at angle $\theta$ above the floor, the height is $h=L\sin\theta$ and the ladder weight's horizontal arm is $(L/2)\cos\theta$. At impending slip,

$$
N_wL\sin\theta=mg\frac L2\cos\theta,
$$

while $f_s=N_w$, $N=mg$, and $f_s=\mu_sN$. Canceling $mgL$ gives

$$
\boxed{\mu_{s,\min}=\frac12\cot\theta}.
$$

The paired M2-4 lecture problem uses $\theta=52^\circ$:

$$
\mu_{s,\min}=\frac12\cot52^\circ=0.39064\ldots\approx0.39.
$$

This compact formula is only the empty, uniform-ladder special case. It does not replace the torque ledger when a person or another load is present. It also makes a physical trend visible: for otherwise comparable empty ladders, increasing $\theta$ decreases $\cot\theta$, so a steeper ladder requires less friction.

```quiz
type: radio
id: mct-p13-empty-ladder-transfer
shuffle: true
content: |-
  An empty uniform ladder is at impending slip against a frictionless wall. It makes a $60^\circ$ angle above the floor. What is the minimum coefficient of static friction, and what happens if the ladder is made steeper while the other assumptions stay the same?
options:
- id: mct-p13-empty-ladder-transfer-a
  content: |-
    $\mu_{s,\min}=0.289$, and the required coefficient decreases as the ladder becomes steeper.
  correct: true
  feedback: |-
    For an empty uniform ladder, $\mu_{s,\min}=\tfrac12\cot\theta$. Thus $\tfrac12\cot60^\circ=0.2887\approx0.289$. Cotangent decreases over acute angles, so a steeper ladder needs less friction.
- id: mct-p13-empty-ladder-transfer-b
  content: |-
    $\mu_{s,\min}=0.577$, and the required coefficient decreases as the ladder becomes steeper.
  feedback: |-
    $\cot60^\circ=0.577$, but the uniform ladder's weight acts at its midpoint, introducing the factor $1/2$.
- id: mct-p13-empty-ladder-transfer-c
  content: |-
    $\mu_{s,\min}=0.866$, and the required coefficient increases as the ladder becomes steeper.
  feedback: |-
    This uses $\tfrac12\tan60^\circ$ instead of $\tfrac12\cot60^\circ$. The wall-force arm grows relative to the weight arm as the ladder becomes steeper, so less friction is required.
- id: mct-p13-empty-ladder-transfer-d
  content: |-
    $\mu_{s,\min}=0.500$, and the required coefficient does not depend on angle.
  feedback: |-
    The factor $1/2$ comes from the midpoint, but the geometry does not cancel completely. The remaining ratio is $\cot\theta$.
- id: mct-p13-empty-ladder-transfer-e
  content: |-
    $\mu_{s,\min}=0.289$, and the required coefficient increases as the ladder becomes steeper.
  feedback: |-
    The numerical value at $60^\circ$ is right, but the trend is reversed. Since $\cot\theta$ decreases for acute $\theta$, the minimum coefficient also decreases as the ladder becomes steeper.
```

---

<a id="summary"></a>
## Summary

- A frictionless wall exerts only a horizontal normal force. The rough floor supplies a vertical normal and horizontal static friction.
- Pivot at the foot to remove both floor forces from the torque equation.
- Use perpendicular distances to force lines: height for the horizontal wall force, horizontal distance for each vertical weight.
- After torque gives $N_w$, force balance gives $f_s=N_w$ and the floor normal from the total supported weight.
- Combine floor-force components only after solving them.
- Use $f_s=\mu_sN$ only at impending slip; otherwise, $|f_s|\leq\mu_sN$.
- For an empty uniform ladder at threshold, $\mu_{s,\min}=\tfrac12\cot\theta$. Added loads require a new torque ledger.

<!-- lesson-nav:start -->

---

```update-progress
```

[[212/Home|Home]]
[[212/0. Table of Contents/TOC|Table of Contents]]

---

<!-- lesson-nav:end -->
