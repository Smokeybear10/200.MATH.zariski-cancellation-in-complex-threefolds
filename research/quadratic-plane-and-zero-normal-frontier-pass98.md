# Parallel planes and the zero-normal quadratic restriction

Two remaining sectors of the supplied quadratic cancellation frame
admit stronger necessary conditions. In a mixed double/simple fiber,
a nonzero speed-map normal forces both components to be collapsed
and gives two parallel planes in the original four-space. At a
collapsed double component with zero first normal action, the
quotient conormal row has degree at most two and a constant
transverse quadratic coefficient.

Neither result excludes all fixed fibers or recognizes the kernel
as a polynomial three-ring. The corrected complex-threefold
cancellation question remains unresolved here, as does the
reduction from an arbitrary sliced action to this special frame.
The intended correction and field in Luo's email remain unconfirmed.

## 1. The supplied frame and the existing frontier

The hypotheses include actual polynomial coordinates, not only a
relative presentation or a formal local model:
\[
\begin{gathered}
B=\mathbb C[x_1,x_2,x_3,z]=A[u],\qquad E=\partial_u,
\qquad u=Ez/q,\quad E^2z=q\in\mathbb C^*,\quad E^2x_i=0,\\
S=\ker(N|_A)=\mathbb C[s_1,s_2],\qquad
\mathbf b=(Ex_1,Ex_2,Ex_3)^t\in S^3,\\
L=\mathbf b_{s_1}\times\mathbf b_{s_2},\qquad
\Omega=L\cdot\mathbf b\ne0,\qquad
A=S[A_1,A_2,c],\quad A_{\operatorname{Frac}S}=\operatorname{Frac}(S)[v].
\end{gathered}
\tag{1}
\]
Here N is the specified primitive canonical Jacobian LND of the
retained frame. Its extension kills u and commutes with E.
The actual generic degrees of A_1,A_2,c are at most 2,2,4.
The additional smoothness, factoriality, contractibility,
faithful flatness, full-kernel, and actual prime-divisor hypotheses
are retained exactly as in [checkpoint97](checkpoint-pass97-working.json).

The [source-balance theorem97](quadratic-saturated-source-balance-pass97.md)
excludes every closed fiber of total multiplicity four. All reduced
components are disjoint entire affine lines. A fiber containing a
fixed component has only profile (2) or (2,1), where the entries are
the generic scheme multiplicities of the whole fiber.
The [weighted defect theorem97](quadratic-weighted-rank-defect-pass97.md)
makes every admissible relative-linear projection on a total-three
fiber have generic degree four and special dimension three. Its
local base-change module is nonfinite. Nothing below reverses that
nonfiniteness or uses a hypothetical finite cover as an actual one.

## 2. A mixed fiber with nonzero speed normal

Let \(\mathfrak m\subset S\) support a (2,1) fiber with fixed
double component C_2 and simple component C_1. Suppose
\(L_0=L(\mathfrak m)\ne0\). The double component is already
collapsed by the retained compatibility theorem: both relative
good generators A_i restrict to constants on it.

The actual volume relation
\(\Omega h=(L\cdot v_2)A_1+(L\cdot v_3)A_2-\kappa\)
specializes to a nonzero affine-linear equation in A_1,A_2.
Indeed \(\Omega(\mathfrak m)=0\), because N is free on
\(A_\Omega\), while \([\mathbf b,v_2,v_3]\) remains invertible.
Thus the equation cuts out a good line through the constant good
point of C_2.

If C_1 were noncollapsed, its affine good projection would be
that whole line and would attain the good point of C_2. Its full
relative line would then meet the vertical line C_2. This contradicts
disjointness in the actual relative closed embedding. Hence both
components are collapsed.

