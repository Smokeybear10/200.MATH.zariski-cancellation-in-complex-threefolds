# Coefficient compatibility selects the actual first-tail component

In an actual dense chart, the projected functions \(y,z,w_0\)
are algebraically independent complex rational coordinates on the
invariant function field. A formally persistent first-tail component
therefore gives an embedding of that function field. The component
is the actual one precisely when this embedding fixes two speed
ratios and one primitive element of their finite coefficient extension.

Clearing these three rational identities gives a finite polynomial
criterion. After removing denominator factors from a gcd, it recovers
the selected irreducible equation, including when the first tail has
inactive or repeated factors. This identifies the missing coefficient
compatibility; it does not prove that compatibility follows from the
first-tail equation or from the formal recurrences alone.

## 1. Actual source field and the polynomial representatives

Assume the actual dense-chart hypotheses139:
\[
\begin{gathered}
B=\mathbb C[X,Y,Z,W]=A[u],\qquad E=\partial_u,\qquad A=\ker E,\\
E^2X=E^2Y=E^2Z=0,\qquad s=EX,\quad t=EY,\quad b=EZ,\\
\operatorname{trdeg}_{\mathbb C}\mathbb C(s,t,b)=2,\qquad
H(s,t,b)\ne0
\quad\text{for every nonzero homogeneous }H\in\mathbb C[S,T,B_0].
\end{gathered}
\tag{1}
\]
The four displayed generators are polynomial coordinates, and the
slice \(u\) is fixed. There is no bound on \(m=\deg_EW\ge0\).

Use the actual localized chart and intrinsic leading derivation,
with the following particular conclusions.[^1]
\[
\begin{gathered}
T=\partial_W,\qquad N=[u^2]T|_A\ne0,\\
F:=\operatorname{Frac}A=\mathbb C(y,z,w_0),\qquad
y,z,w_0\text{ algebraically independent over }\mathbb C,\\
A_s=\mathbb C[y,z,w_0]_{s_0},\qquad
L=\operatorname{Frac}(\ker_A N),\quad
K=\mathbb C(\tau,\rho),\quad \tau=t/s,\quad \rho=b/s,\\
L/K\text{ finite separable},\qquad F=L(v),\qquad
L[y,z]=L[v],\qquad N'=N/s^2=\partial_v .
\end{gathered}
\tag{2}
\]
The rational presentation of \(F\) in the first line follows from
the actual polynomial presentation of \(A_s\), not merely from
the relative generic Jacobian. The denominator \(s_0\) is nonzero
and disappears on taking the fraction field.

Choose \(e\in L\) with \(L=K(e)\). Such a primitive element exists
because the extension is finite separable and \(K\) is infinite.
For example, two generators can be replaced by \(a+\lambda b\)
with \(\lambda\in K\) outside the finitely many values at which
two distinct embeddings have equal images; iterating gives a
single generator. If \(L=K\), one may take \(e=0\).

Keep the normalized coefficient partials on \(L\) and the exact
peeling coefficients \(f_0,\ldots,f_m,f_{-1}\in L\).
For independent \(U,V\), put
\[
\begin{gathered}
H_d(f;U,V)=\sum_{a+b=d}
 \frac{\partial_\tau^a\partial_\rho^b f}{a!\,b!}U^aV^b,\qquad
\Omega(U,V)=\sum_{j=0}^{m}H_j(f_j;U,V),\quad
w_0=\Omega(y,z),\\
\Phi=-\sum_{j=0}^{m}H_{j+1}(f_j;U,V)-f_{-1}\ne0,\qquad
\Psi=-\sum_{j=0}^{m}H_{j+2}(f_j;U,V)-H_1(f_{-1};U,V),\\
\ker\bigl(L[U,V]\longrightarrow L[v],\ (U,V)\longmapsto(y,z)\bigr)
=(g),\qquad g\text{ irreducible}.
\end{gathered}
\tag{3}
\]
The chart gives the expression for \(w_0\); the tail proof gives
\(g\mid\Phi\), \(\Psi(y,z)=v+c\) for \(c\in L\), and multiplicity
one for \(g\) in \(\Phi\).[^2]
All polynomials and factors below are taken over this same exact
field \(L\), without passing to an algebraic closure.

