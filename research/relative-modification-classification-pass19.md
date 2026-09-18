# Relative isomorphisms of local-slice modifications

For a primitive locally nilpotent derivation on complex polynomial
three-space with connected reduced plinth support, the associated
principal modification is isomorphic to the original ring over the
invariant subring exactly when the modifying coefficient is constant
modulo the full plinth ideal. Congruence only modulo its radical is
insufficient for any such relative isomorphism, not just for the
canonical rescaling considered previously.

This is a working proof of a stronger relative statement. It does not
decide abstract polynomiality of the modification or unrestricted
cancellation. Its priority is not established.

## 1. Setup and the induced primitive derivation

Let
\[
R=\mathbb C[x,y,z],\qquad 0\ne D\in\operatorname{LND}(R)
\text{ primitive},\qquad C=\ker D,\qquad P_D=pC,\qquad Dr=p.
\tag{1}
\]
Here \(r\) is a minimal local slice, \(C\cong\mathbb C^{[2]}\),
and \(p\ne0\). Let \(0\ne V\in C\), assume \((p,V)C=C\), and set
\[
M=R[w]/(Vw-r)=R[r/V].
\tag{2}
\]
The [two-way slice construction](arbitrary-invariant-kernel-pass18.md)
proves \(M[s]\cong\mathbb C^{[4]}\), without asserting that \(M\)
itself is polynomial. In particular \(M\) is a UFD and
\(M^*=\mathbb C^*\). The UFD assertion descends from the polynomial
extension, and its units are those of \(M\).

The derivation
\[
\Delta|_R=VD,\qquad \Delta(w)=p
\tag{3}
\]
is well defined and locally nilpotent on \(M\). It kills the relation
\(Vw-r\); local nilpotence holds separately on the generators \(R,w\).
Its kernel is \(C\). Indeed an invariant in \(M_V=R_V\) belongs to
\(C_V\), and one in \(M_p=C_p[w]\) belongs to \(C_p\).
Their intersection is \(C\), because \((p,V)=1\).

The derivation is primitive: on the \(V\)-chart it is a unit times
the primitive \(D\), and on the \(p\)-chart it has a slice.
No prime divisor can divide all its values on either member of this
cover. Its plinth is exactly \(pC\), by the same localization:
on the first chart the plinth is \(pC_V\), and on the second it is
\(C_p=pC_p\). The
[all-image preservation proof](global-modification-bridge-pass19.md)
gives the stronger statement in every derivative degree.

The standard kernel and plinth inputs on \(R\) are recorded in
Dasgupta--Gaifullin's preliminary theorems.[^1] Their application to
\(M\) here is the explicit two-chart argument, not an assumption that
\(M\) is already affine three-space.

## 2. Residue independence at a plinth prime

Let \(f\) be an irreducible factor of \(p\). Factorial closure of \(C\)
in \(R\) makes \(f\) prime in \(R\), with \(fR\cap C=fC\).
Primitivity makes the induced derivation \(\overline D\) on \(R/(f)\)
nonzero. This is a locally nilpotent derivation on a domain of
transcendence degree two, so its invariant fraction field has
transcendence degree one.

Both \(C/(f)\) and the residue \(\overline r\) lie in that kernel.
Consequently \(\overline r\) is algebraic over
\[
F_f=\operatorname{Frac}(C/(f)).
\tag{4}
\]
It does not belong to \(F_f\). Otherwise there are \(a,b\in C\)
with \(f\nmid a\) and \(ar-b=fu\) in \(R\). Differentiating gives
\(Du=ap/f\in C\). Minimality of \(r\) forces \(Du\in pC\),
and hence \(a/f\in C\), a contradiction. In particular the
algebraic degree of \(\overline r\) over \(F_f\) is at least two.

Also \(r\) is a unit in \(R_{(f)}\): divisibility \(f\mid r\)
would give the same contradiction with \(D(r/f)=p/f\).
If \(q,b\in C_V\) are not both zero, then
\[
v_f(qr+b)=\min\{v_f(q),v_f(b)\}.
\tag{5}
\]
For equal finite valuations, cancellation would give a linear relation
between \(\overline r\) and \(1\) over \(F_f\); unequal valuations
cannot cancel. The convention is \(v_f(0)=+\infty\).

