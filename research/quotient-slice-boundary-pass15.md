# Invariant coefficients: the quotient-slice condition and its gap

Reduction modulo an invariant coefficient gives a genuine quotient
slice, not just a fixed-point-free quotient action. The coefficient
inverse does descend to the common invariant ring in the polynomial
three-variable setting. The remaining issue is lifting that quotient
slice, or showing that an original slice can be chosen affine in the
added variable. Neither implication is proved here in full generality.

## 1. The exact necessary quotient condition

Let \(R=\mathbb C^{[3]}\), \(0\ne D\in\operatorname{LND}(R)\),
\(C=\ker D\), and \(A,\beta\in C\). On \(R[t]\), put
\[
E=AD+\beta\partial_t.
\]
The interesting residue case has \(\beta\ne0\) noninvertible and
\(A\ne0\). If \(\beta\) is a nonzero constant, \(t/\beta\)
is already a slice. If \(\beta=0\), a slice forces \(A\) to be
a unit and \(D\) to have a slice, by evaluation at \(t=0\).

Suppose \(E(s)=1\), and write \(s=\sum_{j=0}^n r_jt^j\).
The constant coefficient of this equation is
\[
AD(r_0)+\beta r_1=1,
\tag{1}
\]
with \(r_1=0\) if \(n=0\). Set
\(S=R/\beta R\), and let \(\overline D\) denote its induced
LND. Reduction of (1) gives
\[
\overline A\,\overline D(\overline r_0)=1.
\tag{2}
\]
Consequently \(\overline A\in S^*\), and
\[
\overline D(\overline A\,\overline r_0)=1.
\tag{3}
\]
Thus \(\overline D\) itself has a slice. This argument is valid
with nilpotents in \(S\); it does not identify \(\ker\overline D\)
with \(C/\beta C\).

In the present polynomial-threefold setting \(C\to R\) is faithfully
flat, as verified from the precise quotient-fiber theorem in
[the commuting-quotient note, Section 6](commuting-quotient-pass15.md).
Its base change \(C/\beta C\to S\) is faithfully flat. Therefore
\(\overline A\) being a unit in \(S\) implies it is a unit in
\(C/\beta C\): the quotient by \(\overline A\) vanishes after a
faithfully flat extension only if it already vanishes. In particular
\[
\boxed{(A,\beta)C=C,\qquad
\overline D\text{ has a slice on }R/\beta R.}
\tag{4}
\]
The inverse of the original invariant coefficient is not the obstacle
to descent here. Without faithful flatness, the purely algebraic
argument through (3) still holds, but the unit assertion in the
smaller quotient ring needs a separate reason.

An immediate weaker consequence is
\((I_D,\beta)R=R\), where \(I_D=(D(R))R\): \(\beta\) is a
unit on the fixed scheme of \(D\). The quotient-slice assertion
in (4) is strictly more informative than that fixed-scheme test.

## 2. The exact affine-slice criterion

Let \(P_D=D(R)\cap C\) be the plinth ideal. Then
\[
E\text{ has a slice affine in }t
\quad\Longleftrightarrow\quad A P_D+\beta C=C.
\tag{5}
\]
Indeed, for \(s=r+ht\), the coefficient of \(t\) in \(E(s)=1\)
forces \(Dh=0\), and its constant coefficient gives
\(ADr+\beta h=1\). Applying \(D\) makes \(D^2r=0\), so
\(Dr\in P_D\). Conversely, if \(1=Ap+\beta h\), with
\(p=Dr\in P_D\), the same formula \(r+ht\) is a slice.

Under the necessary condition \((A,\beta)=C\), equation (5) is
equivalent to
\[
P_D+\beta C=C.
\tag{6}
\]
Thus proving that every invariant-coefficient slice in this setting
is affine in \(t\) is exactly the proposed strengthening from an
arbitrary slice to (6). This note does not prove that strengthening.

## 3. What reduction loses: an exact module comparison

Regard \(D:R\to R\) as a \(C\)-linear map, and put
\(M=R/D(R)\). No finite generation of \(M\) is assumed. The
snake lemma applied to multiplication by the invariant \(\beta\)
gives
\[
0\longrightarrow C/\beta C
\longrightarrow\ker\overline D
\longrightarrow M[\beta]\longrightarrow0,
\tag{7}
\]
where \(M[\beta]=\{m:\beta m=0\}\). Explicitly, an invariant
class \(\overline r\), with \(Dr=\beta h\), maps to the class
of \(h\) in \(M\). This also verifies exactness directly.
Moreover,
\[
\operatorname{coker}\overline D=M/\beta M.
\]
The quotient-slice condition is therefore precisely
\[
[1]\in\beta M.
\tag{8}
\]
By contrast, (6) requires a witness from the image of \(C\) in
\(M\): \([1]=\beta[c]\) for some \(c\in C\).
Equation (1) gives \([1]=\beta[r_1]\), where \(r_1\) need
not be invariant. The other coefficient equations
\[
ADr_j+(j+1)\beta r_{j+1}=0\quad(1\le j<n),
\qquad Dr_n=0
\tag{9}
\]
constrain this witness, but no argument is supplied that replaces
it by an invariant witness. Ignoring this difference would assume
the affine-slice conclusion.

