from socket import *


def smtp_client(port=1025, mailserver='127.0.0.1'):
    msg = "\r\n My message"
    endmsg = "\r\n.\r\n"

    # Choose a mail server (e.g. Google mail server) if you want to verify the script beyond GradeScope

    # Create socket called clientSocket and establish a TCP connection with mailserver and port

    clientSocket: socket.SocketType = socket(AF_INET,SOCK_STREAM)
    clientSocket.connect( (mailserver, port))

    recv = clientSocket.recv(1024).decode()

    # Send HELO command and print server response.
    heloCommand = 'HELO Alice\r\n'
    clientSocket.send(heloCommand.encode())
    validateResponse(clientSocket)

    # Send MAIL FROM command and handle server response.
    mailFrom = "MAIL FROM: <any@gmail.com> \r\n"
    clientSocket.send(mailFrom.encode())
    validateResponse(clientSocket)

    # Send RCPT TO command and handle server response.
    rcptTo = "RCPT TO: <dest@gmail.com> \r\n"
    clientSocket.send(rcptTo.encode())
    validateResponse(clientSocket)

    # Send DATA command and handle server response.
    data = "DATA\r\n"
    clientSocket.send(data.encode())
    validateResponse(clientSocket)

    # Send message data.
    subj = "Subject: SMTP Client LAB \r\n\r\n"
    clientSocket.send(subj.encode())
    clientSocket.send(msg.encode())

    # Message ends with a single period, send message end and handle server response.
    clientSocket.send(endmsg.encode())
    validateResponse(clientSocket)

    # Send QUIT command and handle server response.
    clientSocket.send("QUIT\r\n".encode())
    validateResponse(clientSocket)

    clientSocket.close()

def validateResponse(clientSocket: socket):
    resp = clientSocket.recv(1024).decode()
    if resp[:3] != '250':
        print('250 reply not received from server.')

if __name__ == '__main__':
    smtp_client(1025, '127.0.0.1')