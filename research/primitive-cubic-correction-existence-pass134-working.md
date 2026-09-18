# A weight-three invariant in every supplied primitive quadratic frame

The two correction conditions follow from the actual generic cubic graph.
Its unit Jacobian forces all remaining coefficients into a one-variable
invariant field. A rational generator of that field has numerator and
denominator of original weight at most three. At least one is a
nonconstant invariant, which is exactly the missing correction criterion.

This is a working mathematical proof with the dependencies listed below.
Its scope is the supplied sliced, dense, rank-two, three-good quadratic
class. It does not construct that coordinate profile for an arbitrary
sliced action, and it does not solve unrestricted cancellation.

## 1. Statement and original positive weights

Assume
\[
\begin{gathered}
B=\mathbb C[x_1,x_2,x_3,z]=A[u_0],\qquad E=\partial_{u_0},\qquad A=\ker E,\\
E^2x_i=0,\quad a_i=Ex_i,\quad E^3z=0,\quad q=E^2z,\\
\operatorname{trdeg}_{\mathbb C}\mathbb C(a_1,a_2,a_3)=2,\qquad
a_1v_0,a_2v_0,a_3v_0\text{ algebraically independent over }\mathbb C,\\
q\notin W_2:=\operatorname{span}_{\mathbb C}\{a_i a_j:1\le i\le j\le3\}.
\end{gathered}
\tag{1}
\]
Here \(v_0\) is an independent indeterminate and all four original
generators are actual polynomial coordinates. The conclusion is an
invariant \(I\in A\setminus\mathbb C\) of original weight three,
where the goods have weight one and \(z\) has weight two.

The leading dichotomy supplies the unique primitive relation
\(L(a)q=2F_3(a)\).[^1] Constant good changes and a quadratic bad shear
preserve this weighted filtration in both directions. Localization
rigidity and generic-line exclusion reduce (1) to
\[
\begin{gathered}
B=\mathbb C[X,Y,Z,W],\quad s=EX\ne0,\quad t=EY,\quad r=EZ,\quad
sE^2W=2\gamma t^3,\quad\gamma\in\mathbb C^*,\\
\tau=t/s,\quad \rho=r/s,\quad
\Phi=XW-\gamma Y^3,\quad \operatorname{wt}(X,Y,Z,W)=(1,1,1,2).
\end{gathered}
\tag{2}
\]
No invariant lift is used in those reductions.[^2]
There is no nonconstant invariant of weight at most two: a nonzero
top of that weight cannot belong to the initial-map kernel \((\Phi)\).
The exact low-weight equivalence is
\[
F_2A=\mathbb C,\qquad \dim_{\mathbb C}F_3A\in\{1,2\},\qquad
F_3A\ne\mathbb C
\Longleftrightarrow\text{both original correction conditions pass}.
\tag{3}
\]
Here \(F_jA\) consists of invariants of original weight at most \(j\).
No enlarged-generator weights or graded-ring normality are used.[^3]

## 2. The actual generic graph

The previously established localized presentation and whole generic
polynomial line give
\[
\begin{gathered}
A_s=\mathbb C[y,z,w]_{s_0},\quad s=s_0(y,z,w),\quad B_s=A_s[X],\\
Y=y+\tau X,\quad Z=z+\rho X,\quad W=w+dX+\gamma\tau^3X^2,\\
A_L=L[y,z]=L[v],\quad N'v=1,\quad [L:\mathbb C(\tau,\rho)]<\infty,\\
d=3\gamma\tau^2y+k,\qquad
w=3\gamma\tau y^2+k_\tau y+k_\rho z+\ell,\\
G(U,V)=\gamma U^3+\tfrac12k_{\tau\tau}U^2+\ell_\tau U+\ell_\rho V-m,
\qquad G(y,z)=0,\\
k,\ell,m\in L,\quad k_{\tau\rho}=k_{\rho\rho}=0,\quad\ell_\rho\ne0.
\end{gathered}
\tag{4}
\]
The polynomial \(G\) is irreducible over \(L\). Its graph has \(y\)
of degree one and \(z\) of degree three in \(v\), so \(y_v\in L^*\).
A generic line component was excluded separately because it would
give a constant ambient commuting direction, contrary to primitivity.[^2]

