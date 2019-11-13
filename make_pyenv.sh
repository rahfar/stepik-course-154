#!/bin/bash
sudo apt-get install python3-dev
virtualenv -p python3 pyenv
source pyenv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt