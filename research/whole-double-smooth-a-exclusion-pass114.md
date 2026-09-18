# The distinguished coefficient a cannot be smooth

In the supplied actual proper-image whole-double branch, the distinguished
coefficient a belongs to the square of the base maximal ideal. This excludes
every residual colength with a smooth, including the initially proposed
colength-two case. It does not interchange a and b: G has a nonzero
nilpotent residue, whereas H has zero whole-fiber residue.

The argument uses a coefficient normalization over the completed base and
an all-order factorization of the actual scalar P. The resulting two formal
prime factors contradict the single analytically irreducible support proved
in113. No formal slice or completed-kernel calculation is needed.

## 1. The actual inputs

Retain the entire setup and coefficient identities of
[product-index112](whole-double-product-index-pass112.md), together with
[the one-prime and smooth-h exclusions113](whole-double-smooth-coefficient-exclusion-pass113.md).
Let R be the regular local invariant surface, m its maximal ideal, and A
the actual faithfully flat threefold localized over R. Write

\[
\begin{gathered}
F_1=R\{1,r\},\qquad F_2=R\{1,G,H\},\qquad
r=aG+bH,\qquad Nr=P=ah+bB_2\ne0,\\
NG=\varepsilon br+h,\quad NH=-\varepsilon ar+B_2,
\quad Q=\varepsilon r^2-2B_2G+2hH\in R,
\quad\varepsilon\in R^*,\\
J=(a,b)\text{ is }\mathfrak m\text{-primary},\qquad
a,b\in\mathfrak m\setminus\{0\},\qquad
0\ne h\in\mathfrak m^2,\quad B_2,Q\in\mathfrak m^2,\\
A/\mathfrak mA=\mathbb C[c,G]/(G^2),\qquad
H\in\mathfrak mA,\quad c\in F_4,\quad
\overline{Nc}=\lambda G\ne0,\\
P=v p^e,\qquad v\in R^*,\quad e\ge1,
\qquad \widehat R/(p)\text{ is a domain}.
\end{gathered}
\tag{1}
\]

The last line is the actual whole-fiber topology and finite-normalization
input113, not a consequence of a coefficient ansatz. The actual F4 is free
of rank five. For any actual R-basis E, its coefficient determinant in
1,r,r squared,r cubed,r fourth is a unit times P to the minus fourth.
This is the exact all-divisor result used in product-index112.

Suppose for contradiction that a is smooth, meaning a is not in m squared.
We work over Rhat and A'=A tensor_R Rhat. Flat base change preserves the
finite free modules, their displayed bases, and the whole-fiber residues.
The flat algebra A' embeds in its generic polynomial line over Frac(Rhat),
so it is a domain as well.
All coefficients introduced below belong to Rhat and are N-invariant.

## 2. Normalization without exchanging the distinguished generators

Choose a complementary formal parameter t, so Rhat=C[[a,t]]. The positive
integer n=length(R/J) is also the order of b modulo a. Consequently
b=a tau+u t^n for some tau in Rhat and unit u. Use only the permitted
coefficient shear and unit rescaling

\[
\begin{gathered}
G_1=G+\tau H,\qquad H_1=uH,\qquad b_1=t^n,\qquad a_1=a,\\
h_1=h+\tau B_2,\quad B_{2,1}=uB_2,
\quad\varepsilon_1=u\varepsilon,\quad Q_1=uQ,\\
r=aG_1+b_1H_1,\quad
NG_1=\varepsilon_1b_1r+h_1,\quad
NH_1=-\varepsilon_1ar+B_{2,1},\quad
P=ah_1+b_1B_{2,1}.
\end{gathered}
\tag{2}
\]

These identities follow by direct expansion. The whole residue of G1 is
still G, and H1 still belongs to mA'. Also h1 belongs to m squared because
both h and B2 do. Neither a nor r nor P changes. In particular this is
not an exchange of G and H, or an assertion that the formal coefficients
descend to the uncompleted R.

