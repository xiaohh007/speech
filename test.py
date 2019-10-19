import os
import re

from MysqlHelp import DB

if __name__ == '__main__':
    with DB(host='47.92.33.19',user='root',passwd='1qazxsw2',db='database_fm') as db:
        db.execute("SELECT radio_file_path from fm_t_scan_record WHERE sound_markup IS NULL ORDER BY id DESC limit 100")
        filelist = db.fetchall()
        file = []
        for f in filelist:
            # print(f)
            file = os.path.basename(str(f.values()))
            print(file)
            print(file.split("'",1)[0])
            # url = re.findall('https?://(?:[-\w.]|(?:%[\da-fA-F]{2}))+', str(f.values()))
            # print(url)
