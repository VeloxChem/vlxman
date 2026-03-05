# Reference states

For Kohn–Sham DFT, any of the several available functionals is specified as illustrated below, see the [exchange-correlation functionals](#sec:xc-functionals) page for a complete list of available functionals.

For input text files, a detailed [list of keywords](#sec:text-file-keywords) is available.

:::{note}
By default, the Hartree–Fock method is employed. 
:::

(sec:rhf)=
## Restricted closed-shell

**Python script**

```python
import veloxchem as vlx

mol_xyz_string = """
... 
"""

molecule = vlx.Molecule.read_xyz_string(mol_xyz_string)
basis = vlx.MolecularBasis.read(molecule, "def2-svp")

scfdrv = vlx.ScfRestrictedDriver()

scfdrv.xcfun = "b3lyp"
scf_results = scfdrv.compute(molecule, basis)
```

**Text file**

```
@jobs
task: scf
@end

@method settings
basis: def2-svp
@end

@molecule
charge: 0
multiplicity: 1
xyz:
...
@end
```

(sec:rohf)=
## Restricted open-shell

**Python script**

```python
import veloxchem as vlx

mol_xyz_string = """
...
"""

molecule = vlx.Molecule.read_xyz_string(mol_xyz_string)
molecule.set_multiplicity(2)
basis = vlx.MolecularBasis.read(molecule, "6-31+G*")

scfdrv = vlx.ScfRestrictedOpenDriver()

scfdrv.xcfun = "b3lyp"
scf_results = scfdrv.compute(molecule, basis)
```

**Text file**

```
@jobs
task: roscf
@end

@method settings
basis: 6-31+G*
xcfun: b3lyp
@end

@molecule
charge: 1
multiplicity: 2
xyz:
...
@end
```

(sec:uhf)=
## Unrestricted open-shell

**Python script**

```python
import veloxchem as vlx

mol_xyz_string = """
...
"""

molecule = vlx.Molecule.read_xyz_string(mol_xyz_string)
molecule.set_multiplicity(2)
basis = vlx.MolecularBasis.read(molecule, "CC-PVDZ")

scfdrv = vlx.ScfUnrestrictedDriver()

scfdrv.xcfun = "b3lyp"
scf_results = scfdrv.compute(molecule, basis)
```

**Text file**

```
@jobs
task: uscf
@end

@method settings
basis: CC-PVDZ
xcfun: PBE0
@end

@molecule
charge: 1
multiplicity: 2
xyz:
...
@end
```
