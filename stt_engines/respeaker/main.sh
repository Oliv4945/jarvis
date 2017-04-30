#!/bin/bash
respeaker_STT () { # STT () {} Listen & transcribes audio file then writes corresponding text in $forder
    DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
    $verbose && jv_debug "DEBUG: Starting Respeaker STT"
    $verbose && jv_debug "DEBUG: DIR=$DIR"
    $verbose && jv_debug "DEBUG: forder=$forder"
    python  $DIR/stt_respeaker.py > $forder &
    jv_spinner $!
}
