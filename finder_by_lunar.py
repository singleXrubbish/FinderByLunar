from lunar_python import Lunar
from lunar_python import Solar
from datetime import datetime
import openai
import requests


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
    info = lunar.toFullString()

    # print(info)
    lost_thing = input("请输入丢失的物品：")
    if abort(lost_thing):
        return


if __name__ == '__main__':
    finder()
