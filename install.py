import os
import sys
from time import sleep
from quo import clear
from quo.prompt import Prompt
from quo.text import Text
from src.outlook import *
from src.system import *

session = Prompt()
class tool:
  @classmethod
  def install(self):
    while True:
      system=sys()
      clear() 
      logo.ins_tnc()
      session = Prompt(bottom_toolbar=Text(' <b>Install</b> <style bg="red">sashay</style>'), placeholder=Text(' <gray>([y/n])</gray>'))
      inp= session.prompt("Do you want to install sashay?:")
      if inp=="y" or inp=="Y" or inp=="Yes" or inp=="yes":
        clear() 
        logo.installing()
        if system.sudo is not None:
          #require root permission
          if os.path.exists(system.conf_dir+"/sashay"):
            pass
          else:
            os.system(system.sudo+" mkdir "+system.conf_dir+"/sashay")
          os.system(system.sudo+" cp -r src assets sashay.py "+system.conf_dir+"/sashay")
          os.system(system.sudo+" cp -r assets/sashay "+system.bin)
          os.system(system.sudo+" cp -r assets/sshy "+system.bin)
          os.system(system.sudo+" chmod +x "+system.bin+"/sashay")
          os.system(system.sudo+" chmod +x "+system.bin+"/sshy")
          os.system("cd .. && "+system.sudo+" rm -rf sashay")
          if os.path.exists(system.bin+"/sashay") and os.path.exists(system.conf_dir+"/sashay"):
            clear() 
            logo.ins_sc()
            tmp = session.prompt("|>>")
           # tmp=input("\033[1;36m ##> \033[00m")
            break
          else:
            clear()
            logo.not_ins()
            tmp = session.prompt("|>>")
         #   tmp=input("\033[1;36m ##> \033[00m")
            break
        else:
          if os.path.exists(system.conf_dir+"/sashay"):
            pass
          else:
            os.system("mkdir "+system.conf_dir+"/sashay")
          os.system("cp -r src assets sashay.py "+system.conf_dir+"/sashay")
          os.system("cp -r assets/sashay "+system.bin)
          os.system("cp -r assets/sshy "+system.bin)
          os.system("chmod +x "+system.bin+"/sashay")
          os.system("chmod +x "+system.bin+"/sshy")
          os.system("cd .. && rm -rf sashay")
          if os.path.exists(system.bin+"/sashay") and os.path.exists(system.conf_dir+"/sashay"):
            clear()
            logo.ins_sc()
            tmp = session.prompt("|>>")
           # tmp=input("\033[1;36m ##> \033[00m")
            break
          else:
            clear() 
            logo.not_ins()
            tmp=session.prompt("|>>")
        #    tmp=input("\033[1;36m ##> \033[00m")
            break
      else:
        break

if __name__=="__main__":
  try:
    tool.install()
  except KeyboardInterrupt:
    clear()
    logo.exit()
