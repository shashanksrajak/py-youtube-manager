# Youtube Manager Application

import json

YOUTUBE_FILE = "youtube.txt"


def load_data():
    try:
        with open(YOUTUBE_FILE, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        print(f"{YOUTUBE_FILE} File not found!!!")
        return []


def save_data_helper(videos):
    with open(YOUTUBE_FILE, "w") as file:
        json.dump(videos, file)


def list_all_videos(videos):
    for index, video in enumerate(videos, start=1):
        print(f"{index} : {video["name"]}")


def add_video(videos):
    name = input("Enter video name: ")
    time = input("Enter video time: ")

    videos.append({"name": name, "time": time})
    save_data_helper(videos)


def update_video(videos):
    list_all_videos(videos)
    index_to_update = int(input("Enter the video number to update"))
    if 1 <= index_to_update <= len(videos):
        name = input("Enter new video name")
        time = input("Enter video time")
        videos[index_to_update-1] = {"name": name, "time": time}
        save_data_helper(videos)
    else:
        print("Invalid video number!!!")


def delete_video(videos):
    list_all_videos(videos)
    index_to_delete = int(input("Enter the video number to delete"))
    if 1 <= index_to_delete <= len(videos):
        del videos[index_to_delete-1]
        save_data_helper(videos)
    else:
        print("Invalid video number!!!")


def main():
    videos = load_data()

    while True:
        print(
            "\n---- Welcome to Youtube Manager | Choose an option from below options ----")
        print("1. List all youtube videos")
        print("2. Add a youtube video")
        print("3. Update a youtube video")
        print("4. Delete a youtube video")
        print("5. Exit the app")
        choice = input("Enter your choice (1-5): ")

        match choice:
            case "1":
                list_all_videos(videos)

            case "2":
                add_video(videos)

            case "3":
                update_video(videos)

            case "4":
                delete_video(videos)

            case "5":
                break  # this is for while loop break not for match case

            case _:
                print("Invalid Choice!!!")


if __name__ == "__main__":
    main()
