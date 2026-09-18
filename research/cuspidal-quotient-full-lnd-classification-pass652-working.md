# Full additive-action classification for the changed quotient

For the quotient computed in651, every locally nilpotent derivation
fixes the original two-variable base. Thus the additional plinth
generator found there cannot yield a base-moving auxiliary action.
This closes that specific changed-quotient route. It neither classifies
arbitrary actions on the original cylinder nor proves cancellation.
Novelty is UNKNOWN; the proof below is a private working argument.

## 1. Statement and two elementary facts

Put A=C[a,b], p=b^2-a^3, and
\[
K=\mathbb C[a,b,v,w]/(p^2w-v^5+b^6),\qquad
\delta_0=p^2\partial_v+5v^4\partial_w.
\]
Then
\[
\operatorname{LND}(K)=\{f\delta_0:f\in A\},
\qquad \operatorname{ML}(K)=A.
\tag{1}
\]
Here zero is included among LNDs. All derivations are C-linear.

We use the elementary semivariant property: in a characteristic-zero
domain with LND delta, delta(q) in qR implies delta(q)=0. For if
delta(q)=qh is nonzero, additivity of the delta-degree on products
gives deg_delta(delta(q))>=deg_delta(q), whereas differentiation
lowers its finite positive delta-degree by one.

We also use the following special polynomial-orbit argument. If an
LND on a characteristic-zero domain fixes the nonzero element
p=b^2-a^3, it fixes a and b. Over its fraction field, their orbit
polynomials X(T),Y(T) satisfy Y^2-X^3=p and are coprime. If their
degrees r,s are both positive, differentiating gives X^2 dividing
Y' and Y dividing X'. Thus 2r<=s-1 and s<=r-1, impossible.
If one is constant, the other is also constant. This is the
Mini-Mason argument already attributed in the ledger, not a new
general theorem.

## 2. The associated graded algebra

Embed K into A[p^{-1}][v], with w=(v^5-b^6)/p^2, and use v-degree.
The monic-v basis writes every element uniquely as
\[
\sum_{j\ge0,\ 0\le i<5} f_{ij}(a,b)v^i w^j.
\]
The displayed summands have distinct exact degrees i+5j whenever
their coefficients are nonzero, so the highest degrees cannot cancel.
This is the admissible nonnegative filtration with weights
deg(a)=deg(b)=0, deg(v)=1, deg(w)=5. Its associated graded domain is
\[
G=A[v,w]/(p^2w-v^5).
\tag{2}
\]
For each N>=0, with unique N=i+5j and 0<=i<5, its homogeneous part is
G_N=A v^i w^j. For N<0 it is zero. These assertions follow directly
from the same basis; (2) is also a domain by its primitive linear
equation in w.

## 3. Every nonzero homogeneous LND has degree minus one

Let delta be a homogeneous nonzero LND on G of degree e.
If e<=-2, it kills a,b,v by degree. The defining relation then forces
it to kill w, a contradiction. If e=-1, it kills a,b and has
delta(v)=F in A, delta(w)=Hv^4 with H in A. The relation gives
5F=p^2H. Thus delta=f*delta_0 for f in A.

Suppose e>=0. Unless e=5j-1 for some j>=1, the homogeneous part
G_{e+1} is divisible by v, so delta(v) is divisible by v. The
semivariant property gives delta(v)=0. Since p^2w=v^5, factorial
closure of the kernel gives delta(p)=delta(w)=0. The polynomial-orbit
argument then fixes a,b, making delta zero, a contradiction.

It remains to exclude e=5j-1, j>=1. In that case there are A,B0,C,H
in the polynomial ring C[a,b] such that
\[
\begin{aligned}
\delta(a)&=v^4w^{j-1}A,&\delta(b)&=v^4w^{j-1}B_0,\\
\delta(v)&=w^jC,&\delta(w)&=v^4w^jH.
\end{aligned}
\]
The last expression is divisible by w, so delta(w)=0. Write
M=2bB0-3a^2A. Differentiating p^2w=v^5 now gives
\[
\delta(p)=v^4w^{j-1}M,\qquad C=\frac25pM.
\tag{3}
\]

## 4. Normalization excludes the exceptional case

Since delta fixes w, localize to F=C(w) and put
H0=F[a,b,v]/(p^2w-v^5). The localization remains a domain and
delta remains an LND. In its fraction field put r=p/v^2. Then
\[
r^2=v/w,\qquad r^5=p/w^2.
\]
Its normalization is exactly
\[
S=H_0[r]=F[a,b,r]/(b^2-a^3-w^2r^5).
\tag{4}
\]
Indeed r is integral by its quadratic equation, and v=wr^2,
p=w^2r^5 give the displayed finite birational presentation. This
presentation is a domain: a^3+w^2r^5 is not a square in F(a,r),
as seen from its odd degree in a and the valuation at a=infinity.
The Jacobian of b^2-a^3-w^2r^5 vanishes exactly at a=b=r=0.
Consequently this two-dimensional hypersurface domain is normal
by S2 and R1, proving that it is the whole normalization.

