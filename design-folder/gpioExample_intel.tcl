# qsys scripting (.tcl) file
package require -exact qsys 16.0

create_system {gpioExample_intel}

set_project_property DEVICE_FAMILY {Cyclone V} 
set_project_property DEVICE {5CSEMA5F31C6}
set_project_property HIDE_FROM_IP_CATALOG {false}

#Instances and instance parameters
add_instance CPU altera_nios2_gen2 18.1
set_instance_parameter_value CPU {bht_ramBlockType} {Automatic}
set_instance_parameter_value CPU {breakOffset} {32}
set_instance_parameter_value CPU {breakSlave} {None}
set_instance_parameter_value CPU {cdx_enabled} {0}
set_instance_parameter_value CPU {cpuArchRev} {1}
set_instance_parameter_value CPU {cpuID} {0}
set_instance_parameter_value CPU {cpuReset} {0}
set_instance_parameter_value CPU {data_master_high_performance_paddr_base} {0}
set_instance_parameter_value CPU {data_master_high_performance_paddr_size} {0.0}
set_instance_parameter_value CPU {data_master_paddr_base} {0}
set_instance_parameter_value CPU {data_master_paddr_size} {0.0}
set_instance_parameter_value CPU {dcache_bursts} {false}
set_instance_parameter_value CPU {dcache_numTCDM} {0}
set_instance_parameter_value CPU {dcache_ramBlockType} {Automatic}
set_instance_parameter_value CPU {dcache_size} {2048}
set_instance_parameter_value CPU {dcache_tagramBlockType} {Automatic}
set_instance_parameter_value CPU {dcache_victim_buf_impl} {ram}
set_instance_parameter_value CPU {debug_OCIOnchipTrace} {_128}
set_instance_parameter_value CPU {debug_assignJtagInstanceID} {0}
set_instance_parameter_value CPU {debug_datatrigger} {0}
set_instance_parameter_value CPU {debug_debugReqSignals} {0}
set_instance_parameter_value CPU {debug_enabled} {1}
set_instance_parameter_value CPU {debug_hwbreakpoint} {0}
set_instance_parameter_value CPU {debug_jtagInstanceID} {0}
set_instance_parameter_value CPU {debug_traceStorage} {onchip_trace}
set_instance_parameter_value CPU {debug_traceType} {none}
set_instance_parameter_value CPU {debug_triggerArming} {1}
set_instance_parameter_value CPU {dividerType} {no_div}
set_instance_parameter_value CPU {exceptionOffset} {32}
set_instance_parameter_value CPU {exceptionSlave} {MEMORY1.s1}
set_instance_parameter_value CPU {fa_cache_line} {2}
set_instance_parameter_value CPU {fa_cache_linesize} {0}
set_instance_parameter_value CPU {flash_instruction_master_paddr_base} {0}
set_instance_parameter_value CPU {flash_instruction_master_paddr_size} {0.0}
set_instance_parameter_value CPU {icache_burstType} {None}
set_instance_parameter_value CPU {icache_numTCIM} {0}
set_instance_parameter_value CPU {icache_ramBlockType} {Automatic}
set_instance_parameter_value CPU {icache_size} {4096}
set_instance_parameter_value CPU {icache_tagramBlockType} {Automatic}
set_instance_parameter_value CPU {impl} {Fast}
set_instance_parameter_value CPU {instruction_master_high_performance_paddr_base} {0}
set_instance_parameter_value CPU {instruction_master_high_performance_paddr_size} {0.0}
set_instance_parameter_value CPU {instruction_master_paddr_base} {0}
set_instance_parameter_value CPU {instruction_master_paddr_size} {0.0}
set_instance_parameter_value CPU {io_regionbase} {0}
set_instance_parameter_value CPU {io_regionsize} {0}
set_instance_parameter_value CPU {master_addr_map} {0}
set_instance_parameter_value CPU {mmu_TLBMissExcOffset} {0}
set_instance_parameter_value CPU {mmu_TLBMissExcSlave} {None}
set_instance_parameter_value CPU {mmu_autoAssignTlbPtrSz} {1}
set_instance_parameter_value CPU {mmu_enabled} {0}
set_instance_parameter_value CPU {mmu_processIDNumBits} {8}
set_instance_parameter_value CPU {mmu_ramBlockType} {Automatic}
set_instance_parameter_value CPU {mmu_tlbNumWays} {16}
set_instance_parameter_value CPU {mmu_tlbPtrSz} {7}
set_instance_parameter_value CPU {mmu_udtlbNumEntries} {6}
set_instance_parameter_value CPU {mmu_uitlbNumEntries} {4}
set_instance_parameter_value CPU {mpu_enabled} {0}
set_instance_parameter_value CPU {mpu_minDataRegionSize} {12}
set_instance_parameter_value CPU {mpu_minInstRegionSize} {12}
set_instance_parameter_value CPU {mpu_numOfDataRegion} {8}
set_instance_parameter_value CPU {mpu_numOfInstRegion} {8}
set_instance_parameter_value CPU {mpu_useLimit} {0}
set_instance_parameter_value CPU {mpx_enabled} {0}
set_instance_parameter_value CPU {mul_32_impl} {2}
set_instance_parameter_value CPU {mul_64_impl} {0}
set_instance_parameter_value CPU {mul_shift_choice} {0}
set_instance_parameter_value CPU {ocimem_ramBlockType} {Automatic}
set_instance_parameter_value CPU {ocimem_ramInit} {0}
set_instance_parameter_value CPU {regfile_ramBlockType} {Automatic}
set_instance_parameter_value CPU {register_file_por} {0}
set_instance_parameter_value CPU {resetOffset} {0}
set_instance_parameter_value CPU {resetSlave} {CPU.debug_mem_slave}
set_instance_parameter_value CPU {resetrequest_enabled} {1}
set_instance_parameter_value CPU {setting_HBreakTest} {0}
set_instance_parameter_value CPU {setting_HDLSimCachesCleared} {1}
set_instance_parameter_value CPU {setting_activateMonitors} {1}
set_instance_parameter_value CPU {setting_activateTestEndChecker} {0}
set_instance_parameter_value CPU {setting_activateTrace} {0}
set_instance_parameter_value CPU {setting_allow_break_inst} {0}
set_instance_parameter_value CPU {setting_alwaysEncrypt} {1}
set_instance_parameter_value CPU {setting_asic_add_scan_mode_input} {0}
set_instance_parameter_value CPU {setting_asic_enabled} {0}
set_instance_parameter_value CPU {setting_asic_synopsys_translate_on_off} {0}
set_instance_parameter_value CPU {setting_asic_third_party_synthesis} {0}
set_instance_parameter_value CPU {setting_avalonDebugPortPresent} {0}
set_instance_parameter_value CPU {setting_bhtPtrSz} {8}
set_instance_parameter_value CPU {setting_bigEndian} {0}
set_instance_parameter_value CPU {setting_branchpredictiontype} {Dynamic}
set_instance_parameter_value CPU {setting_breakslaveoveride} {0}
set_instance_parameter_value CPU {setting_clearXBitsLDNonBypass} {1}
set_instance_parameter_value CPU {setting_dc_ecc_present} {1}
set_instance_parameter_value CPU {setting_disable_tmr_inj} {0}
set_instance_parameter_value CPU {setting_disableocitrace} {0}
set_instance_parameter_value CPU {setting_dtcm_ecc_present} {1}
set_instance_parameter_value CPU {setting_ecc_present} {0}
set_instance_parameter_value CPU {setting_ecc_sim_test_ports} {0}
set_instance_parameter_value CPU {setting_exportHostDebugPort} {0}
set_instance_parameter_value CPU {setting_exportPCB} {0}
set_instance_parameter_value CPU {setting_export_large_RAMs} {0}
set_instance_parameter_value CPU {setting_exportdebuginfo} {0}
set_instance_parameter_value CPU {setting_exportvectors} {0}
set_instance_parameter_value CPU {setting_fast_register_read} {0}
set_instance_parameter_value CPU {setting_ic_ecc_present} {1}
set_instance_parameter_value CPU {setting_interruptControllerType} {Internal}
set_instance_parameter_value CPU {setting_itcm_ecc_present} {1}
set_instance_parameter_value CPU {setting_mmu_ecc_present} {1}
set_instance_parameter_value CPU {setting_oci_export_jtag_signals} {0}
set_instance_parameter_value CPU {setting_oci_version} {1}
set_instance_parameter_value CPU {setting_preciseIllegalMemAccessException} {0}
set_instance_parameter_value CPU {setting_removeRAMinit} {0}
set_instance_parameter_value CPU {setting_rf_ecc_present} {1}
set_instance_parameter_value CPU {setting_shadowRegisterSets} {0}
set_instance_parameter_value CPU {setting_showInternalSettings} {0}
set_instance_parameter_value CPU {setting_showUnpublishedSettings} {0}
set_instance_parameter_value CPU {setting_support31bitdcachebypass} {1}
set_instance_parameter_value CPU {setting_tmr_output_disable} {0}
set_instance_parameter_value CPU {setting_usedesignware} {0}
set_instance_parameter_value CPU {shift_rot_impl} {1}
set_instance_parameter_value CPU {tightly_coupled_data_master_0_paddr_base} {0}
set_instance_parameter_value CPU {tightly_coupled_data_master_0_paddr_size} {0.0}
set_instance_parameter_value CPU {tightly_coupled_data_master_1_paddr_base} {0}
set_instance_parameter_value CPU {tightly_coupled_data_master_1_paddr_size} {0.0}
set_instance_parameter_value CPU {tightly_coupled_data_master_2_paddr_base} {0}
set_instance_parameter_value CPU {tightly_coupled_data_master_2_paddr_size} {0.0}
set_instance_parameter_value CPU {tightly_coupled_data_master_3_paddr_base} {0}
set_instance_parameter_value CPU {tightly_coupled_data_master_3_paddr_size} {0.0}
set_instance_parameter_value CPU {tightly_coupled_instruction_master_0_paddr_base} {0}
set_instance_parameter_value CPU {tightly_coupled_instruction_master_0_paddr_size} {0.0}
set_instance_parameter_value CPU {tightly_coupled_instruction_master_1_paddr_base} {0}
set_instance_parameter_value CPU {tightly_coupled_instruction_master_1_paddr_size} {0.0}
set_instance_parameter_value CPU {tightly_coupled_instruction_master_2_paddr_base} {0}
set_instance_parameter_value CPU {tightly_coupled_instruction_master_2_paddr_size} {0.0}
set_instance_parameter_value CPU {tightly_coupled_instruction_master_3_paddr_base} {0}
set_instance_parameter_value CPU {tightly_coupled_instruction_master_3_paddr_size} {0.0}
set_instance_parameter_value CPU {tmr_enabled} {0}
set_instance_parameter_value CPU {tracefilename} {}
set_instance_parameter_value CPU {userDefinedSettings} {}

