(sec:pes)=
# Potential energy surfaces

Structure optimizations are performed with the aid of geomeTRIC {cite}`geomeTRIC`.

## Ground state optimization

**Python script**
```
import veloxchem as vlx

xyz="""
... 
"""

molecule = vlx.Molecule.read_xyz_string(xyz)
basis = vlx.MolecularBasis.read(molecule, 'def2-svp')

scf_drv = vlx.ScfRestrictedDriver()
scf_drv.filename = 'mol-opt'
scf_drv.xcfun = 'b3lyp'
scf_drv.dispersion = True
results = scf_drv.compute(molecule, basis)

opt_drv = vlx.OptimizationDriver(scf_drv)
opt_drv.filename = 'mol-opt'
opt_results = opt_drv.compute(molecule, basis, results)
```

Download a {download}`Python script <../input_files/bithio-S0-opt.py>` type of input file to perform an optimization for the bithiophene molecule at the B3LYP+D4/def2-svp level of theory.

**Text file**

Please refer to the [keyword list](#sec:opt-keywords) for a complete set of options. Dispersion can be activated in the `@method settings` section by using the keyword `dispersion`.

```
@jobs
task: optimize
@end

@method settings
xcfun: b3lyp
basis: def2-svp
dispersion: yes # use dft-d4 correction
@end

@molecule
charge: 0
multiplicity: 1
xyz:
...
@end
```

Download a {download}`text file <../input_files/bithio-S0-opt.inp>` type of input file to perform an optimization for the bithiophene molecule at the B3LYP+D4/def2-svp level of theory.

```{image} ../images/bithio-S0-opt.gif
:alt: cover
:class: bg-primary mb-1
:width: 400px
:align: center
```

## Excited state optimization

**Python script**
```
import veloxchem as vlx

xyz="""
... 
"""

molecule = vlx.Molecule.read_xyz_string(xyz)
basis = vlx.MolecularBasis.read(molecule, 'def2-svp')

scf_drv = vlx.ScfRestrictedDriver()
scf_drv.filename = 'mol-opt'
scf_drv.xcfun = 'b3lyp'
scf_drv.dispersion = True
scf_results = scf_drv.compute(molecule, basis)

rsp_drv = vlx.LinearResponseEigenSolver()
rsp_drv.nstates = 2
rsp_results = rsp_drv.compute(molecule, basis, scf_results)

grad_drv = vlx.TddftGradientDriver(scf_drv)
grad_drv.state_deriv_index = 1

opt_drv = vlx.OptimizationDriver(grad_drv)
opt_drv.filename = 'mol-S1-opt'
opt_results = opt_drv.compute(molecule, basis, scf_drv, rsp_drv, rsp_results)
```

Download a {download}`Python script <../input_files/bithio-S1-opt.py>` type of input file to perform an optimization of the first excited state of bithiophene molecule at the B3LYP/def2-svp level of theory.

**Text file**

To optimize an excited state, you need to use the task optimize and to specify which state you want to optimize with the `state_deriv_index:` keyword in the `@gradient` section.

```
@jobs
task: optimize
@end

@response
property: absorption
nstates: 2
@end

@gradient
state_deriv_index: 1
@end

@method settings
xcfun: b3lyp
basis: def2-svp
@end

@molecule
charge: 0
multiplicity: 1
xyz:
...
@end
```

Download a {download}`text file <../input_files/bithio-S1-opt.inp>` type of input file to perform an optimization of the first excited state of bithiophene molecule at the B3LYP/def2-svp level of theory.

```{image} ../images/bithio-S1-opt.gif
:alt: cover
:class: bg-primary mb-1
:width: 400px
:align: center
```

## Constrained optimization

Internal coordinates (distances, angles, dihedrals) can be constrained during the molecular structure optimization with use of either the `set`, `freeze`, or `scan` options. 

### Set or freeze internal coordinate

`set` will aim at converging an internal coordinate to a desired value while `freeze` will keep it at its initial value. 

**Python script**
```
import veloxchem as vlx

xyz="""
...
"""

molecule = vlx.Molecule.read_xyz_string(xyz)
basis = vlx.MolecularBasis.read(molecule, 'def2-svp')

scf_drv = vlx.ScfRestrictedDriver()
scf_drv.filename = 'bithio-freeze'
scf_drv.xcfun = 'b3lyp'
results = scf_drv.compute(molecule, basis)

opt_drv = vlx.OptimizationDriver(scf_drv)
opt_drv.constraints = [ "set dihedral 1 3 4 2 90.0", "freeze distance 3 4"]
opt_drv.filename = 'bithio-freeze'
opt_results = opt_drv.compute(molecule, basis, results)
```

Download a {download}`Python script <../input_files/bithio-freeze.py>` type of input file to perform a optimization of the bithiophene molecule at the B3LYP/def2-svp level of theory where the inter-ring distance has been frozen to the initial geometry and where the inter-ring dihedral (S-C-C-S) has been constrained to 90°.

**Text file**

```
@jobs
task: optimize
@end

@method settings
xcfun: b3lyp
basis: def2-svp
@end

@optimize
set dihedral 1 3 4 2 90.0
freeze distance 3 4
@end

@molecule
charge: 0
multiplicity: 1
xyz:
...
@end

```

Download a {download}`text file <../input_files/bithio-freeze.inp>` type of input file to perform a optimization of the bithiophene molecule at the B3LYP/def2-svp level of theory where the inter-ring distance has been frozen to the initial geometry and where the inter-ring dihedral (S-C-C-S) has been constrained to 90°.

```{image} ../images/bithio-freeze.gif
:alt: cover
:class: bg-primary mb-1
:width: 400px
:align: center
```

### Scan coordinate

`scan` will scan an internal coordinate from an initial to a final value in a given number of steps. 

```
scan distance 6 1 1.4 1.5 9
scan angle    6 1 2 100 110 9
scan dihedral 6 1 2 3 0 360 19
```

**Python script**

```
import veloxchem as vlx

xyz="""
...
"""

molecule = vlx.Molecule.read_xyz_string(xyz)
basis = vlx.MolecularBasis.read(molecule, 'def2-svp')

scf_drv = vlx.ScfRestrictedDriver()
scf_drv.filename = "bithio-scan"
scf_drv.xcfun = "b3lyp"
results = scf_drv.compute(molecule, basis)

opt_drv = vlx.OptimizationDriver(scf_drv)
opt_drv.constraints = ["scan dihedral 1 3 4 2 180 0 9"]
opt_drv.filename = "bithio-scan"
opt_results = opt_drv.compute(molecule, basis, results)
```

Download a {download}`Python script <../input_files/bithio-scan.py>` type of input file to perform a relaxed scan of the bithiophene molecule at the B3LYP/def2-svp level of theory where the inter-ring dihedral (S-C-C-S) is scanned from 180° to 0° in 9 steps.

**Text file**

```
@jobs
task: optimize
@end

@method settings
xcfun: b3lyp
basis: def2-svp
@end

@optimize
scan dihedral 1 3 4 2 180 0 9
@end

@molecule
charge: 0
multiplicity: 1
xyz:
...
@end

```

Download a {download}`text file <../input_files/bithio-scan.inp>` type of input file to perform a relaxed scan of the bithiophene molecule at the B3LYP/def2-svp level of theory where the inter-ring dihedral (S-C-C-S) is scanned from 180° to 0° in 9 steps.

```{image} ../images/bithio-scan.gif
:alt: cover
:class: bg-primary mb-1
:width: 400px
:align: center
```
## Transition state optimisation
`transition` will optimize a transition state structure. This requires an initial guess structure that is close to the actual transition state. 

**Python script**
```
import veloxchem as vlx

xyz = """
...
"""

molecule = vlx.Molecule.read_xyz_string(xyz)
molecule.set_charge(-1)
basis = vlx.MolecularBasis.read(molecule, "def2-svp")

scf_drv = vlx.ScfRestrictedDriver()
scf_drv.xcfun = "B3LYP"
scf_results = scf_drv.compute(molecule, basis)

opt_drv = vlx.OptimizationDriver(scf_drv)
opt_drv.transition = True
opt_results = opt_drv.compute(molecule, basis, scf_results)

```
Download a {download}`Python script <../input_files/Sn2-ts.py>` type of input file to perform a transition state optimization for the SN2 reaction between methyl chloride and hydroxide at the B3LYP/def2-svp level of theory.
**Text file**
```
@jobs
task: optimize
@end

@method settings
xcfun: b3lyp
basis: def2-svp
dispersion: yes # use dft-d4 correction
@end

@optimize
transition: yes
@end

@molecule
charge: -1
multiplicity: 1
xyz:
...
@end
```
Download a {download}`text file <../input_files/Sn2-ts.inp>` type of input file to perform a transition state optimization for the SN2 reaction between methyl chloride and hydroxide at the B3LYP/def2-svp level of theory.
### Guessing initial transition state structures
The transition-state guesser can be used to efficiently calculate an initial guess for a transition state structure. More information can be found in the [eChem book](https://kthpanor.github.io/echem/docs/mol_struct/ts_guesser.html)
**Python script**
```
import veloxchem as vlx

rea1 = vlx.Molecule.read_smiles("[Br]")
rea2 = vlx.Molecule.read_smiles("CCl")
rea1.set_charge(-1)

pro1 = vlx.Molecule.read_smiles("[Cl]")
pro2 = vlx.Molecule.read_smiles("CBr")
pro1.set_charge(-1)

tsguesser = vlx.TransitionStateGuesser()
results = tsguesser.find_transition_state([rea1, rea2], [pro1, pro2])
```
Download a {download}`Python script <../input_files/Sn2-guess_ts.py>` type of input file to perform a force-field based generation of an initial guess structure for the transition state of the SN2 reaction between methyl chloride and hydroxide.

## Verification of transition state structure with IRC
`irc` will perform an intrinsic reaction coordinate (IRC) calculation to verify that a transition state structure connects the expected reactant and product structures.

**Python script**
```
import veloxchem as vlx

xyz = """
...
"""
molecule = vlx.Molecule.read_xyz_string(xyz)
molecule.set_charge(-1)
basis = vlx.MolecularBasis.read(molecule, "def2-svp")

scf_drv = vlx.ScfRestrictedDriver()
scf_drv.xcfun = "B3LYP"
scf_results = scf_drv.compute(molecule, basis)

opt_drv = vlx.OptimizationDriver(scf_drv)
opt_drv.irc = True
opt_results = opt_drv.compute(molecule, basis, scf_results)

```
Download a {download}`Python script <../input_files/Sn2-irc.py>` type of input file to perform an IRC calculation for the transition state of the SN2 reaction between methyl chloride and hydroxide at the B3LYP/def2-svp level of theory.

**Text file**
```
@jobs
task: optimize
@end

@method settings
xcfun: b3lyp
basis: def2-svp
dispersion: yes # use dft-d4 correction
@end

@optimize
irc: yes
@end

@molecule
charge: -1
multiplicity: 1
xyz:
...
@end
```

Download a {download}`text file <../input_files/Sn2-irc.inp>` type of input file to perform an IRC calculation for the transition state of the SN2 reaction between methyl chloride and hydroxide at the B3LYP/def2-svp level of theory.