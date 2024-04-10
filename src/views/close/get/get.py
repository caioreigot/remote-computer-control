from typing import Tuple, Dict
from flask import jsonify
import os, signal


class Get():
    

    def handle_request(self) -> Tuple[Dict[str, any], int]:
        os.kill(os.getpid(), signal.SIGINT)
        return jsonify({ "success": True, "message": "Server is shutting down..." })
