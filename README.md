# Compiled page
https://kthpanor.github.io/vlxman/docs/intro.html

# Some commands

```
$ conda install jupyter-book -c conda-forge
$ git clone https://github.com/kthpanor/vlxman.git
$ cd vlxman
$ vi docs/dft.md
$ jupyter-book build .
$ open _build/html/index.html
```

# Publish the html-version

```
$ pip install ghp-import
$ ghp-import -n -p -c veloxchem.org -f _build/html
```

The flag `-c veloxchem.org` will create a file named `CNAME` in the `gh-pages` branch containing the published pages. This file contains a single line with `veloxchem.org` that is needed to be able to reach the manual from the `https://veloxchem.org/` domain. 

# References
The file `references.bib` in the top directory is a regular BIBTEX file. Add your references in this file. A citation in the text is added with

```
{cite}`Wang2016, Schlegel2011`
```

Multiple lists of references are possible but not yet propoerly implmented.
