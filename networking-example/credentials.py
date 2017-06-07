import json

class Credentials:

    def __init__(self, fileName='credentials.json'):

        self.stored_credentials = {}
        self.keysRetrieved = False

        try:
            with open(fileName, 'r') as credentials:
                credentials_as_json = json.loads(credentials.read())
                for key in credentials_as_json:
                    self.stored_credentials[key] = credentials_as_json[key]
            self.keysRetrieved = True
        except Exception as e:
            print(e)

    def retrieveByKey(self, key):
        
        assert self.keysRetrieved, "Credentials file not successfully parsed."
        
        value = False

        try:
            value = self.stored_credentials[key]
        except:
            pass

        assert value, "Given key not found in credentials file."
        return str(value)
