```bash
git clone https://github.com/vilus/for_denga.git
cd for_denga
virtualenv .venv
. .venv/bin/activate # or on win - .venv\scripts\activate
pip install -r parens/requirements.txt
pytest -v parens/tests.py
```
