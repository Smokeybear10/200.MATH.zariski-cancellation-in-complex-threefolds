# Nonradial conical speeds are incompatible with a slice

In a supplied sliced polynomial fourfold with three good coordinates
and nonlinear conical speed rank two, quadratic acceleration must obey
the radial identity \(\mathcal R(q)=2q\). The nonradial alternative is
impossible. A hypothetical nonradial frame first yields an invariant
coordinate \(W+P(X,Y,Z)\), with \(\deg P\le4\). A linear-invariant
theorem then forces the speeds to have rank at most one, contradicting
the hypothesis.

This is a restricted working nonexistence theorem, not unrestricted
cancellation. It assumes the displayed coordinate profile. The
intermediate quartic coordinate is not an example in a nonempty
nonradial class. The classical rational-field and linear-invariant
theorems are explicit source inputs, not new claims.

## 1. Exact hypotheses and conclusion

Let
\[
\begin{gathered}
B=\mathbb C[X,Y,Z,W]=A[u],\qquad E=\partial_u,\qquad A=\ker E,\\
E^2X=E^2Y=E^2Z=0,\qquad E^3W=0,\\
s=EX,\quad t=EY,\quad b=EZ,\quad q=E^2W,\\
\operatorname{trdeg}_{\mathbb C}\mathbb C(s,t,b)=2,\qquad
\ker(\mathbb C[S,T,V]\longrightarrow A)=(H),
\end{gathered}
\tag{1}
\]
where \(H\) is irreducible homogeneous of degree at least two.
The displayed four generators are actual polynomial coordinates.
The original slice \(u\) is not assumed to be an ambient coordinate.

The selected-partial reduction135 gives a nonzero intrinsic LND
\(N=[u](\partial_W)|_A\), which kills \(s,t,b,q\).
Its exact degree is one. Put \(L=\operatorname{Frac}\ker_A N\).
This field is finite and separable over the speed field.
The Euler derivation of the homogeneous speed field extends uniquely
to \(\mathcal R\) on \(L\). Assume
\[
\mathcal R(s)=s,\quad\mathcal R(t)=t,\quad\mathcal R(b)=b,
\qquad \mathcal R(q)\ne2q .
\tag{2}
\]
In particular \(q\ne0\). Neither a chosen value of the original slice
nor a choice of an algebraic component is hidden in (2).

Under these hypotheses there is a polynomial
\[
I=W+P(X,Y,Z)\in A,\qquad P\in\mathbb C[X,Y,Z],
\quad\deg P\le4,\qquad
B=\mathbb C[X,Y,Z,I].
\tag{3}
\]
Consequently the regular-kernel theorem would give
\(A=\mathbb C[I]^{[2]}\). More strongly, Section 5 proves that (3)
contradicts the nonlinear conical speed-rank hypothesis in (1).
Thus (1)--(2) cannot hold together.
The coordinate assertion in (3) is stronger than merely producing
a nonconstant invariant or a rational first integral.

## 2. From the actual chart to a monic generic equation

The complete fixed-\(X\) chart argument is given in the
[tangent-graph proof](conical-mismatch-tangent-graph-reduction-pass136.md).
Here are its precise outputs needed for descent:
\[
\begin{gathered}
\tau=t/s,\quad \rho=b/s,\quad \sigma=q/s^2,\qquad
L/\mathbb C(\tau,\sigma)\text{ finite separable},\\
A_s=\mathbb C[y,z,w]_{s_0},\qquad A_L=L[v]=L[y],
\qquad y_v\in L^*,\\
Y=y+\tau X,\quad Z=z+\rho X,\quad
W=w+dX+\tfrac12\sigma X^2,\qquad
z=\rho' y+k,\quad k_\sigma\ne0,\quad \rho''\ne0 .
\end{gathered}
\tag{4}
\]
The original-coordinate partial can move the coefficient field:
indeed that proof shows \(\partial_W(L)\not\subset L\).
The argument therefore never localizes that partial and then silently
retains its local nilpotence. Only the intrinsic \(N\) is localized at
its invariant \(s\).

