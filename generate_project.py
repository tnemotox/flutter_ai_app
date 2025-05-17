import os
import openai
from dotenv import load_dotenv
import re
import subprocess

# .env から APIキーを取得
load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

# Flutterプロジェクト初期化（pubspec.yaml がない場合）
if not os.path.exists("pubspec.yaml"):
    subprocess.run(["flutter", "create", "."], check=True)

# 仕様を読み込む
with open("specs/spec.md", "r", encoding="utf-8") as f:
    spec = f.read()

# AIへのプロンプト
messages = [
    {
        "role": "system",
        "content": "Flutterプロフェッショナルエンジニアとして振る舞ってください。"
    },
    {
        "role": "user",
        "content": f"""以下の仕様に基づいて、Flutterアプリを構築してください。

# 要件
- 状態管理は Riverpod（hooks_riverpod）で実装してください
- 画面遷移には go_router を使用してください
- 再利用可能なWidgetは lib/widgets/ に分離してください
- 以下の3ファイルをコードブロック形式で出力してください：
  - pubspec.yaml（Flutter公式の現在の安定バージョンを記載し、latest や any などの曖昧な指定は使わないでください）
  - lib/main.dart（アプリのエントリーポイント）
  - test/widget_test.dart（基本的なUIテスト）

# アプリ仕様：
{spec}
"""
    }
]

# AIへリクエスト
response = openai.ChatCompletion.create(
    model="gpt-4o",
    messages=messages,
    temperature=0.2
)

content = response['choices'][0]['message']['content']

# コードブロック抽出関数
def extract_code_block(language, text):
    match = re.search(rf"```{language}\s+(.*?)```", text, re.DOTALL)
    return match.group(1).strip() if match else None

# 抽出
yaml_code = extract_code_block("yaml", content)
dart_code = extract_code_block("dart", content)

# 保存先のディレクトリを準備
os.makedirs("lib", exist_ok=True)
os.makedirs("test", exist_ok=True)
os.makedirs("lib/widgets", exist_ok=True)

# 書き込み
if yaml_code:
    with open("pubspec.yaml", "w", encoding="utf-8") as f:
        f.write(yaml_code)

if dart_code:
    with open("lib/main.dart", "w", encoding="utf-8") as f:
        f.write(dart_code)

# widget_test.dart を抽出
test_code = None
dart_blocks = re.findall(r"```dart\s+(.*?)```", content, re.DOTALL)
for block in dart_blocks:
    if "testWidgets" in block:
        test_code = block.strip()
        break

if test_code:
    with open("test/widget_test.dart", "w", encoding="utf-8") as f:
        f.write(test_code)

print("✅ 最新の安定バージョン付き Flutter アプリを生成しました！")
