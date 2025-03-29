# 📝 Notion企業データ管理ツール

このプロジェクトは、企業情報（興味度・ES提出・参加イベントなど）を Notion データベース上で一元管理するための自動化ツールです。

## 📦 機能概要

- 企業一覧（JSON）をもとに Notion にデータベースを作成
- 各企業ごとにテンプレート付きのページを自動追加
- 興味度を ⭐️ の数で可視化
- エラーハンドリングとログ出力に対応

---

## 🧩 ディレクトリ構成
```bash
.
├── .env                    # 環境変数（APIキーなど）※除外対象
├── data/
│   └── companies.json      # 企業情報（興味度・参加など）
├── notion/
│   ├── init.py
│   ├── api.py              # ヘッダー・APIキー取得
│   ├── database.py         # データベース作成処理
│   ├── pages.py            # ページ追加処理
│   └── logger.py           # ターミナル表示用ロガー
├── scripts/
│   └── create_db_and_add_companies.py  # メインスクリプト
│   └── test.py             #接続テスト
├── logs/                   # ログ出力先（今は未使用）
├── venv/                   # 仮想環境（.gitignore 済）
└── README.md
```
---

## ⚙️ セットアップ手順

### 1. 仮想環境の作成

```bash
# /bin/bash
python3 -m venv venv
source venv/bin/activate
```

### 2. 必要なライブラリのインストール
```bash
# /bin/bash
pip install -r requirements.txt
```
### 3. .env ファイルを作成
```bash
# .envファイル
NOTION_API_KEY=secret_xxx...       # Notion Integrationのシークレットキー
NOTION_PARENT_PAGE_ID=xxx...       # 親ページのID（UUID形式）
```
---

## 🧾 企業データ（JSON形式の例）
### 🔍 各フィールドの意味

| フィールド名     | 型         | 説明                                                   |
|------------------|------------|--------------------------------------------------------|
| `name`           | string     | 企業名。Notionページのタイトルとして使われます。         |
| `interest`       | string     | 興味度（1〜5）。Notionでは⭐️の数に変換されます。        |
| `es_submitted`   | boolean    | ES（エントリーシート）を提出済みかどうか。              |
| `attended`       | boolean    | イベント（説明会など）に参加済みかどうか。              |
| `event_name`     | string     | 参加したイベントの名称。空文字でもOK。                  |
| `note`           | string     | 自由記述メモ。会社の印象・社員の雰囲気など。            |
---

### ✅ 企業データの例

```json
[
  {
    "name": "Sansan",
    "interest": "3",
    "es_submitted": false,
    "attended": false,
    "event_name": "2/24 エンカレ合同説明会",
    "note": "オンライン開催、社員の雰囲気が柔らかかった。"
  },
  {
    "name": "PKSHA Technology",
    "interest": "4",
    "es_submitted": false,
    "attended": false,
    "event_name": "",
    "note": ""
  },
  {
    "name": "NTTドコモ",
    "interest": "5",
    "es_submitted": true,
    "attended": true,
    "event_name": "3/29 ONECARRER オンライン合説",
    "note": "技術志向が強く、研究内容との親和性が高そう。"
  }
]
```

## 🚀 実行方法
```bash
#/bin/bash
python scripts/create_db_and_add_companies.py
```
成功すると：
- Notionに「企業情報データベース」が作成される
- 各企業のページがテンプレート付きで登録される
- ログがターミナルに出力される（例：✅ Sansan ページ作成成功）
---

## 🔧 カスタマイズ

### ✅ 登録テンプレート編集

- `pages.py` の `"children"` ブロックで内容を変更できます

---

## 🔐 注意点

- `.env` は `.gitignore` されているため GitHub にアップロードされません
- Notion Integration は DB/ページに **共有されている必要があります**

---

## 📌 今後のアイデア（TODO）

- [ ] CLI引数で企業名をフィルタ指定
- [ ] 登録済みの企業をスキップ or 上書き
- [ ] CSV → JSON 変換サポート
- [ ] Notionからのデータ取得＆更新対応

---

## 🤝 ライセンス

MIT License（自由に使ってOK！）