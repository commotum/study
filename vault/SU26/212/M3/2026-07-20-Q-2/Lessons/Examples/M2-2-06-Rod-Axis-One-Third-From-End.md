# Uniform Rod Rotating One-Third of the Way from an End

Source: [[212/M2/2026-07-08-M2-2/Source/Lecture-Notes#Uniform Rod Rotating One-Third of the Way from an End|Lecture example]]

## 1. The Problem

A uniform thin rod has mass $M$ and length $L$. Its rotation axis is perpendicular to the rod and located a distance $L/3$ from the left end.

**A.** Place the origin at the rotation axis and state the coordinates of the rod’s two ends.

**B.** Use direct integration to calculate the moment of inertia about this axis.

**C.** Independently verify the result with the parallel-axis theorem.

**D.** Check the units.

**E.** Compare the result qualitatively with $I_{\mathrm{cm}}=\frac{1}{12}ML^2$ and $I_{\mathrm{end}}=\frac13ML^2$.

## 2. The Equations

- Uniform mass element:

  $$
  dm=\frac{M}{L}\,dx.
  $$

- Direct definition:

  $$
  I=\int r_\perp^2\,dm.
  $$

- Parallel-axis theorem:

  $$
  I=I_{\mathrm{cm}}+Md^2.
  $$

  Here $d$ is the distance between the rod’s midpoint and the requested axis.

## 3. The Walkthrough

1. Relative to the axis at $L/3$, the left end is at $-L/3$ and the right end is at $2L/3$.

2. Set up the direct integral:

   $$
   I=\frac{M}{L}\int_{-L/3}^{2L/3}x^2\,dx.
   $$

3. Evaluate:

   $$
   I
   =
   \frac{M}{3L}
   \left[
   \left(\frac{2L}{3}\right)^3
   -
   \left(-\frac{L}{3}\right)^3
   \right].
   $$

4. Compute the bracket:

   $$
   \frac{8L^3}{27}-\left(-\frac{L^3}{27}\right)
   =\frac{9L^3}{27}
   =\frac{L^3}{3}.
   $$

   Therefore,

   $$
   I=\frac{1}{9}ML^2.
   $$

5. For the parallel-axis check, the center is at $L/2$, so

   $$
   d=\frac{L}{2}-\frac{L}{3}=\frac{L}{6}.
   $$

6. Apply the theorem:

   $$
   I
   =
   \frac{1}{12}ML^2+M\left(\frac{L}{6}\right)^2
   =
   \left(\frac{1}{12}+\frac{1}{36}\right)ML^2
   =
   \frac19ML^2.
   $$

7. The result has the correct units and lies between the central- and end-axis values, matching the axis’s intermediate location.
