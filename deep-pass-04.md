# All vertical coefficients for one rank-three derivation

September 12, 2026. Private working research note.

## Executive summary

This pass gives a complete working proof of a restricted theorem: every
polynomial vertical extension of the specified Freudenburg derivation has a
slice exactly when its coefficient is a nonzero constant plus a polynomial
derivative. The coefficient may be any polynomial in three variables, with
no degree restriction. In every positive case the invariant ring has explicit
polynomial coordinates.

This is not a proof of the professor's full cancellation conjecture. The
working interpretation of that conjecture is

\[
X\times_{\mathbb C}\mathbb A^1\simeq\mathbb A^4
\quad\Longrightarrow\quad X\simeq\mathbb A^3.
\]

The intended field and dimension have not been confirmed by the professor.
The general characteristic-zero question remains open in the recent primary
literature checked for this investigation.[^1] The theorem below classifies
one family of derivations, not every possible cancellation example.

The key advance over the previous pass is an argument that handles arbitrarily
high powers of a denominator. It combines a polynomial-degree inequality with
formal branches and a finite Newton-polygon calculation. A tempting earlier
version omitted higher-order contributions from some branches; the final
argument includes those contributions explicitly.

Status: complete working derivation, model cross-review, and exact supporting
computations. Originality is unestablished. No expert review, public submission,
or Lean formalization has occurred. The finite tests do not formally verify
the quantified theorem.

## 1. Precise theorem

Let \(k\) be a characteristic-zero field and \(R=k[x,y,z]\). Put

\[
f=xz-y^2,\qquad
g=zf^2+2x^2yf+x^5,\qquad
r=-x^3-fy,
\]

and define \(\Delta(h)=\operatorname{Jac}(f,g,h)\). This is the standard
homogeneous rank-three example discussed by Dasgupta and Gaifullin, following
Freudenburg.[^2] For any \(a\in R\), extend it to

\[
E_a=\Delta+a\partial_w\quad\text{on }R[w].
\]

A **slice** is a polynomial \(s\) satisfying \(E_a(s)=1\). It gives a
product decomposition \(R[w]=(\ker E_a)[s]\). The slice theorem and finite
exponential constructions are standard tools, not discoveries of this
investigation.[^3]

**Working theorem.** For every \(a\in R\), the following are equivalent:

1. \(E_a\) has a polynomial slice.
2. \(a=c+\Delta H\) for some \(c\in k^*\) and \(H\in R\).

In these cases \(\ker E_a\cong k^{[3]}\), with explicit generators.

There is a stronger equivalent condition: the additive-group action generated
by \(E_a\) is proper. Section 4.4 explains why the negative proofs establish
nonproperness, not just absence of a slice.

The implication from 2 to 1 is immediate: set \(s=(w-H)/c\). In the
coordinates \((x,y,z,s)\), the derivation is \(\Delta+\partial_s\).
For \(v=x,y,z\), define

\[
v^*=\sum_{j\ge0}\frac{(-s)^j}{j!}\Delta^j(v).
\]

Each sum is finite. These are invariant, and the inverse finite flow recovers
\(x,y,z\) from \(x^*,y^*,z^*,s\). Thus
\(\ker E_a=k[x^*,y^*,z^*]\).

**Immediate corollary.** If \(\deg a\le4\), a slice exists exactly when
\(a\) is a nonzero constant. Indeed, \(\Delta\) raises ordinary total
degree by four, and its derivative of a nonconstant homogeneous polynomial
is either zero or has degree at least five.

## 2. Structural identities and the obstruction used throughout

The exact identities are

\[
\begin{aligned}
\Delta x&=2fr, &\Delta y&=-g-6x^2r,
&\Delta z&=2xf^2-10xyr,\\
\Delta f&=\Delta g=0, &\Delta r&=fg,
&r^2+f^3&=xg.
\end{aligned}
\]

Furthermore,

\[
\ker\Delta=k[f,g],\qquad
\Delta R\cap k[f,g]=fg\,k[f,g],
\qquad R_{fg}=k[f^{\pm1},g^{\pm1},r].
\]

