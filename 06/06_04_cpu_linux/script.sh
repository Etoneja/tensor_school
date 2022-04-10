#!/usr/bin/env bash

MEASUREMENT_NAME="CPU"
HOSTNAME="$(cat /proc/sys/kernel/hostname)"

CPU_USAGE="$(vmstat 1 2 | tail -1)"
CPU_USER="$(echo ${CPU_USAGE} | awk '{print $13}')"
CPU_SYSTEM="$(echo ${CPU_USAGE} | awk '{print $14}')"
CPU_IDLE="$(echo ${CPU_USAGE} | awk '{print $15}')"
CPU_IOWAIT="$(echo ${CPU_USAGE} | awk '{print $16}')"
CPU_ST="$(echo ${CPU_USAGE} | awk '{print $17}')"
CPU_TOTAL="$(echo $((100-$CPU_IDLE)))"

TAGS="hostname=$HOSTNAME"
METRICS="sh_user=$CPU_USER,sh_system=$CPU_SYSTEM,sh_idle=$CPU_IDLE,sh_iowait=$CPU_IOWAIT,sh_st=$CPU_ST,sh_total=$CPU_TOTAL"
TIMESTAMP="$(date +%s%N)"
OUTPUT="$MEASUREMENT_NAME,$TAGS $METRICS $TIMESTAMP"

echo "$OUTPUT"
