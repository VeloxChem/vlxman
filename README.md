# Locaion of the web pages on the GitHub repo.

https://veloxchem.github.io/vlxman/docs/intro.html

# Environment YML file

To contribute to the manual, create an environment with the Jupyter book software.

```
name: vlxman 
channels:
  - conda-forge
  - veloxchem
dependencies:
  - python>=3.10
  - jupyter-book>=2.1
  - jupyterlab
  - jupyterlab-spellchecker
  - jupyterlab_code_formatter
  - black
  - isort
  - ghp-import
  - k3d
  - ipympl
  - ipywidgets
  - openmm
  - py3dmol
  - pymbar
  - rdkit
  - veloxchem
```

# Get a local copy of the manual

```
$ git clone https://github.com/VeloxChem/vlxman.git
$ cd vlxman
$ jupyter-book start
$ open http://localhost:3000/
```
The browser will show the Jupyter book and interactively update it as you edit pages in JupyterLab or any other tool.

# Publish the manual

```
$ git pull
$ git commit -m 'comment on your modifications'
$ git push
```

# Style directives

- Python script input files are created as code cells and executed. Remove the output from the manual with the tag `remove-output`
- Text format input files are formatted as code with syntax:

````
:::{code}
my input file
:::
````

- Images are included with the syntax:

````
:::{image} ../images/myfig.png
:width: 400px
:align: left
:::
````

- Figures are included with the syntax:

````
:::{figure} ../images/myfig.png
:width: 400px
:align: left

Figure: My figure caption.
:::
````

- Internal links in the manual are created with the syntax:

```
[visible text](#sec:link-name)
```

- Link targets are created with the syntax:

```
(sec:link-name)=
```

# References

The file `references.bib` in the top directory is a regular BIBTEX file. Add your references in this file. A citation in the text is added with

```
{cite}`Wang2016, Schlegel2011`
```

Multiple lists of references are possible but not yet propoerly implmented.
