#MeXT-SE software source code
#author: Md Jubaer Hossain Pantho
#University of Florida

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