The last description follows from
\(x=(r^2+f^3)/g\), \(y=-(r+x^3)/f\), and
\(z=(g+2rx^2+x^5)/f^2\). Thus points with common nonzero \(f,g\)
are on the same orbit, whose time difference is the difference in \(r\)
divided by \(fg\). The global kernel and plinth arguments are documented in
[the lifting note, under “The plinth ideal underlying the invariant-coefficient criterion”](research/lifting-route.md).
The first-pole argument and the independent polynomial-primitive criterion
appear in [the previous complete derivation, Sections 3–4](deep-pass-03.md).
For the higher-pole proof below, only the weaker fact \(f^m\notin\Delta R\)
is needed: that primitive criterion excludes it because
\(L^{-1}(f^m)=f^m/g\) has a genuine \(g\) denominator. Thus this dependency
does not use the extension classification being proved.

The fundamental obstruction is simple. Suppose a valued extension of \(k\)
has two points with all four coordinates in its valuation ring, joined by the
\(E_a\)-flow at a time \(T\) of negative valuation. A polynomial slice would
give

\[
s(p_1)-s(p_0)=T.
\]

The left side is integral and the right side is not. Therefore no slice
exists. This argument applies to every polynomial slice, regardless of its
degree. It is not a conclusion drawn from failure of a bounded search.

## 3. Every possible slice first reduces to a denominator in \(f\)

Assume a slice exists. On the fixed line \(x=y=0\), its equation implies

\[
a(0,0,z)=c\in k^*.
\]

Let \(C=k[x,f,g]\) and
\(L(P)=gP+2(xg-f^3)P_x\). The canonical decomposition proved previously
localizes to

\[
R_f=C_f\oplus rC_f,\qquad
C_f=L(C_f)\oplus k[f,f^{-1}][x].
\]

Consequently

\[
a=A_0(x,f)+\frac{\Delta K}{f},\qquad
K\in R_f,\quad A_0\in k[f,f^{-1}][x].
\tag{1}
\]

To determine \(A_0\), take endpoints \((0,e,Q)\), \((0,-e,Q)\).
They share \(f=-e^2\), \(g=Qe^4\), and their orbit time is
\(2/(Qe^3)\). At normalized time \(u\), put \(v=u^2-u\). The orbit is

\[
\begin{aligned}
x(u)&=4e^2v/Q,\\
y(u)&=e(1-2u)+64e^4v^3/Q^3,\\
z(u)&=Q+32e^3(1-2u)v^2/Q^2+1024e^6v^5/Q^5.
\end{aligned}
\]

The average \(J_a=\int_0^1a(x(u),y(u),z(u))du\) is a Laurent polynomial
in \(Q\), with coefficients in \(k[e]\), and \(J_a\equiv c\pmod e\).
If it had a negative \(Q\) power, multiplying by the smallest clearing
power of \(Q\) would give a polynomial over \(k[[e]]\) with nonzero
constant coefficient and a unit middle coefficient. At least one of its
nonzero roots in a finite valued extension is integral: if all roots had
negative valuation, factorization by their reciprocals would make every
nonconstant coefficient have positive valuation.

At that root the fourth-coordinate displacement is zero, both endpoints
are integral, and the time has a pole. This is impossible. Therefore
\(J_a\) has no negative powers of \(Q\).

Write \(A_0=\sum a_j(f)x^j\). Its negative-power moment coefficients are
exactly

\[
\gamma_j a_j(-e^2)e^{2j}Q^{-j},\qquad
\gamma_j=\frac{4^j(-1)^j(j!)^2}{(2j+1)!}\ne0.
\]

The other terms contribute only positive powers of \(Q\), or average to
zero by reflection. Hence \(a_j=0\) for \(j>0\). The constant coefficient
of \(J_a\) then shows \(a_0\in k[f]\), with \(a_0(0)=c\).

A nonconstant \(a_0\) would have a nonzero root \(\alpha\) after extending
the field. On \(f=\alpha\), the rational shear in (1) is polynomial and
turns the action into the base action with a fixed fourth variable. A slice
would descend to the base surface. But its \(g=0\) fiber consists of two
affine lines, whereas a slice would make every fiber one affine line.
Therefore \(a_0=c\). Clearing powers of \(f\) in (1) gives

\[
a=c+\frac{\Delta H}{f^m},\qquad H\in R,\quad m\ge0.
\tag{2}
\]

