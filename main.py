from requisition import Requisition

r1 = Requisition(
    "03/04/2024",
    "FN19",
    "John Paul"
)

items = [
    {"name": "Laptop", "price": 600},
    {"name": "Mouse", "price": 100}
]
r1.add_requisition(items)

status = r1.approve_requisition()

print("Total:", r1.total)
print("Status:", status)
print("Approval Reference:", r1.approval_reference)