import os
try:
  import seldiscord
except:
  os.system('pip install -U git+https://github.com/h0nde/sel-requests.git')
  os.system('pip install -U git+https://github.com/h0nde/sel-discord.git')
import termcolor
import itertools
import json
import threading
import requests
import random
import time
import string
import base64
import names

statuslis = ['vibin', 'i love her..', 'shes my world..', '❤️', '😐', 'dm me please', 'hiiiii']

firstlist = ["Super", "Retarded", "Great", "Sexy", "Vegan", "Brave", 'X' "Shy", "Cool", 'YOUTUBE', 'YT', 'TTV', 'Twitch' "Poor", "Rich", "Fast", "Gummy", "Yummy", "Masked", "Unusual", "American", "Bisexual", "MLG", "Mlg", "lil", "Lil", "Bro", "Fortnite", "Red", "Ball", "Simp", ".", "$", "!", "al", "ban", "funny", 'epic', 'boi', 'bark', 'dy', 'rd', 'by', 'ac', 'icon', 'joes', 'linus', 'python', 'snake', 'liquid', 'pro', 'metro', 'nic', 'acier', 'ace', 'Nut', 'Ice', 'PS', 'pup', 'BRO', 'RAY', 'system', 'tim', 'theo', 'void', 'yellow', 'skia', 'Festive', 'Why', 'XD', 'homo', 'HA','Beauty','Twig','Cindy Lou Who','Tomcat','Stud','Loosetooth','Harry Potter','Rabbit','Gummi Bear','Tank','Fun Dip','Coke Zero','Raisin','Daria','Cowboy','Chump','Dragonfly','Headlights','Bossy','Big Nasty','Tough Guy','Duckling','Buckeye','Amour','Fatty','Smirk','Mini Me','Autumn','Cheesestick','Amigo','Salt','Diesel','Doctor','Foxy','Swiss Miss','Bumblebee','Midge','Captain','Diet Coke','Music Man','Belch','C-Dawg','Beast','Princess','Buck','Lovely','Prego','Freak','Bunny Rabbit','Carrot','Heisenberg','Cello','Homer','Coach','Cumulus','Gummy Pop','Winnie','Turkey','Bambino','Bubbles','Dorito','Captain Crunch','Pixie Stick','Filly Fally','Backbone','Silly Sally','Pinata','Buzz','Peppa Pig','Halfling','Hubby','Crumbles','Cutie Pie','Tootsie','Twiggy','Dummy','Cookie Dough','Muscles','Oompa Loompa','Chewbacca','Mini Skirt','Bumpkin','Boo Bug','Baby Maker','Cutie','Piglet','Piggy','Dragon','Bean','Beetle','Dimples','Mimi','Bug','Silly Gilly','Rapunzel','Admiral','Brown Sugar','Ringo','Amiga','Nerd','Guy','Junior','Cuddles','Twizzler','Biffle','Lefty','Ginger','Hot Sauce','Pookie','Fiesta','Fifi','Shrinkwrap','Tater','Fun Size','Baldie','Chili','Teeny','Bubba','Redbull','Chubs','Short Shorts','Mouse','Bebe','Dum Dum','Dino','Sugar','Fattykins','Bridge','Dottie','Creep','Herp Derp','Baby Bird','Cruella','Peppermint','Buttercup','Smoochie','Lover','Weirdo','Snoopy','Dulce','Con','Dirty Harry','Brutus','Weiner','Donuts','Braniac','Skinny Minny','Goose','Matey','Cottonball','Candycane','Chuckles','Grease','Barbie','Queenie','Papito','Boo Bear''Rosebud','Lil Mama','Dot','Bud','Honeybun','Figgy','Pork Chop','Angel','Skinny Jeans','Hulk','Miss Piggy','Lion','General','Frauline','Chickie','Senior','Giggles','Marge','Lil Girl','Gordo','Shorty']
secondlist = ["Coder", "Vegan", "Man", "Hacker", "Horse", "Bear", 'lol', 'X', 'famous', '!!!', '   ', 'isnot', 'me', 'help', 'FN', 'MINECRAFT', 'minecraft', 'fortnite', 'PUBG', 'rust', 'CSGO', 'csgo', ' hi there', ' dm me!', ''"Goat", "Goblin", "Learner", "Killer", "Woman", "Programmer", "Spy", "Stalker", "Spooderman", "Carrot", "Goat", "Quickscoper", "Quickscoper", "C#", "lol", 'funny', 'dead', 'TV', 'epic', '23', '656', '1234', '124', '1202', '🎃', '0', 'vie', 'via', 'cier', 'virtual', 'smh', 'pain', 'depress', 'sub', 'YT', 'DOE', ' Water', 'lis', 'hi', ' !', 's', 'vs', 'FUNNY', 'meme', 'guy', 'man', 'nigga', 'black']