## 3. A full affine extension criterion near the identity

Write \(p_0\) for a squarefree generator of the radical of \(pC\).
Let \(\lambda\in C_V^*\), \(b\in C_V\), and suppose
\(\lambda\equiv1\pmod{p_0C_V}\). On
\(R_{pV}=C_{pV}[r]\), define the affine automorphism
\[
\sigma(r)=\lambda r+b,\qquad \sigma|_{C_{pV}}=\operatorname{id}.
\tag{6}
\]
Then the following are equivalent:

1. \(\sigma(R_V)\subseteq R_V\).
2. \(\sigma\) restricts to an automorphism of \(R_V\).
3. \(\lambda-1\in pC_V\) and \(b\in pC_V\).

This extends the
[pure-rescaling criterion](rescaling-obstruction-audit-pass18.md)
to all invariant affine shifts under the same multiplier congruence.

### 3.1. The shift must first vanish on every reduced component

Assume the endomorphism condition in item 1. Fix \(f\mid p\).
In the residue domain, the iterates of \(\overline r\) are
\(\overline r+m\overline b\), since \(\overline\lambda=1\).
Each is a root of the same minimal polynomial over \(F_f\): the
endomorphism fixes its invariant coefficients. A polynomial over a
field cannot have infinitely many distinct roots. Characteristic zero
therefore forces \(\overline b=0\).

This argument does not require that the induced endomorphism modulo
\(f\) be injective. The polynomial relation can be cleared of its
invariant denominators before applying an iterate.

### 3.2. Finite coefficient extraction restores every multiplicity

Let \(n=v_f(p)\), \(q=\lambda-1\), \(L=qr+b\). The preceding
step and the multiplier premise give \(v_f(q),v_f(b)\ge1\).
If \(L=0\), residue independence and algebraic independence of the
local slice over \(C\) give \(q=b=0\), and there is nothing to prove.
Suppose for contradiction that
\(\ell=v_f(L)<n\).

Primitivity supplies an ambient coordinate \(a\) with
\(v_f(Da)=0\). Put \(d=\deg_D(a)\ge1\) and \(N=nd\).
In the DVR \(O=R_{(f)}\), consider the finite polynomial
\[
c(T)=\sum_{j=1}^{N+1}\binom Tj q^{j-1}.
\tag{7}
\]
For \(q=0\), this means \(c(T)=T\). For a nonnegative integer \(m\),
let \(S_m=1+\lambda+\cdots+\lambda^{m-1}\), with \(S_0=0\).
The ordinary binomial theorem gives
\[
c(m)-S_m\in f^{N+1}O.
\tag{8}
\]
For \(q\ne0\), the omitted terms contain at least \(q^{N+1}\).
For \(q=0\), the equality is exact.

The \(m\)-th iterate sends \(r\) to \(r+LS_m\). Thus for the
chosen coordinate \(a\), it is its finite independent-time \(D\)-flow
with time \(LS_m/p\). Define
\[
H(T)=\sum_{i=0}^{d}
\frac{L^iD^i(a)}{i!p^i}\,c(T)^i.
\tag{9}
\]
The coefficient in this sum has valuation at least \(-ni\ge-N\).
Equation (8) makes \(H(m)-\sigma^m(a)\) integral, in fact divisible
by \(f\). Every \(\sigma^m(a)\) is integral by item 1, so \(H(m)\in O\)
at every nonnegative integer.

