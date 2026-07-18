import csv
list_data1=[]
list_data2=[]
data_movement=[]


class CategoryManager:
    def __init__(self, file_path='categories.csv'):
        self.file_path = file_path

    def read_categories(self):
        self.list_data_categories = []
        self.list_data_color = []

        with open(self.file_path, 'r', encoding='utf-8') as csvfile:
            reader = csv.reader(csvfile)

            # Read Header of csv file
            next(reader, None)

            for row in reader:
                if len(row) >= 2:
                    self.list_data_categories.append(row[0])
                    self.list_data_color.append(row[1])
        return self.list_data_categories, self.list_data_color

    def write_category(self, new_data):
        with open(self.file_path, "a", newline="", encoding="utf-8") as csv_file:
            writer = csv.writer(csv_file)
            writer.writerow(new_data)

    def get_categories(self):
        categories, colors = self.read_categories()
        return categories, colors
    

class MovementManager:
    def __init__(self, path='Gestor.csv'):
        self.path = path

    def read_movements(self):
        with open(self.path, newline="", encoding="utf-8") as csv_file:
            lector = csv.reader(csv_file)
            next(lector, None)  # Prevent error if file is empty
            data_movement = list(lector)
            return data_movement

    def write_movements(self, new_data_to_movements):
        with open(self.path, "a", newline="", encoding="utf-8") as csv_file:
            new_writer = csv.writer(csv_file)
            new_writer.writerow(new_data_to_movements)

def verify_data(data_to_be_reviewed):
  manager = CategoryManager()
  valid=0
  list_data1,list_data2=manager.get_categories()
  if data_empty(data_to_be_reviewed):
     for category in list_data1:
        if category==data_to_be_reviewed:
          valid=1
  return valid

def data_empty(data_to_verify):
  data_null=1
  if data_to_verify=="":
    data_null=0
  return data_null

def update_table(window, data, categories):
  try:
      window["TABLE"].update(values=data)
      tree = window["TABLE"].Widget
      for tag, color in categories.items():
        tree.tag_configure(tag, foreground=color)
      items = tree.get_children()
      for index, line_data in enumerate(data):
        category = line_data[3].lower()
        if category in categories:
          tree.item(items[index], tags=(category,))
        else:
          tree.item(items[index], tags=("unknown",))
  except ValueError:
      return False, "There is not data for specified range of dates"

def list_categories(data1,data2):
  list_merged = []
  for index_list in range(len(data1)):
    element1 = data1[index_list]
    element2 = data2[index_list]
    new_raw = [element1,element2]
    list_merged.append(new_raw)
  return list_merged

def update_table_categories(window, data, categories):
  window["TABLE"].update(values=data)
  tree = categories["TABLE"].Widget
  # Create a tag for each unique color
  unique_colors = set(fila[1] for fila in data)
  for color in unique_colors:
    tree.tag_configure(color, foreground=color)
  # Apply the respective color to each raw
  items = tree.get_children()
  for index, data_raw in enumerate(data):
    color = data_raw[1]
    tree.item(items[index], tags=(color,))
