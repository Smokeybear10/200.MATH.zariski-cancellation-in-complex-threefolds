# Exact Artin-length controls

The standalone [checker](fixed_scheme_artin_checks_pass92.py) has two
unittest methods and imports only the standard library and SymPy.
It is a local-algebra control for the fixed-scheme discussion, not a
construction of an original nonconical frame.

The first method checks the quotients by \((x^2,y^2)\),
\((x^2+y^3,xy)\), and \((x^2,y^3)\), of respective lengths
four, five, and six. It computes a lexicographic Gröbner basis,
extracts pure-power bounds from the initial ideal, and enumerates
exactly the monomials outside that initial ideal. There is no
arbitrarily truncated monomial search. The resulting multiplication
matrices commute, satisfy the original defining relations, and are
nilpotent. Thus these finite-dimensional quotients are supported only
at the origin, and their vector-space dimensions equal their local
lengths. The one-dimensional common matrix kernel and explicit
annihilated monomial also check their socles.

The second method checks the two different generic transverse lengths
in [fixed-scheme-structure92](nonconical-fixed-scheme-structure-pass92.md).
For \(e=2,3\) and \(m=1,2,4,7\), it compares the whole fiber ideal
\((p,p^m z-y^e)\), of length e, with the fixed ideal
\((p^m,y^{e-1})\), of length \(m(e-1)\). The calculation is over
\(\mathbb Q(z)\); extension to \(\mathbb C(z)\) preserves these
explicit monomial bases and dimensions. The nilpotence checks and,
when \(m>1\), the nonzero class of p retain the distinction between
fiber multiplicity and fixed-scheme thickness. Eight parameter pairs
are subtests within one method, not eight separate methods.

The finite computations do not prove the all-m formula, the general
Cohen--Macaulay conclusion, a bound on actual closed fibers, or
realizability by an original coordinate inverse. The arbitrary-family
length calculation is the monomial argument in the linked proof.
In particular the length-five and length-six complete intersections
are not asserted to satisfy the original nonconical hypotheses.
No action search, new source theorem, runner or full regression is
included. Pass91 and earlier files remain unchanged.

Jet wrote these controls at Root's request after independently reading
the entire fixed-scheme proof. The first standalone command was:

    /opt/anaconda3/bin/python research/fixed_scheme_artin_checks_pass92.py

It passed both methods in 0.062 seconds, exit zero; complete stdout
and stderr are retained in tool chunk 4ad5a7. No assertion failed.
The saved code and this scope note then received full author EOF
reads. One JavaScript patch-wrapper parse error occurred before any
file operation while adding this paragraph; it was corrected without
changing the checker or mathematical assertions. Repeated runs, if
any, do not add methods or certify the general statements.
