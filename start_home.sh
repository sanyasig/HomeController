#!/bin/bash

ps aux | grep alexa-home.py | awk '{ahlogger.log $2}' | xargs kill

cd /home/nanipi/work/AlexaHome
/usr/bin/git pull

nohup python alexa-home.py>alexa-home.log 2>&1&
#nohup python alexa-home.py &
