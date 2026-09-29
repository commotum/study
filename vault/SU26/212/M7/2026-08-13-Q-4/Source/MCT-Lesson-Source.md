# MCT Q4 Lesson Source Specification

This file defines the canonical three-file MCT lesson sequence for Quiz 4. It covers the attachment-selected M6 wave-optics videos: double-slit maxima, diffraction-grating line density and principal maxima, and single-slit central-width geometry. Coverage is limited to the three exact videos and their two paired lecture notes; overview-only material is not promoted into invented lessons.

## Scope and method

- Scope is exactly the three attachment videos listed below. No `Video-Matches` JSON was used and no unassigned video was added.
- Every listed SRT was read from beginning to end. Repeating auto-caption cues were normalized into chronological spoken text while retaining cue start times.
- Both corresponding `Source/Lecture-Notes.md` files were read completely.
- The first single-slit prompt was not fully stated in the captions, so the local MP4 frame at 00:03:27 was inspected to recover the exact $680\,\mathrm{nm}$ wavelength, $2.0\times10^{-6}\,\mathrm m$ slit width, $1.4\,\mathrm m$ screen distance, diagram relationships, and the request for full central width in degrees and meters.
- Each target below owns one reusable equation-selection or geometry decision. Repeated double-slit/grating structure is linked but not duplicated.

## Counts

| Lecture label | Exact videos read | Target lessons | Notes |
|---|---:|---:|---|
| M6-1 | 2 | 2 | Double-slit maxima; grating density/maxima |
| M6-2 | 1 | 1 | Single-slit minima and central width |
| **Total** | **3** | **3** | Lecture-only grating order limits remain a supplement to Problem 2. |

## Exact source map

### M6-1 — `2026-08-05-M6-1`

- [xaAthgG0o8o](<../../../M6/2026-08-05-M6-1/Source/mct-Young's Double Slit Experiment/Young's Double Slit Experiment [xaAthgG0o8o].en.srt>)
- [gf7j2fumz70](<../../../M6/2026-08-05-M6-1/Source/mct-Diffraction Grating Problems - Physics/Diffraction Grating Problems - Physics [gf7j2fumz70].en.srt>)
- Lecture notes: [Lecture-Notes.md](<../../../M6/2026-08-05-M6-1/Source/Lecture-Notes.md>)

### M6-2 — `2026-08-06-M6-2`

- [9hCrhllI0ck](<../../../M6/2026-08-06-M6-2/Source/mct-Single Slit Diffraction - Physics Problems/Single Slit Diffraction - Physics Problems [9hCrhllI0ck].en.srt>)
- Lecture notes: [Lecture-Notes.md](<../../../M6/2026-08-06-M6-2/Source/Lecture-Notes.md>)

---

## Canonical lesson targets

## Problem 1

### Lesson 1 — Choose the Angular or Screen-Position Form for Double-Slit Maxima

Lecture label: **M6-1**

Target file: `../Lessons/MCT-Problem-1.md`

**Operational core move:** Label the bright order $m$, then use $d\sin\theta_m=m\lambda$ when an angle is given or needed. When a screen position is involved, connect it with $y_m=L\tan\theta_m$, using $y_md\approx Lm\lambda$ only after verifying that the angle is small.

**Recognition cues:** two slits, a bright fringe/order, slit separation $d$, an angle from the central axis, screen distance $L$, or distance $y_m$ from the central maximum.

**Exact transcript and timestamps:** `xaAthgG0o8o`, 00:00:01–00:07:31, 00:07:33–00:10:42, 00:10:45–00:13:08, and 00:13:11–00:16:22.

**Source-video material to preserve:**

