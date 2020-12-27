from datetime import datetime

import requests


def test_case_creat():
    testcaseurl= 'http://127.0.0.1:5000/testcase'
    r=requests.post(
        testcaseurl,
        json={
            'name': f'case1 {datetime.now().isoformat()}',
            'description': 'description 1',
            'steps': ['1', '2', '3']
        }
    )
    assert r.status_code == 200
    r=requests.get(testcaseurl)
    print(r.json())
    assert r.json()['body']