Here is why the needed coefficient restrictions hold after this change.
The pure residue basis 1,G1 in the flat module A' gives the conic extraction
of product-index112:
B2,1 and Q1 belong to
m(h1)+m(a squared)+m(ab1)+m squared(b1 squared).
For the derivative contraction, compute the determinant of the five
elements 1,G1,H1,G1 squared,G1H1 of F4' in the generic r-line. It is
epsilon1 to the fourth times b1 squared divided by 16 P to the fourth.
The old basis E remains a basis over Rhat, with determinant a unit/P^4.
Thus the new product module has determinant a unit times b1 squared;
the adjugate puts b1 squared F4' inside that module. The derivative
calculation112, using the new identities (2), and purity of the nonzero
residue Nc then give b1 squared in (h1)+a(a,b1). This reconstruction
requires no classification of new height-one primes of Rhat.

Suppress the subscripts from now on, and write m for the completed maximal
ideal. The normalized data therefore satisfy

\[
\begin{gathered}
R^\wedge=\mathbb C[[a,t]],\quad b=t^n,\quad J=(a,t^n),\quad
b^2=s h+a^2u_0+abv_0\quad(s,u_0,v_0\in R^\wedge),\\
B_2\in\mathfrak m(h)+\mathfrak m(aJ)+\mathfrak m^2(b^2)
\subseteq\mathfrak m(h)+\mathfrak m(aJ),\\
B_2=h\eta+a\zeta,\qquad
\eta\in\mathfrak m,\qquad\zeta\in\mathfrak mJ.
\end{gathered}
\tag{3}
\]

The second containment uses b squared in (h)+aJ, multiplied by m squared.
It is important here to reconstruct the product restriction, rather than
assume the original asymmetric coefficient bound is invariant under every
change of the F2 basis.

## 3. An exact identity controls the weighted order

Put X=a+b eta. This is another formal parameter with t: b eta has ordinary
order at least two, so the change from a,t is invertible. In C[[X,t]],
assign weight n to X and weight one to t. The inverse equation
a=X-t^n eta shows that a has weight n and initial term X. For example,
successive substitution in that equation gives the inverse and preserves
this leading term. Consequently eta has weight at least one, and zeta has
weight at least n+1, since m has minimum positive weight one and both
generators of J have weight n.

Substitute a=X-b eta in the first identity of (3). Define

\[
\begin{gathered}
W=1-\eta^2u_0+\eta v_0\in R^{\wedge *},\\
b^2W=s h+X\{Xu_0+b(v_0-2\eta u_0)\},\\
P=X\mathcal H-\mathcal R,\qquad
\mathcal H=h+b\zeta,\quad\mathcal R=b^2\eta\zeta.
\end{gathered}
\tag{4}
\]

The first equality follows by expanding a squared and ab; the second
factorization follows from P=ah+bB2 and B2=h eta+a zeta. The unit W has
constant term one. Since b=t^n, every term on the right defining s h
has weight at least 2n.

Evaluate at X=0. The equation for a implies a(0,t) belongs to t^(n+1).
In particular h(0,t) has order at least two, because h belongs to m squared.
Equation (4) gives s(0,t)h(0,t)=t^(2n)W(0,t). Both factors are nonzero.
Write q=ord_t h(0,t). Then ord_t s(0,t)=2n-q. Evaluation gives upper
bounds for weighted orders, while orders of a nonzero product add. Hence

\[
\begin{gathered}
2\le q\le2n,\qquad
\operatorname{wt}(h)\le q,\quad
\operatorname{wt}(s)\le2n-q,\quad
\operatorname{wt}(s h)\ge2n,\\
\operatorname{wt}(h)=q,\qquad
\operatorname{wt}(s)=2n-q,\\
\operatorname{wt}(\mathcal H)=q,\quad
\operatorname{ord}_t\mathcal H(0,t)=q,\qquad
\operatorname{wt}(\mathcal R)\ge3n+2.
\end{gathered}
\tag{5}
\]

