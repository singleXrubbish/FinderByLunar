from typing import Set, Dict, Union, Any, List
import pip
import re
from datetime import datetime
pip.main(["install", "lunar_python"])
from lunar_python import Lunar
from lunar_python import Solar


def remove_duplicate_spaces(s):
    return re.sub(r'\s+', ' ', s).strip()


def abort(s: str) -> bool:
    return s == "quit" or s == "q"


def finder():
    while True:
        input_time = input("请输入丢失物品的时间（例如：2008-08-15 20:30:28，精确到小时即可）:\n")
        if abort(input_time):
            return

        lost_date_time = remove_duplicate_spaces(input_time).split(' ')
        if len(lost_date_time) != 2:
            print("日期输入格式有误")
            continue
        lost_date = lost_date_time[0].split('-')
        if ':' in lost_date_time[1]:
            lost_time: str = lost_date_time[1].split(':')[0]
        else:
            lost_time = lost_date_time[1]

        if len(lost_date) != 3:
            print("日期输入格式有误")
            continue

        # noinspection PyBroadException
        try:
            hour = int(lost_time)
        except BaseException:
            print("日期输入格式有误")
            continue

        try:
            date = datetime(year=int(lost_date[0]), month=int(lost_date[1]), day=int(lost_date[2]), hour=int(lost_time))
        except ValueError:
            print("日期非法")
            continue

        solar = Solar.fromDate(date)
        lunar = Lunar.fromSolar(solar)
        day_gan = lunar.getDayGan()
        time_zhi = lunar.getTimeZhi()
        duty = lunar.getZhiXing()

        # 甲、乙、丙、丁、戊、己、庚、辛、壬、癸
        # 子、丑、寅、卯、辰、巳、午、未、申、酉、戌、亥
        # 建、除、满、平、定、执、破、危、成、收、开、闭
        unlucky_list = [{"甲", "己", "申", "酉"},
                        {"乙", "庚", "午", "未"},
                        {"丙", "辛", "辰", "巳"},
                        {"丁", "壬", "寅", "卯"},
                        {"戊", "癸", "子", "丑"}]
        could_found = True
        for unlucky in unlucky_list:
            if day_gan in unlucky and time_zhi in unlucky:
                print("放弃吧，找不回来了。正所谓，旧的不去新的不来!")
                could_found = False
                break

        if could_found:
            easy = {"满", "成", "定", "执"}
            far = {"危", "收"}
            nearly = {"开", "除"}
            hopeless = {"建", "平", "破", "闭"}

            direction: Dict[Union[str, Any], Union[str, Any]] = {
                "建": "正西",
                "除": "正西",
                "满": "东北",
                "平": "正东",
                "定": "西南",
                "执": "东南",
                "破": "西北",
                "危": "正北",
                "成": "西北",
                "收": "正东",
                "开": "正南",
                "闭": "正南"
            }

            place: Dict[Union[str, Any], Union[str, Any]] = {
                "子": "在树林里或者木头多的地方",
                "丑": "在树林里或者木头多的地方",
                "寅": "在山坡上面或者斜着的地方",
                "卯": "在山坡上面或者斜着的地方",
                "辰": "问一下身边的亲朋好友",
                "巳": "问一下身边的亲朋好友",
                "午": "在桌椅等平面上",
                "未": "在桌椅等平面上",
                "申": "去路边找找",
                "酉": "去路边找找",
                "戌": "悬在半空，比如口袋里",
                "亥": "悬在半空，比如口袋里"
            }

            answer = ""
            if duty in easy:
                answer += "不必担心，很可能东西自己就回来了。\n"
            elif duty in far:
                answer += "能找到，但是要费点功夫，丢到比较远的地方了。\n"
            elif duty in nearly:
                answer += "问题不大，丢的不远。\n"
            elif duty in hopeless:
                answer += "很难找回来了。\n"

            answer += "往{}找，{}。".format(direction[duty], place[time_zhi])
            print(answer)


if __name__ == '__main__':
    finder()
