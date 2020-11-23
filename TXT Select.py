# -*- coding: UTF-8 -*-

"""

@author:smile

@file:TXT Select.py

@time:2020/04/10

"""

# 文件查找

import re  # 引用re模块
import pandas as pd

result_list = []


def txt_select(s_file, select_txt):

    global result_list
    source_file = open(s_file, "r")
    content = source_file.read()

    print("\n文件内容为：\n", content)  # 输出文件内容

    re_list = re.findall(select_txt, content)  # re.findall()返回的是一个列表
    count = len(re_list)

    print("\nre.list()的返回值: ", re_list)
    print("共有{}个%s\n".format(count) % select_txt)

    return re_list


def list_s(excel_File, num):

    df = pd.DataFrame(pd.read_excel(excel_File))
    txt = str(df.iloc[num])
    txt = txt[6:23]
    print('查找信息为:', txt)
    return txt


if __name__ == '__main__':

    for num in range(0, 300):

        try:
            excel = './list.xlsx'
            txt = list_s(excel, num)

            file = './source.txt'
            select = txt
            re_list = txt_select(file, select)

            result_list.append(re_list)
            print(result_list, '\n\n')

            num = num + 1

        except:
            print('本次运行出现Bug，请调试后重试！')

    print('\n\n\n\n\n', result_list)
    print(len(result_list))

    pass
