#!/usr/bin/evn python 

import os

os.system("sudo apt-get install gedit")
os.system("sudo apt-get install tor")
os.system("service tor start")
os.system("sudo apt-get install git")
os.system("git clone https://github.com/ruped24/toriptables2.git")
os.system("git clone https://github.com/ruped24/tor_ip_switcher.git")
os.system("gedit -s etc/tor/torrc")
