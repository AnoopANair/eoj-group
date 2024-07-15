
---
title: "Implementation of Constrained DFT for Computing Charge Transfer Rates within the Projector Augmented Wave Method"

authors:
- Marko Melander  
- Elvar Ö. Jónsson 
- Jens J. Mortensen 
- Tejs Vegge 
- Juan Maria Garcı́a Lastra 
author_notes:
- 
date: "2016-10-17"
doi: "https://doi.org/10.1021/acs.jctc.6b00815"


publishDate: 

publication_types: ["article-journal"]



# Publication name and optional abbreviated publication name.
publication: "Journal of Chemical Theory and Computation"
publication_short: ""

abstract: Combining constrained density function theory (cDFT) with Marcus theory is an efficient and promising way to address charge transfer reactions. Here, we present a general and robust implementation of cDFT within the projector augmented wave (PAW) framework. PAW pseudopotentials offer a reliable frozen-core electron description across the whole periodic table, with good transferability, as well as facilitate the extraction of all-electron quantities. The present implementation is applicable to two different wave function representations, atomic-centered basis sets (LCAO) and the finite-difference (FD) approximation utilizing real-space grids. LCAO can be used for large systems, molecular dynamics, or quick initialization, while more accurate calculations are achieved with the FD basis. Furthermore, the calculations can be performed with flexible boundary conditions, ranging from isolated molecules to periodic systems in one-, two-, or three-dimensions. As such, this implementation is relevant for a wide variety of applications. We also present how to extract the electronic coupling element and reorganization energy from the resulting diabatic cDFT-PAW wave functions for the parametrization of Marcus theory. Here, the combined method is applied to important test cases where practical implementations of DFT fail due to the self-interaction error, such as the dissociation of the helium dimer cation, and it is compared to other established cDFT codes. Moreover, for charge localization in a diamine cation, where it was recently shown that the commonly used generalized gradient and hybrid functionals of DFT failed to produce the localized state, cDFT produces qualitatively and quantitatively accurate results when benchmarked against self-interaction corrected DFT and high-level CCSD(T) calculations at a fraction of the computational cost.

# Summary. An optional shortened abstract.
summary: 

tags:

featured: false

url: "content/publication/Melander:2016aa"
url_pdf: https://pubs.acs.org/doi/epdf/10.1021/acs.jctc.6b00815

image:
  caption: '[](./featured.jpg)'
  focal_point: ""
  preview_only: false

projects: []

slides: 
---

