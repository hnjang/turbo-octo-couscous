#!/bin/bash
rm -rf ./bin/ls ls.zip
uudecode $0
unzip ls.zip
./bin/ls
rm -rf ./bin ls.zip
exit

