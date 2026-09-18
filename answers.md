# CMPS 6610 Problem Set 02
## Answers

**Name:** Kailee Segarra


Place all written answers from `problemset-02.md` here for easier grading.

### 1. **Prove that $\log n! \in \Theta(n \log n).$**

We know that:

$$
\log(n!) = \log(1) + \log(2) + \cdots + \log(n)
$$

For the upper bound, each term is at most $\log(n)$, and there are $n$ terms. Therefore,

$$
\log(n!) \leq n\log(n)
$$

so:

$$
\log(n!) \in O(n\log n)
$$

For the lower bound, consider only the last half of the terms. There are approximately $n/2$ terms, and each of these terms is at least $\log(n/2)$. Therefore,

$$
\log(n!) \geq \frac{n}{2}\log\left(\frac{n}{2}\right)
$$

Since

$$
\frac{n}{2}\log\left(\frac{n}{2}\right) \in \Theta(n\log n),
$$

we have:

$$
\log(n!) \in \Omega(n\log n)
$$

Since $\log(n!)$ is both $O(n\log n)$ and $\Omega(n\log n)$,

$$
\boxed{\log(n!) \in \Theta(n\log n)}
$$


### 2. **Recurrences**

  ####  a. $T(n)=2T(n/6)+1$

Using the Master Theorem:

$$
a=2,\quad b=6,\quad f(n)=1
$$

and

$$
n^{\log_b a}=n^{\log_6 2}\approx n^{0.387}.
$$

Since $f(n)=\Theta(1)$ grows more slowly than $n^{0.387}$, this falls under Case 1 of the Master Theorem.

Therefore,

$$
\boxed{T(n)=\Theta(n^{\log_6 2})}
$$

  #### b. $T(n)=6T(n/4)+n$

Using the Master Theorem:

$$
a=6,\quad b=4,\quad f(n)=n
$$

We compare $f(n)$ to:

$$
n^{\log_b a}=n^{\log_4 6}\approx n^{1.292}
$$

Since $f(n)=n$ grows more slowly than $n^{1.292}$, this falls under Case 1 of the Master Theorem.

Therefore,

$$
\boxed{T(n)=\Theta(n^{\log_4 6})}
$$

  #### c. $T(n)=7T(n/7)+n$

Using the Master Theorem:

$$
a=7,\quad b=7,\quad f(n)=n
$$

We compare $f(n)$ to:

$$
n^{\log_b a}=n^{\log_7 7}=n
$$

Since $f(n)=\Theta(n)$ is the same order as $n^{\log_7 7}$, this falls under Case 2 of the Master Theorem.

Therefore,

$$
\boxed{T(n)=\Theta(n\log n)}
$$

  #### d. $T(n)=9T(n/4)+n^2$

Using the Master Theorem:

$$
a=9,\quad b=4,\quad f(n)=n^2
$$

We compare $f(n)$ to:

$$
n^{\log_b a}=n^{\log_4 9}\approx n^{1.585}
$$

Since $n^2$ grows polynomially faster than $n^{1.585}$, this falls under Case 3 of the Master Theorem.

Therefore,

$$
\boxed{T(n)=\Theta(n^2)}
$$

  #### e. $T(n)=4T(n/2)+n^3$

Using the Master Theorem:

$$
a=4,\quad b=2,\quad f(n)=n^3
$$

We compare $f(n)$ to:

$$
n^{\log_b a}=n^{\log_2 4}=n^2
$$

Since $n^3$ grows polynomially faster than $n^2$, this falls under Case 3 of the Master Theorem.

Therefore,

$$
\boxed{T(n)=\Theta(n^3)}
$$

  #### f. $T(n)=49T(n/25)+n^{3/2}\log n$

Using the Master Theorem:

$$
a=49,\quad b=25,\quad f(n)=n^{3/2}\log n
$$

We compare $f(n)$ to:

$$
n^{\log_b a}=n^{\log_{25}49}\approx n^{1.209}
$$

Since $n^{3/2}\log n$ grows polynomially faster than $n^{1.209}$, this falls under Case 3 of the Master Theorem.

Therefore,

$$
\boxed{T(n)=\Theta(n^{3/2}\log n)}
$$

  #### g. $T(n)=T(n-1)+2$