- A first-order bright fringe at $1.5^\circ$ with $\lambda=600\,\mathrm{nm}$ gives $d=2.29\times10^{-5}\,\mathrm m=0.0229\,\mathrm{mm}$. With the screen $L=4.5\,\mathrm m$ away, find $y_1=0.118\,\mathrm m=11.8\,\mathrm{cm}$. Preserve the two-stage angle/slit-spacing then screen-position structure.
- $\lambda=650\,\mathrm{nm}$, $d=0.050\,\mathrm{mm}$, $L=8.5\,\mathrm m$, and the third-order bright fringe give the small-angle result $y_3=0.3315\,\mathrm m=33.15\,\mathrm{cm}$.
- Light has $\lambda_{air}=550\,\mathrm{nm}$ and passes through slits in water with $n=1.33$. With $L=3.6\,\mathrm m$ and the fourth-order fringe at $y_4=4.5\,\mathrm{mm}$, first convert to $\lambda_{water}=413.5\,\mathrm{nm}$, then find $d=1.32\,\mathrm{mm}$.

**Required content:** bright maxima use integer $m=0,\pm1,\ldots$; path difference at a bright fringe is $m\lambda$; distinguish $d$, $L$, and $y_m$; convert nm, mm, and cm to meters; show the exact route
$$
\theta_m=\sin^{-1}\left(\frac{m\lambda}{d}\right),
\qquad
y_m=L\tan\theta_m,
$$
and justify any small-angle collapse. Include that wavelength changes in a material while frequency does not.

**Exclusions:** do not label dark fringes with the maximum condition; do not claim the small-angle formula is exact; do not make the video's general interference/diffraction overview a separate lesson.

**Merged/supplemental section:** add the M6-1 lecture-note path-difference check, second bright fringe $\to\Delta r=2\lambda$; the intensity-graph example $L=0.85\,\mathrm m$, $d=0.062\,\mathrm{mm}$, $\Delta y=1.0\,\mathrm{cm}$, giving $\lambda\approx730\,\mathrm{nm}$; and the parameter check $\Delta y\propto\lambda L/d$.

## Problem 2

### Lesson 2 — Convert Diffraction-Grating Line Density into an Exact Maximum

Lecture label: **M6-1**

Target file: `../Lessons/MCT-Problem-2.md`

**Operational core move:** Convert the stated line density to lines per meter, invert it to obtain spacing $d=1/N$, then apply $d\sin\theta_m=m\lambda$ with consistent units.

**Recognition cues:** diffraction grating, “lines per cm/mm,” grating spacing, principal maximum, order angle, wavelength, or maximum possible order.

**Exact transcript and timestamps:** `gf7j2fumz70`, 00:00:01–00:04:23, 00:04:28–00:07:01, and 00:07:05–00:10:03.

**Source-video material to preserve:**

- $5000$ lines/cm $\to5.00\times10^5$ lines/m $\to d=2.00\times10^{-6}\,\mathrm m$; with $m=2$ and $\lambda=650\,\mathrm{nm}$, $\theta_2=40.5^\circ$.
- $10000$ lines/cm $\to1.00\times10^6$ lines/m $\to d=1.00\times10^{-6}\,\mathrm m$; a third-order maximum at $25^\circ$ gives $\lambda=1.41\times10^{-7}\,\mathrm m=141\,\mathrm{nm}$.
- A second-order maximum at $18^\circ$ with $\lambda=540\,\mathrm{nm}$ gives $d=3.495\times10^{-6}\,\mathrm m$, $N=2.86\times10^5$ lines/m, or $2861$ lines/cm.

**Required content:** line density and spacing are reciprocals with reciprocal units; use exact sine at grating-sized angles; include both directions of conversion; enforce the physical restriction
$$
\left|\frac{m\lambda}{d}\right|\le1.
$$

**Exclusions/correction:** the narration repeatedly calls the device a “diffraction gradient”; normalize it to **diffraction grating**. Do not assume grating peaks are evenly spaced on a screen at large angles. Spectroscopy history is overview-only and outside this operational lesson.

**Merged/supplemental section:**

