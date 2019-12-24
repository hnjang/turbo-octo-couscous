#!/bin/bash
cp ./template.sh ./self_decode.sh
uuencode /bin/ls ls >> self_decode.sh
