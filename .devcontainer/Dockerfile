# ベースイメージ（軽量なDebian）
FROM debian:bullseye

# 必要パッケージのインストール
RUN apt-get update && apt-get install -y \
    git curl unzip xz-utils zip libglu1-mesa bash \
    build-essential wget openssh-client \
    python3 python3-pip \
    ca-certificates \
    --no-install-recommends && \
    apt-get clean && rm -rf /var/lib/apt/lists/*

# flutter をインストール
RUN git clone https://github.com/flutter/flutter.git /usr/local/flutter

# flutter パスを通す
ENV PATH="/usr/local/flutter/bin:/usr/local/flutter/bin/cache/dart-sdk/bin:${PATH}"

# flutter repo を git safe.directory に追加（git警告回避）
RUN git config --global --add safe.directory /usr/local/flutter

# Python ライブラリのインストール
COPY requirements.txt /tmp/requirements.txt
RUN pip3 install --upgrade pip && pip3 install -r /tmp/requirements.txt

# flutter doctor は postCreateCommand に移動（非 root で実行）
# デフォルトの作業ディレクトリ
WORKDIR /workspaces/flutter_ai_app
