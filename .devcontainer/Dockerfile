# ベースイメージ（軽量なDebian）
FROM debian:bullseye

# vscodeユーザーを事前に作成（Codespacesと一致させる）
RUN useradd -m -u 1000 vscode

# 必要パッケージのインストール
RUN apt-get update && apt-get install -y \
    git curl unzip xz-utils zip libglu1-mesa bash \
    build-essential wget openssh-client \
    python3 python3-pip ca-certificates \
    --no-install-recommends && \
    apt-get clean && rm -rf /var/lib/apt/lists/*

# Flutter をインストール
RUN git clone https://github.com/flutter/flutter.git /usr/local/flutter

# Flutter のパス設定
ENV PATH="/usr/local/flutter/bin:/usr/local/flutter/bin/cache/dart-sdk/bin:${PATH}"

# Python ライブラリのインストール（requirements.txt をルートから取得）
COPY ../requirements.txt /tmp/requirements.txt
RUN pip3 install --upgrade pip && pip3 install -r /tmp/requirements.txt

# Git の警告を回避（flutter ディレクトリを safe.directory に追加）
RUN git config --global --add safe.directory /usr/local/flutter

# 作業ディレクトリ
WORKDIR /workspaces/flutter_ai_app

# vscode ユーザーに切り替え（Codespaceとの整合）
USER vscode