os.system('color')
output_file = open("tokens.txt", "a")

req = requests.Session()

useragents = ['Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36', 'Mozilla/5.0 (iPad; U; CPU iPhone OS 3_2 like Mac OS X; en-us) AppleWebKit/531.21.10 (KHTML, like Gecko) Version/4.0.4 Mobile/7B314 Safari/531.21.10', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36', 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.193 Safari/537.36']

avatars = []
imagestoencode = []

def getDirectory():   
  mypath = os.getcwd()

  path = rf"{mypath}\Avatars"
  dirs = os.listdir( path )
  for fileme in dirs:
    imagestoencode.append(fileme)
  return mypath

with open('config.json','r+', encoding='utf-8') as f:
  config = json.load(f)

threads = config['threads']
serverinvite = config['discordserverinvite']
usernamestartwith = config['usernamestartwith']
accountpassword = config['accountpassword']

with open("proxies.txt", encoding="UTF-8", errors="ignore") as f:
  proxies = f.read().splitlines()
  proxy_iter = itertools.cycle(proxies)

def changeProfile(token, proxy):
  pathto = getDirectory()
  with open(f'{pathto}\Avatars\{random.choice(imagestoencode)}', "rb") as image_file:
    encoded_string = base64.b64encode(image_file.read())
    
  newstr = encoded_string.decode('utf-8')
  headers = {
    "user-agent": (random.choice(useragents)),
    "authorization": token
  }
  data = {
    "avatar": f'data:image/png;base64,{newstr}'
  }
  r = requests.patch('https://discord.com/api/v8/users/@me', headers=headers, json=data)
  print(r.text)
  print(r.status_code)

def noramlizeName(token, proxy):
  firstme = random.choice(firstlist)
  secondme = random.choice(secondlist)
  headers = {
    "user-agent": (random.choice(useragents)),
    "authorization": token
  }
  data = {
    "username": f"{firstme}{secondme}"
  }
  r = requests.patch('https://discord.com/api/v8/users/@me', headers=headers, json=data, proxies=proxy)
  if r.status_code == 200:
    print('Successfully updated avatar')
  else:
    print(f'Failed to update avatar. Account most likely has a password attached. {r.status_code}')

def setPassword(token, proxy):
  data = {
    "username": f"{usernamestartwith}_{random.randint(0,999)}",
    "password": accountpassword
  }
  headers = {
    "user-agent": (random.choice(useragents)),
    "authorization": token
  }
  r = requests.patch('https://discord.com/api/v8/users/@me', json=data, headers=headers, proxies=proxy)
  if r.status_code == 200:
    print(f'Successfully set password {accountpassword}')
    return accountpassword
  else:
    print('Account is banned or is locked.')

def statusSet(token, proxy):
  statustoset = random.choice(statuslis)
  headers = {
    "user-agent": (random.choice(useragents)),
    "authorization": token,
    'content-type': 'application/json'
  }
  data = {
    'custom_status': {'text': statustoset}
  }
  r = requests.patch('https://discord.com/api/v8/users/@me/settings', proxies=proxy, json=data, headers=headers)
  if r.status_code == 200:
    print('Successfully changed status')
def workerOnline(token, proxy):
  randkey = random.randint(1,3)
  print(randkey)
  if randkey == 1:
    data = {
      "status": "online"
    }
  elif randkey == 2:
    data = {
      "status": "dnd"
    }
  elif randkey == 3:
    data = {
      "status": "idle"
    }
  while True:
    onlineStatus(data, token, proxy)
    time.sleep(10)
