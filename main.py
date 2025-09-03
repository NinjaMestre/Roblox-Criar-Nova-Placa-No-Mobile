import requests

universe_id = 0
cookie = ""
api_key = ""

csrf_request = request = requests.post(f"https://apis.roblox.com/universes/v1/user/universes/{universe_id}/places", headers={
    "x-api-key": api_key,
    "Content-Type": "application/json"
}, json={
    "templatePlaceId": 95206881
}, cookies={
    ".ROBLOSECURITY": cookie
})

print(csrf_request.status_code, csrf_request.text, csrf_request.headers)

csrf_token = csrf_request.headers["x-csrf-token"]

print(csrf_token)

request = requests.post(f"https://apis.roblox.com/universes/v1/user/universes/{universe_id}/places", headers={
    "x-api-key": api_key,
    "x-csrf-token": csrf_token,
    "Content-Type": "application/json"
}, json={
    "templatePlaceId": 95206881
}, cookies={
    ".ROBLOSECURITY": cookie
})

print(request.status_code, request.text, request.headers)