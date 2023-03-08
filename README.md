# Mrp

> 基于python异步的TCP反向代理
>
> author: Mz1
>
> email: mzi_mzi@163.com

今天在思考如何把内网socket服务直接转发到本机的问题，说白了就是个反向代理的问题，网上一堆人写的乱七八糟，搞的相当复杂，就自己写了个tcp反向代理。

环境：
python3.7+

## usage:

```bash
> Mrp.py [your_port] [romote_addr] [remote_port]
```

