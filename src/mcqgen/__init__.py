import os
from dotenv import load_dotenv

load_dotenv()


def main() -> None:
    print("Hello from mcqgen!")
    print(f"GOOGLE_API_KEY: {os.getenv('GOOGLE_API_KEY')}")


if __name__ == "__main__":
    main()
