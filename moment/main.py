from sanic import Sanic
from sanic.response import json as response_json
import aiohttp
import json

from moment.gitlab_message_dict import get_dingtalk_data

app = Sanic(__name__)

async def post(url, json_data):
    headers = {
        "Content-Type": "application/json"
    }
    conn = aiohttp.TCPConnector(verify_ssl=False)
    async with aiohttp.ClientSession(connector=conn, headers=headers) as session:
        async with session.post(url, data=json.dumps(json_data)) as resp:
            return await resp.json()


@app.post("/gitlab")
async def test(request):
    access_token = request.args.get('access_token')
    request_data = request.json
    print(f'request: {request.body.decode()}')
    url = f'https://oapi.dingtalk.com/robot/send?access_token={access_token}'
    data = get_dingtalk_data(request_data)

    response = await post(url, data)
    print(f'{url}: {response}')
    return response_json(request.json)
