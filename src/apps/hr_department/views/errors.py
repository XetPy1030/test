class RequiredError(Exception):
    def __init__(self):
        super().__init__("user_id not found in params request")


class UserIsNotEditable(Exception):
    def __init__(self):
        super().__init__("user is not editable")
