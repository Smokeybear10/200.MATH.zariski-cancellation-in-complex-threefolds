# Extra factors in the cusp chart force a simple projected coordinate

**Status: working selected-factor reduction, not global recognition.**

In the nonzero-\(k_\rho\) branch of the actual cusp chart159,
a nonconstant extra factor in its plane relation can occur only
when the first projected coordinate \(y\) is constant on the
generic intrinsic line, or is an affine linear parameter for it.
In the second case the selected curve is a quadratic graph in
the fixed displayed axes.

This is a one-way restriction. It neither constructs an extra
factor in an actual frame nor proves that every resulting
generic parameter descends to an integral slice or coordinate.

## 1. Exact inherited chart and the selected kernel

Retain all actual-frame hypotheses and constructions of the
[first cusp-chart reductions159](cusp-generic-chart-first-reductions-pass159-working.md).[^1]
In particular \(L\) is the exact coefficient field, finite
separable over \(\mathbb C(\tau,\rho)\), the partials commute,
and \(L[y,\vartheta]=L[v]\). Work in the branch \(r=k_\rho\ne0\).
For independent formal variables \(U,V\), the relevant data are
\[
\begin{gathered}
f=U^3+H_2(k;U,V)+H_1(n;U,V),\qquad A_1=f_V,\\
\Phi=A_1\frac{\ell-f}{r}+H_3(k;U,V)+H_2(n;U,V)
 -\ell_\tau U-\ell_\rho V,\\
\Phi(y,\vartheta)=m\in L,\qquad
0\ne\Phi-m\in L[U,V],\qquad \deg\Phi\le4,\\
\ker\{L[U,V]\longrightarrow L[v],\ (U,V)\longmapsto(y,\vartheta)\}=(G),\\
\Phi_4=-\frac{U^3(r_\tau U+r_\rho V)}r .
\end{gathered}
\tag{1}
\]
Here \(k,n,\ell\in L\), and
\(H_j(c;U,V)=\sum_{i=0}^j
c_{\tau^i\rho^{j-i}}U^iV^{j-i}/(i!(j-i)!)\).
The polynomial \(G\) is irreducible and nonconstant, defined
up to \(L^*\). The subscript four denotes the homogeneous
degree-four part, which may vanish.

The actual constant determinant in the cited chart expresses
a nonzero element of \(L\) as an \(L[v]\)-linear combination
of \(\Phi_U(y,\vartheta)\) and \(\Phi_V(y,\vartheta)\).
Thus these two evaluated derivatives generate the unit ideal
in \(L[v]\). This input is stronger than the sole relation
\(\Phi(y,\vartheta)=m\).

## 2. Unit restriction identifies the exact possible remainder

Factor \(\Phi-m=GH\) in \(L[U,V]\).
On the selected curve both gradient entries have the factor
\(H(y,\vartheta)\). The unit-gradient property therefore
forces \(H(y,\vartheta)=c\) for some \(c\in L^*\).
It follows from the full evaluation kernel in (1) that
\[
H=c+GK,\qquad
\Phi-m=cG+G^2K,\qquad c\in L^*,\quad K\in L[U,V].
\tag{2}
\]
In particular the selected factor is simple.
The cofactor \(H\) is nonconstant if and only if \(K\ne0\).
If \(K=0\), the whole relation is already associated to \(G\).

Suppose henceforth that \(K\ne0\), and set \(\delta=\deg G\).
The term \(G^2K\) has larger total degree than \(cG\).
Since the top homogeneous product cannot vanish in the domain
\(L[U,V]\),
\(\deg(\Phi-m)=2\delta+\deg K\le4\).
Thus \(\delta\) is one or two. No claim about a factor of
degree three or four needs a plane-embedding classification.

## 3. A quadratic selected factor makes y an affine parameter

If \(\delta=2\), degree forces \(K=d_0\in L^*\) and
\(\deg\Phi=4\). Consequently
\[
d_0G_2^2=-\frac{U^3(r_\tau U+r_\rho V)}r,\qquad
r_\rho=0,\quad r_\tau\ne0,\qquad
G=a_2U^2+a_1U+b_1V+a_0,
\quad a_2,b_1\in L^* .
\tag{3}
\]
To justify the coefficients, if \(r_\rho\ne0\), the two
linear factors on the right are distinct and have odd
multiplicities three and one. This is impossible for a scalar
times a square in the UFD \(L[U,V]\).
The right side is nonzero, so \(r_\tau\ne0\) once
\(r_\rho=0\). Unique factorization then makes \(G_2\)
a nonzero scalar times \(U^2\). No square root of a
coefficient is adjoined to \(L\).

The remaining assertion \(b_1\ne0\) uses the exact whole-line
quotient. If \(b_1=0\), the equation \(G(y,\vartheta)=0\)
makes \(y\in L[v]\) algebraic over \(L\), hence \(y\in L\).
Then \(U-y\) belongs to the kernel \((G)\), which is impossible
since its degree is one and \(\deg G=2\).

