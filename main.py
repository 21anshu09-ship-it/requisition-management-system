from requisition import Requisition

r1 = Requisition(
    "03/04/2024",
    "FN19",
    "John Paul"
)

items = [
    {"name": "Laptop", "price": 250},
    {"name": "Mouse", "price": 50},
    {"name": "Keyboard", "price": 100}
]

total = r1.add_requisition(items)

print("Requisition Total:", total)