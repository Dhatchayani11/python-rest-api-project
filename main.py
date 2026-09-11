from api import get_github_user


def main():
    username = input("Enter GitHub username: ")

    try:
        user = get_github_user(username)

        print("\nGitHub User Information")
        print("-----------------------")
        print(f"Username: {user['login']}")
        print(f"Name: {user['name']}")
        print(f"Public Repositories: {user['public_repos']}")
        print(f"Followers: {user['followers']}")
        print(f"Following: {user['following']}")
        print(f"Profile: {user['html_url']}")

    except ValueError as error:
        print(f"Error: {error}")

    except Exception as error:
        print(f"Something went wrong: {error}")


if __name__ == "__main__":
    main()