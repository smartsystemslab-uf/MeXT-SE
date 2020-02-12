#MeXT-SE software source code
#author: Md Jubaer Hossain Pantho
#University of Florida
#editor: This section is added by Sujan
import os, sys
import ntpath

def AddNewRuleToFile(filename, subjectData, objectData, classData, commandData, rd, wr, ex, index):
    file_object = open(filename, 'a')

    if (subjectData != "" and objectData != "" and classData != "" and commandData != ""):
        if (rd == 1 or wr == 1 or ex == 1):

            read = ""
            write = ""
            execute = ""

            if (rd):
                read = "read "
            if (wr):
                write = "write "
            if (ex):
                execute = "execute"

            file_object.write("\npolicy_module(policy" + str(index)+  ", 1.0)\n")
            file_object.write("gen_require(`\n")
            file_object.write("type "+ subjectData + ";\n")
            file_object.write("type "+ objectData + ";\n")
            file_object.write("')\n" + commandData + " " + subjectData + " " + objectData + ": " + classData + "{")
        

            file_object.write(read +  write + execute + "};")
        else:
            print("No access permission given. Rule not added")
    else:
        print("Subject/Object Missing. Rule not added")
    # Close the file
    file_object.close()




def GenPolicyScript(filename):
    print("Policy Script Code for ", filename)
    #Code to generate policy source module installation
    f=open("../policy-folder/policy_source_installation.sh","w+")
    f.write("#!/bin/sh\n")
    f.write("#commands for installing policy source module\n")
    f.write("#set SELinux in permissive mode by changing /etc/selinux/config file (Don't forget to put the command touch /.autorelabel before SELinux mode change)\n")
    f.write("wget https://raw.githubusercontent.com/wiki/TresysTechnology/refpolicy/files/refpolicy-2.20180114.tar.bz2\n")
    f.write("tar -jxvf refpolicy-2.20180114.tar.bz2 -C /tmp\n")
    f.write("cd /tmp/refpolicy\n")
    f.write("make install-src\n")
    f.write("cd /etc/selinux/refpolicy/src/policy\n")
    f.write("#open build.conf file and uncomment DISTRO = redhat, make UNK_PERMS = allow, DIRECT_INITRC = y, SYSTEMD = y, MONOLITHIC = y and save the file\n")
    f.write("make install\n")
    f.write("make load\n")
    f.write("#change SELinux type as refpolicy in /etc/selinux/config file (Don't forget to put the command touch /.autorelabel before changing SELinux type)\n")
    f.close()

    #code to generate policy loading script
    filename_new_withEx = ntpath.basename(filename)
    filename_new_noEx = os.path.splitext(filename_new_withEx)[0]
    f=open("../policy-folder/policy_integration.sh","w+")
    f.write("#******Start of Adding new policy module********\n")
    f.write("sestatus\n")
    f.write("#check if SELinux status is enabled in permissive mode and Loaded policy name is refpolicy.\n")
    f.write("#create the .te file, write the policy and save it\n")
    f.write("make -f /usr/share/selinux/devel/Makefile ")
    f.write(filename_new_noEx+".pp\n")
    f.write("semodule -i ")
    f.write(filename_new_noEx+".pp\n")
    f.close()
