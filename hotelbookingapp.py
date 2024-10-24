class hotelbook:
    def __init__(self):
        self.rooms={101:"Available",102:"Available",103:"Available",104:"Available",105:"Available"}
        self.bookings={}
    def display_menu(self):
        print("\n---Hotel Booking Menu---")
        print("1.View available rooms")
        print("2.Book a room")
        print("3.cancel room")
        print("4.view all bookings")
        print("5.exit")
    def view_available_rooms(self):
        print("\n---Available rooms---")
        for room,status in self.rooms.items():
            if status=="Available":
                print(f"room{room}:{status}")
    def book_room(self):
        name=input("\n enter your name:")
        room_number=int(input("enter the room number to book:"))
        if room_number in self.rooms and self.rooms[room_number]=="Available":
            self.rooms[room_number]="Booked"
            self.bookings[room_number]=name
            print(f"room{room_number} successfully booked by {name}.")
        else:
            print(f"room{room_number} is either not available or already booked.")
    def cancel_booking(self):
        room_number=int(input("\n Enter the room number to cancel:"))
        if room_number in self.bookings:
            name=self.bookings.pop(room_number)
            self.rooms[room_number]="Available"
            print(f"Booking for room{room_number} by {name} has been canceled.")
        else:
            print(f"No booking found for room{room_number}.")
    def view_all_bookings(self):
        if not self.bookings:
            print("\n no bookings found.")
        else:
            print("\n---Current bookings---")
            for room,name in self.bookings.items():
                print(f"room {room}:Booked by {name}")
    def run(self):
         while True:
             self.display_menu()
             choice=input("\n enter your choice(1-5):")
             if choice=="1":
                 self.view_available_rooms()
             elif choice=="2":
                 self.book_room()
             elif choice=="3":
                 self.cancel_booking()
             elif choice=="4":
                 self.view_all_bookings()
             elif choice=="5":
                 print("Thank you for using the hotel booking app!")
                 break
             else:
                 print("Invalid choice. Please try again.")
if __name__=="__main__":
    app=hotelbook()
    app.run()
