import telnetlib
import time

TELNET_PORT = 23
TELNET_TIMEOUT = 6

def main():
    ip_addr = '50.76.53.27'
    username = 'pyclass'
    password = '88newclass'

    remote_conn = telnetlib.Telnet(ip_addr, TELNET_PORT, TELNET_TIMEOUT)
    output = remote_conn.read_until("sername:", TELNET_TIMEOUT)
    print output
    remote_conn.write(username + '\n')
    output = remote_conn.read_until("assword:", TELNET_TIMEOUT)
    remote_conn.write(password + '\n')
    print output
    time.sleep(1)
    output = remote_conn.read_very_eager()
    print output
    remote_conn.write('show ip int brief' + '\n')
    time.sleep(1)
    output = remote_conn.read_very_eager()
    print output

    remote_conn.close()
    
if __name__ == "__main__":
    main()
