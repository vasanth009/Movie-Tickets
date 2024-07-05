import datetime
import re
import mysql.connector
import smtplib
def movie_list():
    f=open("movielist.txt","r")
    print(f.read())
def ticket_booking():
#regular expression
    f=open("movies.txt","r")
    txt=f.read()
    your_movies=input("Enter your movie name: ")
    movie=re.search(your_movies,txt)
    print(movie)
    if movie:
        print(f"Yes!! {your_movies} movie is available in movies list...")
        Goat_ticket_price=180
        Star_ticket_price=140
        vidamuyarchi_ticket_price=160
        indian2_ticket_price=150
        Aranmanai4_ticket_price=120
    #exception handling
        try:
            quantity=int(input(f"How many tickets you want to book for {your_movies} movie: "))
            Goat_netprice=200
            Star_netprice=165
            vidamuyarchi_netprice=180
            indian2_netprice=165
            aranmanai4_netprice=130

        #statement for offer price and total price 
            if your_movies=="GOAT" or your_movies=="STAR" or your_movies=="Vidamuyarchi" or your_movies=="Indian 2" or your_movies=="Aranmanai 4":
                if your_movies=="GOAT":
                    total=Goat_ticket_price*quantity
            #GST calculation  
                    gst_percent = round(((Goat_netprice - Goat_ticket_price) * 100) / Goat_ticket_price)
                elif your_movies=="STAR":
                    total=Star_ticket_price*quantity
              #GST calculation  
                    gst_percent = round(((Star_netprice - Star_ticket_price) * 100) / Star_ticket_price)
                elif your_movies=="Vidamuyarchi":
                    total=vidamuyarchi_ticket_price*quantity
              #GST calculation  
                    gst_percent = round(((vidamuyarchi_netprice - vidamuyarchi_ticket_price) * 100) / vidamuyarchi_ticket_price)
                elif your_movies=="Indian 2":
                    total=indian2_ticket_price*quantity
              #GST calculation
                    gst_percent = round(((indian2_netprice - indian2_ticket_price) * 100) / indian2_ticket_price)
                elif your_movies=="Aranmanai 4":
                    total=Aranmanai4_ticket_price*quantity
              #GST calculation  
                    gst_percent = round(((aranmanai4_netprice - Aranmanai4_ticket_price) * 100) / Aranmanai4_ticket_price)


        #condition for offer price and total price and storing database and mail sending
                if quantity>=5:
                    offer=total-100
                    print(f"You booked more than 5 tickets for {your_movies} movie, so your offer ticket price is {offer} RS.") 
                    print(f"GST for the ticket= {gst_percent}%")
                #date and time
                    x=datetime.datetime.now()
                    print(f"Ticket generated Date & Time: {x}")
                #generating ticket at ticket.txt
                    f=open("ticket.txt","w")
                    f.write(f"You booked more than 5 tickets for {your_movies} movie, so your offer ticket price is {offer} RS.")
                    f=open("ticket.txt","a")
                    f.write(f"\nGST for the ticket= {gst_percent}%")
                    f.write(f"\n\n\t\t****INOX Cinemas A/C Dts AEROHUB****")
                    f.write(f"\n\t\t\t\tMovie : {your_movies}\n\t\t\t\tNo of ticket : {quantity}\n\t\t\t\tClass : 1st Class\n\t\t\t\tTime : 6:00PM\n\t\t\t\tTotal : {offer} RS.")
                    f.write(f"\n\nTicket generated Date & Time: {x}")
                    print("----Now your ticket data storing in Database----")
            #python connecting with mysql database
                    mydb=mysql.connector.connect(
                        host="localhost",
                        user="root",
                        password="12345",
                        database="movie_ticket"  
                    )
                    mycursor=mydb.cursor()
                    sql="insert into ticket_details(name,movie,no_of_tickets,time,total) values (%s,%s,%s,%s,%s)"
                    name=input("Enter your name: ")
                    movie=input("Enter the movie name: ")
                    no_of_tickets=int(input("Enter how many tickets you want: "))
                    time=input("Enter your movie time: ")
                    total=int(input(f"Enter your total: "))
                    val=(name,movie,no_of_tickets,time,total)
                    mycursor.execute(sql,val)
                    mydb.commit()
                    print("***Your data's saved successfully in Database***")
                #mail sending to user
                    user=input("Enter your E-mail id: ")
                    if user=="shaik112abdullah@gmail.com":
                        try:
                            receiver_mail=["shaik112abdullah@gmail.com"]
                            for i in receiver_mail:
                                s=smtplib.SMTP('smtp.gmail.com',587) 
                                s.starttls()
                                s.login("shaikh113abdullah@gmail.com","abcd efgh jhyu 1wjfd")
                                message=f"----YOUR MOVIE TICKET----\n\nHello {name}!!, you have booked ticket for {your_movies} movie...\n\n\t\t****INOX Cinemas A/C Dts AEROHUB****\n\t\t\t\tMovie : {your_movies}\n\t\t\t\tNo of ticket : {quantity}\n\t\t\t\tClass : 1st Class\n\t\t\t\tTime : 6:00PM\n\t\t\t\tTotal : {offer} RS.\nTicket generated Date & Time: {x}\n\n*****Thanks for visiting Movieshow Booking App*****"
                                s.sendmail("shaikh113abdullah@gmail.com",i,message) 
                                s.quit()                                                  
                                print("***Movie ticket generated to user mail Successfully***")
                                print("******Thanks for visiting Movieshow Booking App******")
                        except:
                            print("Mail not sent to user..")  
                else:
                    print(f"You booked {quantity} tickets for {your_movies} movie, so your total ticket price is {total} RS.")
                    print(f"GST for the ticket= {gst_percent}%")
                #date and time
                    x=datetime.datetime.now()
                    print(f"Ticket generated Date & Time: {x}")
                #generating ticket at ticket.txt
                    f=open("ticket.txt","w")
                    f.write(f"You booked {quantity} tickets for {your_movies} movie, so your total ticket price is {total} RS.")
                    f=open("ticket.txt","a")
                    f.write(f"\nGST for the ticket= {gst_percent}%")
                    f.write(f"\n\n\t\t****INOX Cinemas A/C Dts AEROHUB****")
                    f.write(f"\n\t\t\t\tMovie : {your_movies}\n\t\t\t\tNo of ticket : {quantity}\n\t\t\t\tClass : 1st Class\n\t\t\t\tTime : 6:00PM\n\t\t\t\tTotal : {total} RS.")
                    f.write(f"\n\nTicket generated Date & Time: {x}")
                    print("----Now you ticket data storing in Database----")
            #python connecting with mysql database
                    mydb=mysql.connector.connect(
                        host="localhost",
                        user="root",
                        password="12345",
                        database="movie_ticket"  
                    )
                    mycursor=mydb.cursor()
                    sql="insert into ticket_details(name,movie,no_of_tickets,time,total) values (%s,%s,%s,%s,%s)"
                    name=input("Enter your name: ")
                    movie=input("Enter the movie name: ")
                    no_of_tickets=int(input("Enter how many tickets you want: "))
                    time=input("Enter your movie time: ")
                    total=int(input(f"Enter your total: "))
                    val=(name,movie,no_of_tickets,time,total)
                    mycursor.execute(sql,val)
                    mydb.commit()
                    print("***Your data's saved successfully in Database***")
                #mail sending to user
                    user=input("Enter your E-mail id: ")
                    if user=="shaik112abdullah@gmail.com":
                        try:
                            receiver_mail=["shaik112abdullah@gmail.com"]
                            for i in receiver_mail:
                                s=smtplib.SMTP('smtp.gmail.com',587) 
                                s.starttls()
                                s.login("shaikh113abdullah@gmail.com","abdc fhge wwee 1f2a")
                                message=f"----YOUR MOVIE TICKET----\n\nHello {name}!!, you have booked ticket for {your_movies} movie...\n\n\t\t****INOX Cinemas A/C Dts AEROHUB****\n\t\t\t\tMovie : {your_movies}\n\t\t\t\tNo of ticket : {quantity}\n\t\t\t\tClass : 1st Class\n\t\t\t\tTime : 6:00PM\n\t\t\t\tTotal : {total} RS.\n\nTicket generated Date & Time: {x}\n\n*****Thanks for visiting Movieshow Booking App*****"
                                s.sendmail("shaikh113abdullah@gmail.com",i,message) 
                                s.quit()                                                  
                                print("***Movie ticket generated to user mail Successfully***")
                                print("******Thanks for visiting Movieshow Booking App******")
                        except:
                            print("Mail not sent to user..")
                    else:
                        print("You entered wrong mail-id...")        
        except: 
              print("Please type numbers only...")
    else:
        print(f"Sorry!! {your_movies} movie is not available in movies list...")

#calling function
movie_list()
ticket_booking()

