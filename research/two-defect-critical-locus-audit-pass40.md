# Independent audit of the two-defect critical-locus controls

The complete [proof note](two-defect-critical-locus-pass40.md) was read
and independently reconstructed. No mathematical or scope correction
was found. The obstruction concerns the prescribed leading module,
not cancellation or all choices of frame.

## 1. Actual polynomial actions and both height notions

The supplied identity \(\alpha f+\beta g=1\) gives both inverse
compositions for
\(s=\alpha a+\beta c\), \(r=ga-fc\). In particular the
kernel is really \(\mathbb C[u,v,r]\). The separate quadratic
physical-coordinate change also has the stated two-sided inverse.

Differentiating the physical inverse gives the four actual partials.
Their commutators reconstruct (8), including the factors \(2f\)
and \(2g\) and both signs in the first commutators. The determinant
of the two highest bad columns in their last two rows is
\(4fg\det\operatorname{Jac}(f,g)\), so assumption (9) gives
independence. The next commutators vanish because all highest fields
fix \(u,v\) and have coefficients in that plane.

When both displayed \(\Delta\)'s are nonzero, the highest
coefficients act nontrivially on the invariant \(r\). This attains
the horizontal degree, not merely a possibly shifted vertical degree.
The exact slice-filtration profile is therefore also \((1,1,2,2)\).
The independent checker computes these shifts from the transformed
coefficients on \((u,v,r,s)\), rather than inferring them only from
the iterated brackets.

## 2. The entire leading ideal and its four reduced points

Direct application to \(r\) gives the intrinsic coefficients
\[
\Delta_u,\quad\Delta_v,\quad-2f\Delta_u,\quad-2g\Delta_v.
\]
Thus all four generate exactly \((\Delta_u,\Delta_v)\), also
after extending to \(\mathbb C[u,v,r]\). The proof correctly
distinguishes plane-coefficient combinations, which are LNDs, from
arbitrary kernel-coefficient combinations, which need not be.

For \(f=u^2+v^2\), \(g=uf-1\), the direct differential calculation
is
\[
\Delta_u=f^2+2u,\qquad \Delta_v=2v,
\qquad\det\operatorname{Jac}(f,g)=-2vf.
\]
The scalar gcd is one: any common prime factor must divide \(v\),
but \(v\) does not divide the first generator. This does not make
the ideal the unit ideal. Its exact lexicographic Groebner basis is
\[
u^4+2u,\quad v.
\]
In particular it is proper, including because both generators vanish
at \((0,0)\), and the quotient has complex dimension four. The
polynomial \(u^4+2u\) is squarefree: its derivative is 2 at zero
and is \(-6\) modulo \(u^3+2\). Equivalently its gcd with the
derivative is one. Over \(\mathbb C\), this proves exactly four
reduced points without numerical root approximations.

Extending this ideal to the invariant three-ring gives four disjoint
reduced \(r\)-lines. A member \(h\partial_r\) of the module is
nowhere zero only if the polynomial \(h\) is a nonzero constant.
That would put one in the ideal, which the quotient excludes. Thus
the nonvanishing failure persists after any polynomial module
combination. It is not a fixed locus of the original sliced action.

## 3. Repeated roots and the highest-field boundary

For \(f=p(u)\), \(g=vp(u)-1\), the exact ideal is
\((p',p^2)\). The univariate principal ideal has a factor of
order \(e-1\) at a root of \(p\) of multiplicity \(e\), and
is the unit ideal precisely for squarefree \(p\). This uses the
actual principal ideal in \(\mathbb C[u]\), not a multivariate
Bezout inference.

For \(p=u^N\), the physical highest vector field satisfies
\(Uu=u^{2N}\), so the stated nonzero iterate formula follows by
induction. The displayed identity involving \(p^2,g^2\) expands
to one using \(vp=g+1\). Hence the vector field is genuinely
non-LND even though its own coefficient ideal is the unit ideal.
This is a different ideal from the intrinsic leading ideal and
does not conflict with its fixed lines or divisorial zeros.

## 4. Independent exact checks

The standalone file
[two_defect_critical_locus_checks_pass40.py](two_defect_critical_locus_checks_pass40.py)
imports only `unittest` and `sympy`. It contains six methods covering
both coordinate inverses and the actual slice, both exact height
profiles and defect ranks, the full intrinsic ideal and signs, the
gcd-one proper ideal with four reduced points, individual repeated-root
orders, and the actual highest-field nonnilpotence/unit-ideal control.

The initial run was:

```text
/opt/anaconda3/bin/python research/two_defect_critical_locus_checks_pass40.py
Ran 6 tests in 0.196s
OK
```

No initial assertion failure or formula correction occurred. The
checker is frozen after this passing run. Its finite representatives
support the separately reconstructed all-polynomial and all-multiplicity
arguments; they do not prove a classification of arbitrary actions.

This is independent AI reconstruction and exact algebraic testing,
not expert review or a public novelty assessment. No existing proof,
registry, or top-level metadata was edited for this audit.
