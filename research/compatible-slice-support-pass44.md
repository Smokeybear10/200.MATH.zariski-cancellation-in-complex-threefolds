# Compatible-slice obstructions have only divisorial support

There is an exact applicability reduction for the pass-43 rank-two
repair. A compatible slice exists globally if it exists after localization
at every prime divisor of the invariant plane. Isolated points cannot be
the sole remaining obstruction. In particular, the known localization at
\(g\) suffices when \(g\) has no common irreducible factor with a
nonzero plinth element of the actual intrinsic derivation.

The result does not show that those common factors are absent in the
remaining full-frame problem. It treats the cokernel of the first
derivation map, not all higher image ideals.

## 1. The faithfully flat cokernel lemma

Let \(R\) be a noetherian UFD, let \(A\) be a domain faithfully
flat over \(R\), and let \(D:A\to A\) be an \(R\)-derivation
whose kernel is exactly \(R\). Set
\[
H=A/D(A)
\tag{1}
\]
as an \(R\)-module. Local nilpotence is not needed in this section.

**Lemma.** If \(p,q\in R\setminus\{0\}\) are coprime and
\(p\xi=q\xi=0\) in \(H\), then \(\xi=0\).

Write \(\xi=[f]\) and choose \(a,b\in A\) with
\(Da=pf\), \(Db=qf\). Then
\[
c:=qa-pb\in\ker D=R.
\]
Faithful flatness gives the ideal contraction
\((p,q)A\cap R=(p,q)R\). Consequently
\(c=q\alpha-p\beta\) for some \(\alpha,\beta\in R\), and
\[
q(a-\alpha)=p(b-\beta).
\tag{2}
\]
Coprimality in the UFD \(R\) makes multiplication by \(q\)
injective on \(R/pR\). Flatness preserves that injection after
tensoring with \(A\). Thus (2) implies
\(a-\alpha=pt\) for some \(t\in A\). Because \(A\)
is a domain and \(p\ne0\), applying \(D\) gives
\(pf=pDt\), hence \(f=Dt\). This proves the lemma.

In particular, \((p,q)=R\) is not required. In the plane the two
curves may meet in finitely many points. No factoriality of \(A\)
is required either; flatness supplied the precise saturation in (2).

## 2. Principal annihilators and height-one detection

Every torsion element \(\xi\in H\) has a nonzero principal
annihilator. Indeed its nonzero annihilator ideal \(I\subset R\)
has finitely many generators. Let \(d\) be their greatest common
divisor and write \(I=dJ\), where the generators of \(J\) have
greatest common divisor one. The element \(d\xi\) is killed by
every member of \(J\).

There are two coprime nonzero members of \(J\): choose one nonzero
\(p\in J\), and use finite prime avoidance to choose
\(q\in J\) outside all the finitely many prime ideals generated
by the irreducible factors of \(p\). No such prime contains \(J\),
because its generators have gcd one. If \(p\) is already a unit,
the conclusion is immediate. The lemma gives \(d\xi=0\), so
\(d\in I\), and therefore
\[
\operatorname{Ann}_R(\xi)=dR.
\tag{3}
\]
This uses finite generation of an ideal of the noetherian ring \(R\),
not finite generation of the generally infinite module \(H\).

For a torsion element \(\xi\), (3) gives
\[
\xi=0
\quad\Longleftrightarrow\quad
\xi_{(\pi)}=0\text{ for every irreducible }\pi\in R.
\tag{4}
\]
If \(d\) is a nonunit, any irreducible factor of \(d\) detects
the nonzero cyclic submodule \(R\xi\simeq R/dR\).
Equivalently, the torsion submodule of \(H\) injects into the
product of its height-one localizations. The cyclic submodule of each
element has only divisorial associated primes, including their possible
multiplicities, and no component supported solely at an intersection point.

## 3. Local nilpotence confines the possible support to the plinth

Now assume that \(A\) is a complex algebra and that \(D\) is a
nonzero LND. For any nonzero plinth element
\(p=Dr\in R\), the local-slice theorem gives
\[
A_p=R_p[r/p],\qquad D(r/p)=1.
\tag{5}
\]
Integration of one-variable polynomials over the complex algebra
\(R_p\) makes \(D:A_p\to A_p\) surjective. Hence \(H_p=0\),
so every element of \(H\) is torsion and is killed by some power
of \(p\).

Suppose also that \(\xi_g=0\) for some nonzero \(g\in R\).
For suitable positive integers \(N,M\),
\(g^N\xi=p^M\xi=0\). Its exact annihilator generator \(d\)
therefore divides both \(g^N\) and \(p^M\). In particular
\[
\gcd_R(g,p)=1\quad\Longrightarrow\quad\xi=0.
\tag{6}
\]
More generally it suffices to check \(\xi_{(\pi)}=0\) at just
the finitely many prime factors common to \(g\) and \(p\).
No conclusion that the class vanishes at those common factors is
automatic. A principal full plinth may be used for \(p\), but its
principality is not needed to prove (6).

## 4. Application to a compatible slice of two commuting actions

Let
\[
B=A[s_*],\quad E=\partial_{s_*},\quad
0\ne U\in\operatorname{LND}(B),\quad [E,U]=0,
\]
and suppose \(D=U|_A\ne0\). Since \(E(U(s_*))=0\), write
\[
U=D+a_0\partial_{s_*},\qquad a_0=U(s_*)\in A.
\tag{7}
\]
Every \(E\)-slice in \(B\) is \(s_*+f\), \(f\in A\).
It is killed by \(U\) exactly when
\[
Df=-a_0.
\tag{8}
\]
Thus the exact compatibility obstruction is
\(\xi=[a_0]\in A/D(A)\). Replacing \(s_*\) changes this
class by an element of \(D(A)\), so the class is independent of
the chosen original \(E\)-slice.

In our original cylinder, \(B\simeq\mathbb C^{[4]}\).
The [previously proved intrinsic quotient theorem](intrinsic-quotient-surface-pass.md)
supplies
\[
R=\ker_A D\simeq\mathbb C^{[2]},\qquad R\to A
\text{ faithfully flat}.
\tag{9}
\]
All hypotheses of Sections 1--3 are therefore genuine, even though
\(A\) has not been identified with a polynomial three-ring.

In the pass-43 \(T_cg=0\) branch one may take
\(U=[E,T_c]=-aV/g\), up to a nonzero constant. It is an actual
polynomial LND commuting with \(E\), with \(D\ne0\). Its
compatible slice after \(g\)-localization is
\[
t=\tau/g^m\in B_g,\qquad Et=1,\qquad Ut=0,
\tag{10}
\]
because \(E\tau=g^m\), \(U\tau=0\), and \(Ug=0\).
The difference \(t-s_*\) belongs to \(A_g\). Consequently
\(\xi_g=0\), and (6) applies to the actual intrinsic plinth.
The factor in (10) is \(g^m\), not \(g^{m-1}\): the latter
normalizes a slice for \(E/g\), not for \(E\).

If the compatibility class vanishes, we obtain a new genuine global
slice \(s_*+f\) for \(E\) that is killed by \(U\). This does
not by itself make \(D\) sliced or free and is not a cancellation
conclusion. The remaining high-degree branch may have common factors
of \(g\) and its intrinsic plinth.

## 5. Scope controls

### 5.1 Genuine common-divisor torsion

On \(A=\mathbb C[x,y,t]\), set \(D=x\partial_t\) and
\(R=\mathbb C[x,y]\). The derivation \(\partial_t\) is
surjective as an \(R\)-linear map, so
\[
A/D(A)\simeq (R/xR)[t].
\]
The class \([y]\) is nonzero and its annihilator is exactly \(xR\).
On \(B=A[s]\), the commuting LND
\(U=x\partial_t+y\partial_s\) has this obstruction relative
to \(E=\partial_s\). A compatible slice exists after inverting
\(x\), namely \(s-yt/x\), but not globally. This is a genuine
polynomial-ring control for surviving divisorial support, not an
example satisfying the high-degree adjoint-frame hypotheses.

### 5.2 Faithfulness cannot be omitted

