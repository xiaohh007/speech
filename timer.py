import os
import time
import datetime


import schedule

from MysqlHelp import DB
from pcm_8000 import RunScript, RunScript16000
from speech_recognition import RunSpeech, fileslist


# def job1(self):
#     print('Job1:每隔10秒执行一次的任务，每次执行2秒')
#     print('Job1-startTime:%s' %(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')))
#     time.sleep(2)
#     print('Job1-endTime:%s' % (datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')))
#     print('------------------------------------------------------------------------')
#定时文件转码任务,每隔5s将文件转成pcm8000hz
def fileformatswitcher():
    startpath = r"E:/FM_DEVICE_SERVER/public/record/"
    with DB(host='47.92.33.19',user='root',passwd='1qazxsw2',db='database_fm') as db:
        db.execute("SELECT id,radio_file_path,sound_markup from fm_t_scan_record "+
                   " WHERE sound_markup IS NULL and radio_file_path != 'undefined' and id % 2 = 1 "+
                   " ORDER BY id DESC limit 100")
        filelist = db.fetchall()
        for f in filelist:
            file = os.path.basename(str(f.values()))
            filepath = startpath+str(file.split("'",1)[0])
            print("fileformatswitcher"+filepath)
            wav_pcm8000(filepath)


def fileformatswitch():
    startpath = r"E:/FM_DEVICE_SERVER/public/record/"
    with DB(host='47.92.33.19',user='root',passwd='1qazxsw2',db='database_fm') as db:
        db.execute("SELECT id,radio_file_path,recognition,sound_markup FROM (SELECT id,radio_file_path,recognition,sound_markup from fm_t_scan_record "+
        " WHERE recognition = '未识别' and id % 2 = 1 ORDER BY id DESC limit 100) temp WHERE temp.sound_markup = 'human' OR temp.sound_markup = 'music'")
        filelist = db.fetchall()
        for f in filelist:
            file = os.path.basename(str(f.values()))
            filepath = startpath+str(file.split("'",1)[0])
            print("fileformatswitcher"+filepath)
            wav_pcm16000(filepath)

# 每隔30s,对转码过后的文件进行分类,保存到数据库
def speechrecognition():
    # fileDir = r'E:/FM_DEVICE_SERVER/public/pcm8000/'
    fileDir = r'E:/FM_DEVICE_SERVER/public/pcm8000b/'
    allfile = []
    fileslist(fileDir,allfile)
    for name in allfile:
        # print(name,file=fff)
        print(name)
    RunSpeech()


def wav_pcm8000(filepath):
    print("wav_8000"+filepath)
    RunScript(filepath)


def wav_pcm16000(filepath):
    print("wav_16000"+filepath)
    RunScript16000(filepath)







if __name__ == '__main__':


    # schedule.every(5).seconds.do(job1)
    schedule.every(29).seconds.do(fileformatswitcher)
    schedule.every(34).seconds.do(fileformatswitch)
    schedule.every(61).seconds.do(speechrecognition)

    while True:
        schedule.run_pending()