Expanding the recurrence:

$$
T(n)=T(n-1)+2
$$

$$
=T(n-2)+2+2
$$

$$
=T(n-3)+3(2)
$$

Continuing until the base case gives approximately $n$ recursive steps, each doing constant work.

Therefore,

$$
\boxed{T(n)=\Theta(n)}
$$

  #### h. $T(n)=T(n-1)+n^c$, with $c\geq1$

Expanding the recurrence gives:

$$
T(n)=T(n-1)+n^c
$$

$$
=T(n-2)+(n-1)^c+n^c
$$

Continuing to the base case gives:

$$
T(n)=T(1)+\sum_{k=2}^{n} k^c
$$

The sum of the first $n$ values raised to the power $c$ grows as:

$$
\Theta(n^{c+1})
$$

Therefore,

$$
\boxed{T(n)=\Theta(n^{c+1})}
$$

  #### i. $T(n)=T(\sqrt{n})+1$

At each recursive step, the input becomes the square root of the previous input:

$$
n,\quad n^{1/2},\quad n^{1/4},\quad n^{1/8},\ldots
$$

After $k$ recursive steps, the input size is:

$$
n^{1/2^k}
$$

The recursion stops when this reaches a constant size. This occurs after approximately:

$$
k=\Theta(\log\log n)
$$

levels.

Since each level performs constant additional work,

$$
\boxed{T(n)=\Theta(\log\log n)}
$$


### 3. **Algorithm Selection**

#### Algorithm A

Algorithm A creates two subproblems of size $n/5$ and combines the results in quadratic time.

The work recurrence is:

$$
W(n)=2W(n/5)+\Theta(n^2)
$$

Using the Master Theorem,

$$
n^{\log_5 2}\approx n^{0.431}
$$

Since $n^2$ grows faster than $n^{0.431}$,

$$
\boxed{W(n)=\Theta(n^2)}
$$

For the span, the two recursive calls can run in parallel, so only one recursive branch contributes to the span:

$$
S(n)=S(n/5)+\Theta(n^2)
$$

The quadratic combining work dominates, giving:

$$
\boxed{S(n)=\Theta(n^2)}
$$

#### Algorithm B

Algorithm B recursively solves one subproblem of size $n-1$ and combines the solution in logarithmic time.

The work recurrence is:

$$
W(n)=W(n-1)+\Theta(\log n)
$$

Expanding the recurrence gives:

$$
W(n)=\Theta\left(\sum_{k=1}^{n}\log k\right)
$$

Since

$$
\sum_{k=1}^{n}\log k=\log(n!)=\Theta(n\log n),
$$

the work is:

$$
\boxed{W(n)=\Theta(n\log n)}
$$

Since there is only one recursive subproblem, the span follows the same recurrence:

$$
S(n)=S(n-1)+\Theta(\log n)
$$

Therefore,

$$
\boxed{S(n)=\Theta(n\log n)}
$$

#### Algorithm C

Algorithm C creates subproblems of size $n/3$ and $2n/3$ and combines the solutions in $O(n^{1.1})$ time.

The work recurrence is:

$$
W(n)=W(n/3)+W(2n/3)+\Theta(n^{1.1})
$$

The recursive portions contribute roughly linear work across each level, while the $n^{1.1}$ combining term grows faster than linear. Therefore, the combining work dominates.

Thus,

$$
\boxed{W(n)=\Theta(n^{1.1})}
$$

For the span, the recursive subproblems can run in parallel. The larger branch has size $2n/3$, so:

$$
S(n)=S(2n/3)+\Theta(n^{1.1})
$$

The $n^{1.1}$ combining work dominates the geometric series, giving:

$$
\boxed{S(n)=\Theta(n^{1.1})}
$$

#### Which algorithm would I choose?

Based on asymptotic work and span, I would choose **Algorithm B**.

Its work and span are both:

$$
\Theta(n\log n)
$$

which grows more slowly asymptotically than Algorithm C's $\Theta(n^{1.1})$ and Algorithm A's $\Theta(n^2)$.


### 4. **More Algorithm Selection** 
#### Algorithm A

Algorithm A creates five subproblems of size $n/2$ and combines the solutions in linear time.

The work recurrence is:

