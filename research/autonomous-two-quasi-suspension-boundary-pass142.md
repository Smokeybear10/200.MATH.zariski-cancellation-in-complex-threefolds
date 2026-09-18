# Autonomous two-quasi suspensions have a linear first tail

The autonomous suspension construction cannot produce an actual dense
three-good example with a nonprimitive first tail. A published
three-variable classification forces an invariant last-coordinate
shear in every dense member of this construction. The last coordinate
may initially have large time degree, but its fixed-good minimum is
zero.

This rules out one construction lane. It is not a classification of
all actual three-good frames or a proof of cancellation.

## 1. The exact construction

Let \(C=\mathbb C[y,z,w]\), and let
\(\delta\in\operatorname{LND}_{\mathbb C}(C)\) satisfy
\(\delta^2y=\delta^2z=0\). On \(C[u]\), set \(E=\partial_u\), fixing
the three source variables, and define
\[
\begin{gathered}
X=u,\qquad Y=\exp(u\delta)y=y+u\delta y,\qquad
Z=\exp(u\delta)z=z+u\delta z,\qquad W=\exp(u\delta)w,\\
\mathbb C[X,Y,Z,W]=C[u],\qquad
(EX,EY,EZ)=(1,\delta y,\delta z),\qquad
E^2X=E^2Y=E^2Z=0 .
\end{gathered}
\tag{1}
\]
The exponential fixes \(u\) and has the polynomial inverse
\(\exp(-u\delta)\), since \(\delta\) is locally nilpotent. The source
and target coordinate rings in (1) are therefore actually equal.
Equivalently, in the original source coordinate presentation the
transported action is \(\partial_u+\delta\).

Assume the speed row in (1) has dense homogeneous cone. Because its
first entry is one, this says precisely that
\(\delta y,\delta z\) are algebraically independent over \(\mathbb C\).
In particular the rank is two and \(\delta\ne0\).

## 2. Removing the content preserves local nilpotence

Let \(f\) be a greatest common divisor of the three polynomial
coefficients \(\delta y,\delta z,\delta w\), and write
\(\delta=fD\). Here \(D\) is a polynomial derivation with relatively
prime coefficients.

The following elementary argument checks the needed hypotheses for
the classification, even if \(\delta\) is reducible. One has
\(\delta f=fD(f)\). If \(D(f)\ne0\), the degree for the nonzero LND
\(\delta\) gives
\[
\deg_\delta(\delta f)=\deg_\delta f-1
\quad\text{but}\quad
\deg_\delta(fD(f))=\deg_\delta f+\deg_\delta D(f)
\ge\deg_\delta f ,
\]
a contradiction. The degree of a nonzero product is additive because
the ring is a characteristic-zero domain; the top Leibniz coefficient
cannot vanish. It follows that
\[
\delta f=0,\qquad Df=0,\qquad
\delta^n(a)=f^nD^n(a)\ (a\in C),\qquad
D\in\operatorname{LND}_{\mathbb C}(C),\qquad D^2y=D^2z=0 .
\tag{2}
\]
The iterate identity follows by induction using \(Df=0\), and proves
local nilpotence of \(D\). Its coefficients are relatively prime, so
\(D\) is irreducible in the sense used by the cited classification.
It is nonzero because \(\delta\ne0\).

## 3. The classification leaves an invariant bad-slot shear

Wang's two-quasi classification, stated in Dasgupta--Gupta
Theorem 4.1, applies to the actual coordinates \((y,z,w)\) and the
irreducible derivation \(D\).[^1] Its first case supplies a nonzero
constant linear form \(\ell(y,z)\) killed by \(D\). Then
\(\delta\ell=fD\ell=0\), which is a nontrivial homogeneous linear
relation on the last two entries of the speed row. This contradicts
density.

In the other case there is a coordinate \(\xi\) with
\[
\mathbb C[\xi,y,z]=\mathbb C[w,y,z],\qquad D\xi=0 .
\tag{3}
\]
Put \(R=\mathbb C[y,z]\). The equality \(R[\xi]=R[w]\) forces
\(\xi=cw+P(y,z)\) for \(c\in\mathbb C^*\) and \(P\in R\).
Indeed write \(\xi\) as a polynomial in \(w\) and \(w\) as a
polynomial in \(\xi\). Neither degree is zero, and the degree of
their composition is one. Both degrees are therefore one, and the
leading coefficients multiply to one in \(R\). Its units are the
nonzero complex constants.

Since \(\delta\xi=fD\xi=0\), apply the exponential in (1) to obtain
\[
\xi=cW+P(Y,Z),\qquad
I=W+c^{-1}P(Y,Z)=c^{-1}\xi,\qquad EI=0,\qquad
\mu=0,\qquad \deg\Phi=1 .
\tag{4}
\]
The shear is a complex polynomial in the fixed good coordinates,
and its inverse is explicit. The equality \(\mu=0\) follows from
the invariant representative \(I\), whose degree cannot be negative.
The last equality uses the actual dense shear-minimum theorem141.[^2]

Thus the first tail is linear and associated to its exact generic-line
equation. No enumeration of autonomous candidates is needed.
The zero derivation and all nondense cases are outside the stated
dense conclusion, not counterexamples to it.

## 4. The remaining construction problem

The proof only covers frames obtained by this single exponential of
an autonomous three-variable derivation with the two specified
square-zero coordinates. It does not put an arbitrary three-good
polynomial frame into this form. In particular, a polynomial inverse
depending on the slice parameter need not arise from one autonomous
derivation on the projected three-ring.

This boundary is a direct application of a known classification plus
the recorded shear minimum. It is not a historical novelty claim.
An actual extra-factor search must leave this construction class;
the general primitivity and cancellation questions remain open here.

## Sources

1. Nikhilesh Dasgupta and Neena Gupta.
   [*Nice derivations over principal ideal domains*](https://arxiv.org/pdf/1701.03635v1),
   arXiv:1701.03635v1, January 13, 2017, Theorem 4.1, printed p. 9.
   The authors attribute the two alternatives to Z. Wang,
   Theorem 4.7 and Remark 5 of their reference [14].
   The classification is an external input; Wang's original proof
   is not reconstructed here.
2. [Fixed-good shears preserve the tails and determine minimal time degree141](dense-shear-minimal-tail-pass141-working.md),
   Sections 1--4. Actual dense normalization and
   \(\mu=\deg\Phi-1\).

[^1]: Source 1. Nonzero, irreducible, characteristic-zero and
    two-square-zero-coordinate hypotheses are all checked above.
[^2]: Source 2.
