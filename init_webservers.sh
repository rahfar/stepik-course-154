#! /bin/bash
source /home/${USER}/web/pyenv/bin/activate && 
sudo nginx -c "/home/${USER}/web/config/nginx.conf" &&
cd ask && 
gunicorn \
    --bind="0.0.0.0:8000" \
    ask.wsgi
