import csv

def verification_csv_file(file_path):
  error=0
  try:
    with open(file_path,"r",encoding='utf-8')as csvfile:
      reader = csv.reader(csvfile)
  except FileNotFoundError as e:
    print(f"Error [FileNotFoundError]: Unable to find file CSV. Details:{e}")
    error=1
  return error

def write_csv_filedata(file_path,list_of_header, data_list):
  with open(file_path, 'w', encoding='utf-8', newline='' ) as file:
    writer = csv.DictWriter(file,fieldnames=list_of_header)
    writer.writeheader()
    writer.writerows(data_list)

def read_csv_file(file_path):
  students_list=[]
  with open(file_path, 'r', encoding='utf-8') as csvfile:
    reader = csv.DictReader(csvfile)
    for row_info in reader:
      students_list.append(row_info)
  return students_list







