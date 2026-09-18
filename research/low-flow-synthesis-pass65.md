# Low-flow recognition and the remaining rank-three case

The new conditional results reduce the low-flow part of the supplied
two-quadratic frame to a single explicitly stated rank configuration.
They do not solve unrestricted complex-threefold cancellation.
Higher-flow cases and the existence of a suitable frame remain separate.

## 1. Fixed problem and degree conventions

The working cancellation question is
\[
A[s_*]\simeq\mathbb C^{[4]}\quad\Longrightarrow\quad A\simeq\mathbb C^{[3]}.
\]
This corrects the dimension in the pasted conjecture and specializes
to the complex threefold case. The professor has not confirmed that
interpretation.

Transport \(\partial_{s_*}\) to a sliced polynomial LND \(E\) on
\(B=\mathbb C[x_1,x_2,X,Y]\), with \(A=\ker E\).
The supplied frame assumptions are
\[
\operatorname{ad}_E^2T_1=\operatorname{ad}_E^2T_2=0,\qquad
\operatorname{ad}_E^3T_X=\operatorname{ad}_E^3T_Y=0.
\tag{1}
\]
These are actual coordinate partials. Define the two defect fields
\(V_X=\operatorname{ad}_E^2T_X\), \(V_Y=\operatorname{ad}_E^2T_Y\),
the good tops \(W_i=[E,T_i]\), and
\[
d=\operatorname{rank}(V_X,V_Y),\qquad
m=\max\{j:E^j(x_1,x_2,X,Y)\ne0\},\qquad
q=\operatorname{rank}\{E,W_1,W_2,V_X,V_Y\}.
\tag{2}
\]
All field ranks are over \(\operatorname{Frac}B\).
The flow degree \(m\), defect rank \(d\), and joint rank \(q\)
are different quantities.

## 2. What is now recognized at low flow

The complete [dependent low-flow proof](dependent-low-flow-pass65.md)
uses both highest identities
\[
(0,0,a,b)h_m=0,\qquad (0,0,a,b)\operatorname{Jac}h_m=0
\]
when \(V_X=aD,V_Y=bD\) and \(a,b\) have no complex constant relation.
They force the bad components of \(h_m\) to vanish, without treating
\(a,b\) as constants under ordinary differentiation.
For \(m=1\), this makes \(X,Y\) actual invariant coordinates.

For \(m=2\), it makes \(f=EX,g=EY\) invariant. Algebraically independent
speeds are now recognized in the dependent-defect case: a transverse
bad projection supplies the actual graph of pass64, while a rank-one
projection gives a nice commuting good-output field and invokes the
existing exact recognition lemma.

The new [speed-curve graph proof](dependent-speed-curve-graph-pass65.md)
handles dependent speeds when the joint leading rank is at most two.
For a transverse bad projection, it uses a rational parameter \(u\)
for the speed curve and the basis \(v,v_u\), where \(v=(f,g)^t\).
Two exact Schur integrations produce a quadratic graph whose positive
coefficients all lie in \(k(u)\). Actual generation then supplies the
generic polynomial pair; the one-parameter pole argument yields
an actual invariant ambient coordinate or an explicit affine slice.
The rank-one-projection alternative is recognized separately by the
relative-plane and two-quasi classification gates.

The resulting low-flow map is:

| Case under the supplied frame | Current conclusion |
| --- | --- |
| Defects have a complex constant relation, including both zero | Recognized by the inherited constant-frame reduction. |
| Independent defects and \(m=2\) | Recognized by passes42–44 and64. The independent \(m=1\) alternative is excluded by the inherited companion theorem. |
| Dependent defects with no constant relation and \(m=1\) | Recognized by the new highest-column argument. |
| Dependent defects, \(m=2\), and algebraically independent bad speeds | Recognized by the new low-flow theorem. |
| Constant projective bad speeds, including constant or zero speeds | An actual invariant bad linear coordinate gives recognition. |
| Dependent defects, \(m=2\), nonconstant-projective rank-one speeds, \(q\le2\) | Recognized by the speed-curve graph theorem and its projection corollary. |
| Same speed-curve setting with \(q=3\) | Not recognized in full by this packet. Existing individual recognition criteria remain available. |

Thus any low-flow instance still outside the recognized cases must have
\[
\boxed{
d=1,\quad m=2,\quad
\operatorname{rank}\operatorname{Jac}(f,g)=1,\quad
[f:g]\text{ nonconstant},\quad q=3,
}
\tag{3}
\]
with no complex constant relation between the two defects.
This is a necessary residual list, not an existence statement.
It does not assert that individual rank-three instances cannot meet
another already established recognition criterion.

## 3. The independent constant-top cubic reduction

