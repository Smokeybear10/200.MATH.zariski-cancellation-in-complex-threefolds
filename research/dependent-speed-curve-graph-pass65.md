# A speed curve gives an actual one-parameter quadratic graph

The rank-one-speed branch can be recognized when its displayed leading
fields have joint rank two and their actual bad projection is transverse.
The two speeds do not need to be algebraically independent. Their
nonconstant projective direction supplies a different basis for the
Schur calculation, and every varying graph coefficient belongs to one
rational function field. The determinant and actual-generation argument
then extracts an invariant ambient coordinate or an explicit affine slice.

The transverse graph theorem is followed by a rank-one-projection
corollary. Together they recognize the dependent-defect speed-curve
sector whenever the joint leading rank is at most two. They do not
close every rank-one-speed instance, every two-quadratic frame, or
general cancellation.

## 1. Actual hypotheses and the localized chart

Let \(k=\mathbb C\), and let
\[
B=k[Q_1,Q_2,X,Y]=A[s_*],\qquad
E(s_*)=1,\quad A=\ker E,
\]
where \(E\) is a polynomial LND. Assume
\[
\operatorname{ad}_E^2\partial_{Q_i}=0\quad(i=1,2),
\qquad
\operatorname{ad}_E^3\partial_X
=\operatorname{ad}_E^3\partial_Y=0,
\]
\[
E^3(Q_1,Q_2,X,Y)=0,\qquad E^2X=E^2Y=0.
\tag{1}
\]
Write \(W_i=[E,\partial_{Q_i}]\) for the good tops and
\(V_X,V_Y\) for the bad second adjoints. The actual conjugated
columns make these leading fields commuting LNDs, and make them
annihilate the bad speeds and highest vector, as in the
[degree-two coefficient proof](two-quadratic-degree-two-pass42.md).
Put
\[
v=\binom f g=\binom{EX}{EY},\qquad
h=E^2\binom{Q_1}{Q_2}.
\]
Assume the speeds have Jacobian rank one and the displayed fields have
joint rank exactly two:
\[
\operatorname{rank}\operatorname{Jac}(f,g)=1,\qquad
\operatorname{rank}_{\operatorname{Frac}B}
\{E,W_1,W_2,V_X,V_Y\}=2.
\tag{2}
\]
Choose an actual leading LND \(D\) independent of \(E\).
Its restriction to \(A\) is nonzero. The inherited
[intrinsic quotient theorem](intrinsic-quotient-surface-pass.md)
gives
\[
C=\ker E\cap\ker D\simeq k^{[2]},\qquad
L=\operatorname{Frac}C,\qquad B\cap L=C.
\tag{3}
\]
The premise is the original polynomial cylinder, not an assumed
polynomial presentation of \(A\). Every displayed leading field
annihilates \(C\), since its generic direction lies in the span of
\(E,D\).

The local-slice theorem, followed by integration of the vertical
coefficient of \(D\), supplies the actual invariant localization
\[
B\otimes_C L=L[r,t],\qquad E=\partial_t,\qquad D=\partial_r.
\tag{4}
\]
No polynomial coordinate claim on the unlocalized \(B\) follows.
Write the original coordinates there as
\[
\binom X Y=q(r)+tv,\qquad
\binom{Q_1}{Q_2}=X_0(r)+tP(r)+\tfrac12t^2h,
\tag{5}
\]
with \(q,X_0,P\in L[r]^2\) and \(v,h\in L^2\).
The final additional hypothesis is
\[
\det[q_r\mid v]\ne0.
\tag{6}
\]
Equivalently the projection of the actual two-dimensional distribution
spanned by \(E,D\) to \(X,Y\) has rank two. It does not mean the
two defects themselves are independent.

**Theorem.** Under (1)--(6), \(A\simeq k^{[3]}\).

## 2. A rational parameter for the speed direction

If \(f,g\) have constant projective direction, a nonzero complex
linear form in \(X,Y\) is killed by \(E\). It is an actual ambient
coordinate, and the sliced Dedekind-base theorem recognizes \(A\).[^dedekind]
Hence assume the projective direction is nonconstant.

