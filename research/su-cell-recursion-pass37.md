# Independent recursions for the selected Su braid cell

## 1. Conclusion and source conventions

Work over an algebraically closed field \(k\) of characteristic zero,
with the very generic regular semisimple monodromies of the
\((g,k_{\mathrm{punct}},n)=(0,6,2)\) source setup.
For the selected chronological walk
\[
(1,s,s,s,1,s,1,s,1,s,1)
\]
of \(\sigma_1^{10}\), the actual four-coordinate additive action is
\[
(a,b,c,d)\longmapsto(a-t,b-t,c-t,d-t).
\]
Its quotient is therefore \(\mathbb A^3\), with coordinates
\(b-a,c-a,d-a\). The full source-identification proof is in
[the selected-cell note](su-selected-cell-pass37.md).

Mellit already states that rank-two cancellation can be performed
compatibly with the character-variety stratification. The present
calculation is an explicit reconstruction in Su's coordinates,
not a new rank-two cancellation result.[^2]

The recursions below use Su's \(B(e)=sH(e)\), chronological left
multiplication, Appendix A's primed coordinates, and Definition 1.14's
action. Lemma 2.5 identifies that action with the character-cell action;
the extra factors vanish for the selected five indices \(w_i=s\).
Theorem 2.10 takes the quotient of a fixed torus fiber. These are
source inputs, not consequences of an arbitrary matrix parametrization.[^1]

## 2. Direct matrix derivation

Put
\[
H(e)=\begin{pmatrix}1&e\\0&1\end{pmatrix},\qquad
B(e)=\begin{pmatrix}0&1\\1&e\end{pmatrix},\qquad
P_j=B(e_j)\cdots B(e_1).
\]
For a previous matrix \(P=\left(\begin{smallmatrix}A&B_0\\C&D\end{smallmatrix}\right)\),
\[
B(e)P=
\begin{pmatrix}C&D\\A+eC&B_0+eD\end{pmatrix}.                       \tag{1}
\]
Since \(\det P_j=(-1)^j\), every prefix is invertible. Its Bruhat
state is \(1\) exactly when its lower-left entry is zero.

Start with raw up parameters \(A_1,A_5,A_7,A_9\), and set
\[
r=e_2\ne0,\qquad q=1+r e_3\ne0.
\]
The down-steps force
\[
(e_1,\ldots,e_{10})=
\left(A_1,r,\frac{q-1}{r},-\frac rq,A_5,0,A_7,0,A_9,0\right).
                                                                    \tag{2}
\]
For example, the lower-left entry after step three is \(q\);
the next entry is \(r+e_4q\), forcing \(e_4=-r/q\).
After that, every up/down pair starts from an upper matrix with
diagonal \((q,q^{-1})\), and its down-coordinate is zero. Thus (2)
is both necessary and sufficient for this walk.

To recover the source coordinates independently, use
\[
e'=\frac{De+B_0}{A}\quad(C=0),\qquad
e'=-\frac{C^2}{\det P}\left(e+\frac AC\right)\quad(C\ne0).
                                                                    \tag{3}
\]
The second formula follows from the exact factorization
\[
P=H(A/C)\,s\,\operatorname{diag}(C,-\det(P)/C)\,H(D/C).
\]
Formula (3) also recovers zero at each down-step. For the stay
positions it gives
\[
e'_2=r,\qquad e'_3=-rq.
\]
For the up positions it gives
\[
\begin{aligned}
a&=A_1,\\
b&=A_1+\frac{q-1}{rq}+\frac{A_5}{q^2},\\
c&=A_1+\frac{q-1}{rq}+\frac{A_5+A_7}{q^2},\\
d&=A_1+\frac{q-1}{rq}+\frac{A_5+A_7+A_9}{q^2}.
\end{aligned}                                                       \tag{4}
\]
Consequently the complete forward map in normalized coordinates is
\[
\begin{aligned}
(e_1,\ldots,e_{10})=
\bigg(&a,r,\frac{q-1}{r},-\frac rq,\,
q^2(b-a)-\frac{q(q-1)}r,0,\\
&q^2(c-b),0,q^2(d-c),0\bigg).
\end{aligned}                                                       \tag{5}
\]
Equations (4) and (5) are inverse regular maps over
\(k[r^{\pm1},q^{\pm1}]\). No denominator other than the specified
invertible stay parameters is used.

Let \(V=qa+(q-1)/r\). The nontrivial prefix checks simplify to
\[
\begin{aligned}
P_3&=\begin{pmatrix}r&1+ra\\q&V\end{pmatrix},&
P_4&=\begin{pmatrix}q&V\\0&q^{-1}\end{pmatrix},\\
P_5&=\begin{pmatrix}0&q^{-1}\\q&qb\end{pmatrix},&
P_6&=\begin{pmatrix}q&qb\\0&q^{-1}\end{pmatrix},\\
P_7&=\begin{pmatrix}0&q^{-1}\\q&qc\end{pmatrix},&
P_8&=\begin{pmatrix}q&qc\\0&q^{-1}\end{pmatrix},\\
P_9&=\begin{pmatrix}0&q^{-1}\\q&qd\end{pmatrix},&
P_{10}&=\begin{pmatrix}q&qd\\0&q^{-1}\end{pmatrix}.
\end{aligned}                                                       \tag{6}
\]
The lower-left entries are
\[
(0,1,r,q,0,q,0,q,0,q,0),
\]
including \(P_0\). They verify the complete walk, not only the
terminal upper-triangular condition.

