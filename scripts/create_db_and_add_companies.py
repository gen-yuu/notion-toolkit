import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
import json
from notion import *
from notion.logger import setup_logger

logger = setup_logger()


def main():
    logger.info("💻 Notionデータベース作成開始")
    with open("data/companies.json", "r", encoding="utf-8") as f:
        companies = json.load(f)

    PARENT_PAGE_ID = get_parent_page_id()
    db_id = create_company_database("企業情報データベース", PARENT_PAGE_ID)
    if not db_id:
        logger.error("❌ データベース作成失敗")
        return

    for company in companies:
        logger.info(f"➡️ {company['name']} 登録開始")
        create_company_page(company, db_id)
    logger.info("✅ 全企業の登録完了！")


if __name__ == "__main__":
    main()
