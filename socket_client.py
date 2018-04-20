import socket
import struct
import time


HOST = 'localhost'
PORT = 50007
TIMEOUT = 1
BUF_SIZE = 1024


def main():

    print('Ping host {0}:{1}\n{2}'.format(HOST, PORT, '-'*25))
    seq_num = 1

    while True:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            
            # Create a packed data
            current_time = time.time()
            pdata = struct.pack('!Hd', seq_num, current_time)

            # Send ping, receive pong, close connection
            s.connect((HOST, PORT))
            s.sendall(pdata)
            rdata = s.recv(BUF_SIZE)
            s.close()

            # Print seq_num and time_diff
            rseq_num, rtime = struct.unpack('!Hd', rdata)
            current_time = time.time()
            time_diff = current_time - rtime
            print('{0}. {1}'.format(rseq_num, time_diff))
            seq_num += 1

            # Sleep before the next ping
            time.sleep(TIMEOUT)


if __name__=='__main__':
    main()