Let
\[
A_1=\mathbb C[x,y,u,v]/(xv-yu-1),\qquad
D_1=x\partial_u+y\partial_v.
\tag{11}
\]
Then \(R_1=\ker D_1=\mathbb C[x,y]\). To check the kernel,
localize at \(x\): the ring becomes
\(\mathbb C[x,x^{-1},y,u]\), with \(D_1=x\partial_u\).
If an invariant required a negative power \(x^{-N}\), its minimal
numerator would vanish modulo \(x\) in
\(A_1/xA_1=\mathbb C[y,y^{-1},v]\), forcing divisibility by
\(x\) already in \(\mathbb C[x,y]\). This contradiction proves
the displayed kernel.

The class \([1]\in A_1/D_1(A_1)\) is killed by the coprime
elements \(x,y\), since \(D_1u=x\), \(D_1v=y\), but is
nonzero. Otherwise the slice theorem would give
\(A_1=R_1[t]\), where \((x,y)A_1\) is proper, contrary to
\(xv-yu=1\). In this example
\[
(x,y)A_1=A_1,\qquad (x,y)R_1\ne R_1.
\]
The invariant map misses the origin and is not faithfully flat.
This is exactly the contraction step that Section 1 needs; having a
polynomial invariant plane alone would not suffice.

## 6. Deduplication, verification, and remaining boundary

The invariant-subtraction mechanism already appears for the special
class \([1]\) in Daigle--Kaliman's proof of Theorem 1.5, printed
page 539. That proof was directly reread in this pass; it is also
reconstructed in [the pass-27 intrinsic plinth note](intrinsic-plinth-boundary-pass27.md).
The present formulation applies it to every class in \(A/D(A)\),
uses flatness instead of factoriality of the total ring, and records
the resulting annihilator and slice-compatibility consequences.
It is not presented as a new proof mechanism or a novelty claim.

The earlier [whole-plinth component note](whole-plinth-component-pass16.md)
and [higher-image torsion note](invariant-affine-slice-pass16.md) concern
\(D^j(A)\cap R\) for arbitrary \(j\). The present subtraction
works because \(\ker D=R\). Replacing \(D\) by \(D^j\)
would replace that kernel by a larger degree module and invalidate
the invariant subtraction. No principality or saturation of all
higher image ideals follows from this proof.

The bounded independent checker is
`compatible_slice_support_checks_pass44.py`. It checks finite exact
instances of the subtraction identity, repeated-divisor annihilators,
the actual localized compatible slice, and the failed contraction in
(11). It does not replace the flatness or prime-avoidance argument.
All four methods passed in 0.082 seconds; independent complete reads
and runs passed in 0.090 and 0.093 seconds. The first run caught a sign
in the final SL2 control's comparison to its defining relation;
correcting that test assertion did not change the construction.
The theorem is a direct algebraic deduction with an independently
reconstructed proof; no historical novelty or human review is claimed.

## Sources and inherited inputs

- The actual plane and faithful-flat quotient in (9) are proved in
  [the intrinsic quotient note](intrinsic-quotient-surface-pass.md),
  using Kaliman--Saveliev,
  [*C+-actions on contractible threefolds*](https://www.math.miami.edu/~kaliman/library/KaSa.michigan.2004.quotient.pdf),
  Lemma 2.1 and Corollary 2.8. These source passages and their proof
  gates were directly reread in this pass.
- The local-slice statement (5) is also directly proved by the finite
  Taylor projection in that earlier note. Integration uses that the
  coefficient ring contains \(\mathbb Q\).
- Daniel Daigle and Shulim Kaliman,
  [*A Note on Locally Nilpotent Derivations and Variables of k[X,Y,Z]*](https://www.math.miami.edu/~kaliman/library/canada.daigle-kaliman.pdf),
  Theorem 1.5 and its gcd proof, printed pages 537--539. The original
  proof supplies the credited invariant-subtraction mechanism, not a
  claim that all higher image ideals are principal.
- The new cokernel lemma is proved in full above, rather than inferred
  from any assertion about generic fibers or principal higher image ideals.
