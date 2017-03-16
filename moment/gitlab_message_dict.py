

def get_dingtalk_data(request_json):
    print(f"type: {request_json['object_kind']}")

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
    elif request_json['object_kind'] == 'note':
        data = {
            "msgtype": "link",
            "link": {
                "title": f"{request_json['user']['name']} 评论了{request_json['project']['name']}",
                "text": request_json['object_attributes']['note'],
                "picUrl": request_json['user']['avatar_url'],
                "messageUrl": request_json['object_attributes']['url']
            }
        }
    elif request_json['object_kind'] == 'issue' and request_json['object_attributes']['action'] == 'open':
        data = {
            "msgtype": "link",
            "link": {
                "title": f"{request_json['user']['name']} 打开了一个新的问题",
                "text": request_json['object_attributes']['title'],
                "picUrl": request_json['user']['avatar_url'],
                "messageUrl": request_json['object_attributes']['url']
            }
        }
    elif request_json['object_kind'] == 'issue':
        data = {
            "msgtype": "link",
            "link": {
                "title": f"{request_json['user']['name']} 更新了问题",
                "text": request_json['object_attributes']['title'],
                "picUrl": request_json['user']['avatar_url'],
                "messageUrl": request_json['object_attributes']['url']
            }
        }

    return data
