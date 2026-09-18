# Cubic-column recognition and the remaining global extension problem

The supplied cubic-column problem now has polynomial-kernel arguments
for the constant-top degree-six branch, the constant-factor degree-five
branch, and the degree-five branch with dependent leading directions.
The general remaining degree-five case has a commuting polynomial nice
symmetry with a recognized polynomial auxiliary kernel. That alone
does not recognize the original kernel. Explicit polynomial examples
show why neither a slice nor a selected invariant plane can be
transferred automatically.

The full working cancellation question remains
\[
A[s]\simeq\mathbb C^{[4]}
\quad\Longrightarrow\quad A\simeq\mathbb C^{[3]}.
\tag{1}
\]
It is not proved here. This is the corrected complex-threefold
interpretation of the supplied question, not a field and dimension
confirmed by its author. As literally pasted, the conclusion
\(X\simeq\mathbb A^1\) is incompatible with general r: the
product hypothesis makes \(\dim X=r\). No new result or expert
endorsement should be inferred from that correction.

## 1. The exact supplied-frame hypothesis

Let \(B=\mathbb C[x_1,x_2,x_3,x_4]\), let E be a nonzero locally
nilpotent derivation, and let \(T_i=\partial_{x_i}\). The restricted
problem assumes
\[
\operatorname{ad}_E^2T_i=0\quad(i=1,2,3),\qquad
\operatorname{ad}_E^4T_4=0,\qquad
V=\operatorname{ad}_E^3T_4\ne0.
\tag{2}
\]
A slice means a polynomial \(s_*\) with \(E(s_*)=1\). The
slice theorem identifies \(B=(\ker E)[s_*]\); it does not by
itself identify \(\ker E\) with a polynomial ring.[^1]

The preceding [one-cubic-column proof](research/whole-frame-recognition-pass39.md)
bounds the coordinate flow degree by six. It already recognizes
all cases with degree at most four under the slice hypothesis and reduces the others to the
specific configurations below. The degree is the largest j with
\(E^j(x_i)\ne0\) for some generator, not the ordinary polynomial
degree of E's coefficients.

The broader supplied-frame result remains \(H\le9\). The first
profiles not fully recognized are \((0,2,2,2)\), \((1,1,1,3)\),
and \((1,1,2,2)\). Recognizing more cases of the middle profile
does not prove that an arbitrary cylinder admits that profile or
a coordinate change reducing to it.

## 2. The constant-top degree-six case

Write \(h_j=E^jx\), \(J=\operatorname{Jac}(Ex)\),
\(u=(\operatorname{ad}_E^2T_4)(x)\), and \(v=V(x)\).
The residual configuration is
\[
h_6=c\in\mathbb C^4\setminus\{0\},\quad c_4=0,
\qquad (h_4)_4=\lambda\in\mathbb C^*.
\tag{3}
\]
These hypotheses themselves supply the polynomial slice
\(\sigma=(h_3)_4/\lambda\). A separately supplied slice is
unnecessary for this branch.

The actual inverse-flow Jacobian has a six-dimensional companion
\[
M=\begin{pmatrix}J&-u/2&-v/6\\ e_4^{\mathsf t}&0&0\\0&1&0\end{pmatrix},
\qquad M^6=0,
\qquad (M^j)_{1:4,1:4}=\frac{\operatorname{Jac}h_j}{j!}.
\tag{4}
\]
The last two rows are as important as its upper-left block. They
retain the differentials of \((h_{j-1})_4\) and
\((h_{j-2})_4\), with their Taylor factorials.

The rank-one fifth power and rank-two fourth power give constants
d and invariant coefficients k and \(\tau\) satisfying
\[
h_5=c\sigma+d,\quad
h_4=c\sigma^2/2+d\sigma+k,\quad
\tau=(h_2)_4-\lambda\sigma^2/2,
\quad\operatorname{rank}\operatorname{Jac}(k,\tau)\le1.
\tag{5}
\]
For the good fields \(W_i=[E,T_i]\), coefficient comparison gives
\(W_i k=-cT_i\sigma/5\) and
\(W_i\tau=-\lambda T_i\sigma/3\). At least one
\(T_i\sigma\) is nonzero: otherwise the slice would depend only
on \(x_4\), contradicting \(E^4x_4=\lambda\).
Evaluating the rank-one differential relation on that field yields
\(k=3c\tau/(5\lambda)+e\), with e constant and \(e_4=\lambda\).

The resulting polynomial derivation is
\[
Z=T_e+\frac\sigma4T_d+
\left(\frac{\sigma^2}{20}+\frac{3\tau}{10\lambda}\right)T_c.
\tag{6}
\]
Direct coefficient identities give \([E,Z]=0\) and
\(Zx_4=\lambda\). Commutation applied to the actual iterates
defining \(\sigma,\tau\) gives \(Z\sigma=Z\tau=0\).
Thus \(Z^2x_i=0\), so Z is a polynomial LND.

