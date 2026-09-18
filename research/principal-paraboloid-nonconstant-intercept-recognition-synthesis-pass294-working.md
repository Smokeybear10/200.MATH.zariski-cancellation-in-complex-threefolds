# Recognition of the nonconstant-intercept zero-coupling branch

Working theorem: every actual principal1222 frame in the branch271
has a polynomial three-ring kernel. The extra branch conditions are
\(k_s=0\) and \(n_s\ne0\) in the selected chart264.
This note is an exhaustive composition of the retained working
proofs, not a new coefficient calculation.

The conclusion does not include the nonzero-coupling three-generator
sector \(k_s\ne0\), other full initial kernels, or arbitrary entry
into an exact1222 frame. In particular it does not establish general
1222 recognition or unrestricted cancellation.

## 1. Exact actual entry

Let
\[
\mathcal B=\mathbb C[X,Y,Z,W]=A[u],\qquad E=\partial_u,\qquad
A=\ker E,\qquad \deg_E(X,Y,Z,W)=(1,2,2,2).
\tag{1}
\]
Write \(a_0=EX\ne0\), \(b_Y=E^2Y/2\), \(b_Z=E^2Z/2\),
and \(b_W=E^2W/2\). Assume that the full weighted initial map
\[
(\mathsf X,\mathsf Y,\mathsf Z,\mathsf W)
\longmapsto(a_0T,b_YT^2,b_ZT^2,b_WT^2)
\]
has kernel \((\mathsf X^2\mathsf Z-\mathsf Y^2)\).
This is not an equation between the actual polynomial coordinates.

Use the exact selected chart of
[264](principal-one-affine-paraboloid-chart-pass264-working.md).
Thus \(t=b_Y/a_0^2\), \(s=b_W/a_0^2\) are algebraically
independent, \(b_Z/a_0^2=t^2\), and the literal \(Z\)-partial
has exact shift four. Its intrinsic nonzero LND \(N\) gives
\[
\begin{gathered}
L=\operatorname{Frac}\ker_A N,\qquad
[L:\mathbb C(t,s)]<\infty,\qquad
A\otimes_{\ker N}L=L[v],\qquad Nv=1,\\
K=\operatorname{Frac}A=L(v),\qquad
Na_0=Nt=Ns=0 .
\end{gathered}
\tag{2}
\]
The two original coefficient partials are those of this exact
finite extension and fix \(v\).

The literal fixed-\(X\) expressions are
\[
\begin{aligned}
Y&=y+\sigma X+tX^2,\\
Z&=z+(2t\sigma+k)X+t^2X^2,\\
W&=w+\theta X+sX^2,\\
K&=\mathbb C(y,z,w),\qquad L[y,z,w]=L[v],\\
\det\frac{\partial(Y,Z,W)}{\partial(t,s,v)}&=-a_0^4\in L^* .
\end{aligned}
\tag{3}
\]
The coefficient \(k\in L\) and the first-potential intercept
\(n\in L\) are the ones constructed in264. The branch assumption is
\[
\boxed{k_s=0,\qquad n_s\ne0.}
\tag{4}
\]
Subscripts in (4) refer to the original coefficient partial, not
a subsequently moved line parameter.

Under (1)--(4), the conclusion proved below, subject to the stated
retained working dependencies, is
\[
\boxed{A\cong\mathbb C^{[3]}.}
\tag{5}
\]

## 2. The plane reduction and the first exhaustive division

The complete source
[271](principal-paraboloid-nonconstant-intercept-plane-reduction-pass271-working.md)
replaces the coefficient parameter \(s\) by \(n\), retaining the
actual frame, selected derivation and field. Put \(H=s\) in the
new parameters. The resulting data include
\[
\begin{gathered}
F=\ker_L\partial_n,\qquad [F:\mathbb C(t)]<\infty,\qquad
[L:F(n)]<\infty,\qquad \ker(\partial_t|_F)=\mathbb C,\\
H_n\ne0,\qquad L[y,\sigma]=L[v],\qquad
\det\frac{\partial(Y,Z,W)}{\partial(t,n,v)}
=-a_0^4H_n\in L^* .
\end{gathered}
\tag{6}
\]
The equality \(L[y,\sigma]=L[v]\) is proved using the two literal
potentials and the actual return in (3). It is not an assumption
borrowed from the nonzero-coupling surface chart.

