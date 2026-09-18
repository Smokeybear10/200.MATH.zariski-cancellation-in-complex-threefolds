# Closed tail-field fibers and the exact compatible factors

In the actual dense chart, the minimal source curve over the field of
tail coefficients is a closed polynomial line over a finite constant
extension, not merely a rational curve with that function field.
A classical parallel-lines lemma puts its equation in one coordinate.
The trace comparison144 then identifies precisely which first-tail
factors return the two source speed ratios.

The parallel-lines theorem is published mathematics, not a new claim.
The conclusions below are deductions for the retained working chart.
They do not prove automatic base compatibility or cancellation.

## 1. Actual inputs and the smaller coefficient field

Retain the actual dense chart139, the polynomial invariant projection143,
and the degree/norm theorem143.[^1] In particular,
\[
\begin{gathered}
K=\mathbb C(\tau,\rho)\subset L,\qquad [L:K]<\infty,\qquad
F=\operatorname{Frac}A=L(v)=\mathbb C(y,z,w_0),\\
L[y,z]=L[v],\qquad w_0=\Omega(y,z),\\
L_0=K(f_0,\ldots,f_m,f_{-1}),\qquad n=[L:L_0],\\
\Omega,\Phi,\Psi\in L_0[U,V],\qquad
\Phi(y,z)=0,\qquad \Psi(y,z)=v+c,\quad c\in L,\\
\ker(L[U,V]\longrightarrow L[v])=(g),\qquad
\ker(L_0[U,V]\longrightarrow F)=(g_0),\\
g_0\mid\Phi,\qquad \deg g_0=n\deg g,\qquad F=L_0(y,z).
\end{gathered}
\tag{1}
\]
The two coefficient partials preserve \(L_0\) by unique extension
through finite separable fields. Thus the displayed coefficient
membership includes the Taylor derivatives in \(\Omega,\Phi,\Psi\).
Fix a monomial order and normalize \(g\) to leading coefficient one.
Its coefficients generate \(L\) over \(L_0\), by the degree argument143.

There is an element \(e\in\ker_A N\) with \(L=K(e)\), and a complex
polynomial \(p_e\) in three variables such that
\[
e=p_e(y,z,w_0)=p_e(y,z,\Omega(y,z))\in L_0[y,z].
\]
Because \(e\) is algebraic over \(L_0\), its polynomial algebra over
that field is already a field. Since \(K\subset L_0\subset L\),
we obtain the stronger equality
\[
\boxed{\quad
L_0[y,z]=L[y,z]=L[v],\qquad
L_0[U,V]/(g_0)\simeq L[v]\quad\text{as }L_0\text{-algebras}.
\quad}
\tag{2}
\]
Indeed \(L_0[e]=L_0(e)=L\) lies in the left-hand ring.
The polynomial representative of \(e\), rather than just
\(F=L_0(y,z)\), is what closes the affine fiber.

## 2. Applying the classical parallel-lines lemma

Russell and Sathaye's Parallel Lines Lemma, Section 1.2.1, says in
characteristic zero that a polynomial whose plane quotient is a
one-variable polynomial algebra over an algebra is itself a polynomial
in a plane coordinate.[^2] Apply it over \(L_0\) to (2), with the
coefficient algebra \(L\). There are coordinates \(G,H\) such that
\(g_0\) is a polynomial in \(G\).

Translate \(G\) to have constant term zero and scale it to leading
coefficient one in the fixed monomial order. Set \(a=G(y,z)\).
The irreducibility of \(g_0\) and the constants in the quotient yield
\[
\begin{gathered}
L_0[U,V]=L_0[G,H],\qquad L=L_0(a),\\
P(T)=\operatorname{MinPoly}_{a/L_0}(T),\qquad \deg P=n,\\
g=G-a,\qquad g_0\sim P(G),\qquad
L_0[U,V]/(P(G))=L[\,\overline H\,],\\
\overline H=H(y,z)=\lambda v+\delta,\qquad
\lambda\in L^*,\quad\delta\in L .
\end{gathered}
\tag{3}
\]
Here is why the field and normalization assertions are exact.
The algebraic constants of \(L[v]\) over \(L_0\) are precisely \(L\).
In the other quotient presentation they are \(L_0[T]/(P)\).
The selected evaluation therefore identifies this field with \(L\).
Over \(L\), the selected quotient by \(G-a\) is \(L[H]\); hence
its kernel is the selected prime \((g)\).
The chosen leading normalization makes the equality \(g=G-a\)
literal. Finally \(L[\overline H]=L[v]\) forces an affine change
of the single polynomial variable, proving the last line.

This application also explains the norm statement143:
over an algebraic closure of \(L_0\), the \(n\) distinct conjugate
curves are the disjoint parallel fibers \(G=\iota(a)\).
No coordinate over the original complex invariant ring \(A\)
has been produced.

