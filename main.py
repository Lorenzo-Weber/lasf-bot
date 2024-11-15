import json
import time
from datetime import datetime
from proxy import Proxy
from data.API import run
from message import Message
from bot import send

failed = {}

if __name__ == "__main__":
    while True:

        # Obtém a lista de proxies e insere cada um no objeto gerenciador de proxies
        proxies = []
        sender = []
        run()
        with open('data/data.json', 'r') as f:
            data = json.load(f)
        proxies = [Proxy(line) for line in data]  

        # Reseta a lista de falhas se um proxy falhado voltar a ficar online
        for proxy in proxies:
            if proxy.id in failed and proxy.online:
                timeStamp = datetime.now().strftime("%H:%M:%S")
                with open('log.txt', 'a') as log:
                    log.write(f'Proxy {proxy.id} / {proxy.region} {proxy.name} turned on at {timeStamp}\n')
                del failed[proxy.id]  

        # Insere novos proxies falhados na lista de falhas
        for proxy in proxies:
            if not proxy.online:
                if proxy.id not in failed:
                    failed[proxy.id] = {'count': 1}
                else:
                    failed[proxy.id]['count'] += 1

                if failed[proxy.id]['count'] >= 2:
                    sender.append(Message(proxy))
                    failed[proxy.id]['count'] = 0

                # Registra no log o proxy que falhou
                timeStamp = datetime.now().strftime("%d/%m  %H:%M:%S")
                with open('log.txt', 'a') as log:
                    log.write(f'Proxy {proxy.id} / {proxy.region} {proxy.name} failed at {timeStamp}\n')

        # Envia a mensagem sobre o proxy falhado
        for s in sender:
            region = f'PROXY {s.region}'
            sent = send(region, s.__str__())
            timeStamp = datetime.now().strftime("%d/%m  %H:%M:%S")
            with open('log.txt', 'a') as log:
                if sent: 
                    log.write(f"Message sent to {s.region} {s.name} at {timeStamp}\n")
                else:
                    log.write(f"Message failed to {s.region} {s.name} at {timeStamp}\n")

        time.sleep(450)
