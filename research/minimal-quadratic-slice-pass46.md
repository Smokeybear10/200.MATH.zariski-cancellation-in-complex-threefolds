# A quadratic residue field determines the full divisor model

For the primitive intrinsic action, a residue cover of degree two
already forces the full quadratic DVR presentation. The missing
simultaneous-speed case does not require a new localized slice for
the original four-variable action. A finite correction of an actual
minimal intrinsic slice supplies the presentation instead.

Combined with the preceding degree theorem, this classifies every
codimension-one intrinsic degeneration in a still-unrecognized
degree-two independent-defect frame. It does not supply a global
polynomial coordinate system or prove that the resulting divisor
models glue to a polynomial three-ring.

## 1. Precise local hypotheses

Let \(C\simeq\mathbb C^{[2]}\) be the kernel of a primitive
nonzero LND \(D\) on the actual intrinsic ring \(A\). Retain
the inherited factoriality, faithful flatness and principal full
plinth from [the residue-degree proof](quadratic-residue-degree-pass46.md):
\[
\operatorname{pl}(D)=pC,\qquad Dr_*=p.
\tag{1}
\]
Fix an irreducible \(\pi\in C\) dividing \(p\), and put
\[
R=C_{(\pi)},\quad L=\operatorname{Frac}C,\quad
\kappa=R/\pi R,\quad n=v_\pi(p)\ge1.
\]
Write \(p=u\pi^n\), where \(u\in R^*\), and choose the
actual element \(r=r_*/u\in A_R\). Then
\[
Dr=\pi^n,\qquad \operatorname{pl}(D|_{A_R})=\pi^nR,
\qquad (A_R)_\pi=L[r].
\tag{2}
\]
Here the subscript \(\pi\) on \((A_R)_\pi\) means inversion
of \(\pi\); \(A_R\) itself means invariant localization at
the height-one base prime.

Suppose the entire residue curve is
\[
\overline A=A_R/\pi A_R=F[t],\qquad
\ker\overline D=F,\qquad [F:\kappa]=2.
\tag{3}
\]
The preceding note proves these full-ring statements in the
remaining actual frame. They are not assertions about the smaller
image of the bad-coordinate subring.

**Theorem.** There are \(T,Z\in A_R\) and \(\eta\in R^*\)
such that
\[
A_R=R[T,Z]\simeq
R[\mathsf T,\mathsf Z]/
(\pi^n\mathsf Z-\mathsf T^2+\eta),
\qquad \bar\eta\notin\kappa^{*2},
\tag{4}
\]
and
\[
DT=\pi^n,\qquad DZ=2T.
\tag{5}
\]
The exponent is the valuation of the full primitive plinth,
not merely the denominator of a selected generator.

## 2. Minimality makes the residue of the slice a primitive element

Since \(n\ge1\), \(\bar r\) lies in \(\ker\overline D=F\).
It does not lie in \(\kappa\). Otherwise lift its value to
\(a\in R\). Then \((r-a)/\pi\in A_R\) has derivative
\(\pi^{n-1}\), contradicting the exact localized plinth in (2).
As \([F:\kappa]=2\), this proves
\[
F=\kappa[\bar r].
\tag{6}
\]
Choose a monic polynomial \(P_0(\mathsf T)\in R[\mathsf T]\)
of degree two lifting the minimal polynomial of \(\bar r\)
over \(\kappa\). Its reduction is irreducible and separable.
Consequently \(P_0(r)\in\pi A_R\), and
\(P_0'(\bar r)\in F^*\).

## 3. A finite valuation correction reaches exactly the plinth exponent

Consider any monic quadratic \(P\in R[\mathsf T]\) with
\(\bar P=\bar P_0\), and set
\(\ell=v_\pi(P(r))\ge1\), where the valuation is in the
UFD \(A_R\). It is finite because \(r\) is transcendental
over \(L\), and \(\pi\) is a nonunit prime of \(A_R\).

One always has \(\ell\le n\). Indeed
\[
D(P(r))=\pi^nP'(r),
\tag{7}
\]
and \(P'(r)\notin\pi A_R\). If \(P(r)\) were divisible
by \(\pi^{n+1}\), its derivative would be too, because
\(D\pi=0\), contradicting (7).

If \(\ell<n\), let \(z=P(r)/\pi^\ell\in A_R\).
Equation (7) gives
\[
Dz=\pi^{n-\ell}P'(r),\qquad \overline D\bar z=0.
\]
By (6), there are \(\bar a,\bar b\in\kappa\) with
\(\bar z=\bar a\bar r+\bar b\). Lift them to \(a,b\in R\),
and replace \(P\) by
\[
P_{\rm new}(\mathsf T)
=P(\mathsf T)-\pi^\ell(a\mathsf T+b).
\tag{8}
\]
This remains monic quadratic, keeps the same reduction modulo
\(\pi\), and satisfies
\(v_\pi(P_{\rm new}(r))\ge\ell+1\).
The new valuation still cannot exceed \(n\), by (7).

Thus at most \(n-1\) such corrections produce a monic
quadratic \(P\) with
\[
P(r)=\pi^nY,\quad Y\in A_R,\qquad DY=P'(r).
\tag{9}
\]
This is a finite calculation inside \(R\) and \(A_R\).
It does not use a Henselian ring, an infinite power series, or
an algebraization theorem.

## 4. The corrected two-generator subring is the whole local ring

Let \(H=R[r,Y]\subset A_R\). Its exact presentation is
\[
H\simeq R[\mathsf T,\mathsf Y]/
(\pi^n\mathsf Y-P(\mathsf T)).
\tag{10}
\]
To check exactness, the displayed relation is primitive as a
polynomial over the UFD \(R\), since \(\bar P\ne0\), and
is irreducible after passing to \(L\). It is therefore prime
in \(R[\mathsf T,\mathsf Y]\), and its quotient injects
into \(L[r]\). The map in (10) becomes an isomorphism after
inverting \(\pi\), so this prime presentation is its full
kernel before localization as well.

Modulo \(\pi\), (10) gives
\[
H/\pi H=\kappa[\bar r,\bar Y]=F[\bar Y].
\tag{11}
\]
The map from this presented polynomial ring to \(\overline A\)
is injective: \(\bar r\) has minimal polynomial \(\bar P\),
and \(\overline D\bar Y=P'(\bar r)\in F^*\) makes
\(\bar Y\) transcendental over \(F\). More precisely,
\(\overline D\) is a nonzero constant multiple of
\(\partial_t\) on \(F[t]\), so (9) makes \(\bar Y\)
an affine-linear parameter of that entire line. Thus (11)
also equals \(\overline A\).

In particular
\[
H\cap\pi A_R=\pi H.
\tag{12}
\]
Now \(H\subset A_R\subset H[1/\pi]=L[r]\), by (2).
For \(a\in A_R\), choose the smallest \(k\ge0\) with
\(\pi^ka\in H\). If \(k>0\), this element belongs to
\(H\cap\pi A_R\), so (12) allows one factor of \(\pi\)
to be cancelled inside \(H\), contradicting minimality.
Therefore \(k=0\) for every \(a\), and \(A_R=H\).

Finally write \(P(\mathsf T)=\mathsf T^2+a\mathsf T+b\).
Set \(T=r+a/2\), \(Z=Y\), and \(\eta=a^2/4-b\).
Irreducibility of \(\bar P\) makes \(\bar\eta\) a nonzero
nonsquare. Equations (4) and (5) follow.

### 4.1. The exact separable primitive-element generality

The finite correction uses degree two only to establish (6) and
to express every residue correction as a linear polynomial in
\(\bar r\). More generally, under (2) and a full residue line
\(F[t]\), suppose \(F/\kappa\) is finite separable of degree
\(d\) and \(F=\kappa[\bar r]\). Start with its monic
degree-\(d\) minimal polynomial. At each step, express the
invariant residue of \(P(r)/\pi^\ell\) as a polynomial of
degree less than \(d\) in \(\bar r\), lift its coefficients
to \(R\), and subtract \(\pi^\ell\) times that polynomial.
The leading coefficient and the separable reduction stay fixed.
The same valuation bound, presentation, full residue-line
argument and saturation prove
\[
A_R=R[r,Y],\qquad \pi^nY=P(r),\qquad
\deg P=d,\quad P\text{ monic},\quad DY=P'(r).
\tag{12a}
\]
If \(d\) is prime, minimality already gives
\(\bar r\notin\kappa\), so the tower degree forces
\(F=\kappa[\bar r]\). For composite degree this primitive-
element condition is an additional hypothesis on the *actual
minimal slice*, not a consequence of separability alone. Only
the quadratic case is needed for the actual-frame conclusion.

## 5. Consequence for all the actual divisor primes

The [preceding degree theorem](quadratic-residue-degree-pass46.md)
proves that either \(A\simeq\mathbb C^{[3]}\) is already
recognized, or every primitive plinth prime has residue degree
two. In the latter case the present theorem supplies (4) at
**every** primitive plinth prime, including those dividing all
of \(p,f,g,h_1,h_2\). At a prime not dividing \(p\), the
ordinary local slice gives \(A_R=R[t]\).

The normalized global determinant bound
\(p\mid\Delta\), established in
[the acceleration extension](acceleration-divisor-extension-pass45.md),
still applies. Hence each quadratic model has
\[
1\le n=v_\pi(p)\le v_\pi(\Delta).
\tag{13}
\]
The [monodromy theorem](quadratic-monodromy-pass46.md) restricts
the normalized square class of \(\bar\eta\) to \(u-b\)
up to a rational square. It neither fixes the coefficient
\(\eta\) modulo higher powers of \(\pi\) nor identifies
the local coordinates for different primes.

## 6. The remaining global obligation

The codimension-one models are subrings of the same generic line
\(A_L=L[r_*]\). Abstract isomorphisms with (4) do not give a
common polynomial presentation over \(C\): their linear
translations of \(r_*\), quadratic coefficients and denominator
corrections must be compared in that fixed generic ring.

There is no hidden extra normality datum in codimension two once
all these *embedded* subrings are known. Precisely,
\[
A=\bigcap_{\pi\in C\text{ irreducible}} A_{C_{(\pi)}}
\quad\text{inside }A_L.
\tag{14}
\]
There is a direct denominator proof in the actual UFD. Write
\(a=b/c\in A_L\), with \(b\in A\) and \(0\ne c\in C\).
For each prime factor \(\pi\) of \(c\), membership in
\(A_{C_{(\pi)}}\) expresses \(a=b_\pi/d_\pi\), where
\(b_\pi\in A\), \(d_\pi\in C\), and \(\pi\nmid d_\pi\).
The element \(\pi\) stays prime in \(A\), and it still does
not divide \(d_\pi\), by factorial closure. Comparing the
\(\pi\)-valuation in \(d_\pi b=cb_\pi\) shows that
\(v_\pi(b)\ge v_\pi(c)\). All prime factors of \(c\)
therefore cancel in \(A\), so \(a\in A\). This proves (14)
without a separate codimension-two extension assumption.

Equation (14) is an exact reconstruction requirement, not a
polynomiality theorem. The supplied full-frame identities control
generic quadratic graph coefficients, determinant denominators,
and the residue field degrees. The arguments here do not construct
compatible global polynomial generators of this intersection.
In particular they do not prove that the separately chosen
coefficients in (8) descend to one common quadratic equation over
\(C\), or that such an equation, if obtained, defines a
polynomial three-ring. The known polynomial quadratic models
already show that nonempty plinth support need not disappear.

The previous residue note is left unchanged as an intermediate
result; the extra finite correction (8) is the additional gate
that upgrades its field conclusion to a full local presentation.

## Attribution and verification boundary

The principal full plinth, primitive residue line and original
actual-frame degree theorem are inherited and explicitly linked.
The remaining proof is finite valuation correction, the prime
presentation and saturation argument already used in pass 45,
and elementary prime-denominator cancellation in the actual UFD.
No new external classification theorem or
historical novelty is claimed. No actual previously unresolved
frame example or unrestricted cancellation theorem is asserted.

The standalone [three-method checker](minimal_quadratic_slice_checks_pass46.py)
independently reconstructs finite corrections for perturbed minimal
slices in the exact models \(\pi^nZ=T^2-u\), \(1\le n\le6\).
It checks the separable derivative stopping, actual inverse and
relation transport, and a nonsaturated subring with the same generic
ring but a noninjective residue map. Its first run passed three
methods in 0.560 seconds; an independent full-read rerun passed
three in 0.555 seconds. These bounded controls do not replace the
universal valuation and denominator arguments above.
