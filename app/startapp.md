アプリケーションのディレクトリ構成を慣例より1階層深くしているため、  
`startapp`コマンドで新規のアプリケーションを生成する場合は、  
以下の手順のように事前にディレクトリを用意してから実行する必要があります。  
  
1. `mkdir app/[appname]`
2. `docker-compose run web python manage.py [app_name] ./app/[app_name]`
