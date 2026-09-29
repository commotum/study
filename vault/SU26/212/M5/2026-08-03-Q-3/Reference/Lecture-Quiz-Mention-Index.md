# Quiz 3 Lecture-Mention Index

## Purpose and evidence standard

This index records every substantive statement in the M4 and M5 lecture notes and transcripts that does at least one of the following:

- explicitly defines Quiz 3's scope or format;
- explicitly includes or excludes material;
- recommends content for the Quiz 3 note sheet;
- states a condition for receiving quiz credit;
- gives a work-quality instruction that could affect how a written solution is evaluated; or
- strongly signals a likely question type with language such as “most important,” “need to be able to,” or “make sure.”

The raw transcripts are the primary evidence because they are closest to the professor's actual wording. Cleaned `Lecture-Notes.md` and `Lecture-Transcript.md` files were used as cross-checks, not as independent statements. The cleaned notes and transcript for 2026-07-28 are empty, and the cleaned transcript filed under 2026-07-29 contains Doppler material from 2026-07-28; the raw transcripts therefore control the chronology.

### Confidence labels

- **Direct** — the professor explicitly connects the statement to Quiz 3, the quiz note sheet, or quiz credit.
- **Strong contextual** — the professor does not say “this will be a quiz question,” but emphasizes a skill after declaring that Quiz 3 material has begun.
- **Supporting** — useful preparation guidance, but not a promise about a question or a grading rule.
- **Excluded** — explicitly or strongly removed from the assessed scope.
- **Logistics only** — format, timing, or submission information without a content prediction.

## Bottom line

The strongest defensible conclusions are:

1. **Quiz 3 covers oscillations and waves.** On the final lecture day, this is restated as all wave material covered since Quiz 2, including the July 30 lecture.
2. **Explicit exclusions:** damping and driven oscillations; beats. Detailed reflection/transmission at a change of medium is also dropped from the summer course and is therefore a strong implied exclusion.
3. **Explicit note-sheet recommendations:** the four Doppler-effect cases, the speed of sound in air, and the speed of light.
4. **Strongly signaled question families:** SHM graph interpretation; mass–spring energy; simple and physical pendula; traveling-wave functions and direction; wave speed on strings; intensity/decibels; Doppler shift; standing-wave harmonics in strings and pipes; and two-source phase/path-difference interference.
5. **No new points rubric appears in M4 or M5.** The professor does not assign a stated number of points to a derivation, diagram, symbolic step, unit check, or final answer. She does give several work-method directives, indexed below.
6. **The only explicit credit condition in these lectures is procedural:** a quiz note sheet with photo ID must be submitted. The direct “no credit until submitted” statement refers to Quiz 2, while the same submission procedure is repeated for Quiz 3.

## Direct chronological index

### 2026-07-21 — M4-1: Simple harmonic motion

Source: [Raw transcript](../../../M4/2026-07-21-M4-1/Source/Raw-Transcript.md)

1. **Quiz 3 scope begins here — Direct.** Lines 21–25: the professor says that Quiz 3 material starts that day and identifies the material as **oscillations and waves**. Students should begin their Quiz 3 note sheets. Lines 41–45 repeat that students should be thinking about Quiz 3 material and preparing the note sheet.

2. **Note-sheet submission is a credit condition — Direct, but stated about Quiz 2.** Lines 27–37: students do not receive Quiz 2 credit until the note sheet is uploaded; the photo ID must be placed on top of the note sheet in the submitted image. This establishes the course's procedural credit rule, but it is not a rule about the quality of the written solution.

3. **SHM graph interpretation — Strong contextual.** Lines 393–401: students should be able to interpret oscillator plots and identify quantities from them. The following activity asks for amplitude, period, frequency, angular frequency, maximum speed, and the relationships among position, velocity, and acceleration.

4. **Keep units through numerical work — Supporting work instruction.** Lines 625–639: the professor corrects herself and says she should keep units rather than drop them while substituting values. She does not explicitly connect this to quiz points.

5. **Write equations using known quantities — Supporting work instruction.** Lines 735–755: in the mass–spring position problem, the professor first rewrites the position function in terms of the quantities given in the prompt before substituting numbers. This is consistent with the course's symbolic-first convention, but no Quiz 3 point claim is made here.

