# A global degree minimizer with nonsliced primitive top

The remaining assertion from pass 31 is false. For the **same**
canonical vertical action and the full class of horizontal LNDs fixing
\(x\), a horizontal of globally minimal degree one can have a
primitive highest coefficient with no slice. Both coordinate maps are
polynomial, with explicit inverses. No passage to a rational chart is
being treated as a global automorphism.

The primitive bad top is the original nonunit-plinth rank-two
derivation, up to an elementary shift. Thus the failure survives taking
the primitive part. A good degree-one minimizer still exists by pass 31.
This disproves universal success of a degree minimizer, not existence
of a successful choice and not cancellation.

## 1. Fixed input and exact assertion

Retain the actual canonical local-slice model
\[
R=\mathbb C[x,y,z],\quad D=x^2\partial_y+2y\partial_z,
\quad r=y,\quad p=x^2,\quad d=x,
\]
\[
B=R[\lambda,w]/((1+\lambda x)w-y)
 =\mathbb C[x,\lambda,w,z],\qquad v=1+\lambda x,
\]
\[
\Delta x=\Delta\lambda=0,\qquad
\Delta w=x^2,\qquad \Delta z=2v^2w.
\tag{1}
\]
The input is primitive, its full plinth is the nonunit ideal
\(x^2\ker D\), and \(d\in\sqrt{p\ker D}\) but \(p\nmid d\).
These are the unchanged hypotheses proved in
[pass 28](canonical-top-pass28.md).

For
\[
\mathcal H_x=\{\delta\in\operatorname{LND}(B):
                          \delta x=0,\ \delta\lambda=1\},
\]
let \(q(\delta)\) be the degree of \(\Delta\) in the actual
\(\delta\)-slice coordinates. Equivalently it is the largest
\(j\) with \((\operatorname{ad}\delta)^j\Delta\ne0\).
[Pass 31](minimal-horizontal-pass31.md) proved, on this full class,
\[
\min_{\delta\in\mathcal H_x}q(\delta)=1.
\tag{2}
\]
Its zero-degree exclusion does not assume triangular preservation.

**Counterexample theorem.** There exists an actual
\(\delta_{\mathrm{bad}}\in\mathcal H_x\) with \(q=1\) whose
primitive top is
\[
L=x^2\partial_b+(2b+3x/2)\partial_c.
\tag{3}
\]
This is primitive, is locally nilpotent, and has no slice.
Its full plinth is \(x^2\mathbb C[x,J]\), where
\(J=x^2c-(b+3x/4)^2\).

## 2. A determinant-one matrix on the local-slice data

In a second polynomial ring \(\mathbb C[x,\lambda,b,c]\), set
\[
\alpha=\frac23,\qquad
u=1+\alpha\lambda x,\qquad
P=(1-\alpha\lambda x)(1+\alpha^2\lambda^2x^2),\qquad
e=\alpha^4\lambda^3x^2,
\]
\[
H_0=x^2c-b^2.
\tag{4}
\]
The elementary matrix identity
\[
Pu+e\lambda x^2=1
\tag{5}
\]
holds even with \(\alpha\) an indeterminate. Define
\[
W=P b+eH_0,\qquad
H=uH_0-\lambda x^2b,\qquad
Z=\frac{H+v^2W^2}{x^2}.
\tag{6}
\]
No inverse of \(u\) or \(P\) occurs.

The last quotient in (6) is a polynomial. Indeed modulo \(x^2\),
\[
W\equiv(1-\alpha\lambda x)b,\qquad
H\equiv-(1+\alpha\lambda x)b^2,
\]
so
\[
H+v^2W^2\equiv(2-3\alpha)\lambda x b^2\pmod{x^2}.
\tag{7}
\]
The residue vanishes for the actual value \(\alpha=2/3\).
This is global divisibility in a polynomial ring, not evaluation
on a grid or division only where \(x\ne0\).

The inverse formulas use the physical invariant
\[
I=x^2z-v^2w^2
\]
and are
\[
b=u w-eI,\qquad
H_0=\lambda x^2w+P I,\qquad
c=\frac{\lambda x^2w+P I+(u w-eI)^2}{x^2}.
\tag{8}
\]
The inverse quotient is also a polynomial. Its numerator has
residue
\[
(3\alpha-2)\lambda x w^2\pmod{x^2}.
\tag{9}
\]
Again the coefficient vanishes exactly at the chosen \(\alpha\).

