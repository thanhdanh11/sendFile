import socket

ip = socket.gethostbyname(socket.gethostname())
port = 51000
address = (ip, port)
size = 1024
format = "utf-8"

def main():
    #bat dau ket noi voi tcp socket
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    #ket noi toi server
    client.connect(address)

    #mo va doc file
    file = open("data/yt.txt", "r")
    data = file.read()

    #gui ten file den server
    client.send("yt.txt".encode(format))
    msg = client.recv(size).decode(format)
    print(f"{msg}")

    #gui file du lieu toi server
    client.send(data.encode(format))
    msg = client.recv(size).decode(format)
    print(f"{msg}")

    #dong file
    file.close()

    #dong ket noi toi server
    client.close()

if __name__ == "__main__":
    main()