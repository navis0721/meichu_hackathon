import os
import csv
import json

datas = [
    {
        "news_id": 111,
        "title": "新北市立圖書館金石門分館提供免費融合玩具服務",
        "context": "新北市立圖書館特別於金山與石門分館提供免費融合玩具服務，為北海岸的慢飛小天使們提供更完善的學習照顧。"
    },
    {
        "news_id": 111,
        "title": "北海岸偏鄉早療家庭獲得融合玩具資源",
        "context": "金山與石門分館免費提供融合玩具，讓偏鄉早療家庭也能享受到玩具的樂趣，並獲得更完善的學習照顧。"        
    },
    {
        "news_id": 111,
        "title": "新北市立圖書館融合玩具服務多間分館設置",
        "context": "新北市立圖書館共設置有8間融合玩具圖書館，提供多種豐富、經認證的融合玩具，免費供民眾使用。"
    }
]

# with open('output.csv', 'w', newline='') as csvfile:
#         fieldnames = ["news_id", "title", "context"]
#         writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

#         writer.writeheader()  # 写入 CSV 表头

#         # 将标题和短句写入 CSV 文件
#         for data in enumerate(datas):
#             writer.writerow(data)


# 開新檔案
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


# 新增tuple
# with open('output.csv', 'a', newline='') as data_file:
#     csv_writer = csv.writer(data_file)
#     for data in datas:
#       csv_writer.writerow(data.values())
# data_file.close()