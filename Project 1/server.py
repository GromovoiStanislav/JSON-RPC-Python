from jsonrpcserver import method, serve, Success, Result, dispatch, Error, InvalidParams


@method(name="ping")
def ping_444() -> Result:
    return Success("pong")






@method
def hello(name: str) -> Result:
    return Success("Hello " + name)


@method
def greet(greeting: str, name: str):
    return Success(greeting + " " + name)


@method
def greet_context(context, name):
    return Success(context + " " + name)


@method
def add(a, b):
    return Success(a + b)


@method
def test() -> Result:
    return Error(1, "There was a problem")


@method
def within_range(num: int) -> Result:
    if num not in range(1, 5):
        return InvalidParams("Value must be 1-5")
    return Success(num)


print(dispatch('{"jsonrpc": "2.0", "method": "ping", "id": 1}'))

print(dispatch('{"jsonrpc": "2.0", "method": "hello", "params": ["Beau"], "id": 1}'))
print(dispatch('{"jsonrpc": "2.0", "method": "hello", "params": {"name":"Tom"}, "id": 1}'))

print(dispatch('{"jsonrpc": "2.0", "method": "greet", "params": ["Hi","Beau"], "id": 1}'))
print(dispatch('{"jsonrpc": "2.0", "method": "greet", "params": {"greeting":"Hi","name":"Tom"}, "id": 1}'))


print(dispatch('{"jsonrpc": "2.0", "method": "add", "params": [4,7], "id": 1}'))
print(dispatch('{"jsonrpc": "2.0", "method": "add", "params": {"a": 5, "b": 3}, "id": 1}'))

print(dispatch('{"jsonrpc": "2.0", "method": "greet_context", "params": ["Beau"], "id": 1}', context="Hello"))

print(dispatch('{"jsonrpc": "2.0", "method": "test", "id": 1}'))
print(dispatch('{"jsonrpc": "2.0", "method": "within_range","params": [4], "id": 1}'))
print(dispatch('{"jsonrpc": "2.0", "method": "within_range","params": [8], "id": 1}'))

if __name__ == "__main__":
    serve(port=3000,name="localhost")
