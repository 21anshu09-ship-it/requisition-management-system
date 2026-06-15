class Requisition:

    requisition_counter = 10000

    def __init__(self, date, staff_id, staff_name):

        self.date = date
        self.staff_id = staff_id
        self.staff_name = staff_name

        self.items = []

        Requisition.requisition_counter += 1
        self.requisition_id = Requisition.requisition_counter

        self.total = 0

        self.status = "Pending"

        self.approval_reference = "Not available"
        
    def add_requisition(self, items):

        self.items = items

        self.total = sum(item["price"] for item in items)

        return self.total
    
    def approve_requisition(self):

        if self.total < 500:

            self.status = "Approved"

            last_three = str(self.requisition_id)[-3:]

            self.approval_reference = (
                self.staff_id + last_three
            )

        else:

            self.status = "Pending"

            self.approval_reference = "Not available"

        return self.status
    
    