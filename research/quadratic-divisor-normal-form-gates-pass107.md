# The actual degree-two constant divisor has an exact DVR conic

At an actual invariant divisor with quadratic residue constants,
one surviving degree-two element forces an exact conic over the
base DVR. This is an algebraic presentation of the whole localized
ring, not merely of its completion or its fraction field. Its
entire degree filtration has alternating bases, giving the exact
derivative-image valuations e, e, 2e, 2e in degrees one through four.

The surviving degree-two element is essential input. In the actual
quadratic frame it comes from the separate good-generator
noncollapse theorem. Generic polynomial-line geometry alone is not
being used to assert its existence.

## 1. Exact local hypotheses and the actual entry gate

Let p be an irreducible element of the actual invariant plane S,
and use the base localization
\[
\begin{gathered}
V=S_{(p)},\quad K=\operatorname{Frac}V,\quad
k=V/pV,\quad B=A\otimes_S V,\\
\ker(N|_B)=V,\qquad B_K=K[v],\qquad
N|_{B_K}=\lambda\partial_v,\quad\lambda\in K^*,\\
B/pB=k'[w],\qquad [k':k]=2,\qquad
\bar N\ne0,\qquad
U\in\ker N^3\text{ with }\bar U\notin k'.
\end{gathered}
\tag{1}
\]
Here V is a DVR containing Q with uniformizer p and residue
characteristic zero, as is automatic for the actual V over C.
The ring B is a domain, and N is locally nilpotent. All residue and kernel
statements concern the whole indicated rings. In particular the
last condition means that Ubar is a nonconstant polynomial in w.
The nonzero divisor derivation is a translation over k', whose
kernel is exactly k'.

For the supplied original quadratic frame, all these assertions
are verified in [divisor91](nonconical-residue-degree-bound-pass91.md).
That proof gives the actual whole ring k'[w], nonzero reduced
primitive field, and a surviving U among A1,A2. Each good generator
has generic N-degree at most two. Its residue-degree inequality
then gives degree exactly two generically and degree one in w.
The proof below needs only the nonconstant residue, not this last
degree-one conclusion. No first-normal hypothesis or condition on
L at a closed point is required for (1).

## 2. A primitive first-degree generator detects the extension

Put F_n=ker(N^(n+1)|B) and I_n=N^n(F_n). These modules are finite:
F0=V, and N^n identifies F_n/F_(n-1) with the ideal I_n of the
Noetherian ring V. Induction proves finiteness. They are torsion
free because B is a domain, hence free over the DVR. Invariant
localization commutes with kernels, and the generic polynomial
line fixes their ranks at n+1.

The ideal I1 is a nonzero principal ideal p^e V. Choose r with
Nr=p^e, absorbing the invariant unit of a generator into r.
Every F1 element differs from a V-multiple of r by an invariant,
so
\[
\begin{gathered}
F_n\simeq V^{n+1},\qquad F_1=V\oplus Vr,\qquad
Nr=p^e,\\
e\ge1,\qquad \bar r\in k'\setminus k,\qquad
k'=k(\bar r),\qquad \{1,\bar r\}\text{ is a }k\text{-basis of }k'.
\end{gathered}
\tag{2}
\]
If e were zero, r would be a slice and the finite slice expansion
would give B=V[r]. Its residue ring would have constant field k,
contrary to the quadratic extension in (1). Thus e is positive,
so rbar is killed by Nbar and belongs to k'. If rbar belonged to
k, lift it to a0 in V. Then (r-a0)/p belongs to B and has
derivative p^(e-1), contradicting the definition of I1. This is
division in the actual ring B, not in a completion. Since the
extension has degree two, rbar generates it.

The three residues 1,rbar,Ubar are independent over k: a nonzero
coefficient of Ubar would make it algebraic over k', and the
other two are independent by (2). They therefore form an actual
V-basis 1,r,U of the rank-three module F2, by Nakayama. This
also proves its specific fiber injection. It is not a claim
that an arbitrary degree module always injects into B/pB.

## 3. The conic coefficient is a unit

Write NU=alpha r+beta with alpha,beta in V, using F1. The element
gamma=alpha r^2+2beta r-2p^e U is killed by N and thus belongs
to V. If alpha were in pV, reducing this equality would give
2 beta-bar rbar=gamma-bar in k. Independence in (2) would force
beta into pV as well. That would make Nbar Ubar zero, contrary
to Ubar being nonconstant under the translation in (1).
Consequently alpha is a unit. Define
\[
\begin{gathered}
t=2U/\alpha,\qquad a=2\beta/\alpha,\qquad b=-\gamma/\alpha,
\qquad a,b\in V,\\
p^e t=r^2+ar+b,\qquad Nr=p^e,\qquad Nt=2r+a,\\
T^2+\bar aT+\bar b\in k[T]
\text{ is irreducible and separable.}
\end{gathered}
\tag{3}
\]
The final polynomial vanishes at rbar and is monic quadratic;
(2) makes it the minimal polynomial. Characteristic zero gives
separability. In particular its derivative at rbar is nonzero.
No unit assumption on a second image ideal was imported: the
unit alpha was proved from the actual residue field and U.

## 4. All-degree bases give the entire algebra