The two last coefficient equations of the actual unit Jacobian retain
the nonzero factor \(y_v\). With \(\kappa=k\), the
[coefficient-polynomiality proof](conical-mismatch-coefficient-polynomiality-pass136.md)
establishes
\[
\begin{gathered}
K=\ker(\partial_\kappa:L\longrightarrow L)
 =\overline{\mathbb C(\tau)}^{\,L},\qquad
[K:\mathbb C(\tau)]<\infty,\qquad K\subset\operatorname{Frac}A,\\
\sigma\in K[\kappa]_{\le2},\qquad
d\in K[\kappa,y]_{\le3},\qquad w\in K[\kappa,y]_{\le4},\\
y=Y-\tau X,\qquad
\kappa=Z-\rho'Y+(\tau\rho'-\rho)X,\\
W=G_K(X,Y,Z),\qquad G_K\in K[X,Y,Z],\quad \deg G_K\le4 .
\end{gathered}
\tag{5}
\]
The degrees in the middle line are ordinary total degrees over \(K\).
For clarity, polynomiality follows by successively taking the
\(y^5,y^3,y\) coefficients in
\((\partial_\tau-\rho''y\partial_\kappa)w=-1/y_v\).
These give \(\sigma_{\kappa\kappa\kappa}=0\), then
\(\ell_{\kappa\kappa}\in K[\kappa]_{\le1}\), then
\(m_\kappa\in K[\kappa]_{\le3}\).
Subtracting explicit polynomial primitives supplies the integration
constants in \(K\). No arbitrary algebraic antiderivative, equality
\(L=K(\kappa)\), or polynomial generator for \(K\) is assumed.

## 3. Monic rational-pencil descent

Here is a general lemma used at this step. Let
\(B=\mathbb C[x_1,\ldots,x_n,z]\), let \(E\) be an LND on \(B\),
and let \(K\subset\operatorname{Frac}(\ker E)\) have transcendence
degree one over \(\mathbb C\). Suppose
\[
z=G_K(x_1,\ldots,x_n),\qquad
G_K\in K[x_1,\ldots,x_n],\qquad \deg G_K\le d .
\tag{6}
\]
Then some invariant in the original ring is \(z+P(x_1,\ldots,x_n)\),
with \(P\) having complex coefficients and degree at most \(d\).
The lemma does not require a slice.

By the classical rational-field theorem, the subfield \(K\) of the
rational function field \(\operatorname{Frac}B\) is exactly
\(\mathbb C(a)\) for a nonconstant rational function \(a\).[^1]
Choose a reduced original-ring fraction \(a=p/q\), with
\(p,q\in B\), \(q\ne0\), and \(\gcd(p,q)=1\).
Since \(E(a)=0\), one has \(qE(p)=pE(q)\).
Unique factorization gives \(p\mid E(p)\) and \(q\mid E(q)\).
For an LND, a nonzero element cannot divide its nonzero derivative:
the derivative lowers LND degree by one, whereas degrees of products
add. Thus
\[
p,q\in\ker E,\qquad
\ker\bigl(K[\xi_1,\ldots,\xi_n,\zeta]
   \longrightarrow\operatorname{Frac}B\bigr)
=\bigl(p(\xi,\zeta)-a q(\xi,\zeta)\bigr).
\tag{7}
\]

For completeness, the kernel equality is an exact-field assertion.
Introduce an independent indeterminate \(T\).
The polynomial \(p-Tq\) is primitive and linear in \(T\) over
\(\mathbb C[\xi,\zeta]\), hence irreducible and prime there.
The kernel of evaluation \(T\mapsto p/q\) is \((p-Tq)\), by division
over the fraction field followed by Gauss's lemma.
No nonzero polynomial in \(T\) lies in that kernel, since \(a\) is
transcendental over \(\mathbb C\).
Localizing by \(\mathbb C[T]\setminus\{0\}\) therefore gives (7).
This repeats the exact-pencil argument134.[^2]

The equation \(F=\zeta-G_K(\xi)\) also generates this kernel.
Indeed (6) implies
\(\operatorname{Frac}B=K(x_1,\ldots,x_n)\).
This field has transcendence degree \(n\) over \(K\), so the \(n\)
goods are algebraically independent over \(K\).
Division by the monic \(F\) leaves a polynomial in those goods;
evaluation kills such a remainder only when it is zero.
Thus for some \(h(a)\in K^*\),
\[
p(\xi,\zeta)-a q(\xi,\zeta)
=h(a)\bigl(\zeta-G_K(\xi)\bigr).
\tag{8}
\]

