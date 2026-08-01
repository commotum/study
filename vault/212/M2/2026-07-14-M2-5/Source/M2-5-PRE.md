
```quiz
type: radio
id: m2-5pre-q1
shuffle: true
content: |-
  **Question 1**

  In both systems, $m_2>m_1$ and the masses are connected by a massless string. System A has a massless, frictionless pulley. System B is identical except that its pulley has mass.

  Which statement is true?

  ![](<Images/massless-vs-massive-pulley-systems.png>)
options:
- id: a
  content: |-
    The magnitude of the acceleration of $m_2$ is greater in System A than in System B.
  correct: true
  feedback: |-
    In System B, some of the gravitational energy goes into rotating the massive pulley. Equivalently, its rotational inertia adds resistance to the motion:

    $$
    a_A=\frac{(m_2-m_1)g}{m_1+m_2},
    $$

    $$
    a_B=\frac{(m_2-m_1)g}{m_1+m_2+\dfrac{I}{r^2}}.
    $$

    Because $I/r^2>0$, the acceleration satisfies $a_B<a_A$.
- id: b
  content: |-
    The magnitude of the acceleration of $m_2$ is less in System A than in System B.
- id: c
  content: |-
    The magnitude of the acceleration of $m_2$ is the same in both systems.
```
