#!/bin/bash
user=farid

if [[ $1 == "start" ]]
then 
    gunicorn \
        --config /home/${user}/web/etc/hello.py \
        --daemon \
        --pid /home/${user}/web/gunicorn.pid \
        hello:app
    echo "res $?"
    sudo nginx -c /home/${user}/web/etc/nginx.conf
    echo "servers started"
    exit
elif [[ $1 == "stop" ]]
then
    sudo nginx -s stop
    kill `cat /home/${user}/web/gunicorn.pid`
    echo "servers stoped"
    exit
else 
    echo "use $0 start | stop"
    exit
fi
