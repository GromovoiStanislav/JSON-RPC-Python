import requests
from jsonrpcclient import request, parse, Ok
import logging


def send_json_rpc_request(url, method, params):
    payload = {
        "jsonrpc": "2.0",
        "method": method,
        "params": params,
        "id": 1
    }
    response = requests.post(url, json=payload)
    return response.json()


server_url = "http://localhost:3000"

result = send_json_rpc_request(server_url, "add", {"a": 5, "b": 3})
if "error" in result:
    print("Ошибка:", result["error"])
else:
    print("Результат:", result["result"])


response = requests.post(server_url, json=request("ping"))
parsed = parse(response.json())
if isinstance(parsed, Ok):
    print("Result:",parsed.result,"Id:",parsed.id)
else:
    logging.error(parsed.message)


response = requests.post(server_url, json=request("add", params={"a": 10, "b": 4}, id="foo"))
parsed = parse(response.json())
if isinstance(parsed, Ok):
    print("Result:",parsed.result,"Id:",parsed.id)


else:
    logging.error(parsed.message)
