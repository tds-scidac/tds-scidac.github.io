# Anisotropic Transport in PIXIE3D
Highlight by Luis Chacon (LANL)

**LA-UR-22-22433. Approved for public release; distribution is unlimited.** 

## Overview

* Magnetic fusion plasmas feature large heat-transport anisotropy between directions parallel and perpendicular to the magnetic field ($\chi_\parallel/\chi_\perp \sim 10^{10}$).
* Such anisotropies prevent standard MHD discretizations to preserve positivity and to leverage multigrid methods for efficiency (even algebraic MG).
* We have adapted a recently proposed idea [E.J. du Toit et al., Computer Physics Communications 228 (2018)] to transform problematic diffusive cross-fluxes into nonlinear advection operators.
* Approach is amenable to limiting (for positivity preservation) and to multigrid techniques (for solver efficiency).
* Approach can be implemented with high-order accuracy robustly, which is required to simulate large anisotropies accurately (our implementation is a mixed 3rd/4th-order finite-difference representation).

----

## Result

![](img/gallery/iter-anisotropic-xport.jpg)
*Poincare plot (left) and poloidal electron temperature (right) field during a (1,1) kink relaxation event in ITER using $\chi_\parallel/\chi_\perp \sim 10^{7}$ with Braginskii transport and Spitzer resistivity. The alignment of the temperature field with the Poincare plot at the plasma core is apparent.*

----

<video controls preload="metadata" width="100%">
    <source src="../img/gallery/bpnch-hall-mhd-unif-rho-chi_par_1e3.mp4" type="video/mp4">
    Sorry, your browser doesn't support embedded videos.
</video>
*Movie of a full reconnection event induced by a (1,1) kink instability of a Bennet pinch equilibrium in helical geometry with $\chi_\parallel/\chi_\perp \sim 10^{7}$.*

<script type="text/x-mathjax-config">MathJax.Hub.Config({TeX: {equationNumbers: {autoNumber: "all"}}, tex2jax: {inlineMath: [['$','$']]}});</script>
<script type="text/javascript" src="https://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.2/MathJax.js?config=TeX-AMS_HTML"></script>
