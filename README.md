# divin-calcutils

A small, dependency-free Python package with basic arithmetic and statistical
helpers. The importable Python package is named `calcutils`.

## Installation

```bash
python -m pip install divin-calcutils
```

## Usage

```python
from calcutils import add, average, multiply

print(add(10, 25))                 # 35
print(multiply(4, 5))              # 20
print(average([10, 20, 30, 40]))   # 25.0
```

`average()` returns `0.0` when given an empty iterable.

## Development

Build the source distribution and wheel from the project root:

```bash
python -m pip install --upgrade build
python -m build
```

The distribution files are written to `dist/`. To publish them to TestPyPI,
configure a TestPyPI API token and run:

```bash
python -m pip install --upgrade twine
python -m twine upload --repository testpypi dist/*
```

The distribution name `divin-calcutils` must be available on the registry
before it can be published. Add your author details and project URLs to
`pyproject.toml` before release if you want them shown in package metadata.

## License

This project is licensed under the MIT License. See [LICENSE](LICENSE).
