# Exceptional divisors in the two-quadratic cancellation problem

The unrestricted complex threefold cancellation conjecture is not
proved here. The remaining supplied two-quadratic frame now has a more
explicit denominator problem. In its independent-defect degree-two
case, the two actual bad coordinates generate the entire generic fiber,
and the original good coordinates form a quadratic graph over them.
Its determinant actions commute globally. In the higher-degree case,
two preceding layers fit inside an actual polynomial two-ring, allowing
a smaller polynomial replica of the commuting repair.

A separate algebraic result shows that compatibility of two commuting
actions is detected at prime divisors of their invariant plane. There
cannot be an obstruction supported only at isolated points. This does
not eliminate the remaining common divisors. The dependent-defect
case also acquires an exhaustive univariate normal form, with a
divisibility obstruction to movement of its parameter.

## 1. Scope and established geometric input

The working cancellation question is
\[
A[s_*]\simeq\mathbb C^{[4]}
\quad\Longrightarrow\quad A\simeq\mathbb C^{[3]}.
\tag{1}
\]
Here \(A\) is a complex affine domain. This is the corrected
three-dimensional interpretation, not a confirmation of the field and
dimension intended in the original email. Its literal conclusion
\(X\simeq\mathbb A^1\) has the wrong dimension when \(r>1\).

Write \(B=A[s_*]\), \(E=\partial_{s_*}\). An LND is a derivation
for which every polynomial is killed by some iterate. It corresponds
to an algebraic additive-group action. A slice is a polynomial \(s\)
with \(Es=1\); it identifies \(B\) with \((\ker E)[s]\), but does
not by itself identify the kernel as a polynomial three-ring.

The supplied frame consists of actual polynomial coordinates
\(x_1,x_2,x_3,x_4\), with actual partials \(T_i=\partial_{x_i}\),
satisfying
\[
\operatorname{ad}_E^2T_1=\operatorname{ad}_E^2T_2=0,
\qquad \operatorname{ad}_E^3T_3=
\operatorname{ad}_E^3T_4=0.
\tag{2}
\]
No theorem here places every sliced LND into such a frame. Even full
recognition of (2) would leave that universal reduction unproved.

An important earlier theorem must already be used at the outset.
For every nonzero intrinsic LND \(D\) of \(A\),
\[
C:=\ker_A D\simeq\mathbb C^{[2]},\qquad
C\longrightarrow A\text{ is faithfully flat}.
\tag{3}
\]
The cylinder makes \(X=\operatorname{Spec}A\) smooth and contractible.
Its projection from affine four-space restricts dominantly to an affine
linear three-plane: choose a tangent complement to the projection's
one-dimensional kernel. Kaliman--Saveliev's quotient theorem then
identifies the invariant surface as an affine plane and gives nonempty
curve fibers. Miracle flatness supplies (3). A free intrinsic action
would moreover imply \(A\simeq\mathbb C^{[3]}\).[^1][^2]

This is an established input, not a new plane-recognition result.
The [common-base audit](research/heisenberg-common-base-pass44.md)
corrects the earlier roadmap: the unknown part is the inclusion
\(C\subset A\) and its exceptional fibers. Localizing a nonconstant
\(g\in C\) gives \(C_g\), an open plane with nonconstant units,
not another polynomial plane.

## 2. The actual bad coordinates generate the generic fiber

Assume the independent-defect degree-two residual of (2). Thus
\(E^3x=0\), the two defects \(V_i=[E,[E,T_i]]\), \(i=3,4\),
are independent, and the bad speeds
\(f=Ex_3\), \(g=Ex_4\) are algebraically independent.
The previous projection-rank exclusion gives rank two for
\(L_0[V_3(x)\mid V_4(x)]\), where \(L_0\) selects the last
two entries. In this section \(g\) is a speed, not the
higher-degree top parameter used later.

