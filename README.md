# Number Formatter
A simple [FastAPI](https://fastapi.tiangolo.com/) application with a REST endpoint accepts a numeric type and returns a truncated, "pretty" string version.

Examples:
* input: 500 output 500
* input: 3400 outputs 3.5k
* input: 1000000 output: 1M
* input: 2500000.34 output: 2.5M
* input: 1123456789 output: 1.1B

## Quick Start:

1. Install poetry from https://python-poetry.org/docs/:
   
2. Run: `poetry install`
3. To start the application, run: `uvicorn app.main:app --reload`

Note: If you want to test the application, run: `pytest`