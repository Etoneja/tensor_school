#!/bin/bash
# WANT_JSON

addr=$(cat $1 | jq -r '.addr')
tls=$(cat $1 | jq -r '.tls // true')

if [ "$tls" = "true" ] ; then
    proto="https"
else
    proto="http"
fi

url="${proto}://${addr}"

status_code=$(curl -L -X GET \
    --write-out '%{http_code}' \
    --silent --output /dev/null $addr)
rc=$?

changed=false

if [ $rc -ne 0 ] ; then
    failed=true
    msg="Task failed"
else
    failed=false
    msg="Task executed successfully!"
fi

res="{\
\"rc\": $rc,\
\"failed\": $failed,\
\"result_str\": \"$status_code\",\
\"msg\": \"$msg\"\
}"

echo $res