Invert the Vandermonde matrix at
\(0,1,\ldots,\deg H\). Its determinant is a nonzero integer and
therefore a unit in \(O\). Every coefficient of \(H\) lies in \(O\).
But \(c(0)=0\), and
\[
c'(0)=1+\sum_{j=2}^{N+1}
\frac{(-1)^{j-1}}j q^{j-1}\in O^*.
\]
Consequently
\[
H'(0)=\frac{L\,Da}{p}c'(0),\qquad
v_f(H'(0))=\ell-n<0,
\tag{10}
\]
a contradiction. Thus \(v_f(L)\ge n\). Equation (5) forces both
\(v_f(q)\ge n\) and \(v_f(b)\ge n\).
Doing this for every factor of \(p\) proves item 3.

### 3.3. Sufficiency and the inverse

Under item 3, \(T_0=((\lambda-1)r+b)/p\) belongs to \(R_V\), and
\[
\sigma(a)=\sum_{j\ge0}\frac{T_0^j}{j!}D^j(a)
\tag{11}
\]
is polynomial for every \(a\in R_V\). It equals the affine change
(6) on the localized polynomial ring. The inverse multiplier
\(\lambda^{-1}\) and shift \(-\lambda^{-1}b\) satisfy the same
full-plinth divisibility, so the inverse is polynomial too.
This is evaluation of a finite flow, not the assertion that
\(T_0D\) is locally nilpotent.

## 4. What an arbitrary relative isomorphism would have to do

Suppose \(\phi:R\longrightarrow M\) is a \(C\)-algebra isomorphism.
The transported derivation \(\phi D\phi^{-1}\) is primitive and has
kernel \(C\). It and \(\Delta\) become constant-coefficient derivatives
on the generic line over \(\operatorname{Frac}(C)\), so they differ
by a nonzero rational function in \(\operatorname{Frac}(C)\).
Primitivity in the UFD \(M\), in both directions, makes this ratio
a unit of \(M\), hence a complex nonzero constant.

Since \(\Delta(w)=p\) and \(\ker\Delta=C\), it follows that
\[
\phi(r)=a w+b=\frac aV r+b,\qquad
a\in\mathbb C^*,\quad b\in C.
\tag{12}
\]
After inverting \(V\), this is an automorphism of \(R_V\) fixing
\(C_V\), not merely a rational map into a different chart.

For each \(f\mid p\), initially regard the residue
\(\overline V\) as an arbitrary element of \(F_f^*\).
The residue multiplier in (12) is \(a/\overline V\).
By the algebraicity in Section 2, the iterates of \(\overline r\)
lie in a finite set of roots of its minimal polynomial.
Two iterates coincide, and their affine difference implies
\((a/\overline V)^N=1\) for some positive \(N\), since
\(\overline r\notin F_f\).
The polynomial \(T^N-1\) splits into linear factors over \(\mathbb C\);
in the field \(F_f\), one of those factors must vanish.
Thus the residue \(\overline V\) is a nonzero complex constant
\(c_f\), and \(a/c_f\) is a root of unity.

This conclusion follows from the hypothetical relative isomorphism.
It does not require a prior theorem about the geometry or normalization
of the reduced plinth components.

Choose one common positive \(N\) for all components. The \(N\)-th
iterate of (12) has multiplier \((a/V)^N\equiv1\pmod{p_0}\)
and an invariant shift. Section 3 applies and gives
\[
V^N-a^N\in pC.
\tag{13}
\]
Contraction from \(C_V\) to \(C\) is valid because \((p,V)=1\).
Thus the class of \(V\) modulo the full plinth, after multiplication
by a nonzero scalar, must have finite order in the unit group.
This is necessary, not asserted sufficient for disconnected support.

The framework of kernel-fixing automorphisms acting affinely on a
minimal local slice, with a multiplier character, has a primary
announced predecessor in Kuroda.[^2] The proof above explicitly
checks the localized modification and multiplicity conditions; it
does not infer (13) from a theorem about the centralizer alone.

## 5. Exact classification for common constant residue

Assume \(p\) is nonunit and
\[
V=c+p_0Q,\qquad c\in\mathbb C^*,\quad Q\in C.
\tag{14}
\]
The theorem first assumes (14), even if the support is disconnected.
Then
\[
\boxed{R\cong_C R[r/V]\quad\Longleftrightarrow\quad V-c\in pC.}
\tag{15}
\]

For necessity, (13) and the residue on any component give \(a^N=c^N\).
Factor \(V^N-c^N=(V-c)J\). Modulo every \(f\mid p\),
the factor \(J\) is the nonzero constant \(Nc^{N-1}\).
It is therefore coprime to \(p\). Equation (13) implies \(p\mid V-c\),
with all multiplicities.

For sufficiency, write \(V=c+pH\). There is an explicit isomorphism
fixing \(C\):
\[
\phi(a)=\sum_{j\ge0}\frac{(-Hw)^j}{j!}D^j(a)
\quad(a\in R).
\tag{16}
\]
It sends \(r\) to \(cw\). Its inverse on the included copy of \(R\)
in \(M\), together with the extra generator, is
\[
\psi(a)=\sum_{j\ge0}\frac{(Hr/c)^j}{j!}D^j(a),
\qquad \psi(w)=r/c.
\tag{17}
\]
The relation \(Vw=r\) is respected since \(\psi(r)=Vr/c\).
The two maps are inverse after inverting \(pV\), where they are
inverse affine changes of a line. As both rings inject into that
localization, they are inverse globally.

If \(p\) is a unit, \(R=C[r]\) and \(M=C[w]\), so relative
polynomiality is immediate without a connected-support condition.

**Connected-support corollary.** If \(p\) is nonunit and its reduced
support is connected, then \(R\cong_C M\) if and only if
\(V-c\in pC\) for some \(c\in\mathbb C^*\).
Indeed Section 4 supplies a constant \(c_f\) on every component
whenever an isomorphism exists. Constants on intersecting components
must agree. Connectedness of the finite component-intersection graph
therefore supplies one common \(c\), after which (15) applies.
Sufficiency is (16)-(17). This corollary is entirely algebraic; it
does not use the independent source-dependent assertion that all
admissible coefficients already have constant component residues.

## 6. Why the residue condition cannot be removed

Let \(p=x(x-1)\), take
\[
D=p\partial_y+2y\partial_z,\quad h=pz-y^2,\quad
C=\mathbb C[x,h],\quad V=2x-1.
\tag{18}
\]
The derivation is primitive, \(r=y\) is a minimal local slice,
and \(V^2-1=4p\). Although \(V\) has distinct residues \(1,-1\)
on the two plinth components, there is a relative isomorphism
to \(M\): put \(z'=z-4w^2\). Then
\[
h=pz'-w^2,\qquad M=\mathbb C[x,w,z'].
\tag{19}
\]
The isomorphism from \(R\) sends \(y\) to \(w\) and \(z\) to \(z'\),
and fixes \(x,h\). This is consistent with (13), with \(N=2\).
It rules out replacing the common-residue premise of (15) by mere
comaximality.

## 7. Absolute cancellation remains a different question

The [pass-18 polynomial-curve examples](polynomial-curve-lift-pass18.md)
include connected repeated plinths and coefficients of form (14) that
are not constant modulo \(p\), yet their modifications are abstract
polynomial three-rings. Formula (15) now excludes relative isomorphisms
for all primitive bases with these coefficient properties, rather than
only the earlier Danielewski example.

This does not prove that any modification is nonpolynomial. It proves
that a successful general polynomial recognition argument must be able
to change the embedding of \(C\). The agreement of all higher image
ideals also cannot recover that embedding or force a filtered
isomorphism. Reduction of an arbitrary slice derivation on
\(\mathbb C^{[4]}\) to these modifications remains unproved as well.

The finite affine argument, localized comparison and two inverse maps
have been separately reconstructed twice without an identified gap.
These are internal mathematical cross-checks, not human expert review,
formal proof-assistant verification or a novelty determination.
The reconstruction details are in the
[pass-19 audit record](proof-audits-pass19.md).

The [statement-level literature comparison](literature-boundary-pass19.md)
identifies the pure-translation automorphism case of Section 3 as a
corollary of Stampfli's existing UFD centralizer lemma. Its proof also
supplies the iteration/differentiation predecessor. Novelty of the
noncommuting near-identity endomorphism refinement or the relative
modification corollary remains unestablished.

## Sources

[^1]: N. Dasgupta and S. A. Gaifullin, [*On locally nilpotent derivations of polynomial algebra in three variables*](https://www.mathnet.ru/eng/sm10094), *Sbornik: Mathematics* 216(4) (2025), 456-484, preliminary three-variable kernel, factorial-closure and plinth results. The extension to \(M\) is proved in Section 1.
[^2]: S. Kuroda, [*The automorphism group of a UFD over the kernel of a locally nilpotent derivation*](https://www.math.okayama-u.ac.jp/~hashimoto/paper/Comm-Alg/35/jsca35kurodas.pdf), eight-page primary symposium announcement, Propositions 2.1-2.2 and Theorem 2.4. Announced framework credited; neither complete journal publication nor priority for the present criterion is assumed.