Because \(f,g\) have transcendence degree one in the rational
two-field \(L\), choose a nonzero \(k\)-derivation \(\mathscr H\)
of \(L\) killing them. Its constant field has transcendence degree
one: two independent constants would make \(\mathscr H\) vanish
on an algebraic separable extension, whereas a nonconstant speed
supplies the lower bound. Generalized Lüroth gives
\[
\ker_L\mathscr H=k(u)
\tag{7}
\]
for an actual rational \(u\in L\).[^luroth]
Choose \(w\in L\) transcendental over \(k(u)\), and normalize
\(\mathscr H\) by its nonzero value on \(w\). Then
\(\mathscr H=\partial_w\), while the commuting \(\partial_u,\partial_w\)
extend uniquely from \(k(u,w)\) to the finite separable field \(L\).
In particular \(\ker_L\partial_w=k(u)\).

The parameter \(u\) need not be a polynomial or an ambient coordinate.
The speed vector is a rational vector \(v(u)\in k(u)^2\), with
\[
\det[v\mid v_u]\ne0,\qquad
v_{uu}=a_0(u)v+b_0(u)v_u.
\tag{8}
\]
The determinant is nonzero precisely because the projective direction
is nonconstant in characteristic zero.

## 3. The actual good columns force the first integration

Subscripts \(u,w\) initially mean base differentiation fixing \(r,t\).
Let
\[
U=[\,\partial_{Q_1}(u,w)^{\mathsf t}
       \mid\partial_{Q_2}(u,w)^{\mathsf t}\,].
\]
These entries belong to \(L[r]\): the original partials extend
by the quotient rule to the invariant localization, and
\(E(\partial_{Q_i}b)=W_i b=0\) for every \(b\in L\).
Put \(M=[q_r\mid v]\). Applying the actual good partials first
to \(X,Y\), then to \(Q_1,Q_2\), gives the exact Schur identity
\[
K(t)U=I,\qquad
K(t)=(X_0)_{(u,w)}+tP_{(u,w)}
+\tfrac12t^2h_{(u,w)}
-[X_{0,r}+tP_r\mid P+th]M^{-1}(q_{(u,w)}+t v_{(u,w)}).
\tag{9}
\]
Thus \(U\) is invertible and \(K(t)=U^{-1}\) is independent of \(t\).
This identity is obtained from actual coordinate partials, not
postulated for a rational graph.

Use the basis (8) to write, uniquely,
\[
q(r)=a(r)v+b(r)v_u,\qquad a,b\in L[r].
\]
Condition (6) makes \(b_r\ne0\). The \(t^2\) coefficient of (9)
first gives \(h_w=0\), and its other column gives
\[
P_r-a_rh=\tfrac12 b_r h_u.
\]
Integration in the original polynomial variable \(r\) yields
\[
h\in k(u)^2,\qquad
P=ah+\tfrac12 b h_u+k,\qquad k\in L^2.
\tag{10}
\]
At this point \(k_w=0\) has not yet been proved.

## 4. The second integration and the true generic graph

Put
\[
y=a(r)+t,\qquad z=b(r),\qquad
Z=X_0-aP+\tfrac12 a^2h.
\]
Then in the original field,
\[
\binom X Y=yv+zv_u,\qquad
\binom{Q_1}{Q_2}=Z+y(\tfrac12zh_u+k)+\tfrac12y^2h.
\tag{11}
\]
The extension \(L(r)/L(z)\) is finite and separable. It is used
only for differentiation at fixed \(z\); no descent or coordinate
conclusion is inferred from finiteness. The derivative
\(\partial_z\) acts on \(L(r)\) by \(b_r^{-1}\partial_r\).

When \(X,Y\) are held fixed, differentiation of their first
expression in (11), using (8), gives
\[
y_u=-a_0z,\qquad z_u=-y-b_0z,\qquad y_w=z_w=0.
\tag{12}
\]
The base derivatives of the second expression in (11), with
\(X,Y\) fixed, are exactly the Schur matrix (9). They must
therefore be independent of \(t\), equivalently of \(y\),
over \(L(r)\).

