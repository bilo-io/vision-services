# Python Project

## Quickstart

| Command                                        | Description                                             |
| :--------------------------------------------- | :------------------------------------------------------ |
| 1. `python3 -m venv .env`                      | To create a virtual environment for this project        |
| 2. `source .env/bin/activate`                  | To activate the Virtual Environment                     |
| 3. `pip install -r requirements.txt`           | To install dependencies                                 |
| 4. `pip freeze \| xargs pip uninstall -y`      | To clean `venv`                                         |
| 5. `uvicorn main:app --reload`                 | To run the app in watch mode                            |
| 6. `sudo lsof -t -i tcp:8000 \| xargs kill -9` | Kill process listening to TCP connectons on port `8000` |
| 7. `deactivate`                                | To deactivate the Virtual Environment                   |

> Swagger docs: [http://0.0.0.0:8000/docs](http://0.0.0.0:8000/docs)

## Docker

| Command                                                 | Description      |
| :------------------------------------------------------ | :--------------- |
| `docker build -t myminimalapi .`                        | Builds the image |
| `docker run -e APP_WORKERS=8 -p 8000:8000 myminimalapi` | Runs the image   |

## Project Structure

```text
vision-services/
│
├── main.py
├── requirements.txt
└── src/
    ├── services/
    │   └── image.py
    └── models.py
```
