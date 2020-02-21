#MeXT-SE software source code
#author: Md Jubaer Hossain Pantho
#University of Florida

import IPparse, XilinxScript, IntelScript, XilinxSecureScript

def assembleTree(filePath, securityBit =0):

    systemData, cpuConfList, memConfList, comConfData = IPparse.parseFile(filePath)
    
    
    if (systemData[0][0] == "Xilinx"):
        if (securityBit == 0):
            XilinxScript.ScriptGeneration(systemData, cpuConfList, memConfList, comConfData, filePath)
        else:
            XilinxSecureScript.ScriptGeneration(systemData, cpuConfList, memConfList, comConfData, filePath)
    else:
        IntelScript.ScriptGeneration(systemData, cpuConfList, memConfList, comConfData, filePath)