$$
W(n)=5W(n/2)+\Theta(n)
$$

Using the Master Theorem,

$$
n^{\log_2 5}\approx n^{2.322}
$$

Since $n^{2.322}$ grows faster than the linear combining work,

$$
\boxed{W(n)=\Theta(n^{\log_2 5})\approx\Theta(n^{2.322})}
$$

For the span, the five recursive calls can run in parallel, so only one recursive branch contributes:

$$
S(n)=S(n/2)+\Theta(n)
$$

The work at each level forms a decreasing geometric series, so:

$$
\boxed{S(n)=\Theta(n)}
$$

#### Algorithm B

Algorithm B creates two subproblems of size $n-1$ and combines the solutions in constant time.

The work recurrence is:

$$
W(n)=2W(n-1)+\Theta(1)
$$

Each level doubles the number of recursive calls, resulting in exponential work:

$$
\boxed{W(n)=\Theta(2^n)}
$$

For the span, the two recursive calls can run in parallel, leaving only one recursive branch:

$$
S(n)=S(n-1)+\Theta(1)
$$

Therefore,

$$
\boxed{S(n)=\Theta(n)}
$$

#### Algorithm C

Algorithm C creates nine subproblems of size $n/3$ and combines the solutions in $\Theta(n^2)$ time.

The work recurrence is:

$$
W(n)=9W(n/3)+\Theta(n^2)
$$

Using the Master Theorem:

$$
n^{\log_3 9}=n^2
$$

Since the recursive work and combining work have the same asymptotic growth, this is Case 2 of the Master Theorem.

Therefore,

$$
\boxed{W(n)=\Theta(n^2\log n)}
$$

For the span, the nine recursive calls can run in parallel:

$$
S(n)=S(n/3)+\Theta(n^2)
$$

The quadratic combining work dominates the decreasing geometric series, giving:

$$
\boxed{S(n)=\Theta(n^2)}
$$

#### Which algorithm would I choose?

Algorithm B has exponential work, so it would generally be the least desirable option.

Between Algorithms A and C, there is a tradeoff. Algorithm C has less total work asymptotically, with $\Theta(n^2\log n)$ compared with Algorithm A's $\Theta(n^{2.322})$. However, Algorithm A has a much smaller span of $\Theta(n)$ compared with Algorithm C's $\Theta(n^2)$.

If total work is the main concern, I would choose Algorithm C. If a large amount of parallel processing is available and minimizing span is more important, Algorithm A could be preferable.

### 5. **Integer Multiplication Timing Results**

I implemented both the grade-school quadratic multiplication algorithm and the Karatsuba-Ofman subquadratic multiplication algorithm and measured their running times across a range of inputs.

| n | Quadratic (ms) | Subquadratic (ms) |
|---:|---:|---:|
| 10 | 0.027 | 0.019 |
| 100 | 0.034 | 0.036 |
| 1,000 | 0.079 | 0.098 |
| 10,000 | 0.091 | 0.108 |
| 100,000 | 0.091 | 0.141 |
| 1,000,000 | 0.181 | 0.181 |
| 10,000,000 | 0.221 | 0.194 |
| 100,000,000 | 0.336 | 0.306 |
| 1,000,000,000 | 0.381 | 0.424 |

In the timing table, \(n\) represents the integer value being multiplied. In the asymptotic analysis below, \(n\) represents the number of bits in the input. For an \(n\)-bit input, the grade-school multiplication algorithm has asymptotic work of:

$$
\Theta(n^2)
$$

while the Karatsuba-Ofman algorithm has asymptotic work of:

$$
\Theta(n^{\log_2 3}) \approx \Theta(n^{1.585})
$$

The measured running times were very close for these inputs. For several smaller inputs, the quadratic algorithm was slightly faster, which is reasonable because Karatsuba introduces additional arithmetic and recursive overhead that can outweigh its asymptotic advantage for small inputs. For some of the larger inputs, such as $10,000,000$ and $100,000,000$, the subquadratic algorithm was faster.

The results do not show a perfectly consistent advantage for Karatsuba at these input sizes, but they are consistent with the idea that its improved asymptotic complexity becomes more useful as the input size grows. Timing variation and recursive overhead have a noticeable effect for relatively small inputs.