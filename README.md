# Reddit Ideas Research

Small personal, read-only example for exploring public Reddit posts about business operations and automation.

## Purpose

This project is for personal learning and non-commercial research. It reads public posts from selected business and operations subreddits, then filters them for signals of manual or painful processes.

The results may be used for personal learning, ideas for educational LinkedIn posts about automation, and small automation experiments for learning purposes.

This example does not contact or profile Reddit users, sell or redistribute Reddit data, or store Reddit data on disk. It only prints matching post titles and short text previews to the terminal during a run.

The script represents the core logic of a private n8n workflow: authenticate with Reddit OAuth, read public posts, filter by keywords, and extract lightweight tags for inspection.

## Setup

Requirements: Python 3.9+, requests, a Reddit application with OAuth credentials, and a Reddit account authorized to use that application.

Install requests with: python -m pip install requests

Set these environment variables without committing them to Git: REDDIT_CLIENT_ID, REDDIT_CLIENT_SECRET, REDDIT_USERNAME, REDDIT_PASSWORD. Optional variables are REDDIT_SUBREDDIT=smallbusiness and REDDIT_LIMIT=50.

The Reddit app must be approved for this personal, non-commercial experiment.

## Usage

Run: python reddit_example.py

The script calls Reddit OAuth, reads the hot listing for the selected subreddit, prints matching posts, and keeps no local file or database.

## Scope and limits

Use a clear user agent, keep request volume low, respect Reddit policies and API limits, and stop using the example if access is not approved. This repository does not automate posting, messaging, voting, scraping, user profiling, or long-term retention.
