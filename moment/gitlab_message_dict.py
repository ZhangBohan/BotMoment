

def get_dingtalk_data(request_json):
    if request_json['object_kind'] == 'push':
        commit = request_json['commits'][0]
        data = {
            "msgtype": "link",
            "link": {
                "title": f"{request_json['user_name']} 推送了{len(request_json['commits'])}个提交。",
                "text": commit['message'],
                "picUrl": request_json['user_avatar'],
                "messageUrl": commit['url']
            }
        }

    return data
