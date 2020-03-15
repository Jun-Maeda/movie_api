import requests
import json

# apiを取得できるURLの取得
url = "https://api.themoviedb.org/3/movie/"
# apiキーの設定と言語を日本語にする設定
set = "?api_key=a382ce65ddfcb96058e463c40a246707&language=ja&page=1"

# idと似たジャンルの一覧を取得する関数
def Similar(num):
    sim_id = num + "/similar"
    set_url = url + sim_id + set
    response = requests.get(set_url)
    back = response.text
    # jsonファイルを辞書に変換する
    jsn = json.loads(back)
    results = jsn["results"]
    return results

# 人気の映画を取得する関数
def Popular():
    set_url = url + "popular" + set
    response = requests.get(set_url)
    back = response.text
    jsn = json.loads(back)

    # タイトルのみ取得する
    # jsonで取得したもののresultsの中にデータがあるのでまずはそこだけを取り出す。
    results = jsn['results']
    return results

def Detail(num):
    set_url = url + num + set
    response = requests.get(set_url)
    back = response.text
    jsn = json.loads(back)
    return jsn




# 人気の映画情報を取得する
# pop = Popular()
# for key in pop:
#     print("タイトル：" + key['title'])
#     print("img：" + key["poster_path"])
#     print("リリース日：" + key["release_date"])

# 似ている映画リスト
# simi = Similar("290859")
# for key in simi:
#     print("タイトル：" + key['title'])
#     print("img：" + key["poster_path"])
#     print("リリース日：" + key["release_date"])
