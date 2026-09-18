# Gauge promotion to an actual first-shift frame

## 1. Uniform statement

Let \(R=\mathbb C[x,y,z]\), and let \(H\ne0\) be a locally
nilpotent derivation homogeneous of positive ordinary derivation
degree \(d>0\). Thus, for the ordinary Euler derivation \(D_R\),
\([D_R,H]=dH\). For nonzero \(P\in R\), write
\(\deg_H P=\max\{j:H^jP\ne0\}\), and set
\(\deg_H0=-\infty\).
After a permutation of the supplied coordinates, suppose
\[
 N=\deg_Hz=\max\{\deg_Hx,\deg_Hy,\deg_Hz\}\ge1.
\tag{1}
\]
Let \(\psi\in R\) be ordinary homogeneous of degree
\(\ell>d\), and put \(q=\ell-d\ge1\). The zero polynomial is
allowed, with \(\ell\) then an assigned degree for this statement.
Assume precisely
\[
 \deg_H\psi\le qN-1.
\tag{2}
\]
On \(B=R[T]\), define the LND
\(E_0=H+(1+\psi)\partial_T\).

There are complex constants \(\gamma\ne0,\lambda,\mu\) such that
the actual polynomial coordinates
\[
 X=x+\lambda z,\qquad Y=y+\mu z,\qquad Z=z,\qquad
 t=T+\gamma z^q
\tag{3}
\]
have exact positive \(E_0\)-degrees \((N,N,N,qN)\).
In these coordinates the same derivation, written as \(E\), is
\[
 E=H+h\partial_t,\qquad
 h=1+\psi+\gamma H(z^q).
\tag{4}
\]
Its actual degree-weighted Euler derivation is
\[
 D=N D_R+qNt\partial_t.
\tag{5}
\]
In (4)--(5), the derivations \(H,D_R\) of \(R\) are extended
by killing the new coordinate \(t\). They are not being retained
as extensions that kill the old \(T\). The linear change of the
three base coordinates preserves their ordinary grading.
The all-ring \(E\)-filtration shift of \(D\) is exactly one,
without any assumption that \(E_0\) or \(E\) has a polynomial slice.
Moreover, \(E\) is the sum of two commuting \(D\)-homogeneous LNDs.

When \(\deg_H\psi<qN-1\), every \(\gamma\ne0\), in particular
\(\gamma=1\), is permitted. Under equality in (2), there is at
most one additional forbidden value of \(\gamma\). The boundary
\(qN=1\) has no forbidden value at all. The choices for \(\lambda\)
and \(\mu\) each exclude at most one complex value.

This is an elementary coordinate-gauge statement, not a recognition
theorem or a novelty claim. It does not say that arbitrary sliced
actions admit this homogeneous presentation or satisfy (2).
It does not say that the change lowers a degree-minimizing complexity.
The distinction between transporting an Euler field and recomputing
one after a new frame selection is essential and is made explicit
in Sections 5 and 6.

## 2. All degree and cancellation cases

The derivation \(E_0\) is locally nilpotent: its restriction to \(R\)
is \(H\), and its successive derivatives on \(T\) are the finite
\(H\)-sequence starting with \(1+\psi\). The displayed gauge and
linear mixing are genuine polynomial coordinate changes, with full
inverse
\[
 x=X-\lambda Z,\qquad y=Y-\mu Z,\qquad
 z=Z,\qquad T=t-\gamma Z^q.
\tag{6}
\]
Equation (4) follows by applying \(E_0\) to (3), not by treating
a coefficient-field expression as an ambient map.

For a nonzero LND in characteristic zero, its degree is additive
on products. The highest Leibniz term proves this: if the degrees
of \(P,Q\) are \(i,j\), then
\(H^{i+j}(PQ)=\binom{i+j}{i}H^i(P)H^j(Q)\ne0\).
Also \(\deg_H(HP)=\deg_HP-1\) whenever \(HP\ne0\).
Consequently, with \(k=qN-1\ge0\),
\[
 \deg_H(z^q)=qN,\qquad
 \deg_H H(z^q)=k.
\tag{7}
\]

First suppose \(k>0\). If the inequality in (2) is strict,
the highest \(H\)-degree term of \(h\) comes uniquely from
\(\gamma H(z^q)\), so \(\deg_Hh=k\) for every nonzero \(\gamma\).
If \(\deg_H\psi=k\), cancellation can occur only when
\[
 H^k\psi+\gamma H^{k+1}(z^q)=0.
\tag{8}
\]
The second coefficient is nonzero by (7), so (8) has at most
one solution \(\gamma\in\mathbb C\). Avoid it and zero.
No assertion that a ratio of the two invariant coefficients is
complex is needed.

If \(k=0\), then \(q=N=1\). Both \(\psi\) and \(H(z)\) are
\(H\)-invariant. Their sum is ordinary homogeneous of degree
\(\ell=d+1>0\), possibly zero. Therefore
\(h=1+\psi+\gamma H(z)\ne0\), even if those two positive-degree
summands cancel. Thus \(\deg_Hh=0=k\) for every \(\gamma\).
Under the strict inequality in this case, \(\psi=0\) by convention.

