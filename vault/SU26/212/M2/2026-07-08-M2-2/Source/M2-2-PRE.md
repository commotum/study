
```quiz
type: radio
id: m2-2pre-q1
shuffle: true
content: |-
  **Question 1**

  Two sets of barbells with identical weights and identical center bars are configured as shown.

  Which set has the smaller moment of inertia about its center of mass?

  ![](<Images/barbell-mass-distribution.png>)
options:
- id: a
  content: |-
    Set A
- id: b
  content: |-
    Set B
  correct: true
  feedback: |-
    Moment of inertia depends on the distance of each mass from the rotation axis:

    $$
    I=\sum mr^2.
    $$

    In Set B, the weights are closer to the center of mass, so their $r$ values are smaller. The identical center bars contribute the same moment of inertia, making Set B's total moment of inertia smaller.
- id: same
  content: |-
    They have the same moment of inertia
```
