import json

class Environment:
    env = {}

    def __init__(self) -> None:
        try:
            with open('../env.json') as f:
                env = json.load(f)
                for key, val in env.items():
                    self.env[key] = val
        except:
            raise Exception
    