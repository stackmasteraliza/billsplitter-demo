# billsplitter

A tiny library to split a restaurant bill across people, with tip and rounding.

```python
from billsplitter import split_bill

split_bill(100, 4, tip_percent=20)   # -> 30.00  (each person, tip included)
```

## Running the tests

```bash
pip install -e .
pip install pytest
pytest
```

> This project ships with a deliberate bug (the tip is computed but never
> added) so you can watch **[FixForward](https://github.com/stackmasteraliza/fixforward)**
> detect the failing tests, ask GitHub Copilot for a fix, verify it, and open a PR.

## .gitignore
See `.gitignore`.
