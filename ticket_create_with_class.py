import requests
import json

class Incident:
    api_url="https://dev49357.service-now.com/api/now/table/incident"
    
    headers={"Accept":"appliction/json","content-type":"appliction/json"}
    
    descrip={"description":"money deducted","short_desription":"ticket creation testing from service now api"}


    def __init__(self,user,powd):
        self.user=user
        self.powd=powd
        
    def note(self):
        response=requests.post(self.api_url,auth=(self.user,self.password),headers=self.headers,data=json.dumps(self.descrip))
        print(response.json())
    
obj=Incident("admin","9t@q5ApTYn^K")
obj.note()

'''import requests
import json

api_url = "https://dev85426.service-now.com/api/now/table/incident"
body={   "caller_id": "Vijay Bhaskar",
    "description": "money deducted",
    "short_description": "ticket creation testing from postman"
    }
headers={"accept": "application/json","content-type": "application/json"}
response = requests.post(api_url,headers=headers,data=json.dumps(body),
auth=("admin","FGf6L*8P$lxt"))
print(response.json())'''