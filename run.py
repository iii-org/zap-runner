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
    subprocess.run(f'python zap-full-scan.py -P 9487 -t {os.getenv("TARGET_URL")} -r report.html -J report.json',
                            stdout=subprocess.PIPE, shell=True).stdout.decode('utf-8').strip()
    result = {
        '0': 0,
        '1': 0,
        '2': 0,
        '3': 0
    }
    with open('/zap/wrk/report.json', 'r') as f:
        data = json.load(f)
        alerts = data['site'][0]['alerts']
        for alert in alerts:
            result[alert['riskcode']] += 1

    report = None
    with open('/zap/wrk/report.html', 'r') as file:
        report = file.read()

    print('Uploading to nexus...')
    res = api_put('/zap', {
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

    url = f'{os.getenv("api_origin")}{path}'

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
