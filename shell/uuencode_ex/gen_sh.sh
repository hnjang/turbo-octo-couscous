#!/bin/bash
cp ./template.sh ./decode1.sh
uuencode -m /bin/ls ls >> decode1.sh
cp ./template2.sh ./decode2.sh
zip - /bin/ls | uuencode -m ls.zip >> decode2.sh
