# 軽量な Debian イメージをベースに使用
FROM debian:bullseye

# flutter を /opt/flutter にインストールするために必要なパッケージをインストール
RUN apt-get update && apt-get install -y \
    git curl unzip xz-utils zip libglu1-mesa bash \
    build-essential wget openssh-client \
    python3 python3-pip sudo ca-certificates \
    --no-install-recommends && \
    apt-get clean && rm -rf /var/lib/apt/lists/*

# flutter を /opt/flutter に clone
RUN git clone https://github.com/flutter/flutter.git /opt/flutter

# flutter にパスを通す
ENV PATH="/opt/flutter/bin:/opt/flutter/bin/cache/dart-sdk/bin:${PATH}"

# flutter repo を git safe.directory に追加（git警告対策）
RUN git config --global --add safe.directory /opt/flutter

# flutter doctor キャッシュ用に必要ファイル作成（Permission denied 対策）
RUN mkdir -p /opt/flutter/bin/cache && chmod -R 777 /opt/flutter

# requirements.txt をルートからコピーして Python ライブラリをインストール
COPY ../requirements.txt /tmp/requirements.txt
RUN pip3 install --upgrade pip && pip3 install -r /tmp/requirements.txt

# デフォルトの作業ディレクトリ
WORKDIR /workspaces/flutter_ai_app