add_instance GPIO altera_avalon_pio 18.1
set_instance_parameter_value GPIO {bitClearingEdgeCapReg} {0}
set_instance_parameter_value GPIO {bitModifyingOutReg} {0}
set_instance_parameter_value GPIO {captureEdge} {0}
set_instance_parameter_value GPIO {direction} {Output}
set_instance_parameter_value GPIO {edgeType} {RISING}
set_instance_parameter_value GPIO {generateIRQ} {0}
set_instance_parameter_value GPIO {irqType} {LEVEL}
set_instance_parameter_value GPIO {resetValue} {0.0}
set_instance_parameter_value GPIO {simDoTestBenchWiring} {0}
set_instance_parameter_value GPIO {simDrivenValue} {0.0}
set_instance_parameter_value GPIO {width} {8}

add_instance MEMORY1 altera_avalon_onchip_memory2 18.1
set_instance_parameter_value MEMORY1 {allowInSystemMemoryContentEditor} {0}
set_instance_parameter_value MEMORY1 {blockType} {AUTO}
set_instance_parameter_value MEMORY1 {copyInitFile} {0}
set_instance_parameter_value MEMORY1 {dataWidth} {32}
set_instance_parameter_value MEMORY1 {dataWidth2} {32}
set_instance_parameter_value MEMORY1 {dualPort} {0}
set_instance_parameter_value MEMORY1 {ecc_enabled} {0}
set_instance_parameter_value MEMORY1 {enPRInitMode} {0}
set_instance_parameter_value MEMORY1 {enableDiffWidth} {0}
set_instance_parameter_value MEMORY1 {initMemContent} {1}
set_instance_parameter_value MEMORY1 {initializationFileName} {onchip_mem.hex}
set_instance_parameter_value MEMORY1 {instanceID} {NONE}
set_instance_parameter_value MEMORY1 {memorySize} {409600.0}
set_instance_parameter_value MEMORY1 {readDuringWriteMode} {DONT_CARE}
set_instance_parameter_value MEMORY1 {resetrequest_enabled} {1}
set_instance_parameter_value MEMORY1 {simAllowMRAMContentsFile} {0}
set_instance_parameter_value MEMORY1 {simMemInitOnlyFilename} {0}
set_instance_parameter_value MEMORY1 {singleClockOperation} {0}
set_instance_parameter_value MEMORY1 {slave1Latency} {1}
set_instance_parameter_value MEMORY1 {slave2Latency} {1}
set_instance_parameter_value MEMORY1 {useNonDefaultInitFile} {0}
set_instance_parameter_value MEMORY1 {useShallowMemBlocks} {0}
set_instance_parameter_value MEMORY1 {writable} {1}

