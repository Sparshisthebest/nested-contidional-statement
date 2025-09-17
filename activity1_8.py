#exam eligibility check
medical_cause=input("do you have a medical cause Y or N: ")
attendance=int(input("enter the attendance of the student: "))
if medical_cause=="Y":
    print("you're  allowed")
else:
    if attendance>=75:
        print("allowed")
    else:
        print("not allowed")