Let \(C\) be the common intrinsic leading kernel and
\(L=\operatorname{Frac}C\). The simultaneous local-slice chart is
\(B\otimes_C L=L[r,t]\), with
\(E=\partial_t\), \(V_3=\partial_r\), and
\(V_4=b_4\partial_r+c_4\partial_t\), where \(c_4\ne0\).
Put \(v=(f,g)^{\mathsf t}\). The actual generators have the form
\[
x_B=q(r)+tv,\qquad
x_G=X(r)+tP(r)+t^2h/2,
\tag{4}
\]
where \(x_B=(x_3,x_4)^{\mathsf t}\), \(x_G=(x_1,x_2)^{\mathsf t}\),
and \(h\in L^2\). Crucially,
\(L[x_G,x_B]=B\otimes_C L\), because these are the original
coordinate generators.

The matrix \(U=[T_1v\mid T_2v]\) is independent of \(t\).
Apply the good partials to (4), first solving the two bad-coordinate
equations and then differentiating the good coordinates. The resulting
Schur complement is the inverse of \(U\), so its coefficients of
\(t,t^2\) vanish. With base differentiation in \(f,g\), this yields
\[
P=\tfrac12h_vq+k,\qquad h_vv=2h,\qquad k_vv=k,
\tag{5}
\]
and, componentwise,
\[
X_i=\tfrac14q^{\mathsf t}\operatorname{Hess}(h_i)q
+(\nabla k_i)q+\ell_i.
\tag{6}
\]
The base derivatives extend uniquely to the algebraic field extension
\(L/\mathbb C(f,g)\), since characteristic is zero. They are not
being promoted to polynomial coordinate partials of \(B\).

Define the degree-at-most-two graph
\[
\mathcal Q_i(\xi)
=\tfrac14\xi^{\mathsf t}\operatorname{Hess}(h_i)\xi
+(\nabla k_i)\xi+\ell_i.
\tag{7}
\]
Expansion of (4)--(6) proves \(x_G=\mathcal Q(x_B)\). The
original-generator equality, not merely a nonzero Jacobian, now gives
\[
\boxed{B\otimes_C L=L[x_3,x_4],\qquad
A\otimes_C L=L[j],\quad j=gx_3-fx_4.}
\tag{8}
\]
Thus the bad pair is not a finite covering of the generic plane.
The transverse polynomial \(gq_1-fq_2\) has degree exactly one
in \(r\). The
[complete derivation](research/generic-bad-pair-pass44.md)
retains the inverse matrix and every coefficient comparison.

## 3. Determinant actions and the remaining coefficients

Both \(U\) and its inverse \(\mathcal Q_v\) belong to
\(\operatorname{Mat}_2(L[x_3,x_4])\); hence \(\det U\in L^*\).
Writing \(H=h_v\), the actual bad-projection identity simplifies to
\(L_0[V_3(x)\mid V_4(x)]=UH\). Therefore
\[
0\ne\Delta:=\det(L_0[V_3(x)\mid V_4(x)])\in C.
\tag{9}
\]
Here \(B\cap L=C\), since every polynomial in that intersection
is killed by the original and leading actions.

The polynomial determinant LNDs
\[
K_3=(V_4x_3)V_3-(V_3x_3)V_4,\quad
K_4=(V_4x_4)V_3-(V_3x_4)V_4
\tag{10}
\]
are exactly \(-\Delta\partial_{x_4}\) and
\(\Delta\partial_{x_3}\) on the whole generic fiber. Consequently
\[
[K_3,K_4]=[E,K_i]=0,
\qquad \Delta E=fK_4-gK_3,
\qquad K_3j=f\Delta,\quad K_4j=g\Delta.
\tag{11}
\]
Each satisfies \(K_i^3x_\ell=0\). This bounds its coordinate
flow, not all adjoints on the actual partials. The restrictions of
these two fields to \(A\) still have only one generic direction.

The coefficients have a fixed denominator bound. Applying two
determinant fields to a good coordinate puts every second derivative
of \(\Delta^2\mathcal Q_i\) in \(B\cap L=C\). Subtracting
these quadratic terms from its first derivatives, and then subtracting
the linear terms from \(\Delta^2x_i\), puts all coefficients in
\(C\). With \(P_i=\Delta^2\mathcal Q_i\), this gives
\[
B=C[x_3,x_4,P_1/\Delta^2,P_2/\Delta^2],\qquad
\deg_{x_3,x_4}P_i\le2,\qquad
B_\Delta=C_\Delta[x_3,x_4].
\]
This is an exact subring equality. Its two defining equations require
\(\Delta\)-saturation; discarding that saturation is not justified.

