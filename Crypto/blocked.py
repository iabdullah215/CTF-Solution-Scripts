import socket
import time

# Define the host and port
HOST = 'ctf-pcc.nccs.pk'
PORT = 12345

def connect_to_server():
    """Establish a connection to the server."""
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((HOST, PORT))
    return s

def send_data(sock, data):
    """Send data to the server and return the response."""
    sock.sendall(data.encode('utf-8') + b'\n')
    time.sleep(0.5)  # Wait for the server to respond
    response = sock.recv(4096).decode('utf-8')
    return response

def encrypt_and_get_ciphertext(plaintext):
    """Encrypt a plaintext and get the ciphertext."""
    sock = connect_to_server()
    response = send_data(sock, plaintext)
    sock.close()
    # Extract the ciphertext from response
    lines = response.strip().split("\n")
    return lines[-1]  # Adjust this based on the response format

def main():
    # Step 1: Encrypt "PC"
    print("Sending 'PC'...")
    pc_ciphertext = encrypt_and_get_ciphertext("PC")
    print(f"Ciphertext for 'PC': {pc_ciphertext}")

    # Step 2: Encrypt "C"
    print("Sending 'C'...")
    c_ciphertext = encrypt_and_get_ciphertext("C")
    print(f"Ciphertext for 'C': {c_ciphertext}")

    # Combine them manually
    combined_ciphertext = pc_ciphertext + c_ciphertext
    print(f"Combined Ciphertext: {combined_ciphertext}")

if _name_ == "__main__":
    main()
