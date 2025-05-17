# ベースイメージ
FROM debian:bullseye

# 必要なパッケージのインストール
RUN apt-get update && apt-get install -y \
    git curl unzip xz-utils zip libglu1-mesa bash \
    build-essential wget openssh-client \
    python3 python3-pip \
    ca-certificates \
    --no-install-recommends && \
    apt-get clean && rm -rf /var/lib/apt/lists/*

# flutter をインストール（所有者変更は後回しにする）
RUN git clone --depth=1 https://github.com/flutter/flutter.git /usr/local/flutter

# flutter パスを通す
ENV PATH="/usr/local/flutter/bin:/usr/local/flutter/bin/cache/dart-sdk/bin:${PATH}"

# flutter doctor を一度実行してキャッシュ生成（ここで root でOK）
RUN flutter doctor || true

# Pythonライブラリのインストール
COPY requirements.txt /tmp/requirements.txt
RUN pip3 install --upgrade pip && pip3 install -r /tmp/requirements.txt

# git safe.directory 設定（rootでOK）
RUN git config --global --add safe.directory /usr/local/flutter

# vscodeユーザーに切り替える（devcontainerが作成後に適用される）
USER vscode

# flutter の所有者を vscode に変更（ここで chown）
RUN sudo chown -R vscode:vscode /usr/local/flutter

# デフォルトの作業ディレクトリ
WORKDIR /workspaces/flutter_ai_app
