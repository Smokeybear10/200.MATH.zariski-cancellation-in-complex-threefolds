# Binary parameters and the remaining original-action obstruction

The current argument gives an exact two-parameter description of a
restricted cancellation branch and controls its common-zero scheme.
It also identifies why two proposed ways to exclude that scheme fail.
The unrestricted cancellation question is not solved.

The full working question remains A[s]=C^[4] implies A=C^[3], under
the unconfirmed complex-threefold interpretation of the professor's
email. The email's displayed conclusion has a dimension mismatch.
Neither that correction nor this choice of field and dimension has
been confirmed. The results below do not supply a nice coordinate
frame for an arbitrary sliced action.

## 1. Exact hypotheses and the binary reduction

Begin only with an actual polynomial locally nilpotent derivation,
meaning a polynomial vector field whose repeated action eventually
kills each polynomial:
\[
\begin{gathered}
B=\mathbb C[x_1,x_2,x_3,w]=A[s],\quad A=\ker E,\quad Es=1,\\
E=P\cdot\partial,\quad E(P_i)=0,\quad
(\operatorname{Jac}P)^2\ne0,\quad T=\partial_w,\quad
[E,[T,E]]=0.
\end{gathered}
\tag{1}
\]
The equation E(P_i)=0 says that each original coordinate moves
linearly along an E-orbit. This is the additional nice-frame
hypothesis, not an automatic consequence of having a slice.
Assume also that the ternary velocity cone obtained in pass76 is
nonlinear. The chosen good direction T must already be supplied.

The [binary descent proof](nice-binary-parameter-descent-pass77.md)
uses the full-gcd homogeneous parametrization in de Bondt's thesis,
with its selected complete proof read and its unused refinements
excluded.[^binary] It produces actual invariant polynomials p,q and
coprime homogeneous binary forms h_i of one degree e>=2 such that
\[
\begin{gathered}
P_i=h_i(p,q)\quad(i\le3),\qquad p,q\in A,\quad
\gcd_B(p,q)=1,\\
I_R^{\,2e-1}\subseteq L_R\subseteq I_R^e,\qquad
I_R=(p,q)R,\quad L_R=(P_1,P_2,P_3)R\quad(R=A,B).
\end{gathered}
\tag{2}
\]
Thus the parameter zero set and the transverse velocity zero set
are identical, including explicit bounds on their ideal
thickenings. Their unreduced ideals need not be equal.
The slice makes P4 a unit modulo L_B, so the original field does
not vanish there.

The [conormal proof](binary-conormal-obstruction-pass77.md) further
shows that a proper I_A requires p and q to be algebraically
independent. For a dependent pair, a finite homogeneous
parametrization gives p=f(a), q=g(a) with an actual invariant a;
ordinary polynomial Bezout then makes their ideal the unit ideal.
No coordinate status for a, p or q is inferred.

## 2. The scheme and its derived action

The [scheme-jet proof](transverse-ideal-scheme-jets-pass77.md) starts
from the actual slice, not just gcd one. It proves that L_B is
extended from C[x1,x2,x3], and identifies
A/L_A with C[x1,x2,x3]/(L_B intersect C[x1,x2,x3]).
Both descriptions occur inside the same quotient ring and have
the same derivation kernel. This is not cancellation of a variable.
Nilpotents and the full fourth Jacobian row are retained.

Put Q=[T,E]. The conormal proof shows Qp=Qq=0 and
Tp,Tq,TP4 in I_A^e. For the independent case let
delta=Q|A=hD, where h is its exact common factor and D its
primitive intrinsic locally nilpotent derivation.
Combining the wedge-image identity from pass75 with the
intrinsic quotient and content arguments gives
\[
\begin{gathered}
\delta(A)\subseteq I_A^{2e-1},\qquad
\delta(I_A^r)\subseteq I_A^{r+2e-1}\quad(r\ge0),\\
S=\ker D=\ker\delta\simeq\mathbb C[u,v],\qquad
h\in(p,q)^{2e-1}S.
\end{gathered}
\tag{3}
\]
The last conclusion does not assume that D is free. The
[content proof](primitive-fiber-content-pass77.md) obtains it
from a flat-annihilator lemma: when D is nonzero on every whole
scheme fiber of a flat quotient, cD(A) lies in LA exactly when
the base element c lies in L. The inherited pass54 theorem
supplies the required scheme-fiber nonvanishing.
The same proof also gives Th in (p,q)^(3e-2)A. It does not
assert that T preserves S or allow iteration on arbitrary A.

