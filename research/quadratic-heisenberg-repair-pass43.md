# A global normalizer and a locally nilpotent quotient repair

In the nonconstant two-quadratic power-law branch, the condition
\(T_cg=0\) permits a global polynomial LND construction. The first
field is a normalizer, not the commuting candidate from the previous
pass. A second construction uses a compatible local slice and a
centralizer lemma to produce an explicit global LND commuting with
the original action.

These deductions do not assume that arbitrary partials stay locally
nilpotent after localization. They do not automatically produce
independent quotient directions or an ambient coordinate.

## 1. Actual hypotheses and notation

Retain the nonzero-\(\ell\) branch of the
[full companion reduction](two-quadratic-top-line-pass42.md).
Thus \(B=\mathbb C[x_1,x_2,x_3,x_4]\), \(E\) is a sliced LND,
the first two actual partials have second adjoint zero and the last
two have third adjoint zero, and their two defects are independent.
For \(3\le m\le5\), the highest data satisfy
\[
E^mx=cg^m,\qquad L_0E^{m-1}x=\lambda g^{m-1},
\quad Eg=0,\quad g\notin\mathbb C,
\tag{1}
\]
where \(c\ne0\) is a constant good-direction vector and
\(\lambda\ne0\) is a constant bad-direction vector. Assume
\[
T_cg=0.
\tag{2}
\]
Put \(a=(m-1)/2\), \(W_c=[E,T_c]\),
\(W=[E,T_\lambda]\), and \(V=[E,W]\). The earlier top
identities and denominator gate give
\[
gW_c=-aV,\qquad Wg=Vg=0,\qquad [E,V]=0.
\tag{3}
\]
Here \(V\ne0\), since it is a nonzero constant combination of
independent defects. It is an actual polynomial LND: it is the top
coefficient of the actual conjugated coordinate partial \(T_\lambda\).

## 2. A polynomial family gives a new LND

Let \(u\) be an external parameter, killed by all fields. Define
\[
P_u=gT_c+2auT_\lambda.
\tag{4}
\]
The constant directions \(T_c,T_\lambda\) are independent.
Choose actual linear coordinates \(b,v,z_1,z_2\) with
\(T_c=\partial_b\), \(T_\lambda=\partial_v\).
Condition (2) says \(g\in\mathbb C[v,z_1,z_2]\).
Thus (4) is a triangular LND of \(B[u]\), and also of
\(B[u,u^{-1}]\).

On the latter ring, \(\exp(E/u)\) is an actual automorphism.
The given adjoint bounds truncate its conjugation exactly:
\[
\begin{aligned}
\exp(\operatorname{ad}_{E/u})(P_u)
&=gT_c+u^{-1}gW_c
  +2auT_\lambda+2aW+a u^{-1}V\\
&=Y+2auT_\lambda,\qquad Y:=gT_c+2aW.
\end{aligned}
\tag{5}
\]
The last equality uses the full cancellation in (3).
The conjugated field is an LND on the Laurent ring and preserves the
polynomial subring \(B[u]\). Its restriction is therefore an LND:
an iterate vanishing in the Laurent ring vanishes in the subring.
Its ideal \((u)\) is stable, so specialization at \(u=0\) proves
\[
Y\in\operatorname{LND}(B).
\tag{6}
\]
This is not a specialization of an arbitrary pointwise family with
an unproved uniform nilpotence bound. The entire Laurent-ring field
is locally nilpotent before restriction and specialization.

In addition, \(Yg=0\), and (3) gives \([E,Y]=aV\).
The \(t^2\) coefficient in the commutation of the two actual
conjugated partials \(T_c,T_\lambda\) is
\[
[T_c,V]+2[W_c,W]=0.
\tag{7}
\]
Using \(W_c=-aV/g\) and \(Wg=Vg=0\) in (7) yields
\[
[E,Y]=aV,\qquad [Y,V]=[E,V]=0.
\tag{8}
\]
All three are polynomial LNDs of the original ring. In particular,
\(Y\) is not being called a coordinate partial or a field commuting
with \(E\).

## 3. A centralizer lemma

**Lemma.** Let \(A\) be a domain containing \(\mathbb Q\),
\(0\ne C\in\operatorname{LND}(A)\), and let \(D\) be a derivation
of \(A\) commuting with \(C\). If the restriction of \(D\) to
\(S=\ker C\) is locally nilpotent, then \(D\) is locally nilpotent
on \(A\).

Choose a local slice \(r_0\) of \(C\), with
\(c_0=Cr_0\ne0\) in \(S\). The \(C\)-plinth
\(S\cap C(A)\) is \(D\)-stable, since \(DC=CD\).
Take the largest \(N\) with \(D^Nc_0\ne0\), and set
\[
c=D^Nc_0,\qquad r=D^Nr_0.
\]
Then \(c\in S\setminus\{0\}\), \(Dc=0\), and \(Cr=c\).
The local-slice theorem gives
\[
A_c=S_c[r].
\tag{9}
\]
Commutation now gives \(C(Dr)=D(Cr)=Dc=0\), so \(Dr\in S\).
The derivation on \(S_c\) is locally nilpotent because \(Dc=0\);
adjoining \(r\), whose derivative belongs to that base, remains
locally nilpotent. Restriction from \(A_c\) to \(A\) proves the
lemma. The local-slice theorem is the only external step.[^slice]

