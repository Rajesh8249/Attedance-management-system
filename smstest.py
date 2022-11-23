import requests

url = "https://www.fast2sms.com/dev/bulkV2"

querystring = {"authorization":"G2Ar0mNkVSLjctuRZxDIoyzYXJ5TpQ3v9EqF8dBa76sMw4PCgWhC0NbGVwrHd2SiIM9WeqkPJnc3YBOD","variables_values":"Hi Rajesh","route":"otp","numbers":"8249154144"}

headers = {
    'cache-control': "no-cache"
}

response = requests.request("GET", url, headers=headers, params=querystring)

print(response.text)

