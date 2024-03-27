# Virtual Environment

A virutal environment is a Python environment such that the Python interpreter, libraries and scripts installed into it are isolated from those installed in other virtual environments, and (by default) any libraries installed in a "system" Python, i.e., one which is installed as part of the operating system.

## Initialize & Activate

**Initialize venv**

```sh
python -m venv [project_dir]/[venv_name] --system-site-packages
```

**Activate venv**

```sh
source [project_dir]/[venv_name]/bin/activate
```

## Environment Info

**Check active environment**

```sh
which python
```

**List local (environment) packages**

```sh
pip list --local
```

## Delete & Deactivate

**Deactivate Environment**

```sh
deactivate
```

**Delete Environment**

Delete the environment folder

## Requirements

**Generate Requirements**

```
pip freeze > requirements.txt
```

**Install Requirements**

```
pip install -r requirements.txt
```
