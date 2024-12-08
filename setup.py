from setuptools import setup, find_packages

setup(
    name="gsheet_handler",  # 包名稱
    version="0.1.0",  # 版本號
    description="A Python package for Google Sheets integration using OAuth2 and Pandas.",
    author="hank.liao",
    author_email="harry90911@gmail.com",
    # url="https://github.com/your_username/gsheet_handler",  # GitHub 項目地址（可選）
    packages=find_packages(),  # 自動查找包
    install_requires=[
        "google-auth",
        "google-auth-oauthlib",
        "google-auth-httplib2",
        "gspread",
        "pandas",
    ],  # 包的依賴
    python_requires=">=3.6",  # 最低 Python 版本
)