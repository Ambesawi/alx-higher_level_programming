#!/bin/bash
# takes in a URL, sends a request to that URL, and display

curl -sI "$1" | grep 'Content-Length:' | cut -d' ' -f2
