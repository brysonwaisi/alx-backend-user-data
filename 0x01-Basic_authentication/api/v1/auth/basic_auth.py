#!/usr/bin/env python3
'''Basic Authentication Module'''
from api.v1.auth.auth import Auth
from base64 import b64decode
from models.user import User
from typing import TypeVar


class BasicAuth(Auth):
    '''Basic authentication class'''
    pass
