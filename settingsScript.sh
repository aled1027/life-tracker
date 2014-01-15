#!/bin/bash

# provide either local or heroku as the one and only argument
ARG=$1
cd LifeTracker
rm settings.py
cp settings-${ARG}.py settings.py
cd ..



