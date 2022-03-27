# PIXIE3D Extended MHD Simulation
Ioannis Keramidas (LANL), Luis Chacón (LANL), and Xianzhu Tang (LANL)

**LA-UR-21-30976. Approved for public release; distribution is unlimited.** 

## Overview

PIXIE3D simulations have been routinely deployed to investigate flux surface break-up due to a variety of MHD modes on ITER. In particular, we have uncovered that parallel thermal transport can have a large impact on flux surface break-up. This sensitivity brings additional burden on incorporating the correct parallel transport physics (more later) to get the “MHD” right, i.e. field topology & stochasticity. 

----

## Result
We run  simulations of a (1,1) internal kink mode and a (3,2) double tearing profile in ITER geometry with the extended MHD code PIXIE3D. 

### (1,1) Internal Kink Mode without thermal diffusion

In this simulation, the parallel thermal conductivity is turned off.

<video controls preload="metadata" width="100%">
    <source src="../img/pixie3d/11-visc-poinc.mp4" type="video/mp4">
    Sorry, your browser doesn't support embedded videos.
</video>
*Magnetic topology in excerpt of (1,1) kink simulation. As the (1,1) mode grows the core splits and gets expelled while magnetic stochasticity has set in at the outer edge. Towards the end, isolated islands reform but nothing remains from the original core.*

----

<video controls preload="metadata" width="100%">
    <source src="../img/pixie3d/11-visc-dTe.mp4" type="video/mp4">
    Sorry, your browser doesn't support embedded videos.
</video>
*Temperature perturbation of the (1,1) kink simulation. The (1,1) mode develops fast. When the core is destroyed a general cooling is observed.*

----

<video controls preload="metadata" width="100%">
    <source src="../img/pixie3d/11-visc-bnm.mp4" type="video/mp4">
    Sorry, your browser doesn't support embedded videos.
</video>
*Amplitude of the largest modes of the radial magnetic field perturbation during the (1,1) kink simulation. The (1,1) mode and its sidebands dominate.*



### (1,1) Internal Kink Mode with thermal diffusion

In this simulation, the parallel thermal conductivity is turned on.

<video controls preload="metadata" width="100%">
    <source src="../img/pixie3d/chipar-poinc.mp4" type="video/mp4">
    Sorry, your browser doesn't support embedded videos.
</video>
*Magnetic topology in excerpt of (1,1) kink simulation. The mode grows and splits the core. Magnetic stochasticity sets in outside the core.<br> The core eventually reheals forming a transport barrier.*

----

<video controls preload="metadata" width="100%">
    <source src="../img/pixie3d/chipar-dTe.mp4" type="video/mp4">
    Sorry, your browser doesn't support embedded videos.
</video>
*Temperature perturbation of the (1,1) kink simulation. The (1,1) mode develops fast. As the core reheals an m=2 mode is observed. At the end, a toroidal structure is observed that strongly localizes the leaking heat.*

----

<video controls preload="metadata" width="100%">
    <source src="../img/pixie3d/chipar-bnm.mp4" type="video/mp4">
    Sorry, your browser doesn't support embedded videos.
</video>
*Amplitude of the largest modes of the radial magnetic field perturbation during the (1,1) kink simulation. The (1,1) mode and it is sidebands dominate. Towards the end, an m=5, n=2 mode gets excited at the edge.*

### Double Tearing at $q = 3/2$
            
In this simulation, the parallel thermal conductivity is turned off.

<video controls preload="metadata" width="100%">
    <source src="../img/pixie3d/db-poinc.mp4" type="video/mp4">
    Sorry, your browser doesn't support embedded videos.
</video>
*Magnetic topology in excerpt of the double tearing simulation. Lots of different islands form due to multiple double tearing surfaces of higher order. The edge develops stochasticity while the core and some isolated islands survive.*

----

<video controls preload="metadata" width="100%">
    <source src="../img/pixie3d/db-dTe.mp4" type="video/mp4">
    Sorry, your browser doesn't support embedded videos.
</video>
*Temperature perturbation of the double tearing simulation. We initially see a dominant tearing mode (m=5, n=3). Towards the end, the structure is getting deformed possibly transitioning to a low (n,m) mode with strong ballooning.*

----

<video controls preload="metadata" width="100%">
    <source src="../img/pixie3d/db-bnm.mp4" type="video/mp4">
    Sorry, your browser doesn't support embedded videos.
</video>
*Amplitude of the largest modes of the radial magnetic field perturbation during the double tearing simulation. Various high order modes exist giving rise to high order islands.*

<script type="text/x-mathjax-config">MathJax.Hub.Config({TeX: {equationNumbers: {autoNumber: "all"}}, tex2jax: {inlineMath: [['$','$']]}});</script>
<script type="text/javascript" src="https://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.2/MathJax.js?config=TeX-AMS_HTML"></script>
