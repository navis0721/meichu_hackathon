# -*- coding: utf-8 -*-
import os
import csv
import json
import requests
# from flask import Flask, request, render_template
from flask import request, redirect, url_for, Flask, render_template, session, send_from_directory

app = Flask(__name__)
Data = None

@app.route('/dummies')
def formPage():
    return render_template('dummies.html')


@app.route('/submit', methods=['GET','POST'])
def submit():
    if request.method == 'POST':
        news_id = request.form['news_id']
        context = request.form['context']
    else:
        news_id = request.args.get('news_id')
        context = request.args.get('context')


# news_id = 1760711
# context = "\r\n▲+慢飛天使最棒暑假禮物！新北市圖金山石門分館提供融合玩具服務。（圖／新北市立圖書館提供）\r\n記者郭世賢／新北報導\r\n暑假到來！新北市立圖書館特別於金山與石門分館提供北海岸首創的免費融合玩具服務，除了讓北海岸的慢飛小天使，可以透過遊戲的方式訓練治療，也提供地方居民視障、聽障、自閉症、多重障礙、銀髮、親子等六種需求的融合玩具服務，獲得更完善的學習照顧。\r\n石門早療師陳老師表示，早療對慢飛天使相當重要，以繪本搭配玩具，可以進行更有效的教學；但融合玩具對許多偏鄉的早療家庭來說，是不易獲得的資源。現在金山及石門分館免費提供融合玩具，搭配臺大醫院提供的專業早期療育書單，相信可以讓北海岸的慢飛小天使們，獲得更完善的學習照顧。\r\n金山及石門分館蕭千惠主任表示，偏鄉早期療育的學習資源較為缺乏，為了讓特殊需求的兒童也能享受到玩具的樂趣，金山與石門分館取得認證，並推出融合玩具服務，搭配早療教材及相關書籍，免費提供家長及老師預約使用，讓北海岸的慢飛天使們，可以藉由閱讀結合遊戲的方式，增加多重感官的刺激，也可以透過共融體驗，幫助他們趕上成長的腳步。\r\n新北市立圖書館目前於新莊、鶯歌、土城親子、淡水水碓、淡水竹圍、蘆洲兒童親子、金山與石門分館共設置有8間融合玩具圖書館，均提供多種豐富、經認證的融合玩具，免費讓民眾使用，歡迎有需要的民眾多加利用。相關服務資訊請至新北市立圖書館網站：http://www.library.ntpc.gov.tw查詢，洽詢電話：金山分館02-2498-4714、石門分館02-2638-1202。\r\n「美麗最大的祕密」\r\n二手票券豐富你的生活++++++++++++"


    OPENAI_API_KEY = "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"  

    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {OPENAI_API_KEY}"
    }


    body = {
        "model": "gpt-3.5-turbo",
        "messages": [
            {
                "role": "system",
                "content": "你是一個新聞編輯，善於擷取內文的重點，生成使用於懶人包的短句"},
            {
                "role": "user",
                "content": f"""
                請用以下輸入資料生成出幾個適合此新聞懶人包的標題(約十字以內)，與其對應的短句或條列式，並用json檔的形式顯示:
                "news_id": {news_id}
                "新聞內文": {context}

                其中，輸入的欄位有"news_id", "新聞內文"，
                你要輸出的json檔的欄位名稱分別有"news_id", "title", "context"，
                例如:
                [
                    {{
                        "news_id": "111",
                        "title": "咖啡打折",
                        "context": "國內棒球賽開打，推出咖啡折價優惠"
                    }},
                    {{
                        "news_id": "111",
                        "title": "買一送一",
                        "context": "10/10前，全家單品咖啡買一送一"
                    }},
                    {{
                        "news_id": "111",
                        "title": "全家優惠",
                        "context": "因應棒球賽，全家推出了其他優惠，如霜淇淋第二個6折"
                    }}
                ]
                如果是整理成多個條列式重點的話，盡量把它拆成每一列csv表格只有三項，例如:
                [
                    {{
                        "news_id": "111",
                        "title": "減肥要成功，避免8個錯誤習慣1",
                        "context": "1. 避免一成不變的運動習慣
                                    2. 不要忽略重量訓練
                                    3. 運動後不要有補償心理；"
                    }},
                    {{
                        "news_id": "111",
                        "title": "減肥要成功，避免8個錯誤習慣2",
                        "context": 4. 不要忽略能運動的時間 
                                   5. 不要因為太累放棄運動
                                   6. 不要攝取過多蛋白質；"
                    }},
                    {{
                        "news_id": "111",
                        "title": "減肥要成功，避免8個錯誤習慣3",
                        "context": "7. 不要以果汁取代早餐
                                    8. 睡眠不足易多吃"
                    }}
                ]
                生成的行數盡量控制在五個以內
                """
            },
        ]
    }


    url = "https://api.openai.com/v1/chat/completions"

    res = requests.post(url, headers=headers, json=body)
    resDict = json.loads(res.text)

    # print(res.text)

    # 将结果写入 CSV 文件
    datas = resDict["choices"][0]["message"]["content"]
    datas = json.loads(datas)
    print(datas)

    data_file = open('output.csv', 'w', newline='', encoding='utf-8')
    csv_writer = csv.writer(data_file)
    count = 0
    for data in datas:
        if count == 0:
            header = data.keys()
            csv_writer.writerow(header)
            count += 1
        csv_writer.writerow(data.values())
    data_file.close()


    return render_template('tables.html', datas=datas)


@app.route('/images', methods=['GET','POST'])
def form_image():
    return render_template('images.html')



if __name__ == '__main__':
    app.run(host="localhost", port=5000, debug=True)