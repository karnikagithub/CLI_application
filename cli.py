"""Command Line Calendar
Functionalities:
 - View the calendar
 - Add an event to the calendar
 - Update an existing event
 - Delete an existing event
 The program should behave in the following way:

Prompt the user to view, add, update, or delete an event on the calendar
Depending on the user's input: view, add, update, or delete an event on the calendar
The program should never terminate unless the user decides to exit
"""
from time import sleep, strftime
from calendar import monthrange

def welcome():
  print("Welcome to Command Line Calendar!")
  name = str(input("What's your name?"))
  print("Hello, ", name, ". It's nice to meet you!", sep="")
  sleep(1.5)
  return


def print_menu():
    # Prints menu options in cmd line.
    print(strftime("%A, %m-%d-%Y %H:%M:%S"))
    print("Menu: ")
    sleep(0.5)
    print("1 - View the calendar")
    sleep(0.5)
    print("2 - Add an event to the calendar")
    sleep(0.5)
    print("3 - Update an existing event")
    sleep(0.5)
    print("4 - Delete an existing event")
    sleep(0.5)
    print("0 - Exit the calendar")
    sleep(0.7)
    return


def get_user_input():
    # Gets user_input. Blocks wrong user_input. Only integers 0-4.
    while True:
        try:
            user_input = int(input("Choose your option: "))
            if user_input > 4 or user_input < 0:
                raise ValueError
            break
        except ValueError:
            print("Should be an integer 0-4.")

    return user_input


def choose_function(user_input, cal):
    # Processes user_input and forwards to proper function.
    if user_input == 0:
        exit_calendar()
    elif user_input == 1:
        view_calendar(cal)
    elif user_input == 2:
        add_event(cal)
    elif user_input == 3:
        update_event(cal)
    elif user_input == 4:
        delete_event(cal)
    return


def exit_calendar():
    # Prints a message and exits the program using exit().
    print("Thank you for using Command Line Calendar!")
    print("Exiting...")
    exit()
    return


def view_calendar(cal):
  if len(cal) == 0:
    print("There are no entries to show.")
    print()
    sleep(1)
  else:
    cal_keys_sorted = sorted(cal)
    for k in cal_keys_sorted:
      print(k, "-", cal[k])
    print()


def add_event(cal):
  print("We need 2 piece of data: date and event name.")
  date_str = get_date_as_string()
  event_name = str(input("Event name: "))
  cal[date_str] = event_name
  print()
  print("Calendar item:", date_str, "-", cal[date_str]) # Prints event and date added.
  print()
  print("Item successfully added to the calendar!")
  sleep(1)
  return


def update_event(cal):
    return


def delete_event(cal):
  view_calendar(cal)
  print("We need to find an item you want to delete.")
  find_calendar_item(cal)


def create_calendar():
  calendar = {}
  return calendar

def get_date_as_string():
  # This function takes user input and makes sure it's in proper format: MM/DD/YYYY.
  while True:
    try:
      y = int(input("Year formatted YYYY: "))
      if str(y) < strftime("%Y"):
        raise ValueError
      break
    except ValueError:
      print("Try again with suggested format. Year must be", strftime("%Y"), "or further.")

  while True:  
    try:
      mo = str(input("Month formatted MM: "))
      if len(mo) > 2 or len(mo) < 2:
        raise ValueError
      if int(mo) > 12 or int(mo) < 1:
        raise ValueError
      if str(y) == strftime("%Y"):
        if str(mo) < strftime("%m"):
          raise ValueError
      break
    except ValueError:
      print("Try again with the format suggested. Month should be within 1-12 range, but not in the past.")

  while True:
    try:
      d = str(input("Day formatted DD: "))
      if len(d) > 2 or len(d) < 2:
        raise ValueError
      if int(d) > monthrange(y,int(mo))[1] or int(d) < 1:
        raise ValueError
      if str(y) == strftime("%Y") and \
         str(mo) == strftime("%m") and \
         str(d) < strftime("%d"):
           raise ValueError
      break
    except ValueError:
      print("Try again with the format suggested. Also number of days has to be in range: 01 -", monthrange(y,int(mo))[1])

  date = str(y) + "/" + str(mo) + "/" + str(d)

  return date

def find_calendar_item(cal):
  print("1 - Find calendar item by date")
  print("2 - Find calendar item by event name")
  # Checks if input is an integer 1-2
  while True:
    try: 
      user_input = int(input("Choose your option: "))
      if (user_input > 2) or (user_input < 1):
        raise ValueError
      break
    except ValueError: 
      print("Choose 1 to find by date or 2 to find by event name.")
    if user_input == 1:
      find_item_by_date(cal)
    if user_input == 2:
      item_name = find_item_by_name(cal)


def find_item_by_name(cal):
  temp_cal = {}
  while True:
    user_input = str(input("What name do you want to find? "))
    # Adding substrings found to temp_cal
    i = 1
    for k in cal:
      if user_input.lower() in str(cal[k]).lower():
        temp_cal[i] = cal[k]
        i += 1
    # If no items found
    if len(list(temp_cal.keys())) == 0:
      print("No items with", user_input, "found. Try again!")
      print()
    else: 
      break

  for k1 in temp_cal:
    print(k1, '-', temp_cal[k1])
  print("0 - It's not on the list")
  while True:
    try:
      user_input2 = int(input("Is the item you are looking for any of these?"))
      if user_input2 < 0 or user_input2 > len(list(temp_cal.keys())):
        raise ValueError
      break
    except ValueError:
      print("Choose from 0-", len(list(temp_cal.keys())))
  if user_input2 == 0:
    print("Okay, let's try another name.")
    print()
    find_item_by_name(cal)
    return
  for key in cal:
    if temp_cal[user_input2] == cal[key]:
      return key

def find_item_by_date(cal):
  return

def calendar_app():
  welcome()
  cal = create_calendar()
  while True:
    print_menu()
    user_input = get_user_input()
    choose_function(user_input, cal)
  return

#calendar_app()
cal = 
print(strftime("%A, %m - %d - %Y"))
welcome()
print_menu()
get_user_input()
choose_function(1,cal)
