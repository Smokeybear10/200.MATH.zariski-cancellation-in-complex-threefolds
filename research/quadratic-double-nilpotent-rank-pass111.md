# A collapsed double has at most one quadratic nilpotent direction

In the supplied actual nonconical quadratic frame, the restrictions of
degree-at-most-two elements that are constant on a collapsed fixed double
component have at most one independent nilpotent coefficient. This holds
without a nonzero speed normal. The actual two good generators therefore
have constant nilpotent coefficients and supply a degree-two generator of
the double's nilradical.

The proof uses a local chart chosen from two hypothetical independent
quadratic elements. Its transverse coefficient and its volume factor are
initially allowed to vary along the component. The derivative equations,
not a normalization of those functions, give the contradiction.

## 1. Actual assumptions and statement

Retain the actual frame and quotient in
[fixed-fiber collapse111](quadratic-fixed-fiber-low-degree-collapse-pass111.md).
Localize the invariant plane at a closed point m, writing R=S_m and
n=mR. Write A for the actual localized algebra in this note. It is a
faithfully flat domain over the regular local surface R. Its primitive
canonical Jacobian LND N has kernel R and generic line K[v]. The retained
finite-free degree-module proof102 gives
\[
\begin{gathered}
F_j=\ker(N^{j+1}|_A)\simeq R^{j+1},\qquad
A=R[A_1,A_2,c],\quad A_1,A_2\in F_2,\quad c\in F_4,\\
D_2=\mathbb C[c,\epsilon]/(\epsilon^2)
\text{ is a whole collapsed fixed-double factor of }A/\mathfrak nA,\\
\bar N|_{D_2}=\lambda\epsilon\partial_c,\qquad
\lambda\in\mathbb C^*.
\end{gathered}
\tag{1}
\]
The factor, the actual c, and its action are the conclusions of111,
Sections 3--4. In particular they do not require L(m) nonzero.
There may initially be other disjoint factors. The theorem is
\[
\boxed{\quad
\dim_{\mathbb C}\{\bar U\in\epsilon\mathbb C[c]:
       U\in F_2,\ \bar U_{\mathrm{red}}=0\}\le1.
\quad}
\tag{2}
\]
Bars in (2) mean projection to this particular double factor. Constants
may be subtracted before applying the statement. No claim says every
quadratic element is constant on the reduced component.

## 2. Two nilpotent coefficients would give an actual module basis

Suppose U,V in F2 have independent images epsilon u0(c), epsilon v0(c),
where u0,v0 are complex polynomials. The three images 1,U,V are independent
over C in D2. They therefore give a basis of F2/nF2, and Nakayama gives
an R-basis 1,U,V of F2.

The induced N kills the entire nilradical of D2 by (1). Expand NU and
NV in this actual basis, reduce their scalar coefficients modulo n,
and project to D2. Independence of 1,U,V forces every coefficient to
vanish. Thus
\[
\begin{gathered}
F_2=R\{1,U,V\},\qquad N(F_2)\subseteq\mathfrak nF_2,\\
F_1=R\{1,r\},\qquad r=aU+bV,\qquad
Nr=p\in R\setminus\{0\},\qquad \gcd_R(a,b)=1.
\end{gathered}
\tag{3}
\]
This basis-first projection needs no prior assertion about N on another
fiber factor. The element 1 extends to a basis of F1 because it cannot
belong to nF1. Subtract the scalar part of the other basis element to
obtain r as displayed. The quotient F2/F1 embeds into R under N squared,
so is torsion free. A nonunit common factor of a,b would give a nonzero
torsion class there, proving coprimality.

## 3. The conic relation forces square-order scalar coefficients

As in102, write NU and NV in F1. From N(aU+bV)=p and coprimality
there is a nonzero theta in R with
\[
\begin{gathered}
NU=\theta b r+B_1,\qquad NV=-\theta a r+B_2,\qquad
p=aB_1+bB_2,\\
Q=\theta(aU+bV)^2-2B_2U+2B_1V\in R,\\
B_1,B_2,\theta a^2,\theta ab,\theta b^2,Q\in\mathfrak n,
\qquad \boxed{B_1,B_2,Q\in\mathfrak n^2.}
\end{gathered}
\tag{4}
\]
Theta cannot be zero, since N squared is nonzero on the generic
rank-three module. Differentiation gives NQ=0. The derivative matrix
in (3) gives all displayed memberships in n except that of Q; its
expression then puts Q in nA, and faithful-flat contraction gives
Q in n. There is no unit assumption on theta.

Flatness identifies nA/n squared A with the tensor product of n/n squared
and A/nA. Take the first base coefficients of the conic relation and
project to D2. All three products U squared, UV, V squared vanish in
that factor. Independence of 1,epsilon u0,epsilon v0 forces the first
coefficients of Q,B2,B1 to vanish separately. This proves the boxed
memberships in (4). It is a first-coefficient argument in the base
ring, not a comparison of higher coefficients after discarding
nilpotents.

## 4. An actual generic transverse chart with variable coefficients

At the generic point of this double component, choose a constant linear
combination x of the centered base parameters with dx nonzero. The
everywhere-rank statement95 supplies this choice; a second constant
combination f completes the base pair. Since U has nonzero generic
nilpotent image, x and y=U are regular transverse parameters. Indeed,
on the smooth surface x=0 the fiber is a unit times the square of its
smooth reduced equation, and U has nonzero linear term in that equation.
This is the local factorization proved in111, Section 4, now at the
generic point.

