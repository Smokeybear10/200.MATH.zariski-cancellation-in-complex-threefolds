# Reciprocal coefficient rigidity in the nonzero-R absent-variable chart

**Status: working generic-chart reduction, not original-ring coordinate recognition.**

Under the supplied actual \((1,1,2,2)\) chart with full initial
kernel \((X^2Z-Y^4)\), assume \(R=k_\rho\ne0\) and
\(y\notin L\). Then the whole generic line has \(y\) as an affine
parameter, \(\vartheta\) is a polynomial of degree exactly four in
\(y\), and
\[
 R=\frac1{A t+B},\qquad n=C R^2\rho+n_0,\qquad
 A,B,C\in\mathbb C,\quad (A,B)\ne(0,0),\quad n_0\in K.
\tag{1}
\]
Here \(K=\ker_L\partial_\rho\), not an assumed rational field.
The proof excludes the vanishing quartic top, both possible
quadratic-projection configurations, and all smaller graph degrees.
It returns no generic parameter to an original polynomial coordinate.

## 1. Actual input and exact coefficient fields

Use the actual hypotheses, scalar determinant, whole-line return
and evaluated-cofactor conclusions of
[nonzero-R188](weight-four-absent-variable-nonzero-r-rigidity-pass188-working.md).
Explicitly,
\[
\begin{gathered}
 B=\mathbb C[X,Y,Z,W]=A_0[u],\qquad E=\partial_u,\qquad A_0=\ker E,\\
 \deg_E(X,Y,Z,W)=(1,1,2,2),\qquad
 \ker\theta_0=(\mathsf X^2\mathsf Z-\mathsf Y^4),\\
 N=[u^3](\partial_Z|_{A_0}),\qquad
 L=\operatorname{Frac}(\ker_{A_0}N),\qquad (A_0)_L=L[v],\qquad Nv=1,\\
 a=EX\in L^*,\quad t=EY/a,\quad
 \rho=(E^2W/2)/a^2,\quad (E^2Z/2)/a^2=t^4,\quad
 [L:\mathbb C(t,\rho)]<\infty .
\end{gathered}
\tag{2}
\]
The two ratios are algebraically independent. Coefficient partials
\(\partial_t,\partial_\rho\) commute on \(L\) and initially fix \(v\).
The chart is
\[
\begin{gathered}
 Y=y+tX,\quad Z=z+(4t^3y+k)X+t^4X^2,\quad
 W=w+\vartheta X+\rho X^2,\\
 L[y,z,w]=L[v],\qquad
 \det\frac{\partial(y,z,w)}{\partial(t,\rho,v)}=-a^3\in L^*.
\end{gathered}
\tag{3}
\]
All projected quantities are in \(L[v]\).

Assume \(R=k_\rho\ne0\) and \(y\notin L\). The proved conclusion
of188 is \(R_\rho=0\). Thus
\[
 K=\ker_L\partial_\rho,\qquad
 R\in K^*,\qquad k=R\rho+k_0,\quad k_0\in K.
\tag{4}
\]
Primes below denote \(\partial_t\) on \(K\), never a line-parameter
derivative. The field \(K\) is a finite extension of
\(\mathbb C(t)\), and its prime-constants are exactly \(\mathbb C\).
For clarity, the usual constant-field argument is algebraic:
differentiate the monic minimal polynomial of a
\(\partial_\rho\)-constant over \(\mathbb C(t,\rho)\).
Minimality forces every coefficient to be \(\rho\)-constant,
hence in \(\mathbb C(t)\). The degree is bounded by
\([L:\mathbb C(t,\rho)]\), since \(\rho\) is transcendental over
\(K\); otherwise its differentiated minimal polynomial would give
\(1=0\). This gives finiteness. Applying the same minimal-polynomial
argument to a prime-constant in \(K\) puts it algebraically over
\(\mathbb C\), hence in \(\mathbb C\).
No equality \(K=\mathbb C(t)\) is assumed.

## 2. The exact eliminant and its coefficients

For independent \(U,V\), set
\[
\begin{gathered}
 S=4tU^3+\frac{k_{tt}}2U^2+R'UV+n_tU+n_\rho V,\qquad
 A_1=R'U+n_\rho,\\
 T=U^4+\frac{k_{ttt}}6U^3+\frac{R''}2U^2V
       +\frac{n_{tt}}2U^2+n_{t\rho}UV+\frac{n_{\rho\rho}}2V^2,\\
 \mathcal H=R(T-\ell_tU-\ell_\rho V-m)+A_1(\ell-S).
\end{gathered}
\tag{5}
\]
The universal potentials give \(\mathcal H(y,\vartheta)=0\).
Since \(R\in L^*\), the first potential solves \(w\)
polynomially in \(y,\vartheta\) over \(L\), and the formula for
\(z\) does the same. Therefore
\[
 L[y,\vartheta]=L[v],\qquad
 \mathcal H\ne0,\qquad
 \mathcal H=\omega G+G^2D,\quad
 \omega\in L^*,\quad D\in L[U,V],
\tag{6}
\]
where \(G\) generates the whole kernel of
\(L[U,V]\longrightarrow L[v]\).
The nonvanishing and evaluated-unit assertion use the actual
cleared scalar determinant in188, not merely a birational
parametrization. In particular, (6) does not initially say that
the polynomial cofactor is constant.

