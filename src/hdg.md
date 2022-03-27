# Scalable Hybridized DG and Exponential DG for Fluid Models
Highlight by Tan Bui-Thanh (UT Austin).


## Overview

Advanced Tokamak simulations need rigorous high-order accuracy, efficient temporal simulations at desperately different scales.

* We proposed and analyzed a high-order hybridized Discontinuous Galerkin (HDG) framework for MHD system to achieve stable and high-order accuracy in space
* We proposed and analyzed multigrid, multilevel approaches for HDG
* We proposed and analyzed high-order IMEX and exponential time integrators  to over time-step limitation due to fast physics
 

----

## Scalable, high-order HDG-based MHD solver

[![](img/gallery/2d-ic.png)](img/gallery/2d-ic.mp4)
<div align="center">*2D island coalescence using a very high-order HDG scheme. The current sheet breaks into plasmoids.*</div>

[![](img/gallery/3d-ic.png)](img/gallery/3d-ic.mp4)
<div align="center">*3D island coalescence using a very high-order HDG scheme. A current sheet is forming in the center of the domain.*</div>

[![](img/gallery/kh-mhd.png)](img/gallery/kh-mhd.mp4)
<div align="center">*3D Kelvin-Helmholtz instability of MHD*</div>

----

## Kelvin-Helmholtz instability using IMEX or exponential time integrator 

Several Kelvin-Helmholtz instabilities for different models are studied. 
Two types of time integrators are considered: exponential integrator and IMEX integrators.
We are currently extending the proposed schemes to MHD.

![](img/gallery/hp-HDG.png)
<div align="center">*hp-adaptive HDG solver*</div>

[![](img/gallery/kh-euler.png)](img/gallery/epi2-Cr5-1em7.mp4)
<div align="center">*3D Kelvin-Helmholtz instability for Euler equations. An exponential time integrator is used along with a high-order DG scheme.*</div>

[![](img/gallery/hdg-dg-kh.png)](img/gallery/KelvinHelmholtzInstabilityForShallowWaterOnTheEarth.mp4)
<div align="center">*3D Kelvin-Helmholtz instability for shallow water equations on a sphere. A IMEX integrator is used along with a high-order HDG-DG scheme.*</div>


<script type="text/x-mathjax-config">MathJax.Hub.Config({TeX: {equationNumbers: {autoNumber: "all"}}, tex2jax: {inlineMath: [['$','$']]}});</script>
<script type="text/javascript" src="https://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.2/MathJax.js?config=TeX-AMS_HTML"></script>
