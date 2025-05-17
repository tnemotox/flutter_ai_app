FROM debian:bullseye

# 必要なパッケージをインストール（Flutter, Python, build関連）
RUN apt-get update && apt-get install -y \
  git curl unzip xz-utils zip libglu1-mesa \
  bash build-essential wget openssh-client \
  python3 python3-pip

# requirements.txt をルートからコピーしてPythonライブラリをインストール
COPY requirements.txt /tmp/requirements.txt
RUN pip3 install -r /tmp/requirements.txt

# python コマンドをエイリアスとして追加（python3 → python）
RUN ln -s /usr/bin/python3 /usr/bin/python

# Flutter SDK を clone（安定版）してPATHを通す
RUN git clone https://github.com/flutter/flutter.git /opt/flutter -b stable

# 環境変数にFlutter/Dartのパスを追加
ENV PATH="/opt/flutter/bin:/opt/flutter/bin/cache/dart-sdk/bin:${PATH}"

# Flutterキャッシュの事前取得と診断実行
RUN flutter precache --web
RUN flutter doctor --verbose