- M6-1 exact screen-geometry variant: $d=3.0\,\mu\mathrm m$, $L=1.8\,\mathrm m$, and $y_3=1.20\,\mathrm m$ give $\theta_3=33.7^\circ$ and $\lambda\approx550\,\mathrm{nm}$. Contrast the invalid small-angle result $670\,\mathrm{nm}$.
- M6-2 line-density variant: $\lambda=633\,\mathrm{nm}$, $L=2.4\,\mathrm m$, and separation between the two first-order peaks $1.70\,\mathrm m$, so $y_1=0.85\,\mathrm m$, $\theta_1\approx19.5^\circ$, and density about $5.3\times10^2$ lines/mm.
- M6-2 order-limit extension: $d=1.8\times10^{-6}\,\mathrm m$ and $\lambda=633\,\mathrm{nm}$ give $d/\lambda=2.84$, hence $m_{max}=2$, allowed orders $-2,-1,0,1,2$, and five total maxima. Keep this as a section inside the grating lesson rather than a transcript-free standalone target.

## Problem 3

### Lesson 3 — Recover a Single-Slit Width or Central-Maximum Width

Lecture label: **M6-2**

Target file: `../Lessons/MCT-Problem-3.md`

**Operational core move:** Remember that $a\sin\theta_p=p\lambda$ locates **dark minima**. The central maximum extends from $-y_1$ to $+y_1$, so use $w=2y_1$ and $y_1=L\tan\theta_1$, with the small-angle shortcut only when warranted.

**Recognition cues:** one slit, slit width $a$ (the video uses $d$), a dark minimum, central-maximum width/angular width, or a screen-width measurement centered on the main bright band.

**Exact transcript and timestamps:** `9hCrhllI0ck`, 00:00:01–00:03:25, 00:03:26–00:07:02, and 00:07:04–00:12:37.

**Source-video material to preserve:**

- MP4-frame-verified prompt at 00:03:27: $\lambda=680\,\mathrm{nm}$, one slit $a=2.0\times10^{-6}\,\mathrm m$, and screen $L=1.4\,\mathrm m$; find the central-maximum width in degrees and meters. The first minimum has $\theta_1=\sin^{-1}(0.34)=19.877^\circ$, so the full angular width is $2\theta_1=39.75^\circ$. Then $y_1=L\tan\theta_1=0.5062\,\mathrm m$ and the full width is $w=1.01\,\mathrm m$. Preserve the deliberate rejection of the small-angle shortcut at this large angle.
- $\lambda=570\,\mathrm{nm}$, $L=7.5\,\mathrm m$, and measured central width $w=3.2\,\mathrm{cm}$: use $y_1=w/2=1.6\,\mathrm{cm}=0.016\,\mathrm m$, $\theta_1=\tan^{-1}(y_1/L)=0.122^\circ$, then $a\approx2.68\times10^{-4}\,\mathrm m=0.268\,\mathrm{mm}$. The small-angle calculation gives $0.267\,\mathrm{mm}$.

**Required content:** single-slit integer $p=1,2,\ldots$ labels minima and has no $p=0$ dark fringe; use slit width $a$ to avoid collision with double-slit/grating spacing $d$; distinguish half-width $y_1$, full linear width $2y_1$, half-angle $\theta_1$, and full angular width $2\theta_1$; show exact and small-angle workflows.

**Exclusions/corrections:** do not use $m$ as a bright-order label here. The caption calls $0.122$ “meters”; correct the unit to degrees. Do not add spectroscopy or promote the lecture-only secondary-maxima midpoint approximation into a separate lesson.

**Merged/supplemental section:** add the M6-2 dark-minimum/screen-distance variant $\lambda\approx633\,\mathrm{nm}$, $a=0.15\,\mathrm{mm}$, $y_1=2.0\,\mathrm{cm}$, giving $L\approx4.7\,\mathrm m$. Retain the warning that midpoint estimates for secondary bright maxima are approximate and that exact noncentral maxima satisfy $\tan\beta=\beta$, but keep it as a caveat rather than practice in this lesson.

## Coverage audit

- Problems 1–3 map uniquely to `../Lessons/MCT-Problem-1.md` through `../Lessons/MCT-Problem-3.md`.
- All three exact Q4 transcript IDs occur in the source map and in one timestamped lesson entry.
- Overview-only diffraction/reflection/refraction definitions, wave-versus-particle history, spectroscopy, and formula derivations without a new decision are not separate lessons.
