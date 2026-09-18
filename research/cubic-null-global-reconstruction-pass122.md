# Global reconstruction and finite-place residues for the null cubic axis

In the actual null cubic branch, the degree-three relative element is
already global, not merely defined after inverting the velocity
determinant. The coefficient a in rho=aY+B satisfies aY squared in S.
Moreover that polynomial has complex-constant residue along every
irreducible divisor of Y, even if the coefficient field is a proper
finite extension of C(h).

These statements use the actual original coordinates and their full
invariant kernel. They supply the reconstruction and residue ingredients
for the original-coordinate divisibility argument; no constant relative
Jacobian, global generic-parameter normalization or polynomial first
integral is assumed.

## 1. Retained actual cubic data

Retain the full original-coordinate framework90 and the surviving null
cubic alternative of [the scalar classification121](cubic-null-axis-scalar-constraint-pass121.md).
Use a for the coefficient of rho, and reserve A for the actual kernel
ring. The relevant identities are
\[
\begin{gathered}
B_{\mathrm{amb}}=\mathbb C[x_1,x_2,x_3,z]=A[u],\qquad
A=\ker E,\quad Eu=1,\quad \ker(N|A)=S=\mathbb C[s,t],\\
K=\operatorname{Frac}S,\qquad L/\mathbb C(h)\text{ finite},
\quad a\in L,\quad B_0\in\mathbb C,\quad
\rho=aY+B_0/Y,\\
b=(g,P,Y)^t\in S^3,\quad Y\ne0,\quad h=P/Y,\quad
D=a_3h^3+a_2h^2+a_1h+a_0,\quad a_i\in\mathbb C,\quad a_3\ne0,\\
2gY+DY^2=-1,\qquad
x_{\rm tr}=b(u+\rho)+b_hv+b_YR,\qquad
v,R\in A_K,\quad \deg_vR=3 .
\end{gathered}
\tag{1}
\]
The derivatives in the last line are the commuting rational derivatives
from121, with h derivative extended through L and with Y fixed.
Here Y is the third actual polynomial speed and P the second, not new
independent polynomial coordinates on S. The polynomial speed identities
and nonzero original moving-frame determinant are retained throughout.

## 2. Recover both relative elements from the original good coordinates

