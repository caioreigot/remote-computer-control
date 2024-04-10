from typing import Tuple, Dict
import os, signal


class Get():
    

    def handle_request(self) -> Tuple[Dict[str, any], int]:
        os.kill(os.getpid(), signal.SIGINT)