For a concrete strict inclusion in (7), take
\[
D=x\partial_y+2y\partial_z,
\qquad C=\mathbb C[x,v],\qquad v=xz-y^2,
\qquad\beta=x.
\]
Then \(\overline D=2y\partial_z\) on \(\mathbb C[y,z]\),
whose kernel is \(\mathbb C[y]\). The included ring
\(C/xC=\mathbb C[v]\) maps by \(v\mapsto-y^2\), and is
strictly smaller. Plinth or invariant formation cannot be assumed
to commute with this quotient.

## 4. Free quotient actions are not enough, even on the original base

For the same \(D\), let \(A=1\) and \(\beta=v-1\).
Then \(E=D+(v-1)\partial_t\) is fixed-point-free:
\[
1=zE(y)-\frac y2E(z)-E(t).
\]
Nevertheless it has no slice. On
\[
S=\mathbb C[x,y,z]/(xz-y^2-1),
\]
the induced \(\overline D\) has kernel \(\mathbb C[x]\).
To see this, invert \(x\), where
\(S_x=\mathbb C[x,x^{-1},y]\) and
\(\overline D=x\partial_y\). A Laurent polynomial in \(x\)
with a genuine negative power cannot belong to \(S\), since
\(S/(x)\ne0\). This identifies the kernel.

If \(\overline D\) had a slice \(r\), the slice theorem would
give \(S=\mathbb C[x,r]\), whose quotient by \(x\) is a domain.
But
\[
S/(x)=\mathbb C[y,z]/(y^2+1)
\cong\mathbb C[z]\times\mathbb C[z].
\]
This contradiction violates (4), so the original \(E\) has no slice.
It shows why the fixed-scheme unit test alone cannot replace the
quotient-slice condition. It does not show that (4) is insufficient
on a polynomial three-variable base.

## 5. A localized control prevents an abstract lifting argument

Localize that base at the invariant \(v\), writing \(R'=R_v\)
and \(C'=\mathbb C[x,v,v^{-1}]\), and now choose \(\beta=x\).
Modulo \(x\), one has
\[
R'/xR'=\mathbb C[y,y^{-1},z],
\qquad \overline D(z/(2y))=1.
\]
Thus \(\overline D\) has a slice and \((A,\beta)=C'\) for
\(A=1\). However \(D\) has no slice on \(R'\). The original
plinth ideal is \((x)\), as established in
[the commuting-quotient note, Section 7](commuting-quotient-pass15.md),
and invariant localization gives the proper plinth ideal \((x)C'\).

The extension \(E=D+x\partial_t\) has no slice either: the
coordinate change \(\tau=t-y\) gives \(E(\tau)=0\), so a
slice on \(R'[\tau]\), evaluated at \(\tau=0\), would give
a slice for \(D\) on \(R'\).

This is a counterexample to residue-to-global lifting for a smooth
localized base, not for the required unlocalized \(\mathbb A^3\).
It shows that a proof of sufficiency of (4) in the requested setting
must use a genuinely global polynomial-base property. The quotient
slice, faithful flatness, and the coefficient unit alone do not give
an abstract lifting theorem.

## 6. Plinth unimodularity does not imply scalar congruence

Even (6) does not by itself produce a local-slice value \(g\)
such that \(\beta\) is a nonzero scalar modulo \(g\). This
failure already occurs on an actual polynomial three-variable base:
\[
R=\mathbb C[u,v,w],\quad
D=(uv-1)\partial_w,\quad C=\mathbb C[u,v],\quad\beta=u.
\]
Here \(P_D=(uv-1)\), \(P_D+(u)=C\), and
\[
s=-w+vt,\qquad (D+u\partial_t)(s)=1.
\]
Every nonzero local-slice value is divisible by \(uv-1\), whereas
\(u\) is nonconstant modulo that factor. Thus no such value can
divide \(u-c\) for a scalar \(c\). The slice is still a coordinate:
\[
h=uw-(uv-1)t,
\qquad t=us+h,\quad w=(uv-1)s+vh
\]
is the two-sided completion. The matrix on \((w,t)\) has determinant
\(-1\), a unit, so the sign presents no obstruction.

Accordingly, neither the necessary implication from an arbitrary
slice to (6), nor a general reduction from (6) to the earlier scalar
congruence hypothesis, is established by this residue argument.
The first remains unresolved here; the second fails in the stated
all-base generality. No rank-three-specific counterexample to the
first implication is supplied.

Nine independent inline exact checks with `/opt/anaconda3/bin/python`
passed in 0.100 seconds. They verify the invariant equations, the
fixed-point-free negative control, its split quotient fiber, the
enlarged quotient invariant, the localized quotient slice and invariant
coordinate, and the comaximal-plinth example's slice, invariant,
determinant \(-1\), and two-sided inverse. They do not test all
invariant coefficients or settle the general lifting implication.