6. **Use physical interpretation, not only calculation — Strong contextual.** Lines 795–809 and the discussion that follows: use the signs of position and velocity to determine which side of equilibrium the mass is on, its direction of motion, and whether it is speeding up or slowing down.

7. **Mass–spring energy method — Strong contextual.** Lines 905–921: for maximum speed, the professor specifically recommends an energy approach,

   $$
   \frac12 mv_{\max}^2=\frac12 kA^2.
   $$

### 2026-07-22 — M4-2: Simple and physical pendula

Source: [Raw transcript](../../../M4/2026-07-22-M4-2/Source/Raw-Transcript.md)

8. **Same format as the first two quizzes — Direct format statement.** Lines 13–25: Quiz 3 will use the same format as the first two quizzes; students should prepare the note sheet; the content will be **oscillations and waves**. The lecture does not restate the earlier format or its point allocation.

9. **Pendula are inside the stated scope — Strong direct-context signal.** Lines 27–33: immediately after restating the Quiz 3 scope, the professor identifies that day's topics as **simple pendula and physical pendula**.

10. **Damping and driving are not assessed — Explicitly excluded.** Lines 35–45: the professor will not spend class time on damping or driving and “won't put those on the quiz or the final exam.” Damping remains homework-only.

11. **Expected pendulum model — Strong contextual.** Lines 49–277 derive the physical-pendulum result from a force/torque model and the small-angle approximation:

    $$
    T=2\pi\sqrt{\frac{I}{Mg\ell}}.
    $$

    Lines 279–287 say that retaining the exact $\sin\theta$ dependence is not being done. This strongly indicates the small-angle model, but it is not phrased as an absolute quiz exclusion.

12. **Understand notation and equation meaning — Supporting work instruction.** Lines 333–377: distinguish $T$ for tension, $T$ for period, and $\tau$ for torque from context. The professor calls it “very important” to think about what equations mean while writing them.

13. **Use the precision supported by the givens — Supporting work instruction.** Lines 481–489: keep two significant figures because the prompt's givens have two significant figures. No explicit quiz-points statement accompanies this instruction.

14. **Physical-pendulum progression — Strong contextual.** The lecture repeatedly applies the general period formula to increasingly composite objects:

    - simple pendulum, beginning around line 405;
    - uniform rod pivoted at its end, around line 503;
    - offset-pivot rod using the parallel-axis theorem, around line 577;
    - rod plus point mass, around line 699; and
    - rod plus disk, around line 855.

    The repeated structure strongly signals the skill: find total $I$ about the pivot, locate the system center of mass, determine $\ell$, and simplify the period symbolically.

### 2026-07-23 — M5-1: From oscillations to waves

Source: [Raw transcript](../../2026-07-23-M5-1/Source/Raw-Transcript.md)

15. **Quiz 3 retains the prior format — Direct format statement.** Lines 17–25: Quiz 3 is approaching and will use the same format as the previous quizzes. This is logistical and does not restate the grading rubric.

16. **Relating oscillations to waves is emphasized — Strong contextual.** Lines 27–45: as the wave unit begins, the professor calls relating oscillations to waves “probably the most important thing” and stresses both their similarity and their difference.

17. **Core wave-on-a-string relationship — Strong contextual.** Lines 611–649: tension is the restoring force, linear density is $\mu=m/L$, and the wave speed is

    $$
    v=\sqrt{\frac{T}{\mu}}.
    $$

    The professor does not derive it in class, so the evidence supports knowing and applying the relationship more strongly than reproducing its derivation.

18. **Wave motion versus particle motion — Strong contextual.** Lines 800–849: determine the future motion of a marked string particle from the direction in which the wave profile travels. The professor emphasizes that a similar pre-lecture question is not identical, reinforcing the underlying reasoning rather than memorization of an answer.

### 2026-07-27 — M5-2: Wave functions, refraction, and intensity

Source: [Raw transcript](../../2026-07-27-M5-2/Source/Raw-Transcript.md)

19. **No explicit Quiz 3 statement occurs in this lecture.** Its content is nevertheless included by the later direct statement that Quiz 3 covers all wave material since Quiz 2.

