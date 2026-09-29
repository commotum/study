# Composite Object: Rod and Point Mass

Source: [[212/M2/2026-07-08-M2-2/Source/Lecture-Notes#Composite Object: Rod and Point Mass|Lecture example]]

## 1. The Problem

A uniform thin rod has mass $M$ and length $L$. A point mass $3M$ is attached to the rod’s far end. The rigid composite object rotates about an axis through the opposite end of the rod and perpendicular to it.

**A.** Identify the distance from the rotation axis to the attached point mass.

**B.** Write the moment of inertia of the rod about the axis.

**C.** Write the moment of inertia of the attached point mass about the same axis.

**D.** Add the contributions and simplify the total moment of inertia.

**E.** Check the units and explain why the two moments may be added directly.

## 2. The Equations

- Additivity about a common axis:

  $$
  I_{\mathrm{total}}=\sum_j I_j.
  $$

  Every component must be evaluated about the same rotation axis.

- Uniform rod about one end:

  $$
  I_{\mathrm{rod}}=\frac13ML^2.
  $$

- Point mass:

  $$
  I_{\mathrm{point}}=mr^2.
  $$

  The attached mass is concentrated a distance $r=L$ from the pivot.

## 3. The Walkthrough

1. The attached point mass is at the far end, so its distance from the axis is $L$.

2. The rod contributes

   $$
   I_{\mathrm{rod}}=\frac13ML^2.
   $$

3. The point mass contributes

   $$
   I_{\mathrm{point}}=(3M)L^2=3ML^2.
   $$

4. Add the terms about the shared axis:

   $$
   I_{\mathrm{total}}
   =
   \frac13ML^2+3ML^2.
   $$

5. Express both terms with a common denominator:

   $$
   I_{\mathrm{total}}
   =
   \left(\frac13+\frac93\right)ML^2
   =
   \frac{10}{3}ML^2.
   $$

6. Both component inertias have units $\mathrm{kg}\cdot\mathrm{m}^2$. They are directly additive because the rod and point mass rotate rigidly about the same axis with the same angular speed.
