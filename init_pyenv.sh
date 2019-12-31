#!/bin/bash -x
cd /home/${USER}/web/
sudo apt-get install libmysqlclient-dev
sudo apt-get install python-dev default-libmysqlclient-dev
virtualenv -p python3 /home/${USER}/web/pyenv
source /home/${USER}/web/pyenv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt