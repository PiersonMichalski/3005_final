import psycopg2 # type: ignore

def main():
    print("booting up")

    userId = (0,0)
    while userId[0] == 0:
        userId = login()       

    match userId[1]:
        case "1":
            showMemberMenu(userId[0])
        case "2":
            showTrainerMenu(userId[0])
        case "3":
            showAdminMenu(userId[0])
    
def showMemberMenu(id):

    choice = 1

    while choice != "0":
        print("\nMember Menu\nWhat would you like to do next?")
        print("0) exit")
        print("1) update first name")
        print("2) update last name")
        print("3) update Email")
        print("4) update Gender")
        print("5) update Height")
        print("6) add heart rate recording")
        print("7) add weight recording")
        print("8) create goal")
        print("9) complete goal")
        print("10) create routine")
        print("11) remove routine")
        print("12) show trainers")
        print("13) show class scheduale")
        print("14) show heart rate statistics")
        print("15) show weight statistics")
        print("16) show completed goals")
        print("17) show in progress goals")
        print("18) show routines")
        print("19) request personal training session")
        print("20) signup for a class")

        print("\n")
        choice = input("enter number: ")
        print("\n")

        match choice:
            case "0":
                print("exiting\n")
            case "1":
                updateMemberFirstName(id)
            case "2":
                updateMemberLastName(id)
            case "3":
                updateMemberEmail(id)
            case "4":
                updateMemberGender(id)
            case "5":
                updateMemberHeight(id)
            case "6":
                addHeartRateRecording(id)
            case "7":
                addWeightRecording(id)
            case "8":
                createNewGoal(id)
            case "9":
                completeGoal(id)
            case "10":
                createNewRoutine(id)
            case "11":
                removeRoutine(id)
            case "12":
                showTrainers()
            case "13":
                showAllClasses()
            case "14":
                showHeartRateStatistics(id)
            case "15":
                showWeightStatistics(id)
            case "16":
                showCompletedGoals(id)
            case "17":
                showInProgressGoals(id)
            case "18":
                showRoutines(id)
            case "19":
                requestPersonalTraining(id)
            case "20":
                classRegistration(id)
            case _:
                print("error not valid selections")

        input("\npress enter to select a new action")

def showTrainerMenu(id):

    choice = 1

    while choice != "0":
        print("\nTrainer Menu\nWhat would you like to do?") 
        print("0) exit")
        print("1) display members")
        print("2) set schedule")
        print("3) search for member")

        print("\n")
        choice = input("enter number: ")
        print("\n")

        match choice:
            case "0":
                print("exiting\n")
            case "1":
                showMembers()
            case "2":
                setSchedule(id)
            case "3":
                searchMamber()
            case _:
                print("error not valid selections")

        input("\npress enter to select a new action")

def showAdminMenu(id): 

    choice = 1

    while choice != "0":
        print("\nAdmin Menu\nWhat would you like to do?")
        print("0) exit")
        print("1) create new class")
        print("2) show all classes")
        print("3) delete a class")
        print("4) list all equipment")
        print("5) add a new piece of equipment")
        print("6) remove a piece of equipment")
        print("7) update the status of a piece of equipment")
        print("8) show paid bills")
        print("9) show unpaid bills")
        print("10) update a bill")
        print("11) show all rooms")
        print("12) show all events")
        print("13) add a new event")

        print("\n")
        choice = input("enter number: ")
        print("\n")

        match choice:
            case "0":
                print("exiting\n")
            case "1":
                createNewClass()
            case "2":
                showAllClasses()
            case "3":
                deleteClass()               
            case "4":
                showAllEquipment()
            case "5":
                addNewEquipment()
            case "6":
                removeEquipment()
            case "7":
                updateEqipmentStatus()
            case "8":
                showPaidBills()
            case "9":
                showUnPaidBills()
            case "10":
                updateBill()
            case "11":
                showAllRooms()
            case "12":
                showAllEvents()
            case "13":
                addNewEvent()
            case _:
                print("error not valid selections")

        input("\npress enter to select a new action")

