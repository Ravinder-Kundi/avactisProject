import configparser

config = configparser.RawConfigParser()
config.read(".//Configuration//config.ini")

class ReadConfig():
    @staticmethod
    def getApplicationURL():
        url = config.get('common info', 'baseURL')
        return url

    @staticmethod
    def getUserEmail():
        useremail = config.get('common info','adminEmail')
        return useremail

    @staticmethod
    def getPassword():
        password = config.get('common info', 'Password')
        return password

    @staticmethod
    def getPageTitle():
        Homepage_title = config.get('common info','Home_Page_Title')
        return Homepage_title

    @staticmethod
    def getStoreUrl():
        url = config.get('common info', 'store_baseURL')
        return url

    @staticmethod
    def getStoreTitle():
        title = config.get('common info', 'store_Title')
        return title

