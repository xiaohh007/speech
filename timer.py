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
        filepathlist = db.execute("SELECT radio_file_path from fm_t_scan_record WHERE sound_markup IS NULL ORDER BY id DESC LIMIT 3000")
    for filepath in filepathlist:

        wav_pcm8000(r'E:\FM_DEVICE_SERVER\public\record/'+os.path.basename(filepath))

# 每隔30s,对转码过后的文件进行分类,保存到数据库
def speechrecognition():
    fileDir = r'D:/PCM'
    allfile = []
    fileslist(fileDir,allfile)
    for name in allfile:
        # print(name,file=fff)
        print(name)
    RunSpeech(allfile)

def wav_pcm8000(self):
    RunScript(self.filepath)

def wav_pcm16000(self):
    RunScript16000(self.filepath)







if __name__ == '__main__':
    schedule.every(5).seconds.do(job1)
    schedule.every(5).seconds.do(fileformatswitcher())
    schedule.every(30).seconds.do(speechrecognition())

    while True:
        schedule.run_pending()