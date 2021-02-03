# welo.tv test

* **Python version**: `3.6`

# Table of contents

* [Features](#features)   
* [Usage](#usage)  
* [TODO](#todo)  
* [Comments](#comments)  

## Features

* Justify a given text
* Balance the extra spaces between words
* Print the justified text in the output 


## Usage
```bash
$ python justify_line.py <text_to_justify> <line_width> 
```

## Example

```bash
$ python justify_line.py 'La historia de la ópera tiene una duración relativamente corta dentro del contexto de la historia de la música en general: apareció en 1597, fecha en que se creó la primera ópera.' 30

La  historia de la ópera tiene
una   duración   relativamente
corta  dentro  del contexto de
la  historia  de  la música en
general:   apareció  en  1597,
fecha   en   que  se  creó  la
ópera.
```

## Development scenario

* `Conda` environment.
* `Jupyterlab` for draft code.
* `Pycharm` IDE.
* `black`, `flake8` and `isort` for linting.

## TODO

- [ ] make more tests
- [ ] catch more edge cases
- [ ] add the posibility of cut words

## Comments

A pythonic way to do this:

`textwrap.shorten("Hello  world!", width=12)`

