# Django Tutorial Project

## 概要
このプロジェクトはDjangoチュートリアルの学習用リポジトリです。Djangoの基本的な機能を実装し、Webアプリケーション開発の基礎を学びます。

## 必要条件
- Python 3.8以上
- pip (Pythonパッケージマネージャー)

## セットアップ手順

### 1. リポジトリのクローン
```bash
git clone git@github.com:FRISKSYA/django_tutorial.git
cd django_tutorial
```

### 2. 仮想環境の作成と有効化
```bash
# 仮想環境の作成
python -m venv tutorial_env

# 仮想環境の有効化
## Linux/Macの場合
source tutorial_env/bin/activate
## Windowsの場合
.\tutorial_env\Scripts\activate
```

### 3. 依存パッケージのインストール
```bash
pip install django
```

### 4. データベースのマイグレーション
```bash
python manage.py migrate
```

### 5. 開発サーバーの起動
```bash
python manage.py runserver
```

サーバーが起動したら、ブラウザで http://127.0.0.1:8000/ にアクセスできます。

## プロジェクト構造
```
project/
├── manage.py
├── mysite/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
└── polls/
    ├── __init__.py
    ├── admin.py
    ├── apps.py
    ├── models.py
    ├── views.py
    ├── urls.py
    └── tests.py
```

## 開発の流れ
1. モデルの変更を行う
2. マイグレーションを作成: `python manage.py makemigrations`
3. データベースに反映: `python manage.py migrate`
4. 開発サーバーで確認: `python manage.py runserver`

## 参考資料
- [Django公式ドキュメント](https://docs.djangoproject.com/ja/5.1/)
- [Django Girls Tutorial](https://tutorial.djangogirls.org/ja/)