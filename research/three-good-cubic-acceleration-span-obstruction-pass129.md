# Cubic acceleration outside the fixed-good quadratic span

An actual unit, nonconical, rank-two three-good quadratic frame need
not have acceleration in the constant span of the six products of
its good speeds. The same example disproves first-commutator
preservation of the intrinsic speed plane even after requiring
that no fixed-good polynomial shear lower the bad coordinate's
time degree. Its first commutator is itself locally nilpotent.

This is an explicit translation with polynomial inverse formulas,
not a cancellation counterexample or a globally minimal frame.
The general divided-difference construction below supplies the
inverse and adjoints uniformly; a cubic specialization gives the
claimed quadratic obstruction. Files through128 are unchanged.

## 1. A polynomial divided difference and an actual frame

Let \(B=\mathbb C[a,b,v,u]\), \(A=\mathbb C[a,b,v]\), and
\(E=\partial_u\). For a polynomial
\(F(t)=\sum_{j=0}^d f_jt^j\in\mathbb C[t]\), define
\[
\Delta_F(a,v,u)=
\sum_{j=1}^d f_j\sum_{k=1}^j
 \binom jk v^{j-k}a^ku^{k-1},
\qquad
u\Delta_F(a,v,u)=F(v+au)-F(v).
\tag{1}
\]
In particular \(\Delta_F\) is polynomial on \(u=0\).
The quotient notation for this divided difference never means
localizing the original ring.

Define the ordered original frame by
\[
X=u,\qquad Y=v+au,\qquad
Z=a-F(v)+bu,\qquad W=b+\Delta_F(a,v,u).
\tag{2}
\]
Its polynomial inverse is
\[
\begin{gathered}
u=X,\qquad a=Z-XW+F(Y),\\
v=Y-aX,\qquad b=W-\Delta_F(a,v,X).
\end{gathered}
\tag{3}
\]
Every expression in (3) is polynomial in \(X,Y,Z,W\), by (1).
For the forward substitution, (1) gives
\[
Z-uW+F(Y)
=a-F(v)+bu-u(b+\Delta_F)+F(v+au)=a.
\]
The remaining three inverse identities then follow directly.
For the other order, define \(u,a,v,b\) by (3).
The formulas for \(X,Y,W\) in (2) recover themselves. Also
\[
a-F(v)+bX
=a-F(v)+XW-X\Delta_F(a,v,X)
=a+XW-F(Y)=Z.
\]
This proves both inverse orders, including the fiber \(X=0\).
Thus \(B=\mathbb C[X,Y,Z,W]=A[u]\) is an actual polynomial
coordinate frame, with the original coordinate slice \(X=u\).

## 2. The selected rank-two hypotheses

The good coordinates are \(X,Y,Z\), with speeds
\[
\begin{gathered}
EX=1,\qquad EY=a,\qquad EZ=b,\qquad
E^2X=E^2Y=E^2Z=0,\\
\mathbb C[EX,EY,EZ]=\mathbb C[a,b],\qquad
(EX,EY,EZ)B=B,\\
\det[\mathbf a,\partial_a\mathbf a,\partial_b\mathbf a]=1,
\qquad \mathbf a=(1,a,b)^t.
\end{gathered}
\tag{4}
\]
The independent adapted variables \(a,b\) show that the speed
rank is exactly two. The speeds have constant linear span three:
an identity \(\lambda_0+\lambda_1a+\lambda_2b=0\) forces
all three constants to vanish. Their nonconical determinant
is an actual constant unit, not merely a nonzero rational function.

For \(d\ge2\) and \(f_d\ne0\), (1) shows that the exact
\(E\)-degree of \(W\) is \(d-1\), with leading coefficient
\(f_da^d\). If \(F\) has degree at most one, \(W\) is invariant.
The cubic case below has bad degree exactly two.

## 3. The original bad partial and its leading intrinsic action

