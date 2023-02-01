import smtplib
import os
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from email.utils import formatdate
# import subprocess

# os.path.dirname(os.path.abspath(__file__)) -> /home/shiota/document/mitmproject/mitmlearning/email
filepath = os.path.dirname(os.path.abspath(__file__)) + "/file/000690266.pdf"
filename = os.path.basename(filepath)

# メール情報の設定
from_email = ""

# メールの内容を変える関数
# 0でなりすまし被害体験メール、1で対策方法提示メール
def mail_content(flag):
    if flag == 0:
        return impersonation_message()
    else:
        return counter_message()

# 訓練用メールの件名と本文
def impersonation_message():
    mail_title = '訓練用メール(なりすまし被害体験)'
    message = '''
    これは訓練用のメールです。
    ご担当者様
    いつもお世話になっております。〇〇〇の佐藤です。
    先日はお忙しい中ご足労いただき、誠にありがとうございます。
    先日承りました資料をお送りさせていただきます。
    お忙しいところ大変恐縮ですが、ご確認のほどよろしくお願いいたします。
    ##############################################
    メールアドレスとパスワードが流出すると、このようななりすましのメールが取引先などに送信される可能性があります。
    悪意のある第三者は、過去の送信履歴を確認して、あたかもあなたであるかのように振る舞います。
    メールを受け取った人物も普段の文章、言葉遣いと何ら変わりがないので、あなただと信じて添付したファイルを開いてしまうでしょう。
    添付したファイルにウイルスが混入していた場合、会社の機密情報や顧客の連絡先、個人情報が流出する恐れがあります。
    このような被害に合わないためにも、ログインが必要なサイトでは、HTTPS通信の確認と正しいURLかの確認、信頼できる通信環境から送信するようにしましょう。
    ##############################################
    '''
    return mail_title, message

def counter_message():
    mail_title = '訓練用メール(対策方法送付)'
    message = '''
    これは訓練用のメールです。
    最低限、身につけておくべき知識等をまとめている公開された資料のURLを記載します。
    今回演習していただいた内容はあくまで体験です。
    実際の被害にあった場合、自分自身だけでなく周りの人にも影響を及ぼす危険性があります。
    自分のことだからと言って、何も考えずに無線LANを利用しないようにしましょう。
    今回演習した危険性に対する対策をしっかり身につけるようにしましょう。
    ・総務省：Wi-Fi利用者向け簡易マニュアル(令和2年5月版)
    https://www.soumu.go.jp/main_content/000690266.pdf
    ・絶対やっとけ！無料Wi-Fi利用時のセキュリティ対策6選！乗っ取りや詐欺に巻き込まれないために
    https://mixhost.jp/vpn-column/free-wi-fi-security-measures/
    ・これだけはやっておきたい！「無線LAN情報セキュリティ3つの約束」
    https://www.gov-online.go.jp/useful/article/201303/1.html
    '''
    return mail_title, message

def send_email(to_email, flag):
    # メール情報の設定
    from_email = ""
    mail_title, message = mail_content(flag)

    # MIMEオブジェクトでメールを作成
    msg = MIMEText(message, 'html')
    msg = MIMEMultipart()
    msg['Subject'] = mail_title
    msg['To'] = to_email
    msg['From'] = from_email
    msg['Date'] = formatdate()
    msg.attach(MIMEText(message))

    with open(filepath, "rb") as f:
        mf = MIMEApplication(f.read())
    mf.add_header("Content-Disposition", "attachment", filename=filename)
    msg.attach(mf)

    # サーバを指定してメールを送信する
    smtp_host = '##############'
    smtp_port = '##############'
    smtp_password = '###########'

    server = smtplib.SMTP(smtp_host, smtp_port)
    server.starttls()
    server.login(from_email, smtp_password)
    server.send_message(msg)
    server.quit()

    print("Eメールを送信しました。")

# print(os.path.dirname(os.path.abspath(__file__)) )