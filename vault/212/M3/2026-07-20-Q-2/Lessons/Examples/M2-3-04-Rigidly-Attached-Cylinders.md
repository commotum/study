# Two Rigidly Attached Solid Cylinders

Source: [[212/M2/2026-07-09-M2-3/Source/Lecture-Notes#Two Rigidly Attached Solid Cylinders|Lecture example]]

## 1. The Problem

Two uniform solid cylinders are rigidly attached and rotate together about their common central axis.

- The large cylinder has mass $M$ and radius $R$.
- The small cylinder has unknown mass $m$ and radius $r$.
- A tangential force $F$ acts at the outer edge of the large cylinder.
- The measured angular acceleration is $\alpha$.

**A.** Calculate the applied torque about the common axis.

**B.** Write the total moment of inertia of the two-cylinder assembly.

**C.** Apply rotational Newton’s second law and solve symbolically for the unknown mass $m$.

**D.** Check the units of every term in the expression for $m$.

**E.** State the condition the measured quantities must satisfy for the inferred mass to be positive.

## 2. The Equations

- Tangential torque:

  $$
  \tau=FR.
  $$

- Solid-cylinder moment of inertia:

  $$
  I_{\mathrm{cyl}}=\frac12MR^2.
  $$

- Additivity for rigid components about a common axis:

  $$
  I_{\mathrm{total}}=I_{\mathrm{small}}+I_{\mathrm{large}}.
  $$

- Rotational Newton’s second law:

  $$
  \sum\tau=I_{\mathrm{total}}\alpha.
  $$

  The attached cylinders share the same angular acceleration.

## 3. The Walkthrough

1. The force is tangential at radius $R$, so

   $$
   \tau=FR.
   $$

2. Add the two central moments of inertia:

   $$
   I_{\mathrm{total}}
   =
   \frac12mr^2+\frac12MR^2.
   $$

3. Apply the rotational equation:

   $$
   FR
   =
   \left(
   \frac12mr^2+\frac12MR^2
   \right)\alpha.
   $$

4. Multiply by $2/\alpha$:

   $$
   \frac{2FR}{\alpha}=mr^2+MR^2.
   $$

5. Isolate the term containing the unknown mass and divide by $r^2$:

   $$
   m
   =
   \frac{2FR}{\alpha r^2}
   -
   \frac{MR^2}{r^2}.
   $$

6. The first term has units

   $$
   \frac{(\mathrm{N})(\mathrm{m})}
        {(\mathrm{s}^{-2})(\mathrm{m}^2)}
   =\mathrm{kg},
   $$

   and the second term also has units of kilograms.

7. A physical positive mass requires

   $$
   \frac{2FR}{\alpha}>MR^2.
   $$

   If this fails, the stated measurements and model are inconsistent with a positive added cylinder mass.
