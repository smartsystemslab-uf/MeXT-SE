#MeXT-SE software source code
#author: Md Jubaer Hossain Pantho
#University of Florida
from IntelParameter import *
import array

def ScriptGeneration(systemData, cpuConfList, memConfList, comConfData, filePath, securityBit):
    print("Generating script for Intel FPGA")
    print(systemData)
    #added for # DEBUG:
    print(cpuConfList)
    print(memConfList)
    print(comConfData)
    print(filePath)

    tclFile = open(filePath[:-3] + "tcl", "w")
    projectDir = filePath.split('/')
    projectName = projectDir[-1]
    projectName = projectName[:-4]

    tclFile.write("# qsys scripting (.tcl) file\n")
    tclFile.write("package require -exact qsys 16.0\n\n")

    create_project = "create_system " + "{" + projectName + "}" + "\n\n"
    tclFile.write(create_project)

    project = "set_project_property"
    instance = "set_instance_parameter_value"
    connection = "set_connection_parameter_value"

    m = systemData[1][0]
    string = m.split('-')
    device_family = project+" "+"DEVICE_FAMILY" + " {" + string[0] + " " + string[1] + "} " + "\n"
    tclFile.write(device_family)
    device = project+" "+"DEVICE" + " " + "{5CSEMA5F31C6}" + "\n"
    tclFile.write(device)
    ipcatalog = project + " HIDE_FROM_IP_CATALOG " + "{false}" + "\n\n"
    tclFile.write(ipcatalog)

    tclFile.write("#Instances and instance parameters\n")
    count = 0
    numComponent = 0
    comp_array = []
    for item in systemData:
        count = count + 1
        if(count > 2):
            if ("CPU" in item[0]):
                if("standalone" in item and "nios2" in item):
                    cpu_add = "add_instance " + "CPU " + "altera_" + item[1] + "_gen2 " + "18.1\n"
                    tclFile.write(cpu_add)
                    numComponent = numComponent + 1
                    comp_array.append("CPU")
                    for i in range(len(CPU_parameter)):
                        cpu_add_parameter = instance + " CPU " + "{" + CPU_parameter[i][0] +"} " + "{" + CPU_parameter[i][1] + "}\n"
                        tclFile.write(cpu_add_parameter)
                    tclFile.write("\n")
            elif ("ipcore" in item[0]):
                if("GPIO" in item):
                    gpio_add = "add_instance " + "GPIO " + "altera_avalon_pio " + "18.1\n"
                    tclFile.write(gpio_add)
                    numComponent = numComponent + 1
                    comp_array.append("GPIO")

                    for i in range(len(GPIO_parameter)):
                        gpio_add_parameter = instance + " GPIO " + "{" + GPIO_parameter[i][0] +"} " + "{" + GPIO_parameter[i][1] + "}\n"
                        tclFile.write(gpio_add_parameter)
                    tclFile.write("\n")

    memory_add = "add_instance MEMORY1 altera_avalon_onchip_memory2 18.1\n"
    tclFile.write(memory_add)
    numComponent = numComponent + 1
    comp_array.append("MEMORY1")
    for i in range(len(MEMORY_parameter)):
        memory_add_parameter = instance + " MEMORY1 " + "{" + MEMORY_parameter[i][0] +"} " + "{" + MEMORY_parameter[i][1] + "}\n"
        tclFile.write(memory_add_parameter)
    tclFile.write("\n")

    clock_add = "add_instance clk_0 clock_source 18.1\n"
    tclFile.write(clock_add)
    for i in range(len(CLOCK_parameter)):
        clock_add_parameter = instance + " clk_0 " + "{" + CLOCK_parameter[i][0] +"} " + "{" + CLOCK_parameter[i][1] + "}\n"
        tclFile.write(clock_add_parameter)
    tclFile.write("\n")
    #numComponent = numComponent + 1

    if (securityBit == 1):
        himm_add = "add_instance himm_module_v1_0_S00_Avalon_0 himm_module_v1_0_S00_Avalon 1.0\n"
        tclFile.write(himm_add)
        numComponent = numComponent + 1
        comp_array.append("himm_module_v1_0_S00_Avalon_0")
        for i in range(len(HIMM_parameter)):
            himm_add_parameter = instance + " himm_module_v1_0_S00_Avalon_0 " + "{" + HIMM_parameter[i][0] +"} " + "{" + HIMM_parameter[i][1] + "}\n"
            tclFile.write(himm_add_parameter)
        tclFile.write("\n")

    jtag_add = "add_instance jtag_uart_0 altera_avalon_jtag_uart 18.1\n"
    tclFile.write(jtag_add)
    numComponent = numComponent + 1
    comp_array.append("jtag_uart_0")
    for i in range(len(JTAG_parameter)):
        jtag_add_parameter = instance + " jtag_uart_0 " + "{" + JTAG_parameter[i][0] +"} " + "{" + JTAG_parameter[i][1] + "}\n"
        tclFile.write(jtag_add_parameter)
    tclFile.write("\n")
    print(numComponent)

    # Try to automate this section if possible
    tclFile.write("# exported interfaces\n")
    tclFile.write("add_interface clk clock sink\n")
    tclFile.write("set_interface_property clk EXPORT_OF clk_0.clk_in\n")
    tclFile.write("add_interface gpio conduit end\n")
    tclFile.write("set_interface_property gpio EXPORT_OF GPIO.external_connection\n")
    tclFile.write("add_interface reset reset sink\n")
    tclFile.write("set_interface_property reset EXPORT_OF clk_0.clk_in_reset\n\n")
    if (securityBit == 1):
        tclFile.write("add_interface secure_data_out conduit end\n")
        tclFile.write("set_interface_property secure_data_out EXPORT_OF himm_module_v1_0_S00_Avalon_0.conduit_end\n\n")

    #connections and connection parameters
    tclFile.write("# connections and connection parameters\n")
    if (securityBit == 1):
        x = len(DATA_baseAddress)
    else:
        x = len(DATA_baseAddress) - 1
    for i in range(x):
        add_connect = "add_connection CPU.data_master " + DATA_baseAddress[i][0] +"\n"
        tclFile.write(add_connect)
        for j in range(0,3):
            if (j==0):
                param = "arbitrationPriority {1}\n"
            elif (j==1):
                param = "baseAddress {" + DATA_baseAddress[i][1] + "}\n"
            elif (j==2):
                param = "defaultConnection {0}\n"
            set_connect = connection + " CPU.data_master/" + DATA_baseAddress[i][0]+" "+param
            tclFile.write(set_connect)
        tclFile.write("\n")

    for i in range(len(INSTRUCTION_baseAddress)):
        add_connect = "add_connection CPU.instruction_master " + INSTRUCTION_baseAddress[i][0] +"\n"
        tclFile.write(add_connect)
        for j in range(0,3):
            if (j==0):
                param = "arbitrationPriority {1}\n"
            elif (j==1):
                param = "baseAddress {" + INSTRUCTION_baseAddress[i][1] + "}\n"
            elif (j==2):
                param = "defaultConnection {0}\n"
            set_connect = connection + " CPU.instruction_master/" + INSTRUCTION_baseAddress[i][0]+" "+param
            tclFile.write(set_connect)
        tclFile.write("\n")

    tclFile.write("add_connection CPU.irq jtag_uart_0.irq\n")
    tclFile.write("set_connection_parameter_value CPU.irq/jtag_uart_0.irq irqNumber {0}\n\n")

    for i in range(numComponent):
        if(comp_array[i] == "MEMORY1"):
            add_connect = "add_connection clk_0.clk " + comp_array[i] + ".clk1\n"
        elif (comp_array[i] == "himm_module_v1_0_S00_Avalon_0"):
            add_connect = "add_connection clk_0.clk " + comp_array[i] + ".clock_sink\n"
        else:
            add_connect = "add_connection clk_0.clk " + comp_array[i] + ".clk\n"
        tclFile.write(add_connect)
    tclFile.write("\n")
    for i in range(numComponent):
        if(comp_array[i] == "MEMORY1"):
            add_connect = "add_connection clk_0.clk_reset " + comp_array[i] + ".reset1\n"
        elif (comp_array[i] == "himm_module_v1_0_S00_Avalon_0"):
            add_connect = "add_connection clk_0.clk_reset " + comp_array[i] + ".reset_sink\n"
        else:
            add_connect = "add_connection clk_0.clk_reset " + comp_array[i] + ".reset\n"
        tclFile.write(add_connect)
    #print(comp_array)
    tclFile.write("# interconnect requirements\n")
    tclFile.write("set_interconnect_requirement {$system} {qsys_mm.clockCrossingAdapter} {HANDSHAKE}\n")
    tclFile.write("set_interconnect_requirement {$system} {qsys_mm.enableEccProtection} {FALSE}\n")
    tclFile.write("set_interconnect_requirement {$system} {qsys_mm.insertDefaultSlave} {FALSE}\n")
    tclFile.write("set_interconnect_requirement {$system} {qsys_mm.maxAdditionalLatency} {1}\n\n")


    tclFile.write("# To make sure that there is no collision between addresses\n")
    tclFile.write("auto_assign_system_base_addresses\n")

    tclFile.write("#validates the system\n")
    tclFile.write("validate_system\n\n")

    final_system = "save_system " + "{" + projectName + ".qsys}\n"
    tclFile.write(final_system)

    print("Done")
