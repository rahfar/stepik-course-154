#! /bin/bash
# virtualenv -p python3 myvenv
# source myvenv/bin/activate
# pip install --upgrade pip
# pip install django==2.0.0
# pip install gunicorn==19.6.0
#----------------------------------------------------
sudo nginx -c /home/${USER}/web/config/nginx.conf
gunicorn \
    --bind="0.0.0.0:8000" \
    --daemon \
    --pid /home/${USER}/web/gunicorn.pid \
    ask.wsgi

