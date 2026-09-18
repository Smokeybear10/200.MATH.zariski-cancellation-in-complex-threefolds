# Invariant slice extensions and polynomial coordinate lifts

For the known rank-three family
\[
f=xz-y^2,\qquad r=-x^3-yf^n,\qquad
h=zf^{2n}+2x^2yf^n+x^5,\qquad
D_n=\operatorname{Jac}(f,h,\cdot),\quad n\ge1,
\tag{1}
\]
every invariant-coefficient extension \(E=AD_n+B\partial_t\) that has a
slice is a polynomial-coordinate translation. A finite correction modulo
\(f^n\) gives explicit invariant coordinates and a polynomial inverse,
including the nonreduced case \(n>1\). Section 8 extends that construction
to the entire published local-slice family, with arbitrary exponents
and a nonhomogeneous polynomial parameter.

A second, source-dependent working proof addresses arbitrary nonzero
locally nilpotent derivations \(D\) of a complex polynomial three-ring.
Writing \(C=\ker D\) and \(P_D=D(R)\cap C\), it gives
\[
\boxed{
AD+B\partial_t\text{ has a slice}
\iff AP_D+BC=C
\iff \text{it has a slice affine in }t .
}
\tag{2}
\]
This deduction uses a pointwise fiber argument built on Kaliman's
homology diagram. It does not assume the Freeness Conjecture.

Neither statement proves unrestricted complex threefold cancellation.
The coordinate construction is proved for (1) and the larger family (16); equation (2)
recognizes slices in a specified extension frame and does not recognize
their kernels as polynomial rings. No theorem here has human expert
review or proof-assistant verification, and no novelty is asserted.

## 1. The remaining cancellation question

The working target is
\[
X\times_{\mathbb C}\mathbb A^1\cong\mathbb A^4
\quad\Longrightarrow\quad X\cong\mathbb A^3.
\tag{3}
\]
The dimensional correction to the supplied statement remains unconfirmed.
All assertions below use the complex field explicitly.

Transporting translation along the cylinder in (3) produces a locally
nilpotent derivation \(E\) on \(\mathbb C^{[4]}\) with a slice \(s\),
meaning \(E(s)=1\). The slice identity gives
\(\mathbb C^{[4]}=(\ker E)[s]\). The unresolved task is to prove that
\(\ker E\cong\mathbb C^{[3]}\) for an arbitrary such \(E\), without assuming
a special polynomial coordinate frame.

An invariant extension has the additional presentation
\[
\mathbb C^{[4]}=R[t],\quad R=\mathbb C^{[3]},\quad
E|_R=AD,\quad E(t)=B,\quad A,B\in\ker D.
\]
This is a substantive restriction. No argument below shows that every
slice derivation admits it.

## 2. The known family and the exact image ideals

The derivations (1) are the \(m=2\), \(F(t_1,t_2)=t_1^2\) subfamily of
Dasgupta--Gaifullin's Theorem 5.7. Their rank is three and their kernel
and plinth are
\[
C=\mathbb C[f,h],\qquad P_{D_n}=f^nhC.
\tag{4}
\]
These facts are attributed to the published family, not claimed as new.[^1]
For \(n=1\), Freudenburg already computed an adapted basis in every
derivation degree and the associated graded algebra.[^2]

There is a uniform reconstruction of all higher image ideals:
\[
\boxed{
J_j=D_n^j(R)\cap C
=f^{\,n(j-\lfloor j/5\rfloor)}
 h^{\,\lceil j/2\rceil}C,\qquad j\ge0.
}
\tag{5}
\]
The \(n=1\) case recovers the known calculation. Priority for the
uniform extension and its coordinate application has not been established.

