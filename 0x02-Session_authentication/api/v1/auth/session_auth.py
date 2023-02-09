#!/usr/bin/env python3
'''Session Authentication Module'''
from api.v1.auth.auth import Auth
from flask import request
from models.user import User
from uuid import uuid4


class SessionAuth(Auth):
    '''Session Auth Class'''
    user_id_by_session_id = {}

    def create_session(self, user_id: str = None) -> str:
        '''creates session id for user'''
        if type(user_id) is str:
            session_id = str(uuid4())
            self.user_id_by_session_id[session_id] = user_id
            return session_id

    def user_id_for_session_id(self, session_id: str = None) -> str:
        '''Retrieves user id of user associated
        with session id'''
        if type(session_id) is str:
            return self.user_id_by_session_id.get(session_id)
