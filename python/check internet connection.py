from requests import get, exceptions

def internetConnection():
    try:
        get('https://google.com', timeout = 3)
        print('connected')
    except exceptions.ConnectionError:
        print('not connected')
internetConnection()





