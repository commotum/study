# Uniform Thin Rod Rotating About Its Center

Source: [[212/M2/2026-07-08-M2-2/Source/Lecture-Notes#Uniform Thin Rod About Its Center|Lecture example]]

## 1. The Problem

A uniform thin rod has mass $M$ and length $L$. It rotates about an axis through its center and perpendicular to the rod.

**A.** Choose the origin at the rotation axis and state the coordinate limits for the rod.

**B.** Write the uniform linear density and differential mass element.

**C.** Construct the moment-of-inertia integral about the central axis.

**D.** Evaluate the integral symbolically.

**E.** Check the units and explain why contributions from $x$ and $-x$ add rather than cancel.

## 2. The Equations

- Uniform linear density:

  $$
  \lambda=\frac{M}{L}.
  $$

  A uniform rod has the same mass per unit length everywhere.

- Differential mass:

  $$
  dm=\lambda\,dx=\frac{M}{L}\,dx.
  $$

- Continuous moment of inertia:

  $$
  I=\int r_\perp^2\,dm.
  $$

  For a rod along the $x$-axis rotating about its center, $r_\perp=|x|$, so $r_\perp^2=x^2$.

- SI dimensions:

  $$
  [I]=\text{kg}\cdot\text{m}^2.
  $$

## 3. The Walkthrough

1. Place the origin at the rod’s midpoint. The rod occupies

   $$
   -\frac{L}{2}\le x\le\frac{L}{2}.
   $$

2. Substitute the uniform mass element into the definition:

   $$
   I_{\mathrm{cm}}
   =
   \int_{-L/2}^{L/2}x^2\,dm
   =
   \frac{M}{L}\int_{-L/2}^{L/2}x^2\,dx.
   $$

3. Integrate:

   $$
   I_{\mathrm{cm}}
   =
   \frac{M}{L}
   \left[\frac{x^3}{3}\right]_{-L/2}^{L/2}.
   $$

4. Evaluate both limits:

   $$
   I_{\mathrm{cm}}
   =
   \frac{M}{L}
   \left(
   \frac{L^3}{24}-\left(-\frac{L^3}{24}\right)
   \right).
   $$

5. Simplify:

   $$
   I_{\mathrm{cm}}=\frac{1}{12}ML^2.
   $$

6. The integrand is $x^2$, so mass at $+x$ and mass at $-x$ make equal positive contributions. The final dimensions are mass times length squared.
