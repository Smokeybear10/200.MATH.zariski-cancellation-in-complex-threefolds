# The I-only replica mechanism forces unit speed

Status: working intrinsic obstruction to one specified extension of
[the actual node/cusp mechanism207](radical-nodal-cuspidal-actual-frame-pass207-working.md).
The replica remains an actual polynomial automorphism for every
polynomial parameter considered here. However, if its transformed
\(W\)-coordinate is invariant under a globally sliced derivation
with the indicated time degrees, then \(EX\) must be a nonzero
complex constant. Thus this particular invariant-slot mechanism
cannot cover the nonunit-speed case.

This does not concern all invariant parameters for the same auxiliary
derivation, other transformed coordinate slots, or compositions of
different replicas. In particular it does not address parameters
depending on \(X\) or \(Z\), and it is not a cancellation obstruction.

## 1. Precise hypotheses and conclusion

Let
\[
B=\mathbb C[X,Y,Z,W],\qquad E\in\operatorname{LND}(B),\qquad
Es=1\text{ for some }s\in B,
\qquad \deg_E X=1,\quad\deg_E Y\le1,\quad\deg_E W=2.
\tag{1}
\]
Put \(a=EX\ne0\). These hypotheses include the relevant degrees
of an actual sliced1122 radical frame. The result below does not
need a degree assumption on \(Z\) or a leading-kernel hypothesis.

For a polynomial \(P\in\mathbb C[S]\), define
\[
I=W^2+XY-X^2Z,\qquad J=P(I),\qquad x=W-XJ.
\tag{2}
\]
The assertion is
\[
Ex=0\quad\Longrightarrow\quad
\deg P=1,\qquad a\in\mathbb C^*,\qquad
\ker E=\mathbb C[x,r,T]
\tag{3}
\]
for explicit actual polynomial coordinates \(r,T\) below.
The constant polynomials, including zero, cannot satisfy \(Ex=0\)
under (1).

## 2. An actual coordinate system for every P

