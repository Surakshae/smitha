import socket
import ssl

def open_connection(hostname, port):
    sd = socket.create_connection((hostname, port))
    return ssl.wrap_socket(sd, ssl_version=ssl.PROTOCOL_TLS)

def main():
    hostname = input("Enter server hostname: ")
    portnum = int(input("Enter server port number: "))

    try:
        ssl_conn = open_connection(hostname, portnum)
        print("Connected with", ssl_conn.cipher())
        msg = b"Hello???"
        ssl_conn.sendall(msg)
        data = ssl_conn.recv(1024)
        print("Received:", data.decode())
    except ssl.SSLError as e:
        print("SSL Error:", e)
    finally:
        ssl_conn.close()

if __name__ == "__main__":
    main()
