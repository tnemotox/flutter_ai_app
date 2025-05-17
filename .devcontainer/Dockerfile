# ベースイメージ（軽量な Debian）
FROM debian:bullseye

# vscode ユーザー作成（UID 1000はCodespacesの標準）
RUN useradd -m vscode -u 1000

# 環境変数（flutterとchromiumのパスを通す）
ENV PATH="/usr/local/flutter/bin:/usr/local/flutter/bin/cache/dart-sdk/bin:${PATH}"
ENV CHROME_EXECUTABLE=/usr/bin/chromium

# 必要パッケージのインストール（キャッシュ最適化のため一行で）
RUN apt-get update \
 && DEBIAN_FRONTEND=noninteractive apt-get install -y --no-install-recommends \
    git curl unzip xz-utils zip libglu1-mesa bash \
    build-essential wget openssh-client \
    python3 python3-pip \
    clang cmake ninja-build pkg-config \
    libgtk-3-dev mesa-utils mesa-utils-extra \
    chromium \
    ca-certificates \
 && apt-get clean \
 && rm -rf /var/lib/apt/lists/*

# flutter をインストール（version unknown 対策のため shallow clone をやめる）
RUN git clone https://github.com/flutter/flutter.git /usr/local/flutter \
 && chown -R vscode:vscode /usr/local/flutter

# vscode ユーザーに切り替え
USER vscode

# precache（キャッシュ生成を早くするため）
RUN flutter precache --android --ios --web --linux --macos --windows || true

# Python ライブラリのインストール
COPY ../requirements.txt /tmp/requirements.txt
RUN pip3 install --user --root-user-action=ignore -r /tmp/requirements.txt

# Flutter キャッシュ生成（失敗しても止めない）
RUN flutter doctor --android-licenses || true && flutter doctor || true

# デフォルトの作業ディレクトリ
WORKDIR /workspaces/flutter_ai_app
