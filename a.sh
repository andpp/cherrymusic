#!/bin/bash

export CHERRYMUSIC_DATA_HOME=/public/cm
export CHERRYMUSIC_CONFIG_HOME=/public/cm

#printenv | sort | grep CHERRY

./cherrymusicd $1
