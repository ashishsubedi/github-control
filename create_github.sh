#!/bin/sh
BASEDIR=$(dirname $0)
python $BASEDIR/create_github.py "$@"
