#遍历
import fnmatch
import logging
import os
import time
from time import sleep






def fileslist(path, allfile):
    filelist = os.listdir(path)
    for filename in filelist:
        filepath = os.path.join(path, filename)
        if os.path.isdir(filepath):
            path.dirlist(filepath, allfile)
        elif fnmatch.fnmatch(filepath,'*.wav'):#判断文件格式
            allfile.append(filepath)
            # allfile.append('\n')
        print('*'*40,filepath,'\n')

    return allfile

#音频文件解析
def RunSpeech() :
        code = "speaker-recognition.py -t predict -i "
        codeMid = " -m model.out "
        inputname= 'E:/FM_DEVICE_SERVER/public/pcm8000b/*.wav'
        finishcode = code + inputname + codeMid
        os.system(finishcode)









# 主程序运行
# if __name__ =='__main__':
#     # fff = open("E:\\py\\allfile.txt", 'w+')
#     fileDir = r'D:/PCM'
#     allfile = []
#     fileslist(fileDir,allfile)
#     # for name in allfile:
#     #     # print(name,file=fff)
#     #     print(name)
#     RunSpeech(allfile)