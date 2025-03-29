import requests
from .api import get_headers
from .logger import setup_logger

logger = setup_logger()


def create_company_page(company, database_id):
    url = "https://api.notion.com/v1/pages"
    payload = {
        "parent": {
            "database_id": database_id
        },
        "properties": {
            "企業名": {
                "title": [{
                    "text": {
                        "content": company["name"]
                    }
                }]
            },
            "興味度": {
                "select": {
                    "name": "⭐️" * int(company["interest"])
                }
            }
        },
        "children": [{
            "object": "block",
            "type": "heading_2",
            "heading_2": {
                "rich_text": [{
                    "type": "text",
                    "text": {
                        "content": "✅ ES情報"
                    }
                }]
            }
        }, {
            "object": "block",
            "type": "bulleted_list_item",
            "bulleted_list_item": {
                "rich_text": [{
                    "type": "text",
                    "text": {
                        "content": "提出日："
                    }
                }]
            }
        }, {
            "object": "block",
            "type": "bulleted_list_item",
            "bulleted_list_item": {
                "rich_text": [{
                    "type": "text",
                    "text": {
                        "content": "設問内容（抜粋）："
                    }
                }]
            }
        }, {
            "object": "block",
            "type": "bulleted_list_item",
            "bulleted_list_item": {
                "rich_text": [{
                    "type": "text",
                    "text": {
                        "content": "Q1："
                    }
                }]
            }
        }, {
            "object": "block",
            "type": "bulleted_list_item",
            "bulleted_list_item": {
                "rich_text": [{
                    "type": "text",
                    "text": {
                        "content": "Q2："
                    }
                }]
            }
        }, {
            "object": "block",
            "type": "heading_2",
            "heading_2": {
                "rich_text": [{
                    "type": "text",
                    "text": {
                        "content": "🎤 参加メモ"
                    }
                }]
            }
        }, {
            "object": "block",
            "type": "bulleted_list_item",
            "bulleted_list_item": {
                "rich_text": [{
                    "type": "text",
                    "text": {
                        "content": "イベント名："
                    }
                }]
            }
        }, {
            "object": "block",
            "type": "bulleted_list_item",
            "bulleted_list_item": {
                "rich_text": [{
                    "type": "text",
                    "text": {
                        "content": "実施形式：対面 / オンライン"
                    }
                }]
            }
        }, {
            "object": "block",
            "type": "bulleted_list_item",
            "bulleted_list_item": {
                "rich_text": [{
                    "type": "text",
                    "text": {
                        "content": "内容概要："
                    }
                }]
            }
        }, {
            "object": "block",
            "type": "bulleted_list_item",
            "bulleted_list_item": {
                "rich_text": [{
                    "type": "text",
                    "text": {
                        "content": "会社紹介："
                    }
                }]
            }
        }, {
            "object": "block",
            "type": "bulleted_list_item",
            "bulleted_list_item": {
                "rich_text": [{
                    "type": "text",
                    "text": {
                        "content": "印象に残った話："
                    }
                }]
            }
        }, {
            "object": "block",
            "type": "bulleted_list_item",
            "bulleted_list_item": {
                "rich_text": [{
                    "type": "text",
                    "text": {
                        "content": "社員の雰囲気："
                    }
                }]
            }
        }, {
            "object": "block",
            "type": "heading_2",
            "heading_2": {
                "rich_text": [{
                    "type": "text",
                    "text": {
                        "content": "📝 メモ・気づき"
                    }
                }]
            }
        }, {
            "object": "block",
            "type": "bulleted_list_item",
            "bulleted_list_item": {
                "rich_text": [{
                    "type": "text",
                    "text": {
                        "content": "-"
                    }
                }]
            }
        }]
    }
    try:
        res = requests.post(url, headers=get_headers(), json=payload)
        if res.status_code == 200:
            logger.info(f"✅ {company['name']} ページ作成成功")
            return res.json()
        else:
            logger.error(f"❌ {company['name']} ページ作成失敗: {res.status_code}")
            logger.error(res.json())
            return None
    except Exception as e:
        logger.exception(f"🚨 {company['name']} ページ作成中に例外発生")
        return None
