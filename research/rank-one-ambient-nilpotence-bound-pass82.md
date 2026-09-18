# Ambient dimension bounds the nilpotent acceleration

For an actual quadratic-time sliced action on complex n-space with only
one possibly nonzero coordinate acceleration, that acceleration has
nilpotence order at most n on the full good-speed scheme. In dimension
four this proves q to the fourth power belongs to the speed ideal.
No reducedness or principal-ideal assumption is required.

This strengthens radical membership by an explicit uniform exponent.
It does not prove q itself belongs to the ideal, and does not give a
coordinate reduction or a cancellation theorem. The exponent is an
upper bound, not a claim of sharpness among actual ambient actions.

## 1. Exact original-action hypotheses

Let n>=2 and work in actual polynomial coordinates
\[
B=\mathbb C[x_1,\ldots,x_{n-1},z],\qquad
E\in\operatorname{LND}(B),\qquad E(s)=1,
\qquad E^2x_i=0,\quad E^2z=q,\quad E(q)=0.
\tag{1}
\]
Put a_i=E(x_i), b=E(z), T=partial_z, and
\[
I=(a_1,\ldots,a_{n-1})B,\qquad C=B/I.
\tag{2}
\]
The assertion is immediate if I=B. Otherwise retain all nilpotents
in C. A bar denotes the image of a coefficient or matrix in C.

The slice equation gives bar(b) bar(Ts)=1, so bar(b) is a unit.
Invariance of a_i and q gives the exact consequences
\[
T(a_i)\in I,\qquad T(q)\in I,
\qquad \overline q=\overline b\,\overline{T(b)}.
\tag{3}
\]
Indeed E(a_i)=sum_j a_j partial_j(a_i)+b T(a_i)=0, and
E(q)=sum_j a_j partial_j(q)+b T(q)=0. Reduce these identities
modulo I and cancel the unit bar(b). The final identity is E(b)=q
reduced modulo I. It does not assert T(b) lies in I.

## 2. The exact flow determinant on the nonreduced scheme

Use an independent parameter t. The actual flow is
\[
\Phi_t=(x_1+t a_1,\ldots,x_{n-1}+t a_{n-1},
 z+t b+\tfrac12t^2q).
\tag{4}
\]
It is an automorphism over \(\mathbb C[t]\), with inverse Phi_{-t}. Its
Jacobian determinant in the original n variables is one. To justify
the constant, the Jacobian determinant of a polynomial automorphism
over \(\mathbb C[t]\) is a unit of B[t], hence a nonzero complex constant;
specializing t=0 gives one.

Let
\[
L=(\overline{\partial_{x_j}a_i})_{1\le i,j<n},\qquad
d=\overline{T(b)}.
\tag{5}
\]
Differentiate (4) before reducing modulo I. By (3), its last column
has zero entries above 1+td. Its upper-left block is the identity
matrix plus tL. The bottom-left entries can be arbitrary for this
argument and are not assumed zero. Consequently the actual determinant
identity becomes
\[
1=(1+td)\det(\operatorname{Id}_{n-1}+tL)
\quad\text{in }C[t].
\tag{6}
\]
The top-left block has no quadratic t term because the first n-1
coordinate accelerations vanish exactly in B. The last-column
quadratic term vanishes modulo I because T(q) lies in I. These are
separate inputs; neither follows just from reduced pointwise data.

Write det(Id+tL)=sum_{j=0}^{n-1} e_j t^j, with e_0=1. Comparing
coefficients in the polynomial ring over C, including its possible
zero divisors, gives e_j+d e_{j-1}=0 for 1<=j<n and d e_{n-1}=0.
Induction yields
\[
e_j=(-d)^j\ (0\le j<n),\qquad d^n=0.
\tag{7}
\]
Coefficient comparison needs no cancellation of a possible zero
divisor and no rank argument over a fraction field of C.

## 3. Acceleration and the full velocity Jacobian

Combining (3) and (7) proves the dimension-dependent conclusion
\[
\boxed{\ q^n\in I.\ }
\tag{8}
\]
For n=4 the exponent is four. This uses the full scheme ideal,
not its radical, and complements the separate
[divisorial bound](rank-one-acceleration-divisorial-ideal-pass82.md).
That bound retains every multiplicity in the coefficient gcd and
proves q in I for principal I. Neither result is asserted to imply
the remaining primitive divergence condition for all nonprincipal I.

There is also a useful matrix consequence. Let N be the image modulo
I of the full original Jacobian of the velocity vector (a_1,...,a_{n-1},b).
Its last column is (0,...,0,d)^t, by (3). Thus it is block lower
triangular with diagonal blocks L and d. Equations (7) imply
char_L(lambda)=sum_{j=0}^{n-1}d^j lambda^{n-1-j}. Multiplication
by lambda-d gives lambda^n-d^n=lambda^n. Therefore the
Cayley--Hamilton identity over the commutative ring C gives
\[
\operatorname{char}_N(\lambda)=\lambda^n,
\qquad N^n=0.
\tag{9}
\]
This statement is only on the speed scheme. The original velocity
Jacobian over B need not be nilpotent, and no such assertion is made.

## 4. Exact effect on the quotient-only models

The [speed-quotient note](rank-one-speed-quotient-pass82.md) proves
C=R[z]=R[s], with z=c_0+c_1s+(bar(q)/2)s squared, where c_1 is
a unit and bar(q) is nilpotent. Its abstract quotient controls allow
every nilpotence order. Equation (8) supplies an additional ambient
restriction those controls did not impose.

In particular, the quotient model R=C[u,v,epsilon]/(epsilon^N),
z=s+epsilon s squared/2, E=partial_s cannot be the exact speed
quotient of an action satisfying (1) on C four-space if N>=5:
its acceleration epsilon has nonzero fourth power. This does not
exclude those rings as unrelated quotients, and does not exclude
models of orders two through four from ambient realization. No such
realization is constructed here.

The calculation identifies a concrete next proof question: do the
remaining original-coordinate identities reduce the exponent to one,
or can a genuine actual action have a nonzero quadratic coefficient
of one of these bounded nilpotence orders? A formal matrix satisfying
(6) alone would not provide a polynomial action or a global slice.

All steps above are elementary identities in the actual flow and its
specified quotient. No new classification theorem is imported. The
result is a written working proof. Root reconstructed the calculation;
General and Jet each independently read the full note and checked all
nine displayed steps, including coefficient comparison over the
nonreduced quotient and the characteristic-polynomial signs. The
ground-field notation in Section 2 was clarified after review. These
are AI-agent proof audits, not human expert review, a novelty finding
or formal proof certification. The separate
[symbolic controls](rank-one-speed-controls-pass82.md) and
[targeted run](verification-pass82-working.json) now record four finite
methods; they do not formally verify the universal theorem. No frozen
file is changed by this note.