add_instance clk_0 clock_source 18.1
set_instance_parameter_value clk_0 {clockFrequency} {50000000.0}
set_instance_parameter_value clk_0 {clockFrequencyKnown} {1}
set_instance_parameter_value clk_0 {resetSynchronousEdges} {NONE}

add_instance jtag_uart_0 altera_avalon_jtag_uart 18.1
set_instance_parameter_value jtag_uart_0 {allowMultipleConnections} {0}
set_instance_parameter_value jtag_uart_0 {hubInstanceID} {0}
set_instance_parameter_value jtag_uart_0 {readBufferDepth} {64}
set_instance_parameter_value jtag_uart_0 {readIRQThreshold} {8}
set_instance_parameter_value jtag_uart_0 {simInputCharacterStream} {}
set_instance_parameter_value jtag_uart_0 {simInteractiveOptions} {NO_INTERACTIVE_WINDOWS}
set_instance_parameter_value jtag_uart_0 {useRegistersForReadBuffer} {0}
set_instance_parameter_value jtag_uart_0 {useRegistersForWriteBuffer} {0}
set_instance_parameter_value jtag_uart_0 {useRelativePathForSimFile} {0}
set_instance_parameter_value jtag_uart_0 {writeBufferDepth} {64}
set_instance_parameter_value jtag_uart_0 {writeIRQThreshold} {8}

