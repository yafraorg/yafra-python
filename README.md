# pythonsamples
Python Examples / Templates

## use cases
The following use cases are covered:

folder | use case | dependencies | remarks
-- | -- | -- | --
database | work with DB's | mariadb, sqllite | simple data handling
extractor | extract text from image, pdf | pillow, wand, pyocr | text extraction

## setup
* Install Python 3.12+
* Install `uv` from https://docs.astral.sh/uv/
* Run `./setup.sh` (macOS/Linux) or `./setup.ps1` (Windows) from repo root

Each subfolder is a standalone `uv` project with its own `pyproject.toml` and `uv.lock`.
To run an app, sync and execute inside that folder, for example:

```bash
cd fastapi
uv sync
uv run python main.py
```

# Database
https://sqlmodel.tiangolo.com
SQL Alchemy
sqllite async