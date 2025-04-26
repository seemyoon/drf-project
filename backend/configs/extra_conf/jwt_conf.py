from datetime import timedelta

SIMPLE_JWT = {
    "ACCESS_TOKEN_LIFETIME": timedelta(minutes=10),  # how long live access token
    "REFRESH_TOKEN_LIFETIME": timedelta(minutes=20),  # how long live refresh token
    "ROTATE_REFRESH_TOKENS": True,  # True  - return refresh token
    "BLACKLIST_AFTER_ROTATION": True,
    # if we didn't indicate it, we will be able to use refresh tokens several times (but it's bed)
    "UPDATE_LAST_LOGIN": True,  # Update or not last_login (in db)
    "AUTH_HEADER_TYPES": ("Bearer",),  # We can set Jwt as well
    # "SIGNING_KEY": settings.SECRET_KEY == os.environ.get('SECRET_KEY')
}
