from requisition import Requisition

# Requisition 1 (< $500)
r1 = Requisition("03/04/2024", "FN19", "John Paul")
r1.add_requisition([
    {"name": "Laptop Bag", "price": 250},
    {"name": "Mouse", "price": 150}
])
r1.approve_requisition()

# Requisition 2 (> $500)
r2 = Requisition("05/04/2024", "FN20", "Tracy Brown")
r2.add_requisition([
    {"name": "Laptop", "price": 1000}
])
r2.approve_requisition()

# Requisition 3 (> $500)
r3 = Requisition("07/05/2024", "FN15", "Emma Wellington")
r3.add_requisition([
    {"name": "Workstation", "price": 3500}
])
r3.approve_requisition()

# Requisition 4 (< $500)
r4 = Requisition("03/05/2024", "FN02", "Catlin White")
r4.add_requisition([
    {"name": "Monitor", "price": 490}
])
r4.approve_requisition()

# Requisition 5 (> $500)
r5 = Requisition("10/05/2024", "FN25", "Alex Smith")
r5.add_requisition([
    {"name": "Printer", "price": 700}
])
r5.approve_requisition()

# Manager responses
r2.manager_response("Approved")
r3.manager_response("Not approved")

# Display all requisitions
r1.display_requisition()
r2.display_requisition()
r3.display_requisition()
r4.display_requisition()
r5.display_requisition()

# Display statistics
Requisition.requisition_statistics()