## 3. Monodromy and the actual action

Write the monodromies as
\(C_i=\operatorname{diag}(c_{i,1},c_{i,2})\). In this genus-zero,
all-\(s\) case the source's fixed diagonal is
\[
D^0=\left(\prod_{i=1}^5 C_i^s\right)C_6
=\operatorname{diag}(\kappa,\kappa^{-1}),\qquad
\kappa=c_{6,1}\prod_{i=1}^5c_{i,2}.
\]
The determinant condition gives the second entry. The restriction
is exactly \(q=\kappa^{-1}\). The normalized second stay is
\(-\kappa^{-1}r\), so \(r\) remains a free torus coordinate.
Equation (6) then gives \(D^0P_{10}=H(d)\); the eliminated source
variable is \(u^0=H(-d)\). There is no equation \(d=0\).

The action identity
\[
B(e_1)H(-t)=B(e_1-t)                                                \tag{7}
\]
is an elementary absorption of adjacent upper-unipotent factors
at the first crossing. It leaves no residual factor, hence all
later raw \(e_j\) are fixed. Using (4), all four normalized up
coordinates shift by \(-t\), while the stay coordinates remain fixed.

For a torus element with ratio \(\rho=t_1/t_2\), pushing it through
the same matrices gives alternating raw weights. In normalized
coordinates this is
\[
(r,q;a,b,c,d)\longmapsto
(\rho^{-1}r,q;\rho a,\rho b,\rho c,\rho d).                           \tag{8}
\]
Taking the \(U\)-invariant torus fiber \(r=1\) gives the actual
affine prequotient. Its coordinate change
\[
(a,b,c,d)\longmapsto(b-a,c-a,d-a,-a)
\]
has inverse
\[
(X,Y,Z,\tau)\longmapsto(-\tau,X-\tau,Y-\tau,Z-\tau).
                                                                    \tag{9}
\]
Under the action, only \(\tau\) changes, by \(\tau\mapsto\tau+t\).
Thus the entire invariant ring, not merely a polynomial subring,
is \(k[X,Y,Z]\).

For the full projective-Borel quotient before fixing \(r\), the
global invariant coordinates are
\[
r(b-a),\qquad r(c-a),\qquad r(d-a).
\]
The sequence \(U(t=a)\), then \(T(\rho=r)\), puts every point into
the unique section \(a=0,r=1\). This is a second explicit
recognition of the same selected character cell.

## 4. Independent finite controls and proof audit

The standalone
[exact checker](su_cell_checks_pass37.py)
has eight methods. It uses only unittest and SymPy, with no
project or solver imports. Its parameter-recovery routine computes
(3) from the successive actual matrices; it does not call the
claimed forward parametrization to manufacture expected coordinates.

The methods check every prefix and determinant, both coordinate
maps, the independent stay-factor monodromy formula, elementary
unipotent absorption, torus propagation, both quotient/cylinder
maps, the full projective-Borel section, and an explicit very
generic diagonal example. The first run passed all eight methods
in 0.198 seconds with exit status zero. A separate full-file review
and rerun passed the same eight methods in 0.202 seconds.

A full independent read of
[the selected-cell proof](su-selected-cell-pass37.md)
found no mathematical or scope correction. In particular, the
source action identification, fixed monodromy, removal of extra
factors, and distinction between raw and normalized parameters
all agree with the matrix reconstruction here.

These finite controls do not machine-check the source's geometric
identification, prove a statement about the other cell indices, or
solve the general cancellation problem. No expert-review or Lean
verification claim is made.

## Sources

[^1]: Tao Su, *Cell decomposition and dual boundary complexes of
    character varieties*, [arXiv:2307.16657v4](https://arxiv.org/pdf/2307.16657v4),
    30 August 2024. Definitions 1.12 and 1.14, Proposition 1.16,
    equations (2.1.3), (2.2.5), (2.3.6), Lemma 2.5, Proposition 2.9,
    Theorem 2.10, and Appendix A. Matrix order and the action
    convention were also checked directly on manuscript pages 11
    and 32.

[^2]: Anton Mellit, *Toric stratifications of character varieties*,
    [published article](https://link.springer.com/content/pdf/10.1007/s10240-025-00158-0.pdf),
    2025, Section 1.4, journal page 160, PDF page 8. The statement
    explicitly includes all rank-two cases of the source construction;
    it is not a general affine cancellation theorem.
