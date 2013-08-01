#!/bin/bash
FILE=`mktemp test.XXXXXX`
mv "$FILE" "${FILE}.go"
FILE="${FILE}.go"
trap "rm $FILE" EXIT
cat > "$FILE"

go run $FILE