It follows in every permitted case that
\[
 \deg_Et=\deg_Hh+1=k+1=qN.
\tag{9}
\]
For the base coordinates, \(H^Nz\ne0\), while
\(H^N(x+\lambda z)=H^Nx+\lambda H^Nz\). This is nonzero
outside at most one complex value of \(\lambda\). The same
argument applies to \(y+\mu z\). It includes both strict base
degree inequalities and all leading-coefficient ties. Since their
degrees cannot exceed \(N\), these choices give exactly the
tuple in Section 1. Linear mixing among three coordinates of
equal weight \(N\) preserves \(N D_R\), proving (5).

If \(\deg_H\psi>qN-1\), this particular gauge cannot cancel
its higher \(H\)-degree term, since \(H(z^q)\) has degree
\(qN-1\). The claimed degree alignment is then not supplied by
this argument. No conclusion about different gauges or frames
is drawn from that boundary.

## 3. Whole commutator and the upper shift bound

The polynomial \(\psi+\gamma H(z^q)\) is ordinary homogeneous
of degree \(\ell=d+q\). With the convention \([E,D]=ED-DE\),
homogeneity gives the entire derivation identity
\[
 C:=[E,D]=N\ell\,\partial_t-NdE,
 \qquad [E,C]=0.
\tag{10}
\]
For example, the nonconstant vertical coefficient has weight
\(N\ell-qN=Nd\), the same as \(H\), while the constant
vertical field has weight \(-qN\). These identities do not
discard any lower coefficient of \(\psi\) or \(H\).

For every \(j\ge1\), commutation of \(C\) and \(E\) gives
\[
 [E^j,D]=jCE^{j-1}.
\tag{11}
\]
If \(\deg_E P=s\), then (11) at \(j=s+2\) gives
\(E^{s+2}(DP)=0\). Hence the all-ring shift
\[
 \delta_E(D)=
 \sup_{\substack{0\ne P\in B\\DP\ne0}}
       \bigl(\deg_E DP-\deg_E P\bigr)
 \le1.
\tag{12}
\]
This reasoning uses only the LND filtration and the whole
commutator. It does not import a slice-dependent terminal-order
formula.

In particular the two fields
\[
 L=\partial_t,\qquad
 K=H+(\psi+\gamma H(z^q))\partial_t
\tag{13}
\]
are commuting LNDs, and
\([D,L]=-qNL\), \([D,K]=NdK\). The local nilpotence of
\(K\) follows from the same finite-sequence argument as for
\(E_0\). Both are nonzero and have distinct weights, since
\(N,q,d>0\). Thus this is an actual positive-weight commuting
presentation, not merely a formal splitting of the coefficients.

## 4. Cleared polynomial invariant proving exact shift one

An explicit local slice of \(H\) supplies a polynomial witness,
without assuming a global slice. Set
\[
 \rho=H^{N-1}z,\qquad p=H^Nz\ne0,
 \qquad H\rho=p,\qquad Hp=0.
\tag{14}
\]
For the \(h\) of (4), whose exact degree is \(k=qN-1\), put
\[
 B_h=\sum_{j=0}^{k}
       \frac{(-1)^j}{(j+1)!}\rho^{j+1}p^{k-j}H^j(h)
       \in R,
 \qquad I=p^{k+1}t-B_h\in B.
\tag{15}
\]
All exponents are nonnegative; no reciprocal of \(p\) is used
in these polynomials. Differentiating the entire sum, neighboring
terms cancel and the last boundary term contains \(H^{k+1}h=0\).
Precisely,
\[
 HB_h=p^{k+1}h,
 \qquad EI=0,
 \qquad \partial_tI=p^{k+1}\ne0.
\tag{16}
\]
This is the cleared finite antiderivative in the local slice
\(\rho/p\), but its validity is the displayed polynomial
telescoping identity. It remains valid when \(k=0\): then
\(B_h=\rho h\), with \(Hh=0\).

Applying (10) to this actual invariant gives
\[
 E(DI)=CI=N\ell p^{k+1}\ne0,
 \qquad E^2(DI)=0.
\tag{17}
\]
Thus \(\deg_EI=0\), \(\deg_E(DI)=1\), and (12) is sharp:
\(\delta_E(D)=1\). No freeness, unit image ideal, polynomial
kernel, finite generation of the kernel, or global \(E\)-slice
is assumed in this argument.

## 5. What the gauge preserves and what it does not

The elementary substitution \(t=T+\gamma z^q\) conjugates the
two presentations (4) and \(E_0\). Therefore it preserves
existence or nonexistence of a polynomial slice and transports
their kernels isomorphically. The base derivation remains \(H\),
and
\[
 \psi+\gamma H(z^q)\equiv\psi
                \pmod{H(R)+\ker H}.
\tag{18}
\]
The quotient in (18) is a quotient of complex vector spaces;
no assertion that \(H(R)+\ker H\) is an ideal is needed.
In particular gauge promotion cannot repair or disprove membership
in that image-plus-kernel subspace.

