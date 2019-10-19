import os
import time
import datetime


import schedule

from MysqlHelp import DB
from pcm_8000 import RunScript, RunScript16000
from speech_recognition import RunSpeech, fileslist


def job1():
    print('Job1:每隔10秒执行一次的任务，每次执行2秒')
    print('Job1-startTime:%s' %(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')))
    time.sleep(2)
    print('Job1-endTime:%s' % (datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')))
    print('------------------------------------------------------------------------')

#定时文件转码任务,每隔5s将文件转成pcm8000hz
def fileformatswitcher():
    with DB(host='47.92.33.19',user='root',passwd='1qazxsw2',db='database_fm') as db:
        db.execute("SELECT radio_file_path from fm_t_scan_record WHERE sound_markup IS NULL ORDER BY id DESC limit 500 ")
        filelist = db.fetchall()
        for f in filelist:
            file = os.path.basename(str(f.values()))

            filepath = r"E:/FM_DEVICE_SERVER/public/record/"+file.split("'",1)[0]
            print(filepath)
            wav_pcm8000(filepath)



# 每隔30s,对转码过后的文件进行分类,保存到数据库
def speechrecognition():
    fileDir = r'E:/FM_DEVICE_SERVER/public/pcm8000/'
    allfile = []
    fileslist(fileDir,allfile)
    for name in allfile:
        # print(name,file=fff)
        print(name)
    RunSpeech(allfile)

def wav_pcm8000(self):
    RunScript(filepath)

def wav_pcm16000(self):
    RunScript16000(filepath)







if __name__ == '__main__':
    global filepath
    filepath = ""
    # schedule.every(5).seconds.do(job1)
    schedule.every(5).seconds.do(fileformatswitcher())
    schedule.every(30).seconds.do(speechrecognition())

    while True:
        schedule.run_pending()