from typing import Tuple, Dict
import socket
from pathlib import Path
from ....utils.logo import logo


class Get():
    

    def handle_request(self) -> Tuple[Dict[str, any], int]:
        path = Path(__file__)
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        with open(f"{path.parent}/page.html", "r", encoding="utf-8") as f:
            html = f.read()
        html = html.replace("##URL##", f"{s.getsockname()[0]}:5000")
        html = html.replace("##ICON##", logo.decode())
        return html
