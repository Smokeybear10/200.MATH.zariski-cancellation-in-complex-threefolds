# Time-degree two and quasi-nice derivations: statement audit

The bounded search did not locate a published theorem saying that every
slice LND on \(\mathbb C^{[4]}\) with time-degree at most two, or with a
rank-one last coefficient, has an ambient coordinate in its kernel.
This is a coverage statement, not a claim of novelty or openness.

The particular \(m=2\) power-law branch in this investigation is now
closed by the explicit shear in
[height-nine-power-law-pass.md](height-nine-power-law-pass.md), not by
the literature results below. The distinction matters because that
argument uses additional identities of the mixed coordinate frame.

## 1. The precise terminology

For \(\Phi_t=\exp(tE)x\), time-degree at most two means
\(E^3x_i=0\) for every member of the specified coordinate system. In
the power-law case,
\[
E^2x=cg^2,\qquad c\in\mathbb C^4\setminus\{0\},\qquad Eg=0,
\]
a constant linear coordinate change makes three entries of \(E^2x\)
zero. Thus the derivation is 3-quasi: the square of the derivation
kills three coordinate generators. This does not assert that the
derivation itself kills any of them. It also does not assert
*strictly* 3-quasi, which would exclude every coordinate system making
all four second iterates zero. These are the definitions in
[Dasgupta and Lahiri, Definition 2.2 and Definition 2.3](https://arxiv.org/pdf/2302.13787v6).

## 2. Three-variable and fixed-base recognition results

[Dasgupta and Gupta, *Nice derivations over principal ideal domains*,
Theorems 4.1 and 4.8](https://arxiv.org/pdf/1701.03635)
reproduce the following Wang and Daigle results over a
characteristic-zero field \(k\), for an irreducible LND of \(k[X,Y,Z]\):

- Theorem 4.1 assumes \(D\ne0\) and \(D^2X=D^2Y=0\), and gives an
  invariant coordinate and rank at most two.
- Theorem 4.8 assumes a coordinate \(Y\) with \(DY\ne0\) and
  \(D^2Y=0\). It gives coordinates \((X,Y,Z)\) with
  \(DX=0\), \(DY\in k[X]\), and \(DZ\in k[X,Y]\).

Their Proposition 4.4 requires an irreducible \(R\)-LND on
\(R[X,Y,Z]\), \(R\supset\mathbb Q\) a PID, \(D^2X=D^2Y=0\), and
generic case (I) of Theorem 4.1: over \(\operatorname{Frac}R\), suitable
linear forms \(L_1,L_2\) in \(X,Y\) satisfy
\(DL_1=0\), \(DL_2\in K[L_1]\), \(DZ\in K[L_1,L_2]\).
It yields relative rank below three. Corollary 3.8 on \(k^{[4]}\)
already assumes \(DX_1=0\), plus \(D^2X_i=0\) for \(i=2,3,4\).

These hypotheses do not supply the missing four-variable invariant
coordinate. The reproduced statements were inspected; Wang's original
article and Daigle's original theorem were not independently recovered
in this pass.

## 3. The current two-variable-over-a-UFD result

The inspected [Dasgupta and Lahiri manuscript](https://arxiv.org/pdf/2302.13787v6)
is **arXiv:2302.13787v6, July 24, 2026**, titled *On image ideals of nice
and quasi-nice derivations on R[X1,X2]*. Earlier indexing retains a
different title and lemma numbering.

Its Lemma 2.12 assumes a UFD \(R\) containing a characteristic-zero
field, \(B=R[X,Y]\), and an irreducible \(R\)-LND \(D\). If
\(D^2X=0\), then
\[
DX\in R,\quad DY\in R[X],\quad
\ker D=R[bY+f(X)],\qquad b\in R,\quad f\in R[X].
\]
If also \(D^2Y=0\), then
\(D=b\partial_X-a\partial_Y\), \(a,b\in R\), and
\(\ker D=R[aX+bY]\). In that nice case, a PID base guarantees a
slice. The paper attributes this lemma to Wang.

An invariant \(g\) does not justify treating \(\mathbb C^{[4]}\) as
\(\mathbb C[g]^{[3]}\), much less as a polynomial extension by two
variables over a fixed UFD. That presentation is an additional
geometric requirement, not a consequence of the notation.

## 4. Quasi-translations concern the whole coefficient map

[de Bondt, *Quasi-translations and singular Hessians*,
Proposition 1.3](https://arxiv.org/pdf/1501.05168)
identifies a quasi-translation \(x+H\) with \(JH\,H=0\), equivalently
\(H(x+tH)=H\). Its additive flow is \(x+tH\). Theorem 5.5 gives a
linear normal form when such a quasi-translation has Jacobian rank one.

If \(E^2x\ne0\), the flow
\[
x+tEx+\frac{t^2}{2}E^2x
\]
is not of that form. Even when the last coefficient separately defines
a quasi-translation, its invariant coordinates are not thereby
invariants of \(E\). An additional compatibility argument is required.

## 5. Concrete source cross-check: ordinary degree is indispensable

[de Bondt, *Quadratic polynomial maps with Jacobian rank two*,
Theorem 3.2](https://arxiv.org/pdf/1601.00579)
assumes that \(H\) is an ordinary quadratic polynomial map over a
field, \(\operatorname{rank}JH\le2\), and \(JH\) is nilpotent. It
concludes that \(JH\) is similar over the field to a triangular matrix.
Theorem 3.3 likewise assumes ordinary quadratic \(H\), now with
\((JH)^2=0\), and concludes triangular similarity. Its proof on PDF
page 17 explicitly uses \(\deg JH\le1\) to obtain
\[
JH(tx+(1-t)y)=tJH(x)+(1-t)JH(y).
\]
This directly verifies that the degree assumption concerns the spatial
variables, not the action parameter.

For an elementary comparison, take arbitrary \(f,g\in\mathbb C[a]\),
with \(g\ne0\), and put
\[
E=\partial_s+f(a)\partial_y+s\,g(a)^2\partial_z
\quad\text{on }\mathbb C[a,s,y,z].
\]
This triangular LND has slice \(s\), and its exact flow is
\[
\Phi_t(a,s,y,z)=
\left(a,s+t,y+t f(a),z+t s g(a)^2+\frac{t^2}{2}g(a)^2\right).
\]
Consequently \(E^3(a,s,y,z)=0\) and
\(E^2(a,s,y,z)=(0,0,0,g(a)^2)\), although the ordinary degrees of its
coefficients are unbounded as \(f,g\) vary. This is our direct
calculation, not an example attributed to de Bondt. It has the invariant
coordinate \(a\), so it is not a counterexample to recognition.

## 6. What actually closes the current quadratic branch

The project branch has the additional relations
\(E(x_4)=\lambda g\), \(\lambda\in\mathbb C^*\), and \(c_4=0\).
They permit the polynomial shear
\[
y_i=x_i-\frac{c_i}{2\lambda^2}x_4^2,
\qquad
x_i=y_i+\frac{c_i}{2\lambda^2}y_4^2.
\]
Since \(E^2(x_4^2)=2\lambda^2g^2\), all \(E^2y_i\) vanish.
The shear preserves the three good coordinate partials; the separate
commutator calculation verifies that the fourth also becomes good.
Thus the previously established height-eight result applies. This is
the explicit proof in
[the power-law pass](height-nine-power-law-pass.md), not an application
of an unverified general theorem about time-degree-two actions.

No additional broad search was performed for this addendum.
