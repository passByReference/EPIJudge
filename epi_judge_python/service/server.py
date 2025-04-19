import socket
import threading
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime

class SimpleWebServer:
    def __init__(self, host='0.0.0.0', port=8080, max_threads=10):
        self.host = host
        self.port = port
        self.max_threads = max_threads
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.thread_pool = ThreadPoolExecutor(max_workers=max_threads)
        self.running = False

    def handle_client(self, client_socket, client_address):
        """Handle a single client connection"""
        try:
            request = client_socket.recv(1024).decode('utf-8')
            thread_name = threading.current_thread().name
            print(f"\nHandling request on thread: {thread_name}")
            
            # Add artificial delay to see concurrent processing
            import time
            time.sleep(3)  # Sleep for 3 seconds to simulate work
            
            response = self.generate_http_response()
            client_socket.sendall(response.encode('utf-8'))
            print(f"Completed request on thread: {thread_name}")
        except Exception as e:
            print(f"Error handling client {client_address}: {e}")
        finally:
            client_socket.close()

    def generate_http_response(self):
        """Generate a simple HTTP response"""
        response_body = f"""
        <html>
            <head><title>Python Web Server</title></head>
            <body>
                <h1>Welcome to Python Web Server</h1>
                <p>Current time: {datetime.now()}</p>
                <p>Thread: {threading.current_thread().name}</p>
            </body>
        </html>
        """
        
        response = (
            "HTTP/1.1 200 OK\r\n"
            "Content-Type: text/html\r\n"
            f"Content-Length: {len(response_body)}\r\n"
            "Connection: close\r\n"
            "\r\n"
            f"{response_body}"
        )
        return response

    def start(self):
        """Start the web server"""
        self.server_socket.bind((self.host, self.port))
        self.server_socket.listen(5)
        self.running = True
        print(f"Server started on {self.host}:{self.port} with {self.max_threads} threads")

        try:
            while self.running:
                # Accept a new connection
                client_socket, client_address = self.server_socket.accept()
                print(f"Accepted connection from {client_address}")
                
                # Submit the client handling to the thread pool
                self.thread_pool.submit(self.handle_client, client_socket, client_address)
        except KeyboardInterrupt:
            print("Server shutting down...")
        finally:
            self.stop()

    def stop(self):
        """Stop the web server"""
        self.running = False
        self.thread_pool.shutdown(wait=True)
        self.server_socket.close()
        print("Server stopped")

if __name__ == "__main__":
    server = SimpleWebServer(max_threads=3)
    server.start()