The derivations \(\partial_\tau,\partial_\rho\) extend uniquely
through the finite separable field extension, commute, and kill \(v\).
Their common constant field is \(\mathbb C\): differentiating the
monic minimal polynomial of a common constant gives lower-degree
annihilating polynomials. Those polynomials are zero, so the minimal
polynomial has complex coefficients, and \(\mathbb C\) is algebraically
closed. Consequently
\[
\kappa:=k_\rho\in\mathbb C,\qquad
h:=k-\kappa\rho,\quad h_\rho=0,\qquad \delta:=\ell_\rho\in L^*.
\tag{5}
\]
Primes on functions killed by \(\partial_\rho\) denote \(\partial_\tau\).

## 3. The Jacobian forces constant graph slope

Put \(p=(y,z)^T\), \(M=\partial p/\partial(\tau,\rho)\).
The normalized actual Jacobian is
\(1=-\nabla G(p)^T\operatorname{adj}M\,p_v\).
Differentiate \(G(y,z)=0\) in \(v,\tau,\rho\), distinguishing formal
coefficient derivatives \(G_\tau,G_\rho\) from total derivatives
after evaluation. Since \(G_V=\delta\), this gives
\[
p_v=y_v(1,-G_U(p)/\delta)^T,\qquad
1=y_v\left(\frac{G_U(p)}{\delta}G_\rho(p)-G_\tau(p)\right).
\tag{6}
\]
All terms lie in \(L[y]\), and \(y_v\in L^*\). The parentheses
must therefore be constant in \(y\). Substitute
\[
\begin{gathered}
z=(m-\gamma y^3-\tfrac12h''y^2-\ell_\tau y)/\delta,\\
G_\rho(p)=\delta_\tau y+\delta_\rho z-m_\rho,\qquad
G_\tau(p)=\tfrac12h'''y^2+\ell_{\tau\tau}y+\delta_\tau z-m_\tau.
\end{gathered}
\tag{7}
\]
The coefficient of \(y^5\) in the parentheses of (6) is
\(-3\gamma^2\delta_\rho/\delta^2\), forcing \(\delta_\rho=0\).
Then the coefficient of \(y^3\) is \(4\gamma\delta_\tau/\delta\),
forcing \(\delta_\tau=0\). Thus \(\delta\in\mathbb C^*\).
The remaining quadratic and linear coefficients give
\[
m_\rho=-\frac{\delta h'''}{6\gamma},\qquad
\ell_{\tau\tau}=\frac{h''h'''}{6\gamma}.
\tag{8}
\]
Define
\[
\begin{gathered}
\lambda=h'''/(6\gamma),\qquad
\ell_0=\ell-\delta\rho,\qquad m_0=m+\delta\lambda\rho,\\
h,\lambda,\ell_0,m_0\in K:=\ker(\partial_\rho:L\longrightarrow L),\\
\ell_0'=(h'')^2/(12\gamma)+c_0,\qquad c_0\in\mathbb C.
\end{gathered}
\tag{9}
\]
All memberships follow by differentiation and subtraction. The final
formula follows by differentiating its difference and using the common
constant field; no antiderivative has been assumed to exist.

Every element of \(K\) is algebraic over \(\mathbb C(\tau)\).
Indeed its monic minimal polynomial over \(\mathbb C(\tau)(\rho)\),
on differentiation in \(\rho\), gives a lower-degree annihilating
polynomial, which must vanish. Its coefficients therefore lie in
\(\mathbb C(\tau)\). Conversely separability kills the derivative
of any element algebraic over \(\mathbb C(\tau)\).
Thus \(K\) is exactly the relative algebraic closure of
\(\mathbb C(\tau)\) in \(L\). It has transcendence degree one,
lies in \(\operatorname{Frac}A\), and is stable under \(\partial_\tau\).
It is finite over \(\mathbb C(\tau)\), by retaining linear
independence after adjoining \(\rho\) and using (4).

