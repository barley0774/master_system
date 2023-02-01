# mitmlearning

学習者の許可を得ずに実行しないでください．
また，公衆無線LAN環境では絶対に使用しないでください．
自分が管理者のLAN内でのみ実施するようにしてください．

## pythonの仮想環境設定
```sudo apt update```  
```sudo apt install python3.?-venv```    
```python3 -m venv venv```  

## bettercapのインストール
```sudo apt install bettercap```でbettercapのインストール  
```bettercap -version```でバージョンが2.32か確認  
```https://github.com/bettercap/capletsからcaplets```をインストール  
インストール手順は，```https://github.com/bettercap/caplets```を確認  

```master_system/hstshijack.cap```を```caplets/hstshijack```にコピー  
bettercapを起動し，bettercapコンソール内で```caplets.update```と入力  
bettercapコンソール内で，```hstshijack/hstshijack```と入力し，起動するか確認

## python3-devのインストール
netifacesのインストールでエラーが発生するため，python3-devをインストールする  
```sudo apt-get install build-essential libssl-dev libffi-dev python3-dev```

## projectのクローン
任意のディレクトリで，```git clone https://github.com/barley0774/master_system.git```を実行し，projectをクローン  

作成した仮想環境のディレクトリで，```source venv/bin/activate```を実行し，仮想環境を有効化  
projectのディレクトリに移動し，```pip install -r requirements.txt```を実行し，パッケージリストをインストール 

### カテゴリ機能のコメントアウト
カテゴリ機能の実装の仕様上，データベースを作成した場合，カテゴリ機能に関する部分をコメントアウトする必要がある．  
カテゴリ機能のコメントアウトは，ctrl + fで検索バーに「category」と入力して，mitmlearningフォルダ内にあるファイルを探索して，カテゴリ機能に関するコードをmodels.py，admin.py以外コメントアウトする．

### データベース作成
カテゴリ機能のコメントアウト後，```python3 manage.py makemigrations```と```python3 manage.py migration```を実行し，データベースを作成する．  
また，```python3 manage.py createsuperuser```を実行し，スーパーユーザを作成  

スーパユーザ作成後，```python3 manage.py runserver```でサーバを起動するとトップページが確認できる．
次に，```127.0.0.1:8000/admin```とアドレスバーに入力し，管理者画面に遷移する．  
スーパユーザでログインし，カテゴリ機能に用語をいくつか追加する．
追加後，カテゴリ機能のコメントアウトを解除し，```python3 manage.py makemigrations```と```python3 manage.py migration```を実行(Select an optionに1，>>>に1を入力して，データベースの設定を変更する．)

サーバを起動し，メニューバーから用語欄を選択する．用語を適当に追加し，カテゴリ機能が正常に動作するか確認する．
動作の確認後，本システムが正しくインストールされている状態となる．

## 無線LANのアダプタの選択
mitmlearning/mitm/rep_mitm.pyにあるdns_spoof_around関数とsslstrip_around関数の引数を
自身の無線LANアダプタの名前に変更する．これにより，攻撃再現機能を動作させることができる．

以上が本システムのインストール手順です．

#その他
bettercapを攻撃再現機能に使っているので，sslstripやDNS Spoofingが動作しない場合があります．
bettercapの公式HPやGithubの方を確認していただけると幸いです．
攻撃ホストとWebサーバを一緒にしているので，動作が不安定になる場合が多いです．
現実的には，ラズパイを攻撃ホストにして，Webサーバにある機能と切り分ける方が良い気がします．

大学の研究で作成したものなので，至らない点が多数ありますがご了承のほどよろしくお願いいたします。
