"""
Author: Kyle Ong
Date: 11/05/2018

Data Processor class
Handles parsing the data
Handles writing the data to .txt files
"""
from parser import Parser
from utils import Utils
from collections import OrderedDict


class DataProcessor(object):

    def __init__(self, directory):
        self.utils = Utils()
        self.filenames = self.utils.getInputFiles(directory)
        self.data = {}
        self.data["total_applications"] = 0
        tupleOfDicts = self.parseFiles(self.filenames)
        self.data["occupation_data"] = tupleOfDicts[0]
        self.data["state_data"] = tupleOfDicts[1]

    def parseFiles(self, inputFiles):
        SOCDict = {}
        stateDict = {}
        for file in inputFiles:
            with open(file, "r") as fh:
                parser = None
                i = 0
                for line in fh:
                    line = line.split(";")
                    if i == 0:
                        parser = Parser(line)
                        i += 1
                        continue

                    name = parser.name(line)
                    state1 = parser.state1(line)
                    state2 = parser.state2(line)
                    worksite = parser.worksite(line)
                    isCertified = parser.isCertified(line)
                    if name is not None:
                        self.computeStats(name, isCertified, SOCDict)
                    if state1 is not None:
                        self.computeStats(state1, isCertified, stateDict)
                    if state2 is not None:
                        self.computeStats(state2, isCertified, stateDict)
                    if worksite is not None:
                        self.computeStats(worksite, isCertified, stateDict)
                    totalApplications = self.data.get("total_applications", 0)
                    totalApplications += 1
                    self.data["total_applications"] = totalApplications
        self.computePercentages(stateDict)
        self.computePercentages(SOCDict)
        return SOCDict, stateDict

    def computeStats(self, key, isCertified, statsDict):
        stats = statsDict.get(key, {})
        numCertifiedApplications = stats.get(
            "num_certified_applications", 0)
        if isCertified:
            numCertifiedApplications += 1
        stats["num_certified_applications"] = numCertifiedApplications
        statsDict[key] = stats

    def computePercentages(self, statsDict):
        totalApplications = self.data["total_applications"]
        for k, v in statsDict.items():
            numCertifiedApplications = v["num_certified_applications"]
            percentage = round(100 * (numCertifiedApplications
                                      / totalApplications), 1)
            v["percentage"] = percentage

    def sortTopTen(self, data):
        topTen = OrderedDict(sorted(data.items(
        ), key=lambda v: v[1]["num_certified_applications"], reverse=True)[0:10])
        maxCertifiedApplications = 0
        if topTen:
            maxCertifiedApplications = max(
                v["num_certified_applications"] for k, v in topTen.items())
        topTenSorted = []
        while maxCertifiedApplications >= 0:
            unsorted = {k: v for k, v in topTen.items() if
                        v["num_certified_applications"] ==
                        maxCertifiedApplications}
            for ele in (sorted(unsorted.items(), key=lambda v: v[0])):
                name = ele[0]
                stats = ele[1]
                topTenSorted.append({name: stats})
            maxCertifiedApplications -= 1
        return topTenSorted

    def sortTopTenOccupations(self):
        topTen = self.sortTopTen(self.data["occupation_data"])
        return topTen

    def sortTopTenStates(self):
        return self.sortTopTen(self.data["state_data"])

    def writeArrOfDictsToFile(self, arrOfDicts, outputDir, columns):
        with open(outputDir, 'w') as fh:
            i = 0
            for d in arrOfDicts:
                lineToWrite = ""
                if i == 0:
                    fh.write(columns)
                    i = - 1
                for k, stats in d.items():
                    lineToWrite += k
                    lineToWrite += ";"
                    for k in stats:
                        if k == "percentage":
                            lineToWrite += "{}%".format(stats[k])
                            lineToWrite += ";"
                        elif k == "num_certified_applications":
                            lineToWrite += "{}".format(stats[k])
                            lineToWrite += ";"
                lineToWrite = lineToWrite.strip(";")
                lineToWrite += "\n"
                fh.write(lineToWrite)

    def writeToTxtFile(self, arrOfDicts, colNames, outputDir):
        self.writeArrOfDictsToFile(arrOfDicts, outputDir, colNames)
