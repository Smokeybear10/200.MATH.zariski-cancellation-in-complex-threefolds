# Exact slice criteria for the recognized conic-velocity family

The conic family considered below admits complete polynomial coordinates.
In those coordinates, the original nice action is a translation and
the LND derived from its good partial is a two-direction translation
with coefficients in one invariant variable. This gives exact criteria
for a common slice, a global slice for the second action, and primitive
division after fixing any supplied slice.

This classifies these questions inside one explicit parameter family.
It does not classify arbitrary nice sliced four-variable actions or
prove an unrestricted cancellation theorem. The special pairs
\((u,v)=(1,a)\) and \((a,a^2+1)\) were already retained;
the new bounded step is the parameter-independent criterion with
all constant and zero-component boundaries included.

## 1. The parameter family and actual polynomial inverse

Let \(R=\mathbb C[a]\), and choose \(u,v\in R\) with
\((u,v)=R\). Either component may be zero, but not both.
In the actual ring \(B=\mathbb C[x,y,z,w]\), substitute
\(a=xz-y^2+w\) and define
\[
P=(u^2,uv,v^2,-v^2x+2uvy-u^2z)^t,
\qquad E=P\cdot\partial,\qquad T=\partial_w,
\qquad Q=[T,E].
\tag{1}
\]
Primes below denote ordinary derivatives in the indeterminate
\(a\). Directly \(Ea=0\), and \((uv)^2=u^2v^2\) gives
\(EP=0\). Thus \(E\) is nice: its actual flow is
\(x_{\rm vec}+tP\), with inverse \(x_{\rm vec}-tP\).

Choose any \(r,s\in R\) satisfying \(ru+sv=1\). Put
\[
L=\begin{pmatrix}v&-u\\r&s\end{pmatrix},\qquad
L^{-1}=\begin{pmatrix}s&u\\-r&v\end{pmatrix}.
\tag{2}
\]
The following are actual polynomial coordinates:
\[
\begin{aligned}
U&=v^2x-2uvy+u^2z,\\
V&=vrx+(vs-ur)y-usz,\\
S&=r^2x+2rsy+s^2z,
\end{aligned}
\qquad (a,U,V,S).
\tag{3}
\]
Their inverse, now with \((a,U,V,S)\) independent, is
\[
\begin{aligned}
x&=s^2U+2suV+u^2S,\\
y&=-srU+(sv-ru)V+uvS,\\
z&=r^2U-2rvV+v^2S,\\
w&=a-US+V^2.
\end{aligned}
\tag{4}
\]
For complete verification, replacing \(w\) by \(a-xz+y^2\)
first identifies \(B\) with \(R[x,y,z]\). If
\(M=\left(\begin{smallmatrix}x&y\\y&z\end{smallmatrix}\right)\),
the first three expressions in (3) are the entries of \(LML^t\).
Multiplying by \(L^{-1}\) and its transpose gives the first
three inverse expressions in (4). Determinants give
\(US-V^2=xz-y^2\), which verifies the last expression and
recovers \(a\) in both orders. This proves global polynomial
inverses, not a conclusion from a unit Jacobian alone.

Since \(L(u,v)^t=(0,1)^t\), the original derivation becomes
\[
Ea=EU=EV=0,\qquad ES=1,\qquad
E=\partial_S,\qquad \ker E=R[U,V].
\tag{5}
\]
The coprimality premise is also necessary for an \(E\)-slice
within the family (1). If \(u,v\) share a nonconstant factor
\(h(a)\), all four coefficients of \(E\) are divisible by
\(h(a)^2\), so \(1\notin E(B)\). Hence the sliced members
of this full conic family are exactly the coprime pairs.

## 2. The derived action and its constant boundary

