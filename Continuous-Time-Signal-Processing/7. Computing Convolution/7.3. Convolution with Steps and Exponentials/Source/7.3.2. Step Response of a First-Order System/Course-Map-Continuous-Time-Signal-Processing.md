# Continuous-Time Signal Processing

## Course Description

Continuous-Time Signal Processing develops the core concepts and analytical tools used to represent, transform, and interpret continuous-time signals and systems. The course begins with foundational signal descriptions, periodic signals, complex exponentials, and time-domain operations, then builds toward unit step and unit impulse methods, convolution, Fourier analysis, frequency response, Laplace transforms, and transfer-function-based stability analysis.

Throughout the course, students learn how these ideas provide complementary time-domain and frequency-domain views of the same systems. Applications such as RC and RLC circuits appear alongside the core theory, helping students connect mathematical representations to physical systems studied in electrical engineering, physics, communications, and control.

## Course Overview

The course begins with the foundations of continuous-time signals. Students learn to interpret signals as functions of time, read and write piecewise signal definitions, identify support and symmetry, and compute signal energy and power. Periodic signals and sinusoids are introduced together with fundamental period, angular frequency, and harmonic structure.

The course then develops the complex-exponential viewpoint that underlies much of signal processing. Students work with complex numbers in rectangular and polar form, phasors, and generalized exponential signals, using these tools to analyze sinusoidal representations and exponential growth, decay, and oscillation. Time shifting, scaling, and reversal are then studied as basic operations for manipulating signals in the time domain.

Next, students learn how unit step and unit impulse signals provide compact descriptions of signals and systems. These tools lead naturally into the study of continuous-time systems, including linearity, time invariance, and BIBO stability. For linear time-invariant systems, the course develops impulse response and convolution as a complete framework for describing system outputs.

Building on this foundation, students study Fourier methods for periodic and aperiodic signals. The course develops both continuous-time Fourier series and the continuous-time Fourier transform, including coefficient computation, transform pairs, and core properties such as time shifting, scaling, and the convolution theorem. These ideas are then used to analyze frequency response and understand how LTI systems act on sinusoidal inputs, with RC filters serving as central examples.

The final portion of the course develops Laplace-transform methods for signals, systems, and differential-equation models. Students study one-sided Laplace transforms, time shifting, derivative properties, transfer functions, poles, zeros, and stability. The course concludes by integrating time-domain, convolution, Fourier, frequency-response, and Laplace methods into broader signal-processing workflows for analyzing continuous-time systems.

## Course Outcomes

Upon successful completion of this course, students will have mastered the following:

- Represent and interpret continuous-time signals using functional, graphical, and piecewise descriptions.
- Analyze periodic signals and sinusoids in terms of amplitude, phase, fundamental period, angular frequency, and harmonic structure.
- Work with complex numbers, complex exponentials, and phasors in rectangular, polar, and amplitude-phase form.
- Analyze generalized exponential signals, including real exponentials, complex exponentials, and damped or growing sinusoids.
- Apply time shifting, time scaling, time reversal, and combined signal transformations in the continuous-time setting.
- Construct and manipulate signals using unit step and unit impulse functions, including shifted impulses and the sifting property.
- Classify continuous-time systems in terms of linearity, time invariance, and BIBO stability.
- Describe linear time-invariant systems through their impulse response and derive the continuous-time convolution integral.
- Compute convolutions of finite-duration signals, step signals, and exponential signals, and interpret the result as an LTI system output.
- Develop and compute continuous-time Fourier series representations of periodic signals and interpret coefficient, magnitude-spectrum, and phase-spectrum information.
- Compute and interpret continuous-time Fourier transforms, apply standard transform pairs and properties, and use the convolution theorem to simplify analysis.
- Analyze sinusoidal steady-state behavior of LTI systems through frequency response, including magnitude and phase effects and the behavior of RC filters.
- Apply one-sided Laplace transforms and inverse transforms to shifted signals, piecewise signals, and differential-equation models.
- Analyze transfer functions in terms of poles, zeros, and stability, and connect Laplace-domain descriptions to frequency response and circuit behavior.
- Choose appropriately among time-domain, convolution, Fourier-series, Fourier-transform, frequency-response, and Laplace-transform methods when solving integrated signal-processing problems.

## Course Content

### 1. Foundations of Continuous-Time Signals 23 topics

**1.1. Continuous-Time Signal Basics**

