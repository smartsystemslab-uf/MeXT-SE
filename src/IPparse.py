from tkinter import *
from tkinter.ttk import *
import xml.dom.minidom


def getText(nodelist):
    rc = []
    for node in nodelist:
        if node.nodeType == node.TEXT_NODE:
            rc.append(node.data)
    return ''.join(rc)


def parseFile(filePath):

    # The parse() function to load and parse an XML file
    doc = xml.dom.minidom.parse(filePath)

    # get Vendor and board information
    systemDes = (doc.firstChild.tagName)
    systemName = doc.getElementsByTagName(systemDes)[0].getAttribute("name")
    
    splitName = systemName.split()

    systemList = [[splitName[0]], [splitName[1]]]

    #get CPU  info
    ####################################################
    ###             CPU core information             ###
    ####################################################
    cpuData = doc.getElementsByTagName("CPU")
    cpuIndex = 0
    treeIndex = 1

    if cpuData:
        for item in cpuData:
            cpuTag = "CPU_"+ str(cpuIndex)
            systemList.append([cpuTag])
            cpuIndex = cpuIndex + 1
            treeIndex = treeIndex + 1

            #(i.e. zynq/mb0)
            itemBuffer = (item.getAttribute("name"))
            systemList[treeIndex].append(itemBuffer)

            #(i.e. standalone)
            itemBuffer = (item.getAttribute("task"))
            systemList[treeIndex].append(itemBuffer)


            #placeholder for future cpu configuration
            itemBuffer = (item.getAttribute("uconfig"))
            if itemBuffer:
                systemList[treeIndex].append(itemBuffer)
            

    #get CPU config
    cpuConfig = doc.getElementsByTagName("CPUConfig")
    cpuConfList = []

    if cpuConfig:
        for item in cpuConfig:
            cpuConfList.append(getText(item.childNodes))
        

    #get memory  info
    ####################################################
    ###           Memory core information            ###
    ####################################################
    memData = doc.getElementsByTagName("Memory")
    memIndex = 0

    if memData:
        for item in memData:
            memTag = "memory_"+ str(memIndex)
            systemList.append([memTag])
            memIndex = memIndex + 1
            treeIndex = treeIndex + 1

            #(i.e. bram)
            itemBuffer = (item.getAttribute("name"))
            systemList[treeIndex].append(itemBuffer)

            #(i.e. standalone/controller)
            itemBuffer = (item.getAttribute("mode"))
            systemList[treeIndex].append(itemBuffer)


            #placeholder for future memory configuration
            itemBuffer = (item.getAttribute("mconfig"))
            if itemBuffer:
                systemList[treeIndex].append(itemBuffer)
            

    #get MEM config
    memConfig = doc.getElementsByTagName("MemoryConfig")
    memConfList = []

    if memConfig:
        for item in memConfig:
            memConfList.append(getText(item.childNodes))


    #get IP core info
    ####################################################
    ### Placeholder for new IP core information      ###
    ####################################################
    ipData = doc.getElementsByTagName("IP")
    ipIndex = 0

    if ipData:
        for item in memData:
            ipTag = "ipcore_"+ str(ipIndex)
            systemList.append([ipTag])
            ipIndex = ipIndex + 1
            treeIndex = treeIndex + 1

            #(i.e. bram)
            itemBuffer = (item.getAttribute("name"))
            systemList[treeIndex].append(itemBuffer)

            #(i.e. standalone/controller)
            itemBuffer = (item.getAttribute("mode"))
            systemList[treeIndex].append(itemBuffer)


            #placeholder for future IP configuration
            itemBuffer = (item.getAttribute("ipconfig"))
            if itemBuffer:
                systemList[treeIndex].append(itemBuffer)


    ####################################################
    ####################################################

    ####################################################
    ###            get Communication config          ###
    ####################################################
    comConfig = doc.getElementsByTagName("CommMedium")
    comConfData = getText(comConfig[0].childNodes)



    return systemList, cpuConfList, memConfList, comConfData


