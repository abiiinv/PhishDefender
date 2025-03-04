import http.server
import socketserver
import subprocess
import os

PORT = 8000
DIRECTORY = "d:/phish"

class MyHandler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=DIRECTORY, **kwargs)

    def do_GET(self):
        if self.path == '/send_and_redirect':
            # Run the send_emails.py script (Keep this part)
            try:
                result = subprocess.run(['python3', 'send_emails.py'], capture_output=True, text=True, check=True)
                print("send_emails.py output:", result.stdout)
                if result.stderr:
                    print("send_emails.py errors:", result.stderr)
            except subprocess.CalledProcessError as e:
                print("Error running send_emails.py:", e)
                self.send_error(500, "Failed to send emails")
                return

            # Serve mailhog_interface.html directly (Modified part)
            with open(os.path.join(DIRECTORY, 'mailhog_interface.html'), 'r') as f:
                content = f.read()
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.wfile.write(content.encode())

        elif self.path == '/':
            # Serve mailhog_interface.html on the root path as well
            with open(os.path.join(DIRECTORY, 'mailhog_interface.html'), 'r') as f:
                content = f.read()
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.wfile.write(content.encode())
        else:
            super().do_GET()

with socketserver.TCPServer(("", PORT), MyHandler) as httpd:
    print(f"Serving at port {PORT}")
    httpd.serve_forever()
