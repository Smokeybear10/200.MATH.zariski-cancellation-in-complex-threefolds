# All slice shifts and linear frames for a polynomial-cylinder family

Date: September 18, 2026. Private working proof. Novelty: UNKNOWN.

There are actual polynomial cylinders for which NO polynomial slice
shift and NO constant linear ambient frame makes the complementary
projected-basis certificate656 succeed. This note proves that uniform
failure and classifies the successful slices in a whole elementary
family. Every base in the family is already polynomial. The result
limits this certificate; it is not a cancellation counterexample.

## 1. Whole coordinates, all slices, and the exact question

Let k be a field of characteristic zero, B=k[x,b,c,t], q in k[b],
and F in k[x].
Define
\[
E=q(b)\partial_x+\bigl(1+q(b)F'(x)\bigr)\partial_t,
\qquad u=t-F(x),\qquad a=x-q(b)u.
\tag{1}
\]
The four polynomials (a,b,c,u) are whole coordinates. Their inverse is
\[
x=a+q(b)u,\qquad t=u+F\bigl(a+q(b)u\bigr),
\tag{2}
\]
with b,c unchanged. The identities Eu=1, Ea=Eb=Ec=0 therefore make
E the coordinate partial in u and give
\[
A=\ker E=k[a,b,c],\qquad B=A[u].
\tag{3}
\]
Every polynomial slice of THIS E is exactly
\[
u_h=u+h(a,b,c),\qquad h\in A.
\tag{4}
\]
Indeed E(u_h-u)=0, and the converse is immediate. For this slice,
the invariant retraction rho_h fixes A and substitutes u=-h.
Its kernel is (u_h). These are the supplied-action slice retractions;
no claim about every possible principal retraction of B is intended.

For each h, ask whether SOME constant linear ambient frame has three
complementary projected coordinate partials forming a commuting
A-basis. By656--657 this is the exact complementary-basis certificate,
not merely a question about three independent or three commuting
fields. Constant affine translations do not change the test.

For a normalized first-row covector lambda, the necessary normal
equation is lambda(e^h)=1, where
\[
e^h=\rho_h(E(x,b,c,t))
=\bigl(q,0,0,1+qF'(a-qh)\bigr).
\tag{5}
\]
The equality between this normal and the principal-retraction normal
follows by expanding each ambient coordinate as a polynomial in u_h:
its linear coefficient is rho_h applied to its E derivative.
Every successful frame can be normalized this way because its
omitted normal component is a unit of A, hence a scalar in k*.

## 2. Nonconstant q and nonlinear F: uniform exclusion

Assume q is nonconstant and deg F>=2. If any h and any successful
constant linear frame existed, (5) would give constants satisfying
\[
\lambda_x q+\lambda_t\bigl(1+qF'(a-qh)\bigr)=1.
\tag{6}
\]
Reduce this equality modulo q in k[a,b,c]. This quotient is nonzero,
and k embeds into it because q is a nonconstant polynomial in b.
Thus lambda_t=1. Cancelling the nonzero q from the remaining equality
in the domain A gives
\[
F'(a-qh)=-\lambda_x.
\tag{7}
\]
Reduce (7) modulo q once more. It would say F'(a)=-lambda_x in
(k[b]/(q))[a,c]. Since characteristic is zero and deg F>=2, F'
has positive degree and nonzero leading coefficient in k*. That
coefficient remains nonzero in this quotient, a contradiction.
This does not require the quotient modulo q to be reduced.

Hence the unit-normal prerequisite already fails for EVERY polynomial
h and EVERY constant linear ambient frame. No commutator analysis is
needed. The argument permits arbitrary degree, repeated factors, and
reducible q; neither irreducibility nor squarefreeness is assumed.

The retained22/657 control is q=b and F=x^2. In this case (7) becomes
\[
b h=a+\lambda_x/2,
\tag{8}
\]
which is impossible modulo b. Thus657's fixed-slice exclusion extends
here to all polynomial slice shifts as well as all linear frames.

## 3. Nonconstant q and affine F: exact successful slices and frames

Continue to assume q nonconstant, but put F=κx+d with κ,d in k.
Use the constant affine ambient frame (x,b,c,u=t-κx-d). In this
frame E=q partial_x+partial_u and a=x-qu. At the slice u_h=0 the
projected fields are exactly
\[
D_x=\partial_a,\qquad
D_b=\partial_b+q'(b)h\,\partial_a,\qquad
D_c=\partial_c,\qquad D_u=-q(b)\partial_a.
\tag{9}
\]
For example the ambient derivative partial_b(a) is -q'(b)u;
evaluation at u=-h gives the sign in (9).

The normal vector in this frame is (q,0,0,1). Since q is nonconstant,
ALL normalized constant normal covectors are
\[
\lambda=(0,\beta,\gamma,1),\qquad \beta,\gamma\in k.
\tag{10}
\]
A basis of the corresponding complementary constant directions
projects to
\[
V_1=\partial_a,\qquad
V_2=\partial_b+(q'h+\beta q)\partial_a,\qquad
V_3=\partial_c+\gamma q\partial_a.
\tag{11}
\]
The source directions are partial_x, partial_b-beta partial_u,
and partial_c-gamma partial_u. All other constant complementary
bases span the same hyperplane, so their pairwise commutation is
equivalent to the commutation of (11).

The complete nontrivial brackets are
\[
[V_1,V_2]=q'h_a\partial_a,\qquad
[V_2,V_3]=q'\bigl(\gamma-h_c-\gamma qh_a\bigr)\partial_a,
\qquad [V_1,V_3]=0.
\tag{12}
\]
Characteristic zero and nonconstant q give q' nonzero. Thus (11)
commutes if and only if h_a=0 and h_c=gamma. Integrating these
polynomial identities gives the exact condition
\[
h=H(b)+\gamma c,\qquad H\in k[b],\quad \gamma\in k.
\tag{13}
\]
The normal condition makes this complementary list an A-basis, so
there is no separate independence or local-nilpotence premise.

In the ORIGINAL order (x,b,c,t), all normalized successful covectors
are therefore
\[
\lambda=(-\kappa,\beta,\gamma,1),\qquad \beta\in k,
\tag{14}
\]
provided h has form (13). The coefficient gamma is fixed by h;
beta is arbitrary. Any constant matrix whose first row is (14)
and whose other rows complete it to an invertible matrix supplies
a successful complementary frame. Conversely every successful
frame, after normalization, has such a first row.

There is also an explicit whole coordinate certificate. Choose
I in k[b] with I'=q'H+beta q, and put
\[
w=a-\gamma q(b)c-I(b).
\tag{15}
\]
Then A=k[w,b,c], with inverse a=w+gamma q(b)c+I(b), and (11)
becomes precisely the coordinate frame (partial_w,partial_b,partial_c).
Indeed V_1(w)=1 and V_2(w)=V_3(w)=0. The primitives exist over every
characteristic-zero field. Finally
B=k[w,b,c,u_h], with the full inverse supplied by (2), (4), and (15).

Consequently for nonconstant q there exists SOME polynomial slice
and SOME successful constant linear frame if and only if F is affine.
Even in the affine case, an arbitrary slice need not succeed: (13)
is the complete restriction, not just a sufficient example.

## 4. Constant q is a separate regime

If q is a nonzero scalar, the conclusion of Section2 is false for
every F, and the reason is explicit. Since
a=x-qt+qF(x), its original ambient t-derivative is -q and its b,c
derivatives vanish. For EVERY slice shift h and EVERY polynomial F,
\[
\rho_h\partial_t|_A=-q\partial_a,\qquad
\rho_h\partial_b|_A=\partial_b,\qquad
\rho_h\partial_c|_A=\partial_c.
\tag{16}
\]
This is a commuting A-basis, with omitted x-normal e_x=q in k*.
Thus no frame change is needed for success. This paragraph does not
classify every additional successful covector when q is constant.

If q=0, E=partial_t and A=k[x,b,c]. Every rho_h fixes these variables,
so their projected partials are the usual coordinate frame and the
projected t-partial is zero. All four commute for every F and h.

## 5. Antecedents, verification, and exact scope

Note22 already contains the q=b,F=x^2 cylinder and its nonlinear
inverse. Note654 proves an all-slice failure of the STRONGER condition
that all four projected fields commute, for q=b,F=0. That same
affine-F example admits the weaker complementary certificate here,
with precisely the successful slices described by (13).
Notes656--657 supply the complementary-basis theorem and its fixed-
retraction finite linear test. The present calculation quantifies
over every polynomial slice shift in this explicit family.

The relevant sources were read in full or reread where used, and a
targeted archive comparison found no identical all-slice classification.
This is not a literature novelty clearance or a new family of
nonpolynomial varieties. All coordinate inverses, brackets, and
constant-q boundaries were reconstructed directly. No saved checker
was executed, imported, compiled, or modified. Fresh unsaved exact
calculations check whole inverse orders and the printed controls;
the uniform classification follows from the written proof.

Root, Geometry, and Jet read the complete held source. Geometry
reported CLEAN; Jet reported CLEAN under the intended field hypothesis
and requested the explicit word "field" now present in Section1.
Root independently reconstructed the proof and checked whole controls.
The reviewed source hash and read evidence are recorded in the ledger.
These internal AI reviews are not human expert or proof-assistant
certification. No novelty clearance or external review is claimed.

The excluded certificates can be restored by a nonlinear ambient
change using the already known coordinates (a,b,c,u). Therefore the
exclusion gives no obstruction to the existence of intrinsic LNDs,
to the polynomiality of A, or to cancellation. It demonstrates that
slice shifts together with constant linear ambient changes do not
make certificate656 universally available. The general cancellation
problem remains UNSOLVED.
