from http.server import BaseHTTPRequestHandler, HTTPServer
import cv2
import numpy as np
import json
from urllib.parse import parse_qs

class RequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/':
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            with open('index.html', 'r') as file:
                self.wfile.write(file.read().encode('utf-8'))

    def do_POST(self):
        if self.path == '/upload':
            content_length = int(self.headers['Content-Length'])
            post_data = self.rfile.read(content_length)

            file_data = post_data.split(b'\r\n\r\n')[-1]
            npimg = np.frombuffer(file_data, np.uint8)
            img = cv2.imdecode(npimg, cv2.IMREAD_COLOR)
            
            gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            face_cascade = cv2.CascadeClassifier('Haarcascade_frontalface_default.xml')
            stop_cascade = cv2.CascadeClassifier('stop_data.xml')

            faces_rect = face_cascade.detectMultiScale(gray_img, 1.1, 9)
            stop_signs = stop_cascade.detectMultiScale(gray_img, minSize=(20, 20))

            for (x, y, w, h) in faces_rect:
                cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 2)

            for (x, y, width, height) in stop_signs:
                cv2.rectangle(img, (x, y), (x + height, y + width), (0, 255, 0), 5)

            output_path = '/path/to/save/processed_image.jpg'
            cv2.imwrite(output_path, img)

            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            result = {'message': 'Image processed successfully', 'path': output_path}
            self.wfile.write(json.dumps(result).encode('utf-8'))

def run(server_class=HTTPServer, handler_class=RequestHandler, port=5000):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print(f'Starting server on port {port}')
    httpd.serve_forever()

if __name__ == '__main__':
    run()