20. **Draw geometry before forming equations — Strong contextual.** Lines 827–847: for the wavelengths-in-glass problem, the professor says that first drawing a diagram relating the variables is “very important” because the needed relationships come from it.

21. **Connect oscillator frequency to wave frequency — Strong contextual.** Lines 415–439: while finding the maximum speed of a string element, the professor calls it “the key point” that the oscillator and the wave have the same frequency even though particle speed and wave-propagation speed are different quantities.

22. **Use the diagram as a magnitude check — Supporting work instruction.** Lines 595–617: after solving a wavefront-geometry problem, the professor says to draw the diagram, estimate how large the result should be, and reject answers that are visibly inconsistent with the geometry.

23. **Included topic families by later scope statement — Strong contextual.** This lecture covers traveling-wave functions and propagation direction, wave speed versus particle speed, waves on strings, wavefront geometry, index of refraction and wavelength in a material, wave energy/power, intensity, and sound-intensity level.

### 2026-07-28 — M5-3: Intensity, decibels, and Doppler shift

Source: [Raw transcript](../../2026-07-28-M5-3/Source/Raw-Transcript.md)

24. **Quiz 3 note sheet must be ready before starting — Direct procedural instruction.** Lines 35–59: Quiz 3 opens Saturday and closes Monday; students should prepare their Quiz 3 notes and have them ready to submit to Gradescope with photo ID on top before beginning the quiz.

25. **Solve symbolically before entering values — Strong work instruction.** Lines 401–419: while solving the decibel problem, the professor asks students to carry a symbolic solution “all the way to the end” before putting in values. She does not explicitly state a point value for doing so in this lecture.

26. **Put all four Doppler cases on the quiz note sheet — Direct content recommendation.** Lines 559–655 develop the four cases:

    - observer moving toward the source;
    - observer moving away from the source;
    - source moving toward the observer; and
    - source moving away from the observer.

    At lines 647–655, the professor says students can rely on these four equations and “heartily” recommends writing them on the note sheet for the quiz opening that weekend. This is one of the strongest specific Quiz 3 indicators in M4–M5.

27. **Choose the Doppler case before calculating — Strong prospective question cue.** Beginning around line 657, the professor says the first task is to determine which equation applies and then how to apply it. The repeated distinction is source versus observer and toward versus away.

28. **Know the speed of sound — Direct note-sheet recommendation.** Lines 823–839: the professor identifies $343\ \mathrm{m/s}$ as the speed of sound in air, says it would be useful on the equation sheet, and says students “need to know” it.

### 2026-07-29 — M5-4: Superposition, standing waves, and harmonics

Source: [Raw transcript](../../2026-07-29-M5-4/Source/Raw-Transcript.md)

29. **Continue preparing the Quiz 3 note sheet — Direct preparation statement.** Lines 21–31: the professor repeats the Quiz 3 schedule and tells students to work on the note sheet.

30. **Constructive/destructive interference is foregrounded — Strong contextual.** Lines 93–119 describe complete constructive and destructive interference and identify it as one of the next lecture's “main topics.” The next day's direct scope statement confirms that the July 30 lecture is included.

31. **Detailed discontinuity behavior is dropped — Strong implied exclusion.** Lines 145–183: hard and soft reflections are introduced, but the professor says the detailed reflected/transmitted-wave behavior at a change from a heavier to a lighter medium is being dropped from the summer course. This is not phrased as explicitly as the damping or beats exclusions, so it should be treated as an implied, not guaranteed, exclusion. Basic reflection and standing-wave formation remain in scope.

32. **A fundamental/harmonic question is prospectively suggested — Strong prospective cue.** Lines 345–389: while drawing the fundamental mode, the professor says “one question I might have is” and then develops the connection among the string length, fundamental wavelength, wave speed, and fundamental frequency.

33. **Remember the string-wave-speed relationship — Strong contextual.** Lines 623–649: in the fundamental-frequency problem, students need to remember $v=\sqrt{T/\mu}$ and $\mu=m/L$.

34. **Standing-wave diagrams are part of the solution method — Strong contextual.** Lines 773–827: for the third harmonic of a string, the professor begins with diagrams of the fundamental, second, and third harmonics, extracts the wavelength, then combines this with a free-body diagram and $T=Mg$.

