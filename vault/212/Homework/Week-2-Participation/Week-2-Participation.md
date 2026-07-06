## M1-3pre

**Question 1**

```quiz
type: radio
id: m1-3pre-q1
content: |-
  ![](<Source/Week-2-Participation/Images/ferris-wheel-top-bottom-normal-force.png>)
  
  A person is riding on a Ferris wheel which is rotating at constant angular speed. How does the magnitude of the normal force of the Ferris wheel on the person at the top of the wheel compare to the magnitude of the normal force of the wheel on the person at the bottom of the wheel?
options:
- id: a
  content: |-
    $N_{\text{top}} > N_{\text{bottom}}$
- id: b
  content: |-
    $N_{\text{top}} = N_{\text{bottom}}$
- id: c
  content: |-
    $N_{\text{top}} < N_{\text{bottom}}$
  correct: true
  feedback: |-
    At the top, gravity helps provide the downward centripetal force, so $N_{\text{top}}=mg-\frac{mv^2}{r}$. At the bottom, the normal force must exceed gravity, so $N_{\text{bottom}}=mg+\frac{mv^2}{r}$.
```

---
## M1-3asy

**Question 1**

```quiz
type: blank
id: m1-3asy-q1
content: |-
  A Ferris wheel of radius $42\ \mathrm{m}$ is rotating at a constant angular velocity of $0.16\ \mathrm{rad}/\mathrm{s}$. What is the speed of a particle on the rim of the wheel?
  
  Enter your answer in $\mathrm{m}/\mathrm{s}$.
  
  Answer: ==6.7==
feedback: |-
  Use $v=r\omega=(42)(0.16)=6.72\ \mathrm{m}/\mathrm{s}$, which rounds to $6.7\ \mathrm{m}/\mathrm{s}$.
```

---
**Question 2**

```quiz
type: radio
id: m1-3asy-q2
content: |-
  A person rides on a Ferris wheel of radius $r$ at constant angular velocity $\omega$. How does the normal force exerted on the rider from their seat at the top compare to the normal force on the rider from their seat at the bottom?
options:
- id: a
  content: |-
    $N_{\text{top}}=N_{\text{bottom}}$
- id: b
  content: |-
    $N_{\text{top}}>N_{\text{bottom}}$
- id: c
  content: |-
    $N_{\text{top}}<N_{\text{bottom}}$
  correct: true
  feedback: |-
    At the top, $mg-N_{\text{top}}=m\omega^2r$, so $N_{\text{top}}=mg-m\omega^2r$. At the bottom, $N_{\text{bottom}}-mg=m\omega^2r$, so $N_{\text{bottom}}=mg+m\omega^2r$.
```

---
**Question 3**

```quiz
type: blank
id: m1-3asy-q3
content: |-
  A Ferris wheel of radius $42\ \mathrm{m}$ is rotating at a constant angular velocity of $0.16\ \mathrm{rad}/\mathrm{s}$. What is the magnitude of the normal force on a $68\ \mathrm{kg}$ person from their seat when they are at the bottom of the wheel?
  
  Enter your answer in newtons.
  
  Answer: ==740==
feedback: |-
  At the bottom, $N-mg=m\omega^2r$, so $N=mg+m\omega^2r=(68)(9.8)+(68)(0.16)^2(42)\approx 740\ \mathrm{N}$.
```

---
**Question 4**

```quiz
type: blank
id: m1-3asy-q4
content: |-
  A Ferris wheel of radius $42\ \mathrm{m}$ is rotating at a constant angular velocity of $0.16\ \mathrm{rad}/\mathrm{s}$. What is the magnitude of the normal force on a $68\ \mathrm{kg}$ person from their seat when they are at the top of the wheel?
  
  Enter your answer in newtons.
  
  Answer: ==590==
feedback: |-
  At the top, $mg-N=m\omega^2r$, so $N=mg-m\omega^2r=(68)(9.8)-(68)(0.16)^2(42)\approx 590\ \mathrm{N}$.
```

---
**Question 5**

```quiz
type: blank
id: m1-3asy-q5
content: |-
  A $1.3\ \mathrm{g}$ coin on a turntable at radius $0.35\ \mathrm{m}$ has maximum static friction coefficient $\mu_s=0.18$ between the coin and the surface.
  
  Find $\omega$ in $\mathrm{rad}/\mathrm{s}$ such that the coin just starts to slip.
  
  Answer: ==2.2==
feedback: |-
  At the slipping threshold, static friction provides the centripetal force: $\mu_smg=m\omega^2r$. Thus $\omega=\sqrt{\frac{\mu_s g}{r}}=\sqrt{\frac{(0.18)(9.8)}{0.35}}\approx 2.2\ \mathrm{rad}/\mathrm{s}$.
```

---
## M1-4pre

**Question 1**

```quiz
type: radio
id: m1-4pre-q1
content: |-
  ![](<Source/Week-2-Participation/Images/icy-banked-curve-free-body-diagrams.png>)
  
  A car of mass $m$ is going around an icy banked curve with no friction. Which free-body diagram, in side view, could represent the car?
options:
- id: a
  content: |-
    A
- id: b
  content: |-
    B
  correct: true
  feedback: |-
    Since the curve is icy, there is no friction. The only forces are gravity downward and the normal force perpendicular to the surface, pointing up and toward the center of the curve.
- id: c
  content: |-
    C
- id: d
  content: |-
    D
- id: e
  content: |-
    E
```

---

## M1-4asy

**Question 1**

