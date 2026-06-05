import json

FILE_NAME = "new.json"

def load_data():
    with open(FILE_NAME, "r") as file:
        return json.load(file)
    
def save_data(data):
    with open(FILE_NAME, "w") as file:
        json.dump(data, file, indent=4)

def company_info(data):
    print("Company Information")
    print(data["company"]["name"])
    print(data["company"]["founded"])
    

    print("\nThe Headquarter is in ",data["company"]["offices"]["headquarters"]["city"], data["company"]["offices"]["headquarters"]["country"]) 

    print("\nThis Branch is in ", data["company"]["offices"]["branches"][0]["city"],"\nThe Total Employees is :: ",data["company"]["offices"]["branches"][0]["employees_count"]) 

    print("\nThe other Branch is in ", data["company"]["offices"]["branches"][1]["city"],"\nThe Total Employees is :: ",data["company"]["offices"]["branches"][1]["employees_count"],"\n") 

def employee_info(data):
    
    print("Employee Name is :: ",data["company"]["employees"][0]["name"],"\nskills is ", data["company"]["employees"][0]["skills"][0],",",data["company"]["employees"][0]["skills"][1],"and",data["company"]["employees"][0]["skills"][2])

    print("Project is ", data["company"]["employees"][0]["projects"][0]["name"],"and it is ",data["company"]["employees"][0]["projects"][0]["status"])

    print("Project is ", data["company"]["employees"][0]["projects"][1]["name"],"and it is ",data["company"]["employees"][0]["projects"][1]["status"])


    print("\n\nEmployee Name is :: ",data["company"]["employees"][1]["name"],"\nskills is ", data["company"]["employees"][1]["skills"][0],"and",data["company"]["employees"][1]["skills"][1])


    print("Project is ", data["company"]["employees"][1]["projects"][0]["name"],"and it is ",data["company"]["employees"][1]["projects"][0]["status"], "\n")



def main():
    data = load_data()

    while(True):
        print("1. Company Info\n2. Employee Info\n3. Exit")
        choice = int(input("Enter Your Choice :: "))

        if choice == 1:
            company_info(data)

        elif choice == 2:
            employee_info(data)

        elif choice == 3:
            print("Exit")
            exit()

        else :
            print("Invalid Choice")

if __name__ == "__main__":
    main()