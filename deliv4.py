#Project Deliverable 3
#Jacob Dzikowski
#COMPSCI132 Spring 2022
#the scheduler
import pickle
from os.path import exists

#info contains default schedule information and file debugging/loading
class info:
  #default file value
  schedule={"Monday" : ["bread", 6, "pm"],"Tuesday" : ["dairy", 3, "am"],"Thursday" : ["grocery", 4, "pm"],"Saturday" : ["dairy", 7,"pm"],}
  #filename is where the schedule is stored. changes to variable will affect entire program.
  filename = "schedule1.pkl"
  #unit test 1, checks file conditions. if file does not exist will create new with default info
  if exists(filename):
    print("Schedule file exists. Opening...")
    try:
      with open(filename, 'rb') as f:
        schedule = pickle.load(f)
    except EOFError:
      print("Error recieved, the schedule file is likely empty...")
      print("Would you like to overwrite the file with the default data?")
      print("Enter 1 to overwrite file.")
      print("Enter 2 to quit program.")
      #unit test 2, checks if answer is correct
      while True:
        try:
          i = int(input("Enter your selection: "))
          if i!=1 and i!=2:
            raise ValueError
        except ValueError:
          print("Please enter a valid number.")
        else:
          break
      if i==1:
        with open(filename, 'wb') as f:
          pickle.dump(schedule, f)
        print("File overwritten.\n")
      else:
        print("Quitting now.")
        quit()
      
    print("Successfully Opened!")
  else:
    print('Schedule file does not exist. Creating now...')
    with open(filename, 'wb') as f:
      pickle.dump(schedule, f)
      print('File Created!')

#contains code for all main user choices
class options:
  #makes the keys in a dictionary lowercasefor comparison purposes
    def getLower():
      thisList = list(info.schedule.keys())
      thisList = [x.lower() for x in thisList]
      return thisList
        
  #get and display the schedule NEATLY!!!
    def showSchedule():
        print('\n-------------------------------------------------------------')
        #unit test 3
        if len(info.schedule) == 0:
          print("The schedule is empty! Please add a time.")
          return
        for key in info.schedule:
          print("There is a", info.schedule[key][0],"delivery", key, "at", info.schedule[key][1], info.schedule[key][2])
        print('-------------------------------------------------------------\n')
    
    def removeObject():
        #unit test 4
        if len(info.schedule) == 0:
          print("The schedule is empty! Please add a time.")
          return
        #show schedule to remind user of what is in it
        options.showSchedule()
        remove = str(input("Enter the day you would like to remove: "))

        #Unit Test 5, checks if value exists
        while remove not in info.schedule:
            print("Didn't find", remove, "in schedule! Please enter a correct value.")
            remove = str(input("Enter the day you would like to remove: "))
        #get user confirmation
        print("Are you sure you want to remove", remove, "from the schedule?")
        confirm = int(input(" Enter 1 for yes, 2 for no: "))
        if confirm==1:
            print(remove, "has been deleted!\n")
            #remove from the item list
            del info.schedule[remove]
        else:
            print("Deletion cancelled.")
        options.showSchedule()
    
  #modifies an existing day
    def modObject():
        #unit test 6
        if len(info.schedule) == 0:
          print("The schedule is empty! Please add a time.")
          return
        #show schedule to remind user of what is in it
        options.showSchedule()
        #set variable
        confirm = 1
        mod = str(input("Enter the day you would like to modify: "))

        #run test to see if entered value exists (UTest 7)
        while mod not in info.schedule:
            print("Didn't find", mod, "in schedule! Please enter a correct value.")
            mod = str(input("Enter the day you would like to modify: "))
        #clarify
        print("You have chosen to modify the delivery on",mod)

        #Loop until user is done modifying
        while confirm!=2:
            print("\nThere is a", info.schedule[mod][0],"delivery", mod, "at", info.schedule[mod][1], info.schedule[mod][2])
            #user chooses modification type
            print(" Enter 1 to modify the delivery time.")
            print(" Enter 2 to modify the delivery type (bread, dairy etc.)")
            print(" Enter 3 to cancel modification.")
            #Unit Test 8
            modType = int(input("Enter your choice: "))
            while modType!=1 and modType!=2 and modType!=3:
                print("\nThe value you entered is not a valid choice.")
                print(" Enter 1 to modify the delivery time.")
                print(" Enter 2 to modify the delivery type (bread, dairy etc.)")
                print(" Enter 3 to end modification.")
                modType = int(input("Enter your choice: "))
            if modType==1:
                #unit test 9
                while True:
                    try:
                        newHour = int(input("Enter the hour for delivery (1,2,3,4 etc.): "))
                    except ValueError:
                        print("Please enter an integer.")
                    else:
                        break
                amPM = input("AM or PM: ")

                info.schedule[mod][2]=amPM
                info.schedule[mod][1]=newHour
            elif modType==2:
                newType = input("Enter the new delivery type (bread, dairy etc.): ")
                info.schedule[mod][0]=newType
            else:
                break
            print("There is now a", info.schedule[mod][0],"delivery", mod, "at", info.schedule[mod][1], info.schedule[mod][2])
            
            #UnitTest 10
            while True:
                try:
                    confirm= int(input("Enter 1 to continue modifying or 2 to complete modification: "))
                    if confirm==1 or confirm==2:
                        break
                except:
                    print("Not a valid choice, please try again")

        print("Modification Complete!\n")
                
        
    #adds a new day to the schedule
    def addNew():
        options.showSchedule()
        #unit test 11, check to see if all days are in the schedule
        if len(info.schedule)==7:
          print("All 7 days are full! Try deleting a day.")
          return
        
        newDay = input("Enter the day of the new delivery: ")
        
        #unit test 12, checks if entered day is in the dictionary
        while newDay.lower() in options.getLower():
              print("Error! There is already a delivery on", newDay)
              newDay = input("Enter the day of the new delivery: ")

        newType = input("Enter the type of delivery (bread, dairy etc.): ")
        #unit test 13
        while True:
            try:
                newHour = int(input("Enter the hour for delivery (1,2,3,4 etc.): "))
            except ValueError:
                print("Please enter an integer.")
            else:
                break
        amPM = input("AM or PM: ")

        #introduce addition
        info.schedule[newDay] = [newType, newHour, amPM]
        print("\n\nSchedule Addition Completed!!")
        options.showSchedule()