## 3. Exact classification of base-compatible factors

For an \(L\)-irreducible factor \(h\mid\Phi\), let
\[
R_h=L[U,V]/(h),\qquad F_h=\operatorname{Frac}R_h,\qquad
y_h=\overline U,\quad z_h=\overline V,\quad v_h=\Psi(y_h,z_h).
\]
Call \(h\) active when \(v_h\) is transcendental over \(L\).
On an active factor the calibrated initial source substitution gives
an embedding
\(\sigma_h:F\hookrightarrow F_h\) carrying
\((y,z,w_0)\) to \((y_h,z_h,\Omega(y_h,z_h))\).
The precise criterion is
\[
\boxed{\quad
h\text{ is active and }
\sigma_h(\tau)=\tau,\ \sigma_h(\rho)=\rho
\quad\Longleftrightarrow\quad h\mid g_0 .
\quad}
\tag{4}
\]
For the forward implication, the trace theorem144 proves that
\(\sigma_h\) fixes every \(f_j\) and \(f_{-1}\), hence fixes \(L_0\).
Applying it to \(g_0(y,z)=0\) gives \(g_0(y_h,z_h)=0\).
The evaluation kernel over \(L\) is \((h)\), proving divisibility.

Conversely, let \(h\) be any \(L\)-irreducible factor of \(g_0\).
The contraction of \((h)\) to \(L_0[U,V]\) is exactly \((g_0)\).
For example, \(R_h\) is integral over the quotient by this
contraction, because \(L/L_0\) is finite. Their dimensions are one.
The contraction is a height-one prime containing the irreducible
\(g_0\), so equality follows.
Thus evaluation embeds the quotient (2), and then its field
\(F\), into \(F_h\) over \(L_0\).
It sends the source triple to the prescribed triple because
\(\Omega\in L_0[U,V]\).
The image of \(\Psi(y,z)=v+c\) is transcendental over the image
of \(L\); adjoining the original finite coefficient field \(L\)
does not change this. Consequently \(h\) is active.
The embedding is the specified source substitution, and it fixes
\(\tau,\rho\in L_0\), as required.

In particular every factor of \(g_0\) is active and occurs simply
in \(\Phi\). Every remaining factor of \(\Phi\), if active, must
fail at least one base-return identity. The statement does not
say that such remaining factors are absent.

## 4. Component constants and degrees

