import asyncio
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

async def handle_echo(reader: asyncio.StreamReader, writer: asyncio.StreamWriter):
    peername = writer.get_extra_info('peername')
    logging.info(f"Accepted connection from {peername}")

    try:
        while True:
            data = await reader.read(1024) 

            if not data:
                logging.info(f"Client {peername} disconnected.")
                break # Client disconnected

            message = data.decode()
            logging.info(f"Received from {peername}: {message.strip()}")

            response = f"Echo from server: {message}".encode()

            writer.write(response)
            await writer.drain() 

    except asyncio.CancelledError:
        logging.warning(f"Connection handler for {peername} cancelled.")
    except Exception as e:
        logging.error(f"Error handling connection {peername}: {e}")
    finally:
        logging.info(f"Closing connection from {peername}")
        writer.close() 
        await writer.wait_closed()


async def main():
    server = await asyncio.start_server(
        handle_echo, '127.0.0.1', 8888
    )

    addrs = ', '.join(str(sock.getsockname()) for sock in server.sockets)
    logging.info(f"Serving on {addrs}")

    async with server:
        await server.serve_forever()

if __name__ == "__main__":
    try:
        # Run the main asyncio event loop
        asyncio.run(main())
    except KeyboardInterrupt:
        logging.info("Server shutting down.")
    except Exception as e:
        logging.critical(f"Unhandled error in main: {e}")