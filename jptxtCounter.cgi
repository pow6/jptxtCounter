#!/usr/local/bin/python
# -*- coding: utf-8 -*-
html='''Content-Type: text/html

<html>
  <head>
    <meta charset="UTF-8">
    <title>日本語だけカウントするツール【ノベルゲー文字数】</title>
    <meta content="日本語だけを簡単にカウントするツールです。ノベルゲーノベルゲーのスクリプトからセリフの分量を概算するのに便利です" name="description">
    
    <link rel="stylesheet" href="jptxtCounter/jptxtCounter.css">
    <link rel="shortcut icon" href="jptxtCounter/jptxtCounter_icon.png">
    <script type="text/javascript" src="jptxtCounter/jptxtCounter.js"></script>
  </head>
  <body>
    <hr color="#FF8000" size="5">
    <h1>日本語だけカウントするツール ver1.0</h1>
    <p style="text-align: right">製作者：Arutaka　ホームページ：
      <a href="https://pow6.net" target="_blank">https://pow6.net</a>
    </p>
    <hr size="3">
    <div class="intro">
    <p>　日本語だけを簡単にカウントします。
      <br>　ノベルゲーの開発でスクリプトの開発をしながらセリフも作っている人向け。
      <br>　とりあえず日本語のセリフとかをば～～！と数えるのに使えます。要望があればホームページのお問い合わせからどうぞ！
    </p>
    </div>
    <div class="box">使い方：
      <br>　１．変換したい文章を入力
      <br>　２．『日本語をカウント』をクリック
      <br>　※コメント行を無視したい→例外行文字に改行区切りで入力する
    </div>
      <form method="post" action="jptxtCounter.cgi">
        <p><button type="submit" class="square_btn">日本語をカウント</button></p>
        <p><textarea class="ef" name="escapeWord" id="escapeWord" cols="15" rows="3" placeholder="(任意)例外行文字"></textarea></p>
        <p><textarea class="ef" name="originText" id="originText" cols="100" rows="12" placeholder="カウントしたい文章を入力"></textarea></p>
        <span class="focus_bg"></span>
      </form>
  </body>
</html>
'''

result='''
<br>【文字数】
<br>日本語文字数  ：%s文字
<br>日本語バイト数：%s
<br>全文字数　　  ：%s文字
<br>【分量目安】
<br>読了目安（400文字/分）：%s分
<br>読了目安（600文字/分）：%s分
<br>
<br>【検出日本語文字列】
<br>%s
'''

import sys
sys.path.append('/home/pow6/www/python/Python-3.6.2/Lib')
import cgi
import re

form = cgi.FieldStorage()
org_text = form.getvalue("originText")
esc_word = form.getvalue("escapeWord")

#入力が何もない時のエラー処理（←エラーじゃなく例外処理的な）
if not org_text:
    print(html)
else:
    if esc_word:
        esc_word = esc_word.splitlines()
    org_list = org_text.splitlines()
    detected_jp = []
    japanese = re.compile('[ぁ-ゖァ-ヺｦ-ﾟ一-龥]')
    for text in org_list:
        if esc_word:
          if any(text.startswith(esc) for esc in esc_word):
              continue
        text = japanese.findall(text)
        text = ''.join(text)
        detected_jp.append(text)

    jp_sentence = '<br>'.join(detected_jp)
    detected_jp = str(''.join(detected_jp)).decode('utf-8')
    jp_words = len(detected_jp)
    jp_bytes = round(len(detected_jp) / 2 , 2)
    if jp_bytes > 1000:
        jp_bytes = str(jp_bytes) + "B (" + str(round(jp_bytes / 1000, 2)) + "kB)"
    else:
        jp_bytes = str(jp_bytes) + "B"


    jp_read400 = round(len(detected_jp) / 400, 2)
    jp_read600 = round(len(detected_jp) / 600, 2)
    all_words = len(org_text.decode('utf-8'))

    print(html)
    print(result % (jp_words, jp_bytes, all_words, jp_read400, jp_read600, jp_sentence))