Indeed b zeta has weight at least 2n+1, strictly greater than q; thus it
cannot alter the leading term of h. The final bound follows from the
weights 2n, at least one, and at least n+1 of b squared, eta, and zeta.
If eta or zeta is zero, interpret the corresponding order as infinity.
This product-order argument is what makes the proof work for every n;
an ordinary-order bound on h alone would not suffice.

## 4. A smooth formal factor with a nonunit, distinct cofactor

Let M=3n+2 and k=M-q, so k is at least n+2. Substitute X=t^k Z in P.
A monomial X^i t^j of old weight ni+j acquires t-order ki+j. If i is
positive, this exceeds the old weight by at least k-n. Equations (4)--(5)
therefore show that

\[
\Psi(t,Z):=t^{-M}P(t^kZ,t)\in\mathbb C[Z][[t]],\qquad
\Psi(0,Z)=c_0Z-d_0,\quad c_0\in\mathbb C^*,\quad d_0\in\mathbb C.
\tag{6}
\]

Here c0 is the leading coefficient of the calligraphic H at X=0, and d0
is the coefficient of t^M in the calligraphic R at X=0. For each t-degree,
only finitely many monomials of P
contribute after the substitution, so the displayed polynomial-coefficient
series is well defined. The division by t^M removes a common formal factor;
it is not division of an element of the actual algebra A.

The equation Psi(t,Z)=0 has a formal root Z=z(t) in C[[t]] with constant
term d0/c0. One can construct it coefficient by coefficient: the derivative
at t=0 is the nonzero constant c0, so the new coefficient at each successive
t-order is uniquely determined. Put phi(t)=t^k z(t). Then P(phi(t),t)=0.

Formal differentiation lowers weighted order by at most n in the X
direction. Along X=phi(t), the estimates above imply

\[
\begin{gathered}
\operatorname{ord}_t\mathcal H(\phi(t),t)=q,\\
\operatorname{ord}_t\bigl(\phi\mathcal H_X\bigr)
 \ge q+(k-n)>q,\qquad
\operatorname{ord}_t\mathcal R_X(\phi(t),t)
 \ge M-n=2n+2>q,\\
\operatorname{ord}_t P_X(\phi(t),t)=q,\\
P=(X-\phi(t))C(X,t),\qquad
C(\phi(t),t)=P_X(\phi(t),t)\ne0.
\end{gathered}
\tag{7}
\]

For the first equality, every X-dependent term of H acquires strictly
higher order than q after substitution, whereas H(0,t) has order q. The
factorization follows simply by changing coordinates to X-phi(t),t and
using the vanishing constant term in the first variable.

The first factor is a smooth prime. The last equality in (7) shows that it
does not divide C. Since q is positive, C(phi(t),t) is a nonunit, so C is
also a nonunit. Thus P has at least two distinct formal prime factors.
This contradicts (1), where P is a unit times a power of a prime that stays
prime in Rhat. We conclude

\[
\boxed{\quad
\text{actual proper whole-double branch}
\quad\Longrightarrow\quad a\in\mathfrak m^2.
\quad}
\tag{8}
\]

## 5. Scope and provenance

Only the distinguished-a smooth alternative has been excluded here. The
argument does not swap the two coefficients or automatically cover a
smooth b with a in m squared. It also does not exclude the case in which
both coefficients lie in m squared, construct an actual counterexample,
or provide an original frame for an arbitrary cancellation input.

The proof uses actual flat base change, the pure residue submodules and the
full F4 determinant from112, followed by the unique analytically prime
support from113. It does not assume completion of an R-linear derivation
kernel is exact, or require the completed-kernel theorem113. The formal
coefficient normalizations are not claimed to be original polynomial
coordinate changes.

The initial task was the colength-two case. Root's exact weighted product
identity in (4) supplied the all-colength refinement; General independently
reconstructed it before saving this proof. Current112 coefficients and the
complete113 checkpoint and exclusion proof were freshly read. No new
primary-source theorem, numerical method, execution, or claim of novelty
is introduced. All files through113 remain unchanged.