The original slice implies \((f,g)C_\Delta=C_\Delta\).
Choose \(\alpha f+\beta g=1\) there. Then
\(\sigma=\alpha x_3+\beta x_4\), \(j=gx_3-fx_4\)
are polynomial coordinates over \(C_\Delta\), with inverse
\(x_3=f\sigma+\beta j\), \(x_4=g\sigma-\alpha j\).
Thus \(A_\Delta=C_\Delta[j]\). The quotient has become an
explicit polynomial line over a specified open subset of the plane.

At a genuine coefficient pole \(\pi\mid\Delta\), multiplying
by its smallest clearing power and reducing gives a nonzero relation
of degree at most two between the bad coordinates in the generic
divisor fiber. Faithful flatness prevents a constant relation.
Factorial closure makes this fiber a domain. If at least one reduced
speed is nonzero, the bad-image kernel is a prime ideal of height one,
stable under the reduced translation. Its irreducible generator is
therefore an invariant polynomial \(r(\overline j)\), with
\(1\le\deg r\le2\). This describes only the bad-image subring,
not the entire fiber or its whole invariant field.

The [denominator proof](research/quadratic-graph-denominators-pass44.md)
shows that independence of the six quadratic monomials at every
prime factor of \(\Delta\) would remove all coefficients' poles
and prove \(A=C[j]\). That condition is sufficient, not automatic.
The actual linear or quadratic relations, and the zero-reduced-speed
case, remain to be handled.

## 4. Compatibility is detected at divisors

There is an all-degree algebraic reduction independent of the graph
calculation. Its invariant-subtraction mechanism is the published
Daigle--Kaliman plinth gcd argument, extended here from the class
\([1]\) to arbitrary cokernel classes.[^4]
Let \(R\) be a noetherian UFD, let \(A\) be a domain
faithfully flat over \(R\), and let \(D:A\to A\) be an
\(R\)-derivation with \(\ker D=R\). Set \(H=A/D(A)\).

**Coprime-annihilator lemma.** If nonzero coprime \(p,q\in R\)
both kill \(\xi\in H\), then \(\xi=0\).

Indeed, write \(Da=pf\), \(Db=qf\) for a representative \(f\).
Then \(qa-pb\in R\cap(p,q)A=(p,q)R\). Subtract suitable
\(\alpha,\beta\in R\) to obtain
\[
q(a-\alpha)=p(b-\beta).
\tag{12}
\]
Multiplication by \(q\) is injective on \(R/pR\), and remains
injective on \(A/pA\) by flatness. Thus \(a-\alpha=pt\), and
applying \(D\) gives \(f=Dt\). Coprime is sufficient; the
ideals \((p)\) and \((q)\) need not be comaximal.

For a torsion \(\xi\), take the gcd \(d\) of generators of
its nonzero annihilator. The remaining ideal has gcd one. Finite
prime avoidance provides two coprime members, so the lemma gives
\(d\xi=0\). It follows that
\[
\operatorname{Ann}_R(\xi)=dR,
\qquad
\xi=0\Longleftrightarrow
\xi_{(\pi)}=0\text{ for all irreducible }\pi\in R.
\tag{13}
\]
Finite generation is used for the annihilator ideal, not for the
possibly infinite module \(H\). This rules out a cyclic obstruction
supported only at an isolated intersection point.

If \(A\) contains \(\mathbb Q\) and \(D\) is a nonzero LND, a nonzero
plinth element \(p=Dr\in R\) gives \(A_p=R_p[r/p]\).
Polynomial integration makes \(D\) surjective there. Every class
of \(H\) is therefore torsion. If also \(\xi_g=0\), then
\[
\gcd_R(g,p)=1\quad\Longrightarrow\quad\xi=0.
\tag{14}
\]
Otherwise only the finitely many common prime factors require checking.

