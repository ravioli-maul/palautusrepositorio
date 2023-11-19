import re
from entities.user import User
from repositories.user_repository import (
    user_repository as default_user_repository
)


class UserInputError(Exception):
    pass


class AuthenticationError(Exception):
    pass


class UserService:
    def __init__(self, user_repository=default_user_repository):
        self._user_repository = user_repository

    def check_credentials(self, username, password):
        if not username or not password:
            raise UserInputError("Username and password are required")

        user = self._user_repository.find_by_username(username)

        if not user or user.password != password:
            raise AuthenticationError("Invalid username or password")

        return user

    def create_user(self, username, password, password_confirmation):
        self.validate(username, password, password_confirmation)

        user = self._user_repository.create(
            User(username, password)
        )

        return user

    def validate(self, username, password, password_confirmation):
        if not username or not password:
            raise UserInputError("Username and password are required")
        
        # Username only lowercase letters, at least 3 characters long.
        if len(username) < 3 or not re.match("^[a-z]+$", username):
            raise UserInputError("Invalid username. Username must have at least 3 lowercase letters.")

        # Password at least 8 characters, including at least one non-letter character.
        if len(password) < 8 or re.match("^[a-zA-Z]*$", password):
            raise UserInputError("Invalid password. Password must have at least 8 characters and contain non-letter characters.")
        
        if password != password_confirmation:
            raise UserInputError("Password and password confirmation do not match.")


user_service = UserService()
