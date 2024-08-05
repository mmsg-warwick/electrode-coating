# Electrode coating simulation package

[![Actions Status][actions-badge]][actions-link]
[![Documentation Status][rtd-badge]][rtd-link]
[![codecov](https://codecov.io/gh/mmsg-warwick/electrode-coating/graph/badge.svg?token=noM4mVgDpE)](https://codecov.io/gh/mmsg-warwick/electrode-coating)

[![PyPI version][pypi-version]][pypi-link]
[![Conda-Forge][conda-badge]][conda-link]
[![PyPI platforms][pypi-platforms]][pypi-link]

[![GitHub Discussions][github-discussions-badge]][github-discussions-link]

<!-- SPHINX-START -->

<!-- prettier-ignore-start -->

[actions-badge]:            https://github.com/mmsg-warwick/electrode-coating/workflows/CI/badge.svg
[actions-link]:             https://github.com/mmsg-warwick/electrode-coating/actions
[conda-badge]:              https://img.shields.io/conda/vn/conda-forge/electrode-coating
[conda-link]:               https://github.com/conda-forge/electrode-coating-feedstock
[github-discussions-badge]: https://img.shields.io/static/v1?label=Discussions&message=Ask&color=blue&logo=github
[github-discussions-link]:  https://github.com/mmsg-warwick/electrode-coating/discussions
[pypi-link]:                https://pypi.org/project/electrode-coating/
[pypi-platforms]:           https://img.shields.io/pypi/pyversions/electrode-coating
[pypi-version]:             https://img.shields.io/pypi/v/electrode-coating
[rtd-badge]:                https://readthedocs.org/projects/electrode-coating/badge/?version=latest
[rtd-link]:                 https://electrode-coating.readthedocs.io/en/latest/?badge=latest

<!-- prettier-ignore-end -->

## 🚀 Installing the package
The package is not yet available on PyPI so you need to install it from the source code. To do so, first clone the repository:

```bash
git clone git@github.com:mmsg-warwick/electrode-coating.git
```

If you do not have nox installed, install it with

```bash
python3 -m pip install nox
```

Then, navigate to the repository and run

```bash
nox -s dev
```

This will create a virtual environment called `venv` in your current directory and install the package in editable mode with all the development dependencies. To activate the virtual environment, run

```bash
source env/bin/activate
```

If needed, you can deactivate your virtual environment with

```bash
deactivate
```
