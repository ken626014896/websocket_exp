from django.shortcuts import render
from danmu.models import DanmuModel
# Create your views here.
from django.db import connection
from dwebsocket import require_websocket,accept_websocket
def  index(request):

    return  render(request,'danmu/video.html')

@require_websocket
def getDanmu(request):

    # message = request.websocket.wait()

    cursor = connection.cursor()
    for message in request.websocket:
        send_time=message.decode(encoding='utf-8')



        sqlstr="select * from danmu_danmumodel where send_time between %s and %s" % (float(send_time),float(send_time)+0.25)
        cursor.execute(sqlstr)

        raw = cursor.fetchall()


        if(len(raw)>0):

            print('在时间点%s找到%s条弹幕'% (send_time,len(raw)))
            danmuID=raw[0][0]
            danmuText=raw[0][2]
            danmu_data=str(danmuID)+':'+str(danmuText)
            print(danmu_data)

            request.websocket.send(danmu_data.encode(encoding='utf-8'))



