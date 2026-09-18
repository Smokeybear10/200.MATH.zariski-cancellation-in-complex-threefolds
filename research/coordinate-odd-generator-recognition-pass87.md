# A coordinate odd generator is exactly a linearization gate for these fibers

In the constant-acceleration fiber setting, the free odd-module
generator is a polynomial coordinate if and only if the fiber
involution is linearizable. The forward implication uses the
established affine-plane-fibration theorem over a characteristic-zero
PID. Thus coordinate status would suffice, but this is an equivalent
form of the missing linearization premise, not a consequence of the
odd module being principal.

## 1. Exact conditional statement

Fix one of the actual coordinate fibers in the
[constant-acceleration reduction](constant-acceleration-involution-boundary-pass87.md).
Write C for its ring and retain the specified odd generator u:
\[
\begin{gathered}
C\simeq\mathbb C^{[3]},\qquad A=C^\iota,\qquad C=A\oplus Au,
\qquad\iota(u)=-u,\qquad t:=u^2\in A,\\
u\text{ is a polynomial coordinate of }C
\quad\Longleftrightarrow\quad
\iota\text{ is algebraically linearizable}.
\end{gathered}
\tag{1}
\]
Here A is the injected original kernel, a finitely generated domain.
The fixed scheme of iota is nonempty, smooth, and two-dimensional.
Those facts were proved in the cited reduction. The implication
toward linearizability below only needs the displayed quadratic
module presentation and finite generation; the fixed-scheme dimension
identifies the linear representation in the converse.

Because u is a nonzero odd element, it is nonconstant. A polynomial
relation over \(\mathbb C\) would make u constant, so u and t are
transcendental over \(\mathbb C\). In particular \(R=\mathbb C[t]\) is an actual polynomial
subring of A.

## 2. A coordinate u gives all actual plane fibers, including the branch fiber

Assume that there are actual polynomial coordinates u,X,Y of C.
The direct sum in (1) gives the full ring presentation
\[
C=A[U]/(U^2-t)
 \simeq A\otimes_{\mathbb C[t]}\mathbb C[u]
 =\mathbb C[u,X,Y],
\tag{2}
\]
where the map from \(\mathbb C[t]\) to \(\mathbb C[u]\) sends t to
u squared. No claim of etaleness at u=0 is used.

For each complex number c choose a complex alpha with alpha squared
equal to c. Eliminating U in (2) gives
\[
A/(t-c)A\simeq C/(u-\alpha)C\simeq\mathbb C^{[2]}.
\tag{3}
\]
This proves the whole fiber-ring identity also for c=0, not merely
the identity after taking radicals. In parity terms, the branch
contraction is \(A\cap uC=u^2A\); averaging lifts every class of
C/(u), giving the same isomorphism at zero.

A is finitely generated as an R-algebra since it is finitely
generated over \(\mathbb C\). It is torsion-free over the PID R, hence flat.
It remains to check the generic fiber over its actual residue field,
rather than merely geometric fibers.

Set \(K=\mathbb C(t)\) and \(K'=K(\alpha)\), where
\(\alpha^2=t\). This is a separable algebraic extension in
characteristic zero. Base-changing (2) and then setting u=alpha gives
\[
(A\otimes_R K)\otimes_K K'
 \simeq C\otimes_{\mathbb C[u]}K'
 \simeq K'[X,Y].
\tag{4}
\]
Kambayashi's separable affine-plane-form theorem therefore gives
\(A\otimes_R K\simeq K^{[2]}\). Together with (3), finite generation
and flatness, this proves that A is an affine-plane fibration over R:
every prime-residue-field fiber is a polynomial plane.

## 3. Exact source inputs and global conclusion

The field theorem used in (4) says that a k-algebra D satisfying
\(D\otimes_k L=L^{[2]}\) for a separably algebraic field extension
L/k is \(k^{[2]}\). The original is Kambayashi,
[*On the absence of nontrivial separable forms of the affine plane*](https://doi.org/10.1016/0021-8693(75)90058-7),
Journal of Algebra 35 (1975), 449--456, Theorem 3. Its exact statement
was freshly read as Theorem 2.8 in the primary research paper
[Dutta--Gupta--Lahiri, *On Separable A2 and A3-forms*](https://arxiv.org/pdf/1802.03777v2),
printed page 2. No fresh read of Kambayashi's original proof is claimed.

The second input is the established result that an affine-plane
fibration over a PID containing Q is a polynomial algebra over that
PID. Sathaye's DVR theorem and Bass--Connell--Wright globalization give
this implication. It is stated explicitly in the paragraph before
Theorem 4.7, printed page 9, of
[Babu--Das, *Structure of A2-fibrations having fixed point free locally nilpotent derivations*](https://arxiv.org/pdf/2001.07632v5).
That paragraph and the definition of affine-space fibration were
freshly read. The argument here uses this PID result, not their
additional theorems assuming a fixed-point-free relative LND.
No new original Sathaye or Bass--Connell--Wright proof audit is claimed.

Applying this input to the actual R-algebra established in Section 2
produces invariant elements p and q with
\[
A=\mathbb C[t,p,q],\qquad
C=\mathbb C[u,p,q],\qquad
\iota(u,p,q)=(-u,p,q).
\tag{5}
\]
Indeed (2) eliminates t from the polynomial presentation
\(\mathbb C[t,p,q,U]/(U^2-t)\). This is an actual global coordinate
completion, not descent of generic coordinates without the fibration
theorem. In particular \(A\simeq\mathbb C^{[3]}\).

## 4. Converse and precise limitation

If iota is linearizable, its two-dimensional fixed scheme makes it a
reflection. In suitable actual coordinates p,q,v of C, it fixes p,q
and sends v to -v. Thus \(A=\mathbb C[p,q,v^2]\), and its odd summand
is Av. Since the originally supplied u also generates that summand,
u=fv and v=gu for some f,g in A. The domain identity fg=1 makes f
a unit of A, hence a nonzero complex constant. Therefore u itself
is a polynomial coordinate. This proves the converse in (1).

No implication from the principal module Au or its unimodular odd
coefficient row to coordinate status is established here. The
[fiber-row control](constant-acceleration-fiber-row-pass87.md) even has
a coordinate u and is linearizable, while its standard Reynolds map
is not invertible. Coordinate recognition, linearization, and the
behavior of a specified averaging map must remain distinct.

The fibration input is retained elsewhere in the project, including
[the rank-two action note, Section 6](rank-two-action-pass.md).
The new point here is the exact odd-generator application, particularly
the branch-fiber identity (3) and generic separable splitting (4).
This is a conditional recognition lemma with an equivalent hypothesis,
not a proof of that hypothesis for arbitrary fibers, a new general
cancellation theorem, or a novelty claim. It adds no checker or
numerical method and changes no file through pass86.