- 1.1.1. Continuous-Time Signals as Functions
- 1.1.2. Reading Signal Values from Graphs
- 1.1.3. Piecewise Signal Definitions
- 1.1.4. Signal Support and Zero Regions
- 1.1.5. Even and Odd Signal Symmetry
- 1.1.6. Basic Signal Parameters: Amplitude, Offset, and Duration

**1.2. Periodic Signals and Sinusoids**

- 1.2.1. Periodic Continuous-Time Signals
- 1.2.2. Fundamental Period
- 1.2.3. Fundamental Angular Frequency
- 1.2.4. Converting Between Period and Angular Frequency
- 1.2.5. Sinusoidal Signals
- 1.2.6. Amplitude and Phase of a Sinusoid
- 1.2.7. Time Shifts Caused by Phase
- 1.2.8. Harmonics of a Fundamental Frequency
- 1.2.9. Sums of Periodic Signals
- 1.2.10. Rational Period Ratios and Periodicity

**1.3. Signal Size**

- 1.3.1. Instantaneous Power of a Signal
- 1.3.2. Signal Energy
- 1.3.3. Computing Energy of Finite-Duration Signals
- 1.3.4. Computing Energy of Decaying Signals
- 1.3.5. Average Signal Power
- 1.3.6. Power of Periodic Signals
- 1.3.7. Energy Signals vs. Power Signals

### 2. Complex Numbers and Complex Exponential Signals 28 topics

**2.1. Complex Exponential Form**

- 2.1.1. Euler’s Formula
- 2.1.2. Complex Numbers in Rectangular Form
- 2.1.3. Complex Numbers in Polar Form
- 2.1.4. Complex Exponentials
- 2.1.5. Real and Imaginary Parts of Complex Exponentials
- 2.1.6. Magnitude and Phase of a Complex Exponential

**2.2. Phasors and Sinusoids**

- 2.2.1. Phasors at Initial Time
- 2.2.2. Rotating Phasors
- 2.2.3. Counterclockwise and Clockwise Rotation
- 2.2.4. Real-Axis Projection of a Phasor
- 2.2.5. Imaginary-Axis Projection of a Phasor
- 2.2.6. Representing Cosines with Complex Exponentials
- 2.2.7. Representing Sines with Complex Exponentials
- 2.2.8. Positive and Negative Frequency Components

**2.3. Adding Sinusoids with Phasors**

- 2.3.1. Phasor Representation of a Cosine
- 2.3.2. Adding Same-Frequency Cosines
- 2.3.3. Rectangular Form of a Phasor Sum
- 2.3.4. Polar Form of a Phasor Sum
- 2.3.5. Converting a Phasor Sum Back to a Sinusoid
- 2.3.6. Amplitude-Phase Form of a Sinusoidal Sum

**2.4. Generalized Exponential Signals**

- 2.4.1. The Generalized Exponential Signal $e^{st}$
- 2.4.2. Real and Imaginary Parts of $s=\sigma+j\omega$
- 2.4.3. Pure Real Exponentials
- 2.4.4. Pure Complex Exponentials
- 2.4.5. Damped Sinusoids
- 2.4.6. Growing Sinusoids
- 2.4.7. Exponential Envelopes
- 2.4.8. Periodicity of $e^{j\omega t}$

### 3. Time-Domain Signal Operations 18 topics

**3.1. Time Shifting**

- 3.1.1. Delaying a Signal
- 3.1.2. Advancing a Signal
- 3.1.3. Interpreting $x(t-T)$
- 3.1.4. Interpreting $x(t+T)$
- 3.1.5. Time Shifts of Piecewise Signals
- 3.1.6. Time Shifts of Exponential Signals

**3.2. Time Scaling**

- 3.2.1. Time Compression
- 3.2.2. Time Expansion
- 3.2.3. How Time Scaling Moves Key Time Points
- 3.2.4. Time Scaling of Piecewise Signals
- 3.2.5. Time Scaling of Exponentials
- 3.2.6. Comparing Time Shifts and Time Scaling

**3.3. Time Reversal and Combined Operations**

- 3.3.1. Time Reversal
- 3.3.2. Reflecting a Signal Across $t=0$
- 3.3.3. Time Reversal of Piecewise Signals
- 3.3.4. Time Reversal of Exponential Signals
- 3.3.5. Combined Shift and Scale Operations
- 3.3.6. Order of Operations in Signal Transformations

### 4. Unit Step and Unit Impulse Signals 24 topics