Equation (3) now makes \(\vartheta\) a quadratic polynomial
in \(y\) over \(L\). Therefore
\(L[v]=L[y,\vartheta]=L[y]\).
Expressing \(v\) as a polynomial in \(y\) and comparing
degrees in \(v\) proves that \(y=\alpha v+\beta\), with
\(\alpha\in L^*\), \(\beta\in L\).
Thus the graph assertion and affine parameter are over the
original coefficient field, not just its algebraic closure.

## 4. A linear selected factor makes y constant

Let \(\delta=1\). By (2), the square of the leading linear
form \(G_1\) divides the highest homogeneous part of
\(\Phi-m\). There are three possible positive degrees,
two, three and four. All must be treated because (1) does
not assert that \(\Phi_4\ne0\).

If \(\deg\Phi=4\), (1) gives
\[
G_1^2\mid U^3(r_\tau U+r_\rho V).
\tag{4}
\]
When the second linear factor is not proportional to \(U\),
its multiplicity is only one. When it is proportional to
\(U\), there is only the factor \(U\).
In either case a squared linear factor in (4) must be
proportional to \(U^2\). Hence \(G_1\sim U\).

If the quartic part vanishes, (1) first gives
\(r_\tau=r_\rho=0\). Commuting coefficient partials then
give \(k_{\tau\rho}=k_{\rho\rho}=0\) and all their higher
derivatives. Thus \(A_1=n_\rho\), and the cubic part is
\[
\Phi_3=\left(\frac{k_{\tau\tau\tau}}6-
                   \frac{n_\rho}{r}\right)U^3.
\tag{5}
\]
If \(\deg\Phi=3\), the scalar here is nonzero, so
\(G_1^2\mid U^3\) again implies \(G_1\sim U\).

Finally suppose \(\deg\Phi=2\).
Equation (5) gives \(n_\rho=rk_{\tau\tau\tau}/6\).
Differentiating with respect to \(\rho\), using
\(r_\rho=0\) and
\(k_{\tau\tau\tau\rho}=r_{\tau\tau\tau}=0\), gives
\(n_{\rho\rho}=0\).
The exact degree-two part of (1) is consequently
\[
\Phi_2=
\left(\frac{n_{\tau\tau}}2-
      \frac{n_\rho k_{\tau\tau}}{2r}\right)U^2
 +n_{\tau\rho}UV .
\tag{6}
\]
It is nonzero in this case. By (2), \(K\) is a nonzero
constant, so (6) must be a nonzero scalar times \(G_1^2\).
If \(n_{\tau\rho}\ne0\), its two linear factors are
distinct, each of multiplicity one, which is impossible.
Thus it is a nonzero scalar times \(U^2\), and once again
\(G_1\sim U\).

Degree one cannot occur when \(K\ne0\), by the degree
formula in Section 2. This exhausts the degree drops.
Since \(G\) itself is linear and its leading part is
proportional to \(U\), it has the form \(a_1U+a_0\),
with \(a_1\ne0\). Evaluation gives \(y=-a_0/a_1\in L\).

## 5. Exact conclusion and remaining gap

For the actual chart in Section 1, a nonconstant cofactor
in \(\Phi-m=GH\) therefore has only the alternatives
\[
\begin{cases}
\deg G=1,\quad y\in L;\\
\deg G=2,\quad y=\alpha v+\beta\ (\alpha\in L^*),\quad
G=a_2U^2+a_1U+b_1V+a_0\ (a_2b_1\ne0),\quad
\Phi-m=cG+d_0G^2.
\end{cases}
\tag{7}
\]
If \(y\) is neither constant nor an affine linear parameter,
then \(K=0\) in (2): the whole relation is associated to
the selected irreducible kernel and has degree at most four.
None of these implications is a converse asserting that an
extra factor actually exists.

This proof uses only polynomial degrees, exact coefficient
derivatives, the whole-line quotient, and the actual selected
unit-gradient identity. It does not import a plane-coordinate
classification or change the original coordinates by
coefficient-dependent transformations.

Even in the irreducible branch, the result concerns a generic
curve over \(L\). It does not lift its defining equation to
an invariant of source weight at most three in \(B\), remove
divisorial denominators, or recognize every cusp frame.
Arbitrary coordinate entry and unrestricted cancellation
remain outside this note.

## Sources and verification scope

1. [First actual cusp-chart reductions159](cusp-generic-chart-first-reductions-pass159-working.md),
   Sections 1--5, especially its exact whole-line presentation
   and constant-determinant identity. All actual-frame and
   selected-field hypotheses are retained, not replaced by
   a formal gradient ansatz.

The elementary factor and degree arguments are supplied here.
No finite checker is used as a proof of a universal conclusion,
and no historical novelty, human expert review, recursive
source audit or proof-assistant certification is claimed.
No earlier artifact is edited.

[^1]: Source 1.
