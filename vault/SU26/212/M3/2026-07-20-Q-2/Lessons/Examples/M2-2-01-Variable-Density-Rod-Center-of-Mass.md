# Variable-Density Rod: Center of Mass

Source: [[212/M2/2026-07-08-M2-2/Source/Lecture-Notes#Variable-Density Rod: Center of Mass|Lecture example]]

## 1. The Problem

A thin rod occupies $0\le x\le L$, has total mass $M$, and has linear density

$$
\lambda(x)=Cx.
$$

**A.** Construct the mass element $dm$ and use the total mass to solve for $C$.

**B.** Set up the center-of-mass integral about the left end.

**C.** Evaluate the integral and solve symbolically for $x_{\mathrm{cm}}$ in terms of $L$.

**D.** Evaluate $x_{\mathrm{cm}}$ for $L=1.8\ \mathrm{m}$.

**E.** Check the units and explain why the result should lie between $L/2$ and $L$.

## 2. The Equations

- Linear-density mass element:

  $$
  dm=\lambda(x)\,dx.
  $$

  A slice of length $dx$ carries mass equal to the local density times its width.

- Density normalization:

  $$
  M=\int_0^L dm.
  $$

  This determines the unknown constant $C$.

- Continuous center of mass:

  $$
  x_{\mathrm{cm}}=\frac{1}{M}\int_0^L x\,dm.
  $$

  Position is weighted by the mass contained at that position.

- Physical bounds:

  $$
  0\le x_{\mathrm{cm}}\le L.
  $$

  An increasing positive density shifts the center to the right of the midpoint.

## 3. The Walkthrough

1. Write the mass element:

   $$
   dm=Cx\,dx.
   $$

2. Normalize the density:

   $$
   M=\int_0^L Cx\,dx
   =C\left[\frac{x^2}{2}\right]_0^L
   =\frac{CL^2}{2}.
   $$

   Therefore,

   $$
   C=\frac{2M}{L^2}.
   $$

3. Build the center-of-mass integral:

   $$
   x_{\mathrm{cm}}
   =\frac{1}{M}\int_0^L x(Cx)\,dx
   =\frac{C}{M}\int_0^Lx^2\,dx.
   $$

4. Evaluate:

   $$
   x_{\mathrm{cm}}
   =\frac{C}{M}\left[\frac{x^3}{3}\right]_0^L
   =\frac{CL^3}{3M}.
   $$

5. Substitute the normalized value of $C$:

   $$
   x_{\mathrm{cm}}
   =\frac{(2M/L^2)L^3}{3M}
   =\frac{2L}{3}.
   $$

6. For $L=1.8\ \mathrm{m}$:

   $$
   x_{\mathrm{cm}}=\frac{2}{3}(1.8\ \mathrm{m})=1.2\ \mathrm{m}.
   $$

7. The result has units of length and satisfies $L/2<2L/3<L$. That agrees with the increasing density toward the right end.
