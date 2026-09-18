# A cubic root excludes the proper whole-double branch

The supplied actual proper-image whole-double branch is impossible under
the coefficient restrictions112 and analytic-prime support113. A simple
root of an auxiliary cubic produces two nonunit factors of the actual
first-image scalar P. Their joint ideal is primary for the base maximal
ideal, so they cannot both be powers of the same prime.

This is a conditional local theorem. It does not put an arbitrary
cancellation input into the supplied frame, settle the relative cubic
case, or recognize the resulting global threefold as affine space.

## 1. Algebraic statement and actual hypotheses

Let R be a complete regular local surface with maximal ideal m and
residue field C. Suppose a,b are nonzero elements of m and J=(a,b) is
m-primary. Let h belong to m and assume

\[
\begin{gathered}
b^2=s h+a^2u+abv,\qquad s,u,v\in R,\\
B_2\in\mathfrak m(h)+\mathfrak m(a^2)
                    +\mathfrak m(ab)+\mathfrak m^2(b^2),\\
P=ah+bB_2\ne0.
\end{gathered}
\tag{1}
\]

Then P has two nonunit factors L,H satisfying J squared contained in
(L,H). In particular P is not a unit times a power of one prime.

These hypotheses hold over the completed base of the actual proper
branch by [product-index112, equations (2) and (6)](whole-double-product-index-pass112.md).
The [ramified113 argument, Sections 2--3](whole-double-ramified-completion-descent-pass113.md)
separately says that its P is a unit times a power of one prime that
remains prime in the completed base. This is the contradiction used
below. Algebraic irreducibility alone would not justify that input.

The proof needs only h in m, not the stronger h in m squared of113.
It does not use the smooth-a, square-ideal or weighted exclusions114,
or the completed-kernel and finite-degree descent results113.

## 2. Absorb the exceptional square term

Multiplying the first relation in (1) by m squared absorbs the last
term of the B2 bound into the first three. Hence there exist
eta,z,t in m such that

\[
\begin{gathered}
B_2=h\eta+a^2z+abt=h\eta+a\zeta,
\qquad\zeta=az+bt,\\
P=(a+b\eta)h+ab(az+bt).
\end{gathered}
\tag{2}
\]

No change of the distinguished generators or division by a,b,h or s
has been made. This absorption is valid also when the coefficient s
is a nonunit.

## 3. The auxiliary cubic has a simple formal root

Consider the polynomial, whose coefficients are fixed elements of R,

\[
\begin{gathered}
F(T)=(T+\eta)(1-T^2u-Tv)+sT^2z+sTt,\\
F(0)=\eta\in\mathfrak m,\qquad
F'(0)=1-\eta v+st\in R^*.
\end{gathered}
\tag{3}
\]

Its residue has a simple root at zero. Thus there exists rho in m
with F(rho)=0. Here is the direct argument, without a monicity
assumption. Start with rho0=0 and replace rho_n by
rho_n minus F(rho_n)/F'(rho_n). The derivatives remain units, and
the error is squared at every step. The corrections tend to zero
m-adically, so completeness gives a limit rho. Polynomial continuity
gives F(rho)=0. This is the simple-root Newton argument underlying
Hensel's lemma.[^hensel]

Set

\[
\begin{gathered}
D=1-\rho^2u-\rho v\in R^*,\qquad
L=a-\rho b,\qquad M=u(a+\rho b)+bv,\\
(\rho+\eta)D=-s\rho(\rho z+t),\qquad
Db^2-sh=LM.
\end{gathered}
\tag{4}
\]

The last equality follows directly from (1). In particular it does
not treat a,b as algebraically independent over a coefficient ring.

## 4. An explicit cofactor

Define an actual element of R, using only the unit denominator D, by

\[
H=h+b\zeta+\rho b^2z+
       \frac{\rho b(\rho z+t)}{D}M.
\tag{5}
\]

Expansion, using (2), gives the denominator-free identity

\[
D(P-LH)=b h F(\rho)
 +\rho b(\rho z+t)(b^2-sh-a^2u-abv)=0.
\tag{6}
\]

Therefore P=LH. All terms in H belong to m, and L belongs to J,
so both factors are nonunits. The assumption P nonzero ensures neither
factor is zero. This identity also covers eta=0, z=0 or t=0 without
dividing by any of them.

## 5. The factors cannot share their entire prime support

Modulo (L), one has a=rho b, and therefore

\[
\begin{gathered}
H\equiv h+b^2C\pmod{L},\\
C=2\rho z+t+
  \frac{\rho(\rho z+t)(2\rho u+v)}{D}\in\mathfrak m,\\
Db^2\equiv sh\pmod{L},\qquad
H\equiv h\left(1+\frac{sC}{D}\right)\pmod{L},\\
1+\frac{sC}{D}\in R^*,\qquad
(L,H)=(L,h),\qquad b^2\in(L,h).
\end{gathered}
\tag{7}
\]

The equality of ideals uses the displayed unit and is valid even if
R/(L) is nonreduced. Since a=L+rho b, the elements a squared and ab
also belong to (L,b squared). Consequently

\[
\boxed{\qquad P=LH,\quad L,H\in\mathfrak m\setminus\{0\},
\quad J^2\subseteq(L,H),\quad\sqrt{(L,H)}=\mathfrak m.\qquad}
\tag{8}
\]

The regular local surface R is a UFD. If P were a unit times p to
the e for one prime p, both nonunit factors would be units times
positive powers of p. Then (L,H) would be contained in the height-one
ideal (p), contradicting (8). This proves the algebraic statement and
excludes the supplied actual proper-image whole-double alternative.

## 6. Scope and remaining cancellation obligations

The argument treats every residual colength and every coefficient
singularity satisfying (1). It supersedes the restricted exclusions
developed earlier in114. It also avoids trying to construct a formal
quadratic parameter in the proper branch: that branch cannot occur
under the retained actual hypotheses.

The proof does not remove those hypotheses. In particular the all-divisor
degree-module models112 and the one-branch integral-topology input113
are substantive retained dependencies. The arbitrary-frame entry,
relative cubic analysis and global affine-space recognition obligations
are not proved here. Thus this is not a solution of complex-threefold
cancellation, and no novelty or publication claim is made.

An independent argument by homogeneous cubic division is given in
[cubic-division114](whole-double-cubic-division-exclusion-pass114.md).
Finite symbolic identities can check the displayed formulas, but not
the all-order root, analytic-prime hypothesis or geometric dependency
chain. AI proof reviews are not human expert review or formal verification.

[^hensel]: The Stacks Project, [Lemma 10.153.9 (04GM), complete local
    rings are Henselian](https://stacks.math.columbia.edu/tag/04GM).
    The displayed statement and proof were freshly read. Its statement
    is phrased through monic polynomials; the unit-derivative iteration
    required for this potentially nonmonic cubic is proved directly above.
