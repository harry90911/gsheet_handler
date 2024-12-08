import os
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request

SCOPES = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive"
]

CREDENTIALS_FILE = "client_secret.json"  # 替換為你的 OAuth 憑據文件，請透過這個網址來生成
TOKEN_FILE = "token.json"  # 用於保存和重用 OAuth Token



def authenticate_google_client():
    """Authenticate and return a Google API client."""
    creds = None

    # 檢查是否存在憑據文件
    if not os.path.exists(CREDENTIALS_FILE):
        raise FileNotFoundError(
            f"OAuth credentials file '{CREDENTIALS_FILE}' not found. "
            "Please configure and download the credential file from https://console.cloud.google.com/apis/credentials"
        )

    # 如果 token.json 已存在，嘗試加載憑據
    if os.path.exists(TOKEN_FILE):
        creds = Credentials.from_authorized_user_file(TOKEN_FILE, SCOPES)

    # 如果憑據無效，進行授權
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(CREDENTIALS_FILE, SCOPES)
            creds = flow.run_local_server(port=0)
        # 保存 Token
        with open(TOKEN_FILE, "w") as token:
            token.write(creds.to_json())

    return creds