The actual c embeds the residue field C(c) into this local ring. Its
completion is C(c)[[x,y]], retaining this coefficient field. Because
the component multiplicity is two, the other base equation and the
actual canonical Jacobian have the forms
\[
\begin{gathered}
\operatorname{wt}(x)=2,\quad \operatorname{wt}(y)=1,
\quad\operatorname{wt}\mathbb C(c)=0,\\
f=A(c)x+B(c)y^2+O_{\mathrm{wt}}(3),\qquad B(c)\ne0,\\
N=\nu(x,y,c)\bigl(f_y\partial_c-f_c\partial_y\bigr),
\qquad \nu\text{ a unit},\quad \nu_0(c)\ne0,\\
V=\phi(c)y+O_{\mathrm{wt}}(2),\qquad
\phi=v_0/u_0\in\mathbb C(c)\setminus\mathbb C.
\end{gathered}
\tag{5}
\]
The ratio in the last line is nonconstant because the two nilpotent residues
are C-linearly independent. No algebraic extension of C(c) is needed.
The unit-volume Jacobian formula is the actual formula from111,
Section 4, in the chosen local differential basis.

Every base element of n has weight at least two, hence those of n
squared have weight at least four. The displayed derivation raises
weight by at least one: f_y has weight at least one, f_c has weight
at least two, and differentiation in y lowers weight by one.
Differentiation in c preserves the weights and differentiates the
rational coefficients. Higher terms of nu and f contribute strictly
higher operator weight.

## 5. The connection terms rule out the two independent residues

Equation (4) gives weight at least three for NU and NV: each nonconstant
linear coefficient belongs to n, while each scalar term belongs to n
squared. Since y is the actual U, the weight-two part of Ny is
\[
\begin{gathered}
(Ny)_{[2]}=-\nu_0(c)\bigl(A'(c)x+B'(c)y^2\bigr)=0,
\qquad A'=B'=0,\\
(NV)_{[2]}
 =\nu_0(c)\bigl(-A'\phi x+(2B\phi'-B'\phi)y^2\bigr)
 =2\nu_0(c)B(c)\phi'(c)y^2=0.
\end{gathered}
\tag{6}
\]
The nonzero factors nu0 and B force phi prime to vanish, so phi is
constant in C(c), a contradiction. The weight-two contribution from
V is exactly that of phi y, since its remainder has weight at least
two and N raises weight. The coefficient nu0 need not be constant and
is never differentiated in this one-step calculation. Both connection
terms involving A prime and B prime were retained before they were
forced to vanish.

This proves (2). Local nilpotence of N on a completion or on a
non-invariant localization has not been used. Only actual finite-degree
module identities were extended to the chart.

## 6. The actual good generators have constant nilpotent coefficients

On this collapsed double write
\[
\begin{gathered}
\bar A_i=\alpha_i+\epsilon f_i(c),\qquad\alpha_i\in\mathbb C,
\qquad (f_1,f_2)=\mathbb C[c],\\
\dim_{\mathbb C}\operatorname{span}\{f_1,f_2\}\le1
\quad\Longrightarrow\quad
f_1,f_2\in\mathbb C,\qquad (f_1,f_2)\ne(0,0),\\
\boxed{\quad
\text{a constant affine combination of }A_1,A_2
\text{ is }G\in F_2\text{ with }\bar G=\epsilon
\text{ after scaling the nilpotent generator.}\quad}
\end{gathered}
\tag{7}
\]
For the ideal equality, A1,A2,c generate the entire factor D2; their
nilpotent parts must therefore generate its rank-one nilradical over
C[c]. The dimension bound is (2). Two proportional polynomials generate
the unit ideal only if their common nonzero polynomial is a constant.
This proves the conclusion including points where an individual
coefficient might initially have been suspected to vanish.

Moreover every U in F2 with constant reduced value has constant
nilpotent coefficient in this same epsilon coordinate. Apply (2) to
U minus that value and the just-constructed G. Thus this conclusion
does not depend on retaining the original good pair.

## Scope, sources and verification

The proof removes the speed-normal premise from the nilpotent-rank
step, rather than applying the old99 normalized chart outside its
hypotheses. The finite-free argument and conic first-coefficient
construction are retained
[degree-module102](quadratic-degree-module-fiber-rigidity-pass102.md),
Sections 2, 4 and 5. The actual factor, quotient rank and unit-volume
inputs are recorded in
[fixed-fiber111](quadratic-fixed-fiber-low-degree-collapse-pass111.md),
with its95 and92 dependencies. The flat tensor calculation uses
exactness of tensoring by a flat module; faithful-flat detection is
also recorded in [Stacks00HP](https://stacks.math.columbia.edu/tag/00HP).
No numerical calculation substitutes for these geometric inputs.

The [two-method symbolic checker](whole_double_nilrank_checks_pass111.py)
checks the elementary invariant identities and the variable-coefficient
formulas in (6). It does not certify the existence of the actual chart,
flatness or the basis descent. This is a restricted-frame theorem,
not a reduction of arbitrary cancellation to that frame, a recognition
of A as a polynomial ring, a Lean proof or a novelty claim.
