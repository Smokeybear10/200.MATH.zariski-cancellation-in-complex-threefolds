# A highest locally nilpotent adjoint cannot be purely vertical

A sliced locally nilpotent derivation cannot be the sole direction
of a nonzero highest adjoint of another LND. The proof uses an
actual Laurent-parameter conjugation and specialization, not an
assumption that an arbitrary leading coefficient is locally nilpotent.
This supplies the missing original-ring step when a coordinate
partial becomes good only after invariant division of the action.

## 1. Statement

Let \(B\) be a domain over a characteristic-zero field \(k\),
and let
\[
E,T\in\operatorname{LND}_k(B),\qquad E(s)=1,\qquad A=\ker E.
\]
By the slice identity, \(B=A[s]\). Suppose for an integer
\(n\ge1\) that
\[
\operatorname{ad}_E^{n+1}T=0,\qquad
\operatorname{ad}_E^nT=hE\quad
\text{for some }h\in\operatorname{Frac}B.
\tag{1}
\]
**Lemma.** Then \(h=0\), so \(\operatorname{ad}_E^nT=0\).

No coordinate assertion about \(s\) is needed. The polynomial
extension \(A[s]\) is the actual extension supplied by the
original slice. The lemma does not assume that \(A\) is a
polynomial ring over \(k\).

## 2. Exact degree bounds in the sliced extension

Evaluation of (1) on \(s\) gives
\(h=(\operatorname{ad}_E^nT)(s)\in B\).
Taking its bracket with \(E\) gives \((Eh)E=0\), hence
\(Eh=0\) and \(h\in A\).

On \(A[s]\), the original action is \(E=\partial_s\).
For each \(a\in A\), (1) implies \(E^n(Ta)=0\), so
\[
T(a)=\sum_{j=0}^{n-1}a_j s^j,\qquad a_j\in A.
\tag{2}
\]
For \(n\ge1\), the commutator expansion evaluated on \(s\)
is \((\operatorname{ad}_E^nT)(s)=E^n(Ts)\), since
\(T(Es)=T(1)=0\) and \(E^2s=0\). Therefore
\[
T(s)=\sum_{j=0}^{n}b_j s^j,\qquad b_j\in A,
\qquad n!b_n=h.
\tag{3}
\]
These degree statements hold for every actual \(a\in A\);
finite generation of a presentation of \(A\) is not required.

## 3. An actual locally nilpotent degeneration

Adjoin an indeterminate \(z\) killed by \(T\). On
\(A[s,z,z^{-1}]\), let \(\Phi\) be the automorphism fixing
\(A,z\) and taking \(s\) to \(s/z\). Define
\[
T_z=z^{n-1}\Phi T\Phi^{-1}.
\tag{4}
\]
This is an LND of the Laurent ring: conjugation preserves local
nilpotence, and the multiplier is an invariant unit. Equations
(2)--(3) give the explicit images
\[
T_z(a)=\sum_{j=0}^{n-1}a_j s^j z^{n-1-j},\qquad
T_z(s)=\sum_{j=0}^{n}b_j s^j z^{n-j},\qquad T_z(z)=0.
\tag{5}
\]
Thus \(T_z\) preserves the actual polynomial subring \(A[s,z]\).
Its restriction is locally nilpotent, because vanishing in the
Laurent ring implies vanishing in this injected subring.
The ideal \((z)\) is stable. Passing to the quotient produces
an LND \(T_0\) of \(A[s]\) satisfying
\[
T_0(s)=b_n s^n.
\tag{6}
\]
No pointwise family of unrelated derivations has been specialized:
the whole parameter-ring derivation is locally nilpotent before
restriction and quotient.

For a nonzero element \(f\) of a characteristic-zero domain with
LND \(D\), the largest nonzero iterate defines an additive
degree on nonzero products. A nonzero derivative strictly lowers
that degree. Consequently \(f\mid Df\) implies \(Df=0\):
otherwise \(Df=qf\ne0\) would have degree at least that of \(f\).
Apply this fact to \(D=T_0\), \(f=s\) in (6). Since \(n\ge1\),
\(s\) divides its displayed derivative, so \(T_0(s)=0\).
The domain property yields \(b_n=0\), and (3) gives \(h=0\).
This proves the lemma, including \(n=1\).

## 4. Divided-good coordinate partials descend to original-good ones

The instance used in the moving cubic argument is the following.
Let \(B\) be an actual polynomial ring, \(E\) have the original
polynomial slice, and \(0\ne g\in\ker E\). Let \(T\) be an
actual coordinate partial satisfying
\[
\operatorname{ad}_E^3T=0,\qquad
\operatorname{ad}_{E/g}^2T=0
\quad\text{on }B_g.
\tag{7}
\]
The exact rescaling identity is
\[
0=g^{-2}\operatorname{ad}_E^2T
 +2g^{-3}\bigl([E,T]g\bigr)E.
\tag{8}
\]
Hence the original \(\operatorname{ad}_E^2T\) is parallel to
\(E\) over the fraction field. The actual coordinate partial
is an LND on \(B\), and the first condition in (7) gives the
other hypothesis of (1). The lemma with \(n=2\) proves
\(\operatorname{ad}_E^2T=0\) in the original ring.

The conclusion is about the original polynomial partial and
action. It does not assume that \(T\) is an LND on \(B_g\),
or infer a global coordinate from a merely localized slice.
Without the original slice, the Laurent construction over the
actual extension \(A[s]\) has not been supplied by this proof.

## Proof and source scope

The proof of the exclusion is given in full above. Its slice
identity is the domain-and-slice theorem, for example Theorem 2.5
in Dasgupta and Gaifullin's [*On locally nilpotent derivations of
polynomial algebra in three variables*](https://arxiv.org/html/2306.00510v2).
That statement was directly checked; the argument does not
apply a polynomial-kernel classification to the unknown \(A\).
The rescaling formula is the direct derivation identity retained
in [the full highest-vector reduction](two-quadratic-top-line-pass42.md),
Section 5.

This is a conditional algebraic lemma, not a general cancellation
solution. It does not assert a new historical result without a
statement-level novelty audit. Independent AI reconstruction or
finite controls are not human expert review or formal verification.
