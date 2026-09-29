# MTH 256 R1 — Math Academy Matches

[Worksheet](<R1 09-29.md>) · Matched 2026-09-29

Search order: Mathematical Foundations I–III first, then Differential Equations (`DEQ`). The Foundations lessons below remain the primary matches when they directly teach the review skill; the DEQ lessons cover the product-derivative method used to solve the linear equation.

| Problem | Coverage |
| --- | --- |
| 1 | Equivalent product-rule and exponential-chain-rule work for (a)–(c); supporting material but no equivalent combined question found for (d) |
| 2 | Equivalent direct-integration IVP lesson for all four parts |
| 3 | Equivalent product-derivative/integrating-factor IVP workflow |

## Problem 1

Match status: No equivalent Math Academy lesson

Scope: the complete problem, because the combined symbolic task in (d) has no verified equivalent question. [Worksheet Problem 1](</home/jake/Developer/study/vault/F26/256/W1 09-27/R1 09-29/R1 09-29.md:13>).

**Verified match for (a):** [The Product Rule for Differentiation — MF2.12.2.5](</home/jake/Developer/study/vault/MA/Mathematical-Foundations/MF2/12. Introduction to Calculus/12.2. Derivatives of Functions and the Rules of Differentiation/Lessons/12.2.5. The Product Rule for Differentiation.md:242>) ([index](</home/jake/Developer/study/vault/MA/Mathematical-Foundations/MF2/topics.csv:311>)). This worked example differentiates the exact function $e^x\sin x$ before evaluating a tangent slope. The derivative computation at line 258 is the worksheet's task.

**Verified match for (b):** the same Foundations lesson gives the product rule for general functions at line 28 and works a trigonometric product at line 70. For practice retaining an unspecified dependent function, [Solving First-Order Linear ODEs Using Integrating Factors — DEQ.1.1.7](</home/jake/Developer/study/vault/MA/Mathematical-Analysis-&-Modeling/DEQ/1. First-Order Differential Equations/1.1. Techniques for Solving First-Order ODEs/Lessons/1.1.7. Solving First-Order Linear ODEs Using Integrating Factors.md:91>) ([index](</home/jake/Developer/study/vault/MA/Mathematical-Analysis-&-Modeling/DEQ/topics.csv:8>)) explicitly expands $\frac{d}{dx}(y x^2)$ in terms of $y$ and $y'$. Replace the known factor by $\sin x$; the product-rule operation is unchanged.

**Verified match for (c):** [The Chain Rule With Exponential Functions — MF2.12.3.2](</home/jake/Developer/study/vault/MA/Mathematical-Foundations/MF2/12. Introduction to Calculus/12.3. Differentiating Composite Functions/Lessons/12.3.2. The Chain Rule With Exponential Functions.md:209>) ([index](</home/jake/Developer/study/vault/MA/Mathematical-Foundations/MF2/topics.csv:317>)). Question 4 asks for the derivative of $e^{x^2}$, exactly the function in the worksheet.

**Supporting material for (d):** [The Chain Rule With Exponential Functions — MF2.12.3.2](</home/jake/Developer/study/vault/MA/Mathematical-Foundations/MF2/12. Introduction to Calculus/12.3. Differentiating Composite Functions/Lessons/12.3.2. The Chain Rule With Exponential Functions.md:146>) ([index](</home/jake/Developer/study/vault/MA/Mathematical-Foundations/MF2/topics.csv:317>)) teaches the exponential chain rule; [The Antiderivative — MF2.12.4.1](</home/jake/Developer/study/vault/MA/Mathematical-Foundations/MF2/12. Introduction to Calculus/12.4. Indefinite Integrals/Lessons/12.4.1. The Antiderivative.md:26>) ([index](</home/jake/Developer/study/vault/MA/Mathematical-Foundations/MF2/topics.csv:321>)) explains the derivative/antiderivative relationship. [Solving First-Order Linear ODEs Using Integrating Factors — DEQ.1.1.7](</home/jake/Developer/study/vault/MA/Mathematical-Analysis-&-Modeling/DEQ/1. First-Order Differential Equations/1.1. Techniques for Solving First-Order ODEs/Lessons/1.1.7. Solving First-Order Linear ODEs Using Integrating Factors.md:581>) ([index](</home/jake/Developer/study/vault/MA/Mathematical-Analysis-&-Modeling/DEQ/topics.csv:8>)) derives the relation between $I(x)=e^{\int P(x)\,dx}$ and $I'(x)=P(x)I(x)$. This is directly useful, but it is a derivation rather than an inspected exercise asking for the derivative of an exponential of an arbitrary antiderivative. The individual Foundations questions cover the constituent operations, not that entire symbolic task.

Fallback: Run `$lesson-pipeline` in targeted mode for **Problem 1** in `/home/jake/Developer/study/vault/F26/256/W1 09-27/R1 09-29/R1 09-29.md`, focusing on **part (d)** and preserving the verified matches above. This is a follow-up directive; no generated lesson has been created.

## Problem 2

Match status: Equivalent Math Academy lesson found

