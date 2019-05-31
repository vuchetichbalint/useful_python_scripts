# start
vboxmanage startvm "Windows 10" --type headless
# stop (hmmm, it seems like a little too hard...)
vboxmanage startvm "Windows 10" --type emergencystop



https://www.virtualbox.org/manual/ch07.html


VBoxManage list ostypes
# innen az ID kell

VBoxManage createvm --name "Turbo Windows 10" --ostype Windows10_64 --register

VBoxManage modifyvm "Turbo Windows 10" --memory 8192 --cpus 4 --nic1 nat 


VBoxManage createhd --filename "hd/turbowindows.vdi" --size 500000


VBoxManage storagectl "Turbo Windows 10" --name "IDE Controller" --add ide --controller PIIX4

VBoxManage storageattach "Turbo Windows 10" --storagectl "IDE Controller" --port 0 --device 0 --type hdd --medium "hd/turbowindows.vdi"

VBoxManage storageattach "Turbo Windows 10" --storagectl "IDE Controller" --port 0 --device 1 --type dvddrive --medium "/home/virtualbox-vms/iso/win10_1803.iso"

VBoxManage modifyvm "Turbo Windows 10" --vrde on
VBoxManage modifyvm "Turbo Windows 10" --vrdeaddress 3390

VBoxHeadless --startvm "Turbo Windows 10"


--vrde on
 --acpi on --boot1 dvd --nic1 nat



vboxmanage startvm "Turbo Windows 10" --type headless



VBoxManage showvminfo "Turbo Windows 10"


vboxmanage startvm "Turbo Windows 10" --type emergencystop