```quiz
type: radio
id: m1-4asy-q1
content: |-
  A car travels around a level circle at constant speed. The diagram shows the car as seen from above and from the side. Choose the correct free-body diagram for the car as seen from the side view.
  
  Be sure to include your explanation in the document you upload showing your work.
  
  ![](<Source/Week-2-Participation/Images/level-curve-free-body-diagrams.png>)
options:
- id: a
  content: |-
    A
  correct: true
  feedback: |-
    The car has no vertical acceleration, so $N=mg$. Static friction supplies the centripetal force and points toward the center of the circle, which is to the right in the side view.
- id: b
  content: |-
    B
- id: c
  content: |-
    C
- id: d
  content: |-
    D
```

---
**Question 2**

```quiz
type: blank
id: m1-4asy-q2
content: |-
  A $1800\ \mathrm{kg}$ car is going around a level circular curve of radius $49\ \mathrm{m}$ at a speed of $16\ \mathrm{m}/\mathrm{s}$. What is the coefficient of static friction between the car's tires and road that keeps it from sliding? Assume it is going as fast as it can go without sliding.
  
  ![](<Source/Week-2-Participation/Images/level-curve-car-diagram.png>)
  
  Answer: ==0.53==
feedback: |-
  For a flat curve, static friction provides the radial force. At the maximum speed before sliding, $\mu_smg=\frac{mv^2}{r}$, so $\mu_s=\frac{v^2}{rg}=\frac{16^2}{(49)(9.8)}\approx 0.53$.
```

---
**Question 3**

```quiz
type: blank
id: m1-4asy-q3
content: |-
  How fast does a $1800\ \mathrm{kg}$ car need to go to navigate an icy, no-friction banked curve of radius $48\ \mathrm{m}$ and banking angle $6.2^\circ$ without sliding?
  
  Enter your answer in $\mathrm{m}/\mathrm{s}$.
  
  ![](<Source/Week-2-Participation/Images/banked-curve-car-diagram.png>)
  
  Answer: ==7.2==
feedback: |-
  On an icy banked curve, the only forces are $mg$ downward and $N$ perpendicular to the road. Dividing $N\sin\theta=\frac{mv^2}{r}$ by $N\cos\theta=mg$ gives $\tan\theta=\frac{v^2}{rg}$, so $v=\sqrt{rg\tan\theta}\approx 7.2\ \mathrm{m}/\mathrm{s}$.
```

---
**Question 4**

```quiz
type: radio
id: m1-4asy-q4
content: |-
  A car safely navigates an icy banked curve at speed $v$. Now consider that the ice has melted and there is static friction between the tires and road. What is the direction of the friction force if the car is going faster than $v$?
  
  ![](<Source/Week-2-Participation/Images/banked-curve-car-diagram.png>)
options:
- id: a
  content: |-
    in the direction the car is moving around the curve
- id: b
  content: |-
    in the opposite direction that the car is moving around the curve
- id: c
  content: |-
    up the slope of the banked turn
- id: d
  content: |-
    down the slope of the banked turn
  correct: true
  feedback: |-
    At the no-friction speed, the horizontal component of the normal force gives exactly the needed radial force. If the car goes faster, it tends to slide up the bank, so static friction opposes that tendency by pointing down the slope.
- id: e
  content: |-
    none of the above
```

---
**Question 5**

```quiz
type: blank
id: m1-4asy-q5
content: |-
  Consider a car of mass $m$ going around a banked curve of angle $\theta$ and radius $r$. What is the maximum speed at which the car can navigate the curve without sliding, where the coefficient of maximum static friction is $\mu_s$?
  
  Consider the case where $r=55\ \mathrm{m}$, $m=1400\ \mathrm{kg}$, $\theta=12^\circ$, and $\mu_s=0.65$. Enter your answer in $\mathrm{m}/\mathrm{s}$.
  
  ![](<Source/Week-2-Participation/Images/banked-curve-car-diagram.png>)
  
  Answer: ==23.2==
feedback: |-
  At maximum speed, friction points down the slope. Combining the vertical and radial force equations gives $v_{\max}=\sqrt{rg\left(\frac{\sin\theta+\mu_s\cos\theta}{\cos\theta-\mu_s\sin\theta}\right)}$, which gives $23.2\ \mathrm{m}/\mathrm{s}$ for the given values.
```

---
**Question 6**

```quiz
type: radio
id: m1-4asy-q6
content: |-
  A key on a string traces out a horizontal circle as shown. Assume there is no air resistance. Which free-body diagram could accurately depict the key?
  
  ![](<Source/Week-2-Participation/Images/conical-pendulum-key-free-body-diagrams.png>)
options:
- id: a
  content: |-
    A
- id: b
  content: |-
    B
- id: c
  content: |-
    C
  correct: true
  feedback: |-
    The key is a conical pendulum. With no air resistance, the only real forces are weight straight down and tension along the string toward the hand. There is no separate centripetal-force arrow.
- id: d
  content: |-
    D
```

---
## M1-5pre

**Question 1**

```quiz
type: radio
id: m1-5pre-q1
content: |-
  A particle is moving around a circle, with an arrow depicting the magnitude and direction of the net force acting on the particle.
  
  Which diagram represents a particle speeding up in the counterclockwise direction?
  
  ![](<Source/Week-2-Participation/Images/counterclockwise-speeding-up-net-force.png>)
options:
- id: a
  content: |-
    A
- id: b
  content: |-
    B
- id: c
  content: |-
    C
  correct: true
  feedback: |-
    At the lower-right side of the circle, centripetal force points inward toward the center, up-left. For counterclockwise speeding up, the tangential component points along the motion, up-right. The net force points between those directions, matching C.
- id: d
  content: |-
    D
- id: e
  content: |-
    E
- id: f
  content: |-
    F
- id: g
  content: |-
    G
- id: h
  content: |-
    H
```