Define
\[
W=vu'-uv',\qquad \beta=2(ru'+sv').
\tag{6}
\]
The actual derivative in (1) has first three coefficients
\(((u^2)',(uv)',(v^2)')\) and fourth coefficient
\(-(v^2)'x+2(uv)'y-(u^2)'z\). In particular \(Qa=0\).
Thus in applying \(Q\) to (3), its coefficients in \(R\)
are fixed. The matrix calculation
\[
L\binom{u'}{v'}=\binom{W}{\beta/2}
\]
and differentiation of \((u,v)^t(u,v)\) give exactly
\[
Qa=QU=0,\qquad QV=W,\qquad QS=\beta,
\qquad Q=W\partial_V+\beta\partial_S.
\tag{7}
\]
Consequently \(Q\) is a polynomial LND commuting with \(E\).
Both statements concern the actual original ring, by (3)--(4).
Also \(Q(P)=0\): its first three components lie in \(R\)
and its fourth component is \(-U\).

If \(W=0\), the rational function \(u/v\), when defined,
has zero derivative, so it is constant. Coprimality then forces
both \(u,v\) to be constant. If one component is identically
zero, coprimality makes the other a nonzero constant and gives
the same conclusion. Conversely constant \(u,v\) yield
\(W=\beta=0\), hence \(Q=0\). In this boundary \(E\)
is an affine sliced action; every \(E\)-slice is \(Q\)-invariant,
and the zero derivation \(Q\) has no slice or nonzero primitive
adjustment.

For the rest of the note suppose that the pair is nonconstant.
Then \(W\ne0\), and \(E,Q\) are generically independent.
Equations (4) and (7) give
\[
Q^2(x,y,z,w)=(0,0,0,2W^2),\qquad
Q^3(x,y,z,w)=0.
\tag{8}
\]
Thus the derived action is never nice in the original frame in
this nonconstant branch, although it is nice in (3).

## 3. Global slice and primitive criteria for the second action

Let \(d\) be a greatest common divisor of \(u',v'\) in
\(R\), normalized to be monic. At least one derivative is
nonzero in the current branch. Since (2) is invertible over
\(R\), and two is a unit, one has the exact ideal identity
\[
(W,\beta)R=(u',v')R=dR.
\tag{9}
\]
In the actual polynomial coordinates (3), the coefficient ideal
of \(Q\) is therefore \(dB\). The following are equivalent:
\(Q\) is primitive, \(Q\) has no fixed point, \(Q\) has
a polynomial slice, and \(d=1\). Here primitiveness means
that the coefficients have no common nonunit factor, up to units.
These equivalences are specific to the present one-variable
coefficient ring and are not general equivalences for LNDs.

Indeed, if \(d\ne1\), all values of \(Q\) lie in the
proper ideal \(dB\), so it has no slice. A complex root of
\(d\) supplies a nonempty entire fiber on which \(Q\) vanishes.
If \(d=1\), the PID \(R\) supplies \(c_1,c_2\in R\)
with \(c_1W+c_2\beta=1\). Then
\(Q(c_1V+c_2S)=1\), which also prevents fixed points.
Primitiveness and the coefficient ideal statement follow directly
from (9). Polynomial coordinate changes preserve the ideal
generated by the values of a derivation, so this argument also
checks original-frame primitiveness.

## 4. Exact common-slice criterion for the unchanged pair

Every polynomial \(E\)-slice is \(S+h(a,U,V)\).
By (7), it is killed by this fixed \(Q\) precisely when
\[
\beta+W h_V=0.
\tag{10}
\]
Since \(R[U,V]\) is a polynomial extension of \(R\), this
is possible exactly when \(W\mid\beta\) in \(R\).
For example, evaluating \(h_V\) at \(U=V=0\) gives
necessity within \(R\); sufficiency is explicit. All such
slices are
\[
S-\frac{\beta}{W}V+k(a,U),\qquad k\in R[U].
\tag{11}
\]
This retains every multiplicity of \(W\); vanishing on its
reduced zero set is not substituted for divisibility.

There is a parameter-only reformulation:
\[
\begin{aligned}
&\text{some \(E\)-slice is killed by \(Q\)}\\
&\quad\Longleftrightarrow W\mid\beta
\Longleftrightarrow W\mid u'\text{ and }W\mid v'\\
&\quad\Longleftrightarrow
\operatorname{span}_{\mathbb C}\{u,v\}\cap\mathbb C^*
\ne\varnothing.
\end{aligned}
\tag{12}
\]
The middle equivalence follows from the inverse of (2).
Here is a complete degree proof of the last equivalence. A
constant invertible linear change of the pair preserves its
derivative ideal and multiplies \(W\) by a nonzero constant.
Choose such a change so that the two nonzero components have
degrees \(m>n\). This is done by canceling their leading
coefficients if their degrees initially agree. A resulting zero
component would make the original pair linearly dependent;
coprimality would then make both original components constant,
which is excluded. If \(n\ge1\), the transformed Wronskian
has degree \(m+n-1>m-1\), while the derivative of the
degree-\(m\) component is nonzero and has degree \(m-1\).
It cannot divide that derivative. Thus divisibility forces
\(n=0\), giving a nonzero constant linear combination of
\(u,v\). Conversely, if one transformed component is a
nonzero constant, the Wronskian is a nonzero constant times
the derivative of the other component, which proves the
divisibility claim. All degrees in this argument are ordinary
polynomial degrees in the one variable \(a\).

Whenever the criterion holds, a common slice can even be chosen
linear in the original frame. If \(\alpha u+\gamma v=c\ne0\)
with complex constants, then
\[
F_{\rm lin}=\frac{\alpha^2x+2\alpha\gamma y+\gamma^2z}{c^2}
\]
has \(EF_{\rm lin}=1\) and \(QF_{\rm lin}=0\), by (1)
and its derivative in \(a\). At least one coefficient is
nonzero, so this is an actual linear coordinate, not just a
degree-one element in an auxiliary ring.

If \(Q\) also has a global slice, (9) sharpens (12):
a common \(E\)-slice exists exactly when \(W\) is a
nonzero constant. Equivalently both \(u,v\) have degree at
most one and their coefficient vectors are not proportional.
To see the last statement, the same reduced-degree calculation
gives \(m+n-1=0\), hence \(m=1,n=0\).
The pair \((a,a^2+1)\) has \(d=1\) and nonconstant \(W\),
so both actions have global slices but no \(E\)-slice is
fixed by \(Q\), exactly as in the separate obstruction note.

## 5. Fixing any supplied slice and taking the primitive part

Keep any actual supplied \(E\)-slice
\(F=S+h(a,U,V)\). Equations (7) and (10) give
\[
Q_F:=Q-(QF)E
=W\bigl(\partial_V-h_V\partial_S\bigr).
\tag{13}
\]
The coordinates \((a,U,V,F)\) are actual polynomial
coordinates, with inverse \(S=F-h(a,U,V)\) followed by (4).
In that frame, \(Q_F=W\partial_V\). Its exact coefficient
content is \(W\), up to a complex unit, because the primitive
factor has value one on \(V\). Dividing by \(W\) therefore
gives a genuine global coordinate partial with slice \(V\),
fixing \(F\), commuting with \(E\), and having kernel
\(\mathbb C[a,U,F]\). This is valid for every \(h\),
not just the original choice \(F=S\).

This division is justified by the explicit actual coordinates,
not by a general primitive-division theorem for centralizers.
Nor does it bound the primitive field's flow degree in the
original frame when \(h\) varies. The preceding
[slice-adjustment note](good-partial-slice-adjustment-scope-pass75.md)
already gives an unbounded-degree control within this family.

The criteria are independent of the chosen Bezout pair. Every
other choice has the form \(\widehat r=r+kv\),
\(\widehat s=s-ku\), with \(k\in R\). Directly,
\[
\widehat U=U,\quad \widehat V=V+kU,\quad
\widehat S=S+2kV+k^2U,\quad
\widehat W=W,\quad \widehat\beta=\beta+2kW.
\tag{14}
\]
Thus both the ideal (9) and the congruence criterion (10) are
unchanged. The auxiliary adapted coordinate partial may change,
but its actual existence and the stated criteria do not.

## 6. Constant good directions and exact scope

For completeness, every nonconstant coprime member still has
\(G_1=0\) and \(G_2=\mathbb Ce_w\). The exact decomposition
from [the special-pair obstruction](nice-common-slice-obstruction-pass75.md)
works with general \(u,v\): if \(q\) is the coefficient
column of \(Q\), \(r_0=(z,-2y,x,1)\), and
\(\ell=(-v^2,2uv,-u^2,0)\), then
\[
J=q r_0+e_w\ell,\qquad J^2=q\ell,\qquad J^3=0.
\tag{15}
\]
The identities \(r_0q=\ell q=\ell e_w=0\) and
\(r_0e_w=1\) prove this by direct multiplication. Since
the pair is nonconstant, \(q\) has a nonzero entry among
its first three components. Thus \(J\) has rank two and
\(J^2\) rank one over \(\operatorname{Frac}B\).
The rational ratio \(u/v\) is nonconstant, so
\(u^2,uv,v^2\) are linearly independent over \(\mathbb C\).
The row \(\ell\) therefore forces every constant element
of \(\ker J^2\) to be a multiple of \(e_w\), and
\(Je_w=q\ne0\) gives \(G_1=0\).

Consequently this family does not answer whether a nice sliced
action can have \(G_2=0\). It supplies the exact common-slice,
global-slice and primitive-adjustment classification for an
already recognized one-good-direction family. The original
special action, the derived field's failure to be nice, and the
centralizer adjustment were already retained; the uniform
parameter tests (9)--(14) are the bounded addition here.

All required algebraic arguments are proved above. The separate
[three-method checker](conic_slice_family_checks_pass75.py) tests
finite actual inverse pairs, derivative and slice identities,
constant-axis boundaries, and high-degree supplied-slice controls.
It does not prove the all-parameter degree argument in (12).
No new external classification theorem, full regression,
historical novelty, human review, or formal proof-assistant
certificate is claimed. Pass74-or-earlier artifacts and shared
metadata are unchanged.
