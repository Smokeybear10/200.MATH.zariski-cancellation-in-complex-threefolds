# Exact source limits for a good coordinate with low original flow degree

The bounded source check below did not find a recognition theorem
that applies directly to the remaining quintic coordinate data.
There is a precise coordinate-local-slice theorem in three variables,
but its polynomial-three-ring hypothesis has not been obtained here.
The retained four-variable endpoints still require an invariant
coordinate or an actual invariant relative polynomial presentation.

This is an applicability report about three selected primary sources,
not a claim that no stronger result exists anywhere in the literature.

## 1. The actual question and the two different cases

Retain an original sliced LND \(E\) of an actual four-ring
\[
B=\mathbb C[x_1,x_2,x_3,w],\qquad E(s_*)=1,\qquad
0\ne g\in\ker E,\qquad
\operatorname{ad}_E^2\partial_w=0.
\]
In the intended application \(g\) is nonconstant, the two original
quadratic defects have rank two, and their joint rank with \(E\)
is also two. The coordinate \(w\) is genuine.
The possible extra conditions are
\[
Ew=\rho g,\qquad \rho\in\mathbb C,
\quad\text{or}\quad
E^2w=\lambda g^2,\qquad \lambda\in\mathbb C.
\tag{1}
\]

If \(\rho\ne0\), then \(w\) is an original coordinate local
slice, but \(w/(\rho g)\) is a slice only in \(B_g\).
If \(\lambda\ne0\), then \(w\) is not a local slice:
\(Ew\) is a local slice, since \(E(Ew)=\lambda g^2\) and
\(E^2(Ew)=0\). The polynomial \(Ew\) has not been proved
to be an ambient coordinate.
If \(\lambda=0\), one knows \(E^2w=0\), not automatically
that \(Ew\) is zero or proportional to \(g\).

The cases \(Ew=0\) and \(Ew\in\mathbb C^*\) are already
recognized: they give respectively an invariant coordinate
and an original coordinate slice. They are not the remaining
nonconstant-factor case.

## 2. Three exact primary comparisons

### Daigle: a coordinate local slice in three variables

Daniel Daigle's *Triangular derivations of \(k[X,Y,Z]\)*,
Theorem 5.1, assumes an irreducible LND of an actual
three-variable polynomial ring over a characteristic-zero field.
If an actual variable \(Y\) satisfies \(DY\ne0\) and
\(D^2Y=0\), then there are coordinates \(X,Y,Z\) with
\(DX=0\), \(DY\in k[X]\), and \(DZ\in k[X,Y]\).
Corollary 5.2 characterizes triangularity by this coordinate
local-slice condition for irreducible derivations.[^daigle]

The original slice makes our \(E\) irreducible, and the
\(\rho\ne0\) case has the stated coordinate local slice.
The missing premise is the actual polynomial three-ring.
The original \(B\) has four variables. Its kernel is the
unknown threefold, while \(B_g\) is only an invariant localization.
Neither is licensed as \(k^{[3]}\) by this theorem.
The good-partial and joint-rank assumptions do not appear in
the theorem and do not replace its dimension hypothesis.

For \(\lambda\ne0\), even the coordinate local-slice premise
is missing for the proposed coordinate \(w\).
The source's proof uses birational morphisms of surfaces,
so it is not a formal all-dimension local-slice argument.

### Derksen, van den Essen and van Rossum: a fixed relative base

Theorem 4.4 of *The Cancellation Problem in Dimension Four*
recognizes a sliced \(R\)-LND of the actual ring \(R^{[3]}\),
where \(R\) is a Dedekind domain containing \(\mathbb Q\).
Corollary 4.5 treats a sliced LND of \(k[X,Y,Z,W]\) whose
\(W\)-coefficient belongs to \(k[W]\). Its proof splits into
a fixed \(W\) and a nonzero constant \(DW\).[^derksen]

