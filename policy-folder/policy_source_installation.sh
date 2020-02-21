#!/bin/sh
#commands for installing policy source module
#set SELinux in permissive mode by changing /etc/selinux/config file (Don't forget to put the command touch /.autorelabel before SELinux mode change)
wget https://raw.githubusercontent.com/wiki/TresysTechnology/refpolicy/files/refpolicy-2.20180114.tar.bz2
tar -jxvf refpolicy-2.20180114.tar.bz2 -C /tmp
cd /tmp/refpolicy
make install-src
cd /etc/selinux/refpolicy/src/policy
#open build.conf file and uncomment DISTRO = redhat, make UNK_PERMS = allow, DIRECT_INITRC = y, SYSTEMD = y, MONOLITHIC = y and save the file
make install
make load
#change SELinux type as refpolicy in /etc/selinux/config file (Don't forget to put the command touch /.autorelabel before changing SELinux type)