**4.1. Unit Step Function**

- 4.1.1. Definition of the Unit Step Function
- 4.1.2. Unit Step as an On-Off Switch
- 4.1.3. Shifted Unit Step Functions
- 4.1.4. Starting a Signal with a Unit Step
- 4.1.5. Delaying Exponential Signals with Unit Steps
- 4.1.6. Building Rectangular Pulses with Unit Steps

**4.2. Constructing Signals with Unit Steps**

- 4.2.1. Windowing a Signal Over a Time Interval
- 4.2.2. Building Piecewise Constant Signals
- 4.2.3. Building Piecewise Linear Signals
- 4.2.4. Building Triangular Signals
- 4.2.5. Simplifying Step-Function Expressions
- 4.2.6. Converting Graphs into Unit Step Expressions

**4.3. Unit Impulse Function**

- 4.3.1. Definition of the Unit Impulse
- 4.3.2. Impulse Area vs. Impulse Amplitude
- 4.3.3. Scaled Impulses
- 4.3.4. Shifted Impulses
- 4.3.5. Multiplying a Function by an Impulse
- 4.3.6. Multiplying a Function by a Shifted Impulse

**4.4. Sifting and Step-Impulse Relationships**

- 4.4.1. The Sifting Property
- 4.4.2. Evaluating Integrals with Shifted Impulses
- 4.4.3. Impulses with Nonstandard Arguments
- 4.4.4. Change of Variables with Impulses
- 4.4.5. Unit Step as the Integral of an Impulse
- 4.4.6. Unit Impulse as the Derivative of a Unit Step

### 5. Continuous-Time Systems 30 topics

**5.1. Input-Output Systems**

- 5.1.1. Systems as Signal Transformations
- 5.1.2. Inputs and Outputs
- 5.1.3. Continuous-Time System Notation
- 5.1.4. Filters as Systems
- 5.1.5. RC Circuits as Systems
- 5.1.6. Automobile Motion as a System
- 5.1.7. Differential Equations as Input-Output Models

**5.2. Linearity**

- 5.2.1. Additivity
- 5.2.2. Homogeneity
- 5.2.3. The Superposition Test
- 5.2.4. Testing Linearity from a System Rule
- 5.2.5. Linear Derivative Systems
- 5.2.6. Constant Offset Systems
- 5.2.7. Squaring Systems
- 5.2.8. Linear vs. Nonlinear Systems

**5.3. Time Invariance**

- 5.3.1. Meaning of Time Invariance
- 5.3.2. The Shift-Then-System Path
- 5.3.3. The System-Then-Shift Path
- 5.3.4. Testing Time Invariance
- 5.3.5. Time-Invariant Memoryless Systems
- 5.3.6. Time-Varying Systems with Explicit $t$
- 5.3.7. Time Invariance vs. Signal Shifting

**5.4. Stability**

- 5.4.1. Bounded Signals
- 5.4.2. BIBO Stability
- 5.4.3. Stable Physical Systems
- 5.4.4. Damping and Dissipation
- 5.4.5. Unstable Systems
- 5.4.6. Integrator-Type Systems
- 5.4.7. Bounded Inputs with Unbounded Outputs
- 5.4.8. Stability Classification from Examples

### 6. LTI Systems and Impulse Response 19 topics

**6.1. LTI Systems**

- 6.1.1. Linear Time-Invariant Systems
- 6.1.2. Why Linearity and Time Invariance Matter Together
- 6.1.3. The Unit Impulse Input
- 6.1.4. Impulse Response
- 6.1.5. Impulse Response as a System Description
- 6.1.6. Shifted Impulses Through an LTI System
- 6.1.7. Scaled Impulses Through an LTI System

**6.2. Signal Decomposition into Impulses**

- 6.2.1. Representing Signals with Shifted Impulses
- 6.2.2. Continuous-Time Sifting Representation
- 6.2.3. Weighted Impulse Decomposition
- 6.2.4. From Impulse Decomposition to System Output
- 6.2.5. Deriving the Convolution Integral

**6.3. Convolution Setup**

- 6.3.1. Definition of Continuous-Time Convolution
- 6.3.2. Meaning of the Dummy Variable $\tau$
- 6.3.3. Holding $t$ Fixed During Convolution
- 6.3.4. Rewriting Signals as Functions of $\tau$
- 6.3.5. Why $h(t-\tau)$ Appears
- 6.3.6. Flip-Shift-Multiply-Integrate Procedure
- 6.3.7. Convolution as Overlap Area

