# Gyrokinetic Simulations of Thermal Quench and Disruptive MHD Events
Highlight by Min-Gu Yoo (PPPL), Weixing Wang (PPPL), Edward Startsev (PPPL), and Xian-Zhu Tang (LANL)


## Overview

<!---
The novel approaches of the TDS project, such as 3D magnetic topology analysis and the global gyrokinetic simulation by the GTS code, uncovered the collisionless plasma transport mechanisms during the thermal quench in the presence of open stochastic magnetic field lines connected to the wall boundary. Here, we highlight the complex 3D magnetic topology can be understood with two key concepts: the connection length $L_c$ and the effective magnetic mirror ratio $M_{eff}$. The newly developed generalized delta-f particle scheme enabled much more efficient global gyrokinetic simulations of thermal quench phenomena, leading to novel understanding of 3D plasma dynamics including the important electron kinetic physics. 
-->

During tokamak disruption, large MHD perturbations which break the magnetic surface may trigger a sudden loss of energy and particle confinement.  Because the mean free path of particles in the burning plasma by many orders of magnitudes exceeds the size of the configuration, the process cannot be simply reduced to thermo-conduction losses in fluid model. Instead, self-consistent kinetic simulations, complemented with appropriate boundary conditions for the particle and thermal energy losses are needed for modeling of the thermal quench. We have developed and applied kinetic simulation capabilities based on a global gyrokinetic model with GTS code to confront specific challenges in disruption modeling. Highlights here focus on three development fronts.

1. The novel approaches combining gyrokinetic calculations of plasma transport and plasma profile evolution in stochastic magnetic fields and 3D magnetic topology analysis uncovered the collisionless plasma transport mechanisms for the thermal quench in major tokamak disruptions due to the presence of open stochastic magnetic field lines connected to the wall boundary. Here, we highlight the complex 3D magnetic topology can be understood with two key concepts: the connection length Lc and the effective magnetic mirror ratio Meff.  <br />
Details of thermal quench physics can be found in [Min-Gu Yoo, et al., Nuclear Fusion, 61 (12) (2021)](https://doi.org/10.1088/1741-4326/ac30c6).

1. A major development is made in the front of gyrokinetic electromagnetic simulations of disruptive MHD modes. With the aid of an advanced and robust electromagnetic scheme with fully kinetic electrons implemented in EM-GTS code, success in nonlinear simulations have been achieved for various MHD modes in tokamak geometry. These include current-driven kink mode, tearing and double-tearing modes. These MHD modes may cause a rapid loss of energy confinement in tokamaks (i.e., thermal quench) by the break of closed magnetic surfaces with their large magnetic perturbations.  This key progress paves the way for us to explore high fidelity kinetic simulations of disruptive MHD processes and consistent transport in the context of disruption modeling.

1.	A generalized delta-f particle scheme has been developed to simulate plasma systems with arbitrary physics boundary and strong force (for which the standard delta-f scheme often fails to handle). The new scheme is critical to enable global gyrokinetic simulations of thermal quench problem, leading to novel understanding of 3D plasma dynamics including the important electron kinetic physics in the thermal quench process.

----

## Result

![](img/gallery/Lc_3D.png)
*Destructive magnetic perturbations can create open magnetic field lines that randomly wander inside the tokamak and eventually hit wall boundaries. The red line shows the 3D trajectory of an example field line approximately 400 meters long. Each field line can have a significantly different trajectory. The colors of the four circular planes show the complex 3D structure of field line lengths, consisting of shorter (black) and longer (yellow) regions.*

----

<video controls preload="metadata" width="100%">
    <source src="../img/gallery/Meff.mp4" type="video/mp4">
    Sorry, your browser doesn't support embedded videos.
</video>
*The 3D structure of the effective magnetic mirror ratio $M_{eff}$ in the presence of open stochastic magnetic fields. The black line shows an example open magnetic field line. Red and blue colors represent regions of magnetic wells ($M_{eff} > 1$) and magnetic hills ($M_{eff} < 1$), respectively. Charged particles can be trapped in the magnetic well region by the magnetic mirror force.*

----

<video controls preload="metadata" width="100%">
    <source src="../img/gallery/Passing-Trap.mp4" type="video/mp4">
    Sorry, your browser doesn't support embedded videos.
</video>
*The motion of test electrons in the presence of open magnetic field lines: (top left) R-Z cylindrical coordinates, (top right) velocity coordinates, and (bottom) spatial coordinate versus magnetic potential energy along the field line. The blue particle is the passing electron exiting towards the right wall boundary, while the red and green particles are trapped electrons by the magnetic mirror force before hitting the wall boundary.*

----

<video controls preload="metadata" width="100%">
    <source src="../img/gallery/Density_Potential.mp4" type="video/mp4">
    Sorry, your browser doesn't support embedded videos.
</video>
*The temporal evolution of (left) electron density and (right) electrostatic potential in the presence of open stochastic magnetic fields during the thermal quench. Upper figures show the case where the $\mathbf{E}\times\mathbf{B}$ drift motion is ignored, whereas lower figures show the case where the ExB drift motion is included.*



----

<video controls preload="metadata" width="100%">
    <source src="../img/gts/Ed_2_1_tearing.mp4" type="video/mp4">
    Sorry, your browser doesn't support embedded videos.
</video>
*Evolution of electron density perturbations of (2,1) tearing mode simulated by EM-GTS.*

----

<video controls preload="metadata" width="100%">
    <source src="../img/gts/Ed_double_tearing_movie.mp4" type="video/mp4">
    Sorry, your browser doesn't support embedded videos.
</video>
*Evolution of electron density perturbations of double-tearing mode simulated by EM-GTS.*

----

<video controls preload="metadata" width="100%">
    <source src="../img/gallery/Two_Stream.mp4" type="video/mp4">
    Sorry, your browser doesn't support embedded videos.
</video>
*Particle simulation of two-stream instability with three different weight schemes: (left) full-f, (middle) generalized delta-f, and (right) typical delta-f. Upper and lower figures show the motion of electron markers and the evolution of the total electron distribution function in the phase-space ($x-v$), respectively. Whereas the typical delta-f scheme (right) fails after a short time, the newly developed generalized delta-f scheme (middle) successfully simulates the same result as the full-f (left) does.*

Paper: [Min-Gu Yoo, <i>et al., Nuclear Fusion</i> <b>61</b>(12) (2021)](https://doi.org/10.1088/1741-4326/ac30c6)

Invited talks: [5<sup>th</sup> AAPPS-DPP (2021)](http://aappsdpp.org/DPP2021/F/5309.pdf) and [63<sup>rd</sup> APS-DPP (2021)](https://meetings.aps.org/Meeting/DPP21/Session/TI02.1)

<script type="text/x-mathjax-config">MathJax.Hub.Config({TeX: {equationNumbers: {autoNumber: "all"}}, tex2jax: {inlineMath: [['$','$']]}});</script>
<script type="text/javascript" src="https://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.2/MathJax.js?config=TeX-AMS_HTML"></script>