def updateMemberFirstName(id):
    newName = input("enter new first name: ")
    cur.execute("UPDATE Members SET first_name = %s WHERE member_id = %s;", [newName, id])
    conn.commit()

def updateMemberLastName(id):
    newName = input("enter new last name: ")
    cur.execute("UPDATE Members SET last_name = %s WHERE member_id = %s;", [newName, id])
    conn.commit()

def updateMemberEmail(id):
    newEmail = input("enter new email: ")
    cur.execute("UPDATE Members SET email = %s WHERE member_id = %s;", [newEmail, id])
    conn.commit()

def updateMemberGender(id):
    newGender = input("enter new gender: ")
    cur.execute("UPDATE Members SET gender = %s WHERE member_id = %s;", [newGender, id])
    conn.commit()

def updateMemberHeight(id):
    newHeight = input("enter new height in inches: ")
    cur.execute("UPDATE Members SET height = %s WHERE member_id = %s;", [newHeight, id])
    conn.commit()

def addHeartRateRecording(id):
    newHeartRate = input("enter the heart rate you recoreded in beats per minute: ")
    cur.execute("INSERT INTO Heart_rates (heart_rate, member_id) VALUES (%s, %s);", [newHeartRate, id])
    conn.commit()

def addWeightRecording(id):
    newWeight = input("enter the weight you recoreded in pounds: ")
    cur.execute("INSERT INTO Weights (weight, member_id) VALUES (%s, %s);", [newWeight, id])
    conn.commit()

def createNewGoal(id):
    newGoal = input("enter a discription for your new goal: ")
    cur.execute("INSERT INTO Goals (goal, member_id) VALUES (%s, %s);", [newGoal, id])
    conn.commit()

def createNewRoutine(id):
    newRoutine = input("enter a description of your new routine: ")
    cur.execute("INSERT INTO Routines (routine_description, member_id) VALUES (%s, %s);", [newRoutine, id])
    conn.commit()

def removeRoutine(memberId):
    routineId = input("type the id of the routine you would like to delete: ")
    cur.execute("DELETE FROM Routines WHERE routine_id = %s AND member_id = %s;", [routineId, memberId])
    conn.commit()

def completeGoal(id):
    goalId = input("type the id of the goal you have completed")
    cur.execute("UPDATE Goals SET completed = TRUE WHERE goal_id = %s AND member_id = %s;", [goalId, id])
    conn.commit()

def showTrainers():
    cur.execute("SELECT trainer_id, first_name, last_name, email FROM trainers")
    print("ID: first name, last name, email")
    for row in cur.fetchall():
        print(str(row[0]) + ": " + row[1] + ", " + row[2] + ", " + row[3])

def showMembers():
    cur.execute("SELECT member_id, first_name, last_name, email FROM members")
    print("ID: first name, last name, email")
    for row in cur.fetchall():
        print(str(row[0]) + ": " + row[1] + ", " + row[2] + ", " + row[3])

def searchMamber():
    first_name = input("enter first name of member you are searching for: ")
    last_name = input("enter last name of member you are searching for: ")
    cur.execute("SELECT member_id, first_name, last_name, email FROM members WHERE first_name = %s AND last_name = %s", [first_name, last_name])
    print("\n")
    for row in cur.fetchall():
        print(str(row[0]) + ": " + row[1] + ", " + row[2] + ", " + row[3])

def showCompletedGoals(id):
    cur.execute("SELECT goal_id, goal FROM goals WHERE member_id = %s AND completed = TRUE", [id])
    for row in cur.fetchall():
        print(str(row[0]) + ": " + row[1])

def showInProgressGoals(id):
    cur.execute("SELECT goal_id, goal FROM goals WHERE member_id = %s AND completed = FALSE", [id])
    for row in cur.fetchall():
        print(str(row[0]) + ": " + row[1])

def showRoutines(id):
    cur.execute("SELECT routine_id, routine_description FROM routines WHERE member_id = %s", [id])
    for row in cur.fetchall():
        print(str(row[0]) + ": " + row[1])

