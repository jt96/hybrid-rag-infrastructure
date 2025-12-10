import hashlib
import json
import os

class StateManager:
    def __init__(self, state_file="state.json"):
        self.state_file = state_file
        self.state = self._load_state()
        
    def _load_state(self):
        try:
            if os.path.exists(self.state_file) and os.path.isfile(self.state_file):
                if os.path.getsize(self.state_file) == 0:
                    return {}
                with open(self.state_file, "r") as f:
                    return json.load(f)
            else:
                return {}
        except Exception as e:
            print(f"Something went wrong: {e}")
            return {}
    
    def is_processed(self, file_hash):
        return file_hash in self.state
    
    def add_processed(self, file_hash, filename):
        self.state[file_hash] = filename
        with open(self.state_file, "w") as json_file:
            json.dump(self.state, json_file, indent=4)
        

def compute_file_hash(input_file_path, algo="sha256", chunk_size=4096):
    hasher = hashlib.new(algo)
    
    with open(input_file_path, "rb") as f:
        while chunk := f.read(chunk_size):
            hasher.update(chunk)
    
    return hasher.hexdigest()

def main():
    test_file_path = "./data/test.txt"
    hashed_file = compute_file_hash(test_file_path,"sha256",4096)
    print(hashed_file)

if __name__ == "__main__":
    main()