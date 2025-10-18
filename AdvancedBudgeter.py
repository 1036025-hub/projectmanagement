budget_file = "budget-data.txt"


def save_record(month_name, category_name, description_text, amount_value):
 file_handle = open(budget_file, "a")
 file_handle.write(month_name + "|" + category_name + "|" + description_text + "|" + str(amount_value) + "\n")
 file_handle.close()
#saves one record at a time

def read_records():
 all_records = []
 try:
  file_handle = open(budget_file, "r")
  for line_text in file_handle:
   parts = line_text.strip().split("|")
   if len(parts) == 4:
    month_name, category_name, description_text, amount_value = parts
    all_records.append((month_name, category_name, description_text, float(amount_value)))
  file_handle.close()
 except:
  pass
 return all_records
#it helps to read all records from the saved file


def add_new_entry():
 print("\nadding new entry")
 month_name = input("month: ")
 category_name = input("category: ")
 description_text = input("description: ")
 amount_value = float(input("amount (+income/-expense): "))
 save_record(month_name, category_name, description_text, amount_value)
 print("saved!\n")
#ask for input to add new entry


def view_month():
 month_to_view = input("month to view: ")
 all_records = read_records()
 month_entries = [entry for entry in all_records if entry[0] == month_to_view]
 if not month_entries:
  print("no records for that month\n")
  return
 total_income = 0
 total_expense = 0
 print("\n---", month_to_view, "---")
 for record in month_entries:
  month_name, category_name, description_text, amount_value = record
  sign_symbol = "+" if amount_value > 0 else "-"
  print(category_name + " | " + description_text + " | " + sign_symbol + str(abs(amount_value)))
  if amount_value > 0: total_income += amount_value
  else: total_expense += abs(amount_value)
 balance_amount = total_income - total_expense
 print("------------------")
 print("income:", total_income, "expense:", total_expense, "balance:", balance_amount, "\n")
#menu item to view month and detals


def view_all():
 all_records = read_records()
 if not all_records:
  print("no data yet\n")
  return
 summary_by_month = {}
 for record in all_records:
  month_name, category_name, description_text, amount_value = record
  if month_name not in summary_by_month: summary_by_month[month_name] = {"income": 0, "expense": 0}
  if amount_value > 0: summary_by_month[month_name]["income"] += amount_value
  else: summary_by_month[month_name]["expense"] += abs(amount_value)
 print("\n--- all months ---")
 for month_name, totals in summary_by_month.items():
  total_income = totals["income"]
  total_expense = totals["expense"]
  balance_amount = total_income - total_expense
  print(month_name, "income:", total_income, "expense:", total_expense, "balance:", balance_amount)
 print("-----------------\n")
#view every month income and expenses in a single list



def clear_all_data():
 confirm = input("delete all records? yes/no: ")
 if confirm.lower() == "yes":
  open(budget_file, "w").close()
  print("all cleared!\n")
 else: print("cancelled\n")
#clear all saved data from the file


# main loop of the program that helps to add multiple entries!
while True:
 print("\n== welcome to the budget tracker made by Abhiii ==")
 print("1. add new entry")
 print("2. view a month")
 print("3. view all months")
 print("4. clear all data")
 print("5. exit")
 choice = input("option: ")
 if choice == "1": add_new_entry()
 elif choice == "2": view_month()
 elif choice == "3": view_all()
 elif choice == "4": clear_all_data()
 elif choice == "5":
  if input("really exit? y/n: ") == "y":
   print("goodbye!")
   break
 else:
  print("invalid choice\n") #wrong input by user