Compare coefficients in the formal coordinate monomial basis over
\(K\). Every coefficient on the left is \(c-a e\), with
\(c,e\in\mathbb C\), and vanishes only if \(c=e=0\).
The right side contains no \(\zeta^j\) for \(j\ge2\) and no
\(\zeta\) multiplied by a nonconstant good monomial. Therefore
\[
p=c_0z+P_0(x),\qquad q=e_0z+Q_0(x),\qquad
c_0,e_0\in\mathbb C,\qquad c_0-a e_0=h(a)\ne0 .
\tag{9}
\]
At least one of \(c_0,e_0\) is nonzero. If \(c_0\ne0\), take
\(I=p/c_0\); otherwise take \(I=q/e_0\).
It is invariant and has the required leading term \(z\).
Finally the right side of (8) has no pure-good monomial of degree
greater than \(d\). The same coefficient comparison bounds
\(\deg P_0,\deg Q_0\le d\). This proves the lemma.

The proof never replaces \(K\) by a larger algebraic field and then
chooses just one component. For example the generic equation for
\(a=x^2/y^2\) over \(\mathbb C(a)\) is quadratic; its selected linear
factor over \(\mathbb C(x/y)\) cannot bound the old numerator and
denominator. That distinction is essential to (7)--(8).

## 4. Recognition in the original polynomial ring

Apply the lemma to (5), with \(d=4\). It gives exactly (3).
The inverse coordinate change is explicit:
\[
(X,Y,Z,W)\longmapsto(X,Y,Z,I=W+P(X,Y,Z)),
\qquad W=I-P(X,Y,Z).
\tag{10}
\]
In particular the field-level polynomial relation has now descended
to an actual elementary polynomial shear over \(\mathbb C\).

The original slice supplies regularity of \(A\), independently of
the desired cancellation conclusion. Indeed
\(A\simeq B/(u)\), and \(Eu=1\) gives
\[
1=s\,u_X+t\,u_Y+b\,u_Z+(EW)\,u_W .
\tag{11}
\]
The hypersurface \(u=0\) is therefore smooth over \(\mathbb C\)
by the Jacobian criterion. Its coordinate ring \(A\) is regular.
Now \(E\ne0\) is a \(\mathbb C[I]\)-linear LND on
\(\mathbb C[I,X,Y,Z]\). Bhatwadekar, Gupta and Lokhande,
Theorem 3.5, applies and gives \(A=\mathbb C[I]^{[2]}\).[^3]
The necessary invariant coordinate is (3), not the original slice.

There is also a published nice-derivation endpoint after this shear:
the three remaining coordinates still have zero second iterate.
Dasgupta and Gupta, Corollary 3.8, applies because a slice makes
the action irreducible.[^4] This is an alternative recognition theorem
after descent, not a theorem supplying the required coordinate
from the initial assumptions.

## 5. The nonlinear rank-two branch is actually empty

The following obstruction applies whenever a fixed-point-free LND
has an invariant coordinate \(I\) alongside the three original goods.
It does not require a bound on the old fourth coordinate.
In the present situation (3) gives
\[
B=\mathbb C[I,X,Y,Z],\qquad EI=0,\qquad
E^2X=E^2Y=E^2Z=0,\qquad
(s,t,b)B=B .
\tag{12}
\]
The last assertion follows by expressing the original slice in these
coordinates and applying \(E\). The original slice is still a
polynomial after the explicit inverse shear.

Localize only at nonzero polynomials in the invariant \(I\).
Over \(F_0=\mathbb C(I)\), the derivation is a nonzero nice LND on
the actual polynomial ring \(F_0[X,Y,Z]\).
The three-variable linear-invariant theorem, stated as Dasgupta and
Gupta Theorem 3.1(i), supplies
\[
c_0s+c_1t+c_2b=0,\qquad
0\ne(c_0,c_1,c_2)\in F_0^3,\qquad
c_0+c_1\tau+c_2\rho=0 .
\tag{13}
\]
This source theorem is applied only after the invariant coordinate
has been obtained. It could not be applied to the original
\(\mathbb C[X,Y,Z]\) without proving its stability.

The nonlinear homogeneous irreducible \(H\) over the algebraically
closed field \(\mathbb C\) remains geometrically irreducible over
\(F_0\). Its dehomogenization \(H(1,T,V)\) is irreducible and has
degree at least two. Indeed a linear or constant dehomogenization
would make the original homogeneous polynomial of degree at least
two divisible by \(S\). It is therefore not divisible by the
nonzero affine-linear polynomial \(c_0+c_1T+c_2V\).
That line is nonconstant, because otherwise (13) is impossible.