The [cubic normal-form proof](constant-top-cubic-pass65.md)
addresses the independent-defect boundary with constant \(E^3x\ne0\).
Its full six-dimensional companion has Jordan type \((3,3)\).
After constant changes within the good and bad pairs, either
an inherited recognition criterion applies, or there are actual
polynomials \(t,f\) satisfying
\[
\ker(E,V_X,V_Y)=k[t],\qquad
\ker(V_X,V_Y)=k[t,f],\qquad Et=0,\quad Ef=1,
\]
\[
E^2x=(f-F(t),U(t),1,0)^t,\qquad EX=f,\quad EY=G(t),
\tag{4}
\]
where \(U,G\) are nonconstant.
If \(t\) omits any nonzero constant ambient direction, the existing
rank-three commuting-action criterion recognizes the kernel.
The displayed \(t,f\) are not thereby ambient coordinates.

A [further coefficient audit](constant-top-cubic-heisenberg-pass65.md)
constructs the actual LND \(N=W_X+T_1/2\), with
\([E,N]=V_X/2\) central. The full good and bad coefficients force
\[
N(E^2x)=0,\qquad Nt=Nf=0.
\tag{5}
\]
The compatible-slice correction \(R=N-fV_X/2\) is a global LND
commuting with \(E\), but it supplies no fourth generic direction
and no slice through the parameter \(t\).

The initial proposal to use \(Nt\ne0\) for recognition is therefore
not a surviving subcase. It is ruled out by (5).
The corrected zero-motion result, rather than that vacuous proposal,
is the conclusion retained here.

## 4. A genuine moving-top control

The [explicit moving-frame family](moving-frame-divisibility-control-pass65.md)
starts from \(E=\partial_s-F(a)\partial_w\) on \(k[a,s,z,w]\),
with nonconstant \(F\), and the actual polynomial coordinates
\[
x_1=a-zw/3+w^4/24+s,\quad
x_2=a-zw/3+w^4/24-s,\quad
X=z-w^3/6,\quad Y=w.
\tag{6}
\]
The displayed note proves both polynomial inverse compositions.
It has exact adjoint profile \((1,1,2,2)\), independent defects,
flow degree four, and the canonical nonzero preceding bad vector.
Its canonical top parameter moves, \(T_cF=F'\ne0\), and
\(F\nmid T_\lambda F\). The natural moving repair is exactly zero.

This refutes automatic divisibility and automatic production of a new
independent direction from that repair under the full frame.
It is not a cancellation counterexample: its kernel is explicitly
\(k[a,z,w+F(a)s]\), and an omitted good direction already recognizes it.

Replacing \(F(a)\) by \(G(a,z)\) in the same coordinate family produces
\(\operatorname{ad}_E^3T_Y=3G^2G_z\partial_w\). Thus that enlargement
leaves the two-quadratic profile unless \(G_z=0\).
The resulting repair is that same third adjoint, not a non-LND
counterexample.

The separate [finite-graph boundary note](finite-euler-graph-recognition-pass65.md)
records why allowing larger graph degree alone does not fix the
higher-flow problem: the unchanged bad coordinates fail invariant
speeds. It is a scope observation, not an additional branch closure.

## 5. Verification and exact next targets

The [captured verification](verification-pass65-working.json)
contains four new exact methods in two new suites and reruns
26 existing methods across six inherited suites. All passed.
The speed-curve checker includes arbitrary symbolic coefficient
identities and a deliberately nonlinear transverse polynomial before
the actual-generation gate. That formal control is not a coordinate
realization. The moving checker does use the explicit actual frame.

The full-project regression remains the historical full60 run:
1000 methods in 126 suites. The working61–64 packet added one distinct
method in one suite; this pass adds four more in two suites, outside
the central registry and without asserting a fresh full-project run.
Independent AI proof reconstructions are recorded in the
[working audit](proof-audits-pass65-working.md).
Neither symbolic tests nor AI reviews constitute proof-assistant
verification or human expert review.

The next low-flow target is exactly (3), using its full actual
rank-three leading distribution. The cubic target retains the
polynomial subrings in (4), the automatic zero motion in (5),
and the unresolved ambient-generation problem.
The other higher constant-top and moving-top cases in the
[previous dependency map](post-graph-closure-scope-pass64.md)
remain separate. Universal frame existence has not been proved.
The all-profile height threshold therefore remains \(H\le9\),
not \(H\le10\).

No claim of historical novelty, expert approval, publication,
submission, external contact, or a general cancellation solution
is made.

## Established source gates

The full hypotheses and exact applications are in the linked proofs.
Generalized Lüroth is recorded in de Bondt's
[Theorem 1.1](https://arxiv.org/pdf/1501.06046v4).
The final coordinate endpoint uses Derksen, van den Essen and van
Rossum's [Theorem 4.4](https://www.researchgate.net/publication/228571174_The_cancellation_problem_in_dimension_four)
over an actual one-variable Dedekind base.
The intrinsic plane input is Kaliman–Saveliev
[Corollary 2.8(2)](https://www.math.miami.edu/~kaliman/library/KaSa.michigan.2004.quotient.pdf),
with the original polynomial cylinder supplying its geometric premises.
The relative-plane and two-quasi statements are recorded, with their
Daigle–Freudenburg and Wang attributions, in Dasgupta–Gupta
[Theorems 2.2 and 4.1](https://arxiv.org/pdf/1701.03635v1).
These are established inputs, not newly proved classification results.
