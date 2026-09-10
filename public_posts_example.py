"""Minimal personal, read-only Reddit pain-point example."""

from __future__ import annotations

import os
import sys
from typing import Any

import requests

TOKEN_URL = "https://www.reddit.com/api/v1/access_token"
API_BASE_URL = "https://oauth.reddit.com"
USER_AGENT = "personal-research-example/0.1 by reddit-ideas-research"
KEYWORDS = ("manually", "spreadsheet", "copy and paste", "we lose time", "no integration")


def required_env(name: str) -> str:
    value = os.getenv(name)
    if not value:
        raise RuntimeError(f"Missing required environment variable: {name}")
    return value


def get_access_token() -> str:
    response = requests.post(
        TOKEN_URL,
        auth=(required_env("REDDIT_CLIENT_ID"), required_env("REDDIT_CLIENT_SECRET")),
        data={"grant_type": "password", "username": required_env("REDDIT_USERNAME"), "password": required_env("REDDIT_PASSWORD")},
        headers={"User-Agent": USER_AGENT},
        timeout=30,
    )
    response.raise_for_status()
    token = response.json().get("access_token")
    if not token:
        raise RuntimeError("Reddit did not return an access token")
    return token


def get_hot_posts(token: str, subreddit: str, limit: int) -> list[dict[str, Any]]:
    response = requests.get(
        f"{API_BASE_URL}/r/{subreddit}/hot.json",
        params={"limit": limit, "raw_json": 1},
        headers={"Authorization": f"bearer {token}", "User-Agent": USER_AGENT},
        timeout=30,
    )
    response.raise_for_status()
    return [child.get("data", {}) for child in response.json().get("data", {}).get("children", [])]


def matches_keywords(post: dict[str, Any]) -> list[str]:
    text = " ".join(str(post.get(field, "")) for field in ("title", "selftext")).casefold()
    return [keyword for keyword in KEYWORDS if keyword in text]


def main() -> int:
    subreddit = os.getenv("REDDIT_SUBREDDIT", "smallbusiness")
    try:
        limit = min(max(int(os.getenv("REDDIT_LIMIT", "50")), 1), 100)
        posts = get_hot_posts(get_access_token(), subreddit, limit)
    except (RuntimeError, ValueError, requests.RequestException) as error:
        print(f"Error: {error}", file=sys.stderr)
        return 1

    found = 0
    for post in posts:
        matched = matches_keywords(post)
        if not matched:
            continue
        found += 1
        title = str(post.get("title", "Untitled")).strip()
        body = " ".join(str(post.get("selftext", "")).split())
        preview = body[:280] + ("..." if len(body) > 280 else "")
        permalink = post.get("permalink", "")
        print(f"\n[{', '.join(matched)}] {title}")
        if preview:
            print(preview)
        if permalink:
            print(f"https://www.reddit.com{permalink}")

    print(f"\nFound {found} matching post(s) in r/{subreddit}.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