#manager and employee options
class userActions:
    #say goodbye and save changes
    def farewell():
      with open(info.filename, 'wb') as f:
        pickle.dump(info.schedule, f)
      print('-------------------------------------------------------------')
      print("Thank you for using the Delivery Scheduler 9000.")
      print("Goodbye!")
      print('-------------------------------------------------------------\n')
      quit()
      
    #find if user is manager or employee
    def userType():
      print("Are you the manager or an employee?")
      #Unit test 14
      while True:
          try:
              userType = int(input("Enter 1 for Manager, or enter 2 for Employee: "))
          except ValueError:
              print("Error! Please enter a valid integer next time.")
          else:

              break
      #put user into correct userActions function
      if userType==1:
          userActions.manager()
      else:
          userActions.employee()
    #manager UI      
    def manager():
        print("Welcome, manager.")
        while True:
          #list options
          print("\nWhat would you like to do?")
          print(" Enter 1 to show the schedule.")
          print(" Enter 2 to modify a day on the schedule.")
          print(" Enter 3 to add a day to the schedule.")
          print(" Enter 4 to delete a day from the schedule.")
          print(" Enter 5 to change user.")
          print(" Enter 6 to save and end the program.")
          #Unit test 15
          while True:
            try:
                mChose = int(input("\nEnter your choice: "))
            except ValueError:
                print("Error! Please enter a valid integer.")
            else:
              if mChose in (1,2,3,4,5,6):
                break
              else:
                print("Error! Please enter a valid integer.")
          #send user to selected option
          if mChose==1:
            options.showSchedule()
          if mChose==2:
            options.modObject()
          if mChose==3:
            options.addNew()
          if mChose==4:
            options.removeObject()
          if mChose==5:
            userActions.userType()
          if mChose==6:
            userActions.farewell()
            
    #employee UI    
    def employee():
        print("Welcome, employee.")
        while True:
          #list options
          print("\nWhat would you like to do?")
          print(" Enter 1 to show the schedule.")
          print(" Enter 2 to change user.")
          print(" Enter 3 to save and end the program.")
          #Unit test 16
          while True:
            try:
                uChose = int(input("\nEnter your choice: "))
            except ValueError:
                print("Error! Please enter a valid integer.")
            else:
              if uChose in (1,2,3):
                break
              else:
                print("Error! Please enter a valid integer.")
          #execute the choice
          if uChose==1:
            options.showSchedule()
          if uChose==2:
            userActions.userType()
          if uChose==3:
            userActions.farewell()

#main
class main:
    #hello
    print('-------------------------------------------------------------')
    print("Welcome to the Delivery Scheduler 9000!!!!")
    print('-------------------------------------------------------------\n')
    #sendoff
    userActions.userType()

