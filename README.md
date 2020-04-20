# Molecule parser module

This application is a molecule parser. We can parse a chemical formula and generate a python dictionary with the number of atoms of each element contained in the molecule.

## Installation

No python packages necessary to run application, but you can install requirements :

```bash
pip install -r requirements.txt
```

To be able to launch unitary tests.

After that, you can import the main function, parse_molecule like this :

```bash
from molecule_parser import parse_molecule
```

## Launching tests and checking source code

To check if source code is pep8 compliant, launch :

```bash
flake8 --ignore E501
```

NB: too long lines are ignored

Command to check coverage of the source code and run unit tests :

```bash
py.test tests/test_*.py -vv
```
