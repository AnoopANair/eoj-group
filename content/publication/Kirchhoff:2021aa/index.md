
---
title: "Elastic Collision Based Dynamic Partitioning Scheme for Hybrid Simulations."

authors:
- Björn Kirchhoff  
- Elvar Örn Jónsson 
- Asmus Ougaard Dohn 
- Timo Jacob  
- Hannes Jónsson 
author_notes:
- 
date: "2021-08-30"
doi: "https://doi.org/10.1021/acs.jctc.1c00522"


publishDate: 

publication_types: ["article-journal"]



# Publication name and optional abbreviated publication name.
publication: "J Chem Theory Comput"
publication_short: ""

abstract: In hybrid simulations, such as the QM/MM approach, the system is partitioned into regions that are treated at different levels of theory. The key question then becomes how to evaluate the interactions between particles on opposite sides of the boundary. One approach is to place the boundary in such a way that particles near the boundary on both sides are of the same type, thus simplifying the evaluation of the interactions. If mobile particles are present, such as solvent molecules, and particles are allowed to cross the boundary, the conservation of energy and atomic forces is problematic unless the computational effort is increased significantly. By preventing particles from crossing the boundary but allowing the boundary to be flexible, an accurate estimate of average thermodynamic properties is obtained in principle as illustrated by the flexible inner region ensemble separator (FIRES) method [C. Rowley and B. Roux, J. Chem. Theory Comput. 2012, 8, 3526]. In FIRES, a harmonic restraint is applied to particles near the boundary. Therefore, it can occur that particle cross the boundary to some extent resulting in anomalies in the particle density. Here, a constraint approach is presented where particles instantaneously scatter from the boundary. This scattering-adapted FIRES (SAFIRES) implementation makes use of a variable-time-step propagation algorithm where the time step is scaled automatically to identify the moment a collision should occur. If the length of the time step is kept constant, this propagator reduces to a regular Langevin dynamics algorithm, and to the velocity Verlet algorithm for conservative dynamics if the friction coefficient is set to zero. Correct average ensemble statistics are obtained as demonstrated in simulations where, for testing purposes, the particles in the two regions are treated at the same level of theory, namely, a homogeneous Lennard-Jones (LJ) liquid and liquid water based on the TIP4P potential function. In order to illustrate this approach in solid–liquid interface simulations, a LJ liquid in contact with the surface of a crystal is also simulated. The simulations using SAFIRES are shown to reproduce the unconstrained reference simulations without significant deviations in the particle density and the dynamics are shown to conserve energy when coupling to the heat bath is turned off.

# Summary. An optional shortened abstract.
summary:

tags:

featured: false

url: "content/publication/Kirchhoff:2021aa"
url_pdf: https://pubs.acs.org/doi/epdf/10.1021/acs.jctc.1c00522

image:
  caption: '[](./featured.jpg)'
  focal_point: ""
  preview_only: false

projects: []

slides: 
---

