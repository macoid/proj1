import random
import string
import time
from datetime import datetime, timedelta
import re
def random_writer(start_time):
  write_till = start_time + timedelta(minutes=1)
  run_id = 'writer_' + str(start_time)
  file1 = run_id + '_1.txt'
  file2 = run_id + '_2.txt'
  print('Creating the files for current run and writing data')
  with open(file1, 'w') as file1, open(file2, 'w') as file2:
    while datetime.now() < write_till:
      randomizer = random.choice(['CDS','not_CDS'])
    
      
      if randomizer == "not_CDS":
          not_cds_string = ''.join(random.sample(string.ascii_uppercase,7))
          file1.write(not_cds_string + '\n')
          file2.write(not_cds_string + '\n')
          #print(''.join(random.sample(string.ascii_uppercase,7)))
      else:
          cds_string = randomizer
          file1.write(cds_string + '\n')
          file2.write(cds_string + '\n')
          #print(randomizer)
  return run_id

def reader(reader):
  pattern = 'CDS'
  match_count = 0
  lines = 0
  for line in reader:
      match = re.findall(pattern, line)   
      if match:
        match_count += len(match)
        lines += 1
  #print(match_count)
  
  return match_count

def file_watcher(run_id):
  
  file1 = run_id + '_1.txt'
  file2 = run_id + '_2.txt'
  
  with open(file1,'r') as reader1, open(file2, 'r') as reader2:
    match_count1 = reader(reader1)
    match_count2 = reader(reader2)
  with open('search_results.log', 'a') as writer:
    writer.write(file1 + ' - ' + str(match_count1) + '\n')
    writer.write(file2 + ' - ' + str(match_count2) + '\n')

def main():
  

  start_time = datetime.now()
  run_id = random_writer(start_time)
  print('Starting the watcher and counting the record count...')
  file_watcher(run_id)
  print('log file has been appended with recent run data')
  print('Sleeping..process will start in another one hour again')
  time.sleep(3600)

main()
