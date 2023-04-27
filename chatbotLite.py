import datetime
import webbrowser

def main():
    print ('Type "Hey Chatbot" in order to search.')
    start = input()
    
    if start == "Hey Chatbot" or start == "hey chatbot" or start == "Hey chatbot":
      printMenu()   
    
      while True:
         print('')
         option = input('What can Chatbot do for you?: ')
        
         if (option == "q" or option == "quit" or option == "Quit"):
            return
         elif (option == "Date" or option == "date"):
            date(option)
            continue
         elif (option == "Time" or option == "time"):
            time(option)
            continue
         elif (option == "m" or option == "menu" or option == "Menu"):
            printMenu()
            continue  
         elif (option == "Web" or option == "web"):
            web(option)
            continue 
         else:
            print('Wrong option, try again.')
            continue

def printMenu():
    print('')
    print('MENU')
    print('Date - Chatbot will get todays date from you')
    print('Time - Chatbot will get the current time for you')
    print('Open Webpage - Enter "web" in order to open a webpage')
    # Future plan: print('Reminder - Chatbot will set a reminder for you in Google Calendar')
    print('Quit - Enter q or quit to exit the program')
    print('Menu - Enter m or menu to see the menu again')

def date(menuOption):
   dateToday = datetime.date.today()
   dateFormat = dateToday.strftime("%m/%d/%Y")
   print("Today's date is", dateFormat)

def time(menuOption):
   timeNow = datetime.datetime.now()
   print('The time is', timeNow.strftime("%I:%M %p"))

def web(menuOption):
   site = input('Enter a URL, without the http:// : ')
   webbrowser.open('http://' + site)

main()