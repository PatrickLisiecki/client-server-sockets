import socket

# Create a socket object
# cltSkt short for clientSocket
cltSkt = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# The address that the client will connect to
socketAddress = ("127.0.0.1", 1234) # ip address and port number
cltSkt.connect(socketAddress)

# Receive the message from the server
msg = cltSkt.recv(1024) # buffer size 1024 bytes

# Display the decoded message
print(msg.decode("utf-8"))

while True:
  # Prompt user to enter a sentence
  sentence = input("Input a lowercase sentence: ")

  # Send the sentence to the server
  cltSkt.send(bytes(sentence, "utf-8"))

  # Decode and display the received message from the server
  msgRecvd = cltSkt.recv(1024)
  print("From Server: ", msgRecvd.decode("utf-8"))
  cltSkt.close()