This is stronger than a statement about the support or radical
of the content. It does not bound the content from above.
An explicit intrinsic replica of the classical fixed-line
derivation satisfies arbitrarily high raw vanishing while its
primitive field still has fixed points. It is not claimed to
come from the original four-coordinate action in (1).

## 3. A failed shortcut and the condition it omits

The [two-shear control](stationary-parameter-omission-control-pass77.md)
has, for every m>=2, actual coordinate polynomials
p=x+y^m(w+z^2) and q=y+p^m(w+z^3).
Their ideal is the proper ideal (x,y), and Tp,Tq lie in its
m-th power. Nevertheless no nonconstant element of C[p,q]
is killed by any nonzero constant partial direction.
Thus even arbitrary stationarity order combined with the
whole parameter algebra's constant-direction omission property
does not exclude a proper ideal.

The same control sharply distinguishes the missing hypothesis:
every derivation that kills this p,q and square-kills all four
original coordinates must be zero. The second derivative of
y first forces Ez=0, and that of x then forces Ew=0.
So this pair cannot be invariant under a nonzero original nice
action. The counterexample concerns a proposed shortcut, not
cancellation and not the full conditions (1).

## 4. Other construction limits

The [graph-parameter argument](graph-parameter-conic-obstruction-pass77.md)
proves that the actual family a=w+R(x), Ex_i=h_i(a),
Ew=-h(a) dot grad R can have only a conic as its nonlinear
ternary velocity cone in the square-nonzero nice branch.
The proof compares coefficients in the full Hessian identity.
It imposes no degree bound, but it does require this graph
construction. It is not a general conic theorem.

The [aligned-projective-parameter argument](aligned-projective-line-family-obstruction-pass77.md)
excludes nonlinear conical rank-two image for a three-variable
nilpotent-Jacobian map of the special form H=A(x,y,z)(f(y),1,g(y)).
A general rational parameter cannot be replaced by that original
linear coordinate without justification. The standard
Chamberland--van den Essen inverse control is explicitly the
already retained conic seed after a constant coordinate change,
not a new example or a solution of the remaining construction
question.[^aligned]

## 5. Verification and the next mathematical step

The [standalone checker](nice_binary_scheme_checks_pass77.py)
tests finite exact inverse maps, reduced and genuinely nonreduced
scheme jets, selected binary forms, the graph boundary and the
two-shear coefficient identities. The
[saved targeted capture](verification-pass77-working.json)
is separate from the last full regression, which remains
[pass75](verification-pass75-working.json), 146 suites and 1047
methods. Finite controls do not certify the general written
proofs or their published inputs.

~~~sh
/opt/anaconda3/bin/python research/run_targeted_pass77.py
~~~

The next substantive question is whether the actual nice-action
identities impose an upper restriction on h incompatible with
(3), or otherwise exclude a proper parameter ideal. Searching
only for stationary, omission-compatible parameter pairs cannot
answer that question. An alternative is a new actual inverse
construction satisfying every gate in (1), outside the excluded
graph and aligned classes.

The no-good-direction branch and the original arbitrary-frame
problem also remain unresolved. A proof for the supplied-good,
nice branch would still not solve the unrestricted question.
The [proof audit](proof-audits-pass77-working.md) and
[checkpoint](checkpoint-pass77-working.json) separate written
reconstructions, primary inputs, finite tests and file integrity.
No historical novelty, human expert review, formal verification,
public posting, submission or external contact is claimed.

## Sources

[^binary]: Michiel de Bondt, [*Homogeneous Keller maps*](https://webdoc.ubn.ru.nl/mono/b/bondt_m_de/homokema.pdf), doctoral thesis, 2009, Theorem4.3.1, printed87--89. The selected proof and its exact use are recorded in the binary note; [retained-source provenance](../tmp/pdfs/bondt-homogeneous-keller-maps-pass77-source.md) includes immutable PDF/text checksums.

[^aligned]: Marc Chamberland and Arno van den Essen, [*Nilpotent Jacobians in dimension three*](https://chamberland.math.grinnell.edu/papers/essen.pdf). The aligned note separates the source's restricted classifications from its elementary new argument and gives the complete inverse-control formulas.
