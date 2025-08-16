"""Utility to display selected environment variables."""

import os


def dump_env() -> None:
    for key in ["DATABASE_URL", "API_URL"]:
        print(f"{key}={os.getenv(key, '')}")


if __name__ == "__main__":
    dump_env()
