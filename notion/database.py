import requests
from .api import get_headers
from .logger import setup_logger

logger = setup_logger()


def create_company_database(title, parent_page_id):
    url = "https://api.notion.com/v1/databases"
    payload = {
        "parent": {
            "type": "page_id",
            "page_id": parent_page_id
        },
        "title": [{
            "type": "text",
            "text": {
                "content": title
            }
        }],
        "properties": {
            "企業名": {
                "title": {}
            },
            "ES提出": {
                "checkbox": {}
            },
            "興味度": {
                "select": {
                    "options": [{
                        "name": "⭐️" * i
                    } for i in range(1, 6)]
                }
            },
            "参加済み": {
                "checkbox": {}
            },
            "イベント名": {
                "rich_text": {}
            },
            "メモ": {
                "rich_text": {}
            }
        }
    }

    try:
        res = requests.post(url, headers=get_headers(), json=payload)
        if res.status_code == 200:
            logger.info(f"✅ データベース作成成功: {title}")
            return res.json()["id"]
        else:
            logger.error(f"❌ データベース作成失敗: {res.status_code}")
            logger.error(res.json())
            return None
    except Exception as e:
        logger.exception("🚨 APIリクエスト中に例外が発生しました")
        return None
