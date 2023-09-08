from passlib.context import CryptContext
pwd_context = CryptContext(schemes=["bcrypt"], deprecated = "auto") # telling Passlib what the hashing algorith is

def hash(password: str):

    return pwd_context.hash(password)

def verify(plain_password, hashed_password): # Checks whether he password from the login is equal to the hashed
    # password that we retrieved from our database, see user auth.py
    return pwd_context.verify(plain_password, hashed_password)