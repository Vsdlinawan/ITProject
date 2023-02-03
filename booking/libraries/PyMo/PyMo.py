import pymongo

class PyMo:
    def __init__(self, credentials):
        """
        Description: Sets up mongoDB\n
        `credentials: dict` - credentials dictionary containing (user, password, clusterAddress)
        """

        self.credentials = credentials
        
        print(credentials)

        # Check if credentials.json has the keys "user" and "pass"
        self.__validate_credentials();

        # Try to connect to mongoDB
        self.mongoClient = pymongo.MongoClient(f"mongodb+srv://{self.credentials['user']}:{self.credentials['password']}@{self.credentials['clusterAddress']}/?retryWrites=true&w=majority")
        #self.mongoClient = pymongo.MongoClient("mongodb+srv://watermelon:ThisIsWatermelon073@cluster0.vrjatpa.mongodb.net/?retryWrites=true&w=majority")
        pass

    def getDB(self, dbName):
        return self.mongoClient[dbName]

    # Private Methods
    def __validate_credentials(self):
        """
        Description: Validates user mongoDB credentials by checking if JSON has the required keys (user, password, clusterAddress)
        """
        keys_list = []
        if not 'user' in self.credentials:
            keys_list.append("user")
        if not 'password' in self.credentials:
            keys_list.append("password")
        if not 'clusterAddress'in self.credentials:
            keys_list.append("clusterAddress")

        keys_str = ", ".join(keys_list)

        if len(keys_list) != 0:
            raise Exception(f"Invalid credentials missing key/s: {keys_str}")
