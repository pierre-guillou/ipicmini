#!/usr/bin/env bash
# launch with pueue add -- bash ./launch-runs.sh

sim_params=inputfiles/GEM3D.inp
exe=build/iPICmini

echo "B0z = 0.0" >> $sim_params
echo "ns = 4" >> $sim_params
$exe $sim_params

echo "B0z = 0.0195" >> $sim_params
echo "ns = 4" >> $sim_params
$exe $sim_params

echo "B0z = 0.0195" >> $sim_params
echo "ns = 2" >> $sim_params
$exe $sim_params

echo "B0z = 0.0" >> $sim_params
echo "ns = 2" >> $sim_params
$exe $sim_params

python3 inputfiles/clusterDiags.py