Here is the all-degree argument. Direct polynomial identities give
\[
D_nr=f^nh,\qquad
xh=r^2+f^{2n+1},\qquad
f^nS=rx^2+h,\quad S=x^2y+zf^n.
\]
Also
\[
q=h^2S-2r^3f^{n+1}-rf^{3n+2}
\quad\text{satisfies}\quad f^nq=r^5+h^3.
\]
These yield two exact presentations:
\[
R_f=C_f[x,r]/(r^2-hx+f^{2n+1}),\qquad
R_h=C_h[r,q]/(r^5-f^nq+h^3).
\tag{6}
\]
The inverses, including the denominator-free \(h\)-chart inverse, are
written in the [full reconstruction](research/nonreduced-rank-three-images-pass17.md).

Over \(C_f\), the normal-form basis \(x^a r^\epsilon\),
\(\epsilon\in\{0,1\}\), has distinct derivation degrees \(2a+\epsilon\).
Over \(C_h\), the basis \(r^i q^a\), \(0\le i<5\), has distinct degrees
\(i+5a\). With \(D_n=f^nh\partial_r\) over the invariant fraction field,
their leading coefficients give the two valuation bounds in (5).
Distinct degrees prevent cancellation between different basis elements.

The bounds are attained by actual global polynomials. Put
\[
(b_0,\ldots,b_9)=(1,r,x,rx,x^2,S,y,ry,xy,rxy).
\]
If \(j=10k+i\), \(0\le i<10\), then
\[
H_j=\frac{\epsilon_i}{j!}b_i z^k,\qquad
\epsilon_i=\begin{cases}1&i<6,\\-1&i\ge6,\end{cases}
\]
has \(D_n^jH_j\) equal to the generator in (5). This proves equality
without discarding an ideal supported at \(f=h=0\). In particular
\(J_{j+10}=f^{8n}h^5J_j\), and subtracting matching leading derivatives
gives an adapted \(C\)-basis of the whole ring.

## 3. Slice criterion and the nonreduced obstruction

For (1), the higher-image argument and the whole-component exclusion
from the preceding report already imply
\[
E\text{ has a slice}
\iff (Af^nh,B)C=C
\iff (A,B)C=C,\quad B=c+fhQ,\quad c\in\mathbb C^*.
\tag{7}
\]
The general result (2) gives a second route once its geometric input
is accepted. The independent family argument does not depend on that
new pointwise input.

To verify the last equivalence, a unit in \(C/(f^nh)\) restricts to a
nonzero constant on each reduced coordinate axis. Those constants agree
at their intersection. Conversely \(fhQ\) is nilpotent modulo \(f^nh\),
so \(c+fhQ\) has a finite geometric-series inverse there.

The distinction between \(fh\) and \(f^nh\) is essential. When \(n>1\),
\(B=1+fh\) is a unit modulo \(f^nh\) but is not congruent to a scalar
modulo that ideal. Thus the earlier matrix-lift theorem requiring
\(B\equiv1\pmod{f^nh}\) cannot be invoked.

For example, \(n=2\), \(A=1\), \(B=1+fh\) has the affine slice
\[
s=hr+(1-fh)t.
\]
The existence of this slice alone does not prove that its kernel is a
polynomial three-ring. The next section supplies the missing coordinates.

## 4. The finite-jet coordinate construction

Normalize \(c=1\) by replacing \(E,A,B\) with \(E/c,A/c,B/c\).
Both coefficients must be scaled. Choose \(U,V\in C\) such that
\[
Af^nhU+BV=1.
\]
Set
\[
g=f^nh,\quad \rho=Br-Agt,\quad s=Ur+Vt.
\]
Then \(E\rho=0\), \(Es=1\), and
\(r=V\rho+Ags,\ t=-U\rho+Bs\).

Define
\[
X=\frac{\rho^2+f^{2n+1}}{h}.
\tag{8}
\]
This is polynomial: expanding the numerator uses the original relation
\(xh=r^2+f^{2n+1}\), and the only extra quotient is
\((1-B^2)/h\), which is polynomial. Also \(X\equiv x\pmod f\).

In \(\mathbb C[X,f]/(f^n)\), construct the unique \(J\equiv1\pmod f\)
satisfying
\[
J=B(f,X^5J^2)^{-5},\qquad F(X,f)=X^2J(X,f).
\tag{9}
\]
The inverse power is a truncated binomial polynomial. Starting with
\(J_0=1\), apply the right side \(n-1\) times, reducing modulo \(f^n\)
at each step. Because \(B(f,H)-1\) is divisible by \(f\), a difference
divisible by \(f^k\) becomes divisible by \(f^{k+1}\). This proves
finite termination and uniqueness, including after specialization to
any algebra with \(f^n=0\).

Now put
\[
Y=-\frac{\rho+XF}{f^n},\qquad
Z=\frac{h+2\rho F+XF^2}{f^{2n}}.
\tag{10}
\]
Both are polynomials. Modulo \(f^n\),
\[
r=-x^3,\quad h=x^5,\quad \rho=Br,\quad X=B^2x,
\]
and therefore
\(\rho=-B^{-5}X^3,\ h=B^{-10}X^5\).
Uniqueness in (9) makes \(J=B^{-5}\) in this quotient, proving the
divisibility for \(Y\). For \(Z\), the identity
\[
X(h+2\rho F+XF^2)
=(\rho+XF)^2+f^{2n+1}=f^{2n}(Y^2+f)
\]
and \(\gcd(X,f)=1\) prove divisibility in the polynomial UFD.

The invariant coordinates satisfy
\[
f=XZ-Y^2,\quad
\rho=-XF-Yf^n,\quad
h=XF^2+2YFf^n+Zf^{2n}.
\tag{11}
\]
A polynomial inverse is essential here. In the independent ring
\(\mathbb C[X,Y,Z,s]\), define \(f,\rho,h\) by (11), and use the
inverse matrix for \(r,t\). Then
\[
W=\frac{V-1}{h}\rho+Af^ns,\qquad x=X+W(r+\rho)
\]
are polynomials. The Bezout relation makes \(V-1\) divisible by \(h\).
One has \(xh=r^2+f^{2n+1}\) and, modulo \(f^n\),
\[
V=B^{-1},\quad r=-VXF,\quad x=V^2X,\quad F=V^5X^2.
\]
Consequently
\[
y=-\frac{r+x^3}{f^n},\qquad
z=\frac{h+2x^2r+x^5}{f^{2n}}
\]
are polynomial by the same numerator-square and coprimality arguments.
Substitution returns all original coordinates. The resulting surjection
between two polynomial four-rings is injective by dimension.
Thus \(R[t]=\mathbb C[X,Y,Z,s]\) and \(E=\partial_s\).

The [complete coordinate proof](research/nonreduced-coordinate-lift-pass17.md)
keeps the forward and inverse divisibility arguments separate. No use of
cancellation is hidden in the proof of coordinate generation.

## 5. A relative lift is genuinely impossible in a subfamily

The construction changes the polynomial expression of \(h\). That is
necessary for \(n\ge2,\ A=1,\ B=1+fh\): there is no isomorphism
\(R\cong\ker E\) fixing the common subring \(\mathbb C[f,h]\).

The exact \(h\)-localized kernel chart is
\[
(\ker E)_h\cong
\mathbb C[h,h^{-1},f,\rho,Q]/
\bigl(f^nQ-\rho^5-(1+fh)^5h^3\bigr).
\tag{12}
\]
For clarity, this is obtained by an invertible polynomial change, not
an assumed commutation of invariants and specialization. With
\(U=(-1)^nh^{n-1}\) and \(V=\sum_{j=0}^{n-1}(-fh)^j\), the first
invariant chart generator is
\[
\bar q=q-\frac{(V\rho+gs)^5-(V\rho)^5}{f^n}.
\]
It satisfies \(f^n\bar q=V^5\rho^5+h^3\). Setting
\[
W=\frac{1-(BV)^5}{f^n},\qquad Q=B^5\bar q+W\rho^5
\]
gives (12), with inverse \(\bar q=V^5Q+Wh^3\).

At \(h=b\ne0\), an isomorphism fixing \(f,h\) would identify the surfaces
\[
f^nq=r^5+b^3,\qquad
f^nQ=\rho^5+(1+bf)^5b^3
\tag{13}
\]
over \(\mathbb C[f]\). Poloni's Corollary 3.3(1) forces
\(\rho\mapsto\alpha r+\beta(f)\), with \(\alpha\) a nonzero constant.[^3]
Modulo \(f\), the coefficient of \(r^4\) forces \(\beta(0)=0\),
and the constant term forces \(\alpha^5=1\).
Modulo \(f^2\), the remaining equation is
\[
5\alpha^4\beta_1r^4+5b^4=0
\quad\text{in }\mathbb C[r]/(r^5+b^3).
\]
The classes of \(1\) and \(r^4\) are independent, a contradiction.

For \(n=1\), a polynomial shear in \(q\) does give the relative
isomorphism, so the exponent boundary is sharp. The
[relative obstruction](research/danielewski-relative-pass17.md) includes
both chart compositions. This obstruction is consistent with the
abstract polynomial kernel established in Section 4.

## 6. A pointwise criterion for primitive threefold quotients

Let \(D\) now be an arbitrary primitive nonzero LND of
\(R=\mathbb C^{[3]}\). The source-dependent working lemma is
\[
\pi^{-1}(p)\cong\mathbb A^1
\text{ as a reduced scheme}
\quad\Longrightarrow\quad p\notin V(P_D),
\qquad \pi:\operatorname{Spec}R\to\operatorname{Spec}C.
\tag{14}
\]

The [full proof](research/pointwise-plinth-pass17.md) uses the actual
exceptional curve factorization in Kaliman's paper, rather than an
abstract finite map of curves.[^4] Its retained exceptional curve
\(\Gamma\) equals \(V(P_D)\): primitivity turns the product off
\(\Gamma\) into a local slice, while the generic multiple-line fibers
on retained components give the reverse inclusion.

Here is the additional support argument. Delete a finite set
\(F_0\subset\Gamma\), including \(p\), so the exceptional surface is
\(E^*=Z^*\times\mathbb A^1\). The finite map
\(\theta:Z\to\Gamma\) has degree at least two on every retained component.
The exact homology diagram gives
\[
\theta_*\beta\in\operatorname{im}\phi
\ \Longrightarrow\ \beta\in\operatorname{im}\phi'.
\tag{15}
\]
The maps \(\phi,\phi'\) are the Thom maps from the three-dimensional
homology of the complements of the finitely many fibers. Since
\(H_3(\mathbb A^3)=H_4(\mathbb A^3)=0\), excision represents every
class in \(\operatorname{im}\phi'\) arbitrarily close to those whole
fibers.

If \(Y=\pi^{-1}(p)\) is a reduced line, flatness makes \(\pi\) smooth
along all of \(Y\).[^5] Normalization commutes with this smooth base
change.[^6] Consequently, for each analytic branch of \(\Gamma\) at
\(p\), the normalized exceptional surface has exactly one copy of
\(Y\). It reaches one normalized point of \(Z\), and smoothness forces
ramification index one there. The degree bound supplies at least one
other point above that base branch that is not reached.

This alone is not a contradiction. Several normalized points can map
to the same singular point of \(Z\). To exclude the missing branches,
choose disjoint disks about the normalized points and retain only the
reached disks. Their inverse image contains the entire normalized
fiber. Finiteness, hence properness, of the normalization of \(E\)
then gives a neighborhood of the whole \(Y\) whose image avoids every
unreached puncture. No properness of \(\pi\), nor compactness of \(Y\),
is assumed.

The localized image of \(\phi'\) therefore involves only reached
peripheral loops at \(p\). But a weighted sum of loops selecting one
unreached branch and one point over every other base branch maps under
\(\theta_*\) to the sum of the base loops. That sum is \(\phi\) of a
small three-sphere about \(p\), so (15) places the weighted sum in
\(\operatorname{im}\phi'\). This contradicts its support: the finite
puncture loops are independent because every affine curve component
also has a puncture at infinity. This proves (14).

The topological hypotheses are indispensable in this argument.
Deleting a normalization branch of an abstract nodal finite cover can
leave a single reduced fiber, as the preceding report explicitly
demonstrated. That example has no Kaliman homology diagram and is not
a polynomial-threefold quotient.

## 7. From the pointwise lemma to arbitrary affine replacement

The [full algebraic deduction](research/general-invariant-affine-pass17.md)
combines (14) with the previously established whole-component exclusion.

Suppose \(E=AD+B\partial_t\) has a slice. Quotient surjectivity implies
\((A,B)C=C\); otherwise both coefficients vanish above a common base
point, where a slice is impossible. The whole-component argument also
gives \(\gcd(B,p_D)=1\).

Assume a remaining common zero \(p\in V(B)\cap V(P_D)\). Choose a
reduced irreducible component of \(V(B)\) through \(p\), normalize it,
and take the DVR \(V\) at a point above \(p\). The component is not
contained in plinth support. Thus, for \(L=\operatorname{Frac}V\),
faithful flatness gives
\[
T=R\otimes_CV\hookrightarrow L[u],\qquad T_L=L[u].
\]
The generic derivation is translation. Any invariant in \(T\) lies
in \(L\); a negative valuation would make the uniformizer invertible
in \(T\), contradicting its nonempty special fiber. Hence
\(\ker D_V=V\).

In \(T[t]\), \(B=0\). The constant coefficient \(r_0\) of the
specialized slice therefore satisfies \(D_V(A r_0)=1\). The slice
identity gives \(T=V[A r_0]\), whose closed fiber is a reduced
affine line. Because the residue field of \(V\) is \(\mathbb C\),
this is the whole original fiber at \(p\), not one chosen component.
For primitive \(D\), equation (14) is a contradiction.

For a replica \(D=aD_0\), with \(D_0\) primitive and \(a\in C\),
replace \(A\) by \(Aa\); the plinth identity \(P_D=aP_{D_0}\)
gives the same conclusion. Zero and constant coefficients are handled
directly. Therefore \(AP_D+BC=C\). Conversely a Bezout identity
\(A p_DU+BV=1\), with \(D r=p_D\), supplies the affine slice
\(Ur+Vt\). This proves (2).

This closes the affine-replacement restriction for this specified
invariant-extension problem. It does not prove principality of every
higher image ideal for arbitrary rank-three derivations.

## 8. Extension to the full local-slice family

The construction also works for the entire family in
Dasgupta--Gaifullin's Theorem 5.7. Fix \(m\ge2\), \(n\ge1\), and
\(P(x,f)\) with \(P(x,0)\) nonconstant. Put
\[
f=xz-y^m,\quad r=xP(x,f)+yf^n,\quad
h=\frac{r^m+f^{mn+1}}x,\quad
\delta=-\operatorname{Jac}(f,h,\cdot).
\tag{16}
\]
The quotient for \(h\) is polynomial. The source proves rank three,
kernel \(C=\mathbb C[f,h]\), and plinth \(f^nhC\).
Here \(\delta r=f^nh\), with the opposite sign from the source.

Combining (2) with the coordinate construction gives
\[
\boxed{
A\delta+B\partial_t\text{ has a slice}
\iff (A,B)C=C,\ B=c+fhQ,\ c\ne0
\ \Longrightarrow\ \ker(A\delta+B\partial_t)\cong\mathbb C^{[3]}.
}
\tag{17}
\]
Sufficiency and the polynomial inverse below do not use the pointwise
lemma. That lemma is needed for necessity for arbitrary slices in
this larger family.

Normalize \(c=1\), use the same \(U,V,\rho,s\), and put
\(X=(\rho^m+f^{mn+1})/h\). The finite correction is now
\(H\in\mathbb C[X,f]/(f^n)\) determined by
\[
b_H=B(f,X^{m-1}H^m),\qquad
H=b_H^{1-m}P(b_H^{-m}X,f).
\tag{18}
\]
Start with \(P(X,f)\) and make \(n-1\) truncated updates.
Dependence on the input improves \(f\)-adic order by one, so the
same finite uniqueness proof applies. No ordinary homogeneity or
monomial hypothesis on \(P\) is needed.

Set
\[
Y=\frac{\rho-XH}{f^n},\qquad
S_m=\sum_{k=0}^{m-1}\binom mk
 X^{m-k-1}H^{m-k}Y^kf^{nk},\qquad
Z=\frac{h-S_m}{f^{mn}}.
\tag{19}
\]
Modulo \(f^n\), \(X=B^mx\) and
\(H=B^{1-m}P(B^{-m}X,f)\), proving that \(Y\) is polynomial.
Then \(X(h-S_m)=f^{mn}(Y^m+f)\), and coprimality of \(X,f\)
proves that \(Z\) is polynomial and \(f=XZ-Y^m\).

For the inverse, work in independent \(X,Y,Z,s\), define
\(\rho=XH+Yf^n,\ h=S_m+Zf^{mn}\), recover \(r,t\) by the
inverse matrix, and put
\[
W=\frac{V-1}{h}\rho+Af^ns,\qquad
x=X+W\sum_{i=0}^{m-1}r^{m-1-i}\rho^i.
\tag{20}
\]
One has \(xh=r^m+f^{mn+1}\). Modulo \(f^n\),
\(x=V^mX,\ r=VXH,\ H=V^{m-1}P(V^mX,f)\).
Thus \((r-xP(x,f))/f^n\) is polynomial and recovers \(y\);
the binomial identity recovers polynomial \(z\).
This proves coordinate generation without assuming cancellation.

The [full proof](research/general-local-slice-lift-pass17.md)
includes both inverse divisibility arguments, nonvanishing of the
reconstructed \(h\), and the polynomial justification of
\(x=V^mX\pmod{f^n}\). It never cancels \(h\) inside a nonreduced
quotient.

Finite interpolation is established machinery for cylinder
isomorphisms. Moser-Jauslin--Poloni's Theorem 4.0.1 constructs explicit
isomorphisms between cylinders over special Danielewski surfaces
through finite Hermite congruences.[^7] It is a close predecessor,
not the polynomial-kernel conclusion (17). This comparison gives
necessary prior context, not evidence that (17) is new.

## 9. Literature and verification boundaries

The all-degree \(n=1\) basis is known. The broader rank-three family is
known. The relative isomorphism restriction is known. The additional
all-\(n\) reconstruction, finite-jet application, and pointwise deduction
are working proofs whose priority has not been established.

Recent related statements must be read at their actual scope.
Masuda's faithfully flat quotient result identifies the closure of the
bad-fiber set with plinth support; that statement alone does not prove
(14).[^8] Shakhmatov's April 2026 cylinder criterion characterizes
principal open subsets carrying equivariant product structures; it does
not infer such a neighborhood from a single smooth fiber.[^9]
Neither a failed search nor a difference of wording establishes novelty.

The exact checkers are independent of the research solvers:
\[
\texttt{rank\_three\_image\_checks\_pass17.py},\qquad
\texttt{nonreduced\_jet\_checks.py},\quad
\texttt{general\_jet\_lift\_checks.py}.
\]
They test physical Jacobians, localized chart inverses, leading-term
witnesses, finite-jet congruences, Bezout matrices, numerator identities,
and the relative chart changes. The negative control detects the
uncorrected \(Y\)-numerator \(5fx^8\pmod{f^2}\).
Finite symbolic tests do not prove the topological lemma or all
parameter values. Those conclusions rest on their written arguments
and cited inputs.

The full execution record is
[verification-pass-17.json](verification-pass-17.json): all **386 test
methods across 27 suites** passed, including 34 new methods, at
2026-09-13 02:18:32 UTC. The [separate geometry audit](research/pointwise-plinth-audit-pass17.md)
checks the pointwise proof, and the [statement-level literature audit](research/general-jet-literature-pass17.md)
records the finite-congruence predecessors and unresolved priority.
A [second adversarial audit](research/pointwise-plinth-second-audit-pass17.md)
adds an actual additive-action control on a quasi-affine space, showing
exactly where nonzero third homology defeats the pointwise argument.
Reproduction:
~~~sh
cd '/Users/thomasou/Documents/ChatGPT/Long term/zariski-cancellation'
/opt/anaconda3/bin/python research/rank_three_image_checks_pass17.py
/opt/anaconda3/bin/python research/nonreduced_jet_checks.py
/opt/anaconda3/bin/python research/general_jet_lift_checks.py
~~~
The [README](README.md) lists every earlier regression command.

## 10. What is still needed for cancellation

For an arbitrary invariant extension, equation (2) gives an affine slice
but no construction covering bases outside (16). A full argument
must construct its polynomial kernel without preserving invariants
that cannot, in general, be preserved. Section 5 shows why this
qualification is mathematical rather than cosmetic.

More fundamentally, the arbitrary slice derivation on a polynomial
four-ring has not been reduced to an invariant extension of a
three-variable LND at all. A construction that only enlarges a
coefficient family does not establish that reduction. These are the
remaining recognition and reduction steps; neither is certified here.

The next bounded continuation isolates a broader completed subcase in
[the plinth-unit note](research/plinth-units-pass18.md): for primitive
bases with connected squarefree plinth support, the coefficient is
constant modulo the full plinth, so the earlier matrix lift applies.
Repeated components and disconnected support are not silently included.
The [principal-modification note](research/arbitrary-invariant-kernel-pass18.md)
reformulates the remaining invariant-kernel problem without solving it.

## Sources

[^1]: N. Dasgupta and S. A. Gaifullin, [On locally nilpotent derivations of polynomial algebra in three variables](https://www.mathnet.ru/eng/sm10094), *Sbornik: Mathematics* 216(4) (2025), 456–484, Theorem 5.7 and proof. Published full HTML consulted.
[^2]: G. Freudenburg, [Canonical factorization of the quotient morphism for an affine Ga-variety](https://arxiv.org/pdf/1602.08786v3), *Transformation Groups* 24 (2019), 355–377, Sections 8.2.7–8.2.8.
[^3]: P.-M. Poloni, [Classification(s) of Danielewski hypersurfaces](https://arxiv.org/pdf/0912.3241v1), *Transformation Groups* 16 (2011), 579–597, Corollary 3.3(1).
[^4]: S. Kaliman, [Free C+-actions on C3 are translations](https://www.math.miami.edu/~kaliman/library/Ka.invent.2004.c%2B.pdf), *Inventiones Mathematicae* 156 (2004), 163–173. Final author manuscript, Lemmas 2.1, 2.2, 3.1; Proposition 3.2 and its diagram; Theorem 5.2(i). The pointwise statement (14) is a deduction here, not a quoted theorem.
[^5]: The Stacks Project, [Lemma 29.35.14, Tag 01V9](https://stacks.math.columbia.edu/tag/01V9), flatness and smoothness of the scheme-theoretic fiber criterion.
[^6]: The Stacks Project, [Lemma 37.19.2, Tag 03GV](https://stacks.math.columbia.edu/tag/03GV), normalization commuting with smooth base change.
[^7]: L. Moser-Jauslin and P.-M. Poloni, [Isomorphisms between cylinders over Danielewski surfaces](https://arxiv.org/html/2002.12202), arXiv:2002.12202v1, February 27, 2020, Section 4 and Theorem 4.0.1.
[^8]: K. Masuda, [Faithfully flat quotient morphisms by Ga-actions on factorial affine varieties](https://arxiv.org/html/2512.06687v1), *Journal of Algebra* 691 (2026), 577–596, Proposition 2.5 and its remark, Theorem 3.5.
[^9]: K. Shakhmatov, [Cylinders and the zero locus of the plinth ideal](https://arxiv.org/html/2605.00138v1), arXiv:2605.00138v1, April 30, 2026, Theorem 2.6 and Corollary 2.7.
