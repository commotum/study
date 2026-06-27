
## The Dataset

**names.txt**  
A list of English first/given names, written in lowercase, with one name per line. Each line/name becomes a single training sequence. The default file contains no spaces or padding. Below is a 9 name sample from the dataset.

```
eli
elizabeth
ella
emily
emma
emmett
ethan
evan
evelyn
...
```

## Data Preparation

#### Vocabulary 

We will be building a character-level transformer model. So each unique character in `names.txt` becomes a token. Additionally, we will add *Beginning of Sequence* and *End of Sequence* tokens to act as delimiters. Then our vocab $\mathcal{V}$ is defined as:

$$\mathcal{V}=\{\text { all unique characters in the dataset }\} \cup\{\texttt{<BOS>}, \texttt{<EOS>} \}$$

For the default `names.txt` dataset used by the code, the characters are the lowercase English letters:

$$
\mathcal{A}=\{a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, u, v, w, x, y, z\}
$$

So our final vocabulary becomes:

$$\mathcal{V}=\{\mathcal{A}, \texttt{<BOS>}, \texttt{<EOS>} \}$$

#### Supervised Training Pairs

From each name in `names.txt` we will prepare several supervised learning pairs. 

The first step is converting each name into a finite-length discrete-time token signal. For example, the name `emma` becomes:

$$  
\left[  
\begin{array}{c}  
\texttt{<BOS>} \\  
\texttt{e} \\  
\texttt{m} \\  
\texttt{m} \\  
\texttt{a} \\  
\texttt{<EOS>}  
\end{array}  
\right]  
$$

We define this tokenized name as a discrete-time signal $s[n]$:  
  
$$  
s[n] =  
\begin{cases}  
\texttt{<BOS>}, & n = 0 \\  
\texttt{e}, & n = 1 \\  
\texttt{m}, & n = 2 \\  
\texttt{m}, & n = 3 \\  
\texttt{a}, & n = 4 \\  
\texttt{<EOS>}, & n = 5  
\end{cases}  
$$

The model is trained to predict the next token from the tokens that came before it. In other words, the target signal is a one-sample advance of the token signal:  
  
$$  
y[n] = s[n+1]  
$$  
  
Equivalently, for each time index $n$, the model receives the causal prefix:
  
$$  
\mathbf{x}_n =  
\begin{bmatrix}  
s[0] \\  
s[1] \\  
\vdots \\  
s[n]  
\end{bmatrix}  
$$
and learns to predict  
  
$$  
y_n = s[n+1]  
$$  
So the supervised training pairs are  
  
$$  
\left(\mathbf{x}_n, y_n\right)  
=  
\left(  
\begin{bmatrix}  
s[0] \\  
s[1] \\  
\vdots \\  
s[n]  
\end{bmatrix},  
s[n+1]  
\right)  
$$

For `emma`, this produces the following input-target pairs:  

$$  
\begin{array}{ccl}
\mathbf{x}_n & & y_n \\[0.5em]

\begin{bmatrix}  
\texttt{<BOS>}  
\end{bmatrix}  
& \rightarrow &  
\texttt{e}  
\\[1em]  
  
\begin{bmatrix}  
\texttt{<BOS>} \\  
\texttt{e}  
\end{bmatrix}  
& \rightarrow &  
\texttt{m}  
\\[1em]  
  
\begin{bmatrix}  
\texttt{<BOS>} \\  
\texttt{e} \\  
\texttt{m}  
\end{bmatrix}  
& \rightarrow &  
\texttt{m}  
\\[1em]  
  
\begin{bmatrix}  
\texttt{<BOS>} \\  
\texttt{e} \\  
\texttt{m} \\  
\texttt{m}  
\end{bmatrix}  
& \rightarrow &  
\texttt{a}  
\\[1em]  
  
\begin{bmatrix}  
\texttt{<BOS>} \\  
\texttt{e} \\  
\texttt{m} \\  
\texttt{m} \\  
\texttt{a}  
\end{bmatrix}  
& \rightarrow &  
\texttt{<EOS>}  
\end{array}  
$$
  
Thus, preparing the targets is equivalent to shifting the token sequence one sample to the left: every input prefix is paired with the next token in the sequence.

## The Representation

A fundamental problem that makes language modeling and other learning problems difficult is the curse of dimensionality. It is particularly obvious in the case when one wants to model the joint distribution between many discrete random variables, such as words in a sentence or discrete attributes in a data-mining task.

For example, if one wants to model the joint distribution of 10 consecutive words in a natural language with a vocabulary $V$ of size 100,000, there are potentially $100000^{10}-1=10^{50}-1$ free parameters.

Rather than directly modeling every possible sequence with a separate parameter, neural language models learn a continuous representation of each token. This lets the model represent tokens in a shared vector space and learn patterns between them through the geometry of that space.

The token signal $s[n]$ is a discrete-time sequence, but each sample is still a symbol:

