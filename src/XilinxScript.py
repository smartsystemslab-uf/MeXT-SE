#MeXT-SE software source code
#author: Md Jubaer Hossain Pantho
#University of Florida

def ScriptGeneration(systemData, cpuConfList, memConfList, comConfData, filePath):
    print("Generating script for Xilinx FPGA")
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

    create_project = "create_project " + projectName + " " + filePath[:-4] + " -part xc7vx485tffg1157-1\n"
    tclFile.write(create_project)


    if (systemData[1][0] == "zynq-7010"):
        tclFile.write("set_property board_part digilentinc.com:zybo-z7-10:part0:1.0 [current_project]\n")
        tclFile.write("update_ip_catalog\n\n")
    elif(systemData[1][0] == "zynq-7020"):
        tclFile.write("set_property board_part digilentinc.com:zybo-z7-20:part0:1.0 [current_project]\n")
        tclFile.write("update_ip_catalog\n\n")
    else:
        print("INFO: Unknown board file")
        exit(-1)

    gpio_index = -1
    tclFile.write("create_bd_design \"design_1\"\n")
    tclFile.write("update_compile_order -fileset sources_1\n")
    count = 0
    for item in systemData:
        count = count + 1
        if (count > 2):
            if ("CPU" in item[0]):
                if("standalone" in item and "zynq" in item):
                    tclFile.write("startgroup\n")
                    tclFile.write("create_bd_cell -type ip -vlnv xilinx.com:ip:processing_system7:5.5 processing_system7_0\n")
                    tclFile.write("endgroup\n\n")


                if (cpuConfList[0] =="DDR"):
                    tclFile.write('apply_bd_automation -rule xilinx.com:bd_rule:processing_system7 -config {make_external "FIXED_IO, DDR" apply_board_preset "1" Master "Disable" Slave "Disable" }  [get_bd_cells processing_system7_0]\n')


            elif ("memory" in item[0]):
                if ("bram" in item and "controller" in item):
                    #command to add controller
                    tclFile.write("startgroup\n")
                    tclFile.write("create_bd_cell -type ip -vlnv xilinx.com:ip:axi_bram_ctrl:4.0 axi_bram_ctrl_0\n")
                    tclFile.write("endgroup\n\n")

                    #command to add memory generator
                    tclFile.write("startgroup\n")
                    tclFile.write("create_bd_cell -type ip -vlnv xilinx.com:ip:blk_mem_gen:8.4 blk_mem_gen_0\n")
                    tclFile.write("endgroup\n\n")

                    if (memConfList[0] == "Single Port"):
                        tclFile.write("set_property -dict [list CONFIG.SINGLE_PORT_BRAM {1}] [get_bd_cells axi_bram_ctrl_0]\n")
                        tclFile.write("apply_bd_automation -rule xilinx.com:bd_rule:bram_cntlr -config {BRAM \"Auto\" }  [get_bd_intf_pins axi_bram_ctrl_0/BRAM_PORTA]\n\n")

                    if (comConfData == "axi"):
                        tclFile.write("apply_bd_automation -rule xilinx.com:bd_rule:axi4 -config { Clk_master {Auto} Clk_slave {Auto} Clk_xbar {Auto} Master {/processing_system7_0/M_AXI_GP0} Slave {/axi_bram_ctrl_0/S_AXI} intc_ip {Auto} master_apm {0}}  [get_bd_intf_pins axi_bram_ctrl_0/S_AXI]\n\n")

            elif ("ipcore" in item[0]):
                gpio_index = gpio_index + 1
                if ("GPIO" in item):
                    tclFile.write("startgroup\n")
                    tclFile.write("create_bd_cell -type ip -vlnv xilinx.com:ip:axi_gpio:2.0 axi_gpio_"+ str(gpio_index) +"\n")
                    tclFile.write("endgroup\n\n")

                    if ("input" in item):
                        widthSize = item[3]
                        widthSize = widthSize[:-4]
                        tclFile.write("set_property -dict [list CONFIG.C_GPIO_WIDTH {" + widthSize + "}] [get_bd_cells axi_gpio_"+ str(gpio_index) +"]\n\n")
                        tclFile.write("apply_bd_automation -rule xilinx.com:bd_rule:axi4 -config { Clk_master {Auto} Clk_slave {Auto} Clk_xbar {Auto} Master {/processing_system7_0/M_AXI_GP0} Slave {/axi_gpio_"+ str(gpio_index) +"/S_AXI} intc_ip {New AXI Interconnect} master_apm {0}}  [get_bd_intf_pins axi_gpio_" + str(gpio_index) + "/S_AXI]\n\n")


                        tclFile.write("apply_bd_automation -rule xilinx.com:bd_rule:board -config { Board_Interface {Custom} Manual_Source {Auto}}  [get_bd_intf_pins axi_gpio_"+ str(gpio_index) +"/GPIO]\n\n")

                    elif ("output" in item):
                        widthSize = item[3]
                        widthSize = widthSize[:-4]
                        tclFile.write("set_property -dict [list CONFIG.C_GPIO_WIDTH {" + widthSize + "} CONFIG.C_ALL_OUTPUTS {1}] [get_bd_cells axi_gpio_"+ str(gpio_index) +"]\n")
                        tclFile.write("apply_bd_automation -rule xilinx.com:bd_rule:axi4 -config { Clk_master {Auto} Clk_slave {Auto} Clk_xbar {Auto} Master {/processing_system7_0/M_AXI_GP0} Slave {/axi_gpio_"+ str(gpio_index) +"/S_AXI} intc_ip {New AXI Interconnect} master_apm {0}}  [get_bd_intf_pins axi_gpio_"+ str(gpio_index) +"/S_AXI]\n")
                        tclFile.write("apply_bd_automation -rule xilinx.com:bd_rule:board -config { Board_Interface {Custom} Manual_Source {Auto}}  [get_bd_intf_pins axi_gpio_"+ str(gpio_index) +"/GPIO]\n\n")



    tclFile.write("validate_bd_design -force\n")
    tclFile.write("save_bd_design\n")

    tclFile.close()

    print("Done")
