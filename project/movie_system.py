import json

file_name = "movie.json"

def load_data():
    with open(file_name, "r") as file:
        return json.load(file)

def save_data(data):
     with open(file_name, "w") as file:
        json.dump(data, file, indent=4)


def add_movie(data):
    title = input("Enter the Title of Movie :: ")
    type = input("Enter the Type :: ")
    year = input("Enter the Movie Released Year :: ")

    movie = {
        "title": title,
        "type": type,
        "year": year
    }

    data.append(movie)
    print("Movie Added Successfully.....")
    save_data(data)

def update_movie(data):

    title = input("Enter the Movie Title :: ") 
    for movie in data:
        if movie["title"].lower() == title.lower():
            new_title = input("Enter New Title :: ")
            new_type = input("Enter New Type :: ")
            new_year = input("Enter New Year :: ")

            movie["title"] = new_title
            movie["type"] = new_type
            movie["year"] = new_year
            save_data(data)

            print("Movie Updated Successfully....")


def view_movie(data):

    for movie in data:
        print("\nTitle :: ", movie["title"])
        print("Type :: ", movie["type"])
        print("Year :: ", movie["year"])
        

def main():
    data = load_data()

    while True:
        print("1. Add Movie")
        print("2. Update Movie")
        print("3. View Movie")
        print("4. Exit")

        choice = int(input("Enter choice: "))

        if choice == 1:
            add_movie(data)

        elif choice == 2:
            update_movie(data)

        elif choice == 3:
            view_movie(data)

        elif choice == 4:
            print("Exit")
            break

        else:
            print("Invalid Choice")

if __name__ == "__main__":
    main()