FROM debian:bullseye

# システムツール & Python & Flutter前提環境
RUN apt-get update && apt-get install -y \
  git curl unzip xz-utils zip libglu1-mesa \
  bash build-essential wget openssh-client \
  python3 python3-pip

# Pythonパッケージ
COPY .devcontainer/requirements.txt /tmp/requirements.txt
RUN pip3 install -r /tmp/requirements.txt

# python コマンドエイリアス
RUN ln -s /usr/bin/python3 /usr/bin/python

# Flutter SDK セットアップ
RUN git clone https://github.com/flutter/flutter.git /opt/flutter -b stable

# PATH にFlutter & Dart SDK を追加
ENV PATH="/opt/flutter/bin:/opt/flutter/bin/cache/dart-sdk/bin:${PATH}"

# 初期Flutterキャッシュ & 検証
RUN flutter precache --web
RUN flutter doctor --verbose
