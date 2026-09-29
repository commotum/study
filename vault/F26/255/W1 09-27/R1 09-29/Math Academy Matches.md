# MTH 255 R1 — Math Academy Matches

[Worksheet](<R1 09-29.md>) · Matched 2026-09-29

Search order: Mathematical Foundations I–III first, then Multivariable Calculus (`MVC`). Foundations supplies prerequisite calculus and vector work; MVC supplies the main matches. For gaps, I also searched the available group catalogs and relevant lesson text. The documented global `vault/MA/catalog.csv` is absent, so the group catalogs served as the broad fallback.

A match means the inspected lesson teaches the same core operation; it does not mean every number or subpart is identical. Partial coverage is identified below rather than treating an entire multipart problem as covered.

| Problem | Coverage |
| --- | --- |
| 1 | Equivalent questions for (a)–(c); no equivalent found for the full construction in (d) |
| 2 | Equivalent 3D differentiation and arc-length workflow; differential notation explained below |
| 3 | Equivalent polar-conversion/evaluation work for (a); no equivalent found for the Gaussian-integral deduction in (b) |
| 4 | Equivalent multivariable chain-rule computations for (a) and (b) |
| 5 | Equivalent generalized chain-rule computation, with spherical-coordinate formulas as support |
| 6 | Equivalent cylindrical-bound setup for (a); no equivalent found for the general proof in (b) |

## Problem 1

Match status: No equivalent Math Academy lesson

Scope: the complete problem, because part (d) remains unmatched. [Worksheet Problem 1](</home/jake/Developer/study/vault/F26/255/W1 09-27/R1 09-29/R1 09-29.md:15>).

**Verified matches for (a)–(c):** [Directional Derivatives — MVC.2.4.5](</home/jake/Developer/study/vault/MA/Mathematical-Analysis-&-Modeling/MVC/2. Multivariable Functions/2.4. The Gradient Vector/Lessons/2.4.5. Directional Derivatives.md:188>) ([index](</home/jake/Developer/study/vault/MA/Mathematical-Analysis-&-Modeling/MVC/topics.csv:56>)). Question 2 takes a directional derivative in a supplied, nonunit vector direction; Question 3 at line 278 asks for the direction of fastest increase of a three-variable function; the example at line 398 asks for the maximum rate of change. These are the operations in (a), (c), and (b), respectively. The lesson explicitly extends the gradient-direction result to more than two variables at line 243.

**Supporting lesson:** [The Gradient Vector — MVC.2.4.1](</home/jake/Developer/study/vault/MA/Mathematical-Analysis-&-Modeling/MVC/2. Multivariable Functions/2.4. The Gradient Vector/Lessons/2.4.1. The Gradient Vector.md:161>) ([index](</home/jake/Developer/study/vault/MA/Mathematical-Analysis-&-Modeling/MVC/topics.csv:52>)) computes a three-variable gradient at a point, including an $xyz$ term.

**Gap in (d):** constructing two directions that are both perpendicular to the gradient **and mutually orthogonal** is an additional construction, not merely computing one directional derivative. [The Gradient as a Normal Vector — MVC.2.4.2](</home/jake/Developer/study/vault/MA/Mathematical-Analysis-&-Modeling/MVC/2. Multivariable Functions/2.4. The Gradient Vector/Lessons/2.4.2. The Gradient as a Normal Vector.md:368>) ([index](</home/jake/Developer/study/vault/MA/Mathematical-Analysis-&-Modeling/MVC/topics.csv:53>)) teaches normals to level surfaces, but does not ask for that pair of tangent directions. Broad-fallback near miss: [Orthogonal Complements — LAL.6.2.5](</home/jake/Developer/study/vault/MA/Mathematical-Analysis-&-Modeling/LAL/6. Projections/6.2. Orthogonality/Lessons/6.2.5. Orthogonal Complements.md:449>) ([index](</home/jake/Developer/study/vault/MA/Mathematical-Analysis-&-Modeling/LAL/topics.csv:138>)) asks for a basis of an orthogonal complement, but does not require its basis vectors to be mutually orthogonal or connect them to zero voltage change. This LAL reference is outside the normal 255 route and is not a main match.

Fallback: Run `$lesson-pipeline` in targeted mode for **Problem 1** in `/home/jake/Developer/study/vault/F26/255/W1 09-27/R1 09-29/R1 09-29.md`, focusing on **part (d)** and preserving the verified matches above. This is a follow-up directive; no generated lesson has been created.

## Problem 2

Match status: Equivalent Math Academy lesson found

[Worksheet Problem 2](</home/jake/Developer/study/vault/F26/255/W1 09-27/R1 09-29/R1 09-29.md:35>).

**Best match:** [The Arc Length of a Vector-Valued Function — MVC.1.1.6](</home/jake/Developer/study/vault/MA/Mathematical-Analysis-&-Modeling/MVC/1. Vector Functions and Vector Fields/1.1. Vector-Valued Functions/Lessons/1.1.6. The Arc Length of a Vector-Valued Function.md:323>) ([index](</home/jake/Developer/study/vault/MA/Mathematical-Analysis-&-Modeling/MVC/topics.csv:7>)). The worked 3D example computes the component derivatives, takes the norm of the derivative vector, and integrates it over a parameter interval. Question 5 at line 365 uses a spatial curve with a logarithmic component. This verifies the workflow in (a), (c), and (d), rather than relying only on the title.

