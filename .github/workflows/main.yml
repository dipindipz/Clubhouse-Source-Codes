import requests

def perform_action(action, token):
    url = "https://www.clubhouseapi.com/api/perform_hyperview_action"
    headers = {
        "Authorization": f"Token {token}"
    }

    if action == "enable":
        action_name = "settings/account/enable_protected_profile.xml"
    elif action == "disable":
        action_name = "settings/account/disable_protected_profile.xml"
    else:
        raise ValueError("Invalid action. Use 'enable' or 'disable'.")

    payload = {
        "action_name": action_name,
        "pixel_ratio": 2.55,
        "visual_style": "dark",
        "params": "{}"
    }

    response = requests.post(url, headers=headers, json=payload)
    try:
        response_data = response.json()
    except ValueError:
        response_data = {"error": "Invalid response format"}

    return response.status_code, response_data

def main():
    token = input("Please enter your Clubhouse token: ").strip()

    while True:
        print("Choose an action:")
        print("1. Enable protected profile")
        print("2. Disable protected profile")
        choice = input("Enter 1 or 2: ").strip()

        if choice == "1":
            status_code, response_data = perform_action("enable", token)
            if status_code == 200:
                print("Enable action was successful.")
            else:
                print(f"Failed to enable protected profile. Status code: {status_code}")
                print(f"Response: {response_data}")
            break
        elif choice == "2":
            status_code, response_data = perform_action("disable", token)
            if status_code == 200:
                print("Disable action was successful.")
            else:
                print(f"Failed to disable protected profile. Status code: {status_code}")
                print(f"Response: {response_data}")
            break
        else:
            print("Invalid choice. Please enter 1 or 2.")

if __name__ == "__main__":
    main()