For a factor in (4), put \(L'=\sigma_h(L)\) and \(C_h=LL'\)
inside \(F_h\). The full trace theorem and its polynomial-projection
corollary give
\[
\begin{gathered}
R_h=C_h[v_h],\qquad F_h=C_h(v_h),\qquad
\sigma_h(v)=v_h+c_h,\quad c_h\in C_h,\\
W_h=\sigma_h(W),\qquad
M_h:=\mathbb C(X,Y_h,Z_h,W_h)=\sigma_h(F)(X),\\
[F_h(X):M_h]=[C_h:L']=[C_h:L],\\
\deg h=[C_h:L]\deg g .
\end{gathered}
\tag{5}
\]
These equalities keep the possibly proper target field \(M_h\)
distinct from the ambient component field \(F_h(X)\).
They do not assert that the original inverse has multiple branches.

For the final degree equality choose a generic complex
\(\ell=y_h+\zeta z_h\). Over \(C_h\), the degrees of \(y_h,z_h\)
in \(v_h\) agree with the original degrees in \(v\):
the source coefficient embedding preserves nonzero leading
coefficients, and the parameter changes only by a translation.
Thus
\([F_h:C_h(\ell)]=\deg g\).
The coefficient extension contributes
\([C_h(\ell):L(\ell)]=[C_h:L]\).
The generic plane projection of the irreducible equation \(h\)
has degree \(\deg h\), so the tower gives (5).

This describes enlarged-constant components that the stabilizer143
did not cover. The factors with \(C_h=L\) recover exactly its
coefficient-automorphism class. No normality of \(L/L_0\) is needed.

## 5. First-order normal forms for the two tails

Use the coordinates in (3), and identify \(L_0[U,V]\) with
\(L_0[G,H]\). The source gradient calculation139 gives
\((\Phi/g)(y,z)\in L^*\).[^3]
Writing \(\Phi=P(G)R(G,H)\), this says
\[
P'(a)R(a,\overline H)\in L^* .
\]
The derivative is nonzero by characteristic zero. Divide \(R\)
by the monic \(P(G)\), treating \(H\) as a second variable.
Every positive-\(H\)-degree coefficient of the remainder vanishes
at \(a\), hence is divisible by \(P\); its degree is less than
\(\deg P\), so it is zero. It follows that
\[
\begin{gathered}
\Phi=P(G)\bigl(r(G)+P(G)S(G,H)\bigr),\\
r\in L_0[G],\qquad \deg r<n,\qquad \gcd(P,r)=1 .
\end{gathered}
\tag{6}
\]
The nonzero constant remainder on the selected line gives the
coprimality assertion. In particular the first-order coefficient
along every conjugate source line is nonzero.

Similarly, \(\Psi(y,z)=v+c\) and the last line of (3) show that
the quotient of \(\Psi\) is affine in \(\overline H\), with
nonzero leading coefficient in \(L\). Division by \(P\) yields
\[
\begin{gathered}
\Psi=b(G)H+d(G)+P(G)Q(G,H),\\
b,d\in L_0[G],\qquad \deg b,\deg d<n,\qquad
\gcd(P,b)=1 .
\end{gathered}
\tag{7}
\]
These are necessary forms. They do not bound \(S,Q\), and they
are not a sufficient test for an actual sliced fourfold frame.

## 6. Why the normal forms do not close the gap

The formal base-flip control143 already satisfies these forms
and the two tail differential identities.[^4] Its fields are
\(L_0=L=K=\mathbb C(a,\rho)\), where \(a,\rho\) are independent.
Choose \(G=V,H=-U\), so \(P(G)=G-a\). Its tails become
\[
\Phi=P(G)\bigl(2a+P(G)\bigr),\qquad
\Psi=2aH,\qquad
\Psi_U=\Phi_\tau,\quad \Psi_V=\Phi_\rho,\quad\tau=a .
\tag{8}
\]
Here (6) has \(r=2a,S=1\), and (7) has \(b=2a,d=Q=0\).
Nevertheless the residual factor \(G+a\) is active and sends
the first source ratio \(a\) to \(-a\).
The closed source fiber, parallel coordinate, unit first-order
term, quotient parameter, and tail differential identities
therefore do not alone force automatic base compatibility.

This is explicitly a formal boundary. Its original Jacobian
is nonconstant and its target function field has index two
in the source function field. It fails the actual polynomial
inverse premise. No actual extra first-tail factor is exhibited.

## 7. What remains

The geometric part of the compatible-component problem is now
the ordinary factorization of a minimal polynomial in one
coefficient-field coordinate. The unsolved step is to make
actual-coordinate information rule out active factors outside
that minimal source polynomial, and then to control any missing
coefficient extension and inactive factors.

Even a complete first-tail result in this chart would not by
itself remove invariant denominators globally or establish the
three-good coordinate entry for an arbitrary cylinder.
The corrected complex-threefold cancellation target remains
unsolved, and the professor's intended field and dimension
remain unconfirmed.

## Sources

1. [Actual dense chart139](dense-all-degree-taylor-chart-pass139-working.md),
   [polynomial invariant projection143](polynomial-coefficient-fiber-presentation-pass143-working.md),
   and [tail-field degree and norm143](tail-coefficient-field-degree-pass143-working.md).
   The actual source data, primitive polynomial coefficient element,
   and the minimal equation and degree over \(L_0\).
2. Peter Russell and Avinash Sathaye,
   [*On Finding and Cancelling Variables in k[X,Y,Z]*](https://www.ms.uky.edu/~sohum/ma561/affgeom/vars_in_k3.pdf),
   Journal of Algebra 57 (1979), 151--166, Section 1.2.1,
   printed pp. 153--154. The Parallel Lines Lemma applies directly
   to (2). Its proof invokes the plane epimorphism theorem and
   a separately cited descent lemma. Those original proofs are
   not claimed newly reconstructed here.
3. [Negative-tail gradient and unit calculation139](dense-negative-tail-relations-pass139-working.md).
   The selected factor is simple and the complementary factor
   restricts to a nonzero coefficient-field constant.
4. [Formal base-incompatible tail143](formal-base-incompatible-tail-pass143-working.md).
   The example in Section 6 is not an actual frame.
5. [Base-compatible trace rigidity144](dense-base-compatible-trace-rigidity-pass144-working.md).
   Full coefficient fixing, the calibrated parameter, the exact
   compositum, and the polynomial component-ring corollary.

No novelty clearance, human review, or proof-assistant verification
is claimed. The new applications depend on the retained working
chart; they are not an independent proof of all earlier reductions.

[^1]: Sources 1 and 5. The whole-line and actual-source premises
    must not be replaced by formal determinant data alone.
[^2]: Source 2. This is an explicit application of a known theorem.
[^3]: Source 3. The statement concerns the selected evaluated
    factor, not a claim that \(\Phi/g\) is constant as a polynomial.
[^4]: Source 4. Section 6 is a boundary for a weakened implication,
    not a counterexample under the actual hypotheses.