# exported interfaces
add_interface clk clock sink
set_interface_property clk EXPORT_OF clk_0.clk_in
add_interface gpio conduit end
set_interface_property gpio EXPORT_OF GPIO.external_connection
add_interface reset reset sink
set_interface_property reset EXPORT_OF clk_0.clk_in_reset

# connections and connection parameters
add_connection CPU.data_master CPU.debug_mem_slave
set_connection_parameter_value CPU.data_master/CPU.debug_mem_slave arbitrationPriority {1}
set_connection_parameter_value CPU.data_master/CPU.debug_mem_slave baseAddress {0x00100800}
set_connection_parameter_value CPU.data_master/CPU.debug_mem_slave defaultConnection {0}

add_connection CPU.data_master GPIO.s1
set_connection_parameter_value CPU.data_master/GPIO.s1 arbitrationPriority {1}
set_connection_parameter_value CPU.data_master/GPIO.s1 baseAddress {0x00101000}
set_connection_parameter_value CPU.data_master/GPIO.s1 defaultConnection {0}

add_connection CPU.data_master MEMORY1.s1
set_connection_parameter_value CPU.data_master/MEMORY1.s1 arbitrationPriority {1}
set_connection_parameter_value CPU.data_master/MEMORY1.s1 baseAddress {0x00080000}
set_connection_parameter_value CPU.data_master/MEMORY1.s1 defaultConnection {0}

add_connection CPU.data_master jtag_uart_0.avalon_jtag_slave
set_connection_parameter_value CPU.data_master/jtag_uart_0.avalon_jtag_slave arbitrationPriority {1}
set_connection_parameter_value CPU.data_master/jtag_uart_0.avalon_jtag_slave baseAddress {0x00101010}
set_connection_parameter_value CPU.data_master/jtag_uart_0.avalon_jtag_slave defaultConnection {0}

add_connection CPU.instruction_master CPU.debug_mem_slave
set_connection_parameter_value CPU.instruction_master/CPU.debug_mem_slave arbitrationPriority {1}
set_connection_parameter_value CPU.instruction_master/CPU.debug_mem_slave baseAddress {0x00100800}
set_connection_parameter_value CPU.instruction_master/CPU.debug_mem_slave defaultConnection {0}

add_connection CPU.instruction_master MEMORY1.s1
set_connection_parameter_value CPU.instruction_master/MEMORY1.s1 arbitrationPriority {1}
set_connection_parameter_value CPU.instruction_master/MEMORY1.s1 baseAddress {0x00080000}
set_connection_parameter_value CPU.instruction_master/MEMORY1.s1 defaultConnection {0}

add_connection CPU.irq jtag_uart_0.irq
set_connection_parameter_value CPU.irq/jtag_uart_0.irq irqNumber {0}

add_connection clk_0.clk CPU.clk
add_connection clk_0.clk GPIO.clk
add_connection clk_0.clk MEMORY1.clk1
add_connection clk_0.clk jtag_uart_0.clk

add_connection clk_0.clk_reset CPU.reset
add_connection clk_0.clk_reset GPIO.reset
add_connection clk_0.clk_reset MEMORY1.reset1
add_connection clk_0.clk_reset jtag_uart_0.reset
# interconnect requirements
set_interconnect_requirement {$system} {qsys_mm.clockCrossingAdapter} {HANDSHAKE}
set_interconnect_requirement {$system} {qsys_mm.enableEccProtection} {FALSE}
set_interconnect_requirement {$system} {qsys_mm.insertDefaultSlave} {FALSE}
set_interconnect_requirement {$system} {qsys_mm.maxAdditionalLatency} {1}

# To make sure that there is no collision between addresses
auto_assign_system_base_addresses
#validates the system
validate_system

save_system {gpioExample_intel.qsys}