## 2. Every active component gives a source-field embedding

For an irreducible factor \(h\mid\Phi\), let
\[
R_h=L[U,V]/(h),\quad F_h=\operatorname{Frac}R_h,\quad
y_h=\overline U,\quad z_h=\overline V,\quad
w_{0h}=\Omega(y_h,z_h),\quad v_h=\Psi(y_h,z_h).
\tag{4}
\]
Call the component active when \(v_h\) is transcendental over \(L\).
This is stronger than merely \(v_h\notin L\).

For an active component, the persistence theorem141 extends the
coefficient partials through the finite separable field
\(F_h/L(v_h)\), and constructs a polynomial \(W_h(X)\) with
\(W_h(0)=w_{0h}\). Its exact relative Jacobian is one.
Evaluating that identity at \(X=0\) gives
\[
\det\frac{\partial(y_h,z_h,w_{0h})}
              {\partial(\tau,\rho,v_h)}=1,\qquad
\sigma_h:F=\mathbb C(y,z,w_0)\hookrightarrow F_h,\quad
(y,z,w_0)\longmapsto(y_h,z_h,w_{0h}).
\tag{5}
\]
Here the determinant uses the extended derivations, not a claim
that \(F_h\) is a polynomial ring.[^3]

The nonzero determinant proves algebraic independence of the
three images over \(\mathbb C\). One elementary justification is
to choose a nonzero complex polynomial relation of minimal total
degree if a relation existed. Differentiating it with the three
derivations and using the invertible matrix makes every evaluated
partial derivative of the relation zero. At least one such partial
is nonzero in characteristic zero and has smaller degree, a
contradiction. Algebraic independence gives the field embedding
in (5), with no vanishing denominator for a nonzero rational
function of the actual source triple.

The embedding need not fix the already embedded field \(L\subset
F_h\). There are two potentially different values of an element
of \(L\): its coefficient-field value and its value obtained by
rational substitution through \(\sigma_h\).

## 3. Three exact tests for coefficient compatibility

Since \(\tau,\rho,e\in F=\mathbb C(y,z,w_0)\), choose a common
nonzero polynomial denominator and numerators
\[
\begin{gathered}
q,p_\tau,p_\rho,p_e\in
 \mathbb C[\xi_1,\xi_2,\xi_3],\qquad q\ne0,\qquad
\alpha=\frac{p_\alpha(y,z,w_0)}{q(y,z,w_0)}
 \quad(\alpha=\tau,\rho,e),\\
\Delta(U,V)=q(U,V,\Omega(U,V)),\\
A_\alpha(U,V)=p_\alpha(U,V,\Omega(U,V))
                   -\alpha\Delta(U,V)\in L[U,V].
\end{gathered}
\tag{6}
\]
No coprimality of the displayed numerators and denominator is
required. A common denominator exists by multiplying individual
denominators. In particular \(\Delta\ne0\): evaluation on the
actual component gives the nonzero \(q(y,z,w_0)\).
Moreover \(g\nmid\Delta\), and \(g\mid A_\alpha\) for all three
indices.

For every active \(h\), algebraic independence in (5) also gives
\(h\nmid\Delta\). Therefore
\[
\begin{gathered}
h\text{ active}\quad\Longrightarrow\\
h\sim g
\quad\Longleftrightarrow\quad
\sigma_h(\tau)=\tau,\ \sigma_h(\rho)=\rho,\ \sigma_h(e)=e
\quad\Longleftrightarrow\quad
h\mid A_\tau,\ A_\rho,\ A_e .
\end{gathered}
\tag{7}
\]
Here \(\sim\) means association by a nonzero element of \(L\).
The final equivalence follows from (6), since the common
denominator has nonzero residue on that component.

