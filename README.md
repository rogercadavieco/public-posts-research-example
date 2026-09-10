# Public Posts Research Example

Small personal, read-only example for exploring public posts about business operations and automation.

## Purpose

This project is for personal learning and non-commercial research. It reads public posts from selected business and operations communities, then filters them for signals of manual or painful processes. Reddit is the current source used by this example.

The results may be used for personal learning, ideas for educational LinkedIn posts about automation, and small automation experiments for learning purposes.

This example does not contact or profile users, sell or redistribute platform data, or store collected data on disk. It only prints matching post titles and short text previews to the terminal during a run.

## Setup

Requirements: Python 3.9+, requests, a Reddit application with OAuth credentials, and a Reddit account authorized to use that application.

Install requests with: python -m pip install requests

Set these environment variables without committing them to Git: REDDIT_CLIENT_ID, REDDIT_CLIENT_SECRET, REDDIT_USERNAME, REDDIT_PASSWORD. Optional variables are REDDIT_SUBREDDIT=smallbusiness and REDDIT_LIMIT=50.

Use this example only with an application and account approved for the stated personal, non-commercial purpose.

## Usage

Run: python public_posts_example.py

The script calls Reddit OAuth, reads the hot listing for the selected subreddit, filters for a small set of manual-process keywords, prints matching posts, and keeps no local file or database.

## Scope and limits

Use a clear user agent, keep request volume low, respect Reddit policies and API limits, and stop using the example if access is not approved. This repository does not automate posting, messaging, voting, scraping, user profiling, or long-term retention.
