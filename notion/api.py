import os
from dotenv import load_dotenv

load_dotenv()


def get_headers():
    return {
        "Authorization": f"Bearer {os.getenv('NOTION_API_KEY')}",
        "Notion-Version": "2022-06-28",
        "Content-Type": "application/json"
    }


def get_parent_page_id():
    return os.getenv("NOTION_DATABASE_ID")