def createNewClass():
    className = input("enter a name for the new class: ")
    classDate = input("enter date of class (form yyyy-mm-dd): ")
    classTime = input("enter time of class (form 00:00): ")
    print("choose a trainer for the class, listed below are all trainers")
    showTrainers()
    classTrainer = input("enter trainer id: ")
    print("choose a room for the class, listed below are all rooms")
    showAllRooms()
    classRoom = input("enter room id: ")
    cur.execute("INSERT INTO Classes (class_name, class_date, class_time, trainer_id, room_id) VALUES (%s, %s, %s, %s, %s);", [className, classDate, classTime, classTrainer, classRoom])
    conn.commit()

def showAllClasses():
    cur.execute("SELECT class_name, class_date, class_time, trainer_id, room_id FROM classes")
    classes = cur.fetchall()
    for row in classes:
        cur.execute("SELECT first_name, last_name FROM trainers WHERE trainer_id = %s", [row[3]])
        trainer = cur.fetchone()
        cur.execute("SELECT room_name FROM rooms WHERE room_id = %s", [row[4]])
        room = cur.fetchone()
        print(row[0] + " run by " + trainer[0] + " " + trainer[1] + " in " + room[0] + " at " + str(row[2]) + " on " + str(row[1]))

def showAllRooms():
    cur.execute("SELECT room_id, room_name FROM rooms")
    for row in cur.fetchall():
        print(str(row[0]) + ": " + row[1])

def showAllEquipment():
    print("ID: name, status")
    cur.execute("SELECT machine_id, machine_name, machine_status FROM machines")
    for row in cur.fetchall():
        print(str(row[0]) + ": " + row[1] + ", " + row[2])

def addNewEquipment():
    machineName = input("enter a name for the new machine: ")
    machineStatus = input("enter status if machine: ")
    cur.execute("INSERT INTO Machines (machine_name, machine_status) VALUES (%s, %s);", [machineName, machineStatus])
    conn.commit()

def removeEquipment():
    print("chose the equipment you would like to remove, listed below is all equipment")
    showAllEquipment()
    eqipmentId = input("enter equipment id: ")
    cur.execute("DELETE FROM Machines WHERE machine_id = %s;", [eqipmentId])
    conn.commit()

def updateEqipmentStatus():
    print("chose the equipment you would like to update, listed below is all equipment")
    showAllEquipment()
    eqipmentId = input("enter equipment id: ")
    newStatus = input("enter new status for machine: ")
    cur.execute("UPDATE Machines SET machine_status = %s WHERE machine_id = %s;", [newStatus, eqipmentId])
    conn.commit()

def showPaidBills():
    cur.execute("select first_name, last_name, date_issued, amount, bill_id from bills join members on bills.member_id = members.member_id WHERE paid = TRUE")
    for row in cur.fetchall():
        print("{}) bill for ${} issued on {} to {} {}".format(row[4], row[3], row[2], row[0], row[1]))

def showUnPaidBills():
    cur.execute("select first_name, last_name, date_issued, amount, bill_id from bills join members on bills.member_id = members.member_id WHERE paid = FALSE")
    for row in cur.fetchall():
        print("{}) bill for ${} issued on {} to {} {}".format(row[4], row[3], row[2], row[0], row[1]))

def updateBill():
    print("select the bill that has been paid")
    showUnPaidBills()
    billId = input("enter bill id: ")
    cur.execute("UPDATE bills SET paid = TRUE WHERE bill_id = %s;", [billId])
    conn.commit()

def requestPersonalTraining(id):
    date = input("enter date for personal training (form yyyy-mm-dd): ")
    time = input("enter time for personal training (form 00:00): ")
    trainer_id = input("enter id of trainer: ")
    cur.execute("select free from trainer_work_schedule where trainer_id = %s AND block_date = %s AND block_time = %s", [trainer_id, date, time])
    free = cur.fetchone()[0]
    if free == True:
        print("confermed")
        cur.execute("UPDATE trainer_work_schedule SET free = FALSE WHERE trainer_id = %s AND block_date = %s AND block_time = %s", [trainer_id, date, time])
        conn.commit()
    else:
        print("that trainer is not free at that time")

