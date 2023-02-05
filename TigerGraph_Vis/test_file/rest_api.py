import requests, json
URL = "http://43.201.137.235:9000/graph/Recom/vertices/USER/5"
URL = "http://43.201.137.235:14240/restpp/query/Recom/rest_api_edges?input_user=5"

response = requests.get(URL, headers = {"Authorization" : "Bearer token_id"})
# Bearer뒤에 토큰 아이디 
# print(json.loads(response.text))

data = json.loads(response.text)
print(data.len())