**Part (b) and notation:** the worksheet isolates the step $d\mathbf r=\mathbf r'(t)\,dt$ and writes $ds=\|\mathbf r'(t)\|\,dt$. The example performs those derivative/norm operations within its arc-length calculation, but does not ask for these two differential expressions as separate answers. Practice those representations explicitly when using this lesson.

**Supporting lesson:** [Differentiation Rules for Vector-Valued Functions — MVC.1.1.4](</home/jake/Developer/study/vault/MA/Mathematical-Analysis-&-Modeling/MVC/1. Vector Functions and Vector Fields/1.1. Vector-Valued Functions/Lessons/1.1.4. Differentiation Rules for Vector-Valued Functions.md:43>) ([index](</home/jake/Developer/study/vault/MA/Mathematical-Analysis-&-Modeling/MVC/topics.csv:5>)) for componentwise differentiation and its differentiation rules. Foundations near miss: [The Arc Length of a Parametric Curve — MF3.3.1.7](</home/jake/Developer/study/vault/MA/Mathematical-Foundations/MF3/3. Parametric & Polar Coordinates/3.1. Parametric Equations/Lessons/3.1.7. The Arc Length of a Parametric Curve.md:77>) ([index](</home/jake/Developer/study/vault/MA/Mathematical-Foundations/MF3/topics.csv:50>)) gives the analogous planar arc-length setup, but the MVC lesson is the closer three-dimensional match.

## Problem 3

Match status: No equivalent Math Academy lesson

Scope: the complete problem, because the deduction in (b) remains unmatched. [Worksheet Problem 3](</home/jake/Developer/study/vault/F26/255/W1 09-27/R1 09-29/R1 09-29.md:58>).

**Verified match for (a):** [Double Integrals Between Polar Curves — MVC.3.4.2](</home/jake/Developer/study/vault/MA/Mathematical-Analysis-&-Modeling/MVC/3. Multiple Integrals/3.4. Change of Variables for Double Integrals/Lessons/3.4.2. Double Integrals Between Polar Curves.md:360>) ([index](</home/jake/Developer/study/vault/MA/Mathematical-Analysis-&-Modeling/MVC/topics.csv:108>)). Question 4 converts an integral over a region bounded by an origin-centered circle and a vertical line, closely matching this worksheet's boundary geometry. The worked example at line 387 evaluates an integral after deriving angle-dependent polar bounds; Question 6 at line 510 uses a square-root radial integrand. Together these cover the coordinate conversion, Jacobian factor, and evaluation needed in (a); the worksheet's exact integrand is different.

**Supporting lesson for (b):** [Double Integrals in Plane Polar Coordinates — MVC.3.4.1](</home/jake/Developer/study/vault/MA/Mathematical-Analysis-&-Modeling/MVC/3. Multiple Integrals/3.4. Change of Variables for Double Integrals/Lessons/3.4.1. Double Integrals in Plane Polar Coordinates.md:511>) ([index](</home/jake/Developer/study/vault/MA/Mathematical-Analysis-&-Modeling/MVC/topics.csv:107>)) teaches evaluating a double integral by converting to polar coordinates, but its examples use bounded regions. I found no equivalent question combining the improper first-quadrant double integral, its interpretation as a product of one-dimensional integrals, and the deduction of the half-line/full-line Gaussian integrals. A broad text search found the Gaussian value stated in the probability Gamma Function lesson, but it assumes that value instead of deriving it by this method, so it is a near miss.

Fallback: Run `$lesson-pipeline` in targeted mode for **Problem 3** in `/home/jake/Developer/study/vault/F26/255/W1 09-27/R1 09-29/R1 09-29.md`, focusing on **part (b)** and preserving the verified matches above. This is a follow-up directive; no generated lesson has been created.

## Problem 4

Match status: Equivalent Math Academy lesson found

[Worksheet Problem 4](</home/jake/Developer/study/vault/F26/255/W1 09-27/R1 09-29/R1 09-29.md:77>).

**Best match for (a):** [The Multivariable Chain Rule in Vector Form — MVC.2.5.3](</home/jake/Developer/study/vault/MA/Mathematical-Analysis-&-Modeling/MVC/2. Multivariable Functions/2.5. The Multivariable Chain Rule/Lessons/2.5.3. The Multivariable Chain Rule in Vector Form.md:469>) ([index](</home/jake/Developer/study/vault/MA/Mathematical-Analysis-&-Modeling/MVC/topics.csv:60>)). The worked example differentiates a scalar field along the very same helix $\langle\sin t,\cos t,t\rangle$ up to interchange of the first two components; Question 3 at line 261 also differentiates a three-variable scalar field along a trigonometric vector curve. The scalar field differs, but the mathematical operation is the same.

