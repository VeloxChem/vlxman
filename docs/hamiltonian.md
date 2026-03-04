# Hamiltonian
 
For a system with $N$ electrons and $M$ nuclei in the quantum mechanical region, VeloxChem implements the nonrelativic electronic Hamiltonian

\begin{align*}
\hat{H} =
%
&- \sum_{i=1}^N
\frac{\hbar^2}{2 m_\mathrm{e}} \nabla^2_i
%
- \sum_{i=1}^N \sum_{A=1}^M
\frac{Z_A e^2}{4 \pi \varepsilon_0 |\mathbf{r}_i - \mathbf{R}_A|}\\
%
&\qquad + \sum_{i=1}^N \sum_{j>i}^N
\frac{e^2}{4 \pi \varepsilon_0 |\mathbf{r}_i - \mathbf{r}_j|}
%
+ \sum_{A=1}^M \sum_{B>A}^M
\frac{Z_A Z_B e^2}{4 \pi \varepsilon_0 |\mathbf{R}_A - \mathbf{R}_B|}
\end{align*}

introducing in order terms associated with the electronic kinetic energy, electron–nuclear attraction, electron–electron repulsion, and nuclear–nuclear repulsion. We use variables $\mathbf{r}$ and $\mathbf{R}$ to collectively denote the sets of electronic and nuclear coordinates, respectively.

In a brief notation, the electronic Hamiltonian is expressed in terms of the one- and two-electron components in addition to the nuclear repulsion term

$$
\hat{H} =
\sum_{i} \hat{h}(i) +
\sum_{j>i} \hat{g}(i,j) + 
V^\mathrm{n,rep}
$$

## Effective-core potentials

ECPs in VeloxChem follow the conventional partitioning into local and nonlocal components:

$$
\hat{V}_{\text{ECP}}(\mathbf{r})
= \hat{V}_{\text{loc}}(r)
+ \hat{V}_{\text{nl}}(\mathbf{r})
$$

Every atom described by an ECP is associated with such an operator, and they are to replace the corresponding electron–nuclear attraction terms in the one‑electron Hamiltonian. For notational convenience, the coordinate origin has here been assumed to be located at the ECP center.

### Local Component

The **local part** of the ECP represents a spherically symmetric potential applied equally to all components of the valence wave function. It often corresponds to the highest angular‑momentum channel of the pseudopotential:

$$
\hat{V}_{\text{loc}}(r)
= -\frac{Z_{\text{eff}} e^2}{4 \pi \varepsilon_0  r}
  + \sum_{k} A_k \, \frac{r^{n_k}}{r^2} e^{-a_k r^2}
$$

This term captures the screened nuclear attraction and mimics the average effect of the removed core electrons.

### Nonlocal Component

The **nonlocal projector terms** introduce angular‑momentum dependence by projecting the wave function onto specific $l$-channels:

$$
\hat{V}_{\text{nl}}
= \sum_{l} \sum_{m=-l}^{l}
    | Y_{lm} \rangle \, V_l(r) \, \langle Y_{lm} |
$$

Each $V_l(r)$ is a radial potential defined by a parameterized sum of Gaussian functions:

$$
V_l(r) = \sum_{k} A_{lk} \, r^{n_{lk}} e^{-a_{lk} r^2}
$$

These projectors enforce the correct nodal structure and scattering behaviour of the valence orbitals, preserving norm conservation and accuracy across chemical environments.

:::{note}
VeloxChem includes a set of small-core ECPs for elements starting with potassium ($Z = 19$) and ending with radon ($Z = 86$). Alternative choices of ECPs for these elements and also ECPs for other elements can be manually introduced by the user as long as they are of the form described above.
:::

## Static electric fields

A term can be added in the electronic Hamiltonian to describe the coupling of the molecular system and a time-independent (static), homogeneous, electric field, $\mathbf{F}$,

$$
\hat{V} = - \hat{\boldsymbol{\mu}} \cdot \mathbf{F}
$$

where $\hat{\boldsymbol{\mu}}$ is the electric dipole moment operator. The vectorial electric-field strength is specified in atomic units.

**Python script**

```
import veloxchem as vlx

mol_xyz_string = """
...
"""

molecule = vlx.Molecule.read_xyz_string(mol_xyz_string)
basis = vlx.MolecularBasis.read(molecule, 'def2-svp')

scf_drv = vlx.ScfRestrictedDriver()
scf_drv.filename = 'mol-field'
scf_drv.electric_field = [0.01, 0.0, 0.0]  # [x, y, z] components
scf_results = scf_drv.compute(molecule, basis)
```
Download a {download}`Python script <../input_files/pna-field.py>` type of input file to perform an SCF calculation for *para*-nitroaniline in the presence of a static electric field.

**Text file**

```
@jobs
task: scf
@end

@method settings
basis: def2-svp
electric field: 0, 0.001, -0.002
@end

@molecule
charge: 0
multiplicity: 1
xyz:
...
@end
```

Download a {download}`text format <../input_files/pna-field.inp>` type of input file to perform an SCF calculation for *para*-nitroaniline in the presence of a static electric field.

```{image} ../images/pna.png
:alt: cover
:class: bg-primary mb-1
:width: 400px
:align: center
```
