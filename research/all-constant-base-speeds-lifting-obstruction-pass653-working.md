# All constant base speeds in the cuspidal control

For the fixed second-kind control625, no choice of a speed f in
the original base ring makes a plinth-compatible auxiliary lift
move that base. The invariant algebras change with the exact
divisibility of f by the cusp polynomial. We compute each entire
algebra and handle every case, including f=0.

This is a classification of this construction, not of arbitrary
actions on the cylinder. It does not establish polynomiality of
that cylinder or solve the main cancellation problem. Novelty is
UNKNOWN. The rigidity theorem used for comparison is published.

## 1. Setup and full statements

Put A=C[a,b], p=b^2-a^3,
\[
R=A[s,t]/(p^2t-s^5+b),\quad B=R[u],\quad
D(s)=p^2,\ D(t)=5s^4,\ D(A)=0.
\]
For f in A let L_f=D+f*partial_u and K_f=ker_B(L_f).
Here the subscript f denotes the chosen speed, not localization.
These are LNDs because the summands commute.

The full kernels are as follows:

| Speed | Whole invariant algebra and actual coordinates |
| --- | --- |
| p does not divide f | A[v,w]/(p^2w-v^5+bf^5), with v=fs-p^2u, w=(v^5-bf^5)/p^2 |
| f=pg, p does not divide g | A[v,w]/(pw-v^5+bg^5), with v=gs-pu, w=(v^5-bg^5)/p |
| f=p^2g, including f=0 | A[z], with z=u-gs |

The first two rows have Makar-Limanov invariant A. In the last
row the full plinth of L_f is p^2 A[z]. Therefore, in EVERY row,
any auxiliary LND epsilon of K_f whose kernel contains a nonzero
plinth element fixes a,b. The usual local-slice lift, agreeing with
epsilon on K_f up to invariant multiplication, also fixes a,b.
No existence assertion for such a lift is required for this obstruction.

## 2. Saturation proves the first whole kernel

Assume p does not divide f. The proposed v,w are polynomials:
\[
w=f^5t-5f^4s^4u+10f^3s^3p^2u^2-10f^2s^2p^4u^3
       +5fsp^6u^4-p^8u^5.
\]
They are invariant and satisfy p^2w=v^5-bf^5. The candidate S is
a domain by its primitive linear equation in w and has free A-basis
v^i w^j for 0<=i<5. After inverting f, the slice u/f gives
S[1/f]=K_f[1/f]. If f is a nonzero constant this already proves
equality. Otherwise reduce the map S to B modulo f. The residue
coordinates are v=-p^2u and w=-p^8u^5.

Multiplication by p is injective on A/(f), since gcd(f,p)=1 in
the UFD A. The free basis v^i w^j maps to distinct powers u^{i+5j}
times nonzerodivisor coefficients. The ring (A/(f))[u] embeds in
B/fB by the monic relation in s. Thus S/fS to B/fB is injective,
even if f has repeated or multiple irreducible factors. It follows
that S intersect fB=fS, and minimal-denominator descent gives S=K_f.
The action classification652, with q=bf^5, fixes A for every LND
of this entire kernel.

## 3. Saturation in the divisibility-one case

Let f=pg with p not dividing g. In this case the divided coordinate
v=gs-pu is essential. The actual second invariant is
\[
w=g^5pt-5g^4s^4u+10g^3s^3pu^2-10g^2s^2p^2u^3
       +5gsp^3u^4-p^4u^5.
\tag{1}
\]
Whole expansion proves L_f(v)=L_f(w)=0 and pw=v^5-bg^5.
The candidate S=A[v,w]/(pw-v^5+bg^5) is a domain by its primitive
linear equation in w. After inverting p, both S and K_f become
A[1/p][v]: indeed u=(gs-v)/p and L_f(s)=p^2.

Write A0=A/(p), whose fraction field is C(lambda), with
a=lambda^2,b=lambda^3. The element b is not a fifth power there,
and X^5-b is irreducible over C(lambda). For example the extension
obtained by adjoining lambda^(1/5) has degree five and a root
lambda^(3/5) generates it. Consequently
A0[s]/(s^5-b) is a domain, by its free monic basis, and so is
B/pB=(A0[s]/(s^5-b))[t,u].

Modulo p, the candidate map has
\[
v=\overline g s,\qquad w=-5\overline g^4s^4u.
\]
Here gbar is nonzero. In the candidate's free A0-basis v^i w^j,
the index j gives distinct u-powers. For fixed j, cancel the nonzero
common factor (-5gbar^4s^4)^j; the remaining gbar^i s^i for 0<=i<5
are independent over A0 by the monic s-basis. This proves residue
injectivity and hence S intersect pB=pS. Minimal-p-denominator
descent proves the second whole-kernel assertion.

## 4. All actions for coefficient p

For any q in A put H_q=A[v,w]/(pw-v^5+q). Then
\[
\operatorname{LND}(H_q)=A\,(p\partial_v+5v^4\partial_w),
\qquad \operatorname{ML}(H_q)=A.
\tag{2}
\]
Use the same exact monic normal-form filtration as652 with
weights0,0,1,5. The associated graded domain is H=A[v,w]/(pw-v^5).
A homogeneous nonzero LND of degree e<=-2 is impossible by degree
and the relation. At degree -1 it is an A-replica of the displayed
action. For e>=0, unless e=5j-1 with j>=1, its image of v is
divisible by v. The LND semivariant property, factorial closure,
and the fixed-p polynomial-orbit argument then force it to be zero.
In the exceptional case its image of w is divisible by w, hence zero.

