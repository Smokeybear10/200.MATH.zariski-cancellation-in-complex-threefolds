# The full formal Taylor system does not force a coordinate relation

The exact formal Taylor identities, including \(T(W)=1\), do not force
the first tail polynomial \(\Phi\) to be a plane coordinate or its
complementary factor to be constant. The example below satisfies the
whole finite-algebraic-field Taylor system, not just its gradient
identities.

It deliberately fails the actual polynomial-coordinate hypothesis.
Its underlying polynomial tuple has nonunit Jacobian, and the selected
field derivation does not return coefficients to the original polynomial
ring. Thus this is a counterexample to a formal implication, not to the
actual dense-chart theorem or to cancellation.

## 1. Coefficient field, generic line, and exact determinant

Let \(k,\rho,v,X\) be algebraically independent over \(\mathbb C\), and set
\[
\begin{gathered}
L=\mathbb C(k,\rho),\qquad \tau=k^2/2,\qquad F=L(v),\\
\partial_\tau=k^{-1}\partial_k,\qquad
\partial_\rho=\partial/\partial\rho,\qquad \partial_v=\partial/\partial v,\\
y=v,\qquad z=k,\qquad
Y=v+\tau X,\qquad Z=k+\rho X,\qquad
W=\rho k+\tfrac12\rho^2X .
\end{gathered}
\tag{1}
\]
The field \(L\) is a proper separable quadratic extension of
\(\mathbb C(\tau,\rho)\). Its displayed coefficient partials commute
and fix \(v\). We have \(y,z,w_0=\rho k\in L[v]\), and
\(L[y,z,w_0]=L[y,z]=L[v]\).

The relative Jacobian and its selected coordinate-field derivation are
\[
\begin{gathered}
\det\frac{\partial(Y,Z,W)}{\partial(\tau,\rho,v)}
=
\det\begin{pmatrix}
X&0&1\\
1/k&X&0\\
\rho/k&k+\rho X&0
\end{pmatrix}=1,\\
T=-\frac{X}{k}\partial_k+\frac1k\partial_\rho+X^2\partial_v
=-X\partial_\tau+\frac1k\partial_\rho+X^2\partial_v,\\
T(X)=T(Y)=T(Z)=0,\qquad T(W)=1,\qquad
[X^2]T|_F=\partial_v .
\end{gathered}
\tag{2}
\]
These identities follow by direct differentiation.
The top coefficient is the genuine LND \(\partial_v\) on \(L[v]\),
and the degree-two coefficient bound holds on all of \(F\).

Thus the normalized cofactor identities and whole generic line used in
the abstract tail argument hold exactly. No derivative of a hypothetical
coefficient array has been substituted for \(T(W)=1\).

## 2. The entire Taylor embedding is annihilated

Write \(\varepsilon=X^{-1}\), and extend \(T\) continuously to
\(F((\varepsilon))\) by its three coefficient derivations.
It lowers Laurent order by at most two and fixes \(\varepsilon\).
Use the exact positive-sign Taylor embedding from the dense chart:[^1]
\[
\begin{gathered}
\Theta(f)=\sum_{a,b\ge0}
\frac{\partial_\tau^a\partial_\rho^b f}{a!\,b!}
y^az^bX^{-a-b},\\
\Theta(\tau)=\tau+v/X,\qquad
\Theta(\rho)=\rho+k/X,\qquad
\Theta(k)^2=k^2+2v/X,\qquad T\Theta(f)=0\quad(f\in L).
\end{gathered}
\tag{3}
\]
The series is a multiplicative field embedding because the coefficient
partials commute and its constant term is \(f\).
For specificity, the root \(\Theta(k)\) is the unique formal expansion
with constant term \(k\); its first terms are
\(k+v/(kX)-v^2/(2k^3X^2)+\cdots\).

Both \(\Theta(\tau)\) and \(\Theta(\rho)\) are killed by \(T\):
\(T(\tau)=-X\), \(T(v)=X^2\), \(T(\rho)=1/k\), and \(T(k)=-X/k\).
Differentiating the quadratic identity for \(\Theta(k)\) then proves
\(T\Theta(k)=0\), since \(2\Theta(k)\) is a unit of the Laurent field.
This proves annihilation on all of \(L=\mathbb C(k,\rho)\).
The full algebraic Taylor system therefore holds, not merely a bounded
truncation or the rational-base identities.

## 3. Exact tails and a nonconstant complementary factor

The last polynomial has \(X\)-degree one.
Its peeling coefficients are \(f_1=\rho^2/2\) and \(f_0=0\).
Indeed
\[
\begin{gathered}
\mathscr S=X\Theta(\rho^2/2)
=\tfrac12\rho^2X+\rho k+\frac{k^2}{2X},\qquad
W=(\mathscr S)_{\ge0},\\
\mathscr R=W-\mathscr S=-\tau/X,\qquad T\mathscr R=1,\qquad
f_{-1}=-\tau,\\
\mathscr R-X^{-1}\Theta(f_{-1})=v/X^2,\qquad
T(v/X^2)=1 .
\end{gathered}
\tag{4}
\]
Thus both negative stages, with their signs and derivative values,
are exact rational identities.

