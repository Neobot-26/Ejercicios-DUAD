import csv

def read_csv_file(file_path):
  num_register=0
  head_list=[]
  with open(file_path, 'r', encoding='utf-8') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
      if num_register==0:
        head_list=row
      else:
        for index in range(len(head_list)):
          print(f"{head_list[index].capitalize()}: {row[index]}")
        print(" ")
      num_register+=1

def main():
  path='categories.csv' 
  read_csv_file(path)

#main
main()