For \(Ew=\rho g\) with \(\rho\ne0\) and nonconstant \(g\),
the hypothesis \(Ew\in\mathbb C[w]\) is not supplied.
Indeed if it held, invariance of \(Ew\) would give
\((Ew)'(w)Ew=0\), forcing \(Ew\) to be constant.
For \(\lambda\ne0\), an LND with \(Ew\in\mathbb C[w]\)
would again have \(Ew\) constant, contrary to
\(E^2w=\lambda g^2\ne0\).
Thus the corollary does not cover the retained nonzero cases.

Taking \(R=\mathbb C(w)\) does not help: \(Ew\ne0\), so
\(E\) is not an \(R\)-derivation. Taking \(R=\mathbb C[g]\)
does give a fixed base, but the actual presentation
\(B=\mathbb C[g]^{[3]}\) has not been proved.
The good coordinate is \(w\), not \(g\).

### Bhatwadekar, Gupta and Lokhande: an invariant coordinate

Theorem 3.5 assumes a nonzero \(k[T]\)-linear LND of the
actual four-ring \(k[T,X,Y,Z]\), with regular kernel.
It concludes that this kernel is \(k[T]^{[2]}\).
Its displayed proof localizes over the fixed polynomial
coordinate base \(k[T]\).[^bgl]

The original slice supplies regularity in our problem.
For the remaining nonzero cases, it does not supply a
fixed ambient coordinate \(T\). A coordinate merely having
first or second flow derivative as in (1) is not that input.
An invariant polynomial \(g\) is not automatically a coordinate.

## 3. What the good-partial identity actually adds here

Let \(P=Ew\), \(F=E^2w\), and \(W=[E,\partial_w]\).
The good-partial identity is \([E,W]=0\).
Applying it to \(w\) and using
\(E\partial_w-\partial_wE=W\) gives
\[
2WP=-\partial_wF.
\tag{2}
\]
If \(P=\rho g\) with \(\rho\ne0\), then \(F=0\),
so \(Wg=0\).
If \(F=\lambda g^2\) with \(\lambda\ne0\), equation (2)
gives \(WP=-\lambda g\,\partial_wg\). Applying \(E\)
to this equality gives
\[
2\lambda g\,Wg=-\lambda g\,Wg,
\]
and again \(Wg=0\). Consequently
\(E(\partial_wg)=Wg=0\) in both nonzero alternatives.

These identities do not show \(Ew=0\), make \(E\)
\(\mathbb C(w)\)-linear, or produce a polynomial
three-variable quotient. In the actual moving-top setting,
\(Wg=0\) is already part of the highest good-column
identity in [pass42](two-quadratic-top-line-pass42.md),
Section 5. This calculation is a compatibility check,
not a new recognition mechanism.

For a simple boundary to the slice confusion, the actual
polynomial action
\[
E=\partial_s+a\partial_w
\quad\text{on}\quad \mathbb C[a,s,w,z]
\tag{3}
\]
has original slice \(s\), good coordinate partial
\(\partial_w\), and \(Ew=a\). The coordinate \(w\)
is a local slice but not an original slice.
Its kernel is explicitly \(\mathbb C[a,z,w-as]\).
This has zero quadratic defects, not the independent
rank-two defect profile; it only tests the claimed distinction.

## 4. Research consequence and reading limits

None of these three statements closes the terminal quintic
from (1) and the good-partial condition alone.
A usable next input would be an actual invariant coordinate,
an actual relative polynomial presentation over an invariant
coordinate, or the already proved rational two-direction
symmetry with its good output partial.
The present low-flow coordinate condition is not substituted
for any of those premises.

The retained recognition and local-slice notes were searched
first. The Bhatwadekar--Gupta--Lokhande statement and full
displayed proof were reread in the retained primary text.
The Derksen--van den Essen--van Rossum Theorem 4.4 and
Corollary 4.5, with their displayed proofs, were read in
the author-uploaded manuscript text; their earlier patching
dependencies are not claimed as a fresh full source audit.

The indexed author PDF provided Daigle's exact Theorem 5.1,
its proof paragraph and the three-variable context, and the
publisher page confirmed the article metadata. Direct PDF
retrieval failed in both the browser and shell. Accordingly,
no fresh complete read of its Section 4 dependencies or full
paper is claimed. No secondary summary was used as the
substitute theorem statement.

This bounded check adds no numerical method, recognition
theorem, full regression, metadata change, historical novelty
claim or external contact. Frozen pass71 files are unchanged.

[^daigle]: Daniel Daigle, [*Triangular derivations of \(k[X,Y,Z]\)*, author manuscript](https://aix1.uottawa.ca/~ddaigle/articles/preslice.pdf), Section 5, Theorem 5.1 and Corollary 5.2; [publisher record](https://doi.org/10.1016/j.jpaa.2009.10.004), *Journal of Pure and Applied Algebra* 214 (2010), 1173--1180. The direct-retrieval limitation is recorded above.

[^derksen]: Harm Derksen, Arno van den Essen and Peter van Rossum, [*The Cancellation Problem in Dimension Four*, author-uploaded manuscript](https://www.researchgate.net/publication/228571174_The_cancellation_problem_in_dimension_four), Nijmegen Report 0022, October 2000, Theorem 4.4 and Corollary 4.5. The exact relative-base scope was already retained in [the pass64 source comparison](graph-recognition-literature-scope-pass64.md).

[^bgl]: S. M. Bhatwadekar, Neena Gupta and Swapnil A. Lokhande, [*Some K-theoretic properties of the kernel of a locally nilpotent derivation on \(k[X_1,\ldots,X_4]\)*](https://arxiv.org/pdf/1501.01438v1), Theorem 3.5 and its proof, PDF p. 11. Retained primary text: [bgl-1501.01438v1.txt](../tmp/pdfs/bgl-1501.01438v1.txt).
