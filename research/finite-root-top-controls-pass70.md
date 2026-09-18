# Exact controls for finite-root normalization and descent

The finite-root proof uses ordinary coordinate partials extended to an
algebraic field, not coordinate partials in a newly chosen root variable.
It then proves that its root lies in the original fraction field before
using normality. The controls below test these distinctions. They do not
realize the full moving-top frame or replace the written field and
normality arguments.

The corresponding complete theorem is
[dependent-algebraic-root-top-pass70.md](dependent-algebraic-root-top-pass70.md).
Jet independently read that saved proof through EOF and reconstructed
all 20 equations for both orders three and four, clean. The review
included the actual extension ring and inverse-flow calculation,
the two-sided block descent, the common-constant argument and the
order of rational and polynomial root recovery. No fresh review of
every inherited primary-source proof is claimed.

## 1. Actual sliced actions with genuinely nonpolynomial adjoined roots

For each \(m\in\{3,4\}\), take the actual polynomial ring
\[
B=\mathbb C[a,b,x,s],\qquad
E=\partial_s+\frac{a s^{m-1}}{(m-1)!}\partial_x.
\tag{1}
\]
It is a polynomial LND with the original slice \(s\).
Indeed the actual coordinate replacement
\(j=x-a s^m/m!\), with inverse \(x=j+a s^m/m!\), makes
\(E=\partial_s\) on \(\mathbb C[a,b,j,s]\).
In the displayed original coordinates, its highest iterate is
\(E^m(a,b,x,s)=(0,0,a,0)\).

Adjoin \(g\) with \(g^m=a\). Here \(T^m-a\) is irreducible over
\(\mathbb C(a,b,x,s)\), for example by Eisenstein at \(a\).
Thus this is a genuine degree-\(m\) extension, and \(g\) is not
an element of the original polynomial ring.
Use
\[
L=\mathbb C(g,b,x,s),\quad R=\mathbb C[g,g^{-1},b,x,s],
\quad\delta=E/g.
\]
For this example \(R=B[g,g^{-1}]\) is explicitly a Laurent
polynomial ring. No such presentation is presumed in the general
finite-root theorem.

The extended original coordinate partials are
\[
T_a=\frac1{m g^{m-1}}\partial_g,\qquad
T_b=\partial_b,\quad T_x=\partial_x,\quad T_s=\partial_s.
\tag{2}
\]
They commute and evaluate on \((g^m,b,x,s)\) as the identity
matrix. In particular \(T_a\) is not \(\partial_g\).
The checker verifies the root differential relation and a rational
chain-rule expression before eliminating the original variable \(a\).

The actual divided flow on the extension is
\[
g\longmapsto g,\qquad b\longmapsto b,\qquad
s\longmapsto s+t/g,\qquad
x\longmapsto x+
\frac{g^m}{m!}\bigl((s+t/g)^m-s^m\bigr).
\tag{3}
\]
The inverse uses \(-t\). Both inverse orders, the flow differential
equation, and both multiplication orders of the original-partial
Jacobian and its conjugated-partial inverse are checked.
The determinant is one. This is an automorphism of the extension
ring with the time variable adjoined, not an automorphism fixing
the whole original fraction field.

The checker computes every successive original adjoint, rather than
inferring the heights from the coordinate flow degree. It obtains
\[
(\operatorname{ht}_E T_a,\operatorname{ht}_E T_b,
 \operatorname{ht}_E T_x,\operatorname{ht}_E T_s)
 =(m,0,0,m-1).
\tag{4}
\]
The divided adjoint profile is the same in this family.
Thus the cubic example has profile \((3,0,0,2)\), and the quartic
example has profile \((4,0,0,3)\).
Neither meets the required \((1,1,2,2)\) bound after assigning
the two zero-height directions as good. Their nonpolynomial roots
are not counterexamples to the full-frame descent theorem.
Their conjugated-partial matrices must retain these higher terms;
the checker does not truncate them to the target quadratic bound.

## 2. Root relation, constants and polynomial descent are separate gates

The defining equation need not be minimal. For a selected fourth
root of \(a^2\) with \(g^2=a\), the minimal polynomial is quadratic,
although the quartic relation is still legitimate to differentiate:
\[
\frac{T_a(a^2)}{4g^3}=\frac1{2g}=T_a g.
\tag{5}
\]
The checker verifies both the factorization distinction and this
differential identity. The complete proof uses the actual minimal
polynomial only where separability and its degree are required.

For the common-constant argument, differentiating a monic minimal
polynomial of a common invariant yields a lower-degree relation
whose coefficients must vanish. This is a written minimality
argument, not a finite test. Algebraic closedness of the complex
base then identifies an algebraic constant with a base constant.
The checker also considers \(Z^2-2\) over \(\mathbb Q\).
Its coefficients have zero derivatives and it is irreducible,
so a constant algebraic extension over that smaller base supplies
new constants. This deliberately changes the base field and
demonstrates why “algebraic over the constants” is not generally
the same as “already in the constants.”

The actual polynomial root-recovery identity is checked with
repeated factors retained. For
\[
H=(u+v^2)^2v^3,\qquad q=H^m,\qquad
z=\lambda H^{m-1},\quad \lambda\in\mathbb C^*,
\]
one has
\[
\lambda q/z=H,\qquad H^m=q.
\tag{6}
\]
These are exact coefficient controls. They do not prove by finite
examples that an arbitrary fraction-field root is in a normal ring.

Normality has its own exact boundary. In the nonnormal cusp ring
\[
A_0=\mathbb C[t^2,t^3],\qquad
q=t^m,\quad z=t^{m-1},\qquad m=3,4,
\]
both \(q,z\) belong to \(A_0\), and
\[
t=q/z\in\operatorname{Frac}A_0,\qquad t^m=q,
\quad t\notin A_0.
\tag{7}
\]
The last assertion is elementary: every nonconstant monomial in
\(t^2,t^3\) has degree at least two, so every such polynomial has
zero first derivative at zero, whereas \(t\) has derivative one.
The checker verifies the fraction and integral equations and that
chain-rule obstruction with an arbitrary formal function.
This control is not a polynomial-ring or full-frame example.

The common-constant and normality arguments are therefore distinct
from the finite differentiation and quotient identities checked here.
The full theorem also needs its nonzero constant bad component to
produce the fraction-field expression in the first place. That
component is not inferred from these examples.

## 3. Verification record and scope

[finite_root_top_checks_pass70.py](finite_root_top_checks_pass70.py)
has two methods and imports only unittest and SymPy.
Its first complete run passed both methods in 0.214 seconds,
exit zero, with no failed assertion.
A later bounded addition checks the quartic relation whose
chosen root has a quadratic minimal polynomial; it adds no method.
The complete run after that addition passed both methods in
0.217 seconds, exit zero. A final requested rerun passed both in
0.208 seconds, exit zero. Jet completed a full saved-file author
self-review of this note and every checker line, clean.
General independently read both files through EOF, reconstructed
their stated scope and identities, and reran the same two methods:
passed in 0.215 seconds, exit zero. Geometry also completed a full
independent read of both files and reran the two methods cleanly
in 0.212 seconds, exit zero. These executions are not
additional methods or suites.

An earlier direct symbolic diagnostic of the two adjoint profiles
was not another suite or additional method. The checker is not a
classification search, a proof-assistant certificate, or a test
of the full frame for a fabricated action. It does not add a
regression capture or any shared metadata.
Frozen pass69 and earlier artifacts remain unchanged.
