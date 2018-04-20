import socketserver
import socket
import threading


class ThreadedTCPRequestHandler(socketserver.BaseRequestHandler):

    BUF_SIZE = 1024
    
    def handle(self):
        data = self.request.recv(self.BUF_SIZE)
        self.request.sendall(data)


class ThreadedTCPServer(socketserver.ThreadingMixIn, socketserver.TCPServer):
    pass


def main():

    HOST = ''
    PORT = 50007

    server = ThreadedTCPServer((HOST, PORT), ThreadedTCPRequestHandler)
    ip, port = server.server_address

    # Launch server
    server_thread = threading.Thread(target=server.serve_forever)
    server_thread.daemon = True
    server_thread.start()

    # Shutdown server after entering any chars
    input()
    server.shutdown()


if __name__=='__main__':
    main()
