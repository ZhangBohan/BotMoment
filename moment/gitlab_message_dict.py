import json


def get_dingtalk_data(request_json):
    print(f"type: {request_json['object_kind']}")

    if request_json['object_kind'] == 'push':
        project = request_json['project']

        text = f"{request_json['user_name']} 推送了{request_json['total_commits_count']}个提交。"

        for commit in request_json['commits']:
            text += f"\n\n> [{commit['message']}]({commit['url']})"

        text += f"\n\n[@{project['name']}]({project['web_url']})"

        data = {
            "msgtype": "markdown",
            "markdown": {
                "title": "xxx",
                "text": text
            }
        }
    elif request_json['object_kind'] == 'note':

        title = request_json['object_attributes']['note']

        user = request_json['user']
        project = request_json['project']
        issue = request_json.get('issue')
        assignee = request_json.get('assignee', {}).get('name', '')

        data = {
            "msgtype": "markdown",
            "markdown": {
                "title": "xxx",
                "text": f"""{user['name']}：**{title}**
>  [{issue['title']}]({request_json['object_attributes']['url']})
> {issue['description']}

> ----

> ######  [@{project['name']}]({project['web_url']}) Assignee: **{assignee}** State: {issue['state']}"""
            }
        }
    elif request_json['object_kind'] == 'issue':
        user = request_json['user']
        project = request_json['project']
        issue = request_json.get('issue', {})
        assignee = request_json.get('assignee', {}).get('name', '')

        if request_json['object_attributes']['action'] == 'open':
            title = f"{request_json['user']['name']} 打开了一个新问题"
            state = 'open'
            title = request_json['object_attributes']['title']
        else:
            title = f"{request_json['user']['name']} 更新了问题"
            state = issue['state']
            title = issue['title']

        text = f"""{user['name']}：**{title}**
>  [{title}]({request_json['object_attributes']['url']})
> {issue.get('description')}

> ----

> ######  [@{project['name']}]({project['web_url']}) Assignee: **{assignee}** State: {state}"""

        data = {
            "msgtype": "markdown",
            "markdown": {
                "title": "xxx",
                "text": text
            }
        }

    else:
        print(json.dumps(request_json, ensure_ascii=False, indent=4))

    return data
