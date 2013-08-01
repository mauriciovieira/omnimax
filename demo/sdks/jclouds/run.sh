#!/bin/bash
FILE=`mktemp test.groovy.XXXXXX`
trap "rm $FILE" EXIT
cat > "$FILE"

# groovy $FILE
GROOVY_FILE=$FILE mvn -q exec:exec -Dexec.executable="groovy" 2>&1
