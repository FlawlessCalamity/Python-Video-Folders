#!/usr/bin/python3

import sys
import os
from datetime import date

today = str(date.today())
project = input("Project Name:")
client = input("Client:")
cams = 100
audio = 100
passed = False


def project_setup_cameras(passedInFunc, camsInFunc):
    if passedInFunc == False:
        try:
            camsInFunc = int(input("Number of Cameras:"))
            if camsInFunc > 5:
                print("Maximum amount of cameras is 5, please enter 5 or below:")
                project_setup_cameras(passedInFunc, camsInFunc)
            else:
                passedInFunc = True
                return camsInFunc
        except:
            camsInFunc = print("Please enter a number not a word")
            project_setup_cameras(passedInFunc, camsInFunc)
    else:
        return camsInFunc


def project_setup_audio(passedInFunc, audioInFunc):
    if passedInFunc == False:
        try:
            audioInFunc = int(input("Number of Audio recording devices:"))
            if audioInFunc > 5:
                print("Maximum amount of audio recorders is 5, please enter 5 or below:")
                project_setup_audio(passedInFunc, audioInFunc)
            else:
                passedInFunc = True
                return audioInFunc
        except:
            audioInFunc = print("Please enter a number not a word")
            project_setup_audio(passedInFunc, audioInFunc)
    else:
        return audioInFunc


cams = project_setup_cameras(passed, cams)
audio = project_setup_audio(passed, audio)


camdict = {0: "A", 1: "B", 2: "C", 3: "D", 4: "E"}
dir_path = os.path.dirname(os.path.realpath(__file__))
os.chdir(dir_path)
os.mkdir(today + "_" + client + "_" + project)
os.chdir(today + "_" + client + "_" + project)
################################################### PROJECT FILES ###################################################
os.mkdir("00 - PRODUCTION + DOCUMENTS")
os.mkdir("01 - PROJECT FILES")
os.chdir("01 - PROJECT FILES")
os.mkdir("01 - PREMIER PRO")
os.mkdir("02 - AFTER EFFECTS")
os.mkdir("03 - DAVINCI RESOLVE")
os.mkdir("04 - AUDITION")
os.mkdir("05 - PROTOOLS")
os.chdir("..")
################################################### PROJECT FILES ###################################################

################################################### FOOTAGE ###################################################
os.mkdir("02 - FOOTAGE")
os.chdir("02 - FOOTAGE")

for i in range(cams):
    os.mkdir("0"+str(i)+" - CAM " + camdict.get(i)+" - CAMERA MODEL")
    os.chdir("0"+str(i)+" - CAM " + camdict.get(i)+" - CAMERA MODEL")
    os.mkdir(camdict.get(i)+"001")
    os.mkdir(camdict.get(i)+"002")
    os.mkdir(camdict.get(i)+"003")
    os.mkdir(camdict.get(i)+"004")
    os.mkdir(camdict.get(i)+"005")
    os.chdir("..")
os.chdir("..")
################################################### FOOTAGE ###################################################


################################################### AUDIO ###################################################
os.mkdir("03 - AUDIO")
os.chdir("03 - AUDIO")
os.mkdir("01 - RECORDED")
os.chdir("01 - RECORDED")
for i in range(audio):
    os.mkdir("0"+str(i)+" - AUDIO " + camdict.get(i)+" - RECORDER MODEL")
    os.chdir("0"+str(i)+" - AUDIO " + camdict.get(i)+" - RECORDER MODEL")
    os.mkdir(camdict.get(i)+"001")
    os.mkdir(camdict.get(i)+"002")
    os.mkdir(camdict.get(i)+"003")
    os.mkdir(camdict.get(i)+"004")
    os.mkdir(camdict.get(i)+"005")
    os.chdir("..")
os.chdir("..")

os.mkdir("02 - MUSIC")
os.mkdir("03 - SFX")
os.mkdir("04 - VOICE OVERS")
os.mkdir("05 - SOUND MIXES")
os.chdir("..")
################################################### AUDIO ###################################################


################################################### GRAPHICS ###################################################

os.mkdir("04 - GRAPHICS")
os.chdir("04 - GRAPHICS")
os.mkdir("01 - PHOTOSHOP")
os.mkdir("02 - ILLUSTRATOR")
os.mkdir("03 - TITLES")
os.mkdir("04 - IMAGES")
os.mkdir("05 - FONTS")
os.mkdir("06 - GFX")
os.chdir("06 - GFX")
os.mkdir("01 - LUTS")
os.mkdir("02 - EFFECTS")
os.mkdir("03 - TRANSITIONS")
os.mkdir("04 - MISC")
os.chdir("../..")
################################################### GRAPHICS ###################################################


################################################### EXPORTS ###################################################
os.mkdir("05 - EXPORTS")
os.chdir("05 - EXPORTS")
os.mkdir("01 - CUTS")
os.mkdir("02 - RUSHES - DAILIES")
os.mkdir("03 - SCREEN GRABS")
################################################### EXPORTS ###################################################
