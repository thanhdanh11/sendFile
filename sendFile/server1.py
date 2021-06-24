import socket

ip = socket.gethostbyname(socket.gethostname())
port = 51000
address = (ip, port)
size = 1024
format = "utf-8"

def main():
    #bat dau 1 tcp socket
    print("Servering is starting...")
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    #bind ip va port toi server
    server.bind(address)

    #server cho client ket noi toi
    server.listen()
    print("Server is listening...")

    while True:
        #server chap nhan ket noi tu client
        conn, addr = server.accept()
        print(f"{addr} connected.")

        #nhan filename tu client
        fileName = conn.recv(size).decode(format)
        print(f"Receiving the filename.")
        file = open(fileName, "w")
        conn.send("Filename received.".encode(format))

        #nhan file du lieu client
        data = conn.recv(size).decode(format)
        print(f"Receiving the file data.")
        file.write(data)
        conn.send("File data received.".encode(format))

        #dong file
        file.close()

        #dong ket noi
        conn.close()
        print(f"{addr} disconnected")

if __name__ == "__main__":
    main()