#! /bin/bash
# virtualenv -p python3 myvenv
# source myvenv/bin/activate
# pip install --upgrade pip
# pip install -r requirements.txt
#----------------------------------------------------
sudo nginx -c "/home/${USER}/web/config/nginx.conf"
gunicorn \
    --bind="0.0.0.0:8000" \
    --daemon \
    --pid "/home/${USER}/web/gunicorn.pid" \
    ask.wsgi

