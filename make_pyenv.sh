#!/bin/bash -x
sudo apt-get install libmysqlclient-dev
sudo apt-get install python-dev default-libmysqlclient-dev
virtualenv -p python3 pyenv
source pyenv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt