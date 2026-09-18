# An intrinsic additive action fixing every good-coordinate speed

## 1. Statement and what is new here

Suppose \(n\ge2\) and
\[
 \begin{gathered}
 B=\mathbb C[x_1,\ldots,x_{n-1},z],\qquad
 E\in\operatorname{LND}_{\mathbb C}(B),\qquad E(u)=1,\\
 A=\ker E,\qquad B=A[u],\qquad
 E^2(x_i)=0,\qquad a_i=E(x_i)\quad(1\le i<n).
 \end{gathered}
 \tag{1}
\]
If at least one \(a_i\) is nonzero, there is a nonzero
\(N\in\operatorname{LND}_{\mathbb C}(A)\) such that \(N(a_i)=0\)
for every \(i\). No bound on the \(E\)-degree of \(z\), no hypothesis
on the algebraic rank of the speeds, and no unit-ideal assumption on
their row is needed.

If \(z\) has positive \(E\)-degree, \(N\) also kills its leading
coefficient in \(u\). In particular, in the one-quadratic-coordinate
case the acceleration \(q=E^2z\) belongs to the same invariant ring.

For \(n=4\), the retained intrinsic quotient-surface theorem then places
all three speeds in the same actual subring
\(S=\ker N\simeq\mathbb C^{[2]}\), and \(S\subset A\) is faithfully flat.
This supplies a common intrinsic quotient containing the specified speeds,
not just an unrelated intrinsic additive action.

Existence of intrinsic actions and the general leading-derivation mechanism
were already proved in
[the intrinsic-action note](intrinsic-actions-pass.md), especially
Sections 2 and 5. The additional observation here is that the leading
part of the actual partial \(\partial_z\) annihilates every coefficient
\(a_i\) of the supplied \(E\)-affine companions. The construction and
all actual-ring degeneration steps are given below. No historical
novelty claim is made.

The [independent volume proof](three-good-speed-rank-bound-pass125.md)
remains a separate route to the algebraic-rank consequence. Its
independent-speed assumption is unnecessary for the present construction.

## 2. The last-coordinate partial must move the invariant ring

Set \(b_i=x_i-a_i u\), so \(a_i,b_i\in A\) and
\(x_i=b_i+a_i u\). Let \(T=\partial_z\) be the actual polynomial
coordinate partial. It is a nonzero LND of \(B\) and \(T(x_i)=0\).

If \(T(A)=0\), then the identities \(T(x_i)=a_i T(u)=0\), together
with some \(a_i\ne0\) and the domain property, force \(T(u)=0\).
As \(A,u\) generate \(B\), this would make \(T=0\), a contradiction.
Therefore \(T(A)\ne0\).

The algebra \(A\simeq B/(u)\) is finitely generated. Choose a finite
set of algebra generators for \(A\). The images under \(T\) of those
generators are polynomials in \(u\) with coefficients in \(A\).
The derivation rule therefore gives a uniform finite upper bound for
the \(u\)-degree of \(T(f)\) for every \(f\in A\): products of elements
of \(A\) do not increase that bound. Give the zero polynomial degree
\(-\infty\), and define
\[
 \begin{gathered}
 k=\max_{f\text{ in the chosen generators}}\deg_u T(f)\ge0,\qquad
 d=\max\{k,\deg_u T(u)-1\}\ge0,\\
 T(f)=\sum_{j=0}^{d}D_j(f)u^j\quad(f\in A),\qquad
 T(u)=\sum_{j=0}^{d+1}h_j u^j,\quad h_j\in A.
 \end{gathered}
 \tag{2}
\]
Each coefficient map \(D_j:A\to A\) is a complex derivation, by
coefficient comparison in the Leibniz identity on two elements of
\(A\). The integer \(d\) is the exact degree shift of \(T\) for the
\(u\)-degree filtration. At least one of \(D_d\) and \(h_{d+1}\)
is nonzero, by its definition. No coordinates for \(A\) have been chosen.

## 3. A nonzero locally nilpotent leading part on the actual ring

