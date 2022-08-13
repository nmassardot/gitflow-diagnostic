from utils import (
    top_10_most_retweeted,
    top_10_users,
)

def main():
    print("Choose an option")
    path_to_data = "data/farmers-protest-tweets-2021-03-5.json"
    print("- Top 10 tweets most retweeted (1)")
    print("- Top 10 users (2)\n")
    user_input = int(input())

    if user_input == 1:
        most_retweeted = top_10_most_retweeted(path_to_data)

        print("\nTop 10 tweeets most retweeted")
        for i in range(len(most_retweeted)):
            print(f"{i+1}. {most_retweeted[i]}")

    elif user_input == 2:
        top_users = top_10_users(path_to_data)
        print("\nTop 10 users")
        for i in range(len(top_users)):
            print(f"{i+1}. {top_users[i]['username']}: {top_users[i]['tweets']}")

if __name__ == "__main__":
    main()