def classRegistration(id):
    print("which class would you like to regester for? listed below are all classes")
    showAllClasses()
    classId = input("enter class id: ")
    cur.execute("INSERT INTO regestered (member_id, class_id) VALUES (%s, %s);", [id, classId])
    conn.commit()

def setSchedule(id):
    blockDate = input("enter date of work time (form yyyy-mm-dd): ")
    blockTime = input("enter time of work time (form 00:00): ")
    cur.execute("INSERT INTO trainer_work_schedule (block_date, block_time, trainer_id, free) VALUES (%s, %s, %s, TRUE);", [blockDate, blockTime, id])
    conn.commit()

def showHeartRateStatistics(id):
    cur.execute("select AVG(heart_rate) from heart_rates where member_id = %s", [id])
    avg = cur.fetchone()[0]
    print("average heart rate is " + avg + " BPM")

def showWeightStatistics(id):
    cur.execute("select AVG(weight) from weights where member_id = %s", [id])
    avg = cur.fetchone()[0]
    print("average weight is " + avg + " pounds")

def deleteClass():
    print("which class would you like to delete? listed below are all classes")
    showAllClasses()
    classId = input("enter class id: ")
    cur.execute("DELETE FROM classes WHERE class_id = %s;", [classId])
    conn.commit()
    
def showAllEvents():
    cur.execute("select event_name, event_date, event_time, room_name from events join rooms on events.room_id = rooms.room_id")
    for row in cur.fetchall():
        print("{} on {} at {} in {}".format(row[0], row[1], row[2], row[3]))
    
def addNewEvent():
    eventName = input("enter a name for the new event: ")
    eventDate = input("enter date of event (form yyyy-mm-dd): ")
    eventTime = input("enter time of event (form 00:00): ")
    print("choose a room for the event, listed below are all rooms")
    showAllRooms()
    eventRoom = input("enter room id: ")
    cur.execute("INSERT INTO event (event_name, event_date, event_time, room_id) VALUES (%s, %s, %s, %s);", [eventName, eventDate, eventTime, eventRoom])
    conn.commit()

def signUp():
    firstName = input("enter your first name: ")
    lastName = input("enter your last name: ")
    email = input("enter your email: ")
    password = input("enter a password: ")
    cur.execute("INSERT INTO members (first_name, last_name, email, member_password) VALUES (%s, %s, %s, %s);", [firstName, lastName, email, password])
    conn.commit()

def login():
    print("\nWhat Type of user are you?\n1) Member\n2) Trainer\n3) Admin\n4) Regester New User")
    choice = input("enter number: ")

    match choice:
        case "1":
            email = input("enter email: ")
            password = input("enter password: ")
            cur.execute("SELECT member_id, member_password, first_name, last_name FROM Members WHERE email = %s", [email,])
        case "2":
            email = input("enter email: ")
            password = input("enter password: ")
            cur.execute("SELECT trainer_id, trainer_password, first_name, last_name FROM Trainers WHERE email = %s", [email,])
        case "3":
            email = input("enter email: ")
            password = input("enter password: ")
            cur.execute("SELECT admin_id, admin_password, first_name, last_name FROM Admins WHERE email = %s", [email,])
        case "4":
            signUp()
            return(0,0)
        case _:
            print("error: not valid user type, try again")
            return (0,0)

    userInfo = cur.fetchone()

    if userInfo == None:
        print("error: incorrect username or password, try again")
        return (0,0)

    if userInfo[1] == password:
        print("successfully logged in as " + userInfo[2] + " " + userInfo[3])
        return (userInfo[0], choice) 
    
    print("error: incorrect username or password, try again")
    return (0,0)

# connects to db
conn = psycopg2.connect(host="localhost", dbname="final", user="postgres", password="postgres", port=5432)
cur = conn.cursor()

main()

cur.close()
conn.close()