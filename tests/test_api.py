import json

FAIL_CODE = 400
SUCCESS_CODE = 200


def test_ping(client):
    res = client.get('/api/ping')
    assert res.status_code == SUCCESS_CODE
    expected = {'success': True}
    assert expected == json.loads(res.get_data(as_text=True))
