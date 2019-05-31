#mount
sshfs balint@ccnet1.tmit.bme.hu:/home/balint/workspace /home/balint/remote_workspace/
sshfs balint@ccnet3.dmlab.hu:/home/simon /home/balint/remote_workspace/

#unmount
fusermount -u /home/balint/remote_workspace/
#force? unmount
sudo umount -l /home/balint/remote_workspace/


#fusson, amikor kilepek, akkor is
#belepni:
screen
#kilepni:
#   Ctrl-A + Ctrl-D
#listazni a meglevoket:
screen -ls
#visszalepni $(a session szama)
screen -r $(...)
#kill $(a session szama)
screen -X -S $(...) kill