**Best match for (b):** [The Multivariable Chain Rule — MVC.2.5.1](</home/jake/Developer/study/vault/MA/Mathematical-Analysis-&-Modeling/MVC/2. Multivariable Functions/2.5. The Multivariable Chain Rule/Lessons/2.5.1. The Multivariable Chain Rule.md:502>) ([index](</home/jake/Developer/study/vault/MA/Mathematical-Analysis-&-Modeling/MVC/topics.csv:58>)). The example and Questions 7–8 use three intermediate variables that each depend on two independent parameters, and compute a partial derivative by adding the chain-rule contributions. That dependency structure matches the cone parameterization. Use this general rule because here $z=r$; treating $z$ as independent of $r$ would omit a term.

**Supporting lesson:** [The Multivariable Chain Rule With Polar Coordinates — MVC.2.5.2](</home/jake/Developer/study/vault/MA/Mathematical-Analysis-&-Modeling/MVC/2. Multivariable Functions/2.5. The Multivariable Chain Rule/Lessons/2.5.2. The Multivariable Chain Rule With Polar Coordinates.md:78>) ([index](</home/jake/Developer/study/vault/MA/Mathematical-Analysis-&-Modeling/MVC/topics.csv:59>)) gives the trigonometric polar-coordinate derivatives. Its cylindrical example at line 340 has independent $z$, so it alone is not a full match for the cone. The worksheet's request to interpret the result geometrically is an additional reflection prompt.

## Problem 5

Match status: Equivalent Math Academy lesson found

[Worksheet Problem 5](</home/jake/Developer/study/vault/F26/255/W1 09-27/R1 09-29/R1 09-29.md:103>).

**Best match for the computation:** [The Multivariable Chain Rule — MVC.2.5.1](</home/jake/Developer/study/vault/MA/Mathematical-Analysis-&-Modeling/MVC/2. Multivariable Functions/2.5. The Multivariable Chain Rule/Lessons/2.5.1. The Multivariable Chain Rule.md:502>) ([index](</home/jake/Developer/study/vault/MA/Mathematical-Analysis-&-Modeling/MVC/topics.csv:58>)). The worked example and Question 8 at line 595 calculate a partial derivative of a scalar function through three coordinate functions. Repeating that same sum-of-three-contributions operation for each independent parameter is the core task here.

**Spherical-coordinate support:** [The Multivariable Chain Rule With Polar Coordinates — MVC.2.5.2](</home/jake/Developer/study/vault/MA/Mathematical-Analysis-&-Modeling/MVC/2. Multivariable Functions/2.5. The Multivariable Chain Rule/Lessons/2.5.2. The Multivariable Chain Rule With Polar Coordinates.md:444>) ([index](</home/jake/Developer/study/vault/MA/Mathematical-Analysis-&-Modeling/MVC/topics.csv:59>)) explicitly gives the formulas for $f_\rho$, $f_\theta$, and $f_\phi$ with the same spherical-coordinate convention as the worksheet. This section is an explanatory derivation, not a dedicated spherical practice question; the verified practice match is the generalized chain-rule example above. Neither reference supplies this exact temperature example or its reflection prompt.

## Problem 6

Match status: No equivalent Math Academy lesson

Scope: the complete problem, because the proof in (b) remains unmatched. [Worksheet Problem 6](</home/jake/Developer/study/vault/F26/255/W1 09-27/R1 09-29/R1 09-29.md:122>).

**Verified setup match for (a):** [Triple Integrals in Cylindrical Polar Coordinates — MVC.3.5.5](</home/jake/Developer/study/vault/MA/Mathematical-Analysis-&-Modeling/MVC/3. Multiple Integrals/3.5. Change of Variables for Triple Integrals/Lessons/3.5.5. Triple Integrals in Cylindrical Polar Coordinates.md:111>) ([index](</home/jake/Developer/study/vault/MA/Mathematical-Analysis-&-Modeling/MVC/topics.csv:115>)). The example rewrites a three-dimensional region between lower and upper surfaces using cylindrical bounds. The example at line 219 also starts with a set of Cartesian triples. The worksheet generalizes this setup to arbitrary radial functions and a full revolution.

**Supporting material for (b):** the same lesson derives the cylindrical volume element at line 497. Broad-fallback near miss: [The Shell Method: Rotation About the Y-Axis — CA2.2.3.7](</home/jake/Developer/study/vault/MA/Single-Variable-Calculus/CA2/2. Applications of Integration/2.3. Volumes of Revolution/Lessons/2.3.7. The Shell Method- Rotation About the Y-Axis.md:179>) ([index](</home/jake/Developer/study/vault/MA/Single-Variable-Calculus/CA2/topics.csv:60>)) calculates a volume formed by rotating a region between two curves; it also states the shell formula. This CA2 lesson is outside the normal 255 route. Computing a volume with the shell method is not equivalent to proving the general formula from a triple integral, so neither is marked as a main match for (b).

Fallback: Run `$lesson-pipeline` in targeted mode for **Problem 6** in `/home/jake/Developer/study/vault/F26/255/W1 09-27/R1 09-29/R1 09-29.md`, focusing on **part (b), using the region from part (a)** and preserving the verified matches above. This is a follow-up directive; no generated lesson has been created.