The coefficient of \(y\) in its \(w\)-column gives \(k_w=0\).
Here the \(w\)-derivative of \(Z\) is taken at fixed \(z\).
The coefficient of \(y\) in its \(u\)-column is
\[
-Z_z-\tfrac12b_0zh_u+\tfrac12zh_{uu}+k_u-a_0zh.
\]
The \(y^2\) terms cancel exactly. It follows that
\[
k\in k(u)^2,\qquad
Z_z=\tfrac12z(h_{uu}-b_0h_u-2a_0h)+k_u.
\tag{13}
\]
Multiplying by \(b_r\) and integrating in the original \(r\),
not by assuming \(z\) is a coordinate, gives
\[
Z=\tfrac14z^2(h_{uu}-b_0h_u-2a_0h)+zk_u+\ell,\qquad \ell\in L^2.
\]
Consequently
\[
Q=\ell+\tfrac14z^2(h_{uu}-b_0h_u-2a_0h)
+zk_u+y(\tfrac12zh_u+k)+\tfrac12y^2h.
\tag{14}
\]
The variables \(y,z\) are \(k(u)\)-linear functions of \(X,Y\),
with coefficients in \(k(u)\), by (8),(11). Hence (14) says
\[
Q=\ell+S(u;X,Y),\qquad
S\in k(u)[X,Y]^2,\qquad S(u;0,0)=0.
\tag{15}
\]

All four original coordinate generators now belong to \(L[X,Y]\).
Actual generation in (4) therefore proves
\[
B\otimes_C L=L[X,Y].
\tag{16}
\]
This is the missing generation step. In particular the formerly
possibly higher-degree polynomial \(b(r)\) must be affine in \(r\),
because \(L[z]=\ker E=L[r]\) in (16). We do not use that consequence
before establishing (16).

The matrix \(Q_{(u,w)}\), at fixed \(X,Y\), has polynomial entries
in \(L[X,Y]\). Its inverse consists of the actual good partials
applied to \(u,w\), so has entries in the same ring by (16).
Thus
\[
\det Q_{(u,w)}\in L^*,\qquad
k(Q_1,Q_2,X,Y)=L(X,Y).
\tag{17}
\]

## 5. Recognition of a graph depending on one rational parameter

Here is the part of the [pass64 argument](actual-quadratic-graph-cancellation-pass64.md)
that needs no Euler weights. Set \(A_0=\ell_{(u,w)}\).
By (15),(17), it is invertible and
\[
Q_{(u,w)}=A_0+S_u(1,0),\qquad
(1,0)A_0^{-1}S_u=0.
\]
Every coefficient vector of \(S_u\) is therefore collinear with
\[
A_0\binom01=\ell_w\ne0.
\tag{18}
\]

If \(S_u\ne0\), swap rows so that a coefficient of \((S_1)_u\)
is nonzero. The ratio of the two coefficient derivatives gives
\[
\rho\in k(u),\quad (S_2)_u=\rho(S_1)_u,\quad
(\ell_2)_w=\rho(\ell_1)_w,\quad (\ell_1)_w\ne0.
\]
Since \(\ker\partial_w=k(u)\), put
\[
I=\ell_2-\rho\ell_1\in k(u),\qquad D_0=S_2-\rho S_1.
\]
Then
\[
Q_2=\rho Q_1+D_0+I,\qquad (D_0)_u=-\rho_u S_1.
\tag{19}
\]
The nonzero derivative \(\partial_wQ_1\) shows, by separability,
that \(Q_1\) is transcendental over \(k(u,X,Y)\).
For \(K=k(Q_1,X,Y)\), actual field generation gives
\[
K(Q_2)\subseteq K(u)\subseteq L(X,Y)=K(Q_2).
\]
Thus \(Q_2\), as a rational function of \(u\) over \(K\), has degree one.

Write \(D_0=\sum_{\nu\ne0}d_\nu(u)X^{\nu_1}Y^{\nu_2}\).
At each complex point of \(\mathbb P^1\), the pole order of
\(\rho Q_1+\sum d_\nu X^{\nu_1}Y^{\nu_2}+I\) is the maximum
of its coefficient pole orders. The distinct monomials in the
algebraically independent \(Q_1,X,Y\) prevent cancellation.
If \(\rho\) were nonconstant, the total degree-one pole divisor
would force it and the full expression to share one simple pole.
Every \(d_\nu\) would then have the form \(A_\nu+B_\nu\rho\)
with \(A_\nu,B_\nu\in k\). Differentiating (19) would force every
coefficient of \(S_1\) to equal \(-B_\nu\), contradicting
\((S_1)_u\ne0\). Therefore \(\rho\in k\).