## 4. A weight-three relation over that field

Set \(w'=w-\kappa z\) and use the actual linear coordinate
\(U_0=W-\kappa Z\). Then (4) reads
\[
\begin{gathered}
w'=3\gamma\tau y^2+h'y+\delta\rho+\ell_0,\\
0=\gamma y^3+\tfrac12h''y^2+\ell_0'y+\delta z+\delta\lambda\rho-m_0,\\
y=Y-\tau X,\quad z=Z-\rho X,\quad
w'=U_0-(3\gamma\tau^2y+h)X-\gamma\tau^3X^2.
\end{gathered}
\tag{10}
\]
Eliminating \(\rho\) and making these substitutions gives
\[
\begin{aligned}
0=\mathcal F={}&\delta Z+(\lambda-X)U_0+\gamma Y^3
 +A_2Y^2+D_2XY+E_2X^2+B_1Y+C_1X-C_0,\\
A_2={}&\tfrac12h''-3\gamma\tau\lambda,\\
D_2={}&-\tau h''+h'+3\gamma\tau^2\lambda,\\
E_2={}&\tfrac12\tau^2h''-\tau h'+h-\gamma\tau^3\lambda,\\
B_1={}&\ell_0'-\lambda h',\\
C_1={}&-\tau\ell_0'+\lambda\tau h'-\lambda h+\ell_0,\\
C_0={}&m_0+\lambda\ell_0 .
\end{aligned}
\tag{11}
\]
All coefficients are in \(K\); the \(X^3\) terms cancel. This is
an identity from the actual frame, not an assumed realizable curve.

Consider \(\mathcal F\) first in formal indeterminates over \(K\).
It is irreducible because its \(Z\) coefficient is the nonzero
constant \(\delta\). Its weighted degree is three, with top
\(-XU_0+\gamma Y^3\). The change \(U_0=W-\kappa Z\) preserves
the filtration in both directions, giving top \(-XW+\gamma Y^3\)
in the original frame.

## 5. Rational descent gives polynomial invariants of bounded weight

The field \(K\) is a transcendence-degree-one subfield of the actual
rational field \(\operatorname{Frac}B=\mathbb C(X,Y,U_0,Z)\).
The classical generalized Lüroth theorem gives \(K=\mathbb C(a)\).[^4]
This is a rational generator, not a polynomial generator or coordinate.

As \(K\subset\operatorname{Frac}A\), write \(a=p/q\), with
\(p,q\in A\), \(q\ne0\), and divide out their ambient polynomial gcd.
Factorial closure of \(A\) in \(B\) keeps the coprime resulting
numerator and denominator in \(A\). At least one is nonconstant.

Let \(T_0\) be an independent coefficient parameter, identifying
\(\mathbb C(T_0)\) with \(K\) by \(T_0\mapsto a\). The polynomial
\[
p(X,Y,U_0,Z)-T_0q(X,Y,U_0,Z)
\tag{12}
\]
is primitive and linear in \(T_0\) over the UFD \(B\), hence
irreducible in \(B[T_0]\) by Gauss's lemma.
Its prime ideal misses \(\mathbb C[T_0]\setminus\{0\}\), since
\(p/q\) is transcendental. It stays a proper prime after localization
to \(\mathbb C(T_0)[X,Y,U_0,Z]\).

The evaluation kernel to \(\operatorname{Frac}B\) has height one:
the image fraction field has transcendence degree three over \(K\).
Thus (12) generates the kernel. The irreducible polynomial
\(\mathcal F\) lies in that same kernel and is therefore a
\(K^*\)-multiple of (12). This is the exact coefficient field,
not one component after enlarging it.

Coefficient-field units have weight zero. The transcendental
parameter \(T_0\) cannot cancel a nonzero complex coefficient
between the numerator and denominator tops. It follows that
\[
3=\operatorname{wt}\mathcal F
 =\operatorname{wt}(p-T_0q)
 =\max\{\operatorname{wt}p,\operatorname{wt}q\}.
\tag{13}
\]
This uses the whole prime polynomial relation. It does not discard
the base locus \(p=q=0\), assume a polynomial Lüroth generator,
or cancel factors in an associated graded ring.
The [standalone rational-pencil lemma](rational-pencil-weight-descent-pass134-working.md)
reconstructs this exact-field algebra separately, including its
boundary under an algebraic extension of the coefficient field.

At least one of \(p,q\) is a nonconstant invariant of weight at most
three. By (3), its weight is exactly three and both correction
conditions pass. This proves the existence assertion.

## 6. Constant coefficients and direct polynomial recognition

There is a stronger descent that avoids a separate geometric
recognition theorem. Choose the nonconstant \(I\in F_3A\) just
obtained and write its initial form as \(c_I\Phi\), \(c_I\in\mathbb C^*\).
By (3), \(F_3A=\mathbb C\oplus\mathbb CI\). Thus
\[
\begin{gathered}
p=p_1I+p_0,\qquad q=q_1I+q_0,\qquad p_i,q_i\in\mathbb C,\\
\mathcal F=f(a)(p-aq)
=f(a)(p_1-aq_1)I+f(a)(p_0-aq_0),\\
f(a)(p_1-aq_1)=-1/c_I\in\mathbb C^* .
\end{gathered}
\tag{14}
\]
The last equality compares the weight-three tops with
\(\operatorname{in}\mathcal F=-\Phi\). The factor \(p_1-aq_1\)
cannot vanish, since \(a\) is transcendental and not both \(p_1,q_1\)
are zero. This also covers a constant numerator or denominator.

Every coefficient of a nonconstant coordinate monomial in
\(\mathcal F\) is therefore a complex constant. In particular
\(\lambda,A_2,D_2,E_2,B_1,C_1\in\mathbb C\). It follows that
\[
J=\delta Z+(\lambda-X)U_0+\gamma Y^3
       +A_2Y^2+D_2XY+E_2X^2+B_1Y+C_1X
  =C_0(a)\in B\cap\operatorname{Frac}A=A .
\tag{15}
\]
The intersection is the actual invariant-field intersection:
the rational extension of \(E\) kills \(C_0(a)\), and \(J\) is
an actual polynomial. Its coefficient of \(Z\) is the nonzero
complex constant \(\delta\); it is already an ambient coordinate.

There is an explicit affine normalization:
\[
\begin{gathered}
X_0=X-\lambda,\qquad
W_1=U_0-E_2X_0-D_2Y-2E_2\lambda-C_1,\\
F_0(Y)=\gamma Y^3+A_2Y^2+(B_1+D_2\lambda)Y
                       +E_2\lambda^2+C_1\lambda,\\
-J=X_0W_1-F_0(Y)-\delta Z,\qquad \gamma\delta\ne0 .
\end{gathered}
\tag{16}
\]
All four variables \((X_0,Y,Z,W_1)\) are actual coordinates,
\(EX_0=s\ne0\), their three good second derivatives vanish,
and \(E^3W_1=0\). The given slice implies fixed-point freeness
and irreducibility. The normalized cubic classification132,
Sections 1--5, applies directly.[^5] It gives \(s\in\mathbb C^*\)
and explicit polynomial generators of \(A\simeq\mathbb C^{[3]}\).
Its classification uses Wang's exact three-variable theorem.
Neither the geometric normalization in its Section 6 nor the
invariant-suspension topology theorem130 is needed here.

## 7. Original-coordinate consequence and the general problem

Returning through the filtered changes gives
\[
I=L(x)z-F_3(x)+\rho_0z-G_2(x)-G_1(x)-G_0\in A,
\qquad \rho_0,G_0\in\mathbb C,
\tag{17}
\]
with \(G_j\) homogeneous of degree \(j\). Its scale-normalized form
is unique up to its constant term by the primitive criterion.
Here \(\rho_0\) is a constant correction coefficient, not the speed
ratio \(\rho\).

The chosen nonconstant invariant differs from \(J\) by an invertible
affine change, by (14), so it too is an ambient coordinate.
The direction of \(X_0\) in the original goods is exactly \(L\);
only a constant translation was added. Thus the nonzero constant
speed conclusion is the original \(L(a)\in\mathbb C^*\).
Neither this conclusion nor polynomial recognition was assumed in
deriving the correction conditions.

The new step is passage of the two corrections in the supplied
primitive dense quadratic class. The quadratic-span alternative
and other recognized classes retain their separate proofs.
An arbitrary presentation \(A[u]\simeq\mathbb C^{[4]}\) does not
automatically supply three affine-in-time good coordinates and one
quadratic coordinate. That entry problem, and unrestricted
cancellation, remain unresolved. Historical novelty, human expert
review, and proof-assistant verification are not established.

## Sources

1. [Leading dichotomy133](three-good-quadratic-cubic-leading-dichotomy-pass133.md),
   Sections 2--4. Existence and primitivity of the leading relation.
2. [Invariant-localization rigidity134](primitive-binary-cubic-localization-rigidity-pass134-working.md)
   and [Generic-line exclusion134](primitive-generic-line-exclusion-pass134-working.md).
   Actual localized ring, whole generic line, normalized volume,
   and irreducible cubic graph.
3. [Low-weight equivalence134](three-good-low-weight-correction-boundary-pass134-working.md),
   Section 1, and [Correction criterion130](three-good-mixed-cubic-correction-criterion-pass130.md),
   Sections 1--3. Original-filtration equivalence and covariance.
4. Michiel de Bondt. *Rational maps H for which K(tH) has transcendence
   degree 2 over K*. arXiv:1501.06046v4, Theorem 1.1 and classical
   attribution, printed p. 4. [Primary text](https://arxiv.org/pdf/1501.06046v4).
   Also Jack Ohm, *On ruled fields*, Journal de Théorie des Nombres
   de Bordeaux 1 (1989), 27--49, Section 1.2, printed p. 29,
   [primary text](https://www.numdam.org/item/JTNB_1989__1_1_27_0.pdf).
   Only the one-dimensional rational-field theorem is used.
5. [Normalized cubic classification132](normalized-cubic-action-classification-pass132.md),
   Sections 1--5. Classification, fixed-locus test and explicit
   straightening in the actual normalized presentation (16).
   Its input is Wang's classification as restated by Nikhilesh
   Dasgupta and Neena Gupta, *Nice derivations over principal ideal
   domains*, arXiv:1701.03635v1, Theorem 4.1, printed p. 9,
   [primary text](https://arxiv.org/pdf/1701.03635v1).
   The geometric normalization in Section 6 of the local132 note
   is not used.

[^1]: [Leading dichotomy133](three-good-quadratic-cubic-leading-dichotomy-pass133.md), Sections 2--4.
[^2]: [Localized rigidity134](primitive-binary-cubic-localization-rigidity-pass134-working.md), Sections 2--5; [Generic-line exclusion134](primitive-generic-line-exclusion-pass134-working.md), Sections 1--5.
[^3]: [Low-weight equivalence134](three-good-low-weight-correction-boundary-pass134-working.md), Section 1.
[^4]: De Bondt, [Theorem 1.1](https://arxiv.org/pdf/1501.06046v4), printed p. 4; Ohm, [Section 1.2](https://www.numdam.org/item/JTNB_1989__1_1_27_0.pdf), printed p. 29.
[^5]: [Normalized cubic classification132](normalized-cubic-action-classification-pass132.md), Sections 1--5; Dasgupta--Gupta, [Theorem 4.1](https://arxiv.org/pdf/1701.03635v1), printed p. 9.
