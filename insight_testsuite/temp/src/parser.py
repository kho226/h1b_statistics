"""
Author: Kyle Ong
Date: 11/05/2018

Parser class, line by line
"""
import re


class Parser(object):
    def __init__(self, line):
        self.locations = self.getLocations(line)
        self.numColumns = len(line)

    def getLocations(self, line):
        locations = {}
        for idx, ele in enumerate(line):
            if "status" in ele.lower() == "status":
                locations["status"] = idx
            elif "lca_case_workloc1_state" in ele.lower():
                locations["lca_case_workloc1_state"] = idx
            elif "lca_case_workloc2_state" in ele.lower():
                locations["lca_case_workloc2_state"] = idx
            elif "worksite_state" in ele.lower():
                locations["worksite_state"] = idx
            elif "soc_name" in ele.lower():
                locations["soc_name"] = idx
            elif "status" in ele.lower():
                locations["status"] = idx
            elif "soc_code" in ele.lower():
                locations["soc_code"] = idx
        return locations

    def isValid(self, parsed):
        isValid = True
        if len(parsed) != self.numColumns:
            isValid = False
        return isValid

    def status(self, parsed):
        status = None
        if self.isValid(parsed):
            if parsed[self.locations["status"]]:
                status = parsed[self.locations["status"]]
        return status

    def state1(self, parsed):
        state = None
        loc = self.locations.get("lca_case_workloc1_state", None)
        if loc != None and parsed[loc]:
            state = parsed[self.locations["lca_case_workloc1_state"]].strip(
                '\"')
        return state

    def state2(self, parsed):
        state = None
        loc = self.locations.get("lca_case_workloc2_state", None)
        if loc != None and parsed[loc]:
            state = parsed[self.locations["lca_case_workloc2_state"]].strip(
                '\"')
        return state

    def worksite(self, parsed):
        worksite = None
        loc = self.locations.get("worksite_state", None)
        if loc != None and parsed[loc]:
            worksite = parsed[self.locations["worksite_state"]].strip('\"')
        return worksite

    def isCertified(self, parsed):
        isCertified = False
        if self.isValid(parsed):
            if parsed[self.locations["status"]] and\
                    parsed[self.locations["status"]].lower() == "certified":
                isCertified = True
        return isCertified

    def name(self, parsed):
        name = None
        if self.isValid(parsed):
            if parsed[self.locations["soc_name"]]:
                name = parsed[self.locations["soc_name"]].strip('\"')
        return name

    def code(self, parsed):
        code = None
        if self.isValid(parsed):
            if parsed[self.locations["soc_code"]]:
                code = parsed[self.locations["soc_code"]]
        return code
