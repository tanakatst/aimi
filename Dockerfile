# ベースイメージとして公式のPythonイメージを使用
FROM python:3.10-slim

# 作業ディレクトリを設定
WORKDIR /app

# 依存関係ファイルをコンテナにコピー
COPY requirements.txt .

# 依存関係をインストール
RUN pip install --no-cache-dir -r requirements.txt

# 残りのアプリケーションコードをコンテナにコピー
COPY . .

# Streamlitが使用するポートを公開
EXPOSE 8501

# Streamlitアプリを実行
CMD ["streamlit", "run", "app.py"]
