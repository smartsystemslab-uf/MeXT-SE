`timescale 1ns / 1ps



module himm_module_v1_0_S00_Avalon#
    (
    // Users to add parameters here
    parameter integer SECURE_DATA_OUT_WIDTH = 32,

    // User parameters ends
    // Do not modify the parameters beyond this line

    // Width of S_AVALON data bus
    parameter integer C_S_AVALON_DATA_WIDTH = 32,
    // Width of S_AVALON address bus
    parameter integer C_S_AVALON_ADDR_WIDTH = 4
)
(
  // Avalon Slave bus
  input S0_CLK,
  input S0_RESET,
  
  input [C_S_AVALON_ADDR_WIDTH-1 : 0] S0_ADDRESS,
  input S0_WRITE,
  input [C_S_AVALON_DATA_WIDTH-1 : 0] S0_WRITEDATA,
  input S0_READ,
  output [C_S_AVALON_DATA_WIDTH-1 : 0] S0_READDATA,
  
  // External bus
  output wire [SECURE_DATA_OUT_WIDTH - 1 : 0] secure_data_out

    );
    
//Joel For you

 //-- Number of Slave Registers 4
 reg [SECURE_DATA_OUT_WIDTH-1:0]    slv_reg0;
 reg [SECURE_DATA_OUT_WIDTH-1:0]    slv_reg1;
 reg [SECURE_DATA_OUT_WIDTH-1:0]    slv_reg2;
 reg [SECURE_DATA_OUT_WIDTH-1:0]    slv_reg3;

 reg [SECURE_DATA_OUT_WIDTH-1:0]    base_address = 32'h40000000;

always @( posedge S0_CLK)
begin
	
	if (S0_WRITE == 1) begin
	   if (S0_ADDRESS == base_address)
	       slv_reg0 <= S0_WRITEDATA;
	   else if (S0_ADDRESS == base_address + 4)
	       slv_reg1 <= S0_WRITEDATA;
	   else if (S0_ADDRESS == base_address + 8)
           slv_reg2 <= S0_WRITEDATA;
	   else if (S0_ADDRESS == base_address + 12)
           slv_reg3 <= S0_WRITEDATA;
	
	end
	
end


//joel for you
        
// himm user logic here
 reg[31:0] labelList[9:0];
 reg[31:0] count=0;
 reg[31:0] updateLabelTag = 102;  //label tag to update policy from simm
 reg[31:0] dataOut =0;
 
initial begin
     labelList[0] = 100;  // 1 static label
     labelList[1] = -1;
     labelList[2] = -1;
     labelList[3] = -1;
     labelList[4] = -1;
     labelList[5] = -1;
     labelList[6] = -1;
     labelList[7] = -1;
     labelList[8] = -1;
     labelList[9] = -1;
 end
 

 always @(posedge S0_CLK) begin
 
     if (slv_reg0 == labelList[0])
         dataOut <= slv_reg1;
     else if(slv_reg0 == labelList[1])
         dataOut <= slv_reg1;
     else if(slv_reg0 == labelList[2])
         dataOut <= slv_reg1;    
     else if(slv_reg0 == labelList[3])
         dataOut <= slv_reg1;
     else if(slv_reg0 == labelList[4])
         dataOut <= slv_reg1;
     else if(slv_reg0 == labelList[5])
         dataOut <= slv_reg1;
     else if(slv_reg0 == labelList[6])
         dataOut <= slv_reg1;
     else if(slv_reg0 == labelList[7])
         dataOut <= slv_reg1;
     else if(slv_reg0 == labelList[8])
          dataOut <= slv_reg1;
     else if(slv_reg0 == labelList[9])
          dataOut <= slv_reg1;
          
          
     if (slv_reg0 == updateLabelTag && labelList[count] != slv_reg1)
     begin
         labelList[count + 1] <= slv_reg1;
         count <= count + 1;
     end
                 
end



assign secure_data_out[SECURE_DATA_OUT_WIDTH-1:0] = dataOut[SECURE_DATA_OUT_WIDTH-1:0];


endmodule