The full normal-form and fiber justifications appear in
[the proof appendix, Section 5](research/arbitrary-coefficients-pass.md).

## 4. Removing every higher pole

The previous first-pole theorem handles \(m=1\): a slice forces the pole
to be removable by an invariant correction. For completeness, its residue
criterion is \(H\bmod f\in k[x^5]\); its proof uses paired fifth-root
branches at a nonzero value of \(g\), with exact cancellation of the leading
fourth-coordinate pole.

For general \(m\), \(\Delta H\in f^mR\) implies
\(H\bmod f=h(x)\), because the induced kernel modulo \(f\) is \(k[x]\).
If \(h\in k[x^5]\), subtract the corresponding invariant polynomial in
\(g\) and divide \(H\) by \(f\), lowering \(m\). It remains to exclude
\(m\ge2\) with \(h\notin k[x^5]\).

### 4.1. A degree bound

Write \(H=\sum H_D\) in ordinary homogeneous components. Divisibility by
\(f^m\), whose degree is \(2m\), makes every component with
\(D<2m-4\) invariant. At equality a nonzero derivative would be a scalar
multiple of \(f^m\), forbidden by the independent polynomial-primitive
criterion just described. Equivalently, it is excluded by the plinth ideal
\(fgk[f,g]\).
Subtract these invariant components. Every remaining monomial satisfies

\[
D>2m-4. \tag{3}
\]

The residue remains outside \(k[x^5]\).

### 4.2. Exact branches, including their corrections

Fix a primitive fifth root \(\zeta\). Let \(\phi(U)\) be the formal unit
with \(\phi(0)=1\) satisfying

\[
\phi(U)^6-\phi(U)+U=0.
\]

It exists by recursive coefficient comparison, since the derivative at 1
is 5. Put \(U=F^3/B^6\) and

\[
X_0=B\phi(U),\qquad
X_1=\zeta B\phi(\zeta^{-1}U),\qquad
p_i=(X_i,0,F/X_i).
\]

Both points have \(f=F\), \(g=B^5\), and \(r_i=-X_i^3\).
For a monomial \(x^iz^j\) in \(H(x,0,z)\), let \(l=i-j\) and expand
\(\phi(U)^l=\sum q_{l,n}U^n\). Its endpoint difference contributes

\[
q_{l,n}(\zeta^{l-n}-1)B^{l-6n}F^{j+3n}.
\]

Set \(L=l-6n\), \(J=j+3n\), and collect equal terms. Then

\[
H(p_1)-H(p_0)=\sum d_{J,L}B^LF^J,
\qquad L+2J=D>2m-4. \tag{4}
\]

Only finitely many terms have \(J<m-1\). At least one is nonzero: the
\(J=0\) part is \(h(\zeta B)-h(B)\).

Including all \(n\) in this expansion matters. A raw exponent divisible
by five does not justify discarding the monomial: later branch corrections
can contribute. Equation (4) retains them while preserving the degree bound.

### 4.3. Select an exact leading balance

For the nonzero terms with \(J<m-1\), define

\[
q=\min\frac{L+2}{m-1-J}=\frac MN>2,
\qquad B=t^N,\quad F=t^M V.
\]

The inequality follows from (3). All branch expansions now converge
\(t\)-adically since \(M>2N\). Zero fourth-coordinate displacement is
equivalent to

\[
\mathcal E=H(p_1)-H(p_0)
 +cF^{m-1}\frac{r_1-r_0}{B^5}=0.
\]

After division by \(t^{(m-1)M-2N}\), its reduction at \(t=0\) is

\[
P(V)=c(1-\zeta^3)V^{m-1}
 +\sum_{NL+MJ=(m-1)M-2N}d_{J,L}V^J. \tag{5}
\]

The sum has at least one nonzero term and has degree below \(m-1\).
There is no hidden same-degree cancellation: coefficients were collected,
and a fixed \(J\) determines \(L\) on this edge. All terms with
\(J\ge m-1\) have strictly higher order, since their excess order is

\[
N(D-2m+4)+(J-m+1)(M-2N)>0.
\]

Thus (5) has a nonzero root \(V_0\) over an algebraic closure. After
factoring out its smallest power of \(V\), it is a positive-degree
polynomial with nonzero constant coefficient.

