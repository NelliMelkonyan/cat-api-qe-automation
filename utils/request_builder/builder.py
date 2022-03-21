import requests
import json

class Builder():
    """
    The Builder interface specifies methods for creating the different parts of
    the Request.
    """
    __instance = None

    def __init__(self):
        if Builder.__instance != None:
         print("Request object already exists using.")
        else:
          self.headers = {}
          self.params = {}
          self.body = {}
          self.url = ''
          self.method = 'GET'
          Builder.__instance = self


    @staticmethod 
    def useExistingRequest():
      if Builder.__instance == None:
        Builder()
      return Builder.__instance

    @staticmethod 
    def createNewRequest():
      Builder.__instance = None
      Builder()
      return Builder.__instance

    def set_request_params(self, **params):
        self.params = params

    def set_request_method(self, method):
        self.method = method

    def set_request_header(self, **headers):
        self.headers= headers

    def set_request_url(self, url):
        self.url = url

    def set_request_body(self, url):
        self.url = url
    
    def clear_params(self):
        self.params = {}

    def clear_body(self):
        self.body = {}

    def send(self):
      res = {}
      if (self.method.upper() == 'GET'):
        res = requests.get(self.url, params=self.params, headers=self.headers)
      if (self.method.upper() == 'POST'):
        res = requests.post(self.url, params=self.params, headers=self.headers, data=self.body)
      return (res.status_code, json.loads(res.text))