The element r has degree one, and U, hence t, has degree two.
Indeed a degree-one U would be in F1 and would have constant
residue in k'. For every integer j at least zero, set
\[
\begin{aligned}
\mathcal B_{2j}&=\{1,t,\ldots,t^j\}
 \ \cup\ \{r,rt,\ldots,rt^{j-1}\},\\
\mathcal B_{2j+1}&=\{1,t,\ldots,t^j\}
 \ \cup\ \{r,rt,\ldots,rt^j\},\\
\boxed{\qquad F_n=\bigoplus_{q\in\mathcal B_n}Vq,
\qquad F_n\cap pB=pF_n.\qquad}
\end{aligned}
\tag{4}
\]
The second set is empty for j=0 in the first line. Leibniz's
formula puts each set in F_n, and each contains n+1 elements.
A residue relation has the form P(tbar)+rbar Q(tbar)=0 with
P,Q in k[T]. Since tbar is transcendental over k' and 1,rbar
are independent over k, both polynomials are zero. Hence the
n+1 residues are independent. Freeness of rank n+1 and
Nakayama give (4), including its intersection equality.

Local nilpotence makes the union of the F_n equal to B. Thus
B=V[r,t]. The relation in (3) gives a surjection from the conic
presentation below. Its source is free over V[t] with basis
1,r, since the equation is monic in r, and hence is V-torsion-free.
Over K the equation solves for t; r has generic degree one and
generates K[v]. The surjection becomes an isomorphism over K,
so its torsion kernel was already zero. We have proved
\[
\begin{gathered}
\boxed{\quad
B\simeq V[\mathsf r,\mathsf t]/
(p^e\mathsf t-\mathsf r^2-a\mathsf r-b).
\quad}\\
B/pB=k'[\bar t],\qquad
r_0=r+a/2,\quad \eta=a^2/4-b\in V^*,\\
\boxed{\quad p^e t=r_0^2-\eta,\qquad
Nr_0=p^e,\qquad Nt=2r_0,\qquad
\bar\eta\text{ is nonsquare in }k^*.\quad}
\end{gathered}
\tag{5}
\]
Irreducibility in (3) makes eta a unit with nonsquare residue.
The shift by a/2 preserves the bases in (4). The equality of the
whole residue ring also shows tbar is a degree-one coordinate
on the original k'[w]. No normalization, formal descent or
unproved finite-module generation step has been inserted.

## 5. Exact derivative-image valuations

In K[r0], one has N=p^e partial_(r0) and t=(r0^2-eta)/p^e.
The sole basis element of degree 2j is t^j, with top coefficient
p^(-ej). The sole basis element of degree 2j+1 is r0 t^j,
with the same top coefficient. Differentiation therefore gives
\[
\begin{gathered}
N^{2j}(t^j)=(2j)!\,p^{ej},\qquad
N^{2j+1}(r_0t^j)=(2j+1)!\,p^{e(j+1)},\\
\boxed{\quad I_n=p^{\,e\lceil n/2\rceil}V,\qquad
\operatorname{ord}_p(I_1,I_2,I_3,I_4)=(e,e,2e,2e).\quad}
\end{gathered}
\tag{6}
\]
All other members of the indicated basis have lower degree and
contribute zero to N^n. Factorials are units because V contains
the characteristic-zero field k's prime field. This proves
ideal equality, not just an upper bound from sample elements.

## 6. The selected quartic needs its additional actual input

An actual element c of generic degree four has a unique expansion
in the basis (4). Write
\[
\begin{gathered}
c=c_0+c_1r_0+c_2t+c_3r_0t+c_4t^2,\qquad c_i\in V,
\qquad c_4\ne0,\\
N^4c=24p^{2e}c_4,\\
\deg_{\bar t}\bar c=2
\quad\Longleftrightarrow\quad c_4\in V^*
\quad\Longleftrightarrow\quad
\operatorname{ord}_p(N^4c)=2e.
\end{gathered}
\tag{7}
\]
The coefficient of tbar squared is c4-bar, while all other
terms have residue degree at most one. In the actual collapsed
mixed sector with L(m) nonzero, at each quadratic constant-cover
divisor through m the uniform result of
[admissible-boundary106, (8)](mixed-admissible-quartic-boundary-pass106.md)
and its selected-c case give degree exactly two for cbar.
Thus all equivalent conclusions in (7) hold there. This uses
that additional actual boundary input, not generic quartic
degree alone.

For a precise intrinsic countercontrol to that weaker inference,
take V=C[p,q]_(p), eta=q, and the conic (5). Its residue extension
is k(sqrt(q))/k, where k=C(q). The element c_*=t+p t^2 has
generic degree four and nonzero reduced derivative, but its
residue is tbar and its fourth derivative is 24p^(2e+1).
It therefore has the extra valuation one. The conic is smooth:
along p=0 the derivative in r0 is a unit, and after inverting p
the equation eliminates t. It has the good generators r0,t,
so B=V[r0,t,c_*] as well. The underlying intrinsic polynomial
threefold can be written C[p,r0,t], with q=r0^2-p^e t.
None of this constructs the prescribed highest field of an
original E-frame or an actual mixed closed fiber. It isolates
exactly why the separate mixed-sector boundary condition in
(7) is needed.

## Scope and dependencies

This is a direct DVR classification under (1), with the critical
primitive first generator, surviving F2 parameter, all-degree
residue independence and whole-algebra injection proved above.
Normality and flatness are available for the actual B, but do
not replace those gates. In fact the algebraic argument uses
only the stated domain, LND, full kernel, generic line and
whole quadratic-divisor data. The resulting conic is itself
free over V[t], so flatness is also visible in its output.

The complete retained divisor91 and cyclic-module103 proofs were
reread. The latter provides the closely related all-degree
residue-basis method; the present residue argument uses a
quadratic constant field rather than a nonzero nilpotent.
The elementary DVR finite-free argument and slice projection
are written out at their points of use. No new primary-source
classification theorem, numerical method or actual-frame
counterexample is claimed. General independently derived the
unit-coefficient conic and is pursuing its global ideal
consequences. All files through106 remain unchanged.
