# The rank-two repair has an exact local normal form

This note isolates what remains when the global Heisenberg repair
does not produce a second independent direction on the original
kernel. It does not recognize that kernel or assert an actual
high-degree realization of the residual.

## 1. Setup

Use the notation of
[the global repair proof](quadratic-heisenberg-repair-pass43.md).
On \(B'=B_g\) there are actual LNDs \(\delta,L,C\) with
\[
[\delta,L]=C,\qquad [\delta,C]=[L,C]=0,
\qquad \delta\sigma=1,\quad C\sigma=0,\quad C\ne0.
\tag{1}
\]
Assume their fraction-field rank is two. Define
\[
A'=\ker\delta,\qquad S=\ker\delta\cap\ker C,
\qquad b=L\sigma,\qquad D_0=L-\sigma C-b\delta.
\tag{2}
\]
The preceding proof establishes that \(b\in S\), that \(D_0\)
is an actual LND, and that it commutes with \(\delta,C\) and
kills \(\sigma\). The field \(C|_{A'}\) is nonzero: otherwise
\(B'=A'[\sigma]\) would give \(C=0\).

Since \(\delta,C\) are independent and all three fields have
rank two, \(L\) belongs to their fraction-field span. Therefore
\[
L|_S=0.
\tag{3}
\]
In particular the common invariant ring of all three fields is
exactly \(S\). This conclusion uses the rank assumption, not
only their commutation relations.

## 2. An exact simultaneous normal form

Choose a local slice \(z\in A'\) of \(C|_{A'}\), and write
\[
\chi=Cz\in S\setminus\{0\}.
\]
The original rings are complex algebras, so the local-slice
theorem applies. Equation (3) also gives \(L\chi=0\).
After this one invariant localization,
\[
A'_\chi=S_\chi[z],\qquad
B'_\chi=S_\chi[z,\sigma].
\tag{4}
\]
Set \(h=Lz-\chi\sigma\). The brackets give
\[
\delta h=[\delta,L]z-\chi=Cz-\chi=0,
\qquad Ch=LCz=L\chi=0.
\]
Thus \(h\in S\), before localizing at \(\chi\). In the actual
relative coordinates of (4),
\[
\delta=\partial_\sigma,\qquad
C=\chi\partial_z,\qquad
L=b\partial_\sigma+(\chi\sigma+h)\partial_z,
\qquad b,h\in S.
\tag{5}
\]
All three fields kill \(S_\chi\). Consequently the quotient repair is
exactly
\[
D_0=h\partial_z=\frac h\chi C.
\tag{6}
\]
There is no remaining local triangularization issue after (4).
The coefficient \(h/\chi\) need not belong to \(S\), and (4)
does not assert that \(S\) is a polynomial plane. Nor does it
produce a global coordinate of the original four-ring.

## 3. Changing the compatible slice cannot add a direction

Every other \(\sigma'\in B'\) satisfying
\(\delta\sigma'=1\) and \(C\sigma'=0\) is of the form
\(\sigma'=\sigma+q\), with \(q\in S\). By (3),
\(L\sigma'=L\sigma=b\), and the corresponding repair satisfies
\[
D'_0=D_0-qC.
\tag{7}
\]
Thus every such repair has the same at-most-one-dimensional
direction on \(A'\). Selecting a different compatible slice
cannot evade the rank-two condition.

There is also an exact cancellation criterion for this repair:
some compatible slice in \(B'\) makes \(D'_0=0\) if and only if
\[
h\in\chi S.
\tag{8}
\]
Indeed (6)--(7) require \(q=h/\chi\). After passing to
\(B'_\chi\), that choice is always allowed, so the projected
repair can always be made zero there. This statement concerns
the repair field, not the original nonzero action \(E\).

For the concrete top-coordinate choices
\(\tau_j=(E^{m-1}x)_j/c_j\) with \(c_j\ne0\),
the corresponding slices are \(\sigma_j=\tau_j/g^{m-1}\).
Their differences belong to \(S\). Since \(Lg=0\), equation
(3) gives \(Y(\tau_i-\tau_j)=0\). The original polynomial
replicas therefore obey the exact global identity
\[
\mathcal R_i-\mathcal R_j
=-a(\tau_i-\tau_j)V,
\qquad a=(m-1)/2.
\tag{9}
\]
Changing the nonzero component of the highest constant direction
does not create a second quotient action.

## Scope and verification

This is a direct algebraic consequence of the already audited
Heisenberg relations and the standard local-slice theorem used
there. It adds no unittest suite or method count. It does not
assume finite generation or polynomiality of \(S\), transfer
the original slice to the central action, or infer global descent
from (4). The remaining task is a genuine global restriction on
the rank-two common base or an independent ambient coordinate
construction. No such restriction is proved here.
