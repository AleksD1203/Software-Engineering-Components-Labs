from datetime import date, datetime
from decimal import Decimal
from typing import List

class Customer:
    """ Сутність: CUSTOMER """
    def __init__(self, customer_id: int, name: str, email: str, phone_number: str):
        self.customer_id: int = customer_id  # PK
        self.name: str = name
        self.email: str = email
        self.phone_number: str = phone_number
        
        self.bookings: List['Booking'] = []

class Movie:
    """ Сутність: MOVIE """
    def __init__(self, movie_id: int, title: str, release_date: date, duration: int, genre: str):
        self.movie_id: int = movie_id  # PK
        self.title: str = title
        self.release_date: date = release_date
        self.duration: int = duration 
        self.genre: str = genre
        
        self.sessions: List['Session'] = []

class Hall:
    """ Сутність: HALL """
    def __init__(self, hall_id: int, name: str, total_seats: int):
        self.hall_id: int = hall_id  # PK
        self.name: str = name
        self.total_seats: int = total_seats
        
        self.seats: List['Seat'] = []
        self.sessions: List['Session'] = []

class Seat:
    """ Сутність: SEAT """
    def __init__(self, seat_id: int, hall_id: int, row_number: str, seat_number: int):
        self.seat_id: int = seat_id  # PK
        self.row_number: str = row_number
        self.seat_number: int = seat_number
        
        self.hall_id: int = hall_id  # FK

class Session:
    """ Сутність: SESSION """
    def __init__(self, session_id: int, movie_id: int, hall_id: int, session_time: datetime):
        self.session_id: int = session_id  # PK
        self.session_time: datetime = session_time
        
        self.movie_id: int = movie_id  # FK
        self.hall_id: int = hall_id 
        self.tickets: List['Ticket'] = []

class Booking:
    """ Сутність: BOOKING """
    def __init__(self, booking_id: int, customer_id: int, booking_date: date, total_amount: Decimal):
        self.booking_id: int = booking_id  # PK
        self.booking_date: date = booking_date
        self.total_amount: Decimal = total_amount
        
        self.customer_id: int = customer_id  # FK 
        self.tickets: List['Ticket'] = []

class Ticket:
    """ Сутність: TICKET """
    def __init__(self, ticket_id: int, booking_id: int, session_id: int, seat_id: int, price: Decimal):
        self.ticket_id: int = ticket_id  # PK
        self.price: Decimal = price
    
        self.booking_id: int = booking_id  # FK
        self.session_id: int = session_id  # FK
        self.seat_id: int = seat_id      # FK
        
print("--- Example ---")

my_movie = Movie(
    movie_id=101, 
    title="Avatar 3: Fire and Ash", 
    release_date=date(2025, 12, 19), 
    duration=166, 
    genre="Science Fiction"
)

my_customer = Customer(
    customer_id=1,
    name="Aleksandr",
    email="aleksandr@example.com",
    phone_number="+380501234567"
)

print(f"Film was created: {my_movie.title}")
print(f"Genre: {my_movie.genre}")
print(f"Duration: {my_movie.duration} minutes")

print("---")

print(f"Customer was created: {my_customer.name}")
print(f"Email: {my_customer.email}")

print("--- Program was ended ---")