For commuting LNDs \(E,U\) on \(B=A[s_*]\), write
\(U=D+a_0\partial_{s_*}\), \(D\ne0\). An \(E\)-slice
\(s_*+f\) is killed by \(U\) exactly when \(Df=-a_0\).
The slice-independent obstruction is \([a_0]\in A/D(A)\).
The genuine plane and flatness in (3) make (13)--(14) applicable.
The [full support proof](research/compatible-slice-support-pass44.md)
includes both the localized high-degree application and countercontrols.

The divisorial qualification is necessary. On
\(A=\mathbb C[x,y,t]\), \(D=x\partial_t\), the class \([y]\)
has annihilator \((x)\). The commuting field
\(U=x\partial_t+y\partial_{s_*}\) admits the compatible local
slice \(s_*-yt/x\), but no global compatible slice. This is an
actual polynomial example, not a realization of every condition in (2).

### A sharp bound and a failed completion shortcut

The rank-two global Heisenberg normalizer gives more than an unspecified
power annihilator. Write \(U=D+bE\), \(D=\delta D_0\) with
\(D_0\) primitive, and suppose \([E,Y]=-gU\), \([Y,U]=0\).
Rank two and primitive saturation force
\(Y|_A=(r-g\delta s_*)D_0\) for some \(r\in A\).
Commutation gives \(D_0r=gb\), so
\[
\delta g[b]=0\text{ in }A/D(A).
\]
If \(D\) is primitive, the exact annihilator of \([b]\) divides
\(g\), including multiplicities. This bounds the obstruction,
but need not erase it.

For \(D=x\partial_y+2y\partial_z\), \(v=xz-y^2\), the
fields \(E=\partial_{s_*}\), \(U=D+E\),
\(Y=(y-xs_*)U\) satisfy these global Heisenberg equations.
The plinth is \(x\mathbb C[x,v]\), so \([U(s_*)]=[1]\)
is nonzero even at the generic point of \(x=0\). Nevertheless,
with \(c_k=\binom{2k}{k}/4^k\), the actual corrections
\[
f_N=-\sum_{k=1}^N c_k\frac{x^{k-1}yz^k}{v^k}
\quad\text{satisfy}\quad
Df_N=1-(2N+1)c_N(xz/v)^N.
\]
They give compatible slices modulo every power of \(x\), and a
compatible formal limit, but no polynomial solution at that prime.
The [height-one bound and countercontrol](research/heisenberg-height-one-bound-pass44.md)
prove both assertions in all orders. The example does not supply
\(U=[E,T_c]\) for the required actual constant partial. That
additional frame condition remains a possible source of rigidity;
formal correction alone cannot replace it.

## 5. Independent higher-degree preceding layers

Return to the independent-defect high-top branch. Its inherited
power law is
\[
E^mx=cg^m,\qquad z=E^{m-1}x,\qquad
L_0z=\lambda g^{m-1},\qquad 3\le m\le5.
\tag{15}
\]
Here \(c\) is a nonzero constant good vector, \(\lambda\ne0\)
is constant, and \(g\) is nonconstant and invariant. Put
\(b=L_0E^{m-2}x\). The full companion power \(M^{m-1}\)
has rank two, and its base columns contain
\(\operatorname{Jac}z\) and \((m-1)\operatorname{Jac}b\).
For \(\tau=z_j/c_j\), the two differentials \(d\tau,dg\)
span this row space. Thus
\(db=(\lambda/g)d\tau+\omega\,dg\).

The polynomial invariants \(g,z-c\tau,gb-\lambda\tau\)
jointly have transcendence degree one. Polynomial curve factorization
gives an actual \(u\in B\), not necessarily a coordinate.[^3]
Choose \(v=b_i/\lambda_i\) with \(\lambda_i\ne0\). The
intersection identity \(B\cap\mathbb C(u)=\mathbb C[u]\)
then gives univariate vectors \(F,L\) and a polynomial \(G\) with
\[
\boxed{g=G(u),\qquad z=cG(u)v+F(u),\qquad
b=\lambda v+L(u),\qquad Ev=g^{m-1}.}
\tag{16}
\]
Since \(Eu=0\), \(u,v\) are algebraically independent.
These two layers really lie inside the polynomial two-ring
\(\mathbb C[u,v]\subset B\). No ambient-coordinate conclusion
is included.

