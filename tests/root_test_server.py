import requests

def test_service_ok():
    r = requests.get("http://127.0.0.1:8000/redfish/v1/")
    assert r.status_code == 200
    assert r.json()["Name"] == "Root Service"