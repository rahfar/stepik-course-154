#!/bin/bash
virtualenv -p python3 pyenv
source pyenv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt