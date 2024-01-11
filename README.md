# Healthcare Management


## Table of Contents

- [About](#about)
- [Installation](#installation)
- [Usage](#usage)
- [Features](#features)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)

## About

[Provide a more detailed description of your project. What problem does it solve? How does it benefit users?]

## Installation

[Include step-by-step instructions on how to install your project, including any dependencies]

```bash
# Linux Machine Setup
python3 -m venv venv
source venv/bin/activate
python3 -m pip install -r requirements.txt


# run healthcare main service script using make command
make main

# run appointment micro service
make healthcare

# run auth micro service
make auth

# run payment micro service
make payment

# run prescription micro service
make prescription

``` 