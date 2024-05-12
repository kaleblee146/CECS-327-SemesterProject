import socket

HOST = "127.0.0.1"
PORT = 65432

def receive_image():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((HOST, PORT))
        s.listen()
        print("Server is listening for connections...")
        conn, addr = s.accept()
        with conn:
            print(f"Connected by {addr}")
            image_data = b""  # Initialize empty byte string to store image data
            while True:
                chunk = conn.recv(4096)  # Receive data in chunks
                if not chunk:
                    break  # If no more data is received, break the loop
                image_data += chunk  # Append received chunk to image data
        
            with open('received_image.png', "wb") as f:
                f.write(image_data)
            print("Image received and saved.")

if __name__ == '__main__':
    receive_image()
