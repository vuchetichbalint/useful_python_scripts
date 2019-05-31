sudo mount -o ro /dev/sdb1 /home/balint/500gb


time tar -zcvf backup_workspace_$(date +"%Y%m%d").tar.gz workspace/ 

#elsoev
time tar -zcvf backup_00-TANANYAGOK_2011_osz_$(date +"%Y%m%d").tar.gz /home/balint/500gb/e_final/00-TANANYAGOK/2011_osz/ 
time tar -zcvf backup_00-TANANYAGOK_2012_tavasz_$(date +"%Y%m%d").tar.gz /home/balint/500gb/e_final/00-TANANYAGOK/2012__tavasz/

#masodev
time tar -zcvf backup_00-TANANYAGOK_2012_osz_$(date +"%Y%m%d").tar.gz /home/balint/500gb/e_final/00-TANANYAGOK/2012_osz/ 
time tar -zcvf backup_00-TANANYAGOK_2013__tavasz_$(date +"%Y%m%d").tar.gz /home/balint/500gb/e_final/00-TANANYAGOK/2013__tavasz/ 

#harmadev
time tar -zcvf backup_00-TANANYAGOK_2013__osz_$(date +"%Y%m%d").tar.gz /home/balint/500gb/e_final/00-TANANYAGOK/2013_osz/ 
time tar -zcvf backup_00-TANANYAGOK_2014__tavasz_$(date +"%Y%m%d").tar.gz /home/balint/500gb/e_final/00-TANANYAGOK/2014__tavasz/ 

#negyedev
time tar -zcvf backup_00-TANANYAGOK_2014_osz_$(date +"%Y%m%d").tar.gz /home/balint/500gb/e_final/00-TANANYAGOK/2014_osz/ 
time tar -zcvf backup_00-TANANYAGOK_2015__tavasz_$(date +"%Y%m%d").tar.gz /home/balint/500gb/e_final/00-TANANYAGOK/2015__tavasz/ 

#otodev
time tar -zcvf backup_00-TANANYAGOK_2015_osz_$(date +"%Y%m%d").tar.gz /home/balint/500gb/e_final/00-TANANYAGOK/2015_osz/ 
time tar -zcvf backup_00-TANANYAGOK_2016__tavasz_$(date +"%Y%m%d").tar.gz /home/balint/500gb/e_final/00-TANANYAGOK/2016__tavasz/ 

#hatodev
time tar -zcvf backup_00-TANANYAGOK_2016_osz_$(date +"%Y%m%d").tar.gz /home/balint/Documents/000-TANANYAGOK/2016_osz/
time tar -zcvf backup_00-TANANYAGOK_2017__tavasz_$(date +"%Y%m%d").tar.gz /home/balint/Documents/000-TANANYAGOK/2017__tavasz/


keycode 89 = Escape

xmodmap -e "keycode 107 = Escape"