Its slice \(t_0=x_4/\lambda\) is an actual ambient coordinate.
Consequently \(R=\ker Z\simeq B/(x_4)\simeq\mathbb C^{[3]}\).
The invariant coordinates \(y_i=x_i-t_0Zx_i\), \(i\le3\),
have the explicit inverse obtained by evaluating the coefficients
of Z on \((y_1,y_2,y_3,0)\). This is stronger than a unit
Jacobian computation.

The restriction \(E|_R\) retains the slice \(\sigma\).
Miyanishi's known three-variable kernel theorem gives
\(K=\ker(E|_R)\simeq\mathbb C^{[2]}\).[^1]
Since \(R=K[\sigma]\) and \(Et_0\in R\), polynomial
integration supplies \(H\in R\) with \(EH=Et_0\). Therefore
\[
B=K[\sigma,t_0-H],\qquad
\ker E=K[t_0-H]\simeq\mathbb C^{[3]}.
\tag{7}
\]
The [complete degree-six proof](research/cubic-degree-six-pass40.md)
records every coefficient and both coordinate inverse identities.
No example realizing (3) is asserted. The conclusion closes the
specified branch whether or not it is realizable.

## 3. Degree five and the original-slice unit lemma

The other residual has
\[
E^5x=cg^5,\qquad E^3x_4=\lambda g^3,
\qquad 0\ne g\in\ker E,
\quad c_4=0,
\tag{8}
\]
with c nonzero and \(\lambda\ne0\) constant. Put
\(\delta=E/g\) on \(B_g\). The top field remains nonzero
after this rescaling; the proof first excludes rational dependence
of E and V by applying their brackets to the original polynomial
slice and using LND divisibility.

For any invariant f, the exact rescaling rule is
\[
\operatorname{ad}_{fE}^jT
=f^j\operatorname{ad}_E^jT
-j f^{j-1}(\operatorname{ad}_E^{j-1}T)(f)E.
\tag{9}
\]
It verifies that the required double and fourth bounds survive.
The coordinate partials are derivations of the localization, not
asserted to be locally nilpotent on it.

With \(\sigma=E^2x_4/(\lambda g^2)\), the full companion
rows and good-column comparison give constant vectors d,e and
an invariant \(\tau=Ex_4/g-\lambda\sigma^2/2\) such that
\[
Z=T_e+\frac\sigma3T_d+
\left(\frac{\sigma^2}{12}+\frac{\tau}{3\lambda}\right)T_c,
\qquad [\delta,Z]=0,
\quad Zx_4=\lambda,
\quad Z\sigma=Z\tau=0.
\tag{10}
\]
Here Z is initially rational. The proof that some good
\(T_i\sigma\ne0\) is a rational function-field argument: the
opposite conclusion would make \(x_4\) a cubic polynomial in a
rational function \(\sigma(x_4)\) generating the same field,
contradicting degree three. No pole is discarded in this step.

Generator niceness \(Z^2x_i=0\) alone does not make Z locally
nilpotent on \(B_g\). It only gives finite iterates on each
polynomial in B. The original slice supplies the missing unit:
\(\delta(s_*)=g^{-1}\), so commutation gives finite iterates
on \(g^{-1}\) as well. The finite exponential polynomials of
g and its inverse multiply to one in \(\operatorname{Frac}(B)[t]\).
They must both be constant in t. Hence \(Zg=0\), Z is genuinely
locally nilpotent on \(B_g\), and \([E,Z]=0\).

This lemma gives an explicit polynomial commuting nice LND:
\[
W=g^4Z=g^4T_e+\frac{g^2q}{3\lambda}T_d+
\left(\frac{g^3p}{3\lambda}-\frac{q^2}{12\lambda^2}\right)T_c,
\quad p=Ex_4,\quad q=E^2x_4.
\tag{11}
\]
It is independent of E, since it kills \(\sigma\) while
\(E\sigma=g\ne0\). Its restriction to \(\ker E\) is therefore
a nonzero intrinsic LND.

When g is constant, (10) is polynomial and its ambient-coordinate
slice gives precisely the recognition argument in Section 2.
Thus the constant-factor degree-five branch also has polynomial
kernel. When g is nonconstant, (11) only gives
\(Wx_4=\lambda g^4\), a nonunit derivative. The complete
[degree-five proof](research/cubic-degree-five-pass40.md) does not
promote it to a slice.

## 4. The auxiliary quotient is polynomial, but it is a different quotient

