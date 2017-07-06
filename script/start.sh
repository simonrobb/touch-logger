#!/bin/sh

printf "Spawning logger process\n"
nohup python src/main.py >Logger.out &