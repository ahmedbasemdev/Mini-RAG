from helpers.config import get_settings
import os
import random
import string

class BaseController:
    def __init__(self):

        self.settings = get_settings()
        print("Current dir", os.path.dirname(__file__))
        print("base dir", os.path.dirname(os.path.dirname(__file__)))
        self.base_dir = os.path.dirname(os.path.dirname(__file__))
        self.files_dir = os.path.join(self.base_dir, "assests", "files")
    
    def generate_random_string(self, length: int = 12) -> str:
        return ''.join(random.choices(string.ascii_lowercase + string.digits, k=length))
