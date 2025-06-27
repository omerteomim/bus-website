import requests
import json
def lambda_handler(event, context):

    BUS_ROUTES=[ 
        {'company':'metropoline', 'route': '236', 'direction': '0','station': '25637', 'from':'רכבת ההגנה'},
        {'company':'metropoline','route': '236', 'direction': '1','station': '21307', 'from':'בית ספר נתיב/דרך ההגנה'},
        {'company':'dan','route': '38', 'direction': '1','station': '21307', 'from':'בית ספר נתיב/דרך ההגנה'},
        {'company':'dan','route': '38', 'direction': '1','station': '26019', 'from':'משה דיין/צבי נשרי'},
        {'company':'dan','route': '38', 'direction': '0','station': '25637', 'from':'רכבת ההגנה'},
        {'company':'metropoline','route': '35', 'direction': '0','station': '21307', 'from':'בית ספר נתיב/דרך ההגנה'},
        {'company':'metropoline','route': '35', 'direction': '1','station': '25637', 'from':'רכבת ההגנה'},
        {'company':'metropoline','route': '13', 'direction': '4','station': '25637', 'from':'רכבת ההגנה'},
        {'company':'kavim','route': '111', 'direction': '1','station': '20353', 'from':'רכבת ההגנה/החרש'},
        {'company':'kavim','route': '111', 'direction': '3','station': '20353', 'from':'רכבת ההגנה/החרש'},
        {'company':'kavim','route': '111', 'direction': '7','station': '20353', 'from':'רכבת ההגנה/החרש'},
        {'company':'kavim','route': '111', 'direction': '11','station': '20353', 'from':'רכבת ההגנה/החרש'} 
        ]
    returnlist = []
    for bus in BUS_ROUTES:
        station_name = bus['station']
        url = f"https://curlbus.app/{bus['company']}/{bus['route']}/{bus['direction']}/"
        response = requests.get(url)
        for row in list(response.text.splitlines()):
            if station_name in row:
                if 'm' not in row and "Now" not in row:
                    continue
                returnlist.append(bus['route']+" " +bus['from']+" "+row[-3:])
                print(bus['route'],bus['from'],end=" ")
                print(row[-3:])
                break
    return {
        "statusCode": 200,
        "headers": { "Access-Control-Allow-Origin": "*", "Content-Type": "application/json" },
        "body": json.dumps(returnlist, ensure_ascii=False)
    }
