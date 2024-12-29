# pip install pypresence
from pypresence import Presence  # советую ещё поизучать этот модуль, ведь там много интересного: https://qwertyquerty.github.io/pypresence/html/index.html
import time

client_id = "1234567890"  # здесь вы задаёте айди, который берёте отсюда: https://discord.com/developers/applications
rpc = Presence(client_id)
rpc.connect()

try:
    while True:
        rpc.update(
            details="ваш текст",  # надпись "играет в ..."
            large_image="id_photo",  # иконка программы, которая задаётся здесь: https://discord.com/developers/applications/айди/rich-presence/assets
            large_text="ваш текст",  # какая будет надпись при наведении на иконку
            start=time.time()
        )
        time.sleep(15000)  # тайм слип чтобы время активности не сбрасывалось
except KeyboardInterrupt:
    print("закрываюсь...")
    rpc.close()