Their cylinders are therefore distinct parallel affine planes.
There is a constant affine change of the original good coordinates
to \(\ell,Y,W\), with component ideals and speeds
\[
\begin{gathered}
B=\mathbb C[\ell,Y,W,z],\qquad
\mathfrak q_2B=(\ell,Y),\qquad
\mathfrak q_1B=(\ell,Y-1),\\
\ell=L_0\cdot x_{\rm tr}-\kappa(\mathfrak m),\qquad
E\ell=L_0\cdot\mathbf b\in\mathfrak m^2\setminus\{0\},
\qquad E^2\ell=0,\\
F=\ell-uE\ell,\qquad G=Y-uEY,\\
\mathfrak q_2=(F,G),\qquad
\mathfrak q_1=(F,G-1),\qquad
\sqrt{\mathfrak mA}=(F,G(G-1)).
\end{gathered}
\tag{2}
\]
The last line follows by evaluating the actual cylinder at u=0
and using comaximality. It gives global component generators in A,
not ambient coordinates of A. It describes the radical, not the
whole nonreduced fiber ideal. The nonzero speed in (2) expressly
prevents interpreting \(\ell\) as an E-invariant coordinate.

The [complete plane proof](quadratic-normal-companion-collapse-pass98.md)
does not require any hypothesis on the first normal action of N.
It leaves the sector \(L(\mathfrak m)=0\) untreated.

## 3. Zero first normal action at a collapsed double component

This second result applies to a collapsed double component of
either profile (2) or (2,1), independently of the value of L.
Let \(\mathfrak q=(F,G)\) be its actual centered ideal and assume
\(N(\mathfrak q)\subset\mathfrak q^2\). A constant base change
gives centered coordinates x,f on S with
\[
\begin{gathered}
x\equiv p(c)F+q(c)G\pmod{\mathfrak q^2},\qquad f\in\mathfrak q^2,
\qquad (p,q)\mathbb C[c]=\mathbb C[c],\\
f\equiv Q_2(c;F,G)\pmod{\mathfrak q^3},\qquad
\mathcal A:=Q_2(c;-q(c),p(c))\in\mathbb C^*,\\
\deg p\le2,\qquad\deg q\le2.
\end{gathered}
\tag{3}
\]
The polynomial q(c) in this row is unrelated to the nonzero
constant acceleration q in (1).

The constant-coefficient assertion is an all-point argument.
The entire component thickening is free of rank two over the
actual subring \(\mathbb C[c]\). A transverse section c=c_0
therefore has length two at every point of the component.
After eliminating the nonzero linear row of x, the quadratic
coefficient of f cannot vanish. This coefficient is precisely
\(Q_2(c_0;-q(c_0),p(c_0))\), including charts where p vanishes.
A complex polynomial without a zero is a nonzero constant.

At the generic point, take y=G on a chart with p nonzero.
Assign weights two and one to x and y. The exact volume ratio
gives a constant \(\nu\ne0\), and the weighted leading operator is
\[
\begin{gathered}
a=\mathcal A/p^2,\qquad
D_*=-\nu p a' y^2\partial_y+2\nu p a y\partial_c,\qquad
v=y/p(c),\\
D_*v=D_*x=0,\qquad D_*c=2\nu\mathcal A v,\\
F_*=-q(c)v,\qquad G_*=p(c)v,\qquad
D_*^3F_*=D_*^3G_*=0.
\end{gathered}
\tag{4}
\]
The actual identities \(N^3F=N^3G=0\) give the final line.
In the translated variables they force \(p'''=q'''=0\).
No local-nilpotence claim on the coefficient field or completed
local ring is needed. The actual identity \(N^5c=0\) is not used.

Up to a constant row change and an affine change of c, the
polynomial row span is one of
\[
\operatorname{span}\{1\},\quad
\operatorname{span}\{1,c\},\quad
\operatorname{span}\{1,c^2\},\quad
\operatorname{span}\{c,c^2+1\}.
\tag{5}
\]
This classifies the indicated conormal data, not the full actions.
The [complete zero-normal proof](quadratic-zero-normal-row-pass98.md)
retains the whole-thickening and global-volume hypotheses at each step.

