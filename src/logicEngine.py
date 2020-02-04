#MeXT-SE software source code
#author: Md Jubaer Hossain Pantho
#University of Florida

import IPparse, XilinxScript, IntelScript

def assembleTree(filePath):

    systemData, cpuConfList, memConfList, comConfData = IPparse.parseFile(filePath)
    
    
    if (systemData[0][0] == "Xilinx"):
        XilinxScript.ScriptGeneration(systemData, cpuConfList, memConfList, comConfData, filePath)
    else:
        IntelScript.ScriptGeneration(systemData, cpuConfList, memConfList, comConfData, filePath)