### 7. Computing Convolution 25 topics

**7.1. Convolution Mechanics**

- 7.1.1. Finding the Support of $x(\tau)$
- 7.1.2. Finding the Support of $h(t-\tau)$
- 7.1.3. Determining the Overlap Interval
- 7.1.4. Setting Integral Bounds from Overlap
- 7.1.5. Evaluating Convolution Piece by Piece
- 7.1.6. Recognizing No-Overlap Regions
- 7.1.7. Using Commutativity to Simplify Convolution

**7.2. Convolution of Simple Signals**

- 7.2.1. Convolution of Two Equal-Width Rectangular Pulses
- 7.2.2. Convolution of Unequal-Width Rectangular Pulses
- 7.2.3. Triangular Outputs from Rectangular Pulses
- 7.2.4. Trapezoidal Outputs from Rectangular Pulses
- 7.2.5. Geometric Area Methods for Rectangular Pulse Convolution

**7.3. Convolution with Steps and Exponentials**

- 7.3.1. Convolution of a Unit Step with a Decaying Exponential
- 7.3.2. Step Response of a First-Order System
- 7.3.3. Convolution of Two One-Sided Exponentials
- 7.3.4. Equal-Exponent Exponential Convolution
- 7.3.5. Unequal-Exponent Exponential Convolution
- 7.3.6. Interpreting Causal Convolution

**7.4. Direct Convolution for LTI Systems**

- 7.4.1. System Output from Input and Impulse Response
- 7.4.2. Breaking Convolution into Time Regions
- 7.4.3. Convolution with Finite-Duration Signals
- 7.4.4. Convolution with Sloped Signals
- 7.4.5. Using Geometry for Piecewise Convolution
- 7.4.6. Checking Continuity of a Convolution Result
- 7.4.7. Interpreting Convolution as LTI System Output

### 8. Continuous-Time Fourier Series 34 topics

**8.1. Fourier Series Motivation**

- 8.1.1. Periodic Signals as Sums of Sinusoids
- 8.1.2. DC Component
- 8.1.3. Fundamental Frequency in Fourier Series
- 8.1.4. Harmonic Frequencies
- 8.1.5. Sine and Cosine Basis Functions
- 8.1.6. Time-Domain vs. Frequency-Domain Views

**8.2. Trigonometric Fourier Series**

- 8.2.1. Trigonometric Fourier Series Form
- 8.2.2. Cosine Coefficients
- 8.2.3. Sine Coefficients
- 8.2.4. Meaning of Fourier Coefficients
- 8.2.5. Harmonic Index $k$
- 8.2.6. Reconstructing a Periodic Signal from Harmonics

**8.3. Complex Fourier Series**

- 8.3.1. Complex-Exponential Fourier Series Form
- 8.3.2. Complex Fourier Coefficients
- 8.3.3. Coefficient Integral Over One Period
- 8.3.4. DC Coefficient as Average Value
- 8.3.5. Relationship Between Trigonometric and Complex Forms
- 8.3.6. Positive and Negative Harmonics

**8.4. Computing Fourier Series Coefficients**

- 8.4.1. Fourier Coefficients of a Sine Wave
- 8.4.2. Fourier Coefficients of a Rectangular Periodic Signal
- 8.4.3. Duty Cycle and DC Value
- 8.4.4. Even and Odd Harmonics
- 8.4.5. Fourier Coefficients of a Periodic Exponential
- 8.4.6. Complex-Valued Fourier Coefficients
- 8.4.7. Magnitude Spectrum
- 8.4.8. Phase Spectrum

**8.5. Fourier Series Properties**

- 8.5.1. Time-Shifting Property
- 8.5.2. Phase Change from Time Shifting
- 8.5.3. Magnitude Spectrum Under Time Shifting
- 8.5.4. DC Adjustment from Vertical Shifting
- 8.5.5. Time-Reversal Property
- 8.5.6. Time-Scaling Property
- 8.5.7. Conjugate Symmetry for Real Signals
- 8.5.8. Using Properties Instead of Recomputing Integrals

### 9. Continuous-Time Fourier Transform 31 topics

**9.1. From Fourier Series to Fourier Transform**

