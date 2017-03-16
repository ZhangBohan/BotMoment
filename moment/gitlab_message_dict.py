

def get_dingtalk_data(request_json):
    if request_json['object_kind'] == 'push':
        print(f"type: {request_json['object_kind']}")
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
    elif request_json['object_kind'] == 'note':
        print(f"type: {request_json['object_kind']}")
        data = {
            "msgtype": "link",
            "link": {
                "title": f"{request_json['user']['name']} 评论了{request_json['project']['name']}",
                "text": request_json['object_attributes']['note'],
                "picUrl": request_json['user']['avatar_url'],
                "messageUrl": request_json['object_attributes']['url']
            }
        }

    return data
