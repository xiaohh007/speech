import logging
import os		# 获取目录下的所有文件列表
import fnmatch	# 文件格式筛选模块，筛选指定格式文件


#访问转码目录,遍历文件
import time
from os import path


# def dirlist(path, allfile):
#     filelist = os.listdir(path)
#     for filename in filelist:
#         filepath = os.path.join(path, filename)
#         if os.path.isdir(filepath):
#             path.dirlist(filepath, allfile)
#         elif fnmatch.fnmatch(filepath,'*.wav'):#判断文件格式
#             allfile.append(filepath)
#             # allfile.append('\n')
#         print('*'*40,filepath,'\n')
#
#     return allfile

#格式转换
from MysqlHelp import DB


def RunScript(filepath):
    datetime = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
    # 设置ffmpeg命令行格式
    code = "ffmpeg -i "
    codeMid = " -ac 1 -ar 8000 -y "
    outputname= "E:/FM_DEVICE_SERVER/public/pcm8000/"+os.path.basename(filepath)
    if os.path.exists(filepath) and os.path.getsize(filepath) > 30000:
        # 执行ffmpeg命令
        print("开始执行转码任务,将wav文件的编码格式转换成pcm8000hz")
        finishcode = code + filepath + codeMid +outputname
        os.system(finishcode)
    else:
        print("文件不存在,直接更新为异常状态")
        filepath = "http://sh.illegalfm.com:4881/record/"+os.path.basename(outputname)
        with DB(host='47.92.33.19',user='root',passwd='1qazxsw2',db='database_fm') as db:
            db.execute("UPDATE fm_t_scan_record SET sound_markup = 'Error' WHERE radio_file_path = '{}'".format(filepath))

def RunScript16000(filepath) :
        datetime = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
        # 设置ffmpeg命令行格式
        code = "ffmpeg -i "
        codeMid = " -ac 1 -ar 16000 -y "
        outputname= "E:/FM_DEVICE_SERVER/public/pcm16000/"+os.path.basename(filepath)

        # 执行ffmpeg命令
        if os.path.exists(filepath) and os.path.getsize(filepath) > 30000:
            print("开始执行转码任务,将wav文件的编码格式转换成pcm16000hz")
            finishcode = code + filepath + codeMid +outputname
            os.system(finishcode)
            print(datetime+"file format conversion:"+filepath)
        else:
            print("文件错误!")


# 主程序运行
# if __name__ =='__main__':
#     # fff = open("E:\\py\\allfile.txt", 'w+')
#     fileDir = r'D:\record_wav'
#     allfile = []
#     dirlist(fileDir,allfile)
#     for name in allfile:
#         # print(name,file=fff)
#         print(name)
#     RunScript(allfile)