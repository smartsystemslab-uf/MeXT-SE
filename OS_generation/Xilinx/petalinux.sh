#petalinux commands for OS image generation
petalinux-create --type project --template zynq --name <PROJECT_NAME>
cd <PROJECT_NAME>
petalinux-config --get-hw-description=<path-to-directory-containing- hardware description-file(.hdf file)>
petalinux-build
petalinux-package --boot --fsbl <Zynq FSBL image> --fpga <FPGA bitstream> --u-boot
