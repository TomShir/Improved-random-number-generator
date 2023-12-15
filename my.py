#Creating random number generator 
import logging 
from colorama import Fore as Font 
import time 
import sys 
import tqdm 
import os 
import random 
from readchar import readkey,key
run_condition='True'
ranges=list(range(1,100,1))
colors=[Font.GREEN,Font.RED,Font.BLUE,Font.YELLOW,Font.RESET]
#Creating a function that loops over a subscriptable sequence and prints it horizontally
def loop_over(text_color,sequence,delay_time):
    for text in sequence:
        sys.stdout.flush()
        time.sleep(delay_time)
        sys.stdout.write(f'{text_color}{text}')
    else:
        print(f'{colors[-1]}')
        
def log_error_messages(text_message):
    #Creating a logging object which will inevitably log error messages to a log file 
    error_logger=logging.getLogger('error_logger')
    file_handler=logging.FileHandler('ERROR.log')
    myformat=logging.Formatter('%(asctime)s-%(name)s-%(message)s')
    file_handler.setFormatter(myformat)
    error_logger.addHandler(file_handler)
    loop_over(text_color=colors[1],sequence=text_message,delay_time=0.01)
    time.sleep(1)
    error_logger.error(f'{text_message}')
#Creating a global function that can log the randomly generated numbers,displayed in an output stream to a log file 
def log_random_numbers():
    random_number_logger=logging.getLogger('random_number_logger')
    random_number_logger.setLevel(logging.INFO)
    filehandler=logging.FileHandler('random_numbers.txt')
    format=logging.Formatter('%(asctime)s-%(name)s-%(message)s') 
    filehandler.setFormatter(format)
    random_number_logger.addHandler(filehandler)
    random_number_logger.info(f'{random_number_generator}')
program_title=f'Random Number Generator Version:{sys.version[0:6]}'
progress_bar=tqdm.tqdm(program_title,desc='Loading program',colour='CYAN',ncols=100) 
for num in progress_bar:
    time.sleep(0.1)
else:
    time.sleep(1)
    os.system('cls')
    time.sleep(1)
    loop_over(text_color=colors[0],sequence=program_title,delay_time=0.01)
    time.sleep(1)
    os.system('cls')
    time.sleep(1)
    start=int(input('start:'))
    time.sleep(1)
    stop=int(input('stop:'))
try:
  while True:
        random_number_generator=str(random.randrange(start,stop+1,1))
        loop_over(text_color=random.choice(colors[:-1]),sequence=random_number_generator,delay_time=0.01)
except ValueError:
        log_error_messages(text_message='ValueError:An inappropiate value was entered')