import pytest
import requests
import json
import datetime

#Fixer API is capable of delivering real-time exchange rate data for 170 world currencies
# https://fixer.io/documentation
# https://fixer.io/documentation#quickstart

# Define the base URL for the Fixer API
base_url = "https://data.fixer.io/api/" 


@pytest.fixture()
def acc_key():
    return "f3cded4e19632e8560304d053b0b9ee0"
    

def test_get_currency_symbols(acc_key):
    """Test the symbols endpoint of the Fixer API."""
    end_point = "/symbols"
    url = base_url + end_point + "?access_key=" + acc_key
    response = requests.get(url)
    print(json.dumps(response.json(), indent=4))
    assert response.status_code == 200
    assert response.json()['success'] == True

def test_get_specified_symbols(acc_key):
    """Test the latest rate for specific currenc with EUR Base."""
    end_point = "/latest"
    url = base_url + end_point + "?access_key=" + acc_key
    querystring = {"symbols":"USD,CAD,AUD"}
    response = requests.get(url,params=querystring)
    print(json.dumps(response.json(), indent=4))
    assert response.status_code == 200
    assert response.json()['success'] == True

def test_get_specified_symbols_INRBase(acc_key):
    """Test the latest rate for specific currenc with EUR Base."""
    end_point = "/latest"
    url = base_url + end_point 
    querystring = {"symbols":"USD,CAD,AUD"}
    querystring2 = {"base":"INR"}
    params = {"access_key": acc_key} | querystring | querystring2
    response = requests.get(url,params=params)
    print(json.dumps(response.json(), indent=4))
    assert response.status_code == 200
    assert response.json()['success'] == False
   #ACCESS RESTRICTED IN FREE PLAN

#Latest Rate Single Currency:
def test_get_single_currency_rate(acc_key):
    end_point = "/latest"
    url = base_url + end_point 
    querystring = {"symbols":"INR"}
    querystring2 = {"base":"EUR"}
    params = {"access_key": acc_key} | querystring | querystring2
    response = requests.get(url,params=params)
    print(json.dumps(response.json(), indent=4))
    assert response.status_code == 200
    assert response.json()['success'] == True

#Historical Rates Endpoint
def test_historical_currency_rate(acc_key):
    url = base_url
    his_date = "2013-12-24"
    querystring = {"symbols":"INR"}
    querystring2 = {"base":"EUR"}
    params = {"access_key": acc_key} | querystring | querystring2
    response = requests.get(url+his_date,params=params)
    print(json.dumps(response.json(), indent=4))
    print(response.json()['historical'])
    assert response.status_code == 200
    assert response.json()['success'] == True
    assert response.json()['historical'] == True


#Negative testing
#Historical Rates Endpoint_<1998
def test_historical_currency_old_rate(acc_key):
    url = base_url
    his_date = "1998-12-31" #1999-01-01 is available
    querystring = {"symbols":"INR"}
    querystring2 = {"base":"EUR"}
    params = {"access_key": acc_key} | querystring | querystring2
    response = requests.get(url+his_date,params=params)
    print(json.dumps(response.json(), indent=4))
    assert response.status_code == 200
    assert response.json()['success'] == False
    

#Historical Rates Endpoint future date
def test_historical_currency_future_rate(acc_key):
    url = base_url
    current_dateTime = (datetime.datetime.now() + datetime.timedelta(days=2)).date()
    querystring = {"symbols":"INR"}
    querystring2 = {"base":"EUR"}
    params = {"access_key": acc_key} | querystring | querystring2
    response = requests.get(url+str(current_dateTime),params=params)
    print(json.dumps(response.json(), indent=4))
    assert response.status_code == 200
    assert response.json()['success'] == False

#Historical Rates Endpoint_incorrect date format
def test_historical_currency_old_rate(acc_key):
    url = base_url
    his_date = "1998-31-12" 
    querystring = {"symbols":"INR"}
    querystring2 = {"base":"EUR"}
    params = {"access_key": acc_key} | querystring | querystring2
    response = requests.get(url+his_date,params=params)
    print(json.dumps(response.json(), indent=4))
    assert response.status_code == 200
    assert response.json()['success'] == False
    assert "Required format" in response.json()['error']['info']
    
#Currency Convert Endpoint
def test_Convert_Endpoint(acc_key):
    end_point = "convert"
    url = base_url + end_point 
    querystring1 = {"from":"EUR"}
    querystring2 = {"to":"INR"}
    querystring3 = {"amount":"25"}
    params = {"access_key": acc_key} | querystring1 | querystring2 | querystring3
    response = requests.get(url,params=params)
    print(json.dumps(response.json(), indent=4))
    #assert response.status_code == 200
    #assert response.json()['success'] == True
    # "info": "Access Restricted - Your current Subscription Plan does not support this API Function."
    