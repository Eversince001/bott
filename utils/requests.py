import requests


def req(question):
    body = {'question':question, 'token': 'DE637C4783C00E7BE0530718000A6688'}
    header = {'Accept': 'application/json','Content-Type': 'application/json'}
    r = requests.get("http://217.71.129.139:4820/getAnswer", json=body, headers=header)

    return  r.json()
