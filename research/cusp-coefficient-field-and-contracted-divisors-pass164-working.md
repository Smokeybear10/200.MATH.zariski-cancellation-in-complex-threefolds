# Exact coefficient-field return and contracted cusp divisors

**Status: working algebraic restrictions on the actual quartic-graph branch.**

The actual quartic graph163 has coefficient field \(L=K(\rho)\),
where \(K=\ker_L\partial_\rho\) is finite over \(\mathbb C(\tau)\).
Moreover, away from the selected speed \(a=EX=0\), every prime
divisor of \(g=a/r\) maps to one of finitely many points under
the ratio map \((\tau,\rho)\). An explicit polynomial divisibility
proves this contraction, with no quotient-surface or ramification
theorem. Neither assertion supplies a global primitive slice or
a weight-four invariant correction.

## 1. Exact actual hypotheses

Retain the actual cusp hypotheses159 and quartic-graph assumptions163:
\[
\begin{gathered}
B=\mathbb C[X,Y,Z,W]=A[u],\quad E=\partial_u,\quad A=\ker E,\\
(\deg_E X,\deg_E Y,\deg_E Z,\deg_E W)=(1,1,2,2),
\quad \ker\theta_0=(\mathsf X\mathsf Z-\mathsf Y^3),\\
a=EX,\quad b=EY,\quad d=E^2W/2,\quad
N=[u^3]\partial_Z|_A,\quad S=\ker_A N,\quad L=\operatorname{Frac}S,\\
A_L=L[v],\quad Nv=1,\quad \tau=b/a,\quad\rho=d/a^2,
\quad L/\mathbb C(\tau,\rho)\text{ finite separable},\\
\deg_v y=1,\qquad \vartheta=P(y),\qquad P\in L[U],\quad\deg P=4.
\end{gathered}
\tag{1}
\]
Here \(a,b,d\in S\), \(a\ne0\), and the displayed ideal is the
full initial kernel. The coefficient partials are the commuting
extensions from \(\mathbb C(\tau,\rho)\). The actual projection gives
\[
\begin{gathered}
A_a=\mathbb C[y,z,w]_{a_0},\quad a=a_0(y,z,w),\quad
\operatorname{Frac}A=\mathbb C(y,z,w)=L(y),\\
\sigma=3\tau^2y+k,\quad k\in L,\quad
z=3\tau y^2+k_\tau y+r\vartheta+n,\quad r=k_\rho,\\
w=\{\ell-f(y,\vartheta)\}/r,\qquad
f(U,V)=U^3+H_2(k;U,V)+H_1(n;U,V).
\end{gathered}
\tag{2}
\]
In particular \(y,z,w,\sigma\in A_a\). The last field equality
uses that \(y\) is affine in \(v\), not just nonconstant.

Use constants \(c\in\mathbb C^*\), \(e\in\mathbb C\) for
the reciprocal formula163:
\[
\chi:=1/r=c\tau+e,\qquad
g:=cb+ea=a\chi\in S\setminus\{0\},\qquad \tau_0=-e/c.
\tag{3}
\]
No assertion that \(a\) or \(g\) is a unit of \(S\) is made.

## 2. The rho-constant subfield and actual field return

Put \(K=\ker_L\partial_\rho\). It contains \(\mathbb C(\tau)\)
and is preserved by \(\partial_\tau\). Every \(h\in K\) is
algebraic over \(\mathbb C(\tau)\): differentiate its monic
minimal polynomial over \(\mathbb C(\tau,\rho)\). Since
\(h_\rho=0\), the resulting relation has smaller degree,
so all differentiated coefficients vanish. They lie in
the constants \(\mathbb C(\tau)\) of the rational rho-field.