To verify both full inverse compositions, first use the
determinant-one inverse
\[
\begin{pmatrix} W\\H\end{pmatrix}
=
\begin{pmatrix}P&e\\-\lambda x^2&u\end{pmatrix}
\begin{pmatrix}b\\H_0\end{pmatrix},
\qquad
\begin{pmatrix}b\\H_0\end{pmatrix}
=
\begin{pmatrix}u&-e\\\lambda x^2&P\end{pmatrix}
\begin{pmatrix}W\\H\end{pmatrix}.
\tag{10}
\]
Under (6), the physical \(I\) becomes \(H\). Consequently (10)
recovers \(b,H_0\), and \(x^2c=H_0+b^2\) recovers \(c\).
Conversely (8) recovers \(w,I\), and \(x^2z=I+v^2w^2\)
recovers \(z\). Cancellation of \(x^2\) is valid in each
polynomial domain, after both quotients have already been shown
to be polynomial. Thus these are actual inverse automorphisms
over \(\mathbb C[x,\lambda]\). At \(\lambda=0\) they are the
identity.

## 3. The canonical action in the new polynomial frame

Define on the second polynomial ring
\[
D_0=x^2\partial_b+2b\partial_c,\qquad
\widetilde\Delta=uD_0+\lambda x^2\partial_c.
\tag{11}
\]
This is triangular and locally nilpotent. It fixes \(x,\lambda\),
and directly
\[
\widetilde\Delta b=ux^2,\qquad
\widetilde\Delta c=2ub+\lambda x^2,\qquad
\widetilde\Delta H_0=\lambda x^4.
\tag{12}
\]
Equations (5)-(6) now give the three exact identities
\[
\widetilde\Delta W=x^2,\qquad
\widetilde\Delta H=0,\qquad
\widetilde\Delta Z=2v^2W.
\tag{13}
\]
For the last one, differentiate the defining numerator in (6)
and cancel \(x^2\). Hence the inverse polynomial maps from
Section 2 conjugate (11) to the **fixed** canonical action (1).
The target is not just another triangular LND with a similar
plinth.

Define \(\delta_{\mathrm{bad}}\) on the physical ring by
transporting the coordinate partial \(\partial_\lambda\) from
the frame \((x,\lambda,b,c)\) through this verified isomorphism.
Explicitly, for a physical polynomial \(f\), substitute
\((w,z)=(W,Z)\), differentiate in \(\lambda\) while fixing
\(x,b,c\), then substitute the polynomial inverse (8).
This specifies a polynomial derivation with no unresolved
denominators. It is an actual coordinate LND, with
\(\delta_{\mathrm{bad}}x=0\) and
\(\delta_{\mathrm{bad}}\lambda=1\).

In its slice coordinates, the fixed vertical action is exactly
\[
\widetilde\Delta
=D_0+\lambda D_1,\qquad
D_1=\frac23xD_0+x^2\partial_c
    =\frac23xL.
\tag{14}
\]
It follows that
\[
[\partial_\lambda,\widetilde\Delta]=D_1\ne0,\qquad
[\partial_\lambda,D_1]=0.
\]
Thus \(q(\delta_{\mathrm{bad}})=1\). Equation (2) proves that
this is a global minimizer over the full stipulated class.

## 4. Primitivity, full plinth, and failure of a slice

