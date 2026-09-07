import json

def load_data():
    with open("fruit_list.json", "r") as file:
        data = json.load(file)
        return data
    


def save_data(data):
    with open("fruit_list.json", "w") as file:
        json.dump(data, file, indent=4)



def main():

    data = load_data() 
    print(json.dumps(data ["fruit"], indent = 4))     
    save_data(data)        




if __name__ == "__main__":
    main()


