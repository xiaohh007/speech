import os
import time
import datetime


import schedule

from MysqlHelp import DB
from pcm_8000 import RunScript, RunScript16000
from speech_recognition import RunSpeech, fileslist

class timed_task:
    def job1(self):
        print('Job1:每隔10秒执行一次的任务，每次执行2秒')
        print('Job1-startTime:%s' %(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')))
        time.sleep(2)
        print('Job1-endTime:%s' % (datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')))
        print('------------------------------------------------------------------------')

    #定时文件转码任务,每隔5s将文件转成pcm8000hz
    def fileformatswitcher(self):
        with DB(host='47.92.33.19',user='root',passwd='1qazxsw2',db='database_fm') as db:
            db.execute("SELECT radio_file_path from fm_t_scan_record WHERE sound_markup IS NULL ORDER BY id DESC limit 10 ")
            filelist = db.fetchall()
            for f in filelist:
                file = os.path.basename(str(f.values()))

                filepath = startpath+file.split("'",1)[0]
                print(filepath)
                timed_task.wav_pcm8000(filepath)



    # 每隔30s,对转码过后的文件进行分类,保存到数据库
    def speechrecognition(self):
        # fileDir = r'E:/FM_DEVICE_SERVER/public/pcm8000/'
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
    startpath = r"E:/FM_DEVICE_SERVER/public/record/"
    fileDir = r'E:/FM_DEVICE_SERVER/public/pcm8000/'
    # schedule.every(5).seconds.do(job1)
    schedule.every(5).seconds.do(timed_task.fileformatswitcher(startpath))
    schedule.every(30).seconds.do(timed_task.speechrecognition(fileDir))

    while True:
        schedule.run_pending()