The root might be multiple. Ordinary simple-root Hensel lifting is not
sufficient. After base change to an algebraic closure of \(k\), apply
formal Weierstrass preparation at
\(V=V_0+Y\): the normalized equation is a unit times a monic distinguished
polynomial in \(Y\) over \(k[[t]]\). A root of that polynomial in a finite
valued extension has positive valuation. Hence \(V\) remains a unit and
the exact equation \(\mathcal E=0\) holds. The complete-local preparation
theorem applies without a simple-root hypothesis.[^4]

The two endpoints are integral: \(X_i\) has valuation \(N\), and
\(F/X_i\) has valuation \(M-N\). But their time difference is

\[
T=\frac{r_1-r_0}{FB^5},\qquad
\operatorname{val}(T)=3N-M-5N=-M-2N<0.
\]

The fourth displacement is zero by construction. The integral-endpoint
obstruction contradicts a slice. This removes every nonremovable higher
pole, completing the working theorem.

### 4.4. Properness is equivalent to the same criterion

Here properness concerns the action morphism
\((t,p)\mapsto(p,\exp(tE_a)p)\). Integral endpoints joined at a
nonintegral time violate its valuative criterion for properness.[^6]
Thus all of the paired-orbit obstructions above exclude properness directly.
A proper action also has no fixed points, since a fixed point would give the
nonproper group \(\mathbb G_a\) as a fiber of its action morphism.

Only the nonconstant \(f\)-remainder case requires an additional explicit
check. On its invariant fiber \(f=\alpha\ne0\), the shear used in Section 3
makes \(w\) fixed. Choose \(v^2=-\alpha\), and let \(G\) tend formally to
zero. The points

\[
(0,v,G/\alpha^2,0),\qquad(0,-v,G/\alpha^2,0)
\]

have common \(f=\alpha\), \(g=G\), and time difference \(2v/G\).
Their coordinates are integral and the time has a pole. Properness is
preserved on a closed invariant fiber, so the original action cannot have
been proper. Consequently the entire necessary-condition proof works with
properness in place of the slice assumption.

Conversely, the explicit positive coordinates identify every gauge case with
a translation. Its action morphism is a closed immersion and hence proper.
Therefore, for this fixed family,

\[
\text{proper action}\iff\text{polynomial slice}
\iff a\in k^*+\Delta R.
\]

## 5. Controls against misleading generalizations

The constant-plus-derivative criterion is specific to the stated base.
For example,

\[
E=x^2\partial_y+(1+xy)\partial_w
\]

has the nonlinear polynomial slice

\[
s=w+y^3/2+xy^4/8-xyw-x^2y^2w/2+x^3w^2/2,
\]

although \(xy\notin x^2k[x,y]\). The action still has polynomial kernel;
an explicit exponential automorphism exhibits its coordinates. The
[appendix](research/arbitrary-coefficients-pass.md) proves a general
conjugation identity explaining this construction.

There is also a nongauge extension with an affine-in-\(w\) slice over
the nonpolynomial Danielewski surface \(xy=z^2-1\). It reconstructs the
classical isomorphism between its cylinder and the cylinder over
\(x^2Y=Z^2-1\). These surfaces belong to the established Danielewski
cancellation examples.[^5] The explicit maps and their polynomial inverses
are recorded and checked here. They are not counterexamples to cancellation
of affine space.

These controls explain why the proof must use the fixed base's homogeneity,
invariants, and branch geometry. Freeness or the existence of a rational
primitive alone does not justify the theorem.

## 6. Verification, originality, and the actual remaining problem

The companion files distinguish three tasks:

- [The proof appendix](research/arbitrary-coefficients-pass.md) supplies the
  all-degree arguments, including affine slices, denominator reduction, and
  the complete higher-pole proof.
- [Exact identity checks](verify_nonlinear.py) verify polynomial inverse maps,
  derivative identities, and explicit second-pole witnesses using rational
  arithmetic. Additional higher-pole checks test the branch expansions.
- [The global bridge audit](research/global-bridge-pass.md) identifies which
  extra structural hypotheses would be needed to apply positive cancellation
  theorems to an arbitrary slice derivation.

The implemented [exact classifier](research/full_coefficient_classifier.py)
is finite because \(\Delta\) is homogeneous:
for \(\deg a=d\), testing \(a-c\in\Delta R\) only requires homogeneous
primitive components of degree at most \(d-4\). This bound is a consequence
of the grading, not an experimental cutoff on the slice degree.

