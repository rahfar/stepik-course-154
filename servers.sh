#!/bin/bash

# if [[ $1 == "start" ]]
# then 
#     gunicorn \
#         --bind="0.0.0.0:8000" \
#         --daemon \
#         --pid /home/farid/web/gunicorn.pid \
#         hello:app
#     echo "res $?"
#     sudo nginx -c /home/farid/web/etc/nginx.conf
#     echo "servers started"
#     exit
# elif [[ $1 == "stop" ]]
# then
#     sudo nginx -s stop
#     kill `cat /home/farid/web/gunicorn.pid`
#     echo "servers stoped"
#     exit
# else 
#     echo "use $0 start | stop"
#     exit
# fi
