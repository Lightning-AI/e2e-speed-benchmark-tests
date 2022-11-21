#!/usr/bin/env bash

dirname=${PWD##*/}

app_name="$dirname-$RANDOM"

timeout=40
start_time=$SECONDS
end_time=$(($start_time + $timeout))


lightning run app app.py --cloud --name $app_name --open-ui false
while [[ $SECONDS -lt $end_time ]]
do
    time_now=$SECONDS
    if lightning show logs $app_name | grep "BENCHMARK DONE"; then
        echo "PASS: The app $(pwd)/app.py completed in $(($time_now-$start_time)) seconds (less than maximum time of $timeout)"
        exit 0
    fi
done

echo "FAIL: The app $dirname/app.py failed to complete in less than $timeout seconds"
exit 1
