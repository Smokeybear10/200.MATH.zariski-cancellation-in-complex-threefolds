# Rank-two image ideals: primary-source boundary

The published primary abstract confirms the rank-at-most-two freeness result.
The original full text of Theorem 4.1 was not accessible in this bounded pass,
so its numbering and exact higher-image formulation remain verified through
Dasgupta–Lahiri's explicit attribution, not by direct inspection of that theorem.

## 1. Original publication and directly verified scope

A. Ben Khaddah, M. El Kahoui, and M. Ouali, *The Freeness Property for Locally
Nilpotent Derivations of R[2]*, **Transformation Groups 28** (2023), 35–60,
[DOI 10.1007/s00031-022-09705-z](https://link.springer.com/article/10.1007/s00031-022-09705-z).
The publisher records online publication on March 5, 2022, and the March 2023
issue. This is a published article, not only a preprint.

Its abstract assumes a PID \(R\) containing \(\mathbb Q\) and a nonzero LND
\(\xi\) on \(R^{[2]}\), and concludes freeness over the kernel with a
\(\xi\)-basis. It explicitly states the consequence for characteristic-zero
\(K^{[3]}\) derivations of rank at most two. There is no irreducibility,
triangularity, or quasi-nice assumption in the abstract. The original
introduction's first page sets up **\(R\)-derivations**, so the intended
relative statement fixes \(R\). The publisher-supplied first-page preview is
also publicly readable on the
[article's ResearchGate page](https://www.researchgate.net/publication/359037242_THE_FREENESS_PROPERTY_FOR_LOCALLY_NILPOTENT_DERIVATIONS_OF_R2).

The publisher PDF route required subscription access. The author profile and
institutional publication index did not expose a full manuscript. ResearchGate
provided only the first page; text after its preview includes snippets from
citing papers and must not be mistaken for the original Theorem 4.1.

## 2. Exact higher-image formulation attributed to Theorem 4.1

[Dasgupta–Lahiri, arXiv:2302.13787v6, Introduction](https://arxiv.org/html/2302.13787v6),
version dated July 24, 2026, explicitly attributes the following statement to
Ben Khaddah–El Kahoui–Ouali, Theorem 4.1:

For a PID \(R\) containing a characteristic-zero field \(k\),
\(T=R^{[2]}\), and \(D\in\operatorname{LND}_R(T)\), every ideal
\[
I_j=\ker D\cap D^j(T)=D^j(\ker D^{j+1}),\qquad j\ge1,
\]
is principal in \(\ker D\). Their attribution does not impose
irreducibility. It expressly gives the consequence when the kernel of an LND
on \(k^{[3]}\) contains an ambient coordinate.

This is a secondary attribution within an original research paper, clearly
consistent with the original publisher abstract. It is not a substitute for
claiming that the original full theorem and proof were read.

The passage from an adapted basis to principal image ideals is elementary.
If \((e_i)_{i\ge0}\) is a kernel basis with \(\deg_D e_i=i\), distinct
degrees prevent cancellation of the largest nonzero term in a finite basis
expansion. Thus
\[
\ker D^{j+1}=\bigoplus_{i=0}^j(\ker D)e_i,
\qquad I_j=(D^j e_j)\ker D.
\]
For rank at most two on \(k^{[3]}\), choose an invariant coordinate \(x\)
and take \(R=k[x]\). This does not extend the result to rank three.

## 3. Two limits relevant to the extension argument

Principal higher image ideals do not alone give the saturation condition
\(BC\cap I_j=BI_j\) used in general-extension arguments. For example, in
\(C=k[x]\), with \(B=x\) and \(I_j=xC\), the two sides are \(xC\) and
\(x^2C\). The additional coprimality or geometric argument remains necessary.

An especially misleading search hit is Daniel Daigle's
[*The freeness property for locally nilpotent derivations of k[x,y,z]*,
arXiv:2009.14800](https://arxiv.org/abs/2009.14800). Its retained abstract claims
the result for all ranks, but the primary record says the paper was withdrawn
on May 14, 2021 because of an error in the main proof. That claim is not used
here. This audit makes no assertion about the current resolution of the
unrestricted freeness conjecture.