Divide (11) by its coefficient gcd to obtain an irreducible nice
LND D. Factorial closure makes that gcd W-invariant. Primitivity
and \([E,W]=0\) then force the gcd to be E-invariant as well,
so \([E,D]=0\).

The coefficient span of W lies in the constant span of c,d,e.
A nonzero constant linear form w annihilating that span is fixed
by D. Theorem 3.6 of Dasgupta and Gupta applies over the PID
\(\mathbb C[w]\).[^2] After a polynomial coordinate change
with polynomial inverse, it gives
\[
D=a(w,U)\partial_V+b(w,U)\partial_T,
\qquad R=\ker D=\mathbb C[w,U,bV-aT]\simeq\mathbb C^{[3]}.
\tag{12}
\]
The gcd of a,b is one, but their ideal need not be the unit ideal.
The known theorem allows a non-flat quotient in that case.

The restriction \(E|_R\) is nonzero, as can be checked after
localizing at g using \(E\sigma=g\). The known three-variable
kernel theorem recognizes the common invariant ring
\(\ker E\cap\ker D\simeq\mathbb C^{[2]}\). It does not
recognize \(\ker E\). The [bridge proof](research/nice-centralizer-bridge-pass40.md)
keeps the inclusions and the primitive-divisibility argument explicit.

Two controls identify genuine limits of this approach. For
\(D=w\partial_v+u\partial_t\), \(E=\partial_v\), the original
action has a slice but its restriction to
\(\ker D=\mathbb C[w,u,uv-wt]\) is \(u\partial_r\), which
has none. Conjugating E by an automorphism centralizing D also
produces a sliced commuting action that does not preserve the
selected plane \(\mathbb C[w,u]\). Their quotients are polynomial;
neither is claimed to realize (8). They disprove the automatic
transfer steps, not cancellation or existence of another adapted plane.

## 5. A primitive common fixed locus in the two-defect profile

An independent control concerns the other height-ten profile
\((1,1,2,2)\). Let f,g in \(\mathbb C[u,v]\) have a supplied
Bezout identity \(\alpha f+\beta g=1\), and put
\[
E=f\partial_a+g\partial_c,
\quad s=\alpha a+\beta c,
\quad r=ga-fc.
\tag{13}
\]
The inverse \(a=fs+\beta r\), \(c=gs-\alpha r\) proves
\(\ker E=\mathbb C[u,v,r]\). Use the physical coordinates
\((u+a^2/2,v+c^2/2,a,c)\). Their four highest commutators
restrict to scalar multiples of \(\partial_r\) and generate
exactly the ideal
\[
I=(\Delta_u,\Delta_v),
\qquad \Delta_i=f\partial_i g-g\partial_i f.
\tag{14}
\]
Their two quadratic defects are independent when
\(fg\det\operatorname{Jac}(f,g)\ne0\). If both displayed
coefficients are nonzero, the shifted slice-filtration profile,
not just the adjoint profile, is exactly \((1,1,2,2)\).

Take \(f=u^2+v^2\), \(g=uf-1\). Then
\[
I=(f^2+2u,2v),\qquad
\gcd(f^2+2u,2v)=1,
\qquad \mathbb C[u,v]/I\simeq\mathbb C[u]/(u^4+2u).
\tag{15}
\]
The last polynomial is squarefree of degree four. Thus all four
leading intrinsic fields vanish along four reduced r-lines,
despite having no common divisor. No polynomial combination in
their module is nowhere zero. Dividing a divisorial gcd cannot
remove this obstruction, because that gcd is already one.