The coefficients of (3) have gcd one:
\[
\gcd(x^2,2b+3x/2)=1.
\]
After the polynomial coordinate shift \(b'=b+3x/4\), the field
is precisely
\[
L=x^2\partial_{b'}+2b'\partial_c.
\tag{15}
\]
It is locally nilpotent and every image belongs to the proper
ideal \((x,b')=(x,b)\). Its fixed locus contains the entire
line \(x=b=0\), so no polynomial can have image one. In
particular the obstruction is present in the primitive field.

For completeness the exact plinth follows from the same
all-degree pole argument as the canonical input. Put
\(J=x^2c-b'^2\). After inverting \(x\),
\(L=x^2\partial_{b'}\) and
\[
\ker L=\mathbb C[x,J],\qquad
\ker L^2=\mathbb C[x,J]\oplus\mathbb C[x,J]b'.
\tag{16}
\]
To justify contraction in both identities, a highest possible
\(x\)-pole in the second has residue
\(A(-b'^2)+b'B(-b'^2)\). Its even and odd parts vanish only
if both coefficient polynomials vanish. Thus no negative
\(x\)-power survives. Formula (16) gives
\[
L(\ker L^2)=x^2\mathbb C[x,J]
          =L(\mathbb C[x,b,c])\cap\ker L.
\tag{17}
\]
There is neither a hidden unit plinth nor a slice concealed by
the chosen normalization of the top.

## 5. This horizontal is genuinely outside the triangular sector

The new example is not subject to the positive classification
from Section 4 of pass 31. One explicit physical coefficient
makes this visible. Write
\[
T=\alpha x(1-\alpha\lambda x+\alpha^2\lambda^2x^2),
\qquad
U=\alpha^4\lambda^2x^2
       (3-2\alpha\lambda x+\alpha^2\lambda^2x^2).
\]
Differentiating \(W\) and substituting (8) gives
\[
\delta_{\mathrm{bad}}w=-T w+U I.
\tag{18}
\]
Its coefficient of the original \(z\) is \(Ux^2\ne0\).
Thus \(\delta_{\mathrm{bad}}\) does not preserve
\(\mathbb C[x,\lambda,w]\).

For an independent direct coefficient check, put
\[
R_1=(1-\alpha)+(\alpha^2-\alpha)\lambda x
                         +\alpha^2\lambda^2x^2.
\]
The other physical coefficient is
\[
\delta_{\mathrm{bad}}z
=-w+Tz-2\lambda vR_1w^2+2(U/x^2)v^2wI,
\tag{19}
\]
where \(U/x^2\) is the polynomial already displayed in the
definition of \(U\). One also has
\(\delta_{\mathrm{bad}}I=-x^2w+TI\). These identities can be
checked directly against the inverse invariants (8).

It is nevertheless tangent to the reduced canonical fixed locus
\((x,w)\): (18) is divisible by \(x\), and
\(\delta_{\mathrm{bad}}x=0\). Tangency alone is therefore not a
criterion for success of the minimum-selection rule.

No canonical normalizing gauge fixing \(x,\lambda\) can move
this horizontal into the old pointwise \(F=2xz-w^2\)-fixing
sector. Such a gauge preserves \(q\), by conjugating every
iterated bracket and allowing only a nonzero constant rescaling
of \(\Delta\). Every member of that old sector has \(q\ge2\)
by pass 29, whereas the present one has \(q=1\). This argument
does not assert that the fixed-locus tangency obstruction from
pass 30 was sufficient; it was only necessary.

## 6. What has been ruled out

The two cases now have the same model, the same nonunit input
plinth, the same slice parameter, and the same globally minimal
degree:

| Horizontal | Relative degree | Primitive top |
| --- | --- | --- |
| \(\partial_\lambda+2\lambda w^2\partial_z\), pass 31 | \(1\) | \(\partial_c\), sliced |
| The inverse-coordinate construction (6)-(8) | \(1\) | \(L\) in (3), nonsliced |

Therefore minimizing relative coefficient degree alone does not
force a sliced primitive highest field, even with the full
polynomial-cylinder premise and all canonical nonunit-plinth
hypotheses present. The counterexample concerns the universal
claim about **every** minimizer. It leaves the known successful
minimizer intact.

It does not exclude a more discriminating selection rule,
additional bracket operations, or existence of useful intrinsic
actions for an unknown quotient. It gives no exotic
cancellation kernel and makes no assertion about whether an
unknown rank-three input admits the relevant horizontals.

## Verification, attribution, and stopping boundary

The standalone file
[unrestricted_minimum_checks_pass32.py](unrestricted_minimum_checks_pass32.py)
uses only unittest and SymPy. It checks the two formal
\(\alpha\)-remainders before specializing, the determinant,
actual polynomiality, both coordinate inverse compositions,
canonical-action intertwining, the actual degree-one top and
its primitive fixed-locus obstruction. These finite controls
support the global determinant-and-divisibility proof, rather
than replacing it with sample evaluations.

~~~sh
/opt/anaconda3/bin/python research/unrestricted_minimum_checks_pass32.py
~~~

The initial completed run passed all ten methods in 0.677 seconds.
It checks the explicit physical horizontal as well as the target
frame, including its first adjoint and its failure to preserve the
old triangular subalgebra. No formal symbolic identity or test failed
in this initial run.

The global minimum and positive control are inherited from
[pass 31](minimal-horizontal-pass31.md). The model and original
parity calculation are inherited from
[pass 28](canonical-top-pass28.md); the restricted-family bound
is [pass 29](horizontal-selection-pass29.md). The new
countercontrol is the exact matrix and its polynomial lifts,
whose proof is given in full above. A bounded primary-source
search on pencils of LNDs did not supply an applicable theorem;
no such classification is assumed in this proof. Search
non-results are not evidence of novelty.

An independent agent reconstructed both divisibilities,
the determinant-one inverse and all action identities, and
independently checked both full coordinate compositions before
this note was finalized. No cancellation solution, priority
claim, expert review, or proof-assistant certification is asserted.
