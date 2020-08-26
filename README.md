# django_starter

## このリポジトリについて

自分で利用するために作成したDjangoのテンプレートリポジトリです。  
docker-composeを利用して、環境構築作業を簡略化しています。  
  
現状、サーバーサイドに関しては  
`Python 3.7.7` + `Django 3.0.8` + `MySQL 5.7.31`が、  
フロントエンドに関しては  
`HTML` + `SCSS` + `Vue.js(cdn版)`が、  
それぞれすぐに利用できるようになっています。  
  
## 実行環境

### 利用環境(2020.08現在)  
```
- MacOS catalina 10.15.6
- Docker 19.03.8
    (- docker-desktop for Mac 2.2.0.3)
```

## 利用方法

#### 事前準備  
- `./.env`の作成  
`DB_NAME`, `DB_USER`, `DB_PASSWORD`, `DB_ROOT_PASSWORD`を定義
```
DB_NAME=********
DB_USER=********
DB_PASSWORD=********
DB_ROOT_PASSWORD=********
```
- `./config/local_settings.py`の作成  
`SECRET_KEY_LS`( Djangoプロジェクトのシークレットキー )を自分で定義し、  
`.env`と同内容の`DB_NAME`, `DB_USER`, `DB_PASSWORD`を記述
```Python
SECRET_KEY_LS = "*********"
DB_NAME = "***********"
DB_USER = "***********"
DB_PASSWORD = "*********"
```


#### 開発サーバーの実行
```
$ docker-compose up
```
#### 開発作業 ( manage.py 関連コマンドの実行 )  
```
$ docker-compose run web python manage.py [...]
```
そのままのディレクトリ構成で開発を続けたい場合は、  
`startapp`実行前に`app/startapp.md`を参照。
