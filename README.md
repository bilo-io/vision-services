# Python Project

## Quickstart

| Command                                   | Description                                      |
| :---------------------------------------- | :----------------------------------------------- |
| 1. `python3 -m venv .env`                 | To create a virtual environment for this project |
| 2. `source .env/bin/activate`             | To activate the Virtual Environment              |
| 3. `pip install -r requirements.txt`      | To install dependencies                          |
| 4. `pip freeze \| xargs pip uninstall -y` | To clean `venv`                                  |
| 5. `python3 watcher.py & python3 main.py` | To run the app in watch mode                     |
| 6. `deactivate`                           | To deactivate the Virtual Environment            |

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
