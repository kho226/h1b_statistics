"""
Author: Kyle Ong
Date: 11/05/2018

main.py
"""
from parser import Parser
from utils import Utils
import os
import sys
from dataProcessor import DataProcessor


def main():
    args = sys.argv[1:]
    utils = Utils()
    inputDir = os.getcwd() + args[0][1:]
    top10OccupationsOutputDir = os.getcwd() + args[1][1:]
    top10StatesOutputDir = os.getcwd() + args[2][1:]

    dataProcessor = DataProcessor(inputDir)

    topTenOccupations = dataProcessor.sortTopTenOccupations()
    colNames = "TOP_OCCUPATIONS;NUMBER_CERTIFIED_APPLICATIONS;PERCENTAGE\n"
    dataProcessor.writeToTxtFile(topTenOccupations,
                                 colNames, top10OccupationsOutputDir)

    topTenStates = dataProcessor.sortTopTenStates()
    colNames = "TOP_STATES;NUMBER_CERTIFIED_APPLICATIONS;PERCENTAGE\n"
    dataProcessor.writeToTxtFile(topTenStates,
                                 colNames, top10StatesOutputDir)


if __name__ == "__main__":
    main()
