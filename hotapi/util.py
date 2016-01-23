import os
import json


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

"""
    *args (variables non-nommees) : used to pass a non-keyworded variables length argument to the function. It is varargs
    **kwargs (variables nommees): used to pass a keyworded variables length argument to the function. It is varargs
    You should use **kwargs if you want to handle "named arguments" in a function
"""


def get_api_key(name):
    filename = os.path.join(BASE_DIR, 'keys', 'apikeys.json')
    with open(filename, 'r') as fhandler:
        keys = json.loads(fhandler.read())
        return keys[name]['apikey']


def get_str_from_lst(*args):
    return ','.join(args)
