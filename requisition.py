class Requisition:

    requisition_counter = 10000
    requisitions = []

    def __init__(self, date, staff_id, staff_name):

        self.date = date
        self.staff_id = staff_id
        self.staff_name = staff_name
        Requisition.requisitions.append(self)

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
    
    def manager_response(self, decision):

        if self.status == "Pending":

            if decision.lower() == "approved":

                self.status = "Approved"

                last_three = str(self.requisition_id)[-3:]

                self.approval_reference = (
                    self.staff_id + last_three
                )

            elif decision.lower() == "not approved":

                self.status = "Not approved"

                self.approval_reference = "Not available"

        return self.status
    
    def display_requisition(self):

        print("\nDate:", self.date)
        print("Requisition ID:", self.requisition_id)
        print("Staff ID:", self.staff_id)
        print("Staff Name:", self.staff_name)
        print("Total:", self.total)
        print("Status:", self.status)
        print("Approval Reference Number:",
            self.approval_reference)
        
    @classmethod
    def requisition_statistics(cls):

        total = len(cls.requisitions)

        approved = sum(
            1 for req in cls.requisitions
            if req.status == "Approved"
        )

        pending = sum(
            1 for req in cls.requisitions
            if req.status == "Pending"
        )

        not_approved = sum(
            1 for req in cls.requisitions
            if req.status == "Not approved"
        )

        print("\nREQUISITION STATISTICS")
        print("Total Requisitions:", total)
        print("Approved:", approved)
        print("Pending:", pending)
        print("Not Approved:", not_approved)