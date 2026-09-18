# Torsion constraints for smooth rationally acyclic fibers

Let \(G:\mathbb C^3\to\mathbb C\) be a nonconstant polynomial
whose every fiber is smooth and rationally acyclic. Choose a nonempty
finite set \(B\) containing all topological bifurcation values, put
\(s=|B|\), and write \(Y\) for a general fiber. Define
\[
T=H^2(Y;\mathbb Z),\qquad
T_b=H^2(G^{-1}(b);\mathbb Z)\quad(b\in B).
\]
Then these are finite abelian groups and, for the monodromy local
system \(\mathcal T\) on \(U=\mathbb C\setminus B\),
\[
\boxed{
T^{\pi_1(U)}=0,\qquad
H^1(U;\mathcal T)\cong\bigoplus_{b\in B}T_b,\qquad
\prod_{b\in B}|T_b|=|T|^{s-1}.}
\tag{1}
\]
This is a topological constraint, not coordinatehood of \(G\) and
not a proof that \(T=0\). Here the order of the trivial group is one.

The argument is a direct application of the Gysin sequence and the
cohomology of a local system over a graph. It has been separately
reconstructed, but no historical priority or human review is claimed.

## 1. Integral groups of each fiber

A smooth complex affine surface has the homotopy type of a finite
CW complex of real dimension at most two. Its second integral
homology is free abelian; higher homology vanishes. Rational
acyclicity thus gives
\[
H_0=\mathbb Z,\qquad H_1=A\text{ finite},\qquad H_j=0\ (j\ge2).
\]
The integral universal coefficient theorem gives \(H^1=0\) and
\(H^2=\operatorname{Ext}(A,\mathbb Z)\), a finite group of the
same order as \(A\). These standard surface facts are also explicitly
used in the proof of the cited surface lemma.[^1]

## 2. Removing the exceptional fibers

Let
\[
E=G^{-1}(U),\qquad
D=\coprod_{b\in B}G^{-1}(b).
\]
The components of \(D\) are disjoint smooth divisors in
\(\mathbb C^3\). The integral Gysin sequence, using the complex
orientation of each normal line, gives
\[
H^2(E;\mathbb Z)\cong H^1(D;\mathbb Z)=0,
\]
\[
H^3(E;\mathbb Z)\cong H^2(D;\mathbb Z)
=\bigoplus_{b\in B}T_b.
\tag{2}
\]
Both assertions use the vanishing of adjacent positive-degree
cohomology groups of the ambient \(\mathbb C^3\).

By the choice of \(B\), \(G:E\to U\) is a locally trivial
topological fibration. A polynomial map has a finite bifurcation set;
the cited monodromy paper states this setup explicitly.[^2]
The base \(U\) retracts to a graph with \(s\) loops.
In the integral Leray or Serre spectral sequence, only fiber
cohomology rows zero and two survive. The base has cohomological
dimension one for local systems, so no differential can affect them.
It follows that
\[
H^2(E;\mathbb Z)\cong H^0(U;\mathcal T)
=T^{\pi_1(U)},\qquad
H^3(E;\mathbb Z)\cong H^1(U;\mathcal T).
\tag{3}
\]
Combining (2) and (3) proves the first two assertions of (1).

Choose generators of the graph fundamental group, with monodromy
automorphisms \(M_1,\ldots,M_s\) of \(T\). Its cellular
cochain complex is
\[
0\longrightarrow T
\xrightarrow{\delta} T^s
\longrightarrow0,\qquad
\delta(t)=((M_1-1)t,\ldots,(M_s-1)t).
\tag{4}
\]
The first assertion of (1) says \(\delta\) is injective.
Counting finite groups in (4) gives
\[
|H^1(U;\mathcal T)|=\frac{|T|^s}{|T|},
\]
which proves the product formula.

