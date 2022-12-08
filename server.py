from os import listdir, makedirs, remove, rename, system
from shutil import rmtree
from time import sleep
import ctypes

import keyboard
import pyautogui as gui
import Pyro4
import requests
from pytube import YouTube


@Pyro4.expose
class Python():
    def runscript(self, script):
        exec(script)

@Pyro4.expose
class MessageBox():
    def show(self, text, title, type):
        ctypes.windll.user32.MessageBoxW(0, text, title, type)

@Pyro4.expose
class CommandExecute():
    def start(self, program : str):
        system(f'start {program}')
        
    def shutdown(self):
        system('shutdown /s /t 0')

@Pyro4.expose
class Keybind():
    def close(self):
        gui.hotkey('alt', 'f4')
        
    def save_close(self):
        gui.hotkey('ctrl', 's')
        gui.hotkey('alt', 'f4')
        
    def close_tab(self):
        gui.hotkey('ctrl', 'w')
    
    def lock(self):
        ctypes.windll.user32.LockWorkStation()
    
    def change_desktop(self, direction : str):
        if direction == 'left':
            gui.hotkey('win', 'ctrl', 'left')
        elif direction == 'right':
            gui.hotkey('win', 'ctrl', 'right')

@Pyro4.expose
class Download():
    def youtube(self, url : str, path: str):
        yt = YouTube(url)
        yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first().download(path)
        
    def raw_file(self, url : str, path : str):
        resp = requests.get(url)
        with open(path, 'wb') as f:
            f.write(resp.content)        
            f.close()

@Pyro4.expose
class Files():
    def delete(self, path : str):
        remove(path)
    
    def delete_folder(self, path : str):
        rmtree(path)
    
    def list(self, path : str = ".\\"):
        return listdir(path)
    
    def create_folder(self, path : str):
        makedirs(path)
    
    def rename(self, old_path : str, new_path : str):
        rename(old_path, new_path)

@Pyro4.expose
class Spy():
    def screenshot(self):
        return gui.screenshot()

Pyro4.Daemon.serveSimple({
    CommandExecute: 'Execute',
    Python: 'Python',
    Keybind: 'Keybind',
    Download: 'Download',
    Files: 'Files',
    Spy: 'Spy',
    MessageBox: "MessageBox"
}, host="localhost", port=3333, ns=False, verbose=True)