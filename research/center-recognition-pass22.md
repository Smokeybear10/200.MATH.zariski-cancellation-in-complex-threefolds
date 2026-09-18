# Full-center transport can fail even for a polynomial modification

Date: 2026-09-13. This is a bounded countercontrol to the universal
center-transport route proposed after the
[finite-center lemma](universal-bridge-pass21.md). It does not disprove
polynomial recognition or cancellation. There is no priority claim,
expert review, or formal verification.

The improvement over the earlier prescribed-jet counterexample is
substantial: no quotient automorphism is prescribed here, and the
hypothetical ambient automorphism need preserve only the **reduced
denominator support**, not its multiplicities. Even those weaker
transport conditions are impossible for the example below. Its two
modified rings are nevertheless both polynomial three-rings.

## 1. The precise false continuation

The pass-21 setup gives
\[
R=\mathbb C^{[3]},\quad C=\ker D\cong\mathbb C^{[2]},
\quad Dr=p\text{ minimal},\quad(p,V)C=C,
\]
\[
S=C[T],\quad I_N=p^NR\cap C[r],\quad
\theta|_C=\mathrm{id},\quad\theta(T)=VT,
\quad J_N=\theta(I_N)S.
\tag{1}
\]
Here the contraction uses \(T\mapsto r\), and a sufficiently
large \(N\) gives
\[
S[I_N/p^N]=R,\qquad
S[J_N/p^N]\cong_C M:=R[r/V].
\tag{2}
\]

The following proposed repair is false:

> There is some \(\Phi\in\operatorname{Aut}_{\mathbb C}(S)\)
> carrying \(I_N\) onto \(J_N\) and preserving the reduced
> divisor of \(p\).

Unlike the refuted pass-21 assertion, this asks for no specified
action on \(S/(p^N)\), and does not require \(\Phi\) to fix
or preserve \(C\) a priori. Preserving the full denominator
\((p^N)\) would be an even stronger requirement.

## 2. A primitive rank-three input and its canonical centers

In \(R=\mathbb C[x,y,z]\), set
\[
f=xz-y^2,\quad r=x^3+yf^2,\quad
h=zf^4+2x^2yf^2+x^5,\quad
D=-\operatorname{Jac}(f,h,\cdot).
\tag{3}
\]
The displayed family is the \(m=2,n=2,P=x^2\) case of
Dasgupta–Gaifullin Theorem 5.7, with the derivation sign reversed.
Its theorem and proof give the primitive rank-three property, exact
kernel \(C=\mathbb C[f,h]\), and minimal derivative
\(Dr=p=f^2h\). These are the previously audited base hypotheses,
not assertions that rank follows from a proper local-slice subring.[^1]
Directly,
\[
xh=r^2+f^5,\qquad Dx=2f^2r.
\tag{4}
\]
Take
\[
V=1+fh.
\tag{5}
\]
The reduced plinth is the connected union of the two axes in
\(\operatorname{Spec}C\), and
\[
ph+(1-fh)V=1.
\tag{6}
\]

Fix **any integer \(N\ge5\)** and use the actual contraction
\(I_N=p^NR\cap S\), not an artificially chosen center.
This is a valid denominator exponent in (2). To see it explicitly,
write \(F=T^2+f^5\). In the common fraction field,
\[
x=\frac Fh,\qquad
y=\frac{h^3T-F^3}{f^2h^3},\qquad
z=\frac{h^6-2Th^3F^2+F^5}{f^4h^5}.
\tag{7}
\]
Multiplication by \(p^N=f^{2N}h^N\) clears all three
denominators when \(N\ge5\). Thus the finite-center inclusion
proof applies exactly as stated.

The radicals of all these centers have the same two prime components:
\[
\sqrt{I_N}=K_f\cap K_h,
\quad K_f=(f,T^5-h^3),\quad K_h=(h,T^2+f^5).
\tag{8}
\]
Indeed \(f,h\) are prime in \(R\): they are irreducible
coordinates of the factorially closed kernel, and \(R\) is a UFD.
Therefore
\(\sqrt{p^NR}=fR\cap hR\), and radicals commute with
contraction. Modulo \(f\), the local-slice variables become
\(r=x^3,h=x^5\), giving the first contraction in (8).
Modulo \(h\), \(f\) remains transcendental and
\(r^2+f^5=0\). The polynomial \(T^2+f^5\) is irreducible
over \(\mathbb C(f)\), giving the second contraction.

Since \(I_N,J_N\) contain \(p^N\), and \(\theta\) is the
identity modulo \(fh\),
\[
\sqrt{J_N}=\sqrt{I_N}.
\tag{9}
\]
More explicitly, \(I_N+(fh)=J_N+(fh)\); taking radicals
is legitimate because \(fh\in\sqrt{I_N}\cap\sqrt{J_N}\).

## 3. Denominator support and reduced centers constrain every map

Suppose for contradiction that
\[
\Phi(I_N)=J_N,\qquad \Phi((fh))=(fh).
\tag{10}
\]
Unique factorization in \(S=\mathbb C[f,h,T]\) forces
\(\Phi\) either to scale \(f,h\) separately or interchange
them up to nonzero constants. In either event it preserves the
subalgebra \(C\) setwise. Since a one-variable polynomial-ring
automorphism over \(C\), after correcting the coefficient
automorphism, is affine with unit leading coefficient,
\[
\Phi(T)=\kappa T+b(f,h),\qquad
\kappa\in\mathbb C^*,\quad b\in C.
\tag{11}
\]
Thus allowing an arbitrary invariant-plane embedding initially
does not guarantee that the chosen denominator admits such freedom.
Here its two components force that subalgebra to stay fixed setwise.

The interchange case is impossible. It would carry \(K_f\) onto
\(K_h\). Modulo \(h\), the image of its degree-five monic
generator would generate the same principal ideal as
\(T^2+f^5\) in \(\mathbb C[f,T]\). Its degree in \(T\)
is five, whereas the latter has degree two. Generators of a principal
ideal in this domain differ by a nonzero constant, a contradiction.

Consequently write
\[
\Phi(f)=\lambda f,\qquad \Phi(h)=\mu h,
\qquad \lambda,\mu\in\mathbb C^*.
\tag{12}
\]
It now preserves both ideals \(K_f,K_h\) separately.
Modulo \(f\), compare
\((\kappa T+b(0,h))^5-\mu^3h^3\) with
\(T^5-h^3\). Their leading terms give the multiplier
\(\kappa^5\), and their degree-four terms force \(b(0,h)=0\).
The constant term then gives \(\kappa^5=\mu^3\).
The degree-two comparison modulo \(h\) similarly gives
\[
b(f,0)=0,\quad\kappa^2=\lambda^5,
\quad\text{hence } b\in fhC.
\tag{13}
\]

All the remaining scalings actually lift to the original physical
ring. Put \(u=\mu/\lambda^4\). Equations (13) imply
\[
u^6=\lambda,\qquad u^{25}=\mu,\qquad u^{15}=\kappa.
\tag{14}
\]
The automorphism
\[
\tau_R(x)=u^5x,\quad\tau_R(y)=u^3y,\quad\tau_R(z)=uz
\tag{15}
\]
therefore restricts on \(S\) to precisely the scaling part
\(\tau(f,h,T)=(\lambda f,\mu h,\kappa T)\).
It preserves \(I_N\), because it preserves \(R,S\) and
sends \(p^N\) to a constant multiple of itself.

Normalize \(\Psi=\tau^{-1}\Phi\). Then
\[
\Psi|_C=\mathrm{id},\quad \Psi(T)=T+fhB(f,h),
\quad\Psi(I_N)=\theta_{V'}(I_N)S,
\tag{16}
\]
where
\[
V'=\tau^{-1}(V)=1+\alpha fh,
\qquad \alpha=(\lambda\mu)^{-1}\ne0.
\tag{17}
\]
The identity for the transformed center follows from
\(\tau^{-1}\theta_V\tau=\theta_{V'}\) and
\(\tau^{-1}(I_N)=I_N\).

## 4. A first-order obstruction after normalization

Since \(\Psi\) fixes \(p\), (16) and the fraction definition
of affine modification give an isomorphism
\[
R\longrightarrow M':=R[r/V']
\]
fixing \(C\). On the local-slice variable it is
\[
r\longmapsto r/V'+fhB(f,h).
\tag{18}
\]
One can use the previously audited relative-isomorphism obstruction
here, but this example has a shorter direct proof.

Localizing at \(V'\), both source and target identify with
\(R_{V'}\). Let \(\sigma\) denote the resulting automorphism.
Modulo \(f^2\),
\[
\sigma(r)\equiv r+fh(B-\alpha r).
\tag{19}
\]
Using \(x=(r^2+f^5)/h\), the exact square expansion is
polynomial in \(R_{V'}\): the shift in (18) is divisible by
\(h\), and \(V'-1\) is divisible by \(h\).
Its first-order reduction is
\[
\sigma(x)\equiv x+2frB-2\alpha fhx\pmod{f^2R_{V'}}.
\tag{20}
\]
For clarity, if \(\gamma=1/V'\), the exact expression before
reduction is
\[
\sigma(x)=\gamma^2x+(1-\gamma^2)f^5/h
                 +2\gamma frB+f^2hB^2.
\]
Here \((1-\gamma^2)/h\in R_{V'}\), so no cancellation
in a nonreduced quotient is being assumed.

The relation \(f^2y=r-x^3\), together with \(\sigma(f)=f\),
would force \(\sigma(r)-\sigma(x)^3\in f^2R_{V'}\).
Subtract the already divisible \(r-x^3\) and use (19)-(20).
After dividing the difference by \(f\), its residue modulo
\(f\) is
\[
\begin{aligned}
&h(B-\alpha r)-6x^2rB+6\alpha hx^3\\
&\hspace{1cm}=5x^5\bigl(\alpha x^3-B(0,x^5)\bigr),
\end{aligned}
\tag{21}
\]
where \(r=x^3,h=x^5\) in \(R/(f)\).
Localizing at \(V'\) changes nothing in this residue ring,
since \(V'\equiv1\pmod f\). It is a domain and contains
\(\mathbb C[x]\) injectively. Hence (21) would imply
\[
B(0,x^5)=\alpha x^3.
\tag{22}
\]
Every exponent on the left is divisible by five, and
\(\alpha\ne0\), so (22) is impossible.

This proves that (10) has no solution for every \(N\ge5\).
The proof uses the full ideals through their induced modification
map, then detects a failure already at order \(f^2\). It is not
the old constant-Jacobian obstruction to one prescribed quotient map.

## 5. Positive control and consequence for the research route

The modification \(M=R[r/(1+fh)]\) in this counterexample is
already polynomial by the complete
[finite-jet family theorem](general-local-slice-lift-pass17.md).
Precisely, take the invariant extension
\[
E=D+(1-fh)\partial_t.
\]
Equation (6) gives the slice \(s=hr+(1+fh)t\); its quotient
is \(M\). This lies in that theorem with \(A=1\),
\(B=1-fh\), \(m=n=2\), and \(P=x^2\).
It follows that \(M\cong\mathbb C^{[3]}\).

For a concrete check of the direction, put \(w=r/(1+fh)\).
The theorem's first coordinate and finite correction here are
\[
X=\frac{w^2+f^5}{h}=x-fw(r+w),\qquad
\widetilde P(X,f)=X^2+5fX^7\pmod{f^2}.
\tag{23}
\]
The accompanying \(Y,Z\) and global inverse are those of the
linked theorem. These polynomial coordinates change the embedding
of the invariant plane on the modified threefold; they need not
descend to a denominator-support-preserving automorphism of the
particular three-ring \(S=C[r]\).

Therefore the universal implication
\[
\text{polynomial modified rings}
\Longrightarrow
\text{full-center transport over the fixed denominator support}
\]
is false, even for the canonical centers and primitive connected-plinth
inputs. Increasing the common denominator exponent does not repair
this example. A successful universal recognition proof must permit
changing the denominator presentation or using intermediate overrings
or other coordinate constructions that do not descend to such a
single ambient automorphism. The existence of a terminating algorithm
with those freedoms is not established here.

## 6. Exact source boundary

Kaliman–Zaidenberg Proposition 2.1 lifts a homomorphism of affine
domains when it carries the full source ideal into the target ideal
and carries the denominator to a unit times the target denominator.
Equalities and inverse maps give isomorphisms. Corollary 2.2 is its
automorphism case. Both statements and the proposition's proof were
reread.[^2] They are sufficient lifting statements, not converses
claiming that all isomorphisms of modified varieties descend.
The direct fraction argument in Section 4 is exactly their applicable
direction. The countercontrol does not contradict either statement.

The base rank and plinth are source-dependent as stated in Section 2.
The full-center presentation uses the authoritative pass-21 proof.
The polynomiality positive control uses the internally audited family
proof. The new reduced-center comparison, normalization of all possible
scalings, and first-order contradiction are written explicitly above.
No general kernel-graph connectivity or cancellation theorem enters.

An independent symbolic execution with `/opt/anaconda3/bin/python`
and SymPy passed 17 exact controls: the local-slice relation and
derivatives, primitive coefficient gcd, Bezout identity, reduced
curve relation, reconstruction numerator identities, all three
weighted scalings, the first-order obstruction, the positive first
coordinate, and sample denominator bounds. The written exponent
inequalities prove the bound for all \(N\ge5\); finite examples
alone do not. No checker file or registry was changed in this pass.

[^1]: N. Dasgupta and S. A. Gaifullin,
    [*On locally nilpotent derivations of polynomial algebra in three variables*](https://arxiv.org/html/2306.00510v2),
    Theorem 5.7, its family definition, and its irreducibility and
    minimal-local-slice proof. The input is \(E(2,2,t_1^2)\), with
    the sign reversed. The displayed local identities here are checked
    directly and do not rely on typographical intermediate formulas
    in the rendered author text.

[^2]: S. Kaliman and M. Zaidenberg,
    [*Affine modifications and affine hypersurfaces with a very transitive automorphism group*](https://arxiv.org/pdf/math/9801076),
    Proposition 2.1 and proof, printed pp. 8–9; Corollary 2.2,
    printed p. 10. The statement concerns full ideals, not only their
    radicals, and is not a necessary criterion for abstract isomorphism.