Now \(D_0\in k[X,Y]\), and
\[
I=Q_2-\rho Q_1-D_0(X,Y)\in B\cap L=C.
\tag{20}
\]
This is an actual invariant ambient coordinate: its inverse
change is \(Q_2=I+\rho Q_1+D_0(X,Y)\).
The original sliced \(E\) is a \(k[I]\)-LND on \(k[I]^{[3]}\).
The established Dedekind-base theorem gives \(A=k[I]^{[2]}\).[^dedekind]

If instead \(S_u=0\), the graph has complex constant coefficients.
Then \(\ell=Q-S\in C^2\), and \(B=C[X,Y]\).
The original slice gives \((f,g)C=C\). Choose
\(a_1f+b_1g=1\) in \(C\) and set
\[
\sigma=a_1X+b_1Y,\qquad j=gX-fY.
\]
The exact inverses \(X=f\sigma+b_1j\), \(Y=g\sigma-a_1j\)
give \(A=C[j]\simeq k^{[3]}\). This proves the theorem.

## 6. The rank-one projection and the complete rank-at-most-two corollary

Return to the dependent/no-constant-relation hypotheses of
[the low-flow theorem](dependent-low-flow-pass65.md), with \(m=2\).
It proves \(E^2X=E^2Y=0\) before any assumption about the speeds.
Suppose the speed Jacobian has rank one and the joint leading rank
is at most two. A constant projective direction already supplies an
invariant ambient linear coordinate, so exclude it.

If the joint rank is one, both good tops are parallel to \(E\).
Their actual partials preserve \(\ker E\); the primitive same-kernel
conjugation argument in the low-flow theorem makes those good
partials commute with \(E\), giving recognition.