The family \(f=p(u)\), \(g=vp(u)-1\) separately gives
\(I=(p',p^2)\). It is a unit ideal exactly when p is squarefree;
a root of multiplicity e has common vanishing order e minus one.
For \(p=u^N\), the actual highest vector sends u to \(u^{2N}\)
and is not locally nilpotent, even though its own coefficient
ideal is the unit ideal. These two ideals must not be confused.
The [complete construction](research/two-defect-critical-locus-pass40.md)
includes every coordinate inverse and the all-multiplicity argument.

## 6. Dependent leading directions close by coordinate descent

One additional hypothesis now closes the nonconstant-factor case:
the constant vectors c,d in the normalized degree-five argument
are linearly dependent. Write \(d=\mu c\). Since \(e_4=\lambda\)
and \(c_4=0\), actual linear coordinates \((u,v,a,b)\) can be
chosen with \(T_c=\partial_a\), \(T_e=\partial_b\),
and \(x_4=\lambda b\). The rational field has the form
\[
Z=\partial_b+F\partial_a,
\qquad F=\mu\sigma/3+\sigma^2/12+\tau/(3\lambda).
\tag{16}
\]
The original-slice unit lemma has already made Z an LND of
\(B_g\). Its actual flow is \((u,v,a+tF,b+t)\), with
Jacobian determinant \(1+t\partial_aF\). This determinant must
be one, because it is a unit polynomial in t specializing to one.
Thus \(F_a=0\); niceness \(ZF=0\) then gives \(F_b=0\).
Consequently \(F=N/D\in\mathbb C(u,v)\), with coprime
\(N,D\in S:=\mathbb C[u,v]\).

The polynomial field \(g^4Z\) implies \(D\mid g^4\), so
factorial closure gives \(ED=0\). Primitive division gives
\[
W_0=D\partial_b+N\partial_a,\qquad
R=\ker W_0=S[J],\qquad J=Da-Nb,
\quad [E,W_0]=0.
\tag{17}
\]
This elementary kernel formula needs gcd one, not comaximality.
Most importantly, the actual good direction \(\partial_a\)
restricts to \(D\partial_J\) on R. Since E fixes D, (2)
descends to
\[
L=E|_R,\qquad [L,[L,\partial_J]]=0.
\tag{18}
\]
If \(L=0\), u is already an invariant ambient coordinate.
Otherwise the [previously proved single-partial lemma](research/height-seven-audit.md)
can be used with information about where its coordinate lies.

If D is a unit, \(B=R[b]\) in actual polynomial coordinates.
An L-invariant coordinate of R is then an E-invariant ambient
coordinate of B. If D is nonconstant, put \(U_0=[L,\partial_J]\).
In the dependent case, the old lemma's primitive argument produces
an invariant coordinate directly in S. In the independent case,
the known commuting-LND theorem gives
\(\ker L\cap\ker U_0=\mathbb C[p]\), with p a coordinate
of R.[^1] Both fields kill D, so \(D=P(p)\) for a nonconstant
polynomial P. Differentiating with respect to J forces
\(\partial_Jp=0\), hence \(p\in S\).

This last coordinate descends to the original plane. Hamann's
known relative cancellation theorem, stated as Theorem 2.6 in
Dasgupta and Gupta, applies with base \(\mathbb C[p]\):[^2]
\[
S[J]=\mathbb C[p]^{[2]}
\quad\Longrightarrow\quad S=\mathbb C[p]^{[1]}.
\tag{19}
\]
Therefore p is an E-invariant ambient coordinate in every branch.
The original kernel is regular because its polynomial extension B
is regular. The fixed-coordinate regular-kernel theorem of
Bhatwadekar, Gupta and Lokhande now gives
\(\ker E\simeq\mathbb C^{[3]}\).[^3]
The [complete two-output proof](research/two-output-cubic-closure-pass40.md)
checks these separate descent steps. It neither assumes a unit
coefficient ideal nor transfers a slice from B to R.

## 7. Remaining proof obligations

The priority is the nonconstant-g degree-five residual with c,d
linearly independent. Its corrected field has three independent
constant output directions, so the planar rational-function
argument in Section 6 does not apply unchanged. A successful
argument must use the full actual-frame identities to extend the
construction across \(V(g)\), recognize the original kernel through
a different valid criterion, or give a genuine coordinate repair.
The auxiliary polynomial kernel and the common invariant plane
are established inputs, not substitutes for that obligation.

The two other height-ten profiles remain open within this
investigation. A proof for every height-ten profile would still
need a universal frame or reduction argument to settle (1).
The constant-top conclusions above and the explicit negative
controls are partial results. No novelty, expert review, formal
verification, or general cancellation solution is claimed.

## Sources

[^1]: Nikhilesh Dasgupta and Sergey Gaifullin,
[*On locally nilpotent derivations of polynomial algebra in three variables*](https://arxiv.org/pdf/2306.00510v2),
version 2, Theorem 2.5 on PDF p. 5, Theorems 2.7-2.8 on PDF p. 6,
and Proposition 2.14 on PDF p. 7.
Theorem 2.8 explicitly attributes the three-variable kernel theorem
to Miyanishi. These are established external inputs.

[^2]: Nikhilesh Dasgupta and Neena Gupta,
[*Nice derivations over principal ideal domains*](https://arxiv.org/pdf/1701.03635v1),
version 1, 2017, Theorem 2.6 on PDF p. 4, Theorem 3.6 and proof,
PDF pp. 6-7, and Corollary 3.8, PDF p. 8. Irreducibility, an invariant coordinate,
and generator niceness are all verified before this application.

[^3]: S. M. Bhatwadekar, Neena Gupta and S. A. Lokhande,
[*Some K-theoretic properties of the kernel of a locally nilpotent derivation on k[X1,...,X4]*](https://arxiv.org/pdf/1501.01438v1),
version 1, Theorem 3.5 and proof, PDF p. 11. The theorem requires
an invariant ambient coordinate and a regular kernel; neither
condition is replaced by a statement about an abstract auxiliary ring.
