
---
title: "Snell's Law"
source: "http://khadley.com/Courses/Physics/ph_212/topics/rayOptics/snell-s-law.html"
author:
published:
created: 2026-08-10
description:
tags:
  - "clippings"
---
## [PH 212](http://khadley.com/Courses/Physics/ph_212/topics/index.aspx)

## Snell's law

## Practice Problems

```quiz
type: radio
id: khadley-snells-law-q1
shuffle: true
content: |-
  **Question 1**

  Which quantity remains unchanged when light passes from air into glass?

  ![[Images/clicker4.jpg]]
options:
- id: wavelength
  content: Wavelength
  feedback: |-
    The wave speed changes in glass while frequency is fixed by the source, so $\lambda=v/f$ must change.
- id: frequency
  content: Frequency
  correct: true
  feedback: |-
    Frequency is fixed by the source and must remain continuous across the boundary. The change in speed therefore appears as a change in wavelength.
- id: speed
  content: Effective speed
  feedback: |-
    Glass has a larger refractive index than air, so the effective speed $v=c/n$ is smaller in glass.
```

![[Images/reflectrefract2.jpg]] ![[Images/rayeqn1.jpg]] ![[Images/u45969-20.png|The index of refraction is $n=c/v$, and Snell's law is $n_1\sin\theta_1=n_2\sin\theta_2$.]] ![[Images/indextable.jpg]]

The index of refraction is a property of a medium. It describes how light propagates in that medium.

When light crosses from one medium into another medium with a different index of refraction, the ray bends to minimize time.

```quiz
type: radio
id: khadley-snells-law-q2
shuffle: true
content: |-
  **Question 2**

  Which index of refraction is larger?

  ![[Images/clicker2-1.jpg]]
options:
- id: n1
  content: $n_1$
  feedback: |-
    The ray bends toward the normal after entering medium 2, which means its speed decreases and its index increases there.
- id: n2
  content: $n_2$
  correct: true
  feedback: |-
    Bending toward the normal indicates entry into the slower, higher-index medium, so $n_2>n_1$.
- id: indeterminate
  content: Cannot be determined
  feedback: |-
    The bending direction relative to the normal is sufficient to compare the two indices even without numerical angles.
```

<iframe src="https://phet.colorado.edu/sims/html/bending-light/latest/bending-light_en.html" width="800" height="600" allowfullscreen=""></iframe>

[PhET interactive](https://phet.colorado.edu/sims/html/bending-light/latest/bending-light_en.html)

```quiz
type: radio
id: khadley-snells-law-q3
shuffle: true
content: |-
  **Question 3**

  A ray crosses the three media shown. Which relationship between $n_1$ and $n_3$ is true?

  ![[Images/clicker3.jpg]]
options:
- id: n1-greater
  content: $n_1>n_3$
  feedback: |-
    Applying Snell's law at both interfaces shows that the smaller $10^\circ$ angle in medium 3 corresponds to the larger index, not the smaller one.
- id: equal
  content: $n_1=n_3$
  feedback: |-
    If $n_1=n_3$, the ray would have the same angle to the normal in those two media. The diagram shows $20^\circ$ and $10^\circ$.
- id: n3-greater
  content: $n_3>n_1$
  correct: true
  feedback: |-
    Across both boundaries, $n_1\sin20^\circ=n_3\sin10^\circ$. Since $\sin20^\circ>\sin10^\circ$, $n_3$ must exceed $n_1$.
```

## Total Internal Reflection

![[Images/totalinternalreflection.jpg]] ![[Images/u46250-14.png|Transmission gets weaker as the angle of incidence increases. Internal reflection gets stronger. When the angle of transmission reaches 90 degrees, no light is transmitted - it is all reflected internally. The incident angle that results in total internal reflection for two media is called the critical angle, qc. Notice that total internal reflection only happens when n2 < n1 ]] ![[Images/fiberoptics.jpg]]

Fiber optics utilizes total internal reflection to propagate light along a long, narrow glass tube. The tube can bend slightly, as long as the bending doesn't increase the angle of incidence beyond the critical angle (or break the glass!)

```quiz
type: blank
id: khadley-snells-law-q4
input_mode: math
require_exact: true
content: |-
  **Question 4**

  Calculate the critical angle for light traveling from glass $(n=1.5)$ into air $(n=1.0)$. Enter degrees: ==42==
feedback: |-
  At the critical angle the refracted ray is at $90^\circ$, so $1.5\sin\theta_c=1.0$. Thus $\theta_c=41.8^\circ$, which rounds to $42^\circ$.
```

## Image Formation by Refraction

![[Images/23-25-figurea.jpg]] ![[Images/23-25-figureb.jpg]]

The refraction of light rays as they pass from the water to air cause the virtual image of the fish at P' to appear closer than the fish really is.

![[Images/23-26-figure.jpg]]

Angles are measured with respect to the optical axis. Note that the distance l is common to both the incident and reflected rays.

![[Images/rayeqn2.jpg]]

The fact that the relationship between the image distance and the object distance is independent of the angle means that all paraxial rays diverge from the same point P' (in the small angle approximation).

![[Images/spearfish1.jpg]]

```quiz
type: blank
id: khadley-snells-law-q5
input_mode: math
require_exact: true
content: |-
  **Question 5**

  A fish is viewed from air along a ray that makes $50^\circ$ with the normal in air. For water with $n=1.33$, find the ray angle in the water. Enter degrees: ==35==

  ![[Images/spearfish1.jpg]]
feedback: |-
  Snell's law gives $1.33\sin\theta_{\mathrm{water}}=1.00\sin50^\circ$. Therefore $\theta_{\mathrm{water}}=35.2^\circ$, which rounds to $35^\circ$.
```

[PhET Interactive](http://phet.colorado.edu/sims/html/bending-light/latest/bending-light_en.html)

## Color and Dispersion

![[Images/23-28-figure.jpg]]

The index of refraction of glass is higher for short wavelength light than for long wavelength light. This means that violet light refracts more than red.

![[Images/prism.jpg]]

Colors of light spread out through a prism because the index of refraction depends on wavelength.

![[Images/raindrop1.jpg]] ![[Images/raindrop2.jpg]]

The incident angle of light upon a spherical raindrop can mean that there is a lot of internally reflected light. The internally reflected light undergoes dispersion, separating out the colors of light. The light emerges at different angles for different wavelengths. Since red light refracts less, we need to look higher to see refracted red rays.

![[Images/rainbow2.jpg]]

Image source
