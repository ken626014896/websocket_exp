from django.shortcuts import render
from dwebsocket import require_websocket,accept_websocket
# Create your views here.



def home(request):
    return render(request, 'exp/01.html')

@require_websocket
def echo_once(request):
    #两种接受客户端信息的方法
    message = request.websocket.wait()
    for a in range(0,10) :

     request.websocket.send(message)
    # request.websocket.send(mes.encode(encoding='utf-8'))