Let \(U,V\) now be independent formal polynomial variables.
The first relation and second parameter from the full tail formulas are
\[
\begin{gathered}
R_1(U,V)=-V^2/2,\qquad
\Phi(U,V)=R_1(U,V)-f_{-1}=\tau-V^2/2,\\
\Psi(U,V)=U,\qquad
\Phi(y,z)=0,\qquad \partial_v\Psi(y,z)=1,\qquad
(\Psi_U,\Psi_V)=(\Phi_\tau,\Phi_\rho)=(1,0),\\
g=V-k,\qquad
\ker\bigl(L[U,V]\longrightarrow L[v],\ (U,V)\mapsto(v,k)\bigr)=(g),\\
\Phi=gH,\qquad H=-\tfrac12(V+k),\qquad H(y,z)=-k\in L^* .
\end{gathered}
\tag{5}
\]
In particular the evaluated gradient ideal is the unit ideal:
\(\Phi_U(y,z)=0\), \(\Phi_V(y,z)=-k\).
The exact differential identities of the tail lemma are all present.[^2]

Nevertheless \(H\) is a nonconstant polynomial in \(L[U,V]\).
The polynomial \(\Phi\) has the distinct nonconstant factors \(V-k\)
and \(V+k\), up to a nonzero scalar. It cannot be a coordinate of
\(L[U,V]\): its quotient is not a domain, whereas the quotient by
a polynomial coordinate is a one-variable polynomial domain.
The factors are even comaximal because \(2k\in L^*\).
Thus neither the unit restriction of \(H\) to the embedded line nor
the full Taylor system makes \(H\) constant or \(\Phi\) a coordinate.

## 4. Precisely which actual-frame premise fails

There is an underlying polynomial translation action
\(E=\partial_X\) on \(B_*=\mathbb C[X,k,\rho,v]\).
The four displayed polynomials \(X,Y,Z,W\) satisfy
\[
\begin{gathered}
(EX,EY,EZ)=(1,k^2/2,\rho),\qquad
E^2X=E^2Y=E^2Z=0,\qquad EW=\rho^2/2,\quad E^2W=0,\\
EX=1,\qquad \ker_{B_*}E=\mathbb C[k,\rho,v],\qquad
\det\frac{\partial(X,Y,Z,W)}{\partial(X,k,\rho,v)}=k .
\end{gathered}
\tag{6}
\]
The two nonconstant speeds are algebraically independent. Their
homogeneous cone is dense, since no nonzero homogeneous polynomial
can vanish on \((1,k^2/2,\rho)\).
The action has an actual global slice \(X\).

But \(k\) is a nonunit of \(B_*\). The last determinant in (6)
rules out a polynomial inverse for the displayed tuple.
The relative determinant in (2) is one only after replacing the
polynomial variable \(k\) by the coefficient parameter \(\tau=k^2/2\).
It must not be identified with the actual coordinate Jacobian.

The failure is also visible in the Taylor projection at \(X=0\):
the displayed subring is \(\mathbb C[v,k,\rho k]\), not
\(\mathbb C[v,k,\rho]\). It does not contain \(\rho\); modulo \(k\)
its image is only \(\mathbb C[v]\).
Since the selected good speed \(EX\) is one, localization at that
speed cannot repair this strict inclusion.
Also \(T(k)=-X/k\notin B_*\), so this field derivation is not an
actual polynomial coordinate partial on \(B_*\).
These are the actual inverse and coefficient-return gates omitted
by the formal example.

## 5. Arbitrarily high finite degree, with the same limitation

The formal obstruction is not confined to degree one.
For any integer \(\ell\ge2\), put
\[
W_\ell=W+Y^\ell,\qquad
T(W_\ell)=1,\qquad
Y^\ell=X^\ell\Theta(\tau^\ell),\qquad
E^\ell W_\ell=\ell!\,\tau^\ell\ne0 .
\tag{7}
\]
Adding this exact annihilated Taylor term leaves both negative tails
and the polynomials \(\Phi,\Psi\) in (5) unchanged.
The corresponding underlying polynomial tuple still has Jacobian
\(k\), since the last change is a bad-slot shear of the same
noninvertible polynomial tuple.

This proves failure of the proposed formal implication in arbitrarily
high finite degree. It does not decide whether the additional
actual polynomial-coordinate and coefficient-return hypotheses force
\(\Phi\) itself to be a coordinate or \(H\) to be constant.
That stronger actual-frame question remains open in this note.
No example here is a cancellation counterexample.

## Sources

1. [A dense all-degree chart and its formal Taylor peeling](dense-all-degree-taylor-chart-pass139-working.md),
   Sections 5--6. Exact formal embedding, continuous Laurent derivation,
   and nonnegative-part peeling. All identities needed for this example
   are computed directly above.
2. [The first two negative Taylor coefficients in a dense chart](dense-negative-tail-relations-pass139-working.md),
   Sections 2--4. Signed tail definitions and the precise distinction
   between a complementary factor and its unit restriction to the line.

[^1]: [Dense Taylor chart139](dense-all-degree-taylor-chart-pass139-working.md), Sections 5--6.
[^2]: [Negative-tail lemma139](dense-negative-tail-relations-pass139-working.md), Sections 2--4.
