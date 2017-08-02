#!/bin/bash

PACKAGE_NAME=Regextools
PYTHON_FILE=regextools.py

# Don't modify from here -----

TOOLS_BIN_DIR=/usr/lib/libreoffice/sdk/bin/
IDL_INCLUDE_DIR=/usr/lib/libreoffice/sdk/idl
IDL_FILE_NAME=X$PACKAGE_NAME
IDL_FILE=$IDL_FILE_NAME.idl
RDB_FILE=$IDL_FILE_NAME.rdb
URD_FILE=$IDL_FILE_NAME.urd


$TOOLS_BIN_DIR/idlc -w -I $IDL_INCLUDE_DIR ./src/$IDL_FILE

if [ -f ./src/$RDB_FILE ];
then
    rm ./src/$RDB_FILE
fi
/usr/lib/libreoffice/program/regmerge ./src/$RDB_FILE /UCR ./src/$URD_FILE
if [ -f ./src/$URD_FILE ];
then
    rm ./src/$URD_FILE
fi

python src/generate_xml.py
echo 1
#
# Create .OXT file.
#
if [ -d $PACKAGE_NAME ];
then
    rm -rf $PACKAGE_NAME
fi
mkdir $PACKAGE_NAME
mkdir $PACKAGE_NAME/META-INF
mkdir $PACKAGE_NAME/description
mkdir $PACKAGE_NAME/icons
mkdir $PACKAGE_NAME/resources
mv manifest.xml $PACKAGE_NAME/META-INF/
mv description.xml $PACKAGE_NAME/
mv CalcAddIn.xcu $PACKAGE_NAME/
mv src/$RDB_FILE $PACKAGE_NAME/
cp src/$PYTHON_FILE $PACKAGE_NAME/
cp src/description/* $PACKAGE_NAME/description/
cp src/icons/* $PACKAGE_NAME/icons/
cp src/resources/* $PACKAGE_NAME/resources/

if [ -f $PACKAGE_NAME.oxt ];
then
    rm $PACKAGE_NAME.oxt
fi
cd $PACKAGE_NAME
zip -r ../$PACKAGE_NAME.oxt *
cd ..
if [ -d $PACKAGE_NAME ];
then
    rm -rf $PACKAGE_NAME
fi
