# tds-scidac.github.io
Web presence for the Tokamak Disruption Simulation SciDAC project. This repo contains the TDS website [MkDocs](https://www.mkdocs.org/) sources.

To make changes to the website you will need an install of Python version >= 3.6.9 with the following libraries:

- use MkDocs v1.0.4 with Markdown v3.0 and the latest PyYAML and mkdocs-exclude-search:
  * `pip install --upgrade --user mkdocs==1.0.4`
  * `pip install --upgrade --user Markdown==3.0`
  * `pip install --upgrade --user PyYAML`
  * `pip install --upgrade --user mkdocs-exclude-search`
  * `pip install --upgrade --user mkdocs-bibtex`
  * `pip install --upgrade --user mkdocs-macros-plugin`
- or use conda (on one lanl mac, python 3.10 does not work well)
  * `conda create -n web python=3.7`
  * `conda activate web`
  * `conda install -c conda-forge mkdocs=1.0.4`
  * `conda install -c conda-forge pyyaml`
  * `conda install -c conda-forge markdown==3.1.1`
  * `conda install -c conda-forge mkdocs-macros-plugin` or `pip install --upgrade --user mkdocs-macros-plugin`
  * `pip install --upgrade --user mkdocs-bibtex`
- newer versions may not generate correct front page (to see the installed version, use `pip show mkdocs`)
- clone this repo,
- edit or add some `.md` files (you may also need to update the `mkdocs.yml` config),
- preview locally with `mkdocs serve` (Windows users may need to specify a port, such as `mkdocs serve --dev-addr 127.0.0.1:4000`),
- publish with `mkdocs gh-deploy`.

*This website is built upon the template from the [mfem](https://mfem.org) website hosted at https://github.com/mfem/web. We thank the mfem team for their help and suggestions.*
