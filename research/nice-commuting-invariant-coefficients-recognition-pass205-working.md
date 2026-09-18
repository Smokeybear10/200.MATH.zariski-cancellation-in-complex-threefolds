# Recognition from a nice commuting derivation with invariant coefficients

Status: working recognition criterion with precise published endpoints.
The additional coefficient-invariance property of the zero-R derivation204
supplies the step not proved in that note: its primitive auxiliary
derivation has an actual slice. A three-variable triangularization theorem
then gives an invariant coordinate of the original four-ring.

The criterion is stated separately from the weight-four application.
It does not assert that every commuting nice derivation satisfies the
extra coefficient hypothesis, or that the nonzero-R radical-pivot branch
has been recognized.

## 1. Criterion and the primary theorem inputs

Let
\[
\begin{gathered}
B=\mathbb C[X,Y,Z,W]=A[u],\qquad
E=\partial_u,\qquad A=\ker E,\\
a=EX\ne0,\qquad E^2X=0,\\
0\ne P\in\operatorname{LND}_{\mathbb C}(B),\qquad
PX=0,\qquad P^2Y=P^2Z=P^2W=0,\\
[E,P]=0,\qquad E(PY)=E(PZ)=E(PW)=0.
\end{gathered}
\tag{1}
\]
The conclusion is that \(E\) annihilates an ambient polynomial
coordinate of \(B\), and hence
\[
A\simeq\mathbb C^{[3]}.
\tag{2}
\]
Neither regularity of \(\ker P\) nor a slice for \(P\) is an input.
The condition \(E^2Y=0\), available in the application, is not needed
for this criterion.

Three published inputs are used with their stated hypotheses:

1. Dasgupta--Gupta, *Nice derivations over principal ideal domains*,
   Theorem3.6, gives a fixed linear coordinate over a PID for an
   irreducible nice derivation of its polynomial three-ring.
   Lemma2.3(ii) gives the coefficients over an invariant UFD base when
   both remaining coordinate second derivatives vanish.
   [Primary statement and proof, printed pp.3 and6--7](https://arxiv.org/pdf/1701.03635v1).
2. Daigle's three-variable theorem says that an irreducible LND with
   a nonfixed coordinate of derivation-degree one admits a triangular
   coordinate system containing that coordinate. We use its exact
   restatement as Dasgupta--Gupta Theorem4.8, printed p.12, which cites
   Daigle, *Triangular derivations of k[X,Y,Z]*, Theorem5.1.
   [Primary restatement](https://arxiv.org/pdf/1701.03635v1),
   [original publication](https://doi.org/10.1016/j.jpaa.2009.10.004).
3. Bhatwadekar--Gupta--Lokhande Theorem3.5 recognizes a regular kernel
   of a nonzero LND on \(\mathbb C^{[4]}\) that annihilates an ambient
   coordinate.
   [Primary statement and proof](https://arxiv.org/html/1501.01438v1).

The following argument checks the original-ring hypotheses before using
the second and third inputs. In particular it does not restrict the
given slice \(u\) to \(\ker P\).

## 2. Primitive division preserves every required property

Let \(d\) be a greatest common divisor in the UFD \(B\) of the
three coordinate coefficients \(PY,PZ,PW\), and set
\[
D=P/d.
\tag{3}
\]
At least one coefficient is nonzero. Each nonzero coefficient is
annihilated by both \(P\) and \(E\), by (1). Kernels of LNDs on a
characteristic-zero domain are factorially closed: this follows from
additivity of LND degree on a nonzero product. As \(d\) divides a
nonzero such coefficient,
\[
Pd=Ed=0.
\tag{4}
\]
Division of the coordinate coefficients defines \(D\) as a derivation
of \(B\), not only of its fraction field. Equation (4) implies
\(Dd=0\), and \(P^j(b)=d^jD^j(b)\) for \(b\in B\). Thus \(D\)
is locally nilpotent. It is irreducible by the gcd choice and has the
same kernel as \(P\). Moreover,
\[
DX=0,\quad D^2Y=D^2Z=D^2W=0,\quad [E,D]=0,
\quad E(DY)=E(DZ)=E(DW)=0.
\tag{5}
\]
The commutator uses \(Ed=0\); the last three identities follow by
dividing the corresponding identities in (1). In particular the
three coefficients of \(D\) are elements of \(A\).

## 3. A PID-linear invariant descends to a complex-linear invariant

Apply Dasgupta--Gupta Theorem3.6 to the irreducible nice derivation
\(D\) of \(\mathbb C[X][Y,Z,W]\), whose base \(\mathbb C[X]\)
is a PID. It supplies a nonzero row
\((l(X),m(X),n(X))\in\mathbb C[X]^3\) satisfying
\[
l(X)DY+m(X)DZ+n(X)DW=0.
\tag{6}
\]
In fact that theorem supplies a unimodular row and a full linear change
over \(\mathbb C[X]\), but only the nonzero relation is needed here.

The coefficient-invariance assumption is decisive at this point.
Because \(E^2X=0\), write \(X=x_0+au\), with \(x_0,a\in A\)
and \(a\ne0\). Hence \(X\) is transcendental over
\(\operatorname{Frac}A\). Expand the row in powers of \(X\).
Every coefficient of (6) is then an element of \(A\), so each
coefficient separately vanishes. A nonzero row coefficient gives
constants \((l_0,m_0,n_0)\ne(0,0,0)\) with
\[
U=l_0Y+m_0Z+n_0W,\qquad DU=0.
\tag{7}
\]
Complete this row to a matrix in \(\operatorname{GL}_3(\mathbb C)\),
giving coordinates \((U,V,T)\) obtained by a constant linear change
of \((Y,Z,W)\). In particular,
\(B=\mathbb C[X,U,V,T]\), \(D^2V=D^2T=0\), and the values
\(DV,DT\) remain \(E\)-invariant.

Now apply Dasgupta--Gupta Lemma2.3(ii) with the UFD base
\(R_0=\mathbb C[X,U]\). The irreducible derivation is
\[
D=F(X,U)\partial_V+G(X,U)\partial_T,
\qquad \gcd_{R_0}(F,G)=1,
\qquad EF=EG=0.
\tag{8}
\]
Irreducibility over this presentation is unchanged because it is a
coordinate change of the same polynomial ring. The two polynomials
\(F,G\) are not both zero.

## 4. Dependence forces a polynomial Bezout inverse

If one of \(F,G\) is a nonzero constant, they are comaximal. If one
vanishes identically, their coprimality makes the other a nonzero
constant, giving the same conclusion. Consider the remaining case
in which both are nonconstant. The identities in (8) give
\[
F_Xa+F_U(EU)=0,\qquad G_Xa+G_U(EU)=0.
\tag{9}
\]
Multiplying and subtracting eliminates \(EU\). Since \(a\ne0\),
the Jacobian \(F_XG_U-F_UG_X\) vanishes. In characteristic zero
this means that \(F,G\) are algebraically dependent. Equivalently,
their differentials in \(\mathbb C(X,U)\) have rank at most one.

Here is a direct proof that coprime, dependent polynomials in
\(\mathbb C[X,U]\) are comaximal. Let \(Q(S,T)\) be an irreducible
relation for \((F,G)\). The polynomial \(Q(0,T)\) is not identically
zero: otherwise \(S\) divides \(Q\), forcing \(F=0\).
If \(F,G\) had a common zero, choose an irreducible factor \(p\) of
\(F\) vanishing there. In the domain \(R_0/(p)\), the image of
\(G\) satisfies the nonzero polynomial \(Q(0,T)\) over
\(\mathbb C\), so it is a complex constant. Its value at the
common zero is zero. Thus \(p\mid G\), contrary to coprimality.
There is no common zero, so the Nullstellensatz gives
\[
(F,G)R_0=R_0.
\tag{10}
\]

Choose \(p_0,q_0\in R_0\) with \(p_0F+q_0G=1\). Define
\[
H=GV-FT,\qquad s=p_0V+q_0T.
\tag{11}
\]
These are original polynomials. Both inverse orders follow from
the explicit formulas
\[
V=Fs+q_0H,\qquad T=Gs-p_0H.
\tag{12}
\]
For example substitution into (11) gives
\(H=(Gq_0+Fp_0)H\) and \(s=(p_0F+q_0G)s\); substitution in
the other order returns \(V,T\). Consequently
\[
B=\mathbb C[X,U,H,s],\qquad
D=\partial_s,\qquad C:=\ker D=\mathbb C[X,U,H].
\tag{13}
\]
This proves the slice property rather than assuming it. The slice is
for the primitive \(D\); no slice for \(P=dD\) is asserted.

## 5. A coordinate in the auxiliary kernel becomes ambient

The commutator in (5) shows that \(E\) preserves \(C\). Its restriction
\(\delta=E|_C\) is a nonzero LND, since \(\delta X=a\ne0\),
and \(\delta^2X=0\). Divide its three coefficients in the polynomial
ring \(C=\mathbb C[X,U,H]\) by their gcd \(b_0\), writing
\(\delta=b_0\delta_0\). This primitive division is justified as
follows. The nonzero coefficient \(a=\delta X\) belongs to
\(\ker\delta\) and is divisible by \(b_0\). Factorial closure
gives \(\delta b_0=0\). The same iterate argument as in Section2
therefore makes \(\delta_0\) an irreducible LND with the same
kernel, and
\[
\delta_0X=a/b_0\ne0,\qquad \delta_0^2X=0.
\tag{14}
\]

The exact Daigle theorem, in the restatement cited in Section1, now
applies to the actual polynomial three-ring \(C\) and its coordinate
\(X\). It supplies coordinates \(I,X,J\) of \(C\) with
\(\delta_0I=0\). Hence
\[
C=\mathbb C[I,X,J],\qquad EI=0,
\qquad B=\mathbb C[I,X,J,s].
\tag{15}
\]
The last equality uses the proved inverse (12). It is precisely what
makes \(I\) an ambient coordinate, not just a coordinate of an
unrelated subring.

Finally \(A\simeq B/(u)\) is regular. Indeed \(Eu=1\) expresses
one as a polynomial combination of the four partial derivatives of
\(u\), so its zero fiber is smooth. The nonzero original derivation
\(E\) is \(\mathbb C[I]\)-linear by (15). Bhatwadekar--Gupta--Lokhande
Theorem3.5 gives \(A=\mathbb C[I]^{[2]}\), proving (2).
No step required \(u\in C\), or required \(\delta\) to have a slice.

## 6. Application to the zero-R radical-pivot branch204

Retain the exact actual input and the additional branch \(R=0\) in
[the old-W-pivot lemma204](weight-four-radical-pivot-zero-r-nice-derivation-pass204-working.md).
That note proves that
\(P=aN-(NX)E\) is a nonzero nice LND of the original four-ring,
fixes \(X\), and commutes with \(E\). It also proves that the
projected \(y,z,w\) are affine on the generic line and that
\(N\vartheta=N\sigma=0\). Thus its actual chart gives
\[
PY=aNy,\qquad P\widehat Z=aNz,\qquad
P\widehat W=aNw.
\tag{16}
\]
Here \((\widehat Z,\widehat W)=(W,Z)\), as in204. All three
right-hand sides lie in the invariant fraction field
\(\operatorname{Frac}A\), and all three left-hand sides are actual
polynomials. Therefore they are annihilated by \(E\). This verifies
the final hypothesis of (1), not just its commutator hypothesis.
The original global slice and exact time profile give the other
required conditions on \(E\).

The criterion proves recognition of this supplied \(R=0\) branch
with full initial kernel \(\mathsf Z^2-\mathsf X^2\mathsf W\).
It does not say that \(R\) vanishes for every such frame. The
\(R\ne0\) branch and its essential quadratic projected potential
are outside this conclusion.

## 7. Coefficient invariance is an additional hypothesis

Here is a concrete control that separates the hypotheses. Start with
independent \(u,v,c,w_0\), put \(E=\partial_u\), \(P=\partial_v\),
and use the actual coordinates
\[
X=u,\qquad Y=v+cu,\qquad Z=c+u^2,\qquad
W=w_0+uv+u^2.
\tag{17}
\]
The polynomial inverse is
\(u=X\), \(c=Z-X^2\), \(v=Y-X(Z-X^2)\),
\(w_0=W-Xv-X^2\); substitution checks both orders.
The E-degrees are exactly1122, the derivations commute, and
\[
PX=PZ=0,\qquad PY=1,\qquad PW=X,
\qquad P^2X=P^2Y=P^2Z=P^2W=0,
\qquad E(PW)=1.
\tag{18}
\]
In particular \(E^2X=E^2Y=0\), but the final condition of (1)
fails. Thus it cannot be inferred from niceness, commutation and the
global slice alone.

This example does not meet the full initial-kernel condition of204.
Its initial map has entire kernel
\[
(\mathsf Z-\mathsf X^2,\ \mathsf W-\mathsf X^2).
\tag{19}
\]
Indeed its image is \(\mathbb C[\tau,c\tau]\), and these two
elements are algebraically independent over \(\mathbb C\), so the
quotient by the displayed ideal injects. The example therefore has a
height-two initial kernel. It disproves an inference about the abstract
pair, not the coefficient-invariance conclusion proved from the
particular radical-pivot chart.

Nonunit content is also permitted in (1). Replacing \(P\) by
\(c\partial_v\) and replacing (17)'s \(W\) by \(w_0+u^2\)
gives only one nonzero P-coordinate coefficient, \(PY=c\), which
is E-invariant. Here the gcd is the nonunit \(c\), and the primitive
derivation is \(\partial_v\). This is a check on the content-division
step, not another claim about a height-one initial kernel.

## 8. Applicability boundary and verification scope

The bounded audit behind this proof also read Dasgupta--Gaifullin's
three-variable commuting theorem4.5 and fixed-base construction
Corollary3.18. Those statements do not by themselves apply the
desired recognition endpoint to the original four-ring. They are
not proof inputs here.
[Primary full text](https://arxiv.org/html/2306.00510v2).
The earlier
[bounded199 audit](time-degree-1122-primary-literature-audit-pass199-working.md)
remains unchanged: this proof has the extra actual derivation and
coefficient-invariance hypotheses, not merely time profile1122.

All arguments above are written proofs. No finite test suite was
authored or executed for this note. The source checks do not constitute
human expert review, proof-assistant certification or novelty clearance.
The statement supplies no arbitrary-entry theorem and no resolution
of unrestricted complex-threefold cancellation. All earlier sources
remain unchanged.
