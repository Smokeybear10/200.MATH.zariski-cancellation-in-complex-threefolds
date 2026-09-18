# Moving coordinate directions and quadratic divisor covers

The supplied two-quadratic coordinate problem admits stronger restrictions
on both its moving highest coefficients and its exceptional divisor fibers.
An invariant omitted by any good constant direction already recognizes
the original sliced kernel. In the dependent moving branch, a full
companion-matrix identity forces ramification of the entire invariant
curve, not just of its highest coefficient. In the degree-two independent
branch, every remaining primitive plinth cover has degree two and one
finite branch value after normalization.

These are conditional results for actual polynomial coordinate frames.
They do not supply such a frame for an arbitrary cancellation kernel.
The remaining moving cases, and global recognition are not settled. A finite minimal-slice lifting
argument now supplies every remaining codimension-one quadratic model.

## 1. The question and the scope of the reductions

The working question is
\[
A[s_*]\simeq\mathbb C^{[4]}
\quad\Longrightarrow\quad
A\simeq\mathbb C^{[3]}.
\tag{1}
\]
The complex-threefold interpretation has not been confirmed by the
professor. The emailed conclusion \(X\simeq\mathbb A^1\) cannot have
the stated dimension when \(r>1\); replacing it by
\(X\simeq\mathbb A^r\) corrects that mismatch but does not resolve
the intended field or dimension.

Write \(B=A[s_*]=\mathbb C[x_1,x_2,x_3,x_4]\) and
\(E=\partial_{s_*}\). A derivation is locally nilpotent when every
polynomial is killed by some iterate. The actual coordinate partials
\(T_i=\partial_{x_i}\) obey extra commutator bounds only in a
supplied-frame problem. The main residual frame has
\[
\operatorname{ad}_E^2T_1=\operatorname{ad}_E^2T_2=0,\qquad
\operatorname{ad}_E^3T_3=\operatorname{ad}_E^3T_4=0.
\tag{2}
\]
The first two partials are called good. Their top fields
\(W_i=[E,T_i]\) are commuting LNDs and commute with \(E\).
The other top fields are \(V_i=[E,[E,T_i]]\), \(i=3,4\).

An actual frame means polynomial coordinates with a polynomial inverse.
A rational coordinate chart, a prescribed nilpotent matrix, or an
invertible Jacobian without an inverse is not interchangeable with it.
Likewise, no theorem here says that every \(E\) from (1) has a frame
satisfying (2).

The previously complete height-\(H\le9\) and supplied
\((1,1,1,3)\), \((0,2,2,2)\) cases are unchanged.
The complete supplied \((1,1,2,2)\) case remains open.
The new results strengthen several branches inside it.

## 2. An omitted good direction is enough

Suppose only the two good bounds in (2) hold. Let
\[
f\in\ker E\cap\ker W_1\cap\ker W_2\setminus\mathbb C.
\]
If a nonzero constant direction \(S_0=c_1T_1+c_2T_2\) satisfies
\[
S_0f=0,
\tag{3}
\]
then \(E\) fixes an actual ambient coordinate, and \(A\) is
a polynomial three-ring. There is no bound on the other two
coordinate partials in this theorem.

Here is the recognition mechanism. If \(W_0=[E,S_0]\) is
fraction-field parallel to \(E\), then \(S_0\) preserves
\(\ker E\). Its translations conjugate \(E\) into primitive
LNDs with the same kernel. Over the actual polynomial ring with
a parameter, their rational proportionality factor is a unit,
hence a complex constant. Evaluation at parameter zero forces
that constant to be one, so \(W_0=0\). The earlier commuting-partial
recognition lemma then applies with its rational coefficient zero.

If \(E,W_1,W_2\) have rank three, the commuting omitted-coordinate
criterion gives an invariant coordinate. Its proof uses a common
one-variable kernel, general fibers with three independent commuting
actions, complex surface cancellation, and the general-plane-fiber
coordinate theorem. It does not assume the commuting derivations
conjecture in dimension four.

In the remaining rank-two case, \(E,W_0\) are independent.
Set \(C=\ker E\cap\ker W_0\). The actual mixed-column identity
\[
[S_0,W_i]+[W_0,T_i]=0
\tag{4}
\]
puts both \(T_if\) in \(C\). Thus
\(F=\mathbb C[f,T_1f,T_2f]\subset C\) is killed by \(S_0\).

