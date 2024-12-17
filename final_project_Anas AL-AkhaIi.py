from abc import ABC, abstractmethod
from datetime import datetime, timedelta

# الصنف المجرد لإدارة الحجز
class BookingInterface(ABC):
    @abstractmethod
    def book_field(self, field_id, user_name, booking_time):
        pass

    @abstractmethod
    def view_bookings(self):
        pass

# صنف لإدارة بيانات الملاعب
class FieldManager:
    def __init__(self):
        self.fields = {
            1: {"name": "Field 1", "location": "Downtown", "price_per_hour": 50},
            2: {"name": "Field 2", "location": "Uptown", "price_per_hour": 70},
        }

    def list_fields(self):
        print("Available Fields:")
        for field_id, field_info in self.fields.items():
            print(
                f"ID: {field_id}, Name: {field_info['name']}, Location: {field_info['location']}, Price: {field_info['price_per_hour']} USD/hour"
            )

# صنف لإدارة الحجوزات
class BookingManager(BookingInterface):
    def __init__(self):
        self.bookings = []

    def book_field(self, field_id, user_name, booking_time):
        booking_end_time = booking_time + timedelta(hours=1)
        self.bookings.append({
            "field_id": field_id,
            "user_name": user_name,
            "start_time": booking_time,
            "end_time": booking_end_time,
        })
        print(f"Field {field_id} booked successfully for {user_name} from {booking_time} to {booking_end_time}.")

    def view_bookings(self):
        print("Current Bookings:")
        for booking in self.bookings:
            print(
                f"Field ID: {booking['field_id']}, User: {booking['user_name']}, Time: {booking['start_time']} - {booking['end_time']}"
            )

# صنف التطبيق الرئيسي
class FieldBookingApp:
    def __init__(self):
        self.field_manager = FieldManager()
        self.booking_manager = BookingManager()

    def run(self):
        while True:
            print("\n1. View Fields\n2. Book Field\n3. View Bookings\n4. Exit")
            choice = input("Enter your choice: ")

            if choice == "1":
                self.field_manager.list_fields()
            elif choice == "2":
                try:
                    field_id = int(input("Enter Field ID: "))
                    user_name = input("Enter Your Name: ")
                    booking_time_input = input("Enter Booking Time (YYYY-MM-DD HH:MM): ")
                    booking_time = datetime.strptime(booking_time_input, "%Y-%m-%d %H:%M")
                    self.booking_manager.book_field(field_id, user_name, booking_time)
                except Exception as e:
                    print(f"Error: {e}")
            elif choice == "3":
                self.booking_manager.view_bookings()
            elif choice == "4":
                print("Exiting the app. Goodbye!")
                break
            else:
                print("Invalid choice. Try again.")

# Example usage
if __name__ == "__main__":
    app = FieldBookingApp()
    app.run()