Adding a regular value to \(B\) introduces one copy of the general
group \(T\) and one trivial monodromy generator. Both sides of the
product formula are then multiplied by \(|T|\), as required.
If there are no bifurcation values at all, the fibration is over a
contractible base and its total space is \(\mathbb C^3\); its
fiber is contractible. That boundary case can be handled directly.

## 3. Genuine consequences and the remaining loophole

If the integral monodromy on \(T\) is trivial, its invariant
subgroup is all of \(T\). Equation (1) forces \(T=0\);
the product formula then makes every exceptional \(T_b\) zero.
Thus all fibers are integrally acyclic under this additional condition.

Likewise, if all fibers have the same torsion-group order \(a\),
the product formula becomes \(a^s=a^{s-1}\), so \(a=1\).
Constant rational Betti numbers do not establish constant torsion
orders, so that is a genuine extra hypothesis.

For a single bifurcation value, (1) forces the exceptional fiber's
group to vanish, but does not force \(T=0\). As a purely algebraic
model, take \(T=\mathbb Z/3\) and \(M=-1\). Then \(M-1\) is
invertible, with zero kernel and cokernel, even though \(T\ne0\).
This is not an example of a polynomial satisfying all the hypotheses.
It shows exactly why the formal argument cannot conclude \(T=0\).

It is also false that general fibers of arbitrary polynomials
\(\mathbb C^3\to\mathbb C\) automatically have torsion-free first
homology. A published quartic has general-fiber first homology
\(\mathbb Z/3\) with nontrivial monodromy.[^2] That example has a
singular zero fiber and is not rationally acyclic in general; it is
a scope warning, not a counterexample to a stronger all-fiber assertion.

## 4. Application to a stable pure-power slice

For a stable coordinate \(F=xu^n+G\), \(n\ge2\), every
\(G\)-fiber is smooth. For each prime \(p\mid n\), its embedding
as the fixed set of the order-\(p\) subgroup of the cyclic action
on a contractible \(F\)-fiber makes it mod-\(p\) acyclic by
Smith theory.[^3]

The finite CW description above now implies \(H_2=0\) and
finite \(H_1\) whose order is coprime to \(n\). In particular
every \(G\)-fiber is rationally acyclic, and (1) applies. Torsion
at primes not dividing \(n\) is the precise unresolved integral
possibility in this argument.

Even an eventual proof that all these fibers are integrally acyclic
would need a further algebraic step for an arbitrary \(G\).
The binomial-surface rectification theorem is available only in its
specified presentation. Absolute coordinatehood of \(G\), by itself,
would still not give the relative coordinate pair \((x,G)\) needed
for the simplest pure-power completion.

## Verification

The finite-group identities and the nonzero-torsion algebraic model
are checked in the independent standard-library suite
~~~text
python3 verify_torsion_monodromy.py
~~~
Those tests do not implement the Gysin or Leray spectral sequences
and do not decide whether any proposed torsion data are realized by
a polynomial with all fibers smooth and rationally acyclic.

## Sources

[^1]: Shulim Kaliman and Mikhail Zaidenberg.
[*Affine modifications and affine hypersurfaces with a very transitive
automorphism group*](https://arxiv.org/pdf/math/9801076v2).
Lemma 7.1 and its proof, pp. 29–30, for the finite two-dimensional
CW description and integral homology of smooth affine surfaces.

[^2]: Alexandru Dimca and András Némethi.
[*On the monodromy of complex polynomials*](https://arxiv.org/pdf/math/9912072v2).
Section 2.1 for the finite bifurcation set and monodromy;
Example 4.1 for the quartic torsion example. Corollary B provides
related conditional acyclicity results, not automatic triviality
of integral monodromy under rational acyclicity.

[^3]: Peter Symonds. [*Smith theory for algebraic
varieties*](https://personalpages.manchester.ac.uk/staff/peter.symonds/preprints/smith.pdf).
Section 4, Corollary 4.3 and Remark (1). The application here uses
ordinary mod-\(p\) cohomology of the associated finite-dimensional
equivariant CW spaces.