- 9.1.1. Periodic vs. Aperiodic Signals
- 9.1.2. Aperiodic Signals as Infinite-Period Limits
- 9.1.3. Frequency Spacing in Fourier Series
- 9.1.4. Continuous Frequency
- 9.1.5. Fourier Transform Definition
- 9.1.6. Inverse Fourier Transform
- 9.1.7. Fourier Transform Pair Notation

**9.2. Basic Fourier Transform Pairs**

- 9.2.1. Fourier Transform of a One-Sided Exponential
- 9.2.2. Real and Imaginary Parts of an Exponential Transform
- 9.2.3. Fourier Transform of a Rectangular Pulse
- 9.2.4. Sinc-Shaped Spectra
- 9.2.5. Zeros of the Rectangular Pulse Spectrum
- 9.2.6. Fourier Transform of a Time-Domain Impulse
- 9.2.7. Fourier Transform of a Constant Signal
- 9.2.8. Fourier Transform of a Complex Exponential
- 9.2.9. Fourier Transform of a Cosine

**9.3. Fourier Transform Properties**

- 9.3.1. Linearity
- 9.3.2. Time Shifting
- 9.3.3. Magnitude and Phase Effects of Time Shifting
- 9.3.4. Time Scaling
- 9.3.5. Time Reversal
- 9.3.6. Frequency Shifting
- 9.3.7. Cosine Modulation
- 9.3.8. Time-Derivative Property
- 9.3.9. Solving Transform Problems Using Known Pairs

**9.4. Convolution and the Fourier Transform**

- 9.4.1. Convolution Theorem
- 9.4.2. Fourier Transform of a Convolution
- 9.4.3. Multiplication in the Frequency Domain
- 9.4.4. Time-Domain Convolution vs. Frequency-Domain Multiplication
- 9.4.5. Proof Idea of the Convolution Theorem
- 9.4.6. Using the Convolution Theorem to Avoid Direct Convolution

### 10. Frequency Response and Filtering 31 topics

**10.1. Sinusoids Through LTI Systems**

- 10.1.1. Complex Exponentials as LTI System Inputs
- 10.1.2. Deriving the Output for a Complex Exponential Input
- 10.1.3. Frequency Response $H(j\omega)$
- 10.1.4. Frequency Response as Fourier Transform of $h(t)$
- 10.1.5. Sinusoids as Eigenfunctions of LTI Systems
- 10.1.6. Same-Frequency Output Property
- 10.1.7. Amplitude Scaling by $|H(j\omega)|$
- 10.1.8. Phase Shifting by $\angle H(j\omega)$

**10.2. Interpreting Frequency Response**

- 10.2.1. Magnitude Response
- 10.2.2. Phase Response
- 10.2.3. Low-Frequency Behavior
- 10.2.4. High-Frequency Behavior
- 10.2.5. Low-Pass Behavior
- 10.2.6. High-Pass Behavior
- 10.2.7. Filter Interpretation from Magnitude Response

**10.3. RC Filters**

- 10.3.1. RC Low-Pass Circuit Model
- 10.3.2. Low-Pass Differential Equation
- 10.3.3. Low-Pass Frequency Response
- 10.3.4. Low-Pass Magnitude Response
- 10.3.5. RC High-Pass Circuit Model
- 10.3.6. High-Pass Differential Equation
- 10.3.7. High-Pass Frequency Response
- 10.3.8. High-Pass Magnitude Response
- 10.3.9. Comparing RC Low-Pass and High-Pass Filters
- 10.3.10. Effect of $RC$ on Filter Behavior

**10.4. Frequency-Domain LTI System Analysis**

- 10.4.1. Fourier Transform of an LTI System Output
- 10.4.2. Finding Output with $Y(j\omega)=X(j\omega)H(j\omega)$
- 10.4.3. Comparing Direct Convolution and Frequency-Domain Multiplication
- 10.4.4. Periodic Inputs Through an LTI System
- 10.4.5. Aperiodic Inputs Through an LTI System
- 10.4.6. Convolution and Frequency-Response Approaches

### 11. Laplace Transform Foundations 20 topics

**11.1. Motivation for the Laplace Transform**

- 11.1.1. Limitations of the Fourier Transform
- 11.1.2. Signals Whose Fourier Transform Does Not Converge
- 11.1.3. Exponential Weighting
- 11.1.4. The Complex Variable $s=\sigma+j\omega$
- 11.1.5. Laplace Transform as a Generalization of Fourier Transform
- 11.1.6. The $s$-Plane
- 11.1.7. Region of Convergence

