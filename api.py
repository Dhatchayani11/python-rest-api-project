import requests


def get_github_user(username):
    url = f"https://api.github.com/users/{username}"

    response = requests.get(url)

    if response.status_code == 200:
        return response.json()

    if response.status_code == 404:
        raise ValueError("GitHub user not found")

    raise Exception(f"API request failed: {response.status_code}")