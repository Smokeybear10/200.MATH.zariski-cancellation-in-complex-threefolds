# A valuation gap for universal generator pencils

A universal generator pencil prevents its perturbation from having a
pole as large as that of the generator. This gives a precise descent
criterion over a normal ring: a polynomial relation for the generator
whose leading coefficient is squarefree along divisors forces the
perturbation into the base ring. The criterion does not assert that
the original cancellation assumptions supply such a relation.

## 1. The valuation inequality

Let \(R\subset A=R[c]\) be domains, let \(h\in A\), and assume the
following equality inside the polynomial ring \(A[\tau]\):
\[
A[\tau]=R[\tau,c+\tau h],\qquad
c=F(\tau,c+\tau h),\quad F\in R[\tau,T].
\tag{1}
\]
The second identity follows from the first and is an identity before
specialization. It is not an assertion that \(c\mapsto c+\tau h\)
defines an \(R\)-endomorphism of \(A\).

Let \(V\) be any valuation ring of \(L=\operatorname{Frac}(A)\)
containing \(R\), and write its valuation additively as \(\nu\).
No discreteness, rank-one condition, or characteristic assumption is
needed for this step. If \(\nu(h)<0\), then \(c\notin V\), because
otherwise \(R[c]\subset V\) would contain \(h\). If
\(\nu(c)\geq\nu(h)\), then \(-c/h\in V\). Substituting this actual
element of \(L\) into the polynomial identity (1) gives
\[
c=F(-c/h,0)\in V,
\qquad\text{a contradiction. Hence}\qquad
\nu(c)<\nu(h)<0\quad\text{if }\nu(h)<0.
\tag{2}
\]
The argument uses both \(h\in R[c]\) and the universal inverse
identity. A collection of inverse formulas only for constant
parameters would not license this substitution.

## 2. Divisorial descent over a normal base

For the rest of the note assume that \(R\) is a normal Noetherian
domain of characteristic zero. Put \(K=\operatorname{Frac}(R)\).
The [field argument for the pencil](universal-generator-pencil-pass88.md)
gives \(h\in K\). If \(c\) is transcendental over \(K\), that same
argument already gives \(h\in R\). We therefore consider only
algebraic \(c\), so \(L=K[c]\) is finite and separable over \(K\).
No assertion that \(A\) is finite over \(R\) is made.

For a height-one prime \(\mathfrak p\) of \(R\), the local ring
\(R_{\mathfrak p}\) is a DVR with normalized valuation
\(v_{\mathfrak p}:K^*\to\mathbb Z\). Its valuation extends to \(L\):
localizing the integral closure of this DVR at a maximal ideal gives
an extension DVR. Divide its normalized valuation by the ramification
index to obtain \(\nu|_K=v_{\mathfrak p}\). These are rational-valued
valuations, so the normalization is retained in the comparison below.[^extension]

If \(v_{\mathfrak p}(h)=-n<0\), then \(n\) is a positive integer,
and (2) implies \(\nu(c)<-n\) for every such extension. In particular,
\[
\left[
\begin{array}{c}
\text{for each height-one }\mathfrak p,\text{ there is an extension }\nu\\
\text{with }\nu(c)\geq-1
\end{array}
\right]
\quad\Longrightarrow\quad
h\in\bigcap_{\operatorname{ht}\mathfrak p=1}R_{\mathfrak p}=R.
\tag{3}
\]
The intersection identity is the usual height-one description of
a normal Noetherian domain.[^intersection] Only one suitable
extension per divisor is required for this criterion. It does not
assume that \(\operatorname{Spec}(A)\to\operatorname{Spec}(R)\) is
surjective at that divisor.

## 3. Leading-coefficient multiplicity

