# tinkoff_app
Test application for interview


## Development

### Requirements

* python 3.8
* pipenv

Install pipenv package:
```
pip install pipenv
```

Install dev envirionment:
```
pipenv install
```

Start local dev server:
```
pipenv shell
uvicorn test_app.fastapi:app --reload
```
