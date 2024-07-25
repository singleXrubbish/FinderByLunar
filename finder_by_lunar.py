from lunar_python import Lunar
from lunar_python import Solar
from datetime import datetime


def abort(s: str) -> bool:
    return s == "quit" or s == "q"


def finder():
    date = datetime.today()
    while True:
        input_time = input("请输入丢失物品的时间（例如：2008-08-15 20:30:28）:")
        if abort(input_time):
            return

        lost_date_time = input_time.split(' ')
        if len(lost_date_time) != 2:
            print("日期输入格式有误")
            continue
        lost_date = lost_date_time[0].split('-')
        lost_time = lost_date_time[1].split(':')
        if len(lost_date) != 3 or len(lost_time) != 3:
            print("日期输入格式有误")
            continue

        try:
            date = datetime(year=int(lost_date[0]), month=int(lost_date[1]), day=int(lost_date[2]),
                            hour=int(lost_time[0]), minute=int(lost_time[1]), second=int(lost_time[2]))
            break
        except ValueError:
            print("日期非法")

    solar = Solar.fromDate(date)
    lunar = Lunar.fromSolar(solar)
    info = lunar.toFullString().split(" ")
    lunar_day: str = info[4].split("(")[0][0]
    lunar_hour: str = info[5].split("(")[0][0]

    dir_dic = {
        "甲": "正东",
        "乙": "正南",
        "丙": "西南",
        "丁": "西北",
        "戊": "正北",
        "己": "东南",
        "庚": "正西",
        "辛": "西南",
        "壬": "东北",
        "癸": "东北",
    }

    take_person_dic = {
        "甲": "男人",
        "乙": "女人",
        "丙": "小孩",
        "丁": "亲人",
        "戊": "还在家",
        "己": "男人",
        "庚": "女人",
        "辛": "小孩",
        "壬": "亲人",
        "癸": "还在家",
    }

    distance_dic = {
        "甲": "大概5里",
        "乙": "千里之遥",
        "丙": "大概10里",
        "丁": "大概3里",
        "戊": "就在原地",
        "己": "大概5里",
        "庚": "千里之遥",
        "辛": "大概10里",
        "壬": "大概3里",
        "癸": "就在原地",
    }

    way_idc = {
        "子": "去路旁找",
        "丑": "就在身边",
        "寅": "放弃吧！已落入他人之手，找不到了",
        "卯": "去路旁找",
        "辰": "就在身边",
        "巳": "放弃吧！已落入他人之手，找不到了",
        "午": "去路旁找",
        "未": "就在身边",
        "申": "放弃吧！已落入他人之手，找不到了",
        "酉": "去路旁找",
        "戌": "就在身边",
        "亥": "放弃吧！已落入他人之手，找不到了"
    }

    answer = ""

if __name__ == '__main__':
    finder()