If \(F\) has transcendence degree one, polynomial curve factorization
gives a polynomial parameter \(v\) whose good derivatives are constants.
A nonzero derivative makes \(v\) a triangular coordinate. If both
derivatives vanish, \(v\) is a nonconstant invariant in an actual
two-variable coordinate plane. The established binary-invariant
theorem supplies an invariant coordinate of that plane.[^1]

If \(F\) has transcendence degree two, algebraicity forces
\(S_0(C)=0\). A complementary good partial preserves \(C\).
Highest degree in the omitted coordinate extracts an LND on the
actual complementary three-ring with kernel exactly \(C\).
After primitive division, translations in the remaining good coordinate
commute with it. Its actual two-variable restriction then supplies
an invariant plane coordinate. The original slice makes \(A\)
regular, so the fixed-coordinate regular-kernel theorem applies.[^2]

The [complete proof](research/good-direction-recognition-pass46.md)
retains the parallel, rank-three and rank-two branches. For either
highest-parameter branch, it follows that a still-unrecognized
parameter \(f\) must satisfy
\[
T_1f,\ T_2f
\quad\text{are linearly independent over }\mathbb C.
\tag{5}
\]
This is constant-linear independence, not algebraic independence.
The omitted direction need not be the distinguished highest direction.

## 3. The dependent moving branch must ramify in every curve component

In the dependent high-top branch, write
\[
V_3=aD,\quad V_4=bD,\quad
E^mx=cq,\quad m\in\{3,4\},
\]
where \(D\) is primitive, \(c\) is a nonzero constant good vector,
and \(a,b\) are independent over complex constants.
The established preceding layer has actual polynomials
\[
q=Q(u),\quad z=E^{m-1}x=c\tau+K(u),\quad K_j=0,\quad
Eu=Du=0.
\tag{6}
\]
The parameter \(u\) is not assumed to be an ambient coordinate.
Let \(t=D\tau\), \(\alpha=(m-1)/2\), and
\(\beta=m(m-1)/2\). The trace and commutator are
\[
[E,T_c]=-\alpha rD,\qquad T_cq=\beta rt,\qquad Et=0.
\tag{7}
\]
In the rotating alternative \(r=H_1R_1(u)\), with the exact
univariate factors inherited from the preceding-curve normal form.

