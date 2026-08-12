# Plank Just Beginning to Tip

Source: [[212/M2/2026-07-13-M2-4/Source/Lecture-Notes#Example 1: Plank Just Beginning to Tip|Lecture example]]

## 1. The Problem

A uniform plank of length $L$ and mass $M$ rests on two supports. Support $A$ is located $L/5$ from the left end, and support $B$ is located $2L/3$ from the left end. A box of mass $m$ is placed a distance $x$ to the right of support $B$. The system is just beginning to tip about support $B$.

**A.** Draw separate free-body diagrams for the box and plank.

**B.** State what happens to the normal force at support $A$ at the tipping threshold.

**C.** Determine the force the box exerts on the plank.

**D.** Find the lever arm of the plank’s weight about support $B$.

**E.** Write the torque-balance equation about $B$ and solve symbolically for $x$.

**F.** Evaluate the result for $M=2.4\ \mathrm{kg}$, $m=1.6\ \mathrm{kg}$, and $L=1.4\ \mathrm{m}$.

**G.** Check the units and confirm that the box remains on the plank.

## 2. The Equations

- Tipping condition:

  $$
  N_A=0.
  $$

  The plank has just lost contact with the support that is not acting as the pivot.

- Static equilibrium:

  $$
  \sum\vec{F}=0,\qquad \sum\tau_B=0.
  $$

- Newton’s third law at the box-plank contact:

  $$
  N_{m\to M}=N_{M\to m}.
  $$

  The box pushes down on the plank with the same magnitude that the plank pushes up on the box.

- Uniform-plank center of mass:

  $$
  x_{\mathrm{cm}}=\frac{L}{2}
  $$

  measured from the left end.

## 3. The Walkthrough

1. At the tipping threshold, support $A$ no longer pushes on the plank:

   $$
   N_A=0.
   $$

   The impending rotation is about support $B$.

2. The box remains vertically at rest, so its free-body diagram gives

   $$
   N_{M\to m}-mg=0,
   \qquad
   N_{M\to m}=mg.
   $$

   By Newton’s third law, the box pushes downward on the plank with magnitude $mg$.

3. The plank’s center is at $L/2$, while support $B$ is at $2L/3$. Its weight therefore has lever arm

   $$
   \frac{2L}{3}-\frac{L}{2}=\frac{L}{6}.
   $$

4. About support $B$, the box’s weight produces torque in the tipping direction and the plank’s weight opposes it:

   $$
   mgx-Mg\frac{L}{6}=0.
   $$

5. Solve for the box position:

   $$
   mgx=Mg\frac{L}{6},
   \qquad
   x=\frac{ML}{6m}.
   $$

6. Substitute the numerical values:

   $$
   x
   =
   \frac{(2.4\ \mathrm{kg})(1.4\ \mathrm{m})}
        {6(1.6\ \mathrm{kg})}
   =0.35\ \mathrm{m}.
   $$

7. The units reduce to meters. The right end lies $L-2L/3=L/3\approx0.467\ \mathrm{m}$ beyond support $B$, and $0.35\ \mathrm{m}<0.467\ \mathrm{m}$, so the box is still on the plank.
