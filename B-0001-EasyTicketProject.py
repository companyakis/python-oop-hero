class Movie:
  def __init__(self, name):
    self.name = name
    self.tickets = []

  def add_ticket(self, ticket):
    self.tickets.append(ticket)
  
  def print_tickets(self):
    for ticket in self.tickets:
      print(ticket)

class Ticket:
  def __init__(self, date, movie_hall, price, ticket_owner):
    self.date = date
    self.movie_hall = movie_hall
    self.price = price
    self.ticket_owner = ticket_owner

  def __str__(self):
    return f"date: {self.date}, movie hall: {self.movie_hall}, price: {self.price}, ticket owner: {self.ticket_owner}"


movie = Movie("Matrix 1")

ticket_1 = Ticket("12/01/2000", "İzmir Konak Cinema A1", 2, "Mustafa Büyükdereli")

ticket_2 = Ticket("06/25/2004", "İzmir Karşıyaka Cinema A2", 4, "Bilge Güzelce")

movie.add_ticket(ticket_1)

movie.add_ticket(ticket_2)

movie.print_tickets()

"""
date: 12/01/2000, movie hall: İzmir Konak Cinema A1, price: 2, ticket owner: Mustafa Büyükdereli
date: 06/25/2004, movie hall: İzmir Karşıyaka Cinema A2, price: 4, ticket owner: Bilge Güzelce
"""