If the three values are fixed, then \(\sigma_h\) fixes
\(L=\mathbb C(\tau,\rho)(e)\). Apply \(\sigma_h\) to the actual
identity \(g(y,z)=0\), including every coefficient of \(g\).
It gives \(g(y_h,z_h)=0\). The evaluation kernel on \(L[U,V]\)
is \((h)\), so \(h\mid g\), and irreducibility gives \(h\sim g\).

Conversely, for \(h\sim g\), the exact evaluation map identifies
\(F_h\) with \(L(y,z)=F\), fixing \(L\) and sending
\((y_h,z_h,w_{0h})\) to \((y,z,w_0)\).
Under this identification \(\sigma_h\) is the identity.
Also \(v_h\) maps to \(v+c\), so this selected component is active.
This proves every direction in (7).

## 4. The denominator-cleared criterion also handles other factors

An activity hypothesis is unnecessary if compatibility and a
nonvanishing denominator are assumed directly. Specifically,
\[
\begin{gathered}
h\text{ irreducible},\quad h\mid\Phi,\quad
h\mid A_\tau,\ A_\rho,\ A_e,\quad h\nmid\Delta
\quad\Longrightarrow\quad h\sim g .
\end{gathered}
\tag{8}
\]
To prove it, work in \(F_h\) from (4), without assuming anything
about \(v_h\). Put
\(M_h=\mathbb C(y_h,z_h,w_{0h})\subset F_h\).
The identities (6), with a nonzero denominator modulo \(h\),
put \(\tau,\rho,e\) in \(M_h\). Hence
\(L\subset M_h\). Because \(F_h=L(y_h,z_h)\), this implies
\(M_h=F_h\).

The field \(F_h\) has transcendence degree three over \(\mathbb C\),
since \(\operatorname{trdeg}_L F_h=1\) and
\(\operatorname{trdeg}_{\mathbb C}L=2\).
Its three displayed generators \(y_h,z_h,w_{0h}\) must therefore
be algebraically independent over \(\mathbb C\).
Rational substitution again defines \(\sigma_h:F\to F_h\),
now an isomorphism onto \(F_h\), fixing \(\tau,\rho,e\).
The same coefficient-fixing argument with \(g\) proves (8).

Thus every compatible non-base-locus factor is the selected
active factor. Factors on which \(\Delta\) vanishes are not
covered by (8); clearing rational equations can create such
base-locus factors, and they must not be accepted as compatible.

## 5. An explicit finite gcd recovers the selected factor

Gcds are taken in the UFD \(L[U,V]\), up to coefficient-field
units. Put
\[
D=\deg\Phi,\qquad
C_0=\gcd(\Phi,A_\tau,A_\rho,A_e),\qquad
G_0=\frac{C_0}{\gcd(C_0,\Delta^D)} .
\qquad \boxed{\ G_0\sim g\ } .
\tag{9}
\]
The degree \(D\) is a positive integer. Since \(C_0\mid\Phi\),
the multiplicity of any irreducible factor in \(C_0\) is at most
\(D\). Thus dividing by \(\gcd(C_0,\Delta^D)\) removes every
factor of \(C_0\) that divides \(\Delta\), with its full
multiplicity, and removes no other factor.

Every remaining factor satisfies (8), so is associated to \(g\).
Conversely, \(g\) divides all four arguments defining \(C_0\),
does not divide \(\Delta\), and occurs with multiplicity one in
\(\Phi\). Therefore it occurs with multiplicity exactly one
in \(G_0\). This proves (9), including when \(\Phi\) has dead
or repeated factors.

