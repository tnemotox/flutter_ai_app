# ベースイメージを指定（軽量な Debian）
FROM debian:bullseye

# Flutterインストールに必要なパッケージをインストール
RUN apt-get update && apt-get install -y \
    git curl unzip xz-utils zip libglu1-mesa \
    bash build-essential wget openssh-client \
    python3 python3-pip

# Flutter SDKをインストール
ENV FLUTTER_VERSION=3.19.6
RUN git clone https://github.com/flutter/flutter.git /usr/local/flutter \
    && cd /usr/local/flutter \
    && git checkout $FLUTTER_VERSION

# Flutterのパスを通す
ENV PATH="/usr/local/flutter/bin:/usr/local/flutter/bin/cache/dart-sdk/bin:${PATH}"

# Pythonパッケージを requirements.txt からインストール（← このファイルはルート）
COPY requirements.txt /tmp/requirements.txt
RUN pip3 install --no-cache-dir -r /tmp/requirements.txt

# Flutterの初期セットアップ
RUN flutter doctor

# ユーザー設定（Codespacesの標準）
# 末尾に追加（Flutterなどの設定の後）
RUN useradd -m vscode
USER vscode