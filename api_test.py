import requests
import json
from datetime import datetime


def main():
    url = "http://localhost:8000/contacts"
    current_datetime = datetime.now().isoformat()  # JSON変換できるようにISO形式に変換
    body = {
        "id": 1,
        "name": "山田さん",
        "email": "yamada@test.com",
        "url": "https://example.com/",
        "gender": 2,
        "message": "メッセージです",
        "is_enabled": True,
        "created_at": current_datetime,
    }

    # 辞書型 -> JSON形式に変換してPOST通信
    res = requests.post(url, json.dumps(body))
    print(res.json())


if __name__ == "__main__":
    main()
