import yaml
import os

class Client:
    def __init__(self, config):
        self.config = config

    def run(self):
        if self.config['ServerIPAddress'] == '127.0.0.1':
            print("Running on localhost")
        else:
            print("error: Not running on localhost")
if __name__ == "__main__":
    config_path = os.path.join(os.path.dirname(__file__), '../config.yaml')
    with open(config_path, 'r') as file:
        config = yaml.safe_load(file)
    client = Client(config)
    client.run()
