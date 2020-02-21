create_project bramExample /home/mdjubaer/workspace-2020/python-gui/MeXT-SE/design-folder/bramExample -part xc7vx485tffg1157-1
set_property board_part digilentinc.com:zybo-z7-10:part0:1.0 [current_project]
update_ip_catalog

create_bd_design "design_1"
update_compile_order -fileset sources_1
startgroup
create_bd_cell -type ip -vlnv xilinx.com:ip:processing_system7:5.5 processing_system7_0
endgroup

apply_bd_automation -rule xilinx.com:bd_rule:processing_system7 -config {make_external "FIXED_IO, DDR" apply_board_preset "1" Master "Disable" Slave "Disable" }  [get_bd_cells processing_system7_0]
startgroup
create_bd_cell -type ip -vlnv xilinx.com:ip:axi_bram_ctrl:4.0 axi_bram_ctrl_0
endgroup

startgroup
create_bd_cell -type ip -vlnv xilinx.com:ip:blk_mem_gen:8.4 blk_mem_gen_0
endgroup

set_property -dict [list CONFIG.SINGLE_PORT_BRAM {1}] [get_bd_cells axi_bram_ctrl_0]
apply_bd_automation -rule xilinx.com:bd_rule:bram_cntlr -config {BRAM "Auto" }  [get_bd_intf_pins axi_bram_ctrl_0/BRAM_PORTA]

apply_bd_automation -rule xilinx.com:bd_rule:axi4 -config { Clk_master {Auto} Clk_slave {Auto} Clk_xbar {Auto} Master {/processing_system7_0/M_AXI_GP0} Slave {/axi_bram_ctrl_0/S_AXI} intc_ip {Auto} master_apm {0}}  [get_bd_intf_pins axi_bram_ctrl_0/S_AXI]

validate_bd_design -force
save_bd_design