## 4. A Heisenberg projection with a compatible slice

Here is a general form of the quotient construction.
Let \(\delta,L,C\) be LNDs on a domain \(B'\) containing \(\mathbb Q\)
such that
\[
[\delta,L]=C,\qquad [\delta,C]=[L,C]=0.
\tag{10}
\]
Suppose \(\sigma\in B'\) satisfies \(\delta\sigma=1\) and
\(C\sigma=0\). Put \(A'=\ker\delta\) and \(b=L\sigma\).
Then \(\delta b=Cb=0\), and
\[
D_0=L-\sigma C-b\delta
\tag{11}
\]
commutes with \(\delta,C\) and kills \(\sigma\).

If \(C\ne0\), its restriction to \(A'\) is nonzero, since
\(B'=A'[\sigma]\) and \(C\sigma=0\).
On \(S=A'\cap\ker C\), the restriction of \(D_0\) is exactly
that of \(L\). This subring is stable under \(L\), by (10);
hence that restriction is locally nilpotent.
The lemma applies to \(D_0|_{A'}\), which commutes with \(C|_{A'}\).
It follows that \(D_0\) is locally nilpotent on \(A'\), and then
on \(B'=A'[\sigma]\), because it kills \(\sigma\).
If \(C=0\), \(L\) already preserves \(A'\), giving the same
conclusion directly.

This is stronger than polynomial descent alone. The original field
\(L\) is an LND, the commutator is central, and the chosen slice is
killed by that commutator. Those are genuine additional hypotheses.

## 5. An explicit global replica in the power-law branch

Choose \(j\) with \(c_j\ne0\), and put
\[
\tau=(E^{m-1}x)_j/c_j,\qquad
\sigma=\tau/g^{m-1}.
\tag{12}
\]
The actual next-to-top bad-column identity gives
\(V(E^{m-1}x)=-2c g^{m-1}Wg=0\). Therefore
\[
E\tau=g^m,\qquad V\tau=0,\qquad
\delta:=E/g,\quad \delta\sigma=1.
\tag{13}
\]
On \(B_g\), set
\[
L=Y/g,\qquad C=aV/g^2.
\tag{14}
\]
They are actual LNDs because \(E,Y,V\) kill \(g\).
Equations (8) imply (10), and (13) gives \(C\sigma=0\).
Thus (11) is an LND on \(B_g\), commuting with \(\delta,C\).
It kills \(g\) and \(\sigma\).

The clearing is not merely existential. Since
\(L\sigma=Y\tau/g^m\), define
\[
\mathcal R:=g^{m+1}D_0
=g^mY-a\tau V-(Y\tau)E.
\tag{15}
\]
This is polynomial on \(B\). It is an LND on \(B_g\), since
\(D_0g=0\), and hence its polynomial restriction is an LND on \(B\).
Furthermore,
\[
[E,\mathcal R]=[V,\mathcal R]=0,\qquad
\mathcal Rg=\mathcal R\tau=0.
\tag{16}
\]
For example \(E(Y\tau)=Y(g^m)+aV\tau=0\), so the polynomial
bracket with \(E\) can also be checked directly in (15).

Both \(V\) and \(\mathcal R\) restrict to LNDs of the original
kernel \(A=\ker E\), and they commute. Their fraction-field
independence on \(A\) is equivalent to
\[
\operatorname{rank}(E,Y,V)=3.
\tag{17}
\]
Indeed (15) replaces \(Y\) by a nonzero multiple modulo the
span of \(E,V\), and the kernel of restriction of fields centralizing
a sliced \(E\) is its one-dimensional fraction-field span.
If the rank is two, \(\mathcal R|_A\) may be dependent on \(V|_A\)
or zero. It is not automatically a new independent action.

## 6. Recognition and remaining scope

The [omitted-coordinate descent criterion](commuting-coordinate-descent-pass43.md)
recognizes the original kernel if either
\[
\operatorname{rank}(E,V_3,V_4)=3
\quad\text{or}\quad
\operatorname{rank}(E,Y,V)=3.
\tag{18}
\]
The commuting triple in the first case is \(E,V_3,V_4\); in the
second it is \(E,V,\mathcal R\), whose rank equals that of
\(E,Y,V\) by (15). The latter displayed triple itself is not
commuting. Each eligible commuting triple consists of independent
global LNDs fixing the nonconstant polynomial \(g\), and (2) omits
an actual constant coordinate direction from \(g\).

The two constructions do not prove (2) in general, nor do they prove
one of the rank-three alternatives. The earlier nonzero-constant
\(T_cg\) branch is already recognized. Nonconstant \(T_cg\), and
the remaining rank-two branch when \(T_cg=0\), still require an
argument. The complete supplied two-quadratic profile and the
unrestricted cancellation target remain unresolved.

No high-degree example realizing all of (1) is asserted by the
finite normalizer controls. No novelty, human review or formal
proof-assistant claim is made.

[^slice]: Nikhilesh Dasgupta and Sergey Gaifullin, [*On locally nilpotent derivations of polynomial algebra in three variables*](https://arxiv.org/pdf/2306.00510v2), Theorem 2.5 and Proposition 2.6, PDF pp. 5-6. The stated slice and local-slice results apply to domains over a characteristic-zero field, not only to polynomial three-rings. The abstract lemmas here assume a domain containing the rationals; the applications are complex algebras.
