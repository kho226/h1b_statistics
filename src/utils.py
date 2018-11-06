"""
Author: Kyle Ong
Date: 11/05/2018

utils class
"""
import os


class Utils(object):

    def __init__(self):
        pass

    def getInputFiles(self, inputDir):
        inputFiles = []
        # error checking for correct inputDir
        # what happens if we call this function in the wrong location?
        for file in os.listdir(inputDir):
            inputFile = inputDir + "/" + file
            if os.path.exists(inputFile) and inputFile.split(".")[-1] == "csv":
                inputFiles.append(inputFile)
        return inputFiles
