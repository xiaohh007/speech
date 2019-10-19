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


def RunScript(filepath) :
    print("runscript_pcm8000"+filepath)
    datetime = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
    # 设置ffmpeg命令行格式
    code = "ffmpeg -i "
    codeMid = " -ac 1 -ar 8000 -y "

    outputname= "E:/FM_DEVICE_SERVER/public/pcm8000/"+os.path.basename(filepath)
    print("outputname"+os.path.basename(filepath))
    print("outputpath"+outputname)
    if os.path.exists(outputname):
        # 执行ffmpeg命令
        finishcode = code + filepath + codeMid +outputname
        os.system(finishcode)
        print(datetime+"file format conversion:"+filepath)
    else:
        filepath = "http://sh.illegalfm.com:4881/record/"+os.path.basename(outputname)
        with DB(host='47.92.33.19',user='root',passwd='1qazxsw2',db='database_fm') as db:
            db.execute("UPDATE fm_t_scan_record SET sound_markup = 'Exception' WHERE radio_file_path = '{}'".format(filepath))

def RunScript16000(filepath) :

        datetime = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
        # 设置ffmpeg命令行格式
        code = "ffmpeg -i "
        codeMid = " -ac 1 -ar 16000 -y "

        outputname= "E:/FM_DEVICE_SERVER/public/pcm16000/"+os.path.basename(filepath)

        # 执行ffmpeg命令
        finishcode = code + filepath + codeMid +outputname
        os.system(finishcode)
        print(datetime+"file format conversion:"+filepath)


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