import hashlib

from fastapi import FastAPI, Request


app = FastAPI()


def filter_request_scope_headers(scope_headers: list) -> dict:
    filtered_request_scope = {}
    for element in scope_headers:
        filtered_request_scope[element[0].decode()] = element[1].decode()
    return filtered_request_scope


@app.get("/")
async def root(request: Request):
    filtered_request_scope_headers = filter_request_scope_headers(
        request.scope['headers'].copy()
    )
    filtered_request_scope = {
        'headers': filtered_request_scope_headers,
    }
    filtered_request_scope.update({'client_ip': request.scope['client'][0]})
    string_to_be_hashed = filtered_request_scope['client_ip'] \
        + filtered_request_scope['headers']['user-agent']

    visitor_id = hashlib.md5(string_to_be_hashed.encode())

    result = {
        'visitorId': visitor_id.hexdigest(),
        'filteredRequestScope': filtered_request_scope,
    }
    return result