When \(T_cg=0\), retain the global Heisenberg fields
\(Y,V\), with \([E,Y]=aV\) central and \(a=(m-1)/2\).
The new \(v\) is killed by \(V\). Applying the compatible
projection to \(v/g^{m-2}\), a slice for \(E/g\), gives
\[
\mathcal R_1=g^{m-1}Y-a vV-(Yv)E
\in\operatorname{LND}(B),\qquad
[E,\mathcal R_1]=[V,\mathcal R_1]=0.
\tag{17}
\]
The old replica equals \(g\mathcal R_1+a r(u)V\) for a univariate
\(r\). Thus one power of \(g\) has been removed from the
explicit construction, but its generic rank is unchanged. The
[complete preceding-layer proof](research/independent-preceding-layer-pass44.md)
does not claim primitive freeness or removal of \(g=0\).

## 6. Dependent defects: two exhaustive curve forms

If the bad defects are dependent, write
\(V_3=aD,V_4=bD\), with primitive LND \(D\), invariant
multipliers \(a,b\), and no constant relation between them.
The nonconstant high-top case has \(m\in\{3,4\}\),
\(E^mx=cq\), and the inherited relations
\[
Dz=ct,\qquad (0,0,a,b)z=qr,\qquad
[E,T_c]=-\tfrac{m-1}{2}rD.
\tag{18}
\]
The zero-multiplier branch is already recognized. For \(r\ne0\),
the original and primitive actions are independent.

The row nesting of the actual five-dimensional companion proves
\(\operatorname{rank}\operatorname{Jac}(z-c\tau,q)=1\).
The same curve-factorization theorem gives
\(q=Q(u)\), \(z-c\tau=K(u)\), \(Eu=Du=0\).
The full variable-row differential becomes
\[
aA_3(u)+bA_4(u)=0,
\qquad A_i=mQK_i'-(m-1)Q'K_i.
\tag{19}
\]

If both \(A_i\) vanish, comparing root multiplicities gives
\(q=g^m\), \((z_3,z_4)=\lambda g^{m-1}\), and
\(\lambda_3a+\lambda_4b=gr\). The earlier global Heisenberg
repair transfers because the combined defect is nonzero. At
\(T_cg=0\), its eligible rank-three branch is recognized by the
already established commuting-coordinate criterion. Nonconstant
\(T_cg\) and the remaining rank-two case are not recognized.

If the \(A_i\) do not both vanish, both are nonzero and their
projective ratio is nonconstant. Divide by their gcd and write
\(a_0=-A_4/\gcd(A_3,A_4)\),
\(b_0=A_3/\gcd(A_3,A_4)\). With
\(R=a_0K_3+b_0K_4\), cancel the full gcd of \(Q,R\) to
obtain coprime \(Q_1,R_1\). Two univariate Bezout identities give
the actual polynomial normal form
\[
a=H_1Q_1(u)a_0(u),\quad
b=H_1Q_1(u)b_0(u),\quad r=H_1R_1(u),
\qquad(a,b,r)=H_1B.
\tag{20}
\]
Repeated factors are retained. The principal ideal here is proved
by Bezout identities, not inferred from a coefficient gcd.

