# Rod with Position-Dependent Linear Density

Source: [[212/M2/2026-07-07-M2-1/Source/Lecture-Notes#Variable Linear Mass Density|Lecture example]]

## 1. The Problem

A thin rod occupies $0\le x\le L$, has total mass $M$, and has position-dependent linear mass density

$$
\lambda(x)=Cx,
$$

where $C$ is an unknown constant.

**A.** Write the differential mass element $dm$ for a slice of width $dx$.

**B.** Construct the total-mass integral with the correct limits.

**C.** Evaluate the integral and solve symbolically for $C$ in terms of $M$ and $L$.

**D.** Determine the SI units of $C$.

**E.** Substitute the result back into $\lambda(x)$ and verify that integrating the density returns the total mass $M$.

## 2. The Equations

- Definition of linear mass density:

  $$
  \lambda(x)=\frac{dm}{dx}.
  $$

  This converts a density function into a differential mass element.

- Differential mass:

  $$
  dm=\lambda(x)\,dx.
  $$

- Total mass of a continuous distribution:

  $$
  M=\int dm=\int_0^L\lambda(x)\,dx.
  $$

  The integration limits cover the physical rod.

- Dimensional relation:

  $$
  [\lambda]=\frac{\text{mass}}{\text{length}}.
  $$

  Since $\lambda=Cx$, the constant must supply one additional inverse length.

## 3. The Walkthrough

1. Convert the density to a mass element:

   $$
   dm=Cx\,dx.
   $$

2. Accumulate all slices along the rod:

   $$
   M=\int_0^L Cx\,dx.
   $$

3. Evaluate the integral:

   $$
   M=C\left[\frac{x^2}{2}\right]_0^L
   =\frac{CL^2}{2}.
   $$

4. Isolate the density constant:

   $$
   C=\frac{2M}{L^2}.
   $$

5. Check the dimensions:

   $$
   [C]=\frac{\text{mass}}{\text{length}^2}.
   $$

   Multiplying by $x$ gives mass per length, the correct units for $\lambda$.

6. Substitute the normalized density back into the mass integral:

   $$
   \int_0^L\frac{2M}{L^2}x\,dx
   =
   \frac{2M}{L^2}\frac{L^2}{2}
   =M.
   $$

   The normalization is therefore consistent.
