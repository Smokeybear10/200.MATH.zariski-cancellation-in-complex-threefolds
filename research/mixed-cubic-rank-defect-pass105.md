# The actual mixed fiber has a third-degree module image defect

In the actual collapsed mixed quadratic sector with nonzero speed
normal, the image of the rank-four third-degree module has
dimension at most three. Every element of that module is constant
on each reduced component. This conclusion uses the new actual
normalization boundary, not the invalid claim that an affine
nilpotent coefficient alone limits the image to dimension three.

## 1. Exact inputs and the boundary divisor

Retain all the actual hypotheses of
[third-degree image105](mixed-third-degree-image-pass105.md).
Write R=S_m and F_j=ker N^(j+1), and let W_j denote the image
of F_j in the whole fiber. In particular
\[
\begin{gathered}
S=\ker(N|_A)=\mathbb C[s_1,s_2],\quad A_K=K[v],\quad
N|_{A_K}=\lambda_K\partial_v,\quad\lambda_K\ne0,\\
(F_j)_R\simeq R^{j+1},\qquad
A/\mathfrak mA=\mathcal D[c],\qquad
\mathcal D=\mathbb C[G]/(G^2(G-1)),\\
c\in F_4,\quad \deg_Nc=4,\qquad
\dim\mathcal W_2\in\{2,3\},\\
\text{there is an irreducible }p\in\mathfrak m\subset S
\text{ with }\quad
A_{S\setminus(p)}/pA_{S\setminus(p)}=k_p[w],\quad
\bar N\ne0,\quad \deg_w\bar c=3.
\end{gathered}
\tag{1}
\]
The last line is the complete conclusion of
[normalization-boundary105, Section 7](mixed-c-parameter-normalization-boundary-pass105.md).
Here k_p is Frac(S/(p)); it is the full residue constant field,
not a proper subfield of an unrecorded extension. This is a
height-one divisor of the actual invariant plane, lying through
the specified closed base point. The proof below needs that
precise boundary statement, including degree one for its constants.

## 2. An elementary slice lift over that DVR

Put V=S_(p) and B_p=A_(S minus (p)). These are base localizations;
V is a DVR with uniformizer p and residue field k_p. The full
kernel of N on B_p is V. By (1), its reduced closed fiber is
k_p[w]. A nonzero locally nilpotent derivation of a polynomial
line over a characteristic-zero field is a nonzero constant
multiple of its coordinate partial, so its kernel is k_p.

Choose any local slice t in B_p: start with an element of positive
N-degree and apply N until its derivative is a nonzero invariant.
After multiplying t by an invariant unit, one has Nt=p^e for an
integer e at least zero. If e is positive, the residue of t
belongs to ker(bar N)=k_p. Lift this residue to a in V. Then
\[
t_1=(t-a)/p\in B_p,\qquad Nt_1=p^{e-1}.
\quad\Longrightarrow\quad
\boxed{\ B_p=V[t_*],\quad Nt_*=1.\ }
\tag{2}
\]
The membership uses the actual quotient by pB_p, not a fractional
or completed ring. Repeating the same step finitely many times
produces t_*; the slice theorem gives the displayed polynomial
presentation. Equivalently its usual finite Taylor projection
has image V and supplies that presentation directly.

It follows, for each positive j, that the image of N^j on
ker N^(j+1) over this DVR is all of V: the element t_*^j/j!
has j-th derivative one. This division argument would fail if
the residue constants were k'_p properly larger than k_p,
because its invariant residue need not lift from V. No general
fiberwise injectivity of a degree module was used.

## 3. Full third-degree image would make the wrong fourth image

Suppose for contradiction that dim W_3 is four. The residue
of c is independent of W_3. Indeed every third-degree residue
has affine reduced values whose slope vector lies in one fixed
coordinate axis, by third-degree105 (2). The slope vector of
c is (1,1). It cannot belong to that axis, including when all
third-degree slopes are zero. Thus rank and Nakayama give
\[
\begin{gathered}
(F_4)_R=(F_3)_R\oplus Rc,\\
I_4:=N^4((F_4)_R)=R\,N^4c,\qquad
I_4\otimes_R V=V\,N^4c.
\end{gathered}
\tag{3}
\]
More explicitly, choose four actual elements with independent
whole-fiber residues. They are a basis of (F_3)_R; adjoining c
gives five independent residues and a basis of the rank-five
module (F_4)_R. Applying N four times kills the first summand.
Localization at p commutes with these kernels and images since
every inverted base element is invariant. Therefore the last
line is exactly the fourth derivative-image ideal on B_p.

By (1), bar c has degree three on k_p[w], where bar N is a
nonzero translation. Its fourth derivative is zero. Consequently
N^4c belongs to pB_p, and, being invariant, belongs to pV.
The latter contraction also follows directly from the injective
residue map V/pV into B_p/pB_p. Equation (3) therefore makes
I_4 tensor V a proper ideal. Equation (2), applied to t_*^4/24,
makes it the unit ideal. This is the required contradiction.

## 4. Exact residue consequences and limits

The degree-module rank already bounds dim W_3 by four, so
\[
\boxed{\begin{gathered}
\dim\mathcal W_3\le3,\\
\bar U|_{C_2},\ \bar U|_{C_1}\in\mathbb C
\quad\text{for every }U\in F_3,\\
\mathcal W_2=\mathcal D\quad\Longrightarrow\quad
\mathcal W_3=\mathcal D.
\end{gathered}}
\tag{4}
\]
For the second line, when W_2 has dimension two, third-degree105
(3) already proves both slopes zero. When W_2 has dimension
three it equals D, which is contained in W_3; the new bound
forces equality. Nilpotent coefficients can still be nonconstant
in the dimension-two W_2 branch. The proof does not eliminate
that possibility or make every third-degree element invariant.

The earlier rank-four conditional computations remain valid:
D plus C epsilon c really has dimension four, and the conormal
coefficient argument alone does not exclude it. It is now excluded
by the independent actual boundary divisor and DVR slice lift.
Thus no correction to the affine-coefficient dimension count is
being used as a substitute for this new argument.

This proves a genuine image defect for F_3 at the mixed fiber,
not a contradiction to its finite freeness over the base. It
does not supply a cubic presentation, exclude the mixed fiber,
prove a global N-slice, or recognize A. The argument assumes the
supplied original frame throughout its boundary input and does
not solve the entry problem for arbitrary sliced actions.

The complete saved boundary105 and third-degree105 arguments
were read before this deduction. The DVR slice-lift is an
elementary finite division argument; no new external theorem or
numerical method is added. No file through104 is changed.
