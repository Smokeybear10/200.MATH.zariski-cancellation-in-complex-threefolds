# A coefficient-gradient obstruction to every fixed-axis three-stage placement

A normalized canonical tail cannot have three successive nonlinear
stages in the fixed formal axes described below. A single coefficient
derivative identity already contradicts polynomial degree in the
middle residual variable. The obstruction holds for arbitrary stage
degrees at least two, not only the quadratic degree-eight pattern.

The algebraic argument is over a differential field and does not need
an original-ring inverse. Applying it to an actual dense frame does
need the retained canonical parameter and degree statements that
produce its precise second-tail hypothesis. This note does not assert
that arbitrary nongraphs admit the three-stage placement.

## 1. The differential-field statement

Let \(L\) be a field of characteristic zero with a derivation
\(\delta:L\to L\). Extend \(\delta\) to \(L[U,V]\) by fixing
the independent variables \(U,V\). Let
\[
\begin{gathered}
\mathcal A\in L[U],\quad \deg\mathcal A=r\ge2,
\quad a_r=[U^r]\mathcal A\ne0,\\
\mathcal B\in L[T],\quad \deg\mathcal B=q\ge2,
\quad b_q=[T^q]\mathcal B\ne0,\\
\mathcal C\in L[T],\quad \deg\mathcal C=k\ge2,\\
R=V-\mathcal A(U),\qquad H=U-\mathcal B(R),\\
\Phi=\mathcal C(H)+\lambda R+n,
\qquad \lambda\in L^*,\quad n\in L .
\end{gathered}
\tag{1}
\]
Primes on the three calligraphic polynomials mean derivatives in
their polynomial argument. A subscript \(\delta\) means coefficient
derivation, before substituting that argument. These operations are
different when \(R,H\) also have nonzero coefficient derivatives.

There do not exist \(\alpha\in L^*\) and \(\beta,c\in L\) such that
\[
\Psi=\alpha H+\beta+c\Phi,
\qquad \delta\Phi=\partial_U\Psi .
\tag{2}
\]
No centering of any polynomial in (1), root extraction, second
coefficient derivation, or constant-field hypothesis is needed.
The coefficient derivative \(\delta\) may be any derivation of
the stated field.

## 2. The full derivative identity in independent residual variables

The residual variables are independent over \(L\), since the inverse
formulas are
\[
U=H+\mathcal B(R),\qquad
V=R+\mathcal A\bigl(H+\mathcal B(R)\bigr),\qquad
L[U,V]=L[R,H].
\tag{3}
\]
This is a change of variables in the formal plane only. Its use
does not declare an allowed original four-ring coordinate change.

At fixed \(U,V\), the chain rules give
\[
\begin{gathered}
\delta R=-\mathcal A_\delta(U),\qquad
\delta H=-\mathcal B_\delta(R)
                 +\mathcal B'(R)\mathcal A_\delta(U),\\
R_U=-\mathcal A'(U),\qquad
H_U=1+\mathcal B'(R)\mathcal A'(U),\\
P(U)=c\mathcal A'(U)-\mathcal A_\delta(U),
\qquad \deg P\le r .
\end{gathered}
\tag{4}
\]
In particular \(c\) is not differentiated in \(\partial_U\Psi\):
it is a coefficient in \(L\). The coefficients of
\(\mathcal A,\mathcal B,\mathcal C,\lambda,n\), however, all
retain their derivatives in \(\delta\Phi\).

