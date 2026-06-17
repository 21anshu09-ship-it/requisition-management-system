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

r1.approve_requisition()

print("Before Manager Decision")
print("Total:", r1.total)
print("Status:", r1.status)

r1.manager_response("Not Approved")

print("\nAfter Manager Decision")
print("Status:", r1.status)
print("Approval Reference:", r1.approval_reference)