Equivalently, this is the saturation of the principal gcd ideal
\((C_0)\) by powers of \(\Delta\). It is a codimension-one
factor statement. A separate actual generic-fiber argument142
proves the stronger full ideal equality
\((A_\tau,A_\rho,A_e):\Delta^\infty=(g)\), even without
including \(\Phi\). Thus the ideal with \(\Phi\) included also
saturates to \((g)\); this stronger conclusion uses the exact
source-ring graph presentation, not the gcd argument alone.[^5]

A finite criterion for first-tail primitivity follows:
\[
\Phi\in L^*g
\quad\Longleftrightarrow\quad
\gcd(\Phi,\Delta)=1
\quad\text{and}\quad
\Phi\mid A_\tau,\ A_\rho,\ A_e .
\tag{10}
\]
The forward implication was established after (6). Conversely,
the displayed divisibilities make \(C_0\sim\Phi\), and the
coprimality removes nothing in (9), so \(\Phi\sim g\).
These are exact polynomial tests using the actual rational
expressions in (6), not inferred consequences of \(\Phi=0\).

## 6. What this proves and what remains

The three rational identities in (6) are finite source data.
Once their expressions and the Taylor coefficients are known,
(9) selects the actual generic equation by polynomial gcds,
without requiring a prior factorization over a larger field.
No uniform degree bound for the numerators or denominators is
claimed.

Finiteness of \(L/K\) alone does not justify dropping the test
for \(e\). Actual sliced polynomial frames have such extensions
of arbitrarily large degree, even at last-coordinate time degree
one.[^4] Fixing only the base parameters has not been shown to
fix this extension pointwise.

For active components the common denominator never vanishes.
The obstruction there is exactly whether the substitution
embedding fixes the coefficient field. For other factors,
(8)--(9) separate genuine compatibility from denominator
artifacts, without assuming activity or counting them as inverse
branches.

The result does not show that every active component passes the
three tests, that every factor is active, or that the coprimality
and divisibilities in (10) always hold. The full formal recurrence
system supplied by141 does not itself establish these extra
identities. No global invariant coordinate, arbitrary coordinate
entry, or cancellation theorem follows from this criterion alone.

## Sources

1. [A dense all-degree chart and its formal Taylor peeling139](dense-all-degree-taylor-chart-pass139-working.md),
   Sections 1--3 and 6. Actual projected polynomial localization,
   exact invariant field, and the polynomial representative of \(w_0\).
2. [The first two negative Taylor coefficients in a dense chart139](dense-negative-tail-relations-pass139-working.md),
   Sections 2--4. First relation, second-tail parameter, exact kernel
   and selected-factor multiplicity one.
3. [Formal persistence on a first-tail component141](dense-tail-component-persistence-pass141-working.md),
   Sections 1--4. Active-component function field and exact relative
   Jacobian, without a polynomial inverse claim.
4. [Unbounded coefficient-field degree in actual dense sliced frames140](unbounded-actual-coefficient-field-pass140-working.md),
   Sections 1--4. Actual polynomial inverse and unbounded finite
   coefficient-field degree, with the first evaluated tail outside
   the speed-ratio field.
5. [The actual generic fiber gives the full compatibility saturation142](source-generic-fiber-saturation-pass142-working.md),
   Sections 2--4. The exact graph presentation and full ideal
   saturation, strengthening the codimension-one gcd argument.

The compatibility and gcd arguments above are elementary field
and polynomial-ring deductions from these stated inputs. No new
classification theorem or historical novelty claim is invoked.

[^1]: Source 1, especially the actual ring identity
    \(A_s=\mathbb C[y,z,w_0]_{s_0}\).
[^2]: Sources 1--2, the constant coefficient of the peeling formula
    and the exact first two negative tails.
[^3]: Source 3, the coefficient derivations and determinant at \(X=0\).
[^4]: Source 4. This is an actual-frame boundary, not a hypothetical
    finite extension or a Jacobian-only construction.
[^5]: Source 5. Under the exact actual source-ring hypotheses,
    no lower-dimensional condition remains after this saturation.