The LND extends as an LND to S. For completeness, exp(T delta) is
an automorphism of H0[T], fixing T. It extends to the fraction
field and preserves its integral closure S[T]. Thus it sends S
into S[T], and the identity and addition laws still hold there.
In characteristic zero its infinitesimal derivation is locally
nilpotent. This proves the required normalization-extension fact
in this setting; ordinary derivation extension alone would not suffice.

Using (3) in the fraction field computes that extended derivation:
\[
\begin{aligned}
\delta(r)
 &=\frac{\delta(p)}{v^2}-\frac{2p\delta(v)}{v^3}
   =\frac15v^2w^{j-1}M\\
 &=\frac15w^{j+1}r^4M\in rS.
\end{aligned}
\tag{5}
\]
The semivariant property on S forces delta(r)=0. Hence delta(p)=0
and delta(v)=0. The polynomial-orbit argument fixes a,b too, a
contradiction. This excludes the last nonnegative degree case.
Every nonzero homogeneous LND on G therefore has degree -1.

## 5. Return to the whole, nongraded quotient

Any nonzero LND epsilon on K has a finite filtration shift e: take
the maximum of deg(epsilon(z))-deg(z) for the nonzero images of
the generators z=a,b,v,w. The admissible filtration ensures that
this bounds the shift on every element, and equality on a generator
gives a nonzero induced homogeneous derivation on G. It is locally
nilpotent: iteration of its leading action agrees with the leading
image of iteration of epsilon until that image drops degree, at
which point it is zero. The finite nilpotence of every generator
therefore carries over to the graded derivation.

The preceding classification forces e=-1. It follows that epsilon
kills the degree-zero subalgebra A, and epsilon(v)=F in A. Also
epsilon(w) has degree at most four, so write it uniquely as
sum_{i=0}^4 H_i v^i, with H_i in A. The defining equation gives
\[
p^2\sum_{i=0}^4H_i v^i=5v^4F.
\]
Thus H_i=0 for i<4 and F=p^2H_4/5. This proves epsilon=f*delta_0.
Conversely every such invariant replica is locally nilpotent,
since delta_0 is triangular over A. For a nonzero replica its kernel
is A: localizing
at p gives a scalar multiple of partial_v on A[p^{-1}][v], and
the same normal-form degrees show K intersect Frac(A)=A.
The nonzero derivation delta_0 and the fixation of A prove (1).

## 6. Consequence and verification boundary

By651 the plinth of the changed action on R[u] is (b,p^2,v^4)K.
The classification (1) says that EVERY auxiliary LND on K fixes
a,b, whether or not a base invariant was initially supplied.
Moreover, an auxiliary LND fixing v is zero. In particular the
extra generator v^4 cannot be fixed by a nonzero auxiliary LND.
For a nonzero auxiliary LND, its invariant plinth elements lie in A. All
plinth-compatible lifts built from these auxiliary actions fix A.
This last assertion refers to the usual extension on a local-slice
chart that agrees with the auxiliary action on K, possibly after
an invariant multiplication to clear denominators. It does not
classify all LNDs on R[u].

The proof actually applies to every q in A:
\[
K_q=A[v,w]/(p^2w-v^5+q(a,b)),\qquad
\operatorname{LND}(K_q)=A\delta_0,\quad\operatorname{ML}(K_q)=A.
\tag{6}
\]
There is no extra condition on q. The equation remains primitive
linear in w because it is monic in v, and the monic-v basis still
has distinct exact degrees i+5j after substituting
w=(v^5-q)/p^2. Thus the associated graded algebra and its proof are
unchanged. Once epsilon kills A, it also kills q, so Section5
classifies it by exactly the same differentiated relation. This
is a uniform consequence, not an extrapolation from finitely many q.

General found the exceptional normalization argument. Root separately
reconstructed all degree cases and the action extension, and fresh
unsaved4c5b39 checked the complete identities (3)--(5), with an
arbitrary invariant factor standing for w^{j-1}. A finite grading
arithmetic check accompanied it but is not the uniform proof.
Geometry and Jet read all182 initial saved lines at
SHA2563595ac8f2da2a8d67811403e5b6fe5984881f62c43e4202388f462995871d985
(EOFf4eeab andd2a609). Jet requested two explicit nonzero-action
qualifiers, which were applied; both reviewers then reread the
changed tail, including the arbitrary-q corollary, at
SHA256bb231eba5364b7cd8b15a85f2c96b7b893b56bfc835b19df2389fe03d5205c65
and reported CLEAN (e8158d and2cff1e). Jet's separate fresh53c3a2
checked the whole exceptional and canonical-flow identities.
Root's complete revised-source read wasa186f7. Only this provenance
changed after those reviews. Status: internally checked within scope.
No saved checker was run, imported, compiled, or changed. This is
not expert review or proof-assistant verification. No cancellation
theorem, cylinder-polynomiality assertion, or novelty claim is made.
