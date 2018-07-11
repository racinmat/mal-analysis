#!/bin/bash

# now using nohup
# ampersand na konci je na puštění ve forknutým procesu, &> je všechen output (stdout + stderr) přesměrovaný do souboru log.log a nohup říká, ať proces neumře, pokud skončí session, ve které to bylo spuštěný
nohup jupyter notebook "$@" &> log-jupyter.log &
