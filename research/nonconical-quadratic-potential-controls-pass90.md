# Formal controls for the quadratic volume coefficient

This is a symbolic matrix control for the
[quadratic-potential proof](nonconical-quadratic-potential-pass90.md),
not an actual polynomial action or a proof certificate for its
ring-theoretic conclusions. Its one unittest method uses an arbitrary
formal three-by-three matrix \(C\), six independent coefficients for
the two middle columns in the \(C\)-basis, and independent last-row
coefficients.

The exact modeled matrix is
\[
M=\operatorname{diag}(C,1)
\begin{pmatrix}
1&a_{10}&a_{20}&0\\
0&u+a_{11}&a_{21}&v_1\\
0&a_{12}&u+a_{22}&v_2\\
qu&r_1&r_2&r_v
\end{pmatrix},
\qquad \Omega=\det C .
\tag{1}
\]
The zero first coefficient in the last upper column models the
already established cubic-volume constraint. It is an input, not a
new conclusion of this test. All entries of \(C\) are independent
symbols, so the calculation does not rely on a chosen numerical
basis or a determinant-one specialization.

The checker expands the full determinant, checks its factorization
by \(\det C\), and verifies both negative minor signs giving
\[
[u^2]\det M=\Omega\bigl(r_v+q(a_{10}v_1+a_{20}v_2)\bigr),
\qquad [u^3]\det M=0 .
\tag{2}
\]
It then sets
\(a_{10}=\rho_1+\Gamma_{11}y_1+\Gamma_{12}y_2\) and
\(a_{20}=\rho_2+\Gamma_{12}y_1+\Gamma_{22}y_2\).
The gradient of
\(\Psi=\rho_1y_1+\rho_2y_2+
\Gamma_{11}y_1^2/2+\Gamma_{12}y_1y_2+
\Gamma_{22}y_2^2/2\)
is exactly this pair. Substitution of
\(r_v=-q(\Psi_{y_1}v_1+\Psi_{y_2}v_2)\) cancels the
quadratic determinant coefficient. A separate symbolic curl within
the same method is \(\Gamma_{21}-\Gamma_{12}\) when the mixed
coefficients are independent, displaying the necessity of the
symmetry input for this potential.

The
[standalone checker](nonconical_quadratic_potential_checks_pass90.py)
imports only unittest and SymPy and contains one test method.
It does not test that a formal determinant is a unit, construct an
actual local slice, identify an LND kernel, remove a localization
factor, prove faithful flatness, or recognize an unknown three-ring.
Those are the separate written hypotheses and deductions of the
main proof. No old checker or research implementation is imported.

Jet independently reconstructed the determinant signs before the
saved main-proof review, then authored this bounded coefficient
control at Root's request. An initial generic-matrix calculation
passed in tool chunk 745b90; it was not a unittest method. The first
standalone run passed one method in 0.235 seconds, exit zero, with
complete output in tool chunk 121a2f. No assertion failed. The
complete saved code and scope note received author reads through
EOF, followed by a separate read of this final provenance update.
No runner or integration capture is created by this control, and
pass89 and earlier files remain unchanged.
