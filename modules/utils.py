#!/usr/bin/env python2.7
#coding=UTF-8

# Copyright (c) 2016 Angelo Moura
#
# This file is part of the program PytheM
#
# PytheM is free software; you can redistribute it and/or
# modify it under the terms of the GNU General Public License as
# published by the Free Software Foundation; either version 3 of the
# License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# General Public License for more details.
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA 02111-1307
# USA

import os
import sys
import socket
import fcntl
import struct
import urllib
import base64
import termcolor


def decode(base):
        text = raw_input("[*] String to be decoded: ")
        decode = text.decode('{}'.format(base))
	result = "[+] Result: {}".format(decode)
	return result

def encode(base):
        text = raw_input("[*] String to be encoded: ")
	encode = text.encode('{}'.format(base))
	result = "[+] Result: {}".format(encode)
	return result

def cookiedecode():
	cookie = raw_input("[+] Enter the cookie value: ")
	res = base64.b64decode(urllib.unquote(cookie))
	print
	print res

def get_myip(interface):
	s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	return socket.inet_ntoa(fcntl.ioctl(
		s.fileno(),
		0x8915,
		struct.pack('256s', interface[:15])
	)[20:24])


def get_mymac(interface):
    	s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    	info = fcntl.ioctl(s.fileno(), 0x8927,  struct.pack('256s', interface[:15]))
    	return ''.join(['%02x:' % ord(char) for char in info[18:24]])[:-1]		


def set_ip_forwarding(value):
	with open('/proc/sys/net/ipv4/ip_forward', 'w') as file:
		file.write(str(value))
		file.close()
		print "[*] Setting the packet forwarding."
def iptables():
	os.system('iptables -P INPUT ACCEPT && iptables -P FORWARD ACCEPT && iptables -F && iptables -X && iptables -t nat -F && iptables -t nat -X')
	print "[*] Iptables redefined"


def module_check(module):
	confirm = raw_input("[-] Do you checked if your system has [%s] installed?, do you like to try installing? (apt-get install %s will be executed if yes [y/n]: " % (modules,module))
	if confirm == 'y':
		os.system('apt-get install %s' % module)
	else:
		print "[-] Terminated"
		sys.exit(1)

def color(message,color):
	msg = termcolor.colored(str(message), str(color), attrs=["bold"])
	return msg

def jarvis_help(version):
	print
	print color("[ Jarvis - Personal Assistence - v{} ]".format(version),"blue")
	print
	print
	print color("[*] exit |or| quit : 		Terminate the program.","blue")
	print
	print
	print color("[*] sleep |or| stop |or| wait:  	Sleep until you say 'Jarvis'.","blue")
	print
	print
	print color("[*] newspaper |or| news: 		Read the top trending news from reddit.","blue")
	print
	print
	print color("[*] say |or| speak [message]:     Ask Jarvis to say something.","blue")
	print
	print color(" examples(say):","green")
	print
  	print color("  say I like donuts","green")
  	print color("  speak my name is Jarvis","green")
	print
	print
	print color("[*] run [script]:	 		Run .sh script that you place on the scripts folder with chmod +x","blue")
	print
	print color(" example(say):","green")
	print
	print color("  run firewall		 	| Place a firewall.sh on the scripts folder and give execution privilege first.","green")
	print
	print
	print color("[*] browser:		 	Ask Jarvis to start your default browser.","blue")
	print
 	print color(" example(say):","green")
	print
  	print color("  browser","green")
	print
	print
	print color("[*] terminal:		 	Ask Jarvis to open a gnome-terminal.","blue")
	print
 	print color(" example(say):","green")
	print
  	print color("  terminal","green")
	print
	print
	print color("[*] search [query]	 	Ask Jarvis to search query via google.","blue")
	print
	print color(" example(say):","green")
	print
	print color("  search python programming.","green")
	print
	print
 	print color("[*] input [keystroke]:   		Send a command to the Arduino Leonardo without entering editor mode.","blue")
	print
        print color("          * ARDUINO LEONARDO REQUIRED *","red")
	print
	print color("voice commands: (Same as EDITOR MODE )","yellow")
	print
	print
	print color("[*] editor: 			Start the editor mode.","blue")
	print
	print color("          * ARDUINO LEONARDO REQUIRED *","red")
	print
	print color("               [EDITOR MODE]","red")
	print
	print color("voice commands: (anything else will be typed)","yellow")
	print
	print color(" forward   = tab","green")
 	print color(" back      = (shift+tab)","green")
 	print color(" up        = up arrow","green")
	print color(" down      = down arrow","green")
	print color(" right     = right arrow","green")
	print color(" left      = left arrow","green")
	print color(" super     = super/windows","green")
	print color(" slash     = slash(/)","green")
	print color(" backspace = backspace(erase character)","green")
	print color(" erase	  = press backspace 10 times","green")
	print color(" space     = space(spacebar)","green")
	print color(" enter     = enter(return)","green")
	print color(" close	  = close(alt+f4)","green")
	print color(" escape    = escape(esc)","green")
	print color(" exit	  = leaves editor mode","green")
	print



