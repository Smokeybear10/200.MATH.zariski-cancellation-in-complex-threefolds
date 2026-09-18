# Independent audit of the CRT local-slice extension

The algebraic sufficiency proof in Sections 8–9 of
[the nonunit local-slice note](nonunit-local-slice-pass20.md) survives
this audit. No failed divisibility or counterexample was found. The
arbitrary-multiplier theorem retains its stronger coefficient premise;
it does not classify all slice extensions for arbitrary multipliers.

## 1. Primewise correction, including roots away from zero

For \(g=f-\lambda\) and \(g^v\Vert a\), the formulas themselves,
before division by \(h\), give
\[
R_*\equiv hQ,
\qquad k\equiv h^{d-1}Q^d\pmod{g^v}.
\]
The lower homogeneous terms contain \(af^n\), so this holds also
when \(\lambda\ne0\), where \(f\) is a unit. The premise
\(B=1+\operatorname{rad}(af)kJ\) gives a scaling factor congruent
to one modulo \(g\). Its polynomial inverse exists in the finite
nilpotent coefficient ring. The forward and inverse curve identities
therefore kill the respective first reverse numerator modulo
\(g^v\). This works for \(Q=0\) and for nonprimitive replicas
as well; minimality of the displayed local slice is not used.

Polynomial CRT is applied to finitely many coefficient polynomials in
the curve parameter. It yields one polynomial representative meeting
all the congruences, not an infinite formal series.

## 2. The second denominator and the global inverse

Every \(f-\lambda\) is prime in the old surface ring because
\[
\mathbb C[x,h,r]/(xh-K_n(\lambda,r))
\]
is a domain. The polynomial \(K_n(\lambda,r)\) is monic and
nonzero; its irreducibility in \(r\) is not required for this claim.
The relevant recovered \(h\)-coordinate reduces to the independent
\(h\)-coordinate modulo \(g\), so is not divisible by that prime.
Consequently the identity
\(\widehat hN_x=a^dK_n(f,\widehat r)\) forces the full
\(g^{dv}\)-divisibility of \(N_x\), one prime factor at a time.
The independent inverse uses the same argument. No UFD assumption
on the surface and no cancellation in a nilpotent quotient is needed.

The Bezout matrix exists since \((A,B)=1\) and \(B\) is one
modulo every prime dividing \(af^nk\). Its inverse coefficient
satisfies \(V-1\in(k)\), which makes the displayed inverse
\(h\)-formula polynomial even before reducing modulo \(a\).
Both compositions are ordinary inverse identities after inverting
\(af\), and hence hold globally in the domain surface rings.
The note now states this localization explicitly.

## 3. The zero-order case and the physical P-jet

If \(e=\operatorname{ord}_f a=0\), then \(a\) is a unit in
every finite \(f\)-adic coefficient ring. The imposed congruence
\(\widetilde Q\equiv Q\pmod f\), together with \(B\equiv1\),
therefore gives the identity reduction of all three surface coordinates.
No extra normal-displacement argument is needed in this case.

If \(e>0\), write \(a=f^eu\) with \(u(0)\ne0\).
The extra \(f^{e+1}\) congruence retains \(ar\), rather than
only annihilating it. The unit \(u\) is invertible in the finite
coefficient ring. The first reverse numerator is divided by \(a\)
only after this stronger congruence has been established.

The parameter-dependent differences have factors \(af^n\) in
the \(h\)-coordinate and \(f^n\) after the first reverse
division. The surface identity supplies the same independence for
the \(x\)-coordinate. Vertex preservation follows from the explicit
factor \(h\) in the middle correction, followed by the degree-one
part of the cone equation. These checks apply to the inverse too.
Thus the pass-19 finite curve lemma legitimately supplies both
\(P\)-jet identities. The Taylor identity then clears the final
physical denominators in the independent polynomial ring.

## 4. Exact scope and the contrasting family

The stronger premise (27) is sufficient, not necessary in general.
For \(d=2,Q=c\ne0\), the shift \(P\mapsto P+a/c\)
identifies the construction with the earlier base and gives plinth
\(f^nk\), even if \(a\) has roots away from zero. Such roots
must not be added to the actual plinth merely because the displayed
local-slice derivative contains them.

For the separately treated \(a=f-1,Q=h\), both residue-degree
tests check: at \(f=1\), the degrees are \(2d-1>2\); at
\(f=0\), they are \((2d-1)D_0>2D_0\). The residues are
transcendental, so these tests exclude both invariant coefficient
poles and degree-one cancellations. The checks excluding common
factors \(f\), \(f-1\), and \(k\) are valid. Thus the
stated kernel, primitive derivation, and full plinth follow in this
family. Necessity for its slice coefficients still uses the earlier
source-dependent affine-replacement theorem.

## 5. Verification record

The full main note and the pass-19 finite curve lemma were read.
The six-method checker was rerun successfully, including its CRT
control for \(a=f^2(f-1)^2\) and independent inverse congruences
at both primes. That finite run supplements the preceding general
algebra audit; it is not a formal proof.

Two exposition points were resolved: the verification boundary now
distinguishes (13) for powers of \(f\) from (27) for CRT, and
the CRT composition argument explicitly localizes at \(af\).
No change to registries or novelty status is justified by this audit.
