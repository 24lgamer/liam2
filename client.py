import Pyro4
from PIL import Image
import asyncio

liam_ip = "10.4.52.59"
ip = "localhost"
port = 3333

execute = Pyro4.core.Proxy(f'PYRO:Execute@{ip}:{port}')
keybind = Pyro4.core.Proxy(f'PYRO:Keybind@{ip}:{port}')
download = Pyro4.core.Proxy(f'PYRO:Download@{ip}:{port}')
files = Pyro4.core.Proxy(f'PYRO:Files@{ip}:{port}')
spy = Pyro4.core.Proxy(f'PYRO:Spy@{ip}:{port}')
python = Pyro4.core.Proxy(f'PYRO:Python@{ip}:{port}')
msgbox = Pyro4.core.Proxy(f'PYRO:MessageBox@{ip}:{port}')

print(f'Connected to {ip}:{port}!')

while True:
    cmd = input('>> ')
    if cmd == 'exit':
        break
    elif cmd == 'start':
        program = input(">> >> ")
        execute.start(program)
    elif cmd == 'shutdown':
        execute.shutdown()
    elif cmd == 'close':
        keybind.close()
    elif cmd == 'saveClose':
        keybind.save_close()
    elif cmd == 'closeTab':
        keybind.close_tab()
    elif cmd == 'lock':
        keybind.lock()
    elif cmd == 'changeDesk':
        direc = input(">> >> ")
        keybind.change_desktop(direc)
    elif cmd == 'dyt':
        url = input(">> >> ")
        path = input(">> >> >> ")
        download.youtube(url, path)
    elif cmd == 'rawFile':
        url = input(">> >> ")
        path = input(">> >> >> ")
        try:
            download.raw_file(url, path)
        except Exception as e:
            print(f'Error: {e}')
    elif cmd == 'listFiles':
        print(f'Files in current directory: {files.list()}')
    elif cmd == 'delete':
        file = input(">> >> ")
        files.delete(file)
    elif cmd == 'deleteDir':
        direct = input(">> >> ")
        files.delete_folder(direct)
    elif cmd == 'createDir':
        direct = input(">> >> ")
        files.create_folder(direct)
    elif cmd == 'rename':
        old = input(">> >> ")
        new = input(">> >> >> ")
        files.rename(old, new)
    elif cmd == 'screenshot':
        with Image.open(spy.screenshot()) as img:
            img.show()
    elif cmd == 'python':
        script = input(">> >> ")
        python.runscript(script)
    elif cmd == 'message':
        text = input(">> >> ")
        title = input(">> >> ")
        type = input(">> >> ")
        
        msgbox.show(text, title, int(type))
    else:
        print(f'"{cmd}" is not a recognized command.')