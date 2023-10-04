import socket

# Create a socket object
# svrSkt is short for serverSocket
svrSkt = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# The address that the socket will listen on
socketAddress = ("127.0.0.1", 1234)
svrSkt.bind(socketAddress) #OR svrSkt.bind((&#39;localhost&#39;, 1234))

# Allow for 1 connection
svrSkt.listen(1)

while True:
  # Accept incoming connection
  connectionSocket, address = svrSkt.accept()

  # Display the address of the client
  print(f"Connection from {address} has been established!")

  # Send a message to the client
  connectionSocket.send(bytes("Welcome to the server!", "utf-8"))
    
  # Listen for incoming integers
  data = connectionSocket.recv(1024)

  # Check if the integer that was received is valid
  if len(data) <= 0:
    break
  else:
    # Convert the bytes to an int type
    num = int(data)

    # Print the original integer
    print("Original integer: ", num)

    # Calculate the int to the 9th power
    newNum = pow(num, 9)

    # Convert back to a string to send back to the client
    dataToSend = str(newNum)

    # Convert the string back to bytes and send to the client
    connectionSocket.send(bytes(dataToSend, "utf-8"))

    print("Calculated integer: ", newNum)
    
connectionSocket.close()