Suppose \(c\) satisfies any nonzero relation
\[
a_d c^d+\cdots+a_0=0,\qquad
a_i\in R,\quad a_d\ne0,\quad d\geq1.
\tag{4}
\]
Fix a height-one prime and set \(e=v_{\mathfrak p}(a_d)\geq0\).
Every extension \(\nu\) above satisfies \(\nu(c)\geq-e\).
Indeed, if \(\nu(c)<-e\), then for every nonzero \(a_i\), \(i<d\),
\[
\nu(a_i c^i)-\nu(a_d c^d)
=v_{\mathfrak p}(a_i)-e-(d-i)\nu(c)>0.
\tag{5}
\]
The leading term would be the unique term with least valuation,
which cannot occur in a zero sum. Zero coefficients are omitted;
if no lower coefficient is nonzero, the proposed negative valuation
is already impossible.

Combining (2) and (5) gives the stronger necessary condition
\[
v_{\mathfrak p}(h)=-n<0
\quad\Longrightarrow\quad
v_{\mathfrak p}(a_d)\geq n+1
\quad\text{for every relation (4).}
\tag{6}
\]
The final rounding uses integer values on \(K\), not integer values
on \(L\): \(-e\leq\nu(c)<-n\) implies the integer \(e>n\).

Consequently, if there is a relation (4) for which
\(v_{\mathfrak p}(a_d)\leq1\) at every height-one prime, then
\(h\in R\). Over a UFD this condition says that \(a_d\) is squarefree,
up to multiplication by a unit. The relation need not be minimal or
monic. This is a sufficient descent criterion, not a necessary
condition for \(h\in R\).

## 4. Sharpness and the actual remaining obligation

The normal polynomial-ring control from
[pass88](normal-generator-pencil-coordinate-boundary-pass88.md) has
\[
R=\mathbb C[a,t,b]\subset A=\mathbb C[a,t,c],
\quad b=a^2c,\quad h=ac=b/a,\qquad
c=(1-\tau a)(c+\tau h)+\tau^2b.
\tag{7}
\]
The displayed map embeds the abstract polynomial ring \(R\) in
\(A\). At the \(a\)-adic valuation of
\(K=\mathbb C(a,t,b)=\operatorname{Frac}(A)\), one has
\(v(c)=-2\), \(v(h)=-1\). The relation \(a^2c-b=0\) therefore
attains the boundary \(e=n+1=2\) in (6). Normality alone does not
eliminate poles, and replacing the squarefree condition by an
order-at-most-two condition is false. This control does not satisfy
all the original-coordinate hypotheses.

In the actual rank-two conical branch, the
[unit-normal argument](constant-acceleration-conical-normal-pass89.md)
gives \(A=S[Y,c]\). When \(Y\) is transcendental over
\(\operatorname{Frac}(S)\), the ring \(R=S[Y]\) is a normal
polynomial three-ring and the actual pencil supplies (1).
The criterion is therefore applicable if its leading-coefficient
premise can be derived. That premise is not proved here.
Even \(h\in R\), by itself, is not a recognition theorem for \(A\).
The unrestricted complex-threefold cancellation problem remains open
within this investigation.

## 5. Proof and source boundaries

The valuation substitution and leading-coefficient argument are
written algebraic deductions. Finite symbolic examples can check
their controls but do not certify the quantified valuation theorem.
The primary source inputs are only the standard DVR extension and
normal-domain intersection facts. The selected complete displayed
statements and proofs were read for the cited Stacks tags; the
lemmas they invoke remain inherited inputs. No new novelty claim,
formal proof, or expert verification is made.

[^extension]: The Stacks Project, [Remark 15.113.6, tag 09E8](https://stacks.math.columbia.edu/tag/09E8), accessed September 14, 2026. A finite separable extension of the fraction field of a DVR has finite integral closure, whose localizations at maximal ideals are extension DVRs. The valuation is rescaled here by its ramification index.

[^intersection]: The Stacks Project, [Lemma 15.24.18, tag 0AVB](https://stacks.math.columbia.edu/tag/0AVB), accessed September 14, 2026, applied to the reflexive module \(M=R\). The proof also identifies the height-one local rings as DVRs. Section numbering may change; the tags are stable.