Let \(T=\partial_W\) hold \(X,Y,Z\) fixed. Formula (3) gives
\[
\begin{gathered}
Tu=0,\qquad Ta=-u,\qquad Tv=u^2,\qquad
Tb=1+uF'(v),\\
T=-u\partial_a+(1+uF'(v))\partial_b+u^2\partial_v,\\
Q=[E,T]=-\partial_a+F'(v)\partial_b+2u\partial_v,\qquad
R=\frac12[E,Q]=\partial_v,\qquad [E,R]=0,\\
N=[u^2]T|_A=\partial_v,\qquad
S=\ker_A N=\mathbb C[a,b].
\end{gathered}
\tag{5}
\]
For the only less immediate derivative, apply \(T\) to
\(u\Delta_F=F(Y)-F(v)\). Since \(Tu=TY=0\) and
\(Tv=u^2\), this gives \(uT\Delta_F=-u^2F'(v)\).
Cancellation in the polynomial domain yields
\(T\Delta_F=-uF'(v)\), hence the displayed \(Tb\).
No derivation is localized or inferred from a rational inverse.

The \(u\)-filtration shift of \(T\) is exactly two, for every
\(F\): its \(v\)-coefficient is \(u^2\), its other coefficients
have degree at most one, and \(Tu=0\).
The selected adjoint degree is also exactly two.
Here the intrinsic \(N\) and the half second adjoint \(R\)
coincide after extending \(N\) to kill \(u\).
The equality and the actual kernel \(S\) are explicit.

Both \(T\) and \(E\) are coordinate partial LNDs.
The first commutator \(Q\) is also locally nilpotent:
it kills \(u\), sends \(v\) to \(2u\), sends \(a\) to \(-1\),
and sends \(b\) to \(F'(v)\). Repeated \(Q\)-derivatives of
each generator terminate, since successive derivatives of
the polynomial \(F'\) terminate. In fact \(Q(-a)=1\),
so \(Q\) has an actual slice. The intrinsic \(N=\partial_v\)
also has the actual slice \(v\).

Nevertheless, if \(F''\ne0\), then
\[
\begin{gathered}
Q(a)=-1,\qquad Q(b)=F'(v)\in A,\qquad
N(Q(b))=F''(v)\ne0,\qquad Q(S)\not\subset S,\\
D_1=[u]T|_A=-\partial_a+F'(v)\partial_b,\qquad
[N,D_1]=F''(v)\partial_b,\qquad
R^2Z=-F''(v)\ne0.
\end{gathered}
\tag{6}
\]
The bracket in (6) is not a multiple of \(N\): it does not
kill \(b\in S\). Thus the normalizer criterion in
[the rank-two boundary128](three-good-rank-two-commutator-instability-pass128.md)
fails even when both the middle commutator and the highest
intrinsic action are LNDs with slices. These properties do
not supply the missing stability.

## 4. Cubic specialization and the constant-span obstruction

Take \(F(t)=\gamma t^3+\beta t^2+\alpha t+\delta\), where
\(\gamma\in\mathbb C^*\). Then
\[
\begin{gathered}
W=b+\gamma(3av^2+3a^2vu+a^3u^2)
       +\beta(2av+a^2u)+\alpha a,\\
q=E^2W=2\gamma a^3\ne0,\qquad E^3W=0,\qquad q\in S,\\
\operatorname{span}_{\mathbb C}
 \{a_i a_j:1\le i\le j\le3\}
=\operatorname{span}_{\mathbb C}\{1,a,b,a^2,ab,b^2\},
\qquad q\notin
 \operatorname{span}_{\mathbb C}\{1,a,b,a^2,ab,b^2\}.
\end{gathered}
\tag{7}
\]
Nonmembership follows from the algebraic independence of
\(a,b\): the nonzero monomial \(a^3\) is not a polynomial
of total degree at most two in them. This acceleration is
part of the actual inverse-verified frame, unlike an
unrealized coefficient-rank control.
It satisfies all the unit, rank-two, full-span, nonconical,
nonconstant-quadratic hypotheses in (4) and (7).
The unit good-speed ideal makes ideal membership of \(q\)
or \(q^2\) automatic; it does not imply this constant-span
membership.

For completeness, nonremovability by a fixed-good shear can
be checked here without any global recognition theorem.
If \(G\in\mathbb C[X,Y,Z]\) is nonconstant of total degree
\(m\), its highest \(u\)-coefficient after (2) is
\(G_m(1,a,b)\). This coefficient is nonzero: substitution
\((X,Y,Z)=(1,a,b)\) is injective on homogeneous polynomials
of any fixed degree. Indeed distinct monomials of that
degree become distinct monomials in \(a,b\).
Consequently
\[
\deg_E G=\deg G,\qquad
\deg_E(W-G)\ge2
\quad\hbox{for every }G\in\mathbb C[X,Y,Z]
\quad(\deg F=3).
\tag{8}
\]
To prove the second assertion, a \(G\) of degree greater
than two has higher \(E\)-degree than \(W\). A \(G\) of
degree at most two has
\(E^2G=2G_2(1,a,b)\), which cannot equal \(q\) by (7).
The triangular change \(W\mapsto W-G\) is always an actual
polynomial coordinate change; (8) rules out its lowering
the bad time degree. Thus the example meets the additional
fixed-good-shear-minimality hypothesis left open by128.
Together with (6), it refutes first-commutator stability
under that added hypothesis as well.

## 5. The coordinate initial algebra is not the full graded ring

For \(F(t)=t^3/2\), the full associated graded ring of the
\(E\)-degree filtration is \(A[\tau]=\mathbb C[a,b,v,\tau]\),
where \(a,b,v\) have degree zero and \(\tau\) has degree one.
The subalgebra generated by the initials of the four
original coordinates is the image of
\[
\begin{gathered}
\mathbb C[\xi,\eta,\zeta,\omega]\longrightarrow
 \mathbb C[a,b,v,\tau],\\
(\xi,\eta,\zeta,\omega)\longmapsto
 (\tau,a\tau,b\tau,a^3\tau^2/2),\\
\ker=(2\xi\omega-\eta^3),\qquad
\operatorname{trdeg}_{\mathbb C}(\text{image})=3
 <4=\operatorname{trdeg}_{\mathbb C}\operatorname{gr}_E B.
\end{gathered}
\tag{9}
\]
The image has fraction field \(\mathbb C(a,b,\tau)\),
because its first three generators recover \(a,b,\tau\)
rationally. Its prime kernel therefore has height one.
The displayed polynomial is irreducible: as a polynomial
in \(\omega\), its two coefficients \(2\xi,-\eta^3\)
are coprime, and it is linear over the coefficient field.
It belongs to that kernel, proving the equality.

Assigning weights \(1,1,1,2\) to \(\xi,\eta,\zeta,\omega\),
this relation has weight three. Although it is linear in
\(\omega\), that coefficient is the nonunit \(2\xi\).
It is not a monic weight-two relation expressing the bad
initial as a constant quadratic form in the good initials.
The initial subalgebra has degree-zero part only
\(\mathbb C\), whereas the full graded ring has degree-zero
part \(A\). Neither polynomial generation by the original
coordinates nor the original slice \(X\) asserts generation
of the associated graded ring by their four initials.

## 6. What the example does and does not obstruct

For the simplest specialization \(F(t)=t^3/2\), one has
\(q=a^3\), \(N(Qb)=3v\), and the exact mixed-coordinate
identity \(2XW-Y^3=2Z-2a\).
Subtracting \(2Z\) recovers the invariant \(a\); then
(3) recovers \(v,b\).
This involves the old bad coordinate and a cubic expression.
It is not a fixed-good quadratic subtraction.

The original slice \(X=u\) and the inverse (3) already
recognize the action as a translation with kernel
\(\mathbb C[a,b,v]\). The adapted frame has time degrees
\((0,0,0,1)\), so this example is not a global minimum over
all coordinate frames. It does not address a conjecture
restricted to such global minima, show that every supplied
rank-two action is recognized, or establish unrestricted
frame entry or cancellation.

The proof uses displayed polynomial identities, not a Jacobian-only
inverse inference or a formal coefficient ansatz.
No historical novelty claim is made.

## 7. Comparison with published filtration criteria

Dasgupta and Lahiri's
[On image ideals of nice and quasi-nice derivations on R[X1,X2]](https://arxiv.org/html/2302.13787v6),
Section 3, constructs a filtration using known kernel generators
and generators representing the plinth ideal, as well as the original
coordinates. Lemmas 3.1--3.2 and Corollary 3.3 identify the relevant
filtration and image ideals under a proper-filtration or prime-top-ideal
hypothesis. Proposition 3.4 gives sufficient conditions for computing
that top ideal from selected generators.

These statements do not identify the algebra of only the four coordinate
initials with the full associated graded ring. In particular, they do
not force the first relation here to have a constant coefficient on
the bad initial. The explicit inverse and obstruction above need none
of those classification inputs. This is a bounded comparison of
hypotheses, not a novelty audit or a claim that the published results
are contradicted.

## 8. Finite verification

The two-method
[finite checker129](three_good_cubic_divided_difference_checks_pass129.py)
checks both inverse orders for \(F=t^3/2\), its exact
partials and commutators, quadratic-span nonmembership,
and the generic cubic divided-difference identities.
The separate
[canonical capture129](verification-pass129-working.json)
records four passing methods: two new129 and two
retained128, with unchanged checker hashes.
The finite controls do not replace the all-\(F\) proof,
the exact initial-algebra argument (9), or a statement
about globally minimal frames.
