#!/bin/bash
# cURL body size
curl -Si "$1" | grep "Content-Length" | cut -d ':' -f 2
