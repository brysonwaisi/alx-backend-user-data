#!/usr/bin/env python3
'''SEssion Authentication Module'''
from api.v1.auth.auth import Auth
from models.user import User
import uuid


class SessionAuth(Auth):
    '''Session Auth Class'''
    user_id_by_session_id = {}