## 4. Why the leading translation does not finish recognition

On a separate polynomial three-ring, the primitive triangular LND
\(N_0=-x^2\partial_y+2y\partial_c\) has kernel
\(\mathbb C[x,y^2+x^2c]\), double fiber ideal \((x,y^2)\),
and zero first normal action at \((x,y)\). It satisfies
\(N_0^3x=N_0^3y=N_0^5c=0\), but
\(N_0^2c=-2x^2\ne0\). Its weighted leading field is
\(2y\partial_c\), whose square does kill c.

This control rules out lifting \(D_*^2c=0\) to \(N^2c=0\)
without a further argument. It is not a realization of the
specified original nonconical frame or its highest-adjoint kernel,
and so is not a counterexample to the restricted problem.

The new plane equations likewise do not imply N-invariance of F or G.
They are E-invariant by their construction as elements of A.
A global coordinate or recognition result must use additional
information from the actual four-coordinate action. Eliminating
this supplied frame would still leave the arbitrary-frame reduction.

## 5. Literature boundary

The available nice-derivation result over a principal ideal domain
requires an actual polynomial three-ring over that domain. Its
four-variable corollary requires an invariant coordinate and
square-zero derivatives of the other three coordinates. Those are
not the hypotheses in (1).[^nice] The older scope audit is retained
in [the rank-one source note85](rank-one-quasi-nice-source-scope-pass85.md).

A separate lead concerns Pascal-finite automorphisms. For the
actual time-one map \(\Phi_1\), direct calculation gives
\((\Phi_1^*-1)^3(x_1,x_2,x_3,z)=0\). This is a difference-operator
statement, not a spatial polynomial-degree bound. Adamus and
Hajto's Theorem 5.1 runs from strong nilpotence to Pascal finiteness;
Remark 5.2 obstructs the reverse implication in general. It does
not recognize the invariant ring of this sliced action.[^pascal]
Thus this lead supplies no closing theorem here. This is a bounded
applicability check, not a comprehensive novelty clearance.

## 6. Verification and remaining work

The [canonical exact capture](verification-pass98-working.json)
passes one symbolic method. Its coverage is weighted row identities,
a cubic-row negative, a chart at which p vanishes, and the intrinsic
control above. It does not certify the universal geometric proofs.
The [proof audit](proof-audits-pass98-working.md) records separate
AI reconstructions, with no human review or Lean certificate.

~~~sh
/opt/anaconda3/bin/python -m unittest -v research.quadratic_zero_normal_checks_pass98
~~~

The next mathematical task is to combine the exact common-plane
equations with the original velocity Jacobian and the zero-normal
row forms. Any resulting restriction must be checked on both the
simple and double components. Spatial divisibility, a leading
identity, or a relation in a generic localization is insufficient
by itself to produce a global coordinate.

The nonzero-first-normal branch, whole collapsed and noncollapsed
double fibers, and mixed fibers with L=0 remain in scope. No
existence, exclusion, full recognition, historical novelty, expert
endorsement, or publication is asserted. The bookkeeping snapshot
is [checkpoint98](checkpoint-pass98-working.json).

## Sources

[^nice]: Nikhilesh Dasgupta and Neena Gupta,
    [Nice derivations over principal ideal domains](https://arxiv.org/pdf/1701.03635),
    arXiv:1701.03635v1, January 13, 2017, Theorem 3.6 and Corollary 3.8.

[^pascal]: Elżbieta Adamus and Zbigniew Hajto,
    [Strongly nilpotent automorphisms are Pascal finite](https://arxiv.org/html/2604.11693v1),
    arXiv:2604.11693v1, April 13, 2026, Definition 4.1, Theorem 5.1
    and Remark 5.2. Earlier dependencies cited there have not all
    been newly reconstructed for this note.
