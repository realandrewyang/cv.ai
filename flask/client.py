import requests
# res = requests.post('http://localhost:5000/post', json={"data":["hello world", "bye world"]})
res = requests.post('http://35.188.88.169/post', json={"data":["hello world", "bye world"]})
if res.ok:
    print(res.json())
    print('done')