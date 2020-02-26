#MeXT-SE software source code
#author: Md Jubaer Hossain Pantho
#University of Florida

def ScriptGeneration(systemData, cpuConfList, memConfList, comConfData, filePath):
    print("Generating secure script for Xilinx FPGA")
    print(systemData)

    tclFile = open(filePath[:-4] + "Secure.tcl", "w")
    projectDir = filePath.split('/')
    projectName = projectDir[-1]
    projectName = projectName[:-4] + "_secure"
    print(projectName)


    create_project = "create_project " + projectName + " " + filePath[:-4] + "_secure" + " -part xc7vx485tffg1157-1\n"
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


    tclFile.write("create_bd_design \"design_1\"\n")
    tclFile.write("update_compile_order -fileset sources_1\n\n")

    #adding static IP repo. This will be changed to a dynamically added repo in future
    tclFile.write("set_property  ip_repo_paths  /home/mdjubaer/vivado-projects/mext-project/ip_repo [current_project]\n")
    tclFile.write("update_ip_catalog\n\n")

    count = 0

    gpio_index = -1
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

            elif ("ipcore" in item[0]):
                gpio_index = gpio_index + 1
                if ("GPIO" in item):
                    tclFile.write("startgroup\n")
                    tclFile.write("create_bd_cell -type ip -vlnv user.org:user:himm_module:1.0 himm_module_"+ str(gpio_index) +"\n")
                    tclFile.write("endgroup\n\n")

                    if ("output" in item):
                        widthSize = item[3]
                        widthSize = widthSize[:-4]
                        tclFile.write("set_property -dict [list CONFIG.SECURE_DATA_OUT_WIDTH {" + widthSize + "}] [get_bd_cells himm_module_" + str(gpio_index) + "]\n\n")
                    tclFile.write("apply_bd_automation -rule xilinx.com:bd_rule:axi4 -config { Clk_master {Auto} Clk_slave {Auto} Clk_xbar {Auto} Master {/processing_system7_0/M_AXI_GP0} Slave {/himm_module_" + str(gpio_index) + "/S00_AXI} intc_ip {New AXI Interconnect} master_apm {0}}  [get_bd_intf_pins himm_module_" + str(gpio_index) + "/S00_AXI]\n\n") 

                    tclFile.write("startgroup\n")
                    tclFile.write("make_bd_pins_external  [get_bd_pins himm_module_" + str(gpio_index) + "/secure_data_out]\n")
                    tclFile.write("endgroup\n\n")

    tclFile.write("validate_bd_design -force\n")
    tclFile.write("save_bd_design\n")

    tclFile.close()

    print("Secure Script Generation Done")



