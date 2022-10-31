# ASCII ART

```
             _____    _____   _____   _____                 _____    _______ 
    /\      / ____|  / ____| |_   _| |_   _|        /\     |  __ \  |__   __|
   /  \    | (___   | |        | |     | |         /  \    | |__) |    | |
  / /\ \    \___ \  | |        | |     | |        / /\ \   |  _  /     | |
 / ____ \   ____) | | |____   _| |_   _| |_      / ____ \  | | \ \     | |   
/_/    \_\ |_____/   \_____| |_____| |_____|    /_/    \_\ |_|  \_\    |_|
```

This is one of my very first school project, which was firstly made in association with [Jérémie Musoki](https://github.com/jeremBWO) and [Matteo Darwich](https://github.com/Mattdrw).

You can find the original subject [here](./ascii_art.md).



## Table of content
- [ASCII ART](#ascii-art)
  - [Table of content](#table-of-content)
  - [Features](#features)
  - [How to install](#how-to-install)

## Features
* Display ascii art messages
* Choose display font, color, background color and effect
* Letter spacement and line length

## How to install

```bash
# Clone git repository
git clone https://github.com/GouruRK/ASCII-ART.git

# Install unidecode lib
python3 -m pip install unidecode

# Go into the repo
cd ASCII-ART

# Launch
python3 main.py <text>
```

Optionnals arguments :

```bash
# Show help message
python3 main.py -h

# Text color
python3 main.py <text> -c <grey | red | green | yellow | blue | magenta | cyan | white>

# Text background color
python3 main.py <text> -oc <grey | red | green | yellow | blue | magenta | cyan | white>

# Text effects
python3 main.py <text> -e <bold | dark | underline | blink | reverse | concealed>

# Letter spacing
python3 main.py <text> -ls <space>

# Max line length
python3 main.py <text> -l <space>
```

Note that windows user may type `py` instead of `python3`.

Some effects may not work depending on the system you'r using. See [this page](https://pypi.org/project/termcolor/) for more informations.

Fonts are coming from [patorjk](http://www.patorjk.com/software/taag) website.

___

Check out my other projects on github : [Gouru](https://github.com/GouruRK/).