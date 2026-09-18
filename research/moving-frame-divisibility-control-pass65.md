# An actual moving-top frame with a zero commuting repair

Canonical nonzero parameter motion occurs in a genuine sliced
polynomial four-ring with exact adjoint profile \((1,1,2,2)\) and
independent quadratic defects. In this family the proposed divisibility
\(g\mid T_\lambda g\) fails, while the canonical polynomial commuting
repair is zero.

The example is already recognized by an omitted good direction.
It is not an example in the remaining sector where no constant
good direction kills the parameter, and it is not a cancellation
counterexample.

## 1. Polynomial action and an actual coordinate inverse

Work in \(B=k[a,s,z,w]\), \(k=\mathbb C\). Choose any nonconstant
polynomial \(F\in k[a]\), and put
\[
g=F(a),\qquad h=F'(a),\qquad
E=\partial_s-g\partial_w.
\tag{1}
\]
This is a polynomial LND: it fixes \(a,z\) and translates \(s,w\)
by coefficients in \(k[a]\). It has the original slice \(s\).
More explicitly, with
\[
r=w+gs,\qquad w=r-gs,
\tag{2}
\]
one has \(B=k[a,z,r,s]\), \(E=\partial_s\) in these coordinates,
and
\[
\ker E=k[a,z,r].
\tag{3}
\]

Set
\[
A_0=a-\frac{zw}{3}+\frac{w^4}{24},\qquad
x_1=A_0+s,\quad x_2=A_0-s,\quad
x_3=z-\frac{w^3}{6},\quad x_4=w.
\tag{4}
\]
These are actual polynomial coordinates. Their inverse is
\[
w=x_4,\qquad z=x_3+\frac{x_4^3}{6},\qquad
s=\frac{x_1-x_2}{2},\qquad
a=\frac{x_1+x_2}{2}+\frac{x_3x_4}{3}+\frac{x_4^4}{72}.
\tag{5}
\]
Both compositions are the identity; the Jacobian determinant
of (4) in the order \((a,s,z,w)\) is \(-2\).
Neither a rational inverse nor a nonzero-Jacobian-only assertion
is being used.

## 2. All four actual adjoint columns

Write \(T_i=\partial_{x_i}\). Differentiating the actual inverse gives
\[
\begin{aligned}
T_1&=\tfrac12(\partial_a+\partial_s),&
T_2&=\tfrac12(\partial_a-\partial_s),\\
T_3&=\partial_z+\tfrac w3\partial_a,&
T_4&=\partial_w+\tfrac{w^2}{2}\partial_z+\tfrac z3\partial_a.
\end{aligned}
\tag{6}
\]
They therefore commute and are coordinate partials on the whole
original polynomial ring.

For the good columns,
\[
[E,T_1]=[E,T_2]=\frac h2\partial_w,\qquad
\operatorname{ad}_E^2T_1=\operatorname{ad}_E^2T_2=0.
\tag{7}
\]
For the bad columns, the exact first and second brackets are
\[
\begin{aligned}
W_3=[E,T_3]&=-\frac g3\partial_a+\frac{wh}{3}\partial_w,&
V_3=[E,W_3]&=-\frac{2gh}{3}\partial_w,\\
W_4=[E,T_4]&=-gw\partial_z+\frac{zh}{3}\partial_w,&
V_4=[E,W_4]&=g^2\partial_z.
\end{aligned}
\tag{8}
\]
Since \(Eg=Eh=0\), both \(V_i\) commute with \(E\).
As \(F\) is nonconstant in characteristic zero, \(g,h\ne0\).
Thus both first good brackets and both second bad brackets are
nonzero. The exact adjoint profile is
\[
(1,1,2,2),\qquad
\operatorname{rank}_{\operatorname{Frac}B}(V_3,V_4)=2.
\tag{9}
\]
The defects commute with one another. Also
\(\operatorname{rank}(E,V_3,V_4)=3\), since \(E\) has
\(\partial_s\)-coefficient one and their other independent
directions are \(\partial_w,\partial_z\).

## 3. The canonical top and preceding bad pair

The relevant coordinate iterates are
\[
\begin{aligned}
E^2x&=(g^2w^2/2,\ g^2w^2/2,\ -g^2w,\ 0),\\
E^3x&=(-g^3w,\ -g^3w,\ g^3,\ 0),\\
E^4x&=(g^4,\ g^4,\ 0,\ 0),\qquad E^5x=0.
\end{aligned}
\tag{10}
\]
Consequently this is the actual nonconstant high-top branch with
\[
m=4,\qquad c=(1,1,0,0),\qquad
E^mx=cg^m,\qquad
L_0E^{m-1}x=\lambda g^{m-1},\quad \lambda=(1,0).
\tag{11}
\]
In particular the canonical preceding bad vector is nonzero.
The bad partial below is exactly \(T_\lambda\), not an unrelated
choice of a coordinate partial.

Put \(\alpha=(m-1)/2=3/2\) and use the notation of
[the moving repair](moving-commuting-repair-pass46.md):
\[
T=T_c=T_1+T_2=\partial_a,\quad S=T_\lambda=T_3,\quad
U=[E,T]=h\partial_w,\quad W=W_3,\quad V=V_3.
\tag{12}
\]
The equations are
\[
Tg=h\ne0,\qquad [T,S]=0,\qquad
gU=-\alpha V,\qquad Wg=-\frac{gh}{2\alpha},\qquad
Eg=Ug=Vg=0.
\tag{13}
\]
But
\[
Sg=\frac{wh}{3},\qquad g\nmid Sg.
\tag{14}
\]
Indeed \(F(a)\) cannot divide \(wF'(a)\) in \(k[a,s,z,w]\):
comparison as polynomials in the independent variable \(w\)
would give \(F\mid F'\), contrary to their degrees.
For a concrete nonconstant-motion instance, take \(F=a^2+1\);
then \(Tg=2a\) and \(Sg=2aw/3\).

Thus (14) disproves automatic divisibility under the full
supplied adjoint profile, independent defect rank, actual slice,
and canonical nonzero preceding-bad hypotheses. It does not
disprove a divisibility statement with an additional hypothesis
excluding all omitted good directions.

## 4. The canonical commuting repair vanishes

The preceding polynomial from the actual bad coordinate is
\[
v=E^{m-2}x_3=-g^2w,\qquad
Ev=g^3,\qquad Uv=-g^2h.
\tag{15}
\]
It is exactly the required preceding-layer element; no replacement
by an arbitrary preslice is made. The normalizer and repair are
\[
Y=gT+2\alpha W=wh\partial_w,
\]
\[
\mathcal R=g^{m-2}Y+vU
=g^2wh\partial_w-g^2wh\partial_w=0.
\tag{16}
\]
The normalizer is not an LND, since
\(Y^n(w)=h^nw\ne0\) for every \(n\ge1\), or equivalently
its divergence is \(h\ne0\).
The repair is locally nilpotent only in the trivial sense that
it is zero. Hence this example does not refute local nilpotence
of the repair under the full moving-frame hypotheses. It does
refute automatic nonvanishing or a guaranteed new independent
direction from that displayed repair.

## 5. Exact applicability boundary

Despite canonical motion \(T_cg\ne0\), the other actual constant
good direction
\[
T_1-T_2=\partial_s
\tag{17}
\]
commutes with \(E\) and kills \(g\). Equivalently
\(T_1g=T_2g=h/2\), so the two good derivatives are complex-linearly
dependent. Before the constant mixing in (4), the good coordinate
\(s\) already exposed this direction.

The existing [omitted good-direction theorem](good-direction-recognition-pass46.md)
therefore recognizes this example, consistently with the explicit
kernel (3). It does not realize the remaining unrecognized
good-gradient sector.

The actual bad pair also satisfies \(E^2x_3=-g^2w\ne0\).
Its two speeds are not both \(E\)-invariant. Thus one cannot
apply the finite-degree Euler graph theorem to this unchanged
bad pair by simply enlarging the allowed graph degree.
This is a failure of an input hypothesis, not a counterexample
to [pass64](actual-quadratic-graph-cancellation-pass64.md).

All formulas here use an actual polynomial cylinder, its true
coordinate partials, and a two-sided polynomial inverse.
They are not a formal companion-matrix model. No unresolved-frame
realization, novelty, human expert review, formal verification,
or unrestricted cancellation result is claimed.

## 6. The exact obstruction to replacing \(F(a)\) by \(G(a,z)\)

Keep the same actual coordinates (4), but temporarily replace \(g\)
by a nonzero polynomial \(G(a,z)\), retaining
\(E=\partial_s-g\partial_w\). The slice, inverse and flow layers
remain valid because \(Eg=0\). This is a test of this explicit
family, not of every possible coordinate change.

The fourth column now gives
\[
[E,T_4]=-gw\partial_z+
\left(\frac{w^2G_z}{2}+\frac{zG_a}{3}\right)\partial_w,
\]
\[
\operatorname{ad}_E^2T_4
=g^2\partial_z-2gwG_z\partial_w,\qquad
\operatorname{ad}_E^3T_4=3g^2G_z\partial_w.
\tag{18}
\]
Thus its required third-adjoint vanishing holds if and only if
\(G_z=0\). A genuinely \(z\)-dependent choice does not remain
inside the two-quadratic profile.

In fact the canonical repair detects exactly this failure:
\[
W_3=-\frac g3\partial_a+
\left(G_z+\frac{wG_a}{3}\right)\partial_w,\quad
Y=(3G_z+wG_a)\partial_w,
\]
\[
U=G_a\partial_w,\quad v=-g^2w,\qquad
\mathcal R=3g^2G_z\partial_w
=\operatorname{ad}_E^3T_4.
\tag{19}
\]
Consequently this particular enlargement cannot obtain a nonzero
repair while retaining the fourth-column bound. This is an exact
family identity, not a general identification of the repair with
a third adjoint in arbitrary frames.

## Verification boundary

The written formulas hold for every nonconstant \(F(a)\).
A separate exact checker uses the concrete choice \(F=a^2+1\)
to verify the inverse, all four adjoint columns, canonical flow
layers, kernel coordinate change, failed divisibility and zero
repair. It also checks (18)--(19) at \(G=a^2+z+1\), where the
extra third adjoint is nonzero. Its finite checks do not replace
the written all-polynomial-family argument.

The first two-method run passed in 0.142 seconds, exit zero.
After the Section 6 addition, the same two methods passed in
0.155 seconds, exit zero. The affine agent independently read the
complete proof and checker, then reconstructed the final Section 6
delta and reran both final methods in 0.152 seconds, exit zero,
without a correction. No additional method is counted for the
assertion inside the same first test.