def banner(version):
	banner = """\n

              ---_ ...... _/_ -
             /  .      ./ .'*  '
             |''         /_|-'  '.
            /                     )
          _/                  >   '
        /   .   .       _.-" /  .'
        \           __/"     /.'
          \ '--  .-" /     / /'
           \|  \ | /     / /
                \:     / /
             `\/     / /
              \__`\/ /
                  \_|



[ PytheM - Penetration Testing Framework v{} ]\n
""".format(version)
	return color(banner,"blue")


def print_help():
	print
	print color("[*] help:			Print the help message.","blue")
	print
	print
	print color("[*] exit/quit:		Leave the program.","blue")
	print
	print
	print color("[*] set			Set a variable's value.","blue")
	print
	print color(" parameters:","red")
	print
 	print color("  - interface","yellow")
 	print color("  - gateway","yellow")
 	print color("  - target","yellow")
 	print color("  - file","yellow")
 	print color("  - arpmode","yellow")
	print color("  - domain","yellow")
	print color("  - redirect","yellow")
	print color("  - script","yellow")
	print
	print color(" examples:","green")
	print
   	print color("  pythem> ","red") + "set interface         | open input to set"
	print "     or"
   	print color("  pythem> ","red") + "set interface wlan0   | don't open input to set value."
	print
	print
	print color("[*] print		Print a variable's value.","blue")
	print
  	print color(" examples:","green")
	print
	print color("  pythem> ","red") + "print gateway"
	print
	print
	print color("[SECTION - NETWORK AND MAN-IN-THE-MIDDLE]","grey")
	print
	print
	print color("[*] scan		Make a tcp/manualport/arp scan.","blue")
	print
	print "Should be called after setting an interface and a target"
	print
	print color(" examples:","green")
	print color("  pythem> ","red") + "scan"
	print "     or"
   	print color("  pythem> ","red") + "scan tcp"
	print
	print
	print color("[*] arpspoof		Start or stop an arpspoofing attack.","blue")
	print
	print "Optional setting arpmode to select arpspoofing mode should be filled with rep or req"
	print "rep to spoof responses, req to spoof requests"
	print
	print color(" arguments:","red")
	print
	print color("  start","yellow")
 	print color("  stop","yellow")
	print
  	print color(" examples:","green")
	print
   	print color("  pythem> ","red") + "arpspoof start"
   	print color("  pythem> ","red") + "arspoof stop"
	print
	print
	print color("[*] dnsspoof		Start a dnsspoofing attack.","blue")
	print
	print "Should be called after an arpspoofing attack has been started"
	print
	print color(" arguments:","red")
	print
	print color(" start","yellow")
	print color(" stop","yellow")
	print
	print color(" examples:","green")
	print
   	print color("  pythem> ","red")+ "dnsspoof start"
   	print color("  pythem> ","red") + "dnsspoof stop"
	print
	print
	print color("[*] inject			Start and redirect clients to web server with a script to inject in header field","blue")
	print
	print "Should be used after a arpspoof has been started"
	print
	print color(" arguments:", "red")
	print
	print color(" start","yellow")
	print color(" stop","yellow")
	print
	print color(" examples:","green")
	print
	print color("  pythem> ","red") + "inject start"
	print color("  pythem> ","red") + "inject stop"
	print
	print
	print color("[*] sniff			Start sniffing packets.","blue")
	print
	print "Should be called after setting an interface"
	print
  	print color(" sniff custom filters:","red")
	print
    	print color("  - http","yellow")
    	print color("  - dns","yellow")
	print
  	print color(" examples:","green")
	print
   	print color("  pythem> ","red")+ 'sniff http'
	print "     or"
   	print color("  pythem> ","red")+ 'sniff'
   	print "  [+] Enter the filter: port 1337 and host 10.0.1.5  | tcpdump like format or http, dns specific filter."
	print
	print
	print color("[*] pforensic		Start a packet-analyzer","blue")
	print
	print "Should be called after setting an interface and a file with a .pcap file"
	print
  	print color(" examples:","green")
	print
   	print color("  pythem> ","red") + 'pforensic'
	print
   	print color("  pforensic> ","yellow") + 'help'
	print
	print
	print color("[SECTION - EXPLOIT DEVELOPMENT AND REVERSE ENGINERING]","grey")
	print
	print
	print color("[*] xploit		Interactive stdin or tcp exploit development shell.","blue")
	print
	print "The stdin should be called after setting file"
	print "The tcp should be called after setting target"
	print
	print color(" arguments:","red")
	print color("  stdin		| set file before","yellow")
 	print color("  tcp		| set target before","yellow")
	print
  	print color(" examples:","green")
	print
   	print color("  pythem> ","red") + "set file ./exec"
	print
   	print color("  pythem> ","red") + "xploit stdin"
        print "     or"
   	print color("  pythem> ","red") + "xploit"
   	print "  [*] Select one xploit mode, options = stdin/tcp"
   	print "  [+] Exploit mode: stdin"
	print color("  xploit> ","blue") + "help"
	print
	print
	print color("[SECTION - BRUTE-FORCE]","grey")
	print
	print
	print color("[*] brute		Start a brute-force attack.","blue")
	print
	print "Should be called after setting a target and a wordlist file path"
	print
	print color(" arguments:","red")
	print
	print color("  ssh		| ip address as target","yellow")
	print color("  url		| url (with http:// or https://) as target","yellow")
 	print color("  form		| url (with http:// or https://) as target","yellow")
	print
  	print color(" examples:","green")
	print
   	print color("  pythem> ","red") + "brute webform"
   	print color("  pythem> ","red") + "brute ssh"
	print
	print
	print color("[SECTION - UTILS]","grey")
	print
	print color("[*] geoip		Approximately geolocate the location of a IP address.","blue")
	print
	print "Should be called after setting target(ip address)"
	print
	print color(" examples:","green")
	print
   	print color("  pythem> ","red") + "geoip"
	print "     or"
   	print color("  pythem> ","red") + "geoip 8.8.8.8"
	print
	print
	print color("[*] decode and encode	Decode or encode a string with a chosen pattern.","blue")
	print
	print color(" examples:","green")
	print
	print color("  pythem> ","red") + "decode base64"
   	print color("  pythem> ","red") + "encode ascii"
	print
	print
	print color("[*] cookiedecode	Decode a base64 url encoded cookie value.","blue")
	print
	print color(" example:","green")
	print
	print color("  pythem> ","red") + "cookiedecode"
	print
	print
	print color("* Anything else will be executed in the terminal like cd, ls, nano, cat, etc. *","yellow")
	print
	print
	print color("(+) Call the voice-controlled assistant Jarvis","grey")
	print
	print color("link:","green") + color(" https://github.com/m4n3dw0lf/Jarvis","blue")
	print
	print
	print color("[*] jarvis","blue")
	print
	print "Type 'jarvis help' to see the jarvis help page."
	print
	print color(" examples:","green")
	print
	print color("  pythem> ","red")+ "jarvis	  "+color("(Call Jarvis in speech recognition mode)","yellow")
	print
   	print color("  pythem> ","red")+ "jarvis help     "+color("(Print the Jarvis help message)","yellow")
	print
   	print color("  pythem> ","red")+ "jarvis log      "+color("(Check the Jarvis log)","yellow")
	print "     or"
   	print color("  pythem> ","red")+ "jarvis log err"
	print
   	print color("  pythem> ","red") + "jarvis say     "+color(" (Ask Jarvis to say something)","yellow")
	print "     or"
   	print color("  pythem> ","red") + "jarvis say hello my name is Jarvis."
	print
   	print color("  pythem> ","red") + "jarvis read 	  "+color("(If no file is specified, should be called after setting file.)","yellow")
   	print "     or"
   	print color("  pythem> ","red") + "jarvis read file.txt"
	print
	print color("by: ","red") + color("m4n3dw0lf","blue")
	print