Reproduction commands, using the tested local SymPy environment:

```sh
/opt/anaconda3/bin/python research/full_coefficient_classifier.py --self-test
/opt/anaconda3/bin/python research/full_coefficient_classifier.py '1+2*f*r'
/opt/anaconda3/bin/python research/full_coefficient_classifier.py '1+3*g*x-2*f**3'
python3 verify_nonlinear.py
python3 verify_higher_poles.py
python3 verify_outside_coefficients.py
```

The positive example returns \(H=x\), \(s=w-x\), with both derivative
residuals zero. The formerly difficult negative example is now a complete
six-unknown, 28-equation image calculation. The earlier 4,845-unknown slice
search was only a degree-bounded exclusion. The new conclusion is stronger
because of the theorem, not because a larger search was run.

All 107 test methods across the project pass, including the earlier baseline
checks. Some methods contain finite grids; this is not 107 independent proofs.
The higher-pole checker uses independently implemented rational/cyclotomic
arithmetic, verifies formal branches through \(U^{11}\), and checks the
previously missed branch correction as a negative control. It does not
machine-verify the universal Weierstrass lifting step. The classifier rejects
executable input syntax and reports `unknown` if its matrix-work limit is
exceeded. Exact test counts and calculation scopes are recorded in
[the experiment manifest](experiment-manifest.json).

The targeted literature audit checked the specified rank-three example,
extension theorems, image-of-derivation results, proper-action theorems, and
Danielewski cylinder constructions. The extension theorem in Freudenburg's
fundamental-pair paper imposes extra structure and does not directly assert
the unrestricted coefficient classification above.[^3] Search failures do
not establish originality. A comprehensive thesis, MathSciNet, zbMATH, and
citation audit has not been completed. The reproduced Danielewski formulas
must not be marketed as a discovery.

The next global gap is precise: an arbitrary slice derivation on
\(\mathbb C^{[4]}\) has not been shown to admit a coordinate presentation
\(\delta+a\partial_w\), let alone one with this particular \(\delta=\Delta\).
Even a classification for every vertical coefficient of this one base does
not supply that reduction. No such theorem may be assumed.

Before external use, a qualified reader should reconstruct Sections 3 and 4,
check the first-pole dependency, and audit the originality of the resulting
restricted theorem. Separate model critiques are not independent human
review. No publication claim, professor email, or submission has been made.

## Sources

[^1]: Sergey Gaifullin and Mikhail Petrov, [*Non-cancellative varieties, maximal tori, and the Makar-Limanov invariant*](https://arxiv.org/html/2607.13593v1), arXiv:2607.13593v1, July 2026. Used for the source-version-specific status of characteristic-zero affine-space cancellation, not as a proof of the new working theorem.
[^2]: Nikhilesh Dasgupta and Sergey A. Gaifullin, [*On locally nilpotent derivations of polynomial algebra in three variables*, Section 5](https://arxiv.org/html/2306.00510). Used for the standard rank-three example and its established context. The identities and restricted extension arguments have separate local reconstructions.
[^3]: Gene Freudenburg, [*Actions of SL₂(k) on affine k-domains and fundamental pairs*, Section 2.2 and Sections 7–8](https://arxiv.org/html/2108.12021). Used for standard slice/localization tools and the precise distinction between fundamental-derivation extensions and the family studied here.
[^4]: Jesse Elliott, [*Factoring formal power series over principal ideal domains*, Theorem 1.3 and its proof](https://arxiv.org/html/1107.4860v4), arXiv version dated June 26, 2012. Apply with coefficient ring \(k[[t]]\), ideal \((t)\), and variable \(Y=V-V_0\).
[^5]: Lucy Moser-Jauslin and Pierre-Marie Poloni, [*Isomorphisms between cylinders over Danielewski surfaces*, Sections 2.2 and 5.1](https://arxiv.org/html/2002.12202v1). The cylinder phenomenon and associated construction are known prior work.
[^6]: The Stacks Project, [Valuative criterion for properness, Tag 0BX5](https://stacks.math.columbia.edu/tag/0BX5). Used for the necessary lifting condition on the finite-type action morphism.
