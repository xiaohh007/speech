import os
import re

from MysqlHelp import DB

if __name__ == '__main__':
        filepath = 'F:/wav/noise/'
        pathDir = os.listdir(filepath)
        for allDir in pathDir:
            child = os.path.join('%s%s' % (filepath, allDir))
            print(child)# .decode('gbk')是解决中文显示乱码问题
            code = "ffmpeg -i "
            codeMid = " -ac 1 -ar 8000 -y "
            outputname= "F:/wav/noise/pcm/"+"n"+os.path.basename(child)
            finishcode = code + child + codeMid +outputname
            os.system(finishcode)
