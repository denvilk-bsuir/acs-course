import pyotp
from fastapi import Request
from core.config import TOTP_ADMIN_SECRET
from core.exceptions import PERMISSION_DENIED

def IsAdmin(request: Request):
    auth_header = request.headers.get('Authorization')
    if auth_header != pyotp.TOTP(TOTP_ADMIN_SECRET).now():
        raise PERMISSION_DENIED