"""
날짜 : 2020/07/22
이름 : 김나연
내용 : 파이썬 Hadoop 실습하기
"""
import shutil
import schedule
import time
from pywebhdfs.webhdfs import PyWebHdfsClient as hadoop


def copy_file():
    # hadoop 접속
    hdfs = hadoop(host='192.168.100.101', port='50070', user_name='root')

    # Local /home/bigdata/naver/naver-20-xx-xx 를 하둡 /naver/ 복사
    shutil.copytree(src='/home/bigdata/naver/naver-20-xx-xx', dst='/naver/')
    shutil.move(src='/home/bigdata/naver/naver-20-xx-xx', dst='/naver/')

    # Local /home/bigdata/naver/naver-20-xx-xx 를 삭제
    try:
        shutil.rmtree('/home/bigdata/naver/naver-20-xx-xx')
    except OSError as e:
        print('Error')


schedule.every().day.at("00:10").do(copy_file())
