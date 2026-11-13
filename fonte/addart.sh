#!/bin/sh
# addart.sh key suffix
cp /tmp/claude-tool-results/*/*$2* art_final/$1.png && ls -la art_final/$1.png
