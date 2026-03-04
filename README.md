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
  - jupyter-book
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

# Some commands

```
$ conda install jupyter-book -c conda-forge
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

# References

The file `references.bib` in the top directory is a regular BIBTEX file. Add your references in this file. A citation in the text is added with

```
{cite}`Wang2016, Schlegel2011`
```

Multiple lists of references are possible but not yet propoerly implmented.
