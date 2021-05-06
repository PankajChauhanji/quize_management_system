##############################################
#          Quiz Management System.           #
##############################################

#import mydql connector
import mysql.connector

#access for database.
user_name = "root"
password = "Smartserv@123"
host_name = "localhost"
database_name = "quiz_management"

mydb = mysql.connector.connect(host = host_name,
                               user = user_name,
                               passwd = password,
                               database = database_name
                               )
mycursor = mydb.cursor()

#create tables.
question_table = "create table questions (q_id int NOT NULL AUTO_INCREMENT PRIMARY KEY, subject varchar(50), question_description varchar(1000), opt_a varchar(100), opt_b varchar(100), opt_c varchar(100), opt_d varchar(100), ans_option varchar(5))"
participants_table = "create table participants(p_id int NOT NULL AUTO_INCREMENT PRIMARY KEY, p_roll int(5), p_name varchar(50), p_age int(10), p_email varchar(100))"
score_table = "create table scores(score_id int NOT NULL AUTO_INCREMENT PRIMARY KEY, p_name varchar(50), total_score int(50), p_score int(50), total_correct int(50), total_wrong int(50), total_attempted int(50), percent int(50))"

mycursor.execute(question_table)
mycursor.execute(participants_table)
mycursor.execute(score_table)


choice = 1
while(choice):
    print("\n\n\t|'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''|")
    print("\t|\t\t\tQUIZ MANAGEMENT SOFTWARE \t\t\t  |")
    print("\t|________________________________________________________By-Ankaj Chauhan_|\n")
    #choices for options.
    print("0: To Stop")
    print("1: Add Questions")
    print("2: Add Participants")
    print("3: Add Scores")
    print("4: Display Data")
    choice = int(input("choice : "))
    if choice==1:
        # To add questions
        sub = str(input("Enter the subject: "))
        qstn = input("Enter the Question: ")
        opt1 = input("Enter the option a: ")
        opt2 = input("Enter the option b: ")
        opt3 = input("Enter the option c: ")
        opt4 = input("Enter the option d: ")
        opt = input("Enter answer option: ")
        
        #insert into question table.
        sql_query = f"INSERT INTO questions(subject, question_description, opt_a, opt_b, opt_c, opt_d, ans_option) VALUES( '{sub}', '{qstn}', '{opt1}', '{opt2}', '{opt3}', '{opt4}', '{opt}');"
        mycursor.execute(sql_query)
        mydb.commit()
        print("Qestion has been added")

    elif choice==2:
        # To add participants
        roll_no = int(input("Enter the participant Roll No: "))
        p_name = input("Enter the participant name: ")
        p_age = int(input("Enter the age: "))
        email = input("Enter the Email: ")
        # to insert into participants table
        sql_query = f"INSERT INTO participants(p_roll, p_name, p_age, p_email) VALUES({roll_no}, '{p_name}', {p_age}, '{email}');"
        mycursor.execute(sql_query)
        mydb.commit()
        print("Participant Added")
    
    elif choice==3:
        # to add in score table.
        p_name = input("Enter the name of participant: ")
        t_score = int(input("Enter the total score: "))
        p_score = int(input("Enter the particpant score: "))
        correct = int(input("Enter the total correct answer: "))
        incorrect = int(input("Enter the total incorrect answers: "))
        attempted = correct + incorrect
        percentage = ((p_score)/(t_score))*100
        # insert into score table.
        sql_query = f"insert into scores(p_name, total_score, p_score, total_correct, total_wrong, total_attempted, percent) values('{p_name}', '{t_score}', '{p_score}', '{correct}', '{incorrect}', '{attempted}', '{percentage}');"
        mycursor.execute(sql_query)
        mydb.commit()
        print("Scores Added")

    elif choice==4:
        # Display data.
        print("\n***************** Display Data *************\n")
        print("1: Display All Qusetions: ")
        print("2: Display All Participants: ")
        print("3: Display All Scores: ")
        new_choice = int(input())

        if(new_choice==1):
            # to display questions
            mycursor.execute("select * from questions")
            data = mycursor.fetchall()
            print("\n\t\t\t*******ALL Questions Data*****\n")
        elif(new_choice==2):
            # to display participants.
            mycursor.execute("select * from participants")
            data = mycursor.fetchall()
            print("\n\t\t\t*******ALL Participants Data*****\n")
        elif(new_choice==3):
            # to display score card
            mycursor.execute("select * from scores")
            data = mycursor.fetchall()
            print("\n\t\t\t*******ALL Scores Data*****\n")

        for i in range(len(data)):
            # print all the data.
            print("\t", data[i])
        print("******************************************************************************************\n\n\n")