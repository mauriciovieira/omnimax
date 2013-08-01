#!/bin/bash
FILE=`mktemp test.XXXXXX`
mv "$FILE" "${FILE}.cs"
FILE="${FILE}.cs"
trap "rm $FILE" EXIT
cat > "$FILE"

LIBS=("pkgs/Newtonsoft.Json.4.5.11/lib/net40/Newtonsoft.Json.dll" \
      "pkgs/openstack.net.1.1.2.1/lib/net40/openstacknet.dll" \
      "pkgs/SimpleRESTServices.1.0.6.6/lib/net40/SimpleRESTServices.dll" \
)

EXECUTABLE=`echo $FILE | sed 's/.cs$/.exe/'`
LIBS_COMMAS=$( IFS=, ; echo "${LIBS[*]}" )
LIBS_SPACES=$( IFS=" "; echo "${LIBS[*]}" )
echo $LIBS_COMMAS
echo $LIBS_SPACES
dmcs -r:$LIBS_COMMAS $FILE
cp $LIBS_SPACES `dirname $EXECUTABLE`
trap "rm $EXECUTABLE" EXIT
mono $EXECUTABLE

