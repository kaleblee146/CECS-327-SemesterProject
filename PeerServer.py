import socket

# Peer-Server modified and referenced by - https://realpython.com/python-sockets/
HOST = "127.0.0.1"
PORT = 65432

def receive_image():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((HOST, PORT)) # sets up the server
        s.listen()
        print("Server is listening for connections...") # listens for the connection
        conn, addr = s.accept()
        with conn:
            print(f"Connected by {addr}")
            image_data = b""  # takes in the image data
            while True: # while loop to make sure that it gets all parts of the image
                chunk = conn.recv(4096)  
                if not chunk:
                    break  
                image_data += chunk  
        
            with open('received_image.png', "wb") as f: # after we create the image using the datavisualizer tool, to check if it is actually sent, we send it as a received image
                f.write(image_data)
            print("Image received and saved.")

if __name__ == '__main__':
    receive_image()