The last two rows of the reconstruction in (1) give
x2=h x3+Yv and x3=Y(u+rho)+R. The first velocity entry is
g=-(1+DY squared)/(2Y). Thus g_h=-D'Y/2 and
g_Y-g/Y=1/Y squared. Substituting the last coordinate into the first
therefore gives
\[
\begin{gathered}
U:=Yx_2-Px_3=Y^2v\in A,\\
2R=2Y^2x_1+D'Y^2x_2+
          \bigl[1+(D-hD')Y^2\bigr]x_3 .
\end{gathered}
\tag{2}
\]
The membership assertion for U follows from its displayed polynomial
formula and E(U)=YP-PY=0. At this stage the second line is an identity
in the actual fraction field; its coefficients will now be proved
polynomial rather than silently divided in the base ring.

The speed identity in (1) gives
a3 P cubed/Y=-1-2gY-a2 P squared-a1 PY-a0 Y squared, an element of S.
Use this to eliminate the only denominator in (2). The result is
\[
\begin{gathered}
2R=2Y^2x_1+
       (3a_3P^2+2a_2PY+a_1Y^2)x_2\\
\hspace{22mm}+
       (3+4gY+a_2P^2+2a_1PY+3a_0Y^2)x_3,
\qquad R\in A,\\
2R\equiv3x_3\pmod{pB_{\mathrm{amb}}}
\quad\text{whenever }p\mid Y\text{ and }p\mid P .
\end{gathered}
\tag{3}
\]
Every coefficient in the first two lines belongs to S. The displayed
row makes R a member of the original polynomial four-ring; it was
already E-invariant in the fraction field by (1), so R belongs to A.
The last line is just reduction of this exact polynomial row. It does
not rely on a generic parameter being globally polynomial.

The third original coordinate now yields a further global contraction:
\[
F_0:=aY^2=x_3-Yu-R-B_0\in A\cap K=S .
\tag{4}
\]
Indeed x3-Yu and R are actual members of A, while aY squared lies
in K. An element of A intersect K is killed by N, since N kills K;
the full actual kernel is S. This proves the equality used in (4).
It would not be valid to infer it for an arbitrary rational coefficient
tuple lacking those actual invariant-ring hypotheses.

## 3. An elementary finite-place residue lemma

Let L be any finite extension of C(h), and let nu be a discrete
valuation on a containing field, trivial on C, with nu(h)<0.
The residue of every element of L regular for nu belongs to C.

Here is a direct proof requiring no choice of a rational generator of L.
For a regular element alpha in L, choose a nonzero polynomial relation
sum c_i(h) alpha to the power i=0 over C(h). Divide all its coefficients
by one having minimal nu value. Every normalized coefficient is regular,
and at least one is one. A rational function of h regular at this
valuation has complex residue: write it using 1/h, which has positive
valuation, and take its value at zero after cancellation. Reduction
therefore gives a nonzero polynomial over C satisfied by the residue
of alpha. That residue is algebraic over the algebraically closed field
C, hence belongs to C. The nonzero reduced polynomial follows from
the normalized coefficient equal to one; possible vanishing of its
leading coefficient does not affect this argument.

## 4. Apply the lemma at an actual divisor of Y

If Y were a nonzero complex constant, the speed identity would express
g as a polynomial in P. All three velocities would then have
differential rank at most one, contrary to the actual nonzero moving
frame determinant. Thus Y is nonconstant and has an irreducible divisor
p in S. The same argument applies to every such divisor.

Clearing the speed identity shows p divides P. Put
K0=P cubed/Y, which belongs to S by Section2. Reduction gives
K0 congruent to -1/a3 modulo p, so K0 is a unit in S_(p).
Taking p-valuations in P cubed=Y K0 now gives
\[
\begin{gathered}
K_0=P^3/Y\in S,\quad \overline{K_0}=-1/a_3,\quad
\nu_p(Y)=3\nu_p(P)>0,\quad
\nu_p(h)=-2\nu_p(P)<0,\\
\frac{a}{h^3}=\frac{F_0}{K_0}\in L\cap S_{(p)},\qquad
\overline{F_0}\in\mathbb C\subseteq\operatorname{Frac}(S/(p)) .
\end{gathered}
\tag{5}
\]
The residue lemma applies to a/h cubed, not to a itself, which can
have a pole. Its residue is complex. Multiplication by the complex
nonzero residue of K0 gives the final assertion. Since F0 belongs to S,
it follows that F0 differs from that same complex constant by a member
of pS, not merely after a further localization. This uses the injection
S/(p) into its fraction field.

Thus the original-coordinate row (3), contraction (4), and finite-place
assertion (5) are global statements with controlled residues. No
derivative-growth estimates for a, no conditions on the lower cubic
coefficients, and no equality L=C(h) were used.

## Verification and scope

[The one-method checker122](cubic_null_reconstruction_checks_pass122.py)
checks the reconstructed original-coordinate row and its polynomial
absorption, retaining the full speed-relation error in the certificates.
It also checks the row's reduction and the nonzero residue of K0.
The full invariant-kernel contraction, the residue lemma
for every finite field extension, and the use of original coordinates
are written arguments, not properties certified by coefficient tests.
In particular the relative Jacobian remains a base-field unit with
J times N(v)=1 as in121; it has not been assumed to be a complex
constant. Files through121 remain unchanged.

The author ran the method once in execution `a9571c`: it passed in
0.076 seconds of unittest time and 0.256424959 seconds of command
wall time, exit zero. The complete saved proof read was `a15f68`,
with its valuation-hypothesis precision read in `af7bef`.
The complete code read and hash/AST/whitespace check were `4fc317`.
These finite identities do not add a test of the arbitrary finite-place
or original-coordinate arguments.
