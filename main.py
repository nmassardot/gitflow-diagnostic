from utils import top_10_most_retweeted

def main():
    print("Choose an option")
    path_to_data = "data/farmers-protest-tweets-2021-03-5.json"
    user_input = int(input("- Top 10 tweets most retweeted (1)\n"))

    if user_input == 1:
        most_retweeted = top_10_most_retweeted(path_to_data)

        print("\nTop 10 tweeets most retweeted")
        for i in range(len(most_retweeted)):
            print(f"{i}. {most_retweeted[i]}")

if __name__ == "__main__":
    main()
