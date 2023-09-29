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
    
  # Listen for incoming sentences
  sentence = connectionSocket.recv(1024)

  # Check if a sentence was received
  if len(sentence) <= 0:
    break
  else:
    # Print the original sentence
    print(sentence)

    # Send and print the capitalized sentece
    capitalizedSentence = sentence.upper()
    connectionSocket.send(capitalizedSentence)
    print(capitalizedSentence)
    connectionSocket.close()
