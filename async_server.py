import asyncio
import uvloop
from loguru import logger

logger.add("server.log", rotation="100 MB", retention="10 days")

async def handle_echo(reader: asyncio.StreamReader, writer: asyncio.StreamWriter):
    peername = writer.get_extra_info('peername')
    logger.info(f"Accepted connection from {peername}")

    try:
        while True:
            data = await reader.read(1024) 

            if not data:
                logger.info(f"Client {peername} disconnected.")
                break

            message = data.decode()
            logger.info(f"Received from {peername}: {message.strip()}")

            response = f"Echo from server: {message}".encode()

            writer.write(response)
            await writer.drain() 

    except asyncio.CancelledError:
        logger.warning(f"Connection handler for {peername} cancelled.")
    except Exception as e:
        logger.error(f"Error handling connection {peername}: {e}")
    finally:
        logger.info(f"Closing connection from {peername}")
        writer.close() 
        await writer.wait_closed()


async def main():
    server = await asyncio.start_server(
        handle_echo, '127.0.0.1', 8888
    )

    addrs = ', '.join(str(sock.getsockname()) for sock in server.sockets)
    logger.info(f"Serving on {addrs}")

    async with server:
        await server.serve_forever()

if __name__ == "__main__":
    uvloop.install()
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        logger.info("Server shutting down.")
    except Exception as e:
        logger.critical(f"Unhandled error in main: {e}")