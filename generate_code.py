import openai
import os
from dotenv import load_dotenv
import re

# .envの読み込み
load_dotenv()

# APIキーの設定（最新版でもこの方法が推奨）
openai.api_key = os.getenv("OPENAI_API_KEY")

# 仕様ファイル読み込み
with open("specs/spec.md", "r", encoding="utf-8") as f:
    spec_content = f.read()

# メッセージ構築
messages = [
    {
        "role": "system",
        "content": "Flutterエンジニアとして振る舞ってください。ユーザーの仕様を元に、main.dartを生成してください。"
    },
    {
        "role": "user",
        "content": f"以下の仕様に基づいて、Flutterアプリ（main.dart）のコードを生成してください。\n\n{spec_content}"
    }
]

# 最新API（静的呼び出し）で実行
response = openai.chat.completions.create(
    model="gpt-4o",
    messages=messages,
    temperature=0.2
)

# コード抽出
content = response.choices[0].message.content
match = re.search(r"```dart(.*?)```", content, re.DOTALL)
dart_code = match.group(1).strip() if match else content

# 出力保存
os.makedirs("lib", exist_ok=True)
with open("lib/main.dart", "w", encoding="utf-8") as f:
    f.write(dart_code)

print("✅ main.dart を生成しました！")
