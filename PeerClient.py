import socket
HOST = "127.0.0.1"
PORT = 65432

def send_image(image_path):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))
        with open(image_path, "rb") as f:
            while True:
                image_data = f.read(4096)  # Read 4096 bytes at a time
                if not image_data:
                    break  # If no more data left to read, break the loop
                s.sendall(image_data)
        print("Image sent successfully.")

if __name__ == '__main__':
    image_path = input("Enter the image file name and format: -> ")
    send_image(image_path)