Simultaneous conjugacy of a pair \((E,D)\) preserves its shift.
Indeed \(\deg_{\alpha E\alpha^{-1}}(\alpha P)=\deg_E P\),
and \((\alpha D\alpha^{-1})(\alpha P)=\alpha(DP)\).
The definition (12) therefore gives equal shifts. Transporting
the entire coordinate frame transports its weighted Euler field
in exactly this way.

That is not what a fresh frame selection and reweighting does.
Here the old selected coordinate \(T\) is replaced by
\(t=T+\gamma z^q\), and the Euler field is recomputed using
the new actual degree \(qN\). It need not be the transported
Euler field of the old selected frame. Consequently the shift
attached to a selected, reweighted frame is not an invariant of
the derivation alone. The next example verifies this distinction
by both exact shifts, not just by different formulas for Euler
fields.

Within the subclass (1)--(2), existence of some actual first-shift
frame is automatic, whether or not the extension has a slice.
Thus adding that existence condition does not restrict the sliced
members of this subclass or solve their recognition problem.
This is a conditional transfer for the stated homogeneous
extensions, not an equivalence with general cancellation or an
assertion that every remaining sliced action satisfies these
conditions.

## 6. Exact before-and-after control

Take
\[
 H=x^2(\partial_y+\partial_z),\qquad
 \psi=x^3y,\qquad
 E_0=H+(1+x^3y)\partial_T.
\tag{19}
\]
Here \(d=N=1\), \(\ell=4\), \(q=3\), and
\(\deg_H\psi=1<qN-1=2\). The actual old frame and its
full inverse are
\[
 (X,Y,Z,T)=(x+z,y+z,z,T),\qquad
 x=X-Z,\quad y=Y-Z,\quad z=Z.
\tag{20}
\]
Its exact degrees are \((1,1,1,2)\), so its Euler field is
\(D_0=D_R+2T\partial_T\). Entire commutators give
\[
 [E_0,D_0]=-H+(2-2x^3y)\partial_T,
 \quad \operatorname{ad}_{E_0}^2D_0=-x^5\partial_T,
 \quad \operatorname{ad}_{E_0}^3D_0=0.
\tag{21}
\]
The last identity gives shift at most two directly from
\([E_0^j,D_0]=j[E_0,D_0]E_0^{j-1}
 +\binom j2\operatorname{ad}_{E_0}^2D_0 E_0^{j-2}\),
with the second term omitted for \(j=1\).
The actual polynomial
\[
 I_0=x^4T-x^2z(1+x^3y)+x^5z^2/2
\tag{22}
\]
satisfies
\(E_0I_0=0\), \(E_0^2(D_0I_0)=-x^9\ne0\), and
\(E_0^3(D_0I_0)=0\). Therefore \(\delta_{E_0}(D_0)=2\).

Now take \(t=T+z^3\), with inverse \(T=t-z^3\). The new frame
\((X,Y,Z,t)\) has exact degrees \((1,1,1,3)\), and
\[
 E=H+(1+x^3y+3x^2z^2)\partial_t,
 \qquad D_1=D_R+3t\partial_t.
\tag{23}
\]
The uniform witness (15) is, in this case,
\[
 I_1=x^6t-x^4z-x^7yz+x^7z^2/2-x^6z^3,
 \qquad EI_1=0,
 \qquad E(D_1I_1)=4x^6\ne0.
\tag{24}
\]
The next derivative is zero, and the uniform upper bound proves
\(\delta_E(D_1)=1\). Both coordinate transformations are explicit
polynomial automorphisms, and both degrees and shifts have been
verified on the whole polynomial rings.

This changes the degree sum from five to six. Thus the example
does not lower the lexicographic complexity consisting of degree
sum followed by Euler shift. It is not a descent step for a
globally degree-minimizing frame. The example is already sliced:
\(E_0(T-xy^2/2)=1\), and \(T-xy^2/2\) is itself an elementary
coordinate. It is a frame-dependence control, not an unrecognized
kernel or a negative cancellation example.

## 7. Verification and status

The proof is uniform and uses the highest Leibniz coefficient,
the exact homogeneity commutator, and a finite telescoping sum.
Fresh unsaved algebra independently checked the full cleared
antiderivative identity at arbitrary formal successive derivatives
through orders zero to six, the complete before-and-after fields
and invariants, and the \(qN=1,\psi=0\) edge. Those checks
support, rather than replace, the displayed all-order proofs.
No saved checker was executed, imported, or compiled, and no
canonical file was edited.

This is a focused elementary gauge mechanism with explicit limits.
It makes no priority claim for gauge conjugacy, local-slice
integration, or the LND degree identities. The held source is
offered for independent review after complete author EOF review
and final hash handoff, not as an assertion of general recognition.