Let \(G\) generate the kernel of
\(L[U,P]\to L[v]\), \((U,P)\mapsto(y,\sigma)\).
It is a nonconstant irreducible polynomial. The remaining full
Jacobian gives a nonconstant primitive \(Q\) and
\[
Q(y,\sigma)=q_0,\qquad
Q-q_0=\eta G+G^2R,\qquad \eta\in L^*.
\tag{7}
\]
All coefficient derivatives precede formal evaluation in these
identities. The selected cofactor is an \(L[v]\)-unit, not a
claim about units in the original polynomial ring.

The parameter restriction
[277](principal-paraboloid-affine-parameter-restriction-pass277-working.md)
applies throughout (4), before a line/nonlinear split. It proves
\[
H=bn+c,\qquad b,c\in F,\qquad b\ne0 .
\tag{8}
\]
It does not at this stage make \(b\) complex or remove the finite
extension \(L/F(n)\).

There are exactly two possibilities for \(g=\deg G\).

* If \(g\ge2\), the completely read nonlinear synthesis
  [289](principal-paraboloid-nonlinear-recognition-synthesis-pass289-working.md)
  recognizes \(A\).
  It derives its own constant-slope and degree-at-most-four
  restrictions, then exhausts selected degrees \(2,3,4\).
  Its degree-two cases distinguish a quadratic whole primitive
  from a selected conic inside a quartic primitive. Its genuine
  quartic case uses the corrected281 source. None of those
  nonlinear restrictions is applied to a line here.
* If \(g=1\), proceed to Section3.

Thus the only cases still requiring composition are actual
projected lines.

## 3. Every projected line is covered

First suppose \(\sigma\in L\). Then (6) makes \(y\) affine and
nonconstant in \(v\). The actual-coordinate theorem
[278](principal-paraboloid-constant-second-line-recognition-pass278-working.md)
recognizes this case. That argument derives its own complex
coefficient restrictions and an invariant actual coordinate
monic in \(W\); it does not invoke289.

Now suppose \(\sigma\notin L\). Since \(g=1\) and the pair
generates the whole polynomial line, there are \(a,d\in L\) with
\[
G=U-aP-d,\qquad y=a\sigma+d,\qquad
L[\sigma]=L[v],\qquad \sigma_v\in L^* .
\tag{9}
\]
Here \(a\) is the projected slope, not the slice speed \(a_0\).
Use primes for the exact \(t\)-derivative on \(F\), and set
\(\ell=4a+k''\).

The complete line reduction
[288](principal-paraboloid-projected-line-polynomial-reduction-pass288-working.md)
has two branches.

If \(\ell=0\), its calibrated scalar forces \(k\) to be a
complex quadratic. Its specified actual affine change from272
gives \(k_*=0\) and \(y_*\in L\), retaining the selected partial,
fields, full initial relation and actual return. The retained
canonical-line theorem275 recognizes the kernel. This is the
explicit endpoint of288, Section3.

If \(\ell\ne0\), that same source proves all of
\[
\begin{gathered}
a\in F,\qquad d=rn+d_0,\qquad
r=a'/\ell\in F,\qquad d_0\in F,\\
b=\beta t+\beta_0\ne0,\qquad \beta,\beta_0\in\mathbb C,\qquad
T=pn+q,\quad p,q\in F,\\
K=F(n,\sigma),\qquad L=F(n).
\end{gathered}
\tag{10}
\]
The letter \(r\) in the remaining split always means the derivative
of the line intercept, \(d_n=a'/\ell\). It does not mean \(p'\),
which is denoted by \(r\) in some other endpoint sources.