$$
s[n] \in \mathcal{V}
$$

For example, a sample might be

$$
s[n] = \texttt{e}
$$

or

$$
s[n] = \texttt{<BOS>}
$$

A neural network cannot directly operate on symbolic values, so each token is converted into a learned vector representation called an **embedding**. We define an embedding map

$$
E\{\cdot\} : \mathcal{V} \rightarrow \mathbb{R}^{D}
$$

where $D$ is the embedding dimension. For each time index $n$, the symbolic token $s[n]$ is mapped to a vector:

$$
\mathbf{e}[n] = E\{s[n]\}
$$

Thus, the original symbolic signal

$$
s[n] \in \mathcal{V}
$$

is transformed into a vector-valued discrete-time signal

$$
\mathbf{e}[n] \in \mathbb{R}^{D}
$$

The purpose of this representation is to let the model learn continuous features for each token. Instead of treating each character as an unrelated symbol, the model learns a vector for each token that can be adjusted during training to improve next-token prediction.

At this stage, $\mathbf{e}[n]$ represents the identity of the token at time $n$, but it does not yet explicitly encode the token's position in the sequence. It also does not yet describe the dependence between samples of the sequence. The next stage of the model uses attention to form a context-dependent representation of each sample based on the samples that came before it.

## The Attention Mechanism

The previous section transformed the symbolic token signal $s[n]$ into the vector-valued embedding signal

$$
\mathbf{e}[n] \in \mathbb{R}^{D}
$$

However, $\mathbf{e}[n]$ only represents the token at time $n$. It does not yet describe how that token relates to the other tokens in the causal sequence, nor does it contain any positional information.

The attention mechanism forms a new context-dependent representation by allowing each time index $n$ to compare itself with the current and previous time indices:

$$
0 \leq m \leq n
$$

To do this it is passed through a multilayer neural network. To describe repeated layers, let

$$
\mathbf{e}^{(\ell)}[n] \in \mathbb{R}^{D}
$$

denote the vector entering the attention mechanism at layer $\ell$ and time index $n$. For the first layer,

$$
\mathbf{e}^{(0)}[n] = \mathbf{e}[n]
$$

---

#### 1. RMSNorm

Before computing attention, the model normalizes the vector entering the attention mechanism.

We define the RMSNorm operator as

$$
\operatorname{RMSNorm}\{\cdot\} : \mathbb{R}^{D} \rightarrow \mathbb{R}^{D}
$$

For a vector

$$
\mathbf{a}
=
\begin{bmatrix}
a_1 \\
a_2 \\
\vdots \\
a_D
\end{bmatrix}
$$

RMSNorm is

$$
\operatorname{RMSNorm}\{\mathbf{a}\}
=
\frac{\mathbf{a}}
{
\sqrt{
\frac{1}{D}
\sum_{i=1}^{D} a_i^2
+
\epsilon
}
}
$$

where $\epsilon$ is a small constant used for numerical stability and to avoid division by zero errors.

The normalized vector is

$$
\bar{\mathbf{e}}^{(\ell)}[n]
=
\operatorname{RMSNorm}\{\mathbf{e}^{(\ell)}[n]\}
$$

---

#### 2. Learned Query, Key, and Value Operators

The model then applies three learned linear operators:

$$
Q^{(\ell)}\{\cdot\} : \mathbb{R}^{D} \rightarrow \mathbb{R}^{D}
$$

$$
K^{(\ell)}\{\cdot\} : \mathbb{R}^{D} \rightarrow \mathbb{R}^{D}
$$

$$
V^{(\ell)}\{\cdot\} : \mathbb{R}^{D} \rightarrow \mathbb{R}^{D}
$$

These operators produce the query, key, and value vectors:

$$
\mathbf{q}^{(\ell)}[n]
=
Q^{(\ell)}\{\bar{\mathbf{e}}^{(\ell)}[n]\}
$$

$$
\mathbf{k}^{(\ell)}[n]
=
K^{(\ell)}\{\bar{\mathbf{e}}^{(\ell)}[n]\}
$$

$$
\mathbf{v}^{(\ell)}[n]
=
V^{(\ell)}\{\bar{\mathbf{e}}^{(\ell)}[n]\}
$$

The query vector represents what the model is looking for at time $n$. The key vectors represent what information is available at each time index. The value vectors contain the information that will be combined to form the attention output.

---

#### 3. Rotary Position Encoding

The query, key, and value vectors contain token information, but the attention mechanism also needs position information.

To do this, we apply a rotary position encoding to the query and key vectors.

We define the RoPE operator as

$$
\operatorname{RoPE}_{n}\{\cdot\} : \mathbb{R}^{D} \rightarrow \mathbb{R}^{D}
$$

where the subscript $n$ indicates that the rotation depends on the time index.

The rotated query and key vectors are

$$
\hat{\mathbf{q}}^{(\ell)}[n]
=
\operatorname{RoPE}_{n}
\{
\mathbf{q}^{(\ell)}[n]
\}
$$

