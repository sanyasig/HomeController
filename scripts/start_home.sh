#!/bin/bash
pkill -f homec_3_7

#update git repo
cd /home/nanihome/drive/work/HomeController
/usr/bin/git stash
/usr/bin/git pull

# start fauxmo
nohup /home/nanihome/anaconda3/envs/homec_3_7/bin/fauxmo  -c fauxmo/fauxmo_config.json -vv > fauxmo.log 2>&1&

#home controller
nohup /home/nanihome/anaconda3/envs/homec_3_7/bin/python3 start.py > home_controler.log 2>&1&

