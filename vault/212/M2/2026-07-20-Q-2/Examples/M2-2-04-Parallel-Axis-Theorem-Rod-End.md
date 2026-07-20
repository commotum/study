# Parallel-Axis Theorem Applied to a Rod

Source: [[212/M2/2026-07-08-M2-2/Source/Lecture-Notes#Parallel-Axis Theorem|Lecture example]]

## 1. The Problem

A uniform thin rod has mass $M$, length $L$, and known central moment of inertia

$$
I_{\mathrm{cm}}=\frac{1}{12}ML^2.
$$

Use the parallel-axis theorem to determine its moment of inertia about an axis through one end and perpendicular to the rod.

**A.** Identify the center-of-mass axis, requested axis, and separation $d$.

**B.** Apply the parallel-axis theorem symbolically.

**C.** Simplify the result and compare it with a direct-integration result.

**D.** Check the units of the shift term $Md^2$.

**E.** State the geometric condition that must hold before the parallel-axis theorem may be used.

## 2. The Equations

- Parallel-axis theorem:

  $$
  I=I_{\mathrm{cm}}+Md^2.
  $$

  It shifts a known center-of-mass inertia to another axis parallel to it.

- Rod’s central moment of inertia:

  $$
  I_{\mathrm{cm}}=\frac{1}{12}ML^2.
  $$

- Center-to-end separation:

  $$
  d=\frac{L}{2}.
  $$

  The center of a uniform rod is halfway between its ends.

## 3. The Walkthrough

1. The requested end axis is parallel to the central axis, and the separation is

   $$
   d=\frac{L}{2}.
   $$

2. Substitute into the theorem:

   $$
   I_{\mathrm{end}}
   =
   \frac{1}{12}ML^2
   +
   M\left(\frac{L}{2}\right)^2.
   $$

3. Simplify the shift term:

   $$
   I_{\mathrm{end}}
   =
   \frac{1}{12}ML^2+\frac{1}{4}ML^2.
   $$

4. Combine fractions:

   $$
   I_{\mathrm{end}}
   =
   \left(\frac{1}{12}+\frac{3}{12}\right)ML^2
   =
   \frac{1}{3}ML^2.
   $$

5. This matches direct integration about the end. The shift term has units $\text{kg}\cdot\text{m}^2$, so it can be added to $I_{\mathrm{cm}}$.

6. The theorem would not apply directly if the requested axis were tilted relative to the center-of-mass axis; the axes must be parallel.