The intersection of this curve and line is zero-dimensional over
\(F_0\). Equivalently, substitute a solved linear variable into the
curve equation; the remaining nonzero univariate equation makes
both coordinates algebraic over \(F_0\). It follows that
\(\tau,\rho\) are algebraic over \(F_0\).
But \(F_0\) is relatively algebraically closed in the purely
transcendental field \(\operatorname{Frac}B=F_0(X,Y,Z)\).
Consequently
\[
\tau,\rho\in\mathbb C(I),\qquad
(s,t,b)=h(f_0(I),f_1(I),f_2(I)),\qquad
f_i\in\mathbb C[I],\quad\gcd(f_0,f_1,f_2)=1 .
\tag{14}
\]
The second expression comes from clearing the rational denominators
of \((1,\tau,\rho)\), then dividing the polynomial row by its gcd.
Initially \(h\in\operatorname{Frac}B\).
Since \(\mathbb C[I]\) is a PID, choose \(g_i\in\mathbb C[I]\) with
\(\sum_i g_i f_i=1\). Then \(h=g_0s+g_1t+g_2b\in B\), and
\[
(s,t,b)B=(h)B=B,\qquad h\in\mathbb C^*,\qquad
s,t,b\in\mathbb C[I].
\tag{15}
\]
Their transcendence degree is at most one. This contradicts (1)
and proves the claimed nonexistence.

Thus the final elimination uses only the linear-invariant part of
the three-variable theorem, not its stronger rank classification.
The Bhatwadekar--Gupta--Lokhande endpoint in Section 4 is a valid
alternative intermediate implication, but is unnecessary for this
last contradiction.

## 6. Scope and verification

The result eliminates the nonradial alternative inside the nonlinear
conical three-good quadratic branch. It does not assume
the cone has degree at most three; the independent degree bound135
is compatible with the hypotheses but unnecessary in this proof.

Only the radial resonance case \(\mathcal R(q)=2q\) can remain here.
There \(\tau,\sigma\) need not be independent, so the chart in (4)
does not have the same coefficient parameters. The retained
height-eleven bound and its unrecognized \((1,2,2,2)\) endpoint remain
separate. Entry from an arbitrary sliced polynomial fourfold to
this coordinate profile is also unproved.

All conditional calculations in the hypothetical nonradial chart,
including coefficient-field instability, belong to a branch now
excluded by the complete argument. They are not examples realizing
that branch.

Finite symbolic controls check coefficient identities and normalization
factors. They do not certify arbitrary coordinate realization, the
universal field arguments, the external theorems, or novelty.
The complete written derivation has not received human expert review
or proof-assistant verification. No historical novelty claim is made.

## Sources

1. Michiel de Bondt, [*Rational maps H for which K(tH) has transcendence degree 2 over K*](https://arxiv.org/pdf/1501.06046v4),
   arXiv:1501.06046v4, November 2, 2017, Theorem 1.1, printed p. 4.
   Classical Lüroth-Igusa field rationality, not polynomial-generator descent.
2. [The weight of a rational pencil's generic equation](rational-pencil-weight-descent-pass134-working.md),
   Section 2. Exact primitive-pencil evaluation kernel.
3. S. M. Bhatwadekar, Neena Gupta and Swapnil A. Lokhande,
   [*Some K-theoretic properties of the kernel of a locally nilpotent derivation on k[X1,...,X4]*](https://arxiv.org/html/1501.01438v1#S3.Thmtheorem3.5),
   arXiv:1501.01438v1, January 7, 2015, Theorem 3.5.
4. Nikhilesh Dasgupta and Neena Gupta,
   [*Nice derivations over principal ideal domains*](https://arxiv.org/pdf/1701.03635v1),
   arXiv:1701.03635v1, January 13, 2017, Theorem 3.1(i),
   Theorem 3.6 and Corollary 3.8, printed pp. 5--8.
5. [Conical selected-partial reduction135](conical-three-good-adjoint-degree-pass135.md),
   Sections 2--4; [actual tangent chart136](conical-mismatch-tangent-graph-reduction-pass136.md),
   Sections 1--5; [coefficient polynomiality136](conical-mismatch-coefficient-polynomiality-pass136.md),
   Sections 2--5. Working algebraic inputs, with the last two steps
   retaining their complete separate derivations.

[^1]: de Bondt, Theorem 1.1, printed p. 4.
[^2]: [Exact rational-pencil134](rational-pencil-weight-descent-pass134-working.md), Section 2.
[^3]: Bhatwadekar, Gupta and Lokhande, Theorem 3.5.
[^4]: Dasgupta and Gupta, Corollary 3.8, printed pp. 7--8.
