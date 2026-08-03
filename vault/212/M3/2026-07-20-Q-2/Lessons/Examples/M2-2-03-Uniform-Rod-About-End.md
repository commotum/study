# Uniform Thin Rod Rotating About One End

Source: [[212/M2/2026-07-08-M2-2/Source/Lecture-Notes#Uniform Thin Rod About One End|Lecture example]]

## 1. The Problem

A uniform thin rod has mass $M$ and length $L$. It rotates about an axis through its left end and perpendicular to the rod.

**A.** Place the origin at the rotation axis and state the integration limits.

**B.** Write the differential mass element for the uniform rod.

**C.** Construct and evaluate the moment-of-inertia integral about the end.

**D.** Compare the result with the rod’s central moment of inertia, $I_{\mathrm{cm}}=\frac{1}{12}ML^2$.

**E.** Check the units and explain physically why the end-axis value is larger.

## 2. The Equations

- Uniform mass element:

  $$
  dm=\frac{M}{L}\,dx.
  $$

- Moment of inertia:

  $$
  I=\int r_\perp^2\,dm.
  $$

  With the pivot at the left end, the perpendicular distance is $r_\perp=x$.

- Comparison ratio:

  $$
  \frac{I_{\mathrm{end}}}{I_{\mathrm{cm}}}.
  $$

  This measures the effect of moving the axis while keeping the object unchanged.

## 3. The Walkthrough

1. With the origin at the left end, the rod occupies $0\le x\le L$.

2. Substitute the uniform mass element:

   $$
   I_{\mathrm{end}}
   =
   \int_0^Lx^2\,dm
   =
   \frac{M}{L}\int_0^Lx^2\,dx.
   $$

3. Integrate and evaluate:

   $$
   I_{\mathrm{end}}
   =
   \frac{M}{L}
   \left[\frac{x^3}{3}\right]_0^L
   =
   \frac{M}{L}\frac{L^3}{3}.
   $$

4. Simplify:

   $$
   I_{\mathrm{end}}=\frac{1}{3}ML^2.
   $$

5. Compare with the central-axis result:

   $$
   \frac{I_{\mathrm{end}}}{I_{\mathrm{cm}}}
   =
   \frac{(1/3)ML^2}{(1/12)ML^2}
   =4.
   $$

6. Thus $I_{\mathrm{end}}=4I_{\mathrm{cm}}$. More of the rod’s mass is far from an end axis, and the distance enters as $r^2$. Both expressions have units $\text{kg}\cdot\text{m}^2$.
