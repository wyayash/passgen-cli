from zxcvbn import zxcvbn
import secrets
import string
import json
import argparse

def load_config():
    with open("config.json", "r") as f:
        return json.load(f)

def generate_password(length):
    chars = string.ascii_letters + string.digits + string.punctuation
    return ''.join(secrets.choice(chars) for _ in range(length))

def check_strength(password):
    result = zxcvbn(password)
    labels = ["Very weak", "Weak", "Fair", "Strong", "Very strong"]
    return result["score"], labels[result["score"]]

def save_password(password, filename):
    with open(filename, "a") as f:
        f.write(password + "\n")
    print(f"Saved to {filename}")

def main():
    config = load_config()
    parser = argparse.ArgumentParser(description="Password Generator")
    parser.add_argument("-l", "--length", type=int, help="Password length")
    args = parser.parse_args()

    length = args.length or 16
    if length < config["min_length"] or length > config["max_length"]:
        print(f"Length must be between {config['min_length']} and {config['max_length']}")
        return

    password = generate_password(length)
    print(f"Generated: {password}")
    score, label = check_strength(password)
    print(f"Strength:  {label} ({score}/4)")
    save_password(password, config["password_file"])

if __name__ == "__main__":
    main()