There are now exactly three possibilities.

1. **\(\beta=0\).** Since \(b\ne0\), the slope \(b\) is a
   nonzero complex constant. The full line theorem
   [291](principal-paraboloid-constant-slope-line-recognition-pass291-working.md)
   recognizes every such line.
   In particular its argument includes the nonzero complex cubic
   \(k\) mode left open in288; this case is not silently reduced
   to \(k'''=0\).
2. **\(\beta\ne0\) and \(r=0\).** The exclusion
   [293](principal-paraboloid-constant-first-nonconstant-slope-exclusion-pass293-working.md)
   proves that no such actual frame exists.
   Its actual translation \(X_*=X+a\), with the complex constant
   \(a\), rebuilds a constant first intercept. The complete raw
   gradients then make \(w\) a degree-three polynomial in
   \(\sigma\) over \(F(z)\), whereas the actual field return also
   forces \(F(z,\sigma)=F(z,w)\). This contradiction does not
   assume \(F=\mathbb C(y_*)\).
3. **\(\beta\ne0\) and \(r\ne0\).** The moving-line theorem
   [292](principal-paraboloid-moving-line-pencil-recognition-pass292-working.md)
   recognizes the kernel.
   It uses the complete actual pencil return. Its zero-pencil-slope
   alternative proves stability of an actual polynomial three-ring
   by content and the global slice. Its nonzero alternative proves
   the exact curve-field equality, then uses monic division and a
   reduced invariant denominator to obtain an invariant actual
   coordinate. Rational coefficient-field membership alone is not
   substituted for either descent.

These cases exhaust (10). Together with \(\ell=0\) and
\(\sigma\in L\), they exhaust all lines in (9), and with Section2
they prove (5).

## 4. Field and dimension interpretation

The projected affine line in (6) is one-dimensional **over \(L\)**.
The exact field \(L\) has transcendence degree two over
\(\mathbb C\), and \(K=L(v)\) has transcendence degree three.
The ambient polynomial ring still has dimension four.
Classifying \(G\) is not a reduction of the original kernel ring
to a one-dimensional complex algebra.

Likewise \(L\) and \(F\) are initially specified finite extensions,
not freely chosen rational parameter fields.
The equality \(L=F(n)\) in (10) is asserted only in the line branch
where288 proves it by both actual field-return inclusions.
Other endpoints supply their own required field statements.
The synthesis does not infer global rationality of the chosen
intrinsic constant field from the final isomorphism \(A\cong
\mathbb C^{[3]}\).

All moves promoted to ambient coordinates in the endpoint proofs
are actual polynomial automorphisms with explicit polynomial
inverses, or actual coordinates supplied by the precisely stated
published preslice theorem. Where an invariant coordinate is used,
the slice gives regularity of \(A\), so the retained
Bhatwadekar--Gupta--Lokhande regular-kernel theorem has its required
hypotheses. A purely formal polynomial parametrization is not an
entry certificate for this synthesis.

## 5. Exact scope and evidence boundary

This composition recognizes exactly the actual branch (4) of264.
It does not include \(k_s\ne0\), where264 and290 still retain
three projected generators. It does not silently cover the other
zero-coupling condition \(n_s=0\), other initial kernels, other
selected shifts, or arbitrary original-coordinate entry.
Separately proved sectors can be composed only with their own
stated hypotheses.

The directly used final sources271,277,278,288,289,291,292 and293
were completely read before this composition. The new contribution
is the exhaustive case assembly; the previous coefficient proofs
and their historical dependencies remain identified working inputs,
not recursively certified results.

No saved checker was executed, imported, compiled or rerun for this
note. No earlier proof, packet or index was edited. This note does
not assert actual realizability of every case, historical novelty,
human-expert review, proof-assistant certification, or a solution
of unrestricted cancellation.