Localizing w gives an LND on
\[
F[a,b,v]/(b^2-a^3-v^5/w),\qquad F=\mathbb C(w).
\]
Over an algebraic closure of F, choose theta^5=w. The change
(X,Y,Z)=(b,-a,-v/theta) identifies the equation with X^2+Y^3+Z^5.
Gupta--Pal's Theorem5.6 says this domain is rigid.[^rigidity]
A nonzero LND stays nonzero after faithful field extension, so
the exceptional case is impossible too. Returning to H_q, the
leading derivation therefore always has degree -1 and fixes A.
The degree<=4 normal form for epsilon(w) and the differentiated
relation p*epsilon(w)=5v^4*epsilon(v) give (2) exactly, as in652.

There is also an independent elementary exclusion for this last
homogeneous case. Write J=w^{j-1} and
\[
\delta(a)=v^4JP,\quad\delta(b)=v^4JQ,\quad
\delta(v)=\tfrac15wJ(2bQ-3a^2P),\quad\delta(w)=0,
\]
where P,Q belong to A. The ideal I=(a,b,v) is delta-stable,
so its exponential sends I onto I[T]. Over the fraction field
the orbit polynomials X,Y,V of a,b,v therefore generate the unit
ideal. Their relation Y^2-X^3=V^5/w makes them pairwise coprime.
If V is constant, p is invariant and the fixed-p argument finishes.
Otherwise put r=deg(X),s=deg(Y),t=deg(V)>0. The Wronskian
\[
W=(X^3)'Y^2-X^3(Y^2)'
\]
is nonzero: if it vanished, X^3/Y^2 would be constant and
coprimeness would make X,Y, then V, constant. It is divisible by
X^2YV^4, using pairwise coprimeness and the alternative expressions
\[
W=((X^3)'V^5-X^3(V^5)')/w
  =(V^5(Y^2)'-(V^5)'Y^2)/w.
\]
Thus 2r+s+4t<=3r+5t-1 and 2r+s+4t<=2s+5t-1, giving
r<=2t-2 and s<=3t-3. At least one of X,Y is nonconstant.
But X'=V^4JP(X,Y), Y'=V^4JQ(X,Y) imply that any such
nonconstant polynomial has degree at least 4t+1, a contradiction.
This independently verifies the particular homogeneous exclusion
needed here; it is not presented as a new general rigidity theorem.

## 5. The remaining speeds, including zero

If f=p^2g, set z=u-gs. Then B=R[z] and L_f=D, killing z.
The adapted monic basis s^i t^j, 0<=i<5, now over A[z], has
distinct D-degrees i+5j. Therefore its degree-zero module is
A[z] and its degree-at-most-one module is A[z]+A[z]s.
This proves K_f=A[z] and the full plinth p^2 A[z].

If an auxiliary LND fixes a nonzero plinth element p^2h, factorial
closure makes it fix p. The invariant relation p=b^2-a^3 and
the polynomial-orbit argument then make it fix a,b. This includes
the zero auxiliary derivation and f=0. It does not assert that
all LNDs of the polynomial quotient fix A: only those satisfying
the required nonzero invariant-plinth condition do.

## 6. Verification and exact remaining scope

The three rows exhaust every f in A. In the first two rows every
auxiliary LND fixes A; in the third row every plinth-compatible
auxiliary LND fixes A. Thus this entire constant-base-speed family
fails to produce a base-moving action by the specified lift.
There is no bound on the degree of f or on the auxiliary action.

Root's fresh unsaved48e155 and General's separatef6f3fa checked
the full polynomial invariant relations and the shear. Jet's
fresh9f3f45 checked the Wronskian and exceptional-derivation identities.
Root's separatef325e8 also checked both full Wronskian identities
modulo the defining equation and its derivative. The written
basis/saturation and degree proofs supply the all-degree assertions.
General and Jet read all191 saved lines at
SHA256081e3c7959f821a711384307cf94dd8fc586fc6900c0446372982346a8baf730
and reported CLEAN (complete EOF3db881/7cb39e; unchanged final
hashes73c75b/decba0). Jet's independent freshed7b3d checked the whole
invariant constructions, residues, shear inverse, and E8 scaling.
Both reviewers reopened the primary theorem's exact hypotheses
and applicable proof. Root's full saved-source read was0485d3.
Only this verification provenance changed after those reviews.
Status: internally checked within the stated scope.
No saved checker was executed, imported, compiled, or changed.

Arbitrary original-cylinder LNDs are not shown to come from these
quotient actions and lifts. In particular the calculation does not
compute ML(R[u]), and says nothing establishing R[u]=C^[4].
The general cancellation goal remains unsolved. AI checks are not
expert review, a novelty audit, or proof-assistant verification.

[^rigidity]: Neena Gupta and Ananya Pal, [On rigidity of Pham--Brieskorn surfaces, Theorem5.6](https://arxiv.org/html/2310.01864v2), J. Algebra657 (2024), 748--772. The case (2,3,5) satisfies gcd(2,15)=1 and the characteristic-zero hypotheses. Root read the exact statement, supporting Lemmas5.4--5.5, and the applicable Case I proof. This is ordinary rigidity; no stable-rigidity conclusion is used.
