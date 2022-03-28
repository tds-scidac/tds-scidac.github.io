# Adaptive, scalable relativistic Fokker-Planck solver based on PETSc-p4est 

Johann Rudi (ANL), Max Heldman (ANL and Boston), Emil Constantinescu (ANL), Qi Tang (LANL) and Xianzhu Tang (LANL)

**LA-UR-22-22439. Approved for public release; distribution is unlimited.** 

## Overview

We consider a 0D2V relativistic Fokker-Planck equation for runaway electrons with sources of a Columbo collision operator, a radiation damping operator, and a secondary knock on collision source.
We develop a scalable fully implicit solver with dynamic adaptivity. We developed a new data management framework in [PETSc](https://petsc.org) based on the [p4est](https://p4est.org) library that enables simulations with dynamic adaptive mesh refinement (AMR), and implemented a new runaway electron solver that interfaces to the PETSc framework. 

----

## Result

<video controls preload="metadata" width="100%">
    <source src="../img/gallery/E_1.69chiu.mp4" type="video/mp4">
    Sorry, your browser doesn't support embedded videos.
</video>
*The simulation demonstrates the critical need for AMR[^1], in which 7 levels of refinement are used (corresponding to a 128 factor of resolution increase) to resolve both low-energy Maxwellian bulk and high-energy runaway tail. The dynamic AMR successfully captures the interaction between two structures and resolves a forming vortex structure. A delta-function-like Chiu source and practical collision parameters extracted from ITER are also deployed.*


[^1]: J. Rudi, M. Heldman, E. Constantinescu, Q. Tang and X.-Z. Tang. Scalable implicit solvers with dynamic mesh adaptation for a relativistic Fokker-Planck kinetic model, in preparation, 2022.