Also \(\rho\) is transcendental over \(K\). Otherwise
differentiating a monic relation of least positive degree,
using \(\partial_\rho\rho=1\), produces a nonzero relation
of smaller degree in characteristic zero. A finite set
linearly independent over \(\mathbb C(\tau)\) in \(K\)
therefore remains independent over \(\mathbb C(\tau,\rho)\):
clear rho-denominators and compare powers of \(\rho\).
Finiteness of \(L\) gives
\[
[K:\mathbb C(\tau)]<\infty,\qquad
[K:\mathbb C(\tau)]\le[L:\mathbb C(\tau,\rho)].
\tag{4}
\]
No rationality of \(K\) follows by assumption.

The full coefficient comparison163 proves \(k,n,\ell\in K[\rho]\)
and that every coefficient of \(P\) lies in \(K[\rho]\).
In particular its last coefficient has rho-degree at most one
by the \(U^3\) coefficient of the full determinant identity.
This uses the completed lower equations163, not only (3).
Both coefficient partials preserve \(K(\rho)\). Equations (2)
then put \(z,w\) in \(K(\rho)[y]\). Thus actual field return gives
\[
L(y)=\mathbb C(y,z,w)\subset K(\rho)(y)\subset L(y),
\qquad L=K(\rho),\qquad
[L:\mathbb C(\tau,\rho)]=[K:\mathbb C(\tau)].
\tag{5}
\]
For the middle equality intersect with \(L\). Since \(y\)
is transcendental over \(L\), one has
\(L\cap K(\rho)(y)=K(\rho)\): cross multiplication and
coefficient comparison express any element of that intersection
as a ratio of two coefficients in \(K(\rho)\). Adjoining the
independent transcendental \(\rho\) to a basis in (4) gives
the degree equality. This does not identify integral rings.

## 3. A regular rho-constant element and its specialization

The early actual chart already makes \(k\) regular:
\[
k=\sigma-3\tau^2y\in A_a\cap L=S_a,\qquad
\eta:=\rho-\chi k\in S_a,\qquad \eta_\rho=0.
\tag{6}
\]
Indeed write an element of \(A_a\cap L\) as \(f/a^j\),
\(f\in A\). Since \(Na=0\) and \(N\) kills \(L\),
one gets \(Nf=0\), hence \(f\in S\). No finite generation
or smoothness of \(S\) is used. For the final derivative,
\(\chi_\rho=0\) and \(k_\rho=1/\chi\), so
\(\eta_\rho=1-\chi k_\rho=0\). Equivalently
\(\eta=-\chi k_0\in K\), where \(k=r\rho+k_0\).

By Section 2, \(\eta\) is algebraic over \(\mathbb C(\tau)\).
Choose a nonzero \(Q(T,V)\in\mathbb C[T,V]\) satisfying
\(Q(\tau,\eta)=0\). Divide out the largest common power
of \(T-\tau_0\) in its coefficients as a polynomial in \(V\).
This preserves vanishing, since \(\tau-\tau_0\ne0\) in \(L\),
and ensures
\[
Q(\tau,\eta)=0,\qquad
q_0(V):=Q(\tau_0,V)\in\mathbb C[V]\setminus\{0\},
\qquad q_0(\rho)\in gS_a.
\tag{7}
\]
For the last assertion, \(\tau-\tau_0=g/(ca)\) and
\(\rho-\eta=(g/a)k\) belong to \(gS_a\). Polynomial
substitution gives
\(Q(\tau_0,\rho)-Q(\tau,\eta)\in gS_a\).
Regularity of \(k\) in (6) is essential. The specialization
claim (7) needs only the algebraicity argument of Section 2,
not the stronger field equality (5).

## 4. The finite contracted image and the omitted a-zero locus

