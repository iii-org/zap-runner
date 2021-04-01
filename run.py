import json
import os
import re
import subprocess

import requests


def run():
    print('Logging into nexus...')
    token = login()
    print('Mention nexus test starting...')
    res = api_post('/zap', {
        'project_name': os.getenv('PROJECT_NAME'),
        'branch': os.getenv('GIT_BRANCH'),
        'commit_id': os.getenv('GIT_COMMIT_ID')
    }, token)
    test_id = res.json()['data']['test_id']
    print(f'test_id={test_id}, start testing.')
    report = subprocess.run(f'python zap-full-scan.py -t {os.getenv("TARGET_URL")}',
                            stdout=subprocess.PIPE).stdout.decode('utf-8').strip()
    lines = report.splitlines()
    index = -1
    last_line = ''
    while last_line == '':
        last_line = lines[index]
        index -= 1
    stats = re.findall(': (\\d+)', last_line)
    result = {
        'fail': int(stats[0]) + int(stats[1]),
        'warning': int(stats[2]) + int(stats[3]),
        'info': int(stats[4]),
        'ignore': int(stats[5]),
        'pass': int(stats[6])
    }
    print('Uploading to nexus...')
    api_put('/zap', {
        'test_id': test_id,
        'result': json.dumps(result),
        'full_log': report
    }, token)
    print('Job done.')


def login():
    username = os.getenv('username')
    password = os.getenv('password')
    res = api_post('/user/login', {
        'username': username,
        'password': password
    }).json()
    return res['data']['token']


def api_post(path, data, token=None):
    return _request('POST', path, data=data, token=token)


def api_put(path, data, token=None):
    return _request('PUT', path, data=data, token=token)


def _request(method, path, headers=None, params=None, data=None, token=None):
    body = data
    if headers is None:
        headers = {}
    if token is not None:
        headers['Authorization'] = f'Bearer {token}'

    url = os.getenv('api_origin') + path
    print(f'{method} {url}, data={json.dumps(data)}')

    if method.upper() == 'GET':
        return requests.get(url, headers=headers, params=params, verify=False)
    elif method.upper() == 'POST':
        return requests.post(url, data=body, params=params,
                             headers=headers, verify=False)
    elif method.upper() == 'PUT':
        return requests.put(url, data=body, params=params,
                            headers=headers, verify=False)
    elif method.upper() == 'DELETE':
        return requests.delete(url, headers=headers, params=params, verify=False)


run()
