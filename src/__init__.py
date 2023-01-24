# # check valid jwt token
# # check expired jwt token
# import jwt
# 
# 
# def check_jwt_token(token):
#     try:
#         jwt.decode(token)
#         return True
#     except jwt.ExpiredSignatureError:
#         print('Signature expired. Please log in again.')
#         return False
#     except jwt.InvalidTokenError:
#         print('Invalid token. Please log in again.')
#         return False
# 
# 
# token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiaWF0IjoxNTE2MjM5MDIyfQ.SflKxwRJSMeKKF2QT4fwpMeJf36POk6yJV_adQssw5c"
# check_jwt_token(token)
