# pin_to_hosts_By_SecureCRT

This script is executed from the Secure CRT.

It accesses the main GW router by Telnet and performs pings to different vlans within the network.
The script opens "equipos.txt" file and reads the IP address in the first column of each line, to which the ping is performed.

This script generates a .txt file with the response times.
