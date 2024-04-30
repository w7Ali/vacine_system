# Project Name Covid
## Setup Project 
```python
python3 -m venv .venv
source .venv/bin/activate
pip3 install -r requirements.txt
python manage.py makemigrations hospitals
python manage.py migrate hospitals

```