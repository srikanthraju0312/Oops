class Stu_Details:
    def __init__(self, hall_no, name):
        self.hall_no = hall_no
        self.name = name
    def showDetails(self):
        print(f"Hall Ticket no. {self.hall_no} is {self.name}")

class CGPA(Stu_Details):
    def showcgpa(self):
        if self.hall_no == "21S11A66D8":
            print("All subjects Cleared")
        elif self.hall_no == "21S11A66F5":
            print("Cleared only 1 subject")
        
d8 = CGPA("21S11A66D8","Balaji Menan")
e3 = CGPA("21S11A66E3","N.Srikanth Raju")
e5 = CGPA("21S11A66E5","Dilip Kumar")
f5 = CGPA("21S11A66F5","Maniteja")
le13 = CGPA("21S11A66LE13","Upendra Thota")

d8.showDetails()
d8.showcgpa()     
f5.showDetails()
f5.showcgpa()