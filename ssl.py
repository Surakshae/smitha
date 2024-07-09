import socket
import ssl
import os

def open_listener(port):
    sd = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sd.bind(('0.0.0.0', port))
    sd.listen(10)
    return sd

def init_server_ctx():
    ctx = ssl.create_default_context(ssl.Purpose.CLIENT_AUTH)
    ctx.load_cert_chain(certfile="mycert.pem", keyfile="mycert.pem")
    return ctx

def servlet(conn, addr):
    print(f"Connection: {addr[0]}:{addr[1]}")
    conn.settimeout(5)
    try:
        while True:
            data = conn.recv(1024)
            if not data:
                break
            print("Client msg:", data.decode())
            conn.sendall(data)
    except ssl.SSLError as e:
        print("SSL Error:", e)
    except socket.timeout:
        print("Connection timeout")
    finally:
        conn.close()

def main():
    if os.geteuid() != 0:
        print("This program must be run as root/sudo user!!")
        return

    portnum = int(input("Enter port number: "))
    server = open_listener(portnum)
    ctx = init_server_ctx()

    while True:
        conn, addr = server.accept()
        ssl_conn = ctx.wrap_socket(conn, server_side=True)
        servlet(ssl_conn, addr)

    server.close()

if __name__ == "__main__":
    main()
