# Dependent defects at low flow degree

For two rationally dependent quadratic defect fields with no complex
constant relation, the highest flow vector has zero bad components.
This follows directly from the full highest-column equations, without
curve factorization. It recognizes the entire flow-degree-one sector.

At flow degree two, the same fact makes the bad speeds invariant.
If those speeds are algebraically independent, the original kernel is
also polynomial: a transverse bad projection gives the actual graph
recognized in pass64, while a rank-one projection supplies a commuting
nice field in the two good output directions. The latter uses the
existing one-good-output recognition lemma.

This note does not finish the degree-two sector with algebraically
dependent, nonconstant-projective bad speeds. It is a conditional
supplied-frame result, not a universal frame theorem or a solution of
unrestricted cancellation.

## 1. Actual hypotheses and conclusions

Let
\[
B=\mathbb C[x_1,x_2,X,Y]=A[s_*],\qquad
E\in\operatorname{LND}(B),\quad Es_*=1,\quad A=\ker E,
\]
and let \(T_1,T_2,T_3,T_4\) be the actual partials in this order.
Assume
\[
\operatorname{ad}_E^2T_1=\operatorname{ad}_E^2T_2=0,
\qquad \operatorname{ad}_E^3T_3=\operatorname{ad}_E^3T_4=0.
\tag{1}
\]
Write \(W_i=[E,T_i]\), \(V_i=[E,W_i]\) for \(i=3,4\).
The two nonzero defects have fraction-field rank one. Their established
[primitive decomposition](dependent-quadratic-defects-pass42.md#1-what-rank-at-most-one-actually-gives)
is
\[
V_3=aD,\quad V_4=bD,\quad [E,D]=0,\qquad
a,b\in\ker E\cap\ker D,
\tag{2}
\]
where \(D\) is a primitive polynomial LND. Assume \(a,b\) have
no nonzero complex constant relation. Otherwise the earlier constant
frame recombination already recognizes the kernel.

Put \(P=Ex\), \(J=\operatorname{Jac}P\), \(h_j=E^jx\),
\(m=\max\{j:h_j\ne0\}\), and \(\ell=(0,0,a,b)\).
The degree \(m\) is flow-time degree, not ordinary coefficient degree.

**Theorem.** Under (1)--(2):

1. For the highest vector \(h_m\), its \(X,Y\) components vanish.
2. If \(m=1\), both \(X,Y\) are invariant ambient coordinates and
   \(A\simeq\mathbb C^{[3]}\).
3. If \(m=2\) and \(f=EX,g=EY\) are algebraically independent,
   then \(A\simeq\mathbb C^{[3]}\).

No assertion that the primitive defect \(D\) has a slice is used.

## 2. Two full highest identities kill the bad top

The coefficient matrix of the actual conjugated coordinate partials is
\[
\mathcal C(t)=I-tJ+\frac{t^2}{2}D(x)\ell,
\qquad
\mathcal C(t)\operatorname{Jac}(\exp(tE)x)=I.
\tag{3}
\]
It also satisfies \(\mathcal C(t)P(\exp(tE)x)=P\).
The highest coefficients in these two identities give respectively
\[
\ell\operatorname{Jac}h_m=0,\qquad \ell h_m=0.
\tag{4}
\]
Indeed the products have respective highest possible degrees \(m+2\)
and \(m+1\), and their coefficients are nonzero rational factorial
multiples of \(D(x)\ell\operatorname{Jac}h_m\) and
\(D(x)\ell h_m\). The nonzero vector \(D(x)\) can be cancelled.

Set \(u=(h_m)_X\), \(v=(h_m)_Y\). Equation (4) says
\[
au+bv=0,\qquad a\,du+b\,dv=0.
\tag{5}
\]
Here \(d\) is ordinary polynomial differential. If \((u,v)\ne0\),
both this vector and every differential column lie in the same
one-dimensional kernel of \((a,b)\) over \(\operatorname{Frac}B\).
Thus \(u\,dv-v\,du=0\). Since \(a,b\ne0\), both \(u,v\)
would be nonzero, and all four ordinary partials would kill \(v/u\).
Their common rational constants are \(\mathbb C\), so \(v/u=c\)
for a complex constant. Then \(a+cb=0\), contradicting (2).
Consequently
\[
(h_m)_X=(h_m)_Y=0.
\tag{6}
\]
This argument does not differentiate the variable row \(\ell\) as
though it were constant. It uses both independently proved equations
in (4). It also does not require the highest vector to be nonconstant.

For \(m=1\), (6) is \(EX=EY=0\). The original slice makes
\(A\) regular; the established invariant-coordinate recognition
theorem therefore gives polynomial \(A\).[\(\ast\)](#sources-and-verification-scope)

From now on suppose \(m=2\). Write
\[
h=E^2x=(h_1,h_2,0,0)^t\ne0,\qquad f=EX,\quad g=EY.
\tag{7}
\]
In particular \(Ef=Eg=0\).

## 3. The leading family supplies the right common plane

The actual highest-column comparisons give
\[
E,W_1,W_2,V_3,V_4\text{ all kill }f,g,h_1,h_2.
\tag{8}
\]
For example, apply a good column \(T_i+tW_i\) to
\(x+tP+t^2h/2\) and compare its top powers, or just to
\(X+tf,Y+tg\). The bad columns include \(t^2V_i/2\),
and their highest powers give the other annihilations. The fields in
(8) are commuting polynomial LNDs, with zero good tops allowed, by
the full actual conjugated-partial argument.

Assume now \(\operatorname{rank}\operatorname{Jac}(f,g)=2\).
Equation (8) puts their joint fraction-field rank at most two.
If that rank is one, each \(W_i\), \(i=1,2\), is parallel to
\(E\). Then \(T_i\) preserves \(A\), since
\(E(T_iq)=W_iq=0\) for \(q\in A\). Its polynomial translations
preserve \(A[t]\). Conjugating the primitive field \(E\) by these
translations gives primitive LNDs of \(B[t]\) with the same kernel.
Their reduced rational ratio has unit numerator and denominator, so is
a complex constant, equal to one at \(t=0\). Thus \([E,T_i]=0\).
The two genuine commuting partials already recognize \(A\), as in
the [good-direction proof, Section 2](good-direction-recognition-pass46.md#2-the-good-tops-and-the-parallel-case).

We may therefore assume joint rank two. Choose a member \(F_0\)
of the displayed leading family independent of \(E\), and put
\[
C=\ker E\cap\ker F_0,\qquad L=\operatorname{Frac}C.
\tag{9}
\]
Its restriction to \(A\) is a nonzero LND. The inherited
[intrinsic quotient theorem](intrinsic-quotient-surface-pass.md)
therefore applies to the original \(A[s_*]=\mathbb C^{[4]}\), giving
\(C\simeq\mathbb C^{[2]}\). Every field in (8) kills \(C\):
the field \(L\) is algebraic over \(\mathbb C(f,g)\), and all
these fields kill the latter, so separability proves the assertion.
In particular the original primitive \(D\) kills \(C\), since
\(aD=V_3\) does and \(a\ne0\).

The original slice and a local slice for \(F_0|_A\), followed by
polynomial integration over \(L\), give a genuine invariant-localized
chart
\[
B\otimes_C L=L[r,t],\qquad E=\partial_t,\quad F_0=\partial_r.
\tag{10}
\]
To check the last step, before replacing \(s_*\) one has
\(F_0=\partial_r+c(r)\partial_{s_*}\). Replacing
\(t=s_*-\int c(r)dr\) has a polynomial inverse over \(L\).
This is not a global coordinate change of \(B\).

All original generators remain in this ring. For polynomial vectors
over \(L[r]\), their exact expressions are
\[
x_B=\binom XY=q(r)+t\binom fg,\qquad
x_G=\binom{x_1}{x_2}=Q(r)+tP_G(r)+\frac{t^2}{2}h_G,
\tag{11}
\]
where \(h_G=(h_1,h_2)^t\in L^2\). The matrix
\(M_B=[q'\mid(f,g)^t]\) has rank one or two, since \(f\ne0\).

## 4. A transverse bad projection gives the actual pass64 graph

Suppose \(\det M_B\ne0\). The proof of
[pass44, Sections 2--3](generic-bad-pair-pass44.md)
uses only (8)--(11), this invertibility, the genuine good partials,
and algebraic independence of \(f,g\). Its use of independent bad
defects was to establish those inputs in its original setting. Here
they have been established separately.

For clarity, extend \(\partial_f,\partial_g\) uniquely to \(L\)
and fix \(r,t\). Put \(U=[T_1(f,g)^t\mid T_2(f,g)^t]\).
Equation (8) implies \(U\in\operatorname{Mat}_2(L[r])\).
Applying the actual good partials to (11) gives
\[
\begin{split}
K(t)U=I,\quad K(t)={}&Q_v+t(P_G)_v+\tfrac12t^2(h_G)_v\\
&-[Q'+tP_G'\mid P_G+t h_G]M_B^{-1}(q_v+tI),
\end{split}
\tag{12}
\]
where \(v=(f,g)^t\) denotes base differentiation. Since \(U\) is
independent of \(t\), both positive coefficients of \(K(t)\)
vanish. The complete coefficient integration gives
\[
x_i=\frac14(X,Y)\operatorname{Hess}_{f,g}(h_i)\binom XY
 +(\nabla_{f,g}k_i)\binom XY+\ell_i\quad(i=1,2),
\tag{13}
\]
with \(k_i,\ell_i\in L\),
\(\mathscr Hh_i=2h_i\), \(\mathscr Hk_i=k_i\), and
\(\mathscr H=f\partial_f+g\partial_g\).

Actual generation, not a Jacobian conjecture, now gives
\(B\otimes_C L=L[X,Y]\). Differentiating (13) gives
\(U=(x_G)_{(f,g)}^{-1}\); both matrices have entries in \(L[X,Y]\),
so \(\det(x_G)_{(f,g)}\in L^*\). Finally
\(B\cap L=C\) by the joint-kernel definition, and the original
coordinate field is \(L(X,Y)\).

These are exactly the algebraic hypotheses used in
[pass64, equations (1)--(5)](actual-quadratic-graph-cancellation-pass64.md).
Its Euler-field, coefficient-alignment, pole and genuine-coordinate
argument does not use the defect rank after those inputs. Applying
that written argument proves \(A\simeq\mathbb C^{[3]}\).
No claim that \(\det\operatorname{Jac}(h_1,h_2)\ne0\) is made or
needed here.

## 5. A rank-one projection supplies an actual auxiliary three-ring

Suppose \(\det M_B=0\). The global polynomial field
\[
K=fF_0-(F_0X)E
\tag{14}
\]
kills \(X,Y\), commutes with \(E\), and is nonzero. In (10),
\(K=f\partial_r-q_1'(r)\partial_t\). It is triangular and locally
nilpotent over \(L\); every sufficiently high iterate on an original
polynomial therefore vanishes in the injective localization, hence in
\(B\). This proves that (14) is a global LND. Also
\(\ker E\cap\ker K=C\).

The established relative-plane kernel theorem, applied over the actual
UFD \(\mathbb C[X,Y]\), gives
\[
R_0=\ker K=\mathbb C[X,Y,z_0].
\tag{15}
\]
The restricted LND \(E|_{R_0}\) is nonzero. Divide its polynomial
coefficient gcd to obtain a primitive LND \(L_0\). The dividing
factor \(d_0\) is invariant, and \(L_0^2X=L_0^2Y=0\).
The precise established two-quasi theorem has two alternatives.[^dg]
An invariant complex linear form in \(X,Y\) already recognizes the
original \(A\). Otherwise it gives
\[
R_0=\mathbb C[v,X,Y],\quad L_0v=0,\quad
L_0X=p(v),\quad L_0Y=q(v),\quad (p,q)=\mathbb C[v].
\]
With \(j=q(v)X-p(v)Y\), the explicit univariate Bezout inverse gives
\[
C=\mathbb C[v,j],\qquad
f=d_0(v,j)p(v),\quad g=d_0(v,j)q(v).
\tag{16}
\]
Algebraic independence of \(f,g\) forces
\(p'q-pq'\ne0\), as well as \(\partial_jd_0\ne0\).
The generator \(v\) is at this stage a coordinate only of \(R_0\).
No slice is transferred to \(E|_{R_0}\).

## 6. The actual highest field becomes nice and commuting

Let \(H=h\cdot\partial_x\), a nonzero polynomial field with only
good output components. The next coefficient of
\(\mathcal C(t)P(\exp(tE)x)=P\) gives
\[
Jh=\tfrac12(af+bg)D(x),\qquad
[E,H]= -\tfrac12(af+bg)D,\qquad [E,[E,H]]=0.
\tag{17}
\]
The last equality uses invariance of \(a,b,f,g\) under \(E\).
The bracket kills \(C\). Thus \(E(Hc)=0\) for every \(c\in C\).

Since \(HX=HY=0\), differentiate (16):
\[
Hj=(q'(v)X-p'(v)Y)Hv.
\]
Applying \(E\) to this equality gives
\(0=d_0(q'p-p'q)Hv\). Its coefficient is nonzero, so
\(Hv=Hj=0\), and hence
\[
H(C)=0,\qquad H(h_i)=0.
\tag{18}
\]
Therefore \(H\) is a polynomial nice LND. Moreover \(H\) and
\([E,H]\) annihilate \(C\), so they lie in the generic plane
spanned by \(E,F_0\). Both have zero bad components: for the bracket
use \([E,H](X)=-Hf=0\), and likewise for \(Y\).
The projection of that plane has rank one. Its intersection with the
good output plane is consequently the line spanned by \(H\).
Write \([E,H]=\eta H\) over \(\operatorname{Frac}B\).

Divide the coefficients of \(H\) by their polynomial gcd \(c_0\).
Since \(Eh_i=0\), factorial closure gives \(Ec_0=0\).
The primitive polynomial field \(H_0=H/c_0\) satisfies
\([E,H_0]=\eta H_0\). Comparing a reduced denominator against its
primitive coefficients proves \(\eta\in B\). Equation (17) yields
\(E\eta+\eta^2=0\). If \(\eta\ne0\), induction gives
\(E^n\eta=(-1)^n n!\eta^{n+1}\), contradicting local nilpotence.
Thus
\[
[E,H]=0.
\tag{19}
\]

Choose a nonzero good component \(h_b\), using a constant good
coordinate swap if necessary, and denote the other good coordinate
by \(a_0\). On \(B_{h_b}\),
\[
Z=H/h_b=\partial_b+(h_{a_0}/h_b)\partial_{a_0}
\tag{20}
\]
is a genuine nice LND, because \(Hh_b=0\). It commutes with \(E\),
and \(h_bZ=H\) is polynomial. The denominator \(h_b\) is
\(E\)-invariant. The surviving actual partial
\(\partial_{a_0}\) still has vanishing second \(E\)-adjoint.
All hypotheses of the [one-good-output lemma](three-output-cubic-closure-pass41.md#1-a-recognition-lemma-requiring-only-one-good-partial)
are therefore met, with its denominator \(g=h_b\) and exponent one.
That lemma gives an invariant ambient coordinate and
\(A\simeq\mathbb C^{[3]}\). This finishes the independent-speed
part of the theorem.

## 7. The exact remaining low-flow boundary

Within the present dependent/no-constant-relation sector, flow degree
one is recognized. At degree two, algebraically independent bad speeds
are recognized by Sections 3--6. If the two speeds have a constant
complex projective direction, an actual linear combination of \(X,Y\)
is invariant and recognition is immediate, including a zero speed.

The remaining possibility has \(m=2\) and a nonconstant curve of bad
speeds with nonconstant projective direction. Polynomial curve
factorization gives \(f=p(u),g=q(u)\) with actual \(u\in B\),
and all leading fields kill \(u\). It does not make \(u\) ambient
or supply the two speed-field partials used in (12). The original
independent-defect image condition must not be imported here: the
[genuine dependent control](dependent-quadratic-defects-pass42.md#3-a-sliced-full-frame-realization-of-the-distinction)
already has speeds \(f,f^2+1\) without a constant projective ratio.
Its kernel is explicitly polynomial, so it is not an obstruction to
cancellation, only to that proposed image implication.

The broader [omitted-good-direction criterion](good-direction-recognition-pass46.md)
still recognizes this residual whenever a nonzero constant good
direction kills the speed parameter. No such direction is proved to
exist in every case here. Higher-flow and constant-top sectors outside
the stated low-flow conclusions also remain separate.

## Sources and verification scope

The actual primitive decomposition and conjugation identities are
inherited from the linked complete proofs. The nonzero intrinsic
partner uses the source-audited quotient theorem for the original
stably polynomial threefold, not a theorem which first assumes
\(A=\mathbb C^{[3]}\). The rank-one projection uses the same
relative-plane and two-quasi inputs as
[pass43](bad-projection-determinant-pass43.md), with the original
coordinate pair retained.

The complete statements of the two relevant results in
Dasgupta--Gupta were freshly read in their retained primary text and
the arXiv PDF. They explicitly attribute the inputs to
Daigle--Freudenburg and Wang. This audit does not claim a fresh read
of the complete original 1998 or 2005 proofs. The complete saved
one-good-output proof was reread, including its primitive denominator,
relative cancellation and actual coordinate-transfer gates. Its
external Maubach, Hamann, Rentschler and regular-kernel dependencies
are retained. The pass64 graph proof likewise retains its stated
generalized-Luroth and Dedekind recognition inputs.

No finite test is substituted for these theorem hypotheses or for the
all-degree coefficient argument. No new suite, regression count,
metadata update, unrestricted frame-existence theorem, historical
novelty, human expert review or proof-assistant verification is claimed.

[^dg]: Nikhilesh Dasgupta and Neena Gupta,
[*Nice derivations over principal ideal domains*](https://arxiv.org/pdf/1701.03635v1),
Theorem 2.2, PDF p. 3, records the relative UFD-plane kernel theorem
of Daigle--Freudenburg, Theorem 2.4; Theorem 4.1, PDF p. 9, records
Wang, Theorem 4.7 and Remark 5. The first needs an actual polynomial
plane over a UFD containing \(\mathbb Q\), namely the actual
presentation \(B=\mathbb C[X,Y][x_1,x_2]\) used before (15). The
second needs a nonzero primitive LND of the actual polynomial
three-ring and the two named second-iterate vanishings, established
before (16). Both complete statements were directly reread.

The invariant-coordinate endpoint throughout is Bhatwadekar--Gupta--
Lokhande, [Theorem 3.5](https://arxiv.org/pdf/1501.01438v1), applied
only after an actual ambient invariant coordinate and regularity of
the original sliced kernel have been established. It is an inherited
recognition theorem, not a consequence of the companion matrix alone.