Define, without using \(E\),
\[
Y'=Y+2WJ-XJ^2,\qquad
r=\frac{Y'-XZ}{2},\qquad T=Z-J^2.
\tag{4}
\]
Then \((X,x,r,T)\) is an actual polynomial coordinate system.
Here division is only by the nonzero complex constant two.

For completeness, start instead with independent symbols
\((\xi,\eta,\varrho,\mathcal T)\). Set
\[
j=P(\eta^2+2\varrho\xi),\qquad
X=\xi,\quad W=\eta+\xi j,\quad
Z=\mathcal T+j^2,\quad
Y=2\varrho+\xi\mathcal T-2\eta j.
\tag{5}
\]
Substitution gives
\[
W^2+XY-X^2Z=\eta^2+2\varrho\xi.
\tag{6}
\]
Thus the \(J\) recomputed using (2) is exactly \(j\).
Equations (2) and (4) then return
\(x=\eta\), \(r=\varrho\), \(T=\mathcal T\), and
\(X=\xi\). This proves one inverse order.

Conversely, begin with \(X,Y,Z,W\) and form (2), (4).
Direct expansion gives
\[
x^2+2rX=I,
\qquad W=x+XJ,
\qquad Z=T+J^2,
\qquad Y=2r+XT-2xJ.
\tag{7}
\]
The first equality makes \(P(x^2+2rX)=J\), so (5) reconstructs
every original coordinate. This proves the reverse inverse order.
In particular
\(B=\mathbb C[X,x,r,T]\) before any invariance is claimed.

This map also has the replica interpretation used in207:
\[
\delta=X\partial_W-2W\partial_Y,\qquad
\delta I=0,\quad\delta J=0,
\qquad \exp(-J\delta)(W)=x,
\qquad \exp(-J\delta)(Y)=Y'.
\tag{8}
\]
The derivation \(\delta\) is locally nilpotent, and the invariance
of \(J\) makes its replica locally nilpotent. The inverse
exponential is \(\exp(J\delta)\). The changes from \(Y',Z\)
to \(r,T\) are triangular: after introducing \(r\), the identity
\(J=P(x^2+2rX)\) makes \(J\) independent of \(Z\).

## 3. Exact time-degree rigidity

For a nonzero element \(f\), let \(\deg_E f\) be the largest
integer \(n\) for which \(E^nf\ne0\). In a characteristic-zero
domain, the Leibniz rule gives
\(\deg_E(fg)=\deg_E f+\deg_E g\): the top derivative is the
nonzero product of the top derivatives multiplied by a nonzero
binomial coefficient. If the two degrees are different, the
degree of a sum is their maximum.

Assume now \(Ex=0\). Since \(W=x+XJ\) has degree two and
\(x\) has degree zero, \(J\) is nonzero and
\[
\deg_E J=1.
\tag{9}
\]
A constant \(P\) would make \(J\) invariant and give degree at
most one for \(W\), so \(P\) is nonconstant. Also \(I\) cannot
be invariant. If \(m=\deg P\) and \(n=\deg_E I>0\), the terms
of \(P(I)\) have distinct time degrees, and its leading term
gives
\[
1=\deg_E J=m n.
\tag{10}
\]
Both integers are positive. Hence \(m=n=1\). No degree argument
of this form is being asserted for \(P(X,I)\): its coefficients
would then have their own time degrees and could cancel.

By (7), \(I=x^2+2rX\). Since \(x\) is invariant and
\(\deg_E I=\deg_E X=1\), additivity of product degree gives
\(\deg_E r=0\). The element \(r\) is nonzero because it is
an actual coordinate. Therefore \(Er=0\).

Finally the last identity in (7) gives
\[
XT=Y-2r+2xJ.
\tag{11}
\]
Every term on the right has degree at most one. The nonzero
product on the left has degree \(1+\deg_E T\), so
\(\deg_E T=0\). Thus \(ET=0\). Again \(T\) is an actual
coordinate, not a possibly zero generic coefficient.

We have proved that \(E\) fixes three members of the actual
coordinate system (4). Consequently
\[
E=a\partial_X\text{ on }\mathbb C[x,r,T][X],\qquad
a\in\mathbb C[x,r,T]\setminus\{0\}.
\tag{12}
\]
To justify the coefficient assertion, \(E^2X=Ea=0\) and
\(E=a\partial_X\) give \(a\partial_Xa=0\), hence
\(\partial_Xa=0\). The global slice now gives
\(1=Es=a\partial_Xs\). Thus \(a\) is a unit of the polynomial
ring \(B\), namely a nonzero complex constant. The kernel in
(12) is exactly \(\mathbb C[x,r,T]\), proving (3).

## 4. What the radical leading relation does give globally

There is a separate useful fact which does not force unit speed.
For this paragraph, assume an actual radical frame of exact
time profile \((1,1,2,2)\), and write
\[
A=\ker E,\quad a=EX,\quad
e=E^2Z/2,\quad h=E^2W/2,
\qquad a^2e=h^2.
\tag{13}
\]
The coefficients belong to \(A\). The global slice gives
\(B=A[s]\); normality of \(B\) implies normality of \(A\).
Indeed an element of \(\operatorname{Frac}A\) integral over
\(A\) is integral over \(B\), hence belongs to
\(B\cap\operatorname{Frac}A=A\).

The element \(g=h/a\) in \(\operatorname{Frac}A\) satisfies
the monic equation \(g^2-e=0\). Thus \(g\in A\), not merely
in a coefficient field. In particular the following are actual
polynomial identities:
\[
\begin{gathered}
d=EW-2gX\in A,\qquad c=aEZ-gEW\in A,\\
E(aW-gX^2)=a d,\qquad E(aZ-gW)=c.
\end{gathered}
\tag{14}
\]
For example \(Ed=E^2W-2ga=2h-2ga=0\), and
\(Ec=2ae-2gh=0\). These identities give polynomial invariants
and elements of time degree at most one. They do not make
\(g,d,c\), \(aW-gX^2\), or \(aZ-gW\) coordinates; nor do
they make division by \(a\) an allowed polynomial operation.

## Scope

Taking \(P(S)=(S-\mu)/2\) includes the precise invariant-slot
construction207. The result explains why making that same
\(W-XP(I)\) invariant in a globally sliced frame of the stated
degrees automatically returns to unit \(EX\).

It does not exclude an invariant coordinate in another slot, a
replica with a more general parameter in \(\ker\delta\), a
different auxiliary derivation, or a longer composition. It does
not show that every radical frame admits (2) with \(Ex=0\).
The leading-root facts (13)--(14) remain possible input to such
a broader construction, with their coordinate and denominator
issues still open. No coefficient-field reparameterization is
treated as an original polynomial automorphism.

The complete coordinate and degree argument is written above;
no saved checker was executed, imported or compiled for this
note. No earlier source, index or packet was edited. There is
no unrestricted cancellation, arbitrary-entry, minimum-profile,
historical novelty or expert-certification claim.
