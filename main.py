from utils import (
    top_10_most_retweeted,
    top_10_users,
    top_10_days_with_more_tweets,
    top_10_hashtags,
)

def main():
    print("Choose an option")
    path_to_data = "data/farmers-protest-tweets-2021-03-5.json"
    print("- Top 10 tweets most retweeted (1)")
    print("- Top 10 users (2)")
    print("- Top 10 days with more tweets (3)")
    print("- Top 10 used hashtags (4)\n")
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

    elif user_input == 3:
        top_days = top_10_days_with_more_tweets(path_to_data)

        print("\nTop 10 days with more tweets")
        for i in range(len(top_days)):
            print(f"{i+1}. {top_days[i]['date']}: {top_days[i]['count']}")

    elif user_input == 4:
        top_hashtags = top_10_hashtags(path_to_data)

        print("\nTop 10 used hashtags")
        for i in range(len(top_hashtags)):
            print(f"{i+1}. {top_hashtags[i]['hashtag']}: {top_hashtags[i]['count']}")


if __name__ == "__main__":
    main()
