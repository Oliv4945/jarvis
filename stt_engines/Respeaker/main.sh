#!/bin/bash

_Respeaker_hotword () {
    $verbose && jv_debug "DEBUG Respeaker: Starting STT"
    http_code=$(curl --write-out %{http_code} --silent -o $forder -G "localhost:8082" --data-urlencode "hotword=jarvis")
    $verbose && jv_debug "DEBUG Respeaker: reponse: $(cat $forder)"
    $verbose && jv_debug "DEBUG Respeaker: http_code: $http_code"
    if [ $http_code -eq 200 ]; then
        return 0
    fi
    return 1
}

_Respeaker_order () {
    $verbose && jv_debug "DEBUG Respeaker: Starting STT"
    http_code=$(curl --write-out %{http_code} --silent -o $forder -G "localhost:8082" --data-urlencode "action=rec")
    $verbose && jv_debug "DEBUG Respeaker: reponse: $(cat $forder)"
    $verbose && jv_debug "DEBUG Respeaker: http_code: $http_code"
    if [ $http_code -eq 200 ]; then
        return 0
    fi
    return 1
} 

Respeaker_STT () { 
    if $bypass; then
        _Respeaker_order & 
    else
        _Respeaker_hotword &
    fi
    jv_spinner $!
}
