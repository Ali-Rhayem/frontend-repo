import yaml

class Client:
    def __init__(self, config):
        self.config = config

    def run(self):
        if self.config['ServerIPAddress'] == '127.0.0.1':
            print("Running on localhost")

if __name__ == "__main__":
    with open('config.yaml', 'r') as file:
        config = yaml.safe_load(file)
    client = Client(config)
    client.run()
