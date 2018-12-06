from django.shortcuts import render
from danmu.models import DanmuModel
import logging
# Create your views here.
from django.db import connection
from dwebsocket import require_websocket,accept_websocket

logger = logging.getLogger(__name__)

def  index(request):

    return  render(request,'danmu/video2.html')

@require_websocket
def getDanmu(request):

    # message = request.websocket.wait()

    cursor = connection.cursor()
    if request.is_websocket():

        for message in request.websocket:
            if(message is None):

                print('客户端断开')
                break
            else:
                try:
                    message_data=message.decode(encoding='utf-8')


                    if message_data[0]=='g':
                        send_time=message_data[2:]

                        sqlstr="select * from danmu_danmumodel where send_time_float between %s and %s" % (float(send_time),float(send_time)+0.25)
                        cursor.execute(sqlstr)

                        raw = cursor.fetchall()


                        if(len(raw)>0):

                            print('在时间点%s找到%s条弹幕'% (send_time,len(raw)))
                            danmuID=raw[0][0]
                            danmuText=raw[0][2]
                            danmu_data=str(danmuID)+':'+str(danmuText)
                            print(danmu_data)

                            request.websocket.send(danmu_data.encode(encoding='utf-8'))

                    elif message_data[0]=='a':
                        data_list=message_data[2:].split(':')
                        send_time=data_list[1]
                        danmuText=data_list[0]
                        DanmuModel.objects.get_or_create(name='null',message=danmuText,send_time_float=float(send_time))

                        sqlstr = "select * from danmu_danmumodel where send_time_float == %s" % (float(send_time))
                        cursor.execute(sqlstr)

                        raw = cursor.fetchall()
                        danmuID = raw[0][0]
                        danmuText = raw[0][2]
                        danmu_data = str(danmuID) + ':' + str(danmuText)
                        print(danmu_data)

                        request.websocket.send(danmu_data.encode(encoding='utf-8'))
                except Exception as e:
                     logger.error(e)