# Python 3 Pure Starter Template with Pipenv (Project Dependencies Manager)

## 1. Setting up Python before launching the project:

#### Install "Python Version Manager" (pyenv):

```bash
curl https://pyenv.run | bash
```

```bash
# add this commands:
export PYENV_ROOT="$HOME/.pyenv"
command -v pyenv >/dev/null || export PATH="$PYENV_ROOT/bin:$PATH"
eval "$(pyenv init -)"
```

```bash
# here:
nano ~/.bash_profile
```

```bash
# here:
nano ~/.profile
```

```bash
# and here:
nano ~/.bashrc
```

```bash
# then add this commands:
eval "$(pyenv virtualenv-init -)"
```

```bash
# here:
nano ~/.bashrc
```

#### Restart terminal and install Python LTS:

```bash
pyenv install 3.12.0
pyenv global 3.12.0
```

#### Check Python version:

```bash
python3 --version
```

#### Upgrade PIP manager to latest version [maybe with sudo]:

```bash
pip install --upgrade pip
```

## 2. Install the package manager and run the project:

#### Install Project Dependencies Manager (pipenv) [maybe with sudo]:

```bash
pip install --user pipenv
```

#### Run the project using Pipfile script "dev":

```bash
pipenv run dev
```

#### To install new packages with pipenv:

```bash
pipenv install [package_name]
```

#### To install all packages from Pipfile:

```bash
pipenv install
```

## If you want to share your code with someone, but make it unreadable:

#### 1. Obfuscate using https://pyob.oxyry.com:

#### 2. Compile using:

```bash
python3 -OO -m py_compile [your_file_name].py
```

### 3. Run:

```bash
python3 __pycache__/[your_file_name].pyc
```