Adjoin an indeterminate \(\varepsilon\), extend \(T\) to kill it,
and work temporarily in \(B[\varepsilon,\varepsilon^{-1}]\).
Let \(\Phi\) fix \(A,\varepsilon\) and send \(u\) to \(u/\varepsilon\).
Define
\[
 \begin{gathered}
 T_\varepsilon=\varepsilon^d\Phi T\Phi^{-1},\\
 T_\varepsilon(f)=
   \sum_{j=0}^{d}D_j(f)u^j\varepsilon^{d-j}\quad(f\in A),\\
 T_\varepsilon(u)=
   \sum_{j=0}^{d+1}h_j u^j\varepsilon^{d+1-j},\qquad
 T_\varepsilon(\varepsilon)=0.
 \end{gathered}
 \tag{3}
\]
The Laurent-ring derivation is locally nilpotent: it is an actual
conjugate of \(T\), multiplied by an invariant unit. All displayed
exponents are nonnegative, so it preserves \(B[\varepsilon]\).
The restriction is locally nilpotent since that polynomial subring
injects into the Laurent ring. The ideal \((\varepsilon)\) is stable,
so specialization gives a nonzero LND \(H\) of the original domain
\(B=A[u]\), with
\[
 H(f)=u^dD_d(f)\quad(f\in A),\qquad
 H(u)=h_{d+1}u^{d+1}.
 \tag{4}
\]
It is nonzero because at least one of the two leading terms in (2)
is nonzero.

For an LND on a characteristic-zero domain, \(f\mid D(f)\) forces
\(D(f)=0\). Indeed the largest nonzero iterate defines an additive
degree on nonzero products, whereas a nonzero derivative decreases
that degree by one. Since \(d\ge0\), \(u\) divides \(H(u)\), so
\(H(u)=0\) and \(h_{d+1}=0\).
It follows that \(D_d\ne0\). Put \(N=D_d\).

Now \(H(f)=u^dN(f)\) and \(H(u)=0\) imply
\(H^r(f)=u^{dr}N^r(f)\) for every \(f\in A\) and \(r\ge0\).
Local nilpotence of \(H\), together with the domain property,
proves that \(N\) is locally nilpotent on \(A\).
It is nonzero by the preceding paragraph.

This argument includes \(d=0\). It does not divide an arbitrary
polynomial vector field and declare the quotient locally nilpotent.
The coefficient derivation \(N\) is known to be locally nilpotent
because its iterates occur in those of the actual specialized LND \(H\).

## 4. The leading identity annihilates all the speeds

The preceding argument also shows \(\deg_u T(u)\le d\).
Apply \(T\) to each original companion:
\[
 0=T(x_i)=T(b_i)+uT(a_i)+a_iT(u).
 \quad\text{The coefficient of }u^{d+1}\text{ is }N(a_i),
 \qquad N(a_i)=0.
 \tag{5}
\]
Both \(T(b_i)\) and \(a_iT(u)\) have degree at most \(d\).
Thus no term other than the displayed top coefficient of \(uT(a_i)\)
can contribute. This proves the assertion for every speed, including
any zero entries.

There was no choice of rational speed parameters and no nonconical
determinant condition. In particular the construction does not split
into separate cases according to a determinant
\(\det(a_s,a_t,a)\).

There is a further leading-coefficient consequence from the other exact
coordinate identity \(T(z)=1\). If
\[
 z=\sum_{j=0}^{\ell}c_j u^j,\qquad
 c_j\in A,\qquad c_\ell\ne0,\qquad \ell\ge1,
 \quad\text{then}\quad N(c_\ell)=0.
 \tag{6}
\]
Indeed \(T(z)=\sum_jT(c_j)u^j+
\sum_j j c_j u^{j-1}T(u)\). The second sum has degree at most
\(d+\ell-1\), and the coefficient of \(u^{d+\ell}\) in the first
sum is exactly \(N(c_\ell)\). Since \(d+\ell>0\), that coefficient
vanishes in \(T(z)=1\). If \(\ell=2\), this gives
\(q=E^2z=2c_2\in\ker N\). The restriction \(\ell\ge1\) is deliberate:
when \(\ell=d=0\), the same comparison would instead give \(N(z)=1\).

For fixed \(E\) and the actual partial \(T\), changing the slice from
\(u\) to \(u+\alpha\), \(\alpha\in A\), does not change the intrinsic
coefficient \(N\) on \(A\). The filtration is unchanged, and a
translation of \(u\) does not alter the highest coefficient of \(T(f)\).
Equivalently \(N(f)=E^d(T(f))/d!\) for \(f\in A\).
The extension of \(N\) to \(B\) that kills the chosen slice can change;
no independence from the supplied ambient frame or from the chosen
coordinate partial is asserted.

## 5. Algebraic-rank consequence in every dimension

