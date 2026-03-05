(sec:vib_spect)=
# Vibrational spectroscopies

Calculations of normal modes are performed with the aid of [geomeTRIC](https://pypi.org/project/geometric/).

The associated IR spectrum is calculated by default also when Raman or resonance Raman calculations are requested except if specified otherwise.

(sec:ir)=
## Infrared

**Python script**

```python
import veloxchem as vlx

xyz="""
... 
"""

molecule = vlx.Molecule.read_xyz_string(xyz)
basis = vlx.MolecularBasis.read(molecule, 'def2-svp')

scf_drv = vlx.ScfRestrictedDriver()
scf_drv.filename = 'mol-ir'
scf_drv.xcfun = 'b3lyp'
results = scf_drv.compute(molecule, basis)

vib_drv = vlx.VibrationalAnalysis(scf_drv)
vib_drv.do_ir = True
scf_drv.filename = 'mol-ir'
vib_results = vib_drv.compute(molecule, basis)
```

**Text file**

```
@jobs
task: vibrational
@end

@method settings
xcfun: b3lyp
basis: def2-svp
@end

@vibrational
do_ir: yes
@end

@molecule
charge: 0
multiplicity: 1
xyz:
...                     
@end
```

(sec:raman)=
## Raman

**Python script**

```python
import veloxchem as vlx

xyz="""
... 
"""

molecule = vlx.Molecule.read_xyz_string(xyz)
basis = vlx.MolecularBasis.read(molecule, 'def2-svp')

scf_drv = vlx.ScfRestrictedDriver()
scf_drv.filename = 'mol-raman'
scf_drv.xcfun = 'b3lyp'
results = scf_drv.compute(molecule, basis)

vib_drv = vlx.VibrationalAnalysis(scf_drv)
vib_drv.do_ir = False
vib_drv.do_raman = True
vib_drv.filename = 'mol-raman'
vib_results = vib_drv.compute(molecule, basis)
```

**Text file**

```
@jobs
task: vibrational
@end

@method settings
xcfun: b3lyp
basis: def2-svp
@end

@vibrational
do_raman: yes
@end

@molecule
charge: 0
multiplicity: 1
xyz:
...                     
@end
```

(sec:rrs)=
## Resonance Raman

**Python script**

```python
import veloxchem as vlx

xyz="""
... 
"""

molecule = vlx.Molecule.read_xyz_string(xyz)
basis = vlx.MolecularBasis.read(molecule, 'def2-svp')

scf_drv = vlx.ScfRestrictedDriver()
scf_drv.filename = 'mol-reson-raman'
scf_drv.xcfun = 'b3lyp'
results = scf_drv.compute(molecule, basis)

vib_drv = vlx.VibrationalAnalysis(scf_drv)
vib_drv.do_ir = False
vib_drv.do_raman = True
vib_drv.filename = 'mol-reson-raman'
vib_results = vib_drv.compute(molecule, basis)
```

**Text file**

```
@jobs
task: vibrational
@end

@method settings
xcfun: b3lyp
basis: def2-svp
@end

@vibrational
do_resonance_raman: yes
frequencies: 0.05-0.10 (0.05)
@end

@molecule
charge: 0
multiplicity: 1
xyz:
...                      
@end
```