35. **Do not study the sound-speed derivation — Strong implied exclusion.** Lines 923–947: the pressure/density expression for sound speed is labeled “just an aside,” and students are twice told not to worry about it. Use $343\ \mathrm{m/s}$ for ordinary air instead.

36. **Be able to draw open–closed pipe harmonics — Strong directive.** Lines 1039–1045: for the third-harmonic frequency of an open–closed pipe, the professor says to “make sure that you're able to draw a diagram for that.”

### 2026-07-30 — M5-5: Phase difference and two-source interference

Source: [Raw transcript](../../2026-07-30-M5-5/Source/Raw-Transcript.md)

37. **Final scope statement — Direct.** Lines 21–27: Quiz 3 is “over waves,” specifically **all material covered since Quiz 2, including that day's lecture**. Read together with the earlier explicit “oscillations and waves” statements, this includes the M4 oscillation/pendulum material and all M5 wave lectures through July 30.

38. **Beats are not on the quiz — Explicitly excluded.** Lines 41–55: the raw transcript mistranscribes the word as “beading,” but the surrounding discussion clearly concerns **beating/beats**. The professor says she will not cover it in class and will not put questions about it on the quiz.

39. **Prospective graphical interference question — Strong prospective cue.** Lines 95–119: the professor says she could choose a random location and ask whether it has complete constructive interference, complete destructive interference, or neither.

40. **Know the general phase-difference equation and classification conditions — Strong contextual.** Lines 355–379 identify the equation “we'll be using,”

    $$
    \Delta\phi=\frac{2\pi\Delta r}{\lambda}+\Delta\phi_0,
    $$

    together with constructive interference at $\Delta\phi=2\pi m$ and destructive interference at odd multiples of $\pi$.

41. **Put wave-speed constants on the note sheet — Direct recommendation.** Lines 401–413: if students do not know the speed of light from memory, it should be on the note sheet, along with the speed of sound:

    $$
    c=3.0\times10^8\ \mathrm{m/s},
    \qquad
    v_{\text{sound}}=343\ \mathrm{m/s}.
    $$

    Lines 593–601 repeat that $343\ \mathrm{m/s}$ should be on the note sheet for sound-wave problems.

42. **Reduce symbolically to the given variables before substitution — Strong work instruction.** Lines 459–489: the phase-difference problem is carried to an expression entirely in the given variables; only then are values inserted.

43. **Include the initial relative source phase — Strong work/content cue.** Lines 545–569: the professor explains that forgetting the additional $\pi$ for initially out-of-phase sources changes the classification and says students need to pay attention to the sources' relative phase.

44. **Draw missing geometry and list givens — Strong work instruction.** Lines 675–699: when the prompt has no diagram, the professor tells students to write what they know and draw the geometry before beginning the calculation.

45. **Keep the integer mode $m$ until the end — Strong problem-solving instruction.** Lines 701–731: for the first point of maximum sound intensity, do not assume $m=0$ or $m=1$ prematurely; retain $m$ throughout the equations and select the physically valid value at the end.

## Explicit note-sheet content

| Item | Evidence | Strength |
|---|---|---|
| Four Doppler equations: moving observer/source, toward/away | Jul. 28 raw transcript, lines 559–655 | Direct |
| Speed of sound in air, $343\ \mathrm{m/s}$ | Jul. 28, lines 823–839; Jul. 30, lines 593–601 | Direct |
| Speed of light, $3.0\times10^8\ \mathrm{m/s}$ | Jul. 30, lines 401–413 | Direct |
| Oscillation and wave material generally | Jul. 21, lines 21–45; Jul. 22, lines 21–25 | Direct but nonspecific |

No other formula, table, constant, or diagram is explicitly said to belong on the Quiz 3 note sheet in these M4–M5 transcripts.

## Work and points index

### Directly stated

- Submit the quiz note sheet with photo ID. The July 21 statement explicitly says Quiz 2 credit is withheld until this is done; the July 28 instruction applies the same submission procedure to Quiz 3.
- Quiz 3 uses the same format as the first two quizzes, but these lectures do not repeat the earlier format or rubric.

### Strong or supporting instructions, but not explicit point rules

