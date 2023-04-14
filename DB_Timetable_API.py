import json
import os
import requests
import xmltodict


def DB_delay():
    evaNo = os.environ.get("EVANO")
    url = f"https://apis.deutschebahn.com/db-api-marketplace/apis/timetables/v1/rchg/{evaNo}"

    payload = {}
    headers = {
        'DB-Client-Id': os.environ.get("DBCLIENTID"),
        'DB-API-Key': os.environ.get("DBAPIKEY"),
        'Cookie': 'AWSALB=YEF7LQQ4RwiV8dDqEm4WcZnWtwR0/pDWFaFwdVfR3m96sFDdhuz5x/MDftHZwtP8m80Cl24cuG'
                  '/t7fG2UHKJupfKG4qnpRX11Tr7qdJGp1da7FP4ZjKWzJgWNOA8; '
                  'AWSALBCORS=YEF7LQQ4RwiV8dDqEm4WcZnWtwR0/pDWFaFwdVfR3m96sFDdhuz5x/MDftHZwtP8m80Cl24cuG'
                  '/t7fG2UHKJupfKG4qnpRX11Tr7qdJGp1da7FP4ZjKWzJgWNOA8; '
                  'TS0197a5e9=01d513bcd14ca307c0096240e91e689d5790a9b80d1f43ee3d99d3a0ce36a075da5fada6bc82f4f048f574c1c4f53e08d2946319de'
    }

    response = requests.request("GET", url, headers=headers, data=payload)
    r = json.loads(json.dumps(xmltodict.parse(response.text)))
    with open('data.json', 'w') as f:
        f.write(str(r).replace("'", '"'))
    print(r)
