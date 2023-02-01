import smtplib
import os
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from email.utils import formatdate
# import subprocess

# os.path.dirname(os.path.abspath(__file__)) -> /home/shiota/document/mitmproject/mitmlearning/test_program
filepath = os.path.dirname(os.path.abspath(__file__)) + "/file/000690266.pdf"
filename = os.path.basename(filepath)

# メール情報の設定
from_email = "ml.test0152@gmail.com"
# to_email = '2133340422k@kindai.ac.jp' 

def mail_content(flag):
    if flag == 0:
        return training_message()
    else:
        return counter_message()

# 訓練用メールの件名と本文
def training_message():
    mail_title = '訓練用メール(なりすまし被害体験)'
    message = '''
    これは訓練用のメールです。

    ご担当者様
    いつもお世話になっております。〇〇〇の田中です。

    先日はお忙しい中ご足労いただき、誠にありがとうございます。
    先日承りました資料をお送りさせていただきます。

    お忙しいところ大変恐縮ですが、ご確認のほどよろしくお願いいたします。

    ---------------------------------------------------------
    [訓練メール作成者]
    近畿大学大学院総合理工学研究科エレクトロニクス系工学専攻
    ネットワーク研究室
    塩田　晃平　（Kohei Shiota)
    2133340422k@kindai.ac.jp
    ---------------------------------------------------------
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

    ---------------------------------------------------------
    [訓練メール作成者]
    近畿大学大学院総合理工学研究科エレクトロニクス系工学専攻
    ネットワーク研究室
    塩田　晃平　（Kohei Shiota)
    2133340422k@kindai.ac.jp
    ---------------------------------------------------------
    '''
    return mail_title, message

def send_emai(to_email, flag):
    # メール情報の設定
    from_email = "ml.test0152@gmail.com"
    # to_email = '2133340422k@kindai.ac.jp'
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
    smtp_host = 'smtp.gmail.com'
    smtp_port = 587
    smtp_password = 'csttuxjswcrlhjvv'

    server = smtplib.SMTP(smtp_host, smtp_port)
    server.starttls()
    server.login(from_email, smtp_password)
    server.send_message(msg)
    server.quit()

    print("Eメールを送信しました。")

send_emai('2133340422k@kindai.ac.jp',0)
send_emai('2133340422k@kindai.ac.jp',1)

# #PDFファイルを開く
# pdf_pro = subprocess.run(["evince",filepath],stdout=subprocess.PIPE)
# time.sleep(2)

# #PDFファイルを終了
# pdf_pro.kill()
# time.sleep(1)