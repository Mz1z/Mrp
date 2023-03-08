import asyncio
import sys


# 转发客户端到服务器的流量
async def trans_c2s(reader, r_writer):
	while not reader.at_eof():
		data = await reader.read(256)
		r_writer.write(data)
		await r_writer.drain()
	r_writer.close()
		
# 转发服务器到客户端的流量
async def trans_s2c(r_reader, writer):
	while not r_reader.at_eof():
		r_data = await r_reader.read(256)
		writer.write(r_data)
		await writer.drain()
	writer.close()

async def handle(reader, writer):
	addr = writer.get_extra_info('peername')
	print(f'> Receive connection: {addr}!')
	
	# 启动反向代理连接
	r_reader, r_writer = await asyncio.open_connection(r_addr, r_port)
	
	ret = await asyncio.gather(
		trans_c2s(reader, r_writer),
		trans_s2c(r_reader, writer)
	)

	print('> Close connection: {addr} !')
	
# 主服务器进程
async def main():
	server = await asyncio.start_server(
		handle, "0.0.0.0", port)
		
	addr = server.sockets[0].getsockname()
	print(f'Serving on {addr}')
	
	async with server:
		await server.serve_forever()
		


if __name__ == "__main__":
	if len(sys.argv) < 4:
		print('> usage: Mrp.py [your_port] [romote_addr] [remote_port]')
		exit(1)
	port = int(sys.argv[1])
	r_addr = sys.argv[2]
	r_port = int(sys.argv[3])
	asyncio.run(main())

