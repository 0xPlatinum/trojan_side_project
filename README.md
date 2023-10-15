Hi, i was curious about trojans, so i made a simple trojan. Running it will display current system stats in one thread, but in another it will make itself persistance between cmd sessions as well as
send a reverse shell every 3 seconds. It also makes itself persistent between restarts/shutdowns by modifying the users home directory .rc file. it finds the shell
the user is currently using and adds the rev shell to it. If they remove the change, it will be added back shortly.
however, sadly, i only found that this works if they run nohup python3 trojan.py > /dev/null 2>&1.
maybe i find a new way in the future.
