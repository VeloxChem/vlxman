# Visualization

# Cube files

```
@jobs
task: visualization
@end

@method settings
basis: def2-svp
@end

@visualization
cubes: density(alpha), mo(homo)
files: density.cube, homo.cube
@end

@molecule
charge: 0
multiplicity: 1
units: au
xyz:  
O   0.0   0.0   0.0
H   0.0   1.4   1.1
H   0.0  -1.4   1.1
@end 
```


