#!/usr/bin/env bash

MEASUREMENT_NAME="MEM"
HOSTNAME="$(cat /proc/sys/kernel/hostname)"

MEM_USAGE=`free -m | grep Mem`
MEM_TOTAL=`echo "$MEM_USAGE" | awk '{print $2}'`
MEM_USED=`echo "$MEM_USAGE" | awk '{print $3}'`
MEM_FREE=`echo "$MEM_USAGE" | awk '{print $4}'`
MEM_BUFFER=`echo "$MEM_USAGE" | awk '{print $6}'`
MEM_CACHE=`echo "$MEM_USAGE" | awk '{print $7}'`
MEM_USED_PRCT=`echo $((($MEM_USED*100)/$MEM_TOTAL)) | cut -d. -f1`

TAGS="hostname=$HOSTNAME"
METRICS="sh_total=$MEM_TOTAL,sh_used=$MEM_USED,sh_free=$MEM_FREE,sh_buffer=$MEM_BUFFER,sh_cache=$MEM_CACHE,sh_user_prct=$MEM_USED_PRCT"
TIMESTAMP="$(date +%s%N)"
OUTPUT="$MEASUREMENT_NAME,$TAGS $METRICS $TIMESTAMP"

echo "$OUTPUT"
