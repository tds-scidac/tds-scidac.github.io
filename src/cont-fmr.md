# Disruption Control and Fast Magnetic Reconnection
Highlight by Allen Boozer (Columbia University)


## Foundational Constraints on Disruption Control

Physics constrains strategies for disruption control.  An understanding of these constraints is essential for reliable computational studies.  Two types of constraints will be discussed in this section.

### Plasma Steering

The constraints on plasma steering as a method for avoiding disruptions are the subject of Reference [@plasma_steering], which has the abstract:  "*Steering tokamak plasmas is commonly viewed as a way to avoid disruptions and runaway electrons. Plasma steering sounds as safe as driving to work but will be shown to more closely resemble driving at high speed through a dense fog on an icy road. The long time required to terminate an ITER discharge compared to time over which dangers can be foreseen is analogous to driving in a dense fog. The difficulty of regaining plasma control if it is lost resembles driving on an icy road. Disruptions and runaways are associated with three issues---a solution to one tends to complicate the solution to the other two: loss of plasma position control, excessive heat deposition, and wall melting due to runaway electrons. All three risks must be addressed for ITER to achieve its mission and essentially eliminated before tokamak power plants can be deployed.*"


### Magnetic Interaction with the Wall

The conducting structures in ITER are greatly simplified in simulations. This can result in an order-of-magnitude error in the force per unit area on structures.  For example, the toroidal wall-currents that arise during disruptions that are due to changes in the poloidal field can have their current path rotated into the poloidal direction when wall melting opens a lower inductance path.  This increases the $\vec{j}\times\vec{B}$ force by the ratio of the toroidal to the poloidal field---approximately a factor of ten---and the current path can become much narrower, which gives an additional increase in the force density.  When wall-currents are induced on a time scale of order 10~ms or less, the dipole moment produced by currents circulating in the individual beryllium tiles can result in strong forces on the tiles.  These effects and practical methods for estimating their importance are discussed in [@wall_magnetics].


## Fast magnetic reconnection during disruptions

Tokamak disruptions are associated with a rapid breakup of magnetic surfaces over a large fraction of the plasma volume. The physical effects that allow the breakup of magnetic surfaces are extremely small in the central part of JET and will be even smaller in ITER. Nevertheless, surface breakup occurs many orders of  magnitude faster than one would naively think possible.  Rapid changes in magnetic topology commonly arise in both laboratory and space settings and are called fast magnetic reconnections.  

Fast magnetic reconnection is ubiquitous, and the literature is extensive.  Unfortunately, the literature grew out of two-dimensional models and ignores what appears to be the dominant effect when the magnetic field depends on all three spatial coordinates.  In three dimensions,  but not in two, the ratio $\Delta_{max}/\Delta_{min}$ between the maximum and minimum separation between two neighboring magnetic field lines at given points in time can become exponentially large on a time scale set by an ideal evolution.  When $\Delta_{min}$ is the scale over which non-ideal effects break field lines, the actual scale over which magnetic field line topology changes is $\Delta_{max}$--a change in the topology anywhere along a magnetic field line implies a change in topology everywhere along the line.  The natural timescale for fast magnetic reconnection is set by the ideal evolution times a factor that depends logarithmically on the strength of non-ideal effects, which means this factor is less than a hundred even in extreme astrophysical situations.

### Fast Breakup of Magnetic Surfaces

Numerical effects allow an unphysical breaking of magnetic surfaces.  The extent to which the surface breaking in simulations is due to numerics, rather than physics, and how that effects the reliability of disruption  simulations is unknown.  

The physics of fast magnetic reconnection giving a rapid destruction of tokamak magnetic surfaces is studied in [@fast_breakup].  As shown, an understanding of the physics gives tests for the accuracy of simulation codes and the extent to which inaccuracies affect the reliability of the simulations.

In a chaotic magnetic field, the ratio $\Delta_{max}/\Delta_{min}$ depends exponentially on the distance a neighboring pair of magnetic field lines are followed.  Magnetic field lines that lie in magnetic surfaces cannot be chaotic.  Neighboring pairs of lines in a surface or magnetic surfaces have a definite $\Delta_{max}/\Delta_{min}$ ratio at any point in time, but that ratio does depend on time.  In an ideal evolution, the time dependence of $\Delta_{max}/\Delta_{min}$ can be exponential  [@exp_separation].  An ideal evolution that strongly contorts the magnetic surfaces can cause a fast magnetic reconnection no matter how small the non-ideal effects may be. 

### Timescale for Magnetic Reconnection Effects

A magnetic field line undergoes a change in topology at a certain instant in time.  A sensible definition of a reconnection timescale requires a focus on the physical effects associated with the topology change rather than the topology change itself.  Reference [@current_flattening] shows that $j_{||}/B$ flattens to a constant along each chaotic magnetic field line on the timescale required for a shear Alfv\'en to propagate along the line.  The plasma resistivity and viscosity give diffusion of $j_{||}/B$ across the lines though the effect is generally weak.  Simple observational and theoretical considerations imply approximately a hundred toroidal transits are required for a chaotic magnetic field line to go from the central to the edge region of a tokamak plasma.   Multi-kilovolt electrons have a mean-free-path greater than a hundred times the distance around the torus, and they spread  [^5] across the plasma in 10's~$\mu$s.  Both the flattening of $j_{||}/B$ and of the spreading of the spatial distribution of hot electrons produce important effects---a spike in the plasma current, fast changes in the plasma pressure, and heat pulses.  In addition, the effects provide a diagnostic for magnetic surface breakup.

\bibliography


<script type="text/x-mathjax-config">MathJax.Hub.Config({TeX: {equationNumbers: {autoNumber: "all"}}, tex2jax: {inlineMath: [['$','$']]}});</script>
<script type="text/javascript" src="https://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.2/MathJax.js?config=TeX-AMS_HTML"></script>
