#******Start of Adding new policy module********
sestatus
#check if SELinux status is enabled in permissive mode and Loaded policy name is refpolicy.
#create the .te file, write the policy and save it
make -f /usr/share/selinux/devel/Makefile dummy.pp
semodule -i dummy.pp