$$
\hat{\mathbf{k}}^{(\ell)}[m]
=
\operatorname{RoPE}_{m}
\{
\mathbf{k}^{(\ell)}[m]
\}
$$

The value vector is not rotated.

RoPE works by rotating pairs of coordinates in the query and key vectors. Since each vector is in $\mathbb{R}^{D}$, we form $D/2$ coordinate pairs. For pair index

$$
i \in \left\{0,1,\ldots,\frac{D}{2}-1\right\}
$$

the angular frequency is

$$
\omega_i = \frac{1}{10000^{2i/D}}
$$

and the position-dependent rotation angle is

$$
\theta_i[n] = n\omega_i
$$

or equivalently,

$$
\theta_i[n] = \frac{n}{10000^{2i/D}}
$$

For each coordinate pair, RoPE applies a two-dimensional rotation. If

$$
\begin{bmatrix}
a_i \\
b_i
\end{bmatrix}
$$

is one coordinate pair, then

$$
\begin{bmatrix}
a_i' \\
b_i'
\end{bmatrix}
=
\begin{bmatrix}
\cos(\theta_i[n]) & \sin(\theta_i[n]) \\
-\sin(\theta_i[n]) & \cos(\theta_i[n])
\end{bmatrix}
\begin{bmatrix}
a_i \\
b_i
\end{bmatrix}
$$

This rotation is applied separately to each coordinate pair. Therefore, the full operator $\operatorname{RoPE}_{n}\{\cdot\}$ applies a collection of rotations, each with a different frequency $\omega_i$.

This introduces position information directly into the query-key comparison. Since the query at time $n$ and the key at time $m$ are rotated by different angles, their dot product depends not only on token content, but also on their relative positions in the sequence.

---

#### 4. RMSNorm on the Rotated Query and Key Vectors

After RoPE is applied, the rotated query and key vectors are normalized:

$$
\tilde{\mathbf{q}}^{(\ell)}[n]
=
\operatorname{RMSNorm}
\{
\hat{\mathbf{q}}^{(\ell)}[n]
\}
$$

$$
\tilde{\mathbf{k}}^{(\ell)}[n]
=
\operatorname{RMSNorm}
\{
\hat{\mathbf{k}}^{(\ell)}[n]
\}
$$

These normalized, position-aware vectors are used to compute attention scores.

---

#### 5. Causal Attention Scores

For a causal language model, the output at time $n$ may only depend on the current and previous time indices.

For each

$$
0 \leq m \leq n
$$

the raw attention score is

$$
r^{(\ell)}[n,m]
=
\frac{
\left(
\tilde{\mathbf{q}}^{(\ell)}[n]
\right)^T
\tilde{\mathbf{k}}^{(\ell)}[m]
}
{
\sqrt{D}
}
$$

This score measures how strongly the vector at time $n$ should attend to the vector at time $m$.

---

#### 6. Softmax

The raw scores are converted into normalized attention weights using Softmax:

$$
\operatorname{Softmax}\{\cdot\} : \mathbb{R}^{n+1} \rightarrow \mathbb{R}^{n+1}
$$

For each

$$
0 \leq m \leq n
$$

the attention weight is

$$
\alpha^{(\ell)}[n,m]
=
\frac{
\exp(r^{(\ell)}[n,m])
}
{
\sum_{j=0}^{n}
\exp(r^{(\ell)}[n,j])
}
$$

The weights satisfy

$$
\sum_{m=0}^{n}
\alpha^{(\ell)}[n,m]
=
1
$$

so the attention output is a weighted combination of previous value vectors.

---

#### 7. Weighted Sum of Value Vectors

The attention output before the final projection is

$$
\mathbf{z}^{(\ell)}[n]
=
\sum_{m=0}^{n}
\alpha^{(\ell)}[n,m]
\tilde{\mathbf{v}}^{(\ell)}[m]
$$

From a signals perspective, this resembles a causal, data-dependent filtering operation. The output at time $n$ is a weighted sum of previous value vectors, but the weights are computed from the sequence itself rather than fixed ahead of time.

---

#### 8. Output Projection

The weighted sum is then passed through a learned output projection:

$$
O^{(\ell)}\{\cdot\} : \mathbb{R}^{D} \rightarrow \mathbb{R}^{D}
$$

giving

$$
\mathbf{o}^{(\ell)}[n]
=
O^{(\ell)}
\{
\mathbf{z}^{(\ell)}[n]
\}
$$

---

#### 9. Residual Update

Finally, the projected attention output is added back to the vector that entered the attention mechanism:

$$
\mathbf{e}^{(\ell+1)}[n]
=
\mathbf{e}^{(\ell)}[n]
+
\mathbf{o}^{(\ell)}[n]
$$

The result $\mathbf{e}^{(\ell+1)}[n]$ is the context-dependent representation passed to the next stage of the model.

## Next Section



