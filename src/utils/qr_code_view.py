import socket
import qrcode
import PySimpleGUI as sg
import threading
import base64
import io
import os
from .logo import logo
import requests


class QRCodeDisplay():
    

    def show(self):
        url_base: str = self.get_url()
        qr: str = self.get_qr(f"{url_base}/champignon")
        thread = threading.Thread(target=self.display, args=(url_base, qr), name=f'Thread QR code')
        thread.start()
    

    def display(self, url_base: str, qr: str):
        sg.theme("DarkBlack1")
        layout = [
            [sg.Text("To access the control either enter the following URL on your browser or read the QR code.", size=(
                40, None), justification="center", font=("Arial", 14), pad=20)],
            [sg.Text(f"{url_base}/champignon", size=(40, None),
                        justification="center", font=("Arial", 15))],
            [sg.Image(qr, expand_x=True, expand_y=True, pad=20)],
        ]
        window = sg.Window(
            'Champignon', layout, icon=logo, element_justification='c')
        while True:
            event, _ = window.read()
            if event in [None, sg.WIN_CLOSED, 'Close']:
                requests.get(f"{url_base}/close")
                break


    def get_url(self) -> str:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        return f"http://{s.getsockname()[0]}:5000"


    def get_qr(self, url: str) -> str:
        img = qrcode.make(url, border=1)
        buffer = io.BytesIO()
        img.save(buffer, format='PNG')
        return base64.b64encode(buffer.getvalue())