def onlineStatus(dataarg, token, proxy):
  headers = {
    "user-agent": (random.choice(useragents)),
    'content-type': 'application/json',
    "authorization": token
  }
  r = requests.patch('https://discord.com/api/v8/users/@me/settings', proxies=proxy, json=dataarg, headers=headers)
  if r.status_code == 200:
    print('Successfully set online')
  print(r.text)
def sendemailVerify(email, password, name, domain, name2, token, proxy):
  data = {
    "email": email,
    "password": accountpassword
  }
def save_token(token):
  print(token)
  output_file.write("%s\n" % token)
  output_file.flush()

class Createjoin(threading.Thread):
    def __init__(self):
      super().__init__()
    
    def do_task(self):
      setuser = f'{usernamestartwith}_{random.randint(0,999)}'
      proxy = "http://%s" % next(proxy_iter)
      with seldiscord.Session(random.choice(useragents), proxy) as dsc:
        dsc.register(
          username=f"{usernamestartwith}_{chr(random.randint(0,999))}",
          invite=serverinvite)
        save_token(dsc.token)
        print(termcolor.colored(f'Successfully created account {setuser}', color='green'))
        
    def run(self):
      while True:
        try:
          self.do_task()
        except Exception as err:
          print(termcolor.colored(f"Worker error: {err} {type(err)}", color='red'))

class CreateAccount(threading.Thread):
    def __init__(self):
      super().__init__()
    
    def do_task(self):
      setuser = f'{usernamestartwith}_{random.randint(0,999)}'
      proxy = "http://%s" % next(proxy_iter)
      with seldiscord.Session(random.choice(useragents), proxy) as dsc:
        dsc.register(
          username=f"{usernamestartwith}_{chr(random.randint(0,999))}")
        save_token(dsc.token)
        print(termcolor.colored(f'Successfully created account {setuser}'))
        
    def run(self):
      while True:
        try:
          self.do_task()
        except Exception as err:
          print(termcolor.colored(f"Worker error: {err} {type(err)}", color='red'))

def workerNoramlize(token, proxy):
  changeProfile(token, proxy)
  noramlizeName(token, proxy)

class createNoramlize(threading.Thread):
    def __init__(self):
      super().__init__()
    
    def do_task(self):
      setuser = f'{random.choice(firstlist)}{random.choice(secondlist)}'
      proxy = "http://%s" % next(proxy_iter)
      with seldiscord.Session(random.choice(useragents), proxy) as dsc:
        dsc.refresh_client_uuid()
        dsc.setup()
        dsc.register(
          username=f"{setuser}",
          invite=serverinvite
        )
        dsc.gateway()
        save_token(dsc.token)
      print(termcolor.colored(f'Successfully created account {setuser}', color='green'))
      changeProfile(dsc.token, proxy)
        
    def run(self):
      while True:
        try:
          self.do_task()
        except KeyError:
          print(termcolor.colored('A captcha was given when attempting to create an account. Retrying.', color='yellow'))
          pass
        except:
          pass

print('''
____ ____ ____ ____ ___ ____ ____ 
|    |__/ |___ |__|  |  |  | |__/ 
|___ |  \ |___ |  |  |  |__| |  \ 

[1] Create discord accounts
[2] Create accounts and join a discord server
[3] Create accounts with real profile pictures and names
[4] Set online and random status\n''')
choice = input('Choice: ')

if "1" in choice:
  for _ in range(int(threads)):
    CreateAccount().start()

if "2" in choice:
  for _ in range(int(threads)):
    Createjoin().start()
  
if "3" in choice:
  for _ in range(int(threads)):
    createNoramlize().start()

if "4" in choice:
  with open('tokens.txt','r+', encoding='utf-8') as f:
	  logins = f.read().splitlines()
  for login in logins:
    proxy = {
      "https": "https://" + next(proxy_iter)
    }
    threading.Thread(target=workerOnline, args=[login, proxy]).start()

if "5" in choice:
  with open('tokens.txt','r+', encoding='utf-8') as f:
	  logins = f.read().splitlines()
  for login in logins:
    proxy = {
      "https": "https://" + next(proxy_iter)
    }
    threading.Thread(target=setPassword, args=[login, proxy]).start()
