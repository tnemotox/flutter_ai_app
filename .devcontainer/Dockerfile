# ベースイメージ（軽量なDebian）
FROM debian:bullseye

# 必要パッケージのインストール
RUN apt-get update && apt-get install -y \
    git curl unzip xz-utils zip libglu1-mesa bash \
    build-essential wget openssh-client \
    python3 python3-pip ca-certificates \
    --no-install-recommends && \
    apt-get clean && rm -rf /var/lib/apt/lists/*

# Flutter をインストール（ユーザー権限は root のままでOK）
RUN git clone https://github.com/flutter/flutter.git /usr/local/flutter

# Flutter のパスを通す
ENV PATH="/usr/local/flutter/bin:/usr/local/flutter/bin/cache/dart-sdk/bin:${PATH}"

# Python ライブラリのインストール
COPY requirements.txt /tmp/requirements.txt
RUN pip3 install --upgrade pip && pip3 install -r /tmp/requirements.txt

# Flutter の Git 所有者警告を抑制
RUN git config --global --add safe.directory /usr/local/flutter

# デフォルトの作業ディレクトリを設定
WORKDIR /workspaces/flutter_ai_app
