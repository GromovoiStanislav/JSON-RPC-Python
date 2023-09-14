from jsonrpclib import Server


client = Server("http://localhost:3000")


result = client.add(5, 3)

print("Результат сложения:", result)