[Worksheet Problem 2](</home/jake/Developer/study/vault/F26/256/W1 09-27/R1 09-29/R1 09-29.md:39>).

**Best match:** [Solving First-Order ODEs Using Direct Integration — MF3.12.1.3](</home/jake/Developer/study/vault/MA/Mathematical-Foundations/MF3/12. Differential Equations/12.1. Introduction to Differential Equations/Lessons/12.1.3. Solving First-Order ODEs Using Direct Integration.md:362>) ([index](</home/jake/Developer/study/vault/MA/Mathematical-Foundations/MF3/topics.csv:244>)). The worked example finds an antiderivative and applies a specified function value to determine the integration constant. Question 7 at line 420 repeats this for an exponential derivative, and Question 8 at line 450 for a rational derivative. The integrands differ, but the task shape—solve $y'=f(x)$ with one initial condition—is the same for (a)–(d).

**Supporting integration skills:** [The Antiderivative — MF2.12.4.1](</home/jake/Developer/study/vault/MA/Mathematical-Foundations/MF2/12. Introduction to Calculus/12.4. Indefinite Integrals/Lessons/12.4.1. The Antiderivative.md:113>) ([index](</home/jake/Developer/study/vault/MA/Mathematical-Foundations/MF2/topics.csv:321>)) covers the power-rule integration used in (a) and, after writing the square root as a power, (b). For (c) and (d), the trigonometric and reciprocal antiderivatives are the extra integration facts; the main IVP workflow remains the Foundations direct-integration lesson. The example at line 77 of that lesson integrates a sine derivative.

**DEQ second-pass result:** [Solving First-Order Linear ODEs Using Integrating Factors — DEQ.1.1.7](</home/jake/Developer/study/vault/MA/Mathematical-Analysis-&-Modeling/DEQ/1. First-Order Differential Equations/1.1. Techniques for Solving First-Order ODEs/Lessons/1.1.7. Solving First-Order Linear ODEs Using Integrating Factors.md:424>) ([index](</home/jake/Developer/study/vault/MA/Mathematical-Analysis-&-Modeling/DEQ/topics.csv:8>)) also solves IVPs, but introduces integrating factors that these four equations do not need. It is a broader, less direct match, so it does not displace the Foundations lesson.

## Problem 3

Match status: Equivalent Math Academy lesson found

[Worksheet Problem 3](</home/jake/Developer/study/vault/F26/256/W1 09-27/R1 09-29/R1 09-29.md:65>).

**Best match:** [Solving First-Order Linear ODEs Using Integrating Factors — DEQ.1.1.7](</home/jake/Developer/study/vault/MA/Mathematical-Analysis-&-Modeling/DEQ/1. First-Order Differential Equations/1.1. Techniques for Solving First-Order ODEs/Lessons/1.1.7. Solving First-Order Linear ODEs Using Integrating Factors.md:131>) ([index](</home/jake/Developer/study/vault/MA/Mathematical-Analysis-&-Modeling/DEQ/topics.csv:8>)). The worked example rewrites a linear ODE as a derivative of a product; the IVP example at line 424 then integrates that product and uses the initial condition to fix the constant. Question 6 at line 505 uses an integrating factor $e^x$, matching the worksheet's product factor. Its forcing term differs, but the solving method is the same.

**Subpart coverage:** (a) is the reverse product-rule step, demonstrated explicitly at line 91; (b) integrates the resulting derivative, with zero right-hand side in this worksheet; (c) applies the initial condition to the product; (d) isolates $y(x)$. This worksheet starts with the equation already multiplied by the integrating factor, so the factor-finding step in the lesson is unnecessary.

**Foundations prerequisite:** [The Product Rule for Differentiation — MF2.12.2.5](</home/jake/Developer/study/vault/MA/Mathematical-Foundations/MF2/12. Introduction to Calculus/12.2. Derivatives of Functions and the Rules of Differentiation/Lessons/12.2.5. The Product Rule for Differentiation.md:28>) ([index](</home/jake/Developer/study/vault/MA/Mathematical-Foundations/MF2/topics.csv:311>)) for the product rule and [Solving First-Order ODEs Using Direct Integration — MF3.12.1.3](</home/jake/Developer/study/vault/MA/Mathematical-Foundations/MF3/12. Differential Equations/12.1. Introduction to Differential Equations/Lessons/12.1.3. Solving First-Order ODEs Using Direct Integration.md:319>) ([index](</home/jake/Developer/study/vault/MA/Mathematical-Foundations/MF3/topics.csv:244>)) for fixing an integration constant. Foundations near miss: [Solving First-Order IVPs Using Separation of Variables — MF3.12.1.5](</home/jake/Developer/study/vault/MA/Mathematical-Foundations/MF3/12. Differential Equations/12.1. Introduction to Differential Equations/Lessons/12.1.5. Solving First-Order IVPs Using Separation of Variables.md:82>) ([index](</home/jake/Developer/study/vault/MA/Mathematical-Foundations/MF3/topics.csv:246>)) solves a homogeneous exponential-growth IVP, but uses separation of variables. It would reach a solution while bypassing the product-rule reasoning explicitly required by this worksheet, so DEQ is the closer main match.
