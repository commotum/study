# Variable-Density Rod: Moment of Inertia

Source: [[212/M2/2026-07-08-M2-2/Source/Lecture-Notes#Variable-Density Rod: Moment of Inertia|Lecture example]]

## 1. The Problem

A thin rod occupies $0\le x\le L$, has total mass $M$, and has linear density

$$
\lambda(x)=Cx.
$$

It rotates about an axis through its left end and perpendicular to the rod.

**A.** Normalize the density and solve for $C$.

**B.** Construct the moment-of-inertia integral about the left end.

**C.** Evaluate the integral and express $I$ only in terms of $M$ and $L$.

**D.** Evaluate the result for $M=0.65\ \mathrm{kg}$ and $L=1.8\ \mathrm{m}$.

**E.** Check the units and compare the result with the uniform-rod end value $\frac13ML^2$.

## 2. The Equations

- Mass element:

  $$
  dm=\lambda(x)\,dx=Cx\,dx.
  $$

- Density normalization:

  $$
  M=\int_0^Ldm.
  $$

- Moment of inertia about the left end:

  $$
  I=\int_0^Lx^2\,dm.
  $$

  The density supplies one factor of $x$, while the squared distance supplies two more.

- Uniform-rod comparison:

  $$
  I_{\mathrm{uniform,end}}=\frac13ML^2.
  $$

## 3. The Walkthrough

1. Normalize the density:

   $$
   M=\int_0^L Cx\,dx=\frac{CL^2}{2},
   \qquad
   C=\frac{2M}{L^2}.
   $$

2. Insert $dm=Cx\,dx$ into the inertia definition:

   $$
   I=\int_0^Lx^2(Cx)\,dx
   =C\int_0^Lx^3\,dx.
   $$

3. Integrate:

   $$
   I=C\left[\frac{x^4}{4}\right]_0^L
   =\frac{CL^4}{4}.
   $$

4. Substitute $C=2M/L^2$:

   $$
   I=\frac{1}{4}\frac{2M}{L^2}L^4
   =\frac12ML^2.
   $$

5. Evaluate numerically:

   $$
   I=\frac12(0.65\ \mathrm{kg})(1.8\ \mathrm{m})^2
   \approx1.05\ \mathrm{kg}\cdot\mathrm{m}^2
   \approx1.1\ \mathrm{kg}\cdot\mathrm{m}^2.
   $$

6. The result exceeds $\frac13ML^2$ because the increasing density places more mass near the far end, where the distance from the axis is largest.
