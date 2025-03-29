import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from notion.logger import setup_logger
from notion import *
import requests

logger = setup_logger()


def test_database_connection(PAGE_ID, headers):
    url = f"https://api.notion.com/v1/pages/{PAGE_ID}"
    res = requests.get(url, headers=headers)
    print(f"📡 DB 接続テスト: {res.status_code}")

    if res.status_code == 200:
        print("✅ 接続成功！データベース情報取得完了。")
    else:
        print("❌ 接続失敗。以下を確認してください：")
        print("- APIキーが正しいか")
        print("- DATABASE_ID が間違っていないか")
        print("- Integration が Notion DB に共有されているか")
        print("- レスポンス詳細:", res.json())


def main():
    PARENT_PAGE_ID = get_parent_page_id()
    headers = get_headers()
    test_database_connection(PARENT_PAGE_ID, headers)


if __name__ == "__main__":
    main()