Substituting (4) into (2), and then using (3), gives the exact
polynomial identity in \(L[H][R]\)
\[
\begin{aligned}
&\mathcal C_\delta(H)
-\mathcal C'(H)\Bigl\{
  \mathcal B_\delta(R)
 +\mathcal B'(R)P\bigl(H+\mathcal B(R)\bigr)+c\Bigr\}\\
&\hspace{1em}
+\lambda_\delta R
+\lambda P\bigl(H+\mathcal B(R)\bigr)+n_\delta\\
&\qquad\qquad
=\alpha\Bigl\{1+\mathcal B'(R)
                \mathcal A'\bigl(H+\mathcal B(R)\bigr)\Bigr\}.
\end{aligned}
\tag{5}
\]
For example the \(\lambda\)-terms on the left combine
\(-\lambda\mathcal A_\delta\), from differentiating \(\Phi\),
with \(+c\lambda\mathcal A'\), after moving the corresponding
term of \(\partial_U\Psi\). This checks the sign of \(\lambda P\).
The term \(-c\mathcal C'(H)\) in (5) comes from the constant
one in \(H_U\) and must also be retained.

## 3. Two successive degree comparisons

Suppose first that \(P\) has degree \(r\), with nonzero leading
coefficient \(p_r\). The term
\(-\mathcal C'(H)\mathcal B'(R)P(H+\mathcal B(R))\)
then has \(R\)-degree \(q(r+1)-1\), and its coefficient is
\[
-q\,b_q^{r+1}\,p_r\,\mathcal C'(H)\ne0 .
\tag{6}
\]
Every other term of (5) has smaller \(R\)-degree:
\(\lambda P(H+\mathcal B(R))\) has degree at most \(qr\);
the right side has degree \(qr-1\);
\(\mathcal B_\delta(R)\) has degree at most \(q\);
and the remaining terms have degree at most one.
Since \(q\ge2\), the degree in (6) is strictly larger than
\(qr\). Its coefficient cannot cancel. Therefore
\(\deg P\le r-1\). This also covers the case \(P=0\).

Now let \(p_{r-1}\in L\) denote the coefficient of \(U^{r-1}\)
in \(P\), possibly zero. Compare the coefficient of
\(R^{qr-1}\) in (5). The only contributions are the
\(\mathcal B'P\) term on the left and the
\(\alpha\mathcal B'\mathcal A'\) term on the right.
Indeed
\[
\begin{gathered}
qr-1>q,\qquad qr-1>q(r-1),\\
-q b_q^r\,p_{r-1}\mathcal C'(H)
 =\alpha q r a_r b_q^r,\qquad
\boxed{\ -p_{r-1}\mathcal C'(H)=\alpha r a_r\ } .
\end{gathered}
\tag{7}
\]
The strict inequalities use \(r,q\ge2\); they include
\(r=q=2\). The coefficient \(\mathcal C_\delta(H)\) has
\(R\)-degree zero, regardless of its degree in \(H\).

If \(p_{r-1}=0\), (7) equates zero with a nonzero field element.
Otherwise its left side has \(H\)-degree \(k-1\ge1\), whereas
its right side is a nonzero element of \(L\).
Both cases are impossible. This proves the differential-field
statement, using only the single identity in (2).

## 4. Why the actual canonical tails meet the second-tail gate

For the application, retain the actual dense leading normalization153
and exact chart139/145, including
\[
\begin{gathered}
B=\mathbb C[X,Y,Z,W]=A[u],\quad E=\partial_u,
\quad E^2X=E^2Y=E^2Z=0,\\
\deg_EW=\mu=m\ge2,\quad d=m+1,
\quad f_m=\gamma\tau^d,\quad\gamma\in\mathbb C^*,\\
L/\mathbb C(\tau,\rho)\text{ finite separable},\quad
L[y,z]=L[v],\quad
\ker(L[U,V]\longrightarrow L[v])=(g),\\
\Phi\in L^*g,\quad \deg\Phi=d,
\quad \Phi_d=-\gamma U^d,\qquad
\Psi(y,z)=v+\beta_0,\quad\beta_0\in L,\\
\Psi_U=\Phi_\tau,\qquad \deg\Psi\le d .
\end{gathered}
\tag{8}
\]
These are actual canonical tails, with their retained selected
partial and generic-line normalization.[^1]
The improved second-tail degree bound follows because the possible
degree-\(d+1\) term differentiates the complex degree-\(d\)
polynomial \(f_m\), and is therefore zero.

Suppose in addition that the literal \(\Phi\) in (8), in those
same formal \(U,V\) axes, has the placement (1). Its degree is
\(rqk=d\), since the successive leading coefficients are nonzero.
The quotient is the whole polynomial line with parameter \(H\):
\[
\begin{gathered}
L[U,V]/(\Phi)=L[H],\qquad
R=-\frac{\mathcal C(H)+n}{\lambda},\quad
U=H+\mathcal B(R),\quad V=R+\mathcal A(U),\\
H(y,z)=a_0v+b_0,\qquad a_0\in L^*,\quad b_0\in L,\\
\Psi-\alpha H-\beta\in(\Phi),\qquad
\alpha=a_0^{-1}\ne0,\quad
\beta=\beta_0-a_0^{-1}b_0,\qquad
\Psi=\alpha H+\beta+c\Phi\quad(c\in L).
\end{gathered}
\tag{9}
\]
The parameter is affine-linear because its polynomial ring is
exactly \(L[v]\), not merely a subring with the same fraction
field. Also \(\deg H=rq<d\), and \(\deg\Psi\le d\), so the
quotient in the last line has degree at most zero. This proves
the precise gate (2); it is not an arbitrary choice of a second
formal polynomial.

The coefficient derivation \(\delta=\partial_\tau\) on the
finite separable field \(L\), extended to fix \(U,V\), now
satisfies (2) by (8). Sections 2--3 give a contradiction.
Thus no actual normalized dense frame has the specified
fixed-axis three-stage placement, for any \(r,q,k\ge2\).

## 5. Exact scope and remaining placement questions

The all-quadratic case \((r,q,k)=(2,2,2)\), with implicit degree
eight, is a special case of the obstruction. This note does not
classify all degree-eight embedded lines, nor does it assert
recognition for every frame of minimum \(\mu=7\).
Such conclusions require a separate exhaustive placement argument.

No coefficient-dependent transformation of the original goods
has been used. The formal inverse (3) is only a device for
coefficient comparison, whereas (8) concerns the actual original
four-ring. An arbitrary plane coordinate or a generic polynomial
parameter does not by itself supply the normalized canonical
second-tail degree and derivative identities.

The proof in Sections 1--3 is purely algebraic and needs no new
classification input. Its actual application inherits the full
chart, primitivity and leading-normalization proofs. No historical
novelty clearance, recursive audit of all earlier dependencies,
human expert verification, proof-assistant certification, or
unrestricted cancellation statement is claimed.

## Sources and retained inputs

1. [All-degree leading normalization153](dense-all-degree-leading-normalization-pass153-working.md).
   The actual complex leading coefficient and normalized fixed axes
   used in (8). This is not a permission to make arbitrary formal
   plane changes in the original ring.
2. [Dense chart139](dense-all-degree-taylor-chart-pass139-working.md),
   [signed negative tails139](dense-negative-tail-relations-pass139-working.md),
   and [first-tail primitivity145](common-gauss-integrality-tail-primitivity-pass145-working.md).
   Whole generic-line generation, the canonical parameter,
   the literal gradient identity, and association to the entire
   generic kernel in (8)--(9).
3. [Nested-quartic exclusion153](nested-quartic-exclusion-pass153-working.md)
   and [two-stage continuation154](two-stage-nongraph-continuation-pass154-working.md).
   These are adjacent placement arguments, not premises of the
   differential-field obstruction in Sections 1--3. The present
   proof does not reuse their actual Nagata reconstruction.

[^1]: Sources 1 and 2. Their hypotheses are retained in full in this
    actual-frame application; the algebraic statement in Section 1
    is deliberately independent of them.