If \(q_0\) is a nonzero constant, (7) makes \(g\) a unit
in \(S_a\), so there are no primes in that open containing it.
Otherwise factor over \(\mathbb C\):
\[
q_0(V)=C\prod_{j=1}^m(V-\rho_j)^{e_j},\qquad
C\in\mathbb C^*,\quad e_j\ge1,\quad
\rho_j\in\mathbb C\text{ distinct}.
\tag{8}
\]
For any prime ideal \(\mathfrak p\subset S\) with
\(g\in\mathfrak p\) and \(a\notin\mathfrak p\),
equation (7) in the prime quotient forces precisely one
factor \(\rho-\rho_j\) to vanish. Consequently
\[
\overline\tau=\tau_0,\qquad \overline\rho=\rho_j
\quad\text{in }\operatorname{Frac}(S/\mathfrak p),
\qquad d-\rho_j a^2\in\mathfrak p.
\tag{9}
\]
The ratios are defined because \(a\notin\mathfrak p\).
The same finite list of complex numbers works for every prime.
Thus the ratio map on \(V(g)\cap\operatorname{Spec}S_a\)
has finite image contained in the points \((\tau_0,\rho_j)\).
This applies to all primes in the locus, not only its divisors.

For divisor notation, \(S\) is a UFD without needing a
quotient-surface theorem. Factoriality descends from \(A[u]\)
to \(A\): factors of an element of \(A\) in \(A[u]\)
have u-degree zero. The kernel \(S\) is factorially closed
in \(A\), since the \(N\)-degree of a product is the sum
of the two degrees in characteristic zero. Factorization in
\(A\) therefore gives factorization into primes in \(S\).
In particular, for a prime element \(\pi\mid g\) with
\(\pi\nmid a\), (9) means \(\pi\mid d-\rho_j a^2\)
in \(S\). No global coordinate property of \(\pi\) is assumed.

There is also a localized divisibility before taking supports:
\[
\prod_{j=1}^m(d-\rho_j a^2)^{e_j}\in gS_a,
\qquad
a^M\prod_{j=1}^m(d-\rho_j a^2)^{e_j}\in gS
\quad\text{for some }M\ge0.
\tag{10}
\]
Multiply (7) by \(a^{2\deg q_0}/C\) for the first assertion;
the second is the definition of localization. No bound on
\(M\) or the multiplicities is asserted.

At a prime containing \(a\), the ratios need not be regular
and this proof does not apply. It gives no contraction statement
there. The divisor of \(g\) can also have no component outside
\(a=0\), making the off-a assertion vacuous.

## 5. Actual compatibility and remaining scope

The actual quartic example163 has \(a=1\), \(b=t\),
\(d=tq\), \(\tau=t\), \(\rho=tq\), \(k=q\),
and \(r=1/t\). Thus \(g=t\), \(\eta=0\), and one
can take \(Q(T,V)=V\). Its divisor \(t=0\) maps to
\((\tau,\rho)=(0,0)\), exactly as (9) requires.
Its primitive selected quotient is nevertheless sliced.
Contracted ratio divisors alone do not obstruct recognition
or imply a nontrivial primitive plinth.

The field identity (5) and specialization (7) are constraints
from the actual chart. They do not construct a weight-four
invariant, prove a generic coordinate polynomial, remove the
\(a=0\) locus, or supply a global primitive slice.
Those additional conclusions are not assumed.

## Retained sources and verification scope

1. [Actual cusp chart159](cusp-generic-chart-first-reductions-pass159-working.md),
   for the exact field, early coefficient return, projected-ring
   equality, and nonzero selected LND.
2. [Quartic graph coefficient rigidity163](cusp-quartic-graph-coefficient-rigidity-pass163-working.md),
   for the affine reciprocal and all coefficients in \(K[\rho]\),
   including the last graph coefficient.
3. [Actual quartic graph boundary163](cusp-actual-quartic-graph-boundary-pass163-working.md),
   for the actual check in Section 5.

No external surface classification or ramification theorem is
used in the new argument. These are retained working inputs,
not a recursive audit of all preceding results. No novelty
clearance, human expert review, proof-assistant certification
or full cancellation theorem is claimed. No163 or earlier
artifact is changed.