The full trace identity gives
\(Q'(u)T_cu=\tfrac{m(m-1)}2H_1R_1(u)t\). If
\(R_1\nmid Q'\), a nonconstant remaining factor of \(R_1(u)\)
divides its own derivative under the actual constant partial
\(T_c\). Local nilpotence forces that derivative to vanish. Hence
\[
R_1\nmid Q'\quad\Longrightarrow\quad T_cu=0,\quad Dz=0.
\tag{21}
\]
The converse is not asserted. Nor is every univariate normal form
an actual action satisfying (2). The
[dependent preceding-curve proof](research/dependent-preceding-curve-pass44.md)
separates those necessary equations from realizability.

There is also a conditional recognition within the zero-motion rotating
branch. The good leading fields \(W_i=[E,T_i]\), \(i=1,2\),
are global LNDs. Commutation of the conjugated good partials gives
\([W_i,rD]=0\). Primitivity of \(D\) makes \(W_i(r)/r\)
polynomial, and LND divisibility then forces \(W_i(r)=0\), hence
\([W_i,D]=0\). Highest coefficients give \(W_i(u)=0\).
Thus \(E,D,W_1,W_2\) commute and fix \(u\).

When \(T_cu=0\), joint rank three gives a commuting independent
triple fixing a polynomial that omits an actual constant coordinate
direction. The established coordinate criterion recognizes \(A\).
In particular this applies when \(R_1\nmid Q'\) and that rank
is three. Only joint rank two remains within this zero-motion branch.
The [good-top recognition proof](research/dependent-good-top-recognition-pass44.md)
does not assert that the rank condition or zero motion is automatic.

## 7. What remains necessary for cancellation

The current reductions expose several concrete obligations. The
degree-two graph needs global coefficient descent or a controlled
analysis of its exceptional fibers. The higher-degree branch needs
control at the common divisors of its top parameter and intrinsic
plinth, an independent intrinsic action, or a proof that a primitive
intrinsic action is free. The dependent rotating branch needs additional
actual-frame equations beyond its necessary curve identities.

A polynomial invariant base does not supply these conclusions.
For example, the primitive triangular action
\(x\partial_y+2y\partial_z\) on a polynomial three-ring has
invariant plane \(\mathbb C[x,xz-y^2]\), but a nonempty fixed
locus and disconnected or nonreduced special fibers. Its invariant
inclusion has no algebra retraction. These failures already occur
when the threefold itself is affine space.

The full supplied profile (2) therefore remains incomplete, and
unrestricted frame existence is a separate unresolved quantifier.
The earlier all-profile bound \(H\le9\) and the complete supplied
profiles \((1,1,1,3)\), \((0,2,2,2)\) are unchanged. Finite
identity controls do not replace these missing all-degree arguments.

The proofs above support restricted deductions, not an unrestricted
solution or a historical novelty claim. The established geometric
inputs must retain their exact hypotheses. In particular, the
withdrawn *Affine threefolds admitting Ga-actions* preprint is not
used as a recognition theorem.[^5]

## Sources

[^1]: Shulim Kaliman and Nikolai Saveliev,
[*C+-actions on contractible threefolds*](https://www.math.miami.edu/~kaliman/library/KaSa.michigan.2004.quotient.pdf),
Lemma 2.1, Theorem 2.7 and Corollary 2.8. The detailed applicability
argument is in the earlier [intrinsic quotient proof](research/intrinsic-quotient-surface-pass.md).

[^2]: The Stacks Project,
[Lemma 10.128.1, Tag 00R4](https://stacks.math.columbia.edu/tag/00R4),
miracle flatness. The local base is regular, the local total ring is
Cohen--Macaulay, and the fiber dimension equality is verified.

[^3]: Michiel de Bondt,
[*Rational maps H for which K(tH) has transcendence degree 2 over K*](https://arxiv.org/pdf/1501.06046v4),
Corollary 3.2 with proof and Lemma 3.3, PDF pp. 20--21.
Its conclusion is a polynomial parameter in the original ring,
not an ambient coordinate.

[^4]: Daniel Daigle and Shulim Kaliman,
[*A Note on Locally Nilpotent Derivations and Variables of k[X,Y,Z]*](https://www.math.miami.edu/~kaliman/library/canada.daigle-kaliman.pdf),
*Canadian Mathematical Bulletin* 52(4) (2009), 535--543,
Theorem 1.5 and its gcd proof on printed p. 539. The preceding
[intrinsic plinth note](research/intrinsic-plinth-boundary-pass27.md)
already records that published mechanism for the plinth.

[^5]: R. V. Gurjar, M. Koras, M. Miyanishi and P. Russell,
[*Affine threefolds admitting Ga-actions*, arXiv:1502.01849v2](https://arxiv.org/abs/1502.01849v2),
withdrawal record of February 11, 2015. The record attributes withdrawal
to an erroneous proof and a false statement of Theorem 3.1 in that version.
This record is a source-exclusion notice, not a mathematical dependency.
