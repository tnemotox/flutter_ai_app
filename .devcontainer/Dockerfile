FROM debian:bullseye

# 基本ツールをインストール
RUN apt-get update && apt-get install -y \
    git curl unzip xz-utils zip libglu1-mesa bash build-essential wget openssh-client

# Flutter SDKをインストール
RUN git clone https://github.com/flutter/flutter.git /opt/flutter -b stable

# 環境変数にFlutterを追加
ENV PATH="/opt/flutter/bin:/opt/flutter/bin/cache/dart-sdk/bin:${PATH}"

# Flutter初期化（Web対応）
RUN flutter precache --web
RUN flutter doctor --verbose