Write \(s=n_\rho\), and define
\[
 C_4=R-4tR',\qquad \Delta=\frac{RR''}2-(R')^2.
\]
Direct expansion of (5) gives
\[
\begin{gathered}
 \deg_V\mathcal H\le2,\qquad [V^2]\mathcal H=\frac{R n_{\rho\rho}}2,\\
 [V]\mathcal H=\Delta U^2+
      (R n_{t\rho}-2R's)U-R\ell_\rho-s^2,\\
 [U^4]\mathcal H=C_4,\qquad
 [U^3V^0]\mathcal H=C_3
    =\frac{Rk_{ttt}}6-\frac{R'k_{tt}}2-4ts.
\end{gathered}
\tag{7}
\]
In particular the full homogeneous degree-four part is \(C_4U^4\).
All coefficient extractions in (7) are in the formal polynomial,
before evaluating \(U=y,V=\vartheta\).

The degree of \(y\) on the line is at most two.
Indeed
\([L(v):L(y)]=\deg_v y\): the polynomial \(y(T)-Y_0\)
is irreducible over \(L(Y_0)\), by its degree-one occurrence of
the independent variable \(Y_0\) and Gauss's lemma.
The defining polynomial \(G\), viewed over \(L(U)\), is the
minimal polynomial of \(\vartheta\), because
\(L(y,\vartheta)=L(v)\).
Consequently \(\deg_v y=\deg_VG\le\deg_V\mathcal H\le2\).

We also use the leading-form fact proved in188:
over \(\overline L\), the top homogeneous part of \(G\) is a
power of one linear form. The proof uses the homogenized actual
polynomial parametrization and its unique point at infinity.
It makes no assumption that \(L\) is algebraically closed.

## 3. The vanishing quartic top is impossible

Suppose \(C_4=0\). Then \(R'=R/(4t)\), and hence
\[
 R''=-\frac{3R}{16t^2},\qquad
 \Delta=-\frac{5R^2}{32t^2}\ne0,\qquad
 \mathcal H_3=U^2(C_3U+\Delta V).
\tag{8}
\]
Thus \(\deg\mathcal H=3\), with distinct leading factors of
multiplicities two and one.
This is not an exclusion based on rationality of \(R\):
the equation \(R^4/t\in\mathbb C^*\) alone would be compatible
with an algebraic coefficient field.

Let \(g=\deg G\). If \(g=3\), then \(\mathcal H\) is a scalar
multiple of \(G\), contradicting the leading-form fact.
If \(g=2\), the cofactor of \(G\) has degree one, so the evaluated
unit in (6) forces that cofactor to equal \(\omega\).
This contradicts degree three.
If \(g=1\), (6) says that \(G_1^2\) divides
\(U^2(C_3U+\Delta V)\). It follows that \(G_1\) is proportional
to \(U\), so \(y\in L\), contrary to the hypothesis.
These exhaust the possible degrees, proving
\[
 C_4\ne0,\qquad \deg\mathcal H=4,\qquad \mathcal H_4=C_4U^4.
\tag{9}
\]

Now \(g=1\) would again force \(y\in L\).
If \(g=3\), the degree-one cofactor and (6) force purity,
contradicting degree four. Thus \(g=2\) or \(4\).

## 4. Exhaustive geometric possibilities

If \(\deg_v y=1\), the exact coordinate ring gives
\(\vartheta=P(y)\) with \(P\in L[U]\), and
\(G=V-P(U)\) up to a scalar. The preceding degree alternatives
leave exactly:
\[
\begin{array}{ll}
 \deg P=4:& \mathcal H=\omega(V-P(U));\\
 \deg P=2:& \mathcal H=\omega(V-P(U))+d(V-P(U))^2,\quad d\in L^*.
\end{array}
\tag{10}
\]
The nonzero square coefficient in the second line follows from
\(\deg\mathcal H=4\).

Suppose instead \(\deg_v y=2\). Since \(\deg_VG=2\), any
nonzero \(G^2D\) in (6) would have \(V\)-degree at least four.
It cannot cancel the \(V\)-degree-two term \(\omega G\).
Thus \(\mathcal H=\omega G\) and \(\deg G=4\).

Here is an exact-field elementary normal form, without a
plane-embedding classification theorem.
Translate the line parameter over \(L\) to write
\(y=a_0v_0^2+b_0\), with \(a_0\in L^*\).
Decompose
\(\vartheta=P(y)+v_0Q(y)\), with \(P,Q\in L[U]\).
The equality \(L[y,\vartheta]=L[v_0]\) persists over \(\overline L\).
If \(Q\) has a root \(u_0\ne b_0\), the two parameters above
\(y=u_0\) have the same projected pair, contradicting the
polynomial inverse.
If \(Q(b_0)=0\), both derivatives at \(v_0=0\) vanish,
also contradicting the differentiated polynomial inverse.
The case \(Q=0\) cannot generate \(v_0\).
Therefore \(Q\) is a nonzero constant in \(L\).
Set \(\zeta=Qv_0\). Then
\[
 y=a_1\zeta^2+b_0,\qquad
 \vartheta=P(y)+\zeta,\qquad a_1\in L^*,\quad \deg P=2,
 \qquad
 \mathcal H=d\big((V-P(U))^2-a_2U-b_2\big),
\tag{11}
\]
with \(d,a_2\in L^*\).
The degree \(\deg P=2\) follows from \(\deg G=4\);
the displayed relation itself generates the kernel, since its
quotient is \(L[\zeta]\).
No square root or coefficient-field extension was used to
obtain (11).

It remains to rule out the second line of (10) and (11).
Completing the square in the second line of (10) changes only
the constant coefficient of \(P\). Both possibilities have
the common form
\[
 \mathcal H=d(V-P(U))^2+B_1U+B_0,\qquad
 d\in L^*,\quad P=p_2U^2+p_1U+p_0,\quad p_2\ne0.
\tag{12}
\]
The constants \(B_1,B_0\) here are arbitrary elements of \(L\);
in the completed graph case \(B_1=0\).
We need no further distinction between the two cases.

## 5. The differential equation forced by square completion

Put \(N_2=n_{\rho\rho}\).
Comparing (7), (9), and (12) yields
\[
\begin{gathered}
 d=\frac{RN_2}{2},\qquad
 p_2=-\frac{\Delta}{RN_2},\qquad
 p_1=-\frac{Rn_{t\rho}-2R'n_\rho}{RN_2},\\
 C_4=d p_2^2,\qquad
 N_2=\frac{\Delta^2}{2RC_4}\in K^*,\qquad \Delta\ne0,\\
 C_3=\frac{\Delta(Rn_{t\rho}-2R'n_\rho)}{RN_2}.
\end{gathered}
\tag{13}
\]
Since \(N_2\in K\), exact primitive subtraction gives
\[
 n=\frac{N_2}{2}\rho^2+s_0\rho+n_0,\qquad s_0,n_0\in K.
\]
This does not require \(L=K(\rho)\).
Differentiate the last equation of (13) in \(\rho\), using
\(k=R\rho+k_0\). One obtains
\[
 \frac{RR'''}6-\frac{R'R''}2-4tN_2
       =\Delta\left(\frac{N_2'}{N_2}-\frac{2R'}R\right).
\tag{14}
\]

Set \(f=1/R\). Then
\[
\begin{gathered}
 \Delta=-\frac{f''}{2f^3},\qquad
 C_4=\frac{f+4tf'}{f^2},\qquad
 N_2=\frac{(f'')^2}{8f^3(f+4tf')},\\
 f''\ne0,\qquad f+4tf'\ne0.
\end{gathered}
\tag{15}
\]
For an explicit check of the reduction, set \(D_f=f+4tf'\).
Then
\[
 \frac{N_2'}{N_2}
    =\frac{2f'''}{f''}-\frac{3f'}f-\frac{D_f'}{D_f},
 \qquad
 \frac{RR'''}6-\frac{R'R''}2
    =\frac{f'f''}{2f^4}-\frac{f'''}{6f^3}.
\]
Substituting these into (14), multiplying by \(6f^3D_f\),
and using \(D_f'=5f'+4tf''\), leaves
\[
 5\big((f+4tf')f'''-3f'f''-3t(f'')^2\big)=0.
\tag{16}
\]
This is an identity in the exact finite algebraic field \(K\).

## 6. An algebraic-function lemma at infinity

**Lemma.** If \(0\ne f\) is algebraic over \(\mathbb C(t)\)
and satisfies
\[
 (f+4tf')f'''-3f'f''-3t(f'')^2=0,
\tag{17}
\]
then \(f=A t+B\), with \(A,B\in\mathbb C\).

We give the local justification so that no global power-law
ansatz or rational-field assumption enters the argument.
Choose a place over \(t=\infty\) of a finite function field
containing \(f\). Equivalently, take a maximal ideal over the
maximal ideal of the \(t^{-1}\)-adic valuation ring in its
integral closure. Its residue field is \(\mathbb C\).
The completed field has a uniformizer \(s\) and Laurent
expansions with complex coefficients: successive subtraction
of the residue times \(s^j\) constructs the expansion.
Initially \(t=s^{-e}u(s)\), with \(e\) a positive integer
and \(u(s)\) a unit. A formal \(e\)-th root of the unit exists
in characteristic zero with algebraically closed residue field.
Replacing \(s\) by \(s\,u(s)^{-1/e}\) gives exactly
\(t=s^{-e}\).

Thus \(f\) has a Laurent expansion in rational powers of \(t\),
with exponents in \(e^{-1}\mathbb Z\), bounded above.
The field embeds injectively in this completion.
The coefficient derivative is the termwise derivative
\[
 \partial_t=-\frac1e s^{e+1}\partial_s,
\]
since it sends \(t\) to one and the extension is separable.
This also verifies derivative compatibility when a leading
derivative coefficient vanishes.

Write the leading term as \(a_0t^\mu\), where
\(a_0\in\mathbb C^*\) and \(\mu\in\mathbb Q\).
The coefficient at exponent \(2\mu-3\) in (17) is
\[
 a_0^2\mu(\mu-1)(\mu^2-7\mu-2).
\tag{18}
\]
All terms involving a lower exponent of \(f\) have strictly
lower exponent. Since \((7\pm\sqrt{57})/2\) are irrational,
one must have \(\mu=0\) or \(1\).

If \(\mu=0\), write \(f=b+h\), with \(b\in\mathbb C^*\).
If \(h\ne0\), its leading term is \(c t^p\), with \(p<0\).
The linear contribution \(b h'''\) has leading coefficient
\(bc\,p(p-1)(p-2)\ne0\), at exponent \(p-3\).
Every nonlinear contribution has exponent at most \(2p-3<p-3\).
This is impossible.

If \(\mu=1\), subtract the leading \(a t\) and, if present,
the constant term \(b\).
If the remaining \(h\ne0\), its leading term is \(c t^p\),
where \(p<1\) and \(p\ne0\).
The linear part in (17) is
\[
 a(5t h'''-3h'')+b h'''.
\]
Its leading coefficient at exponent \(p-2\) is
\(ac\,p(p-1)(5p-13)\ne0\).
The \(b h'''\) term has lower exponent \(p-3\), and all
nonlinear terms have exponent at most \(2p-3<p-2\).
Again this is impossible.

There is no residual Laurent series in either case.
Injectivity of the local expansion gives the asserted equality
\(f=A t+B\) in the original function field.
The lemma allows affine \(f\), including nonzero constants.
It does not infer a conclusion from checking only power solutions.

By (15), the two square-completion cases require \(f''\ne0\).
The lemma contradicts (16). Therefore neither case in (12)
can occur in the actual chart.

## 7. The surviving quartic graph and its scope

Only the first line of (10) remains:
\(y\) is affine in \(v\), and
\(\vartheta=P(y)\), \(\deg P=4\).
The purity \(\mathcal H=\omega(V-P)\) and (7) give
\[
 n_{\rho\rho}=0,\qquad
 \frac{RR''}2-(R')^2=0,\qquad
 Rn_{t\rho}-2R'n_\rho=0.
\tag{19}
\]
The middle equation says \((1/R)''=0\).
The constant-field statement after (4) therefore gives
\(1/R=A t+B\) with \(A,B\in\mathbb C\), not both zero.
Writing \(n=s\rho+n_0\), with \(s,n_0\in K\), the last equation
says \((s/R^2)'=0\), so \(s=C R^2\) for \(C\in\mathbb C\).
This proves (1). The constant case \(A=0\) and the case \(C=0\)
are both permitted.

The result is conditional on the actual hypotheses (2), the
nonzero scalar \(R\), and nonconstant \(y\).
It is stronger than a graph-degree bound, but it does not
recognize the original invariant ring.
In particular, the coefficients \(k_0,n_0,\ell,m\) and the
remaining scalar determinant still require analysis.
Neither the generic affine parameter \(y\) nor a reciprocal
coefficient has been declared an original polynomial coordinate.

The zero-\(R\) branch has its separate
[reduction187](weight-four-absent-variable-zero-r-reduction-pass187-working.md).
The constant-\(y\) branch has its separate
[exclusion188](weight-four-absent-variable-constant-projection-exclusion-pass188-working.md).
No statement about other initial forms, unrestricted entry,
or arbitrary cancellation is made here.
The supplied chart mechanisms are working proof inputs,
not a recursive formal audit of all earlier sources.
No earlier artifact was edited and no checker was executed.
This note makes no historical novelty, human expert-review,
proof-assistant-certification or public-submission claim.