- Interpret SHM position/velocity/acceleration graphs and extract quantities from them.
- Keep units through substitutions.
- Use the significant figures supported by the given data.
- Write equations in terms of known/given variables before inserting numbers.
- Carry a symbolic solution to the end before numerical substitution.
- Draw and label the geometry that produces the equations.
- Use a diagram to estimate the expected magnitude and reject physically implausible results.
- Understand what each symbol and equation means in context.
- Select the correct Doppler case before doing algebra.
- Draw standing-wave/harmonic patterns before calculating wavelengths and frequencies.
- Include the initial relative phase of two sources in interference calculations.
- Keep the interference-order integer $m$ until the end instead of guessing it early.

### Not found

- No explicit allocation of points among diagrams, governing equations, symbolic algebra, numerical substitution, units, or final answers.
- No statement that a particular Quiz 3 derivation must be reproduced for a stated number of points.
- No explicit partial-credit rule.
- No statement that every emphasized lecture example will appear.

## Scope map and likely question families

This table translates the professor's broad scope statements into the concrete skills taught in each lecture. These are **scope implications**, not leaked questions.

| Date | Material inside the declared scope | Strongest question-type signals |
|---|---|---|
| Jul. 21 | SHM; $x$, $v$, and $a$; period/frequency; spring energy | Read an SHM graph; extract $A,T,f,\omega,v_{\max}$; determine direction/speeding up; use spring energy |
| Jul. 22 | Simple and physical pendula | Use the small-angle period formula; compute $I$ and center of mass; apply the parallel-axis theorem to composite pendula |
| Jul. 23 | Connection from oscillators to traveling waves; wave types; string waves | Distinguish wave motion from medium-particle motion; use $v=\sqrt{T/\mu}$; relate $v,f,\lambda$ |
| Jul. 27 | Wave function/direction; refraction; wavefronts; intensity | Read a traveling-wave function; determine propagation/particle direction; use wavelength changes in a material; use inverse-square intensity |
| Jul. 28 | Intensity level and Doppler effect | Manipulate decibel/intensity relations symbolically; choose the correct Doppler case and solve for an unknown |
| Jul. 29 | Superposition; standing waves; harmonics in strings and pipes | Draw nodes/antinodes; infer wavelength; calculate fundamental/harmonic frequencies; distinguish open/closed boundary conditions |
| Jul. 30 | Phase and two-source interference | Determine constructive/destructive interference from phase/path difference; solve source-geometry problems; retain and test the order $m$ |

## Exclusion index

| Material | Status | Evidence |
|---|---|---|
| Damping | Explicitly not on Quiz 3 or final | Jul. 22 raw transcript, lines 35–45 |
| Driven oscillations | Explicitly not on Quiz 3 or final | Jul. 22 raw transcript, lines 35–45 |
| Beats/beating | Explicitly no quiz questions | Jul. 30 raw transcript, lines 41–55 |
| Detailed reflection/transmission at a medium discontinuity | Strong implied exclusion; dropped from summer coverage | Jul. 29 raw transcript, lines 145–183 |
| Pressure/density derivation of sound speed | Strong implied exclusion; labeled an aside and “don't worry about that” | Jul. 29 raw transcript, lines 923–947 |
| Quantum-level coupling between waves | Supporting exclusion only; expressly not pursued in detail | Jul. 29 raw transcript, lines 77–91 |
| Exact finite-angle nonlinear pendulum treatment | Not pursued, but not explicitly excluded from the quiz | Jul. 22 raw transcript, lines 279–287 |

Basic reflection, superposition, standing waves, and hard/soft boundary behavior should **not** be removed merely because discontinuity details were dropped.

## Audit notes and false positives

- References to a “pre-class quiz” or “pre-lecture question” are formative activities, not promises about Quiz 3.
- Requests to enter Poll Everywhere answers for participation credit concern class participation, not quiz grading.
- Quiz 1X/2X deadlines and grading-status announcements do not predict Quiz 3 content and are omitted except where needed to understand the chronology.
- “Important” statements were included only when they identified a concrete skill within the declared Quiz 3 unit. Ordinary emphasis on intermediate algebra was not treated as a quiz promise.
- The direct professor statements support broad scope, exclusions, note-sheet content, and procedure. The likely-question table is an inference from those statements and the emphasized practice—not an assertion that exact questions were disclosed.