**11.2. One-Sided Laplace Transform**

- 11.2.1. One-Sided Laplace Transform Definition
- 11.2.2. The $0^-$ Convention
- 11.2.3. Laplace Transform of $e^{-at}u(t)$
- 11.2.4. Laplace Transform of the Unit Step
- 11.2.5. Laplace Transform of the Unit Impulse
- 11.2.6. Laplace Transform of Shifted Impulses
- 11.2.7. Basic Inverse Laplace Transforms

**11.3. Algebra with Laplace Transforms**

- 11.3.1. Linearity of the Laplace Transform
- 11.3.2. Combining Simple Transform Pairs
- 11.3.3. Rational Functions in $s$
- 11.3.4. Partial-Fraction Setup for Inverse Transforms
- 11.3.5. Inverse Laplace Transform by Known Pairs
- 11.3.6. Interpreting Poles in Simple Transform Pairs

### 12. Laplace Transform Properties and Piecewise Signals 17 topics

**12.1. Time Shifting**

- 12.1.1. Time-Shifting Property of the Laplace Transform
- 12.1.2. Delayed Signals with Unit Steps
- 12.1.3. Transforming Shifted Unit Steps
- 12.1.4. Transforming Shifted Ramps
- 12.1.5. Rewriting Piecewise Signals with Unit Steps
- 12.1.6. Laplace Transforms of Piecewise Signals

**12.2. Derivative Properties**

- 12.2.1. First-Derivative Property
- 12.2.2. Initial Conditions in Laplace Transforms
- 12.2.3. Second-Derivative Property
- 12.2.4. Transforming Differential Equations
- 12.2.5. Impulses from Derivatives of Piecewise Signals
- 12.2.6. Using Derivatives to Transform Piecewise Linear Signals

**12.3. Laplace Transform Solution Methods**

- 12.3.1. Direct and Time-Shifting Laplace Methods
- 12.3.2. Step-Function and Derivative Methods
- 12.3.3. Solving for $X(s)$ from a Derivative
- 12.3.4. Reconstructing a Time-Domain Signal from $X(s)$
- 12.3.5. Checking Initial and Final Behavior from a Transform

### 13. Transfer Functions, Poles, and Stability 34 topics

**13.1. Transfer Functions**

- 13.1.1. Laplace Transform of Convolution
- 13.1.2. $Y(s)=X(s)H(s)$
- 13.1.3. Transfer Function $H(s)=Y(s)/X(s)$
- 13.1.4. Transfer Function vs. Impulse Response
- 13.1.5. Rational Transfer Functions
- 13.1.6. Numerator and Denominator Polynomials

**13.2. Poles and Zeros**

- 13.2.1. Zeros of a Transfer Function
- 13.2.2. Poles of a Transfer Function
- 13.2.3. Pole-Zero Plots
- 13.2.4. Real Poles
- 13.2.5. Complex-Conjugate Poles
- 13.2.6. Repeated Poles
- 13.2.7. Pole Locations in the $s$-Plane

**13.3. Stability of LTI Systems**

- 13.3.1. Causal LTI Systems
- 13.3.2. BIBO Stability from Pole Locations
- 13.3.3. Left-Half-Plane Poles
- 13.3.4. Right-Half-Plane Poles
- 13.3.5. Imaginary-Axis Poles
- 13.3.6. Decaying Exponential Responses
- 13.3.7. Growing Exponential Responses
- 13.3.8. Decaying Oscillatory Responses

**13.4. Transfer-Function Analysis of LTI Systems**

- 13.4.1. Finding Output with $Y(s)=X(s)H(s)$
- 13.4.2. Finding Step Response from a Transfer Function
- 13.4.3. Finding Impulse Response from a Transfer Function
- 13.4.4. Frequency-Response and Transfer-Function Methods
- 13.4.5. Connecting $H(s)$ and $H(j\omega)$
- 13.4.6. Interpreting System Behavior from Poles

**13.5. Circuit Transfer Functions**

- 13.5.1. Deriving Transfer Functions from Differential Equations
- 13.5.2. RC Transfer Functions in the $s$-Domain
- 13.5.3. RLC Circuit Differential Equation
- 13.5.4. RLC Circuit Transfer Function
- 13.5.5. Computing Poles of an RLC Circuit
- 13.5.6. Determining Stability from RLC Poles
- 13.5.7. Circuit Descriptions in Time, Frequency, and $s$ Domains