Put \(y=E^{m-2}x\). Factoring the full rank-two preceding
companion power, including its auxiliary column, gives
\[
Dy=cA_0+\frac{m}{m-1}\frac{t}{Q'(u)}K'(u),
\qquad A_0=D(y_j/c_j)\in B,\quad EA_0=t.
\tag{8}
\]
The coefficient and polynomial membership are determined by that
auxiliary column. Keeping only the base Jacobian block loses the
constraint.

Define the monic univariate polynomial
\[
G_0=\gcd(Q',K_1',K_2',K_3',K_4').
\]
All entries of (8) are polynomial. Univariate Bezout therefore gives
\(t=(Q'/G_0)(u)T\), \(T\in\ker E\). Equation (7) becomes
\(G_0(u)T_cu=\beta H_1R_1(u)T\). If a factor of \(R_1\)
is missing from \(G_0\), with its full multiplicity, the LND
divisibility lemma forces zero motion. Consequently
\[
T_cu\ne0\quad\Longrightarrow\quad R_1\mid G_0.
\tag{9}
\]
This strengthens \(R_1\mid Q'\). A nonconstant reduced
multiplier in a moving case must be supported at common derivative
zeros of the entire curve \((Q,K)\). Constant \(R_1\) and
sufficiently ramified curves are not excluded.

A tempting next step would assert \(Dt=0\). The first trace
does not justify it. In fact the immediate mixed identity just
differentiates that trace. An actual polynomial-coordinate control
has \(E=\partial_s\), \(D=\partial_v\), \(q=u\), \(t=2v\)
and the actual partial
\(T_c=\partial_z+6v\partial_u-s\partial_v\).
It satisfies the relevant highest-vector and trace identities but
\(Dt=2\). Its full adjoint profile is \((1,4,4,4)\),
not (2). It refutes the weakened inference, not a possible proof
using all of (2). The [complete proof and inverse](research/dependent-motion-ramification-pass46.md)
record this distinction.

## 4. The independent moving correction is polynomial, but not yet an LND

In the independent nonconstant high-top branch, the established
power-law identities give, for \(m\ge3\),
\[
gU=-\alpha V,\quad U=[E,T_c],\quad W=[E,T_\lambda],
\quad V=[E,W],\quad h=T_cg,\quad
Wg=-gh/(2\alpha).
\tag{10}
\]
Here \(E,U,V\) kill \(g\), and the preceding polynomial \(v\)
satisfies \(Ev=g^{m-1}\) and \(Uv=-g^{m-2}h\).

The natural normalizer \(Y=gT_c+2\alpha W\) satisfies
\[
Yg=0,\quad [E,Y]=-gU,\quad
[Y,U]=-hU,\quad [Y,V]=-hV,\quad \operatorname{div}Y=h.
\tag{11}
\]
A polynomial LND has zero divergence in actual coordinates.
Thus \(Y\) is not locally nilpotent when \(h\ne0\).
The previously proved zero-motion construction shows the converse
within these hypotheses.

There is nevertheless a global polynomial correction
\[
\mathcal R=g^{m-2}Y+vU.
\tag{12}
\]
The powers are nonnegative before any localization.
Direct bracket and divergence identities give
\[
[E,\mathcal R]=[U,\mathcal R]=[V,\mathcal R]=0,\qquad
\mathcal Rg=0,\qquad\operatorname{div}\mathcal R=0.
\tag{13}
\]
This closes the polynomiality and commutation issue for this
candidate. It does not prove local nilpotence or an additional
independent quotient direction.

For a precise control, take \(B_0=\mathbb C[s,t,u,z]\),
\(g_0=uz\), \(h_0=u\), \(E_0=\partial_s\),
\(U_0=\partial_t\), and \(H=u\partial_u-z\partial_z\).
An actual first partial and suitable \(Y_0,v_0\) satisfy the
derived preslice and commutation package, but the correction is
\[
\mathcal R_0=g_0^{m-2}H,\qquad
\mathcal R_0^n(u)=g_0^{n(m-2)}u\ne0\quad(n\ge1).
\tag{14}
\]
This non-LND control lacks the required second actual partial and
the full highest-flow frame. The
[full correction proof](research/moving-commuting-repair-pass46.md)
does not promote it to a counterexample under the original hypotheses.

## 5. The entire generic divisor fiber and its degree

Now restrict to the independent degree-two branch. The established
actual generator theorem gives, with \(C=\ker D\simeq\mathbb C^{[2]}\)
and \(L=\operatorname{Frac}C\),
\[
B_L=L[x_3,x_4],\qquad
x_i=\mathcal Q_i(x_3,x_4),\quad\deg\mathcal Q_i\le2
\quad(i=1,2).
\tag{15}
\]
The quotient \(C\subset A\) is faithfully flat. Choose \(D\)
primitive, with full principal plinth \(pC\) and an actual
minimal local slice \(Dr=p\). These intrinsic inputs do not
assume \(A\) polynomial.[^3]

For an irreducible \(\pi\in C\), put
\(R=C_{(\pi)}\), \(\kappa=\operatorname{Frac}(C/\pi C)\).
Factorial closure makes \(\pi\) prime in \(A\).
Primitivity ensures that \(D\) reduces to a nonzero LND on
the entire one-dimensional domain \(\overline A=A\otimes_C\kappa\).
Its invariant ring is a finite algebraic field \(F_\pi\),
so a local slice becomes a slice. Hence
\[
\overline A=F_\pi[t],\qquad
\overline B=F_\pi[t,s_*],\qquad
e_\pi=[F_\pi:\kappa]<\infty.
\tag{16}
\]
This identifies the full fiber, not just the image of two generators.

Moreover \(e_\pi=1\) exactly when \(\pi\nmid p\).
The nontrivial direction is elementary. If \(\pi\mid p\) but
\(F_\pi=\kappa\), then \(\bar r\) is a scalar in \(\kappa\).
Lift it to \(a\in R\). The actual element \((r-a)/\pi\)
would have derivative \(p/\pi\), contradicting the full plinth \(pR\).

Let \(V_N\) be the finite free \(R\)-span of coordinate
monomials of total degree at most \(N\). Equation (15) bounds its
rank by \(\binom{2N+2}{2}\). Its residue image has dimension no
larger than that rank. A basis of \(F_\pi/\kappa\), multiplied
by monomials in two algebraically independent residue generators,
gives a lower bound \(e_\pi\binom{N-M+2}{2}\) for a fixed \(M\).
Comparing leading terms proves
\[
e_\pi\le4.
\tag{17}
\]
Only surjectivity from the lattice reduction to its image is used.
No saturation or injectivity of that map is assumed.

## 6. Why only quadratic plinth covers remain

Consider a simultaneous bad-speed prime \(\pi\mid f,g\), where
\(f=Ex_3\), \(g=Ex_4\).
Its bad residues belong to \(F_\pi[t]\). If one, \(\bar z\),
is nonconstant of degree \(d\), localize the actual polynomial ring
\(R[z]\) at \((\pi)\). The remaining generic ring is a
one-variable quadratic graph, while the full residue constant field
has degree \(e_\pi d\) over \(\kappa(\bar z)\).
The one-variable version of the preceding growth comparison gives
\[
e_\pi d\le2.
\tag{18}
\]
At a plinth prime \(e_\pi>1\); thus \(e_\pi=2\) and \(d=1\).
Every nonconstant bad residue is an actual residue-line parameter.

If both bad residues are algebraic, they lie in the field \(F_\pi\)
of complex transcendence degree one. A nonzero complex binary polynomial
\(P(x_3,x_4)\) therefore vanishes in the generic divisor fiber.
Prime saturation gives \(\pi\mid P(x_3,x_4)\) globally.
Because this is an actual coordinate plane, its polynomial factors
remain prime in \(B\), so \(\pi\) itself belongs to that plane.
It is \(E\)-invariant. The published binary-invariant and
fixed-coordinate theorems then recognize \(A\).[^1][^2]

At primes where a bad speed or good acceleration is a unit, the
previous full local classification already supplies residue degree
two at a plinth. Therefore
\[
\boxed{\text{Either }A\simeq\mathbb C^{[3]},
\text{ or every primitive plinth divisor has }e_\pi=2.}
\tag{19}
\]
The [all-prime proof](research/quadratic-residue-degree-pass46.md)
includes every field and localization step.
This does not prove that the simultaneous support
\(\gcd(p,f,g,E^2x_1,E^2x_2)\) is empty. The additional lifting
argument below supplies its full local quadratic presentations.

## 7. Finite minimal-slice lifting gives the full local equation

The missing local presentation follows from the quadratic full
residue field, without a new slice for the original four-variable
action. Normalize the actual intrinsic minimal slice so that
\(Dr=\pi^n\), where \(n=v_\pi(p)\).
Its residue \(\bar r\) is invariant and is not in \(\kappa\),
since that would allow division of a shifted slice by \(\pi\).
Consequently \(F_\pi=\kappa[\bar r]\).

Choose a monic quadratic \(P(T)\in R[T]\) lifting the
minimal polynomial of \(\bar r\). Its residue is separable.
The valuation \(\ell=v_\pi(P(r))\) is positive and finite.
It cannot exceed \(n\), because
\(D(P(r))=\pi^nP'(r)\) and \(P'(r)\) has nonzero residue.
If \(\ell<n\), then \(P(r)/\pi^\ell\) has invariant residue.
Write that residue as \(\bar a\bar r+\bar b\), lift \(a,b\)
to \(R\), and replace
\[
P(T)\longmapsto P(T)-\pi^\ell(aT+b).
\tag{20}
\]
The valuation strictly increases, while monicity and the separable
residue polynomial stay fixed. After at most \(n-1\) corrections
it is exactly \(n\). Thus \(Y=P(r)/\pi^n\) belongs to \(A_R\)
and \(DY=P'(r)\).

The subring \(H=R[r,Y]\) has the exact prime presentation
\(R[T,Y]/(\pi^nY-P(T))\). Modulo \(\pi\), the derivative
of \(\bar Y\) is a nonzero element of \(F_\pi\), so \(\bar Y\)
is an affine-linear parameter of the full residue line.
Hence \(H/\pi H\to A_R/\pi A_R\) is an isomorphism.
It follows that \(H\cap\pi A_R=\pi H\). Since both rings
become \(L[r]\) after inverting \(\pi\), cancelling the
smallest possible denominator shows that \(A_R=H\).
No completion or infinite approximation is used.

Completing the square now gives
\[
A_R\simeq R[T,Z]/(\pi^nZ-T^2+\eta),\qquad
DT=\pi^n,\quad DZ=2T,\quad
\eta\in R^*,\quad\bar\eta\notin\kappa^{*2}.
\tag{21}
\]
Thus, unless \(A\) is already recognized, every primitive plinth
prime has this full model, including simultaneous speed and
acceleration primes. Away from the plinth the local ring is a
polynomial line. The existing bound \(p\mid\Delta\) gives
\(n\le v_\pi(\Delta)\) at every such prime.

The [complete lifting proof](research/minimal-quadratic-slice-pass46.md)
also explains the exact generality: a separable residue extension
of degree \(d\) gives a monic degree-\(d\) presentation by the same
finite method if the residue of the actual minimal slice generates
that extension. Prime degree forces this generation; composite
degree does not automatically do so.

All these local rings sit in the same generic line, and
\[
A=\bigcap_{\pi\in C\ {\rm irreducible}}A_{C_{(\pi)}}
\quad\text{inside }A_L.
\tag{22}
\]
Indeed an element of the intersection has denominator in \(C\);
membership at each prime factor forces that denominator to cancel
in the UFD \(A\). Thus the unresolved issue is compatibility of
the embedded local equations in one generic ring. There is no
additional unspecified extension once those embedded subrings
are known. Their abstract isomorphism types alone do not determine
global polynomial generators.

## 8. The normalized cover has one finite branch value

The cylinder makes \(\operatorname{Spec}A\) smooth, factorial and
contractible. Kaliman's quotient theorem therefore applies before
any polynomiality conclusion about \(A\). Its finite intermediate
curve factorization and retained-component theorem, together with
the normalization Betti-number equality in its proof, make both
normalizations affine lines.[^4]

The full residue ring (16) identifies the function field of that
actual intermediate curve as \(F_\pi\). A degree-two cover
between the affine-line normalizations is a quadratic polynomial map.
After changing its source coordinate, it has the form
\[
u=w^2+b,\qquad
F_\pi=\mathbb C(u)(\sqrt{u-b}).
\tag{23}
\]
If \(F_\pi=\mathbb C(u)(\sqrt{\epsilon})\), then
\(\epsilon/(u-b)\) is a square in \(\mathbb C(u)^*\).
There is exactly one finite odd valuation of the square class
and one at infinity. The parameter \(u\) is a normalization
coordinate, not an asserted coordinate of \(C\).

For example the square class \(u(u-1)\) is excluded: its affine
cover is a punctured line, rather than an affine line.
The permitted single-branch class is not itself a recognition
criterion. The polynomial action
\(D=X\partial_Y+2Y\partial_Z\) already has such a cover.
Nonpolynomial contractible-threefold controls also show why topology
alone cannot replace the supplied-frame information. No such control
is asserted to have polynomial cylinder (1).

The [complete monodromy proof](research/quadratic-monodromy-pass46.md)
applies to any degree-two intrinsic residue field, whether or not
its full local ring has been classified. It bounds neither the
divisor thickness nor the way local coordinates fit together.

## 9. A second-image ideal isolates the equation-gluing obstruction

Keep the global actual minimal slice \(Dr=p\). Its first degree
module is exactly \(F_1=C\oplus Cr\): if \(Dz\) is invariant,
the full plinth makes it a multiple of \(p\), and a multiple
of \(r\) can be subtracted. Define the standard second image
ideal \(I_2=D^2(A)\cap C\). Then
\[
I_2=pJ,\qquad p\in J,\qquad
J_{(\pi)}=C_{(\pi)}\quad\text{for every irreducible }\pi\in C.
\tag{24}
\]
Indeed \(D^2z\in C\) implies \(Dz\in F_1\), so
\(D^2z\in pC\). Also \(D^2(r^2)=2p^2\).
The complete local equations give exactly \(pC_{(\pi)}\)
as the localized second image at every prime.
Thus either \(J=C\), or its failure is supported at finitely
many closed points on \(V(p)\).

There is an exact global criterion:
\[
J=C
\quad\Longleftrightarrow\quad
I_2\text{ is principal}
\quad\Longleftrightarrow\quad
A=C[r,Y],\quad pY=r^2+ar+b,\quad DY=2r+a
\quad(a,b\in C).
\tag{25}
\]
For the nontrivial implication, choose \(D^2Y=2p\).
The formula for \(F_1\) gives \(DY=2r+a\), and one integration
gives the invariant coefficient \(b\).
At each height-one base prime, the local lifting/saturation proof
makes \(C[r,Y]\) equal to the full local ring.
Globally its monic quadratic relation has free \(C\)-basis
\(\{Y^k,rY^k:k\ge0\}\). Expanding an element of \(A\)
in that generic basis, local equality puts every coefficient in
every \(C_{(\pi)}\), hence in \(C\). This proves full generation.

The [complete second-image proof](research/second-image-gluing-pass46.md)
does not prove \(J=C\). An ideal such as \((u,v)\) has no
height-one support without being the whole ring; it is a module
warning, not a realized obstruction for this frame.
The distinction is consistent with (22): the embedded local
rings determine \(A\), but fitting them into a chosen global
quadratic equation is an additional condition.

Even that equation would not automatically identify \(A\) as
affine space. Both principality and hypersurface recognition need
further input. The image-ideal literature supplies relevant
terminology and restricted results, not a theorem satisfying
the missing intrinsic hypotheses here.[^5]

## 10. The remaining proof obligations

| Branch or reduction | Established restriction | Unresolved step |
| --- | --- | --- |
| Moving highest parameter | Both good derivatives must be complex-linearly independent; the dependent rotating branch also satisfies \(R_1\mid G_0\) | Exclude or recognize the remaining actual moving frames |
| Independent moving correction | Global polynomial commutation and zero divergence | Prove local nilpotence from the full frame, or find another recognition route |
| Independent degree-two divisors | Full quadratic local models; a global equation exactly when \(I_2=pC\) | Remove the possible finite second-image obstruction, then recognize the hypersurface |
| General cancellation | Several supplied low-height profiles are recognized | Produce a sufficient actual frame for every original sliced action |

A finite calculation cannot discharge these universal obligations.
An infinite family of nonzero iterates can refute a proposed LND;
a bounded vanishing test cannot prove local nilpotence in general.
The residue field and minimal slice now give the local quadratic
equation. They still do not give one compatible global coordinate
system for \(A\).

The next useful arguments must use information absent from the
controls: the complete moving coordinate identities, compatibility of the
embedded divisor algebras in the generic line, or a genuine
unrestricted coordinate-reduction principle. Repeating the existing
tests without a new implication would not reduce these gaps.

## Sources

[^1]: Shigeru Kuroda, [*Initial forms of stable invariants for additive group actions*](https://arxiv.org/pdf/1304.0313v2), Proposition 3.2, PDF p. 8, states the binary-invariant theorem credited to Daigle--Freudenburg. It does not assume preservation of the entire plane. The curve parameter input is Michiel de Bondt, [*Rational maps H for which K(tH) has transcendence degree 2 over K*](https://arxiv.org/pdf/1501.06046v4), Corollary 3.2 and Lemma 3.3, PDF pp. 20--21.

[^2]: S. M. Bhatwadekar, Neena Gupta and S. A. Lokhande, [*Some K-theoretic properties of the kernel of a locally nilpotent derivation on k[X1,...,X4]*](https://arxiv.org/pdf/1501.01438v1), Theorem 3.5 and preceding Proposition 3.3, PDF pp. 10--11. The complete inherited commuting criterion uses Stefan Maubach, [*The Commuting Derivations Conjecture*](https://www.math.ru.nl/~maubach/Papers/The_Commuting_Dervations.pdf), Theorem 2.4 and Propositions 3.2, 3.4, 3.6, with their explicitly stated complex-surface and plane-theorem inputs.

[^3]: Daniel Daigle and Shulim Kaliman, [*A note on locally nilpotent derivations and variables of k[x,y,z]*](https://www.math.miami.edu/~kaliman/library/canada.daigle-kaliman.pdf), Theorem 1.5, Canadian Mathematical Bulletin 52 (2009), p. 539, supplies the source plinth mechanism. Its precise intrinsic faithfully-flat application and finite-generator primitive extension are reconstructed in [the plinth proof](research/intrinsic-plinth-boundary-pass27.md). The new local residue/support argument is supplied in full above and in the all-prime note.

[^4]: Shulim Kaliman, [*Free C+-actions on C3 are translations*](https://www.math.miami.edu/~kaliman/library/Ka.invent.2004.c%2B.pdf), final author manuscript, Lemma 2.2, Proposition 3.2 including Step 2, Theorem 5.2 and Remark 5.4. These statements have smooth factorial threefold hypotheses with \(H_2=H_3=0\), rather than an assumption that the threefold is already affine space.

[^5]: Nikhilesh Dasgupta and Animesh Lahiri, [*On image ideals of nice and quasi-nice derivations over a UFD*](https://arxiv.org/pdf/2302.13787v3), version 3, December 9, 2023, Introduction and Section 3. That version states the general image-ideal principality question on an actual polynomial three-ring as Freudenburg's Freeness Conjecture and proves results for specified relative polynomial-plane derivations. Those hypotheses have not been established for this intrinsic action; no conclusion about the conjecture's subsequent status is inferred.
