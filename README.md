# 🗓️ Family Birthday Calendar Creator (Google Calendar API)

This Python script automatically creates a separate calendar in your Google Calendar for all family birthdays.

Each event includes:
- Start time: **09:00 AM**
- Duration: **1 hour**
- Repeats: **Annually**
- Guest invitations sent to email addresses loaded from a CSV file

---

## 📂 Input Format

### `birthdays.csv`
A list of birthdays in this format:

```
Name,MM-DD
John Smith,01-14
Jane Doe,03-27
...
```

### `emails.csv`
A list of emails, one per line:

```
email
someone@example.com
another@example.com
...
```

---

## 🔧 Prerequisites

1. Go to [Google Cloud Console](https://console.cloud.google.com/).
2. Create a new project (e.g., `BirthdayEvents`).
3. Enable **Google Calendar API**:
   - APIs & Services → Enable APIs → Search "Google Calendar API" → Enable
4. In the **Credentials** section:
   - Create an **OAuth Client ID** of type `Desktop App`
   - Download the file as `credentials.json`
5. In **OAuth consent screen**:
   - Add your Gmail to the **Test users** list.

---

## 📦 Install dependencies

```bash
pip install --upgrade google-api-python-client google-auth-httplib2 google-auth-oauthlib
```

---

## ▶️ Run the script

1. Download or clone the repository.
2. Place the following files in the same folder:
   - `credentials.json`
   - `birthdays.csv`
   - `emails.csv`
3. Delete `token.json` if it exists (to reset authentication).
4. Run:

```bash
python create_family_birthdays_calendar.py
```

A browser window will open for OAuth authentication.

---

## 📅 What the script does

- Creates a new calendar: **"Family Birthdays"**
- Adds events with:
  - Title: `Birthday: Name`
  - Time: 09:00–10:00 AM
  - Annual recurrence
  - Guest invitations to all listed emails

---

## ⚙️ Customization

To modify birthday list or guests, just edit:

- `birthdays.csv`
- `emails.csv`

No need to change the code.

---

## 🔒 Security note

Do **NOT** upload your credentials or token to public repositories.

Add this to `.gitignore`:

```
credentials.json
token.json
```

---

## 🤖 About

This script was generated using OpenAI's ChatGPT and utilizes the Google Calendar API (v3).
