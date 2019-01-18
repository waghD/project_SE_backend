Projekt SE Backend
=============

Folgende Schritte sind zum starten des Programs notwendig

# Schritt 1

```python
pip install -r requirements.txt
```


# Schritt 2

```python
py manage.py migrate
```

# Schritt 3

```python
py manage.py makemigrations logistics
```
# Schritt 4

```python
py manage.py loaddata initial.json
```


# Schritt 5

```python
py manage.py createsuperuser
```

# Schritt 6

```python
py manage.py runserver
```