#! /bin/bash


TODAY = $ date +'%Y-%m-%d'
PASSED = false


echo Project Name:
read PROJECT
echo Clent:
read CLIENT
echo Number of cameras:
read CAMS 
echo Number of audio recorders:
read AUDIO 

PROJECTFOLDER ="mmmmm"



"cd /Desktop"

mkdir "$PROJECTFOLDER"

cd ${PROJECTFOLDER}
mkdir '00 - PRODUCTION + DOCUMENTS'
mkdir '01 - PROJECT FILES'



PROJECTFOLDER = "${TODAY}_${CLIENT}_${PROJECT}"