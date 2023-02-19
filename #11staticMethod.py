print("Static Method")

class Percentage:
    divisibleby = 100

    @staticmethod
    def myPercent(totalmarks, obtainedmarks):
        print((obtainedmarks/totalmarks)*Percentage.divisibleby,"%")

tm = int(input("Enter the total marks: "))
om = float(input("Enter the obtained marks: "))
Percentage.myPercent(tm, om)