For joint rank two, obtain (3)--(5). Rank-two bad projection has
just been recognized. Suppose its rank is one. Choose the actual
leading field \(D_1=D\) used to construct chart (4). The polynomial field
\[
K=fD_1-(D_1X)E
\tag{21}
\]
is globally locally nilpotent, commutes with \(E\), and kills \(X,Y\).
Indeed in the chart (4) it is
\(f\partial_r-q_1'(r)\partial_t\), a nonzero triangular LND.
Injective localization proves local nilpotence on the original ring.
The relative UFD-plane theorem and the primitive two-quasi theorem,
applied exactly as in the low-flow proof, give either an invariant
ambient linear coordinate, or
\[
\ker K=k[v_0,X,Y],\qquad
C=k[v_0,j],\qquad j=q_0(v_0)X-p_0(v_0)Y,
\]
\[
f=d(v_0,j)p_0(v_0),\qquad
g=d(v_0,j)q_0(v_0),\qquad (p_0,q_0)=k[v_0].
\tag{22}
\]
These established classification inputs are applied to the actual
relative plane \(B=k[X,Y][Q_1,Q_2]\) and then its actual polynomial
three-ring kernel, with primitive division before the second theorem.
Their hypotheses do not require algebraic independence of \(f,g\).
The nonconstant ratio \(g/f=q_0/p_0\) suffices to give
\(q_0'p_0-p_0'q_0\ne0\). No claim that \(d_j\ne0\) is needed.

Let \(H=h_1\partial_{Q_1}+h_2\partial_{Q_2}\ne0\).
The actual flow identity gives
\[
[E,H]=-\tfrac12(fV_X+gV_Y),\qquad [E,[E,H]]=0.
\tag{23}
\]
The bracket \([E,H]\) kills \(C\). For \(c\in C\), therefore \(E(Hc)=0\).
Differentiating the actual expression for \(j\) in (22), then applying
\(E\), gives
\[
0=d(q_0'p_0-p_0'q_0)H(v_0).
\]
The coefficient is nonzero, so \(H(v_0)=H(j)=0\), hence \(H(C)=0\).
Since \(h_i\in C\), this makes \(H\) a nice LND.

Both \(H\) and \([E,H]\) belong to the generic two-plane annihilating
\(C\), and have zero bad components. Rank-one bad projection makes
its good-output intersection one-dimensional. Thus \([E,H]=aH\)
over the fraction field. Divide \(H\) by the invariant gcd of
its coefficients. Primitivity makes \(a\) polynomial, and (23)
gives \(Ea+a^2=0\). Nonzero \(a\) would have
\(E^na=(-1)^n n!a^{n+1}\), contrary to local nilpotence. Thus
\([E,H]=0\).

Choose a nonzero good component \(h_b\). The genuine localized nice
LND \(H/h_b=\partial_b+(h_a/h_b)\partial_a\), with invariant
denominator \(h_b\), meets the exact
[one-good-output lemma](three-output-cubic-closure-pass41.md#1-a-recognition-lemma-requiring-only-one-good-partial).
The remaining actual good partial is still good. That theorem
recognizes the original kernel, with its previously audited
denominator and ambient-coordinate source gates.

Consequently, within the dependent-defect \(m=2\) speed-curve sector,
\[
\boxed{
\operatorname{rank}\{E,W_1,W_2,V_X,V_Y\}\le2
\quad\Longrightarrow\quad A\simeq k^{[3]}.\ }
\tag{24}
\]
The genuinely unclosed joint-rank possibility is three. All displayed
fields annihilate a nonconstant speed, so their joint rank cannot
exceed three. The corollary asserts no rank-three recognition.

## 7. What remains outside this result

The core graph proof requires the stated transverse bad projection.
Section 6 separately recognizes rank-one projection and joint rank
one. No proof that every dependent speed-curve instance has joint
leading rank at most two is included here.
In particular a rank-three leading distribution cannot be
silently replaced by a rank-two one while retaining that both
good tops kill the chosen invariant field.

The nonconstant projective direction is not algebraic independence
of the speeds. The parameter \(u\), auxiliary \(w\), and generic
fiber variables are not assumed global coordinates. All global
conclusions enter only through the actual original-generator equality,
the polynomial graph, and the final explicit coordinate inverse.

The new part is the two integrations (10),(13),(14) using
\(v,v_u\), followed by a source-gated one-parameter graph recognition.
The pole argument is inherited from passes63–64 with its exact
derivation hypotheses verified here, not claimed as a new argument.
General cancellation, the full supplied profile, novelty, human
expert review, and proof-assistant verification remain unestablished.

## Sources and verification boundary

The intrinsic quotient and local-slice inputs retain the full
assumptions and source audits of their linked original notes.
The main agent directly reread the Lüroth statement and attribution
in the retained de Bondt primary text. That passage refers to
classical proofs; no fresh reconstruction of those proofs is claimed.
The Dedekind theorem is the same one fully source-audited in pass64.

No finite symbolic calculation replaces the source inputs,
the actual-generator argument, or the all-degree pole reasoning.
Independent proof review and exact coefficient controls are recorded
in the [working audit](proof-audits-pass65-working.md) and
[captured verification](verification-pass65-working.json).
Geometry, Jet and General independently reconstructed the full core
proof. Geometry and General also reconstructed the complete added
rank-one-projection corollary. General's chart-label clarification
was incorporated before freezing: \(D_1\) is the same field used
for the displayed local-slice chart.

[^luroth]: M. de Bondt, [*Rational maps H for which K(tH) has transcendence degree 2 over K*](https://arxiv.org/pdf/1501.06046v4), Theorem 1.1 and attribution, PDF p. 4. It states the classical generalized Lüroth theorem for transcendence-degree-one subfields of a rational function field.
[^dedekind]: H. Derksen, A. van den Essen and P. van Rossum, [*The Cancellation Problem in Dimension Four*](https://www.researchgate.net/publication/228571174_The_cancellation_problem_in_dimension_four), Nijmegen Report 0022, Theorem 4.4, printed p. 8. Its base here is the actual one-variable ring \(k[I]\), not the intrinsic two-dimensional base \(C\).
