## Local Development SETUP

```bash
git clone https://github.com/nwizugbesamson/UniversityTutoringManager.git

cd UniversityTutoringManager/backend

pip install poetry

poetry config virtualenvs.in-project true

poetry install

poetry shell

uvicorn manage:app --host 0.0.0.0 --port 8080
```