A nonzero LND on the finitely generated domain \(A\) has invariant
field of transcendence degree one less than \(\operatorname{Frac}A\).
Here is the needed elementary argument. Choose \(r\in A\) with
\(N(r)=p\ne0\), \(N^2(r)=0\); such an \(r\) is a suitable iterate of
any element moved by \(N\). Then \(p\in\ker N\).
After inverting this invariant, \(r/p\) is a slice for \(N\).
The finite Taylor expansion in that slice gives
\(A_p=(\ker N)_p[r/p]\). Taking fraction fields yields
\[
 \operatorname{Frac}A
   =\operatorname{Frac}(\ker N)(r/p),\qquad
 \operatorname{trdeg}_{\mathbb C}\operatorname{Frac}(\ker N)=n-2,
 \qquad
 \operatorname{trdeg}_{\mathbb C}\mathbb C[a_1,\ldots,a_{n-1}]
       \le n-2.
 \tag{7}
\]
The slice variable is transcendental over the invariant field, since
its derivative is \(1\). The local Taylor argument does not require
global finite generation of \(\ker N\) in arbitrary dimension.

If all speeds are zero, the asserted dependence is immediate and
there is a direct recognition instead: \(E=E(z)\partial_z\), and
the original slice equation gives \(E(z)\partial_z u=1\).
Thus \(E(z)\in B^*=\mathbb C^*\), and
\(A=\mathbb C[x_1,\ldots,x_{n-1}]\).
This case was deliberately excluded from the nonzero-\(N\) construction.

## 6. The actual affine-plane quotient in dimension four

Now take \(n=4\) and at least one nonzero speed. Apply the retained
[intrinsic quotient-surface theorem](intrinsic-quotient-surface-pass.md)
to the actual threefold algebra \(A\) and the nonzero intrinsic LND
\(N\) just constructed. It gives
\[
 S=\ker N\simeq\mathbb C^{[2]},\qquad
 a_1,a_2,a_3\in S,\qquad
 S\longrightarrow A\text{ is faithfully flat},
 \tag{8}
\]
and the quotient morphism has nonempty purely one-dimensional fibers.
For the one-quadratic-coordinate profile, the acceleration \(q\) lies
in this same \(S\), by (6), without being assumed constant.

The applicability is important. The supplied cylinder
\(\operatorname{Spec}A\times\mathbb A^1\simeq\mathbb A^4\)
makes \(\operatorname{Spec}A\) smooth and contractible.
Projection of the cylinder onto this threefold is smooth of rank three;
its restriction to a suitable affine linear three-plane is dominant.
Thus the threefold is dominated by
\(\mathbb A^3=\mathbb A^1\times\mathbb A^2\).
The retained theorem applies Kaliman--Saveliev's
Lemma 2.1, Theorem 2.7 and Corollary 2.8 with precisely these hypotheses.
Those results identify the quotient as the affine plane and give
nonempty curve fibers. Their pure dimension and smooth total space
then give flatness by miracle flatness, as proved in the retained note.

This invokes that source-dependent retained theorem. It does not
derive an affine-plane kernel from the rank bound alone, nor apply
a theorem about derivations of a polynomial three-ring to the unknown
\(A\). The entire retained quotient proof, including its nonreduced and
disconnected fiber control and its source scope, was read through EOF
for this application; no new full audit of the cited primary proofs
is claimed here.

Nothing in (8) says that the selected speed row generates the unit
ideal of \(S\), that \(N\) is free, that its quotient is a globally
trivial affine-line bundle, or that \(A=S[v]\).
The retained theorem recognizes \(A\) if the intrinsic action is free,
but this construction does not prove that further premise.
Likewise \(S\) being polynomial does not make its generators ambient
coordinates of \(B\).

## 7. Dependency and remaining scope

The preexisting general leading-LND mechanism, rather than a new
classification theorem, produces \(N\). The specific annihilation
identity (5) places all of the actual good speeds in its kernel.
The dimension-four affine-plane and faithful-flat conclusions inherit
the precise source dependencies and confidence limits of the retained
quotient-surface theorem.

This covers supplied three-good-coordinate frames even with variable
acceleration and without any time-degree bound on the fourth coordinate.
It does not give such a frame for an arbitrary sliced derivation.
It supplies neither universal entry nor recognition of every action
in the supplied class, so unrestricted cancellation remains unsolved.

No file through pass124, the independent volume-rank proof125, or a live
index is changed by this note. This is a written AI research deduction,
not human expert review, formal verification, or a historical novelty claim.
