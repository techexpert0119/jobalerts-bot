# Job Alerts Slack Bot

A Flask application that sends job application reminders to a Slack channel and tracks when users mark applications as completed.

## Features

- Send job application reminders to a Slack channel
- Interactive "I've Applied!" button that users can click when they've applied to a job
- Tracks and displays the total number of applications submitted with progress percentage
- Updates the message when a user marks an application as completed
- Daily reports of job application activity with achievement metrics
- Daily target tracking (80 applications per day)
- Automatic counter reset after daily report

## Project Structure

The application is organized into the following structure:

```
jobalerts/
│
├── app/                   # Main application package
│   ├── __init__.py        # App initialization
│   ├── config.py          # Configuration settings
│   │
│   ├── routes/            # API routes
│   │   ├── __init__.py
│   │   └── slack_routes.py # Slack endpoint handlers
│   │
│   ├── services/          # Business logic services
│   │   ├── __init__.py
│   │   └── slack_service.py # Slack API handling
│   │
│   └── utils/             # Utility functions
│       ├── __init__.py
│       └── counter.py     # Job application counting
│
├── run.py                 # Application entry point
├── send_alert.py          # Helper script to send alerts and reports
├── requirements.txt       # Project dependencies
├── .env.example           # Example environment variables
└── .gitignore             # Git ignore file
```

## Setup

1. Clone this repository

2. Create a virtual environment:

   ```
   python -m venv venv
   ```

3. Activate the virtual environment:

   ```
   # On Windows:
   venv\Scripts\activate
   
   # On macOS/Linux:
   source venv/bin/activate
   ```

4. Install the required dependencies:

   ```
   pip install -r requirements.txt
   ```

5. Create a `.env` file from the example:

   ```
   cp .env.example .env
   ```

6. Edit the `.env` file with your Slack credentials:

   ```
   SLACK_BOT_TOKEN=your_slack_bot_token
   JOB_ALERTS_CHANNEL=your_job_alerts_channel_id
   DAILY_REPORT_CHANNEL=your_daily_report_channel_id
   ```

## Usage

1. Run the application:

   ```
   python run.py
   ```

2. The server will run at `http://localhost:5000`

3. Use the helper script to send alerts or daily reports:

   ```
   python send_alert.py
   ```

   This will give you options to:
   - Send a job alert with an "I've Applied!" button
   - Send a daily report (will reset the application counter)

4. Available API endpoints:
   - Send a job alert: `GET /slack/send_alert`
   - Daily job report: `GET /slack/daily_report`
   - Slack actions webhook: `POST /slack/actions`

## Daily Application Target

The application is configured with a daily target of 80 job applications. You can modify this in `app/config.py` by changing the `DAILY_TARGET_COUNT` value.

The daily report shows:

- Current count vs. target (e.g., 65/80)
- Progress percentage
- Status message based on achievement level
- Automatic counter reset after the report is sent

## Slack App Configuration

For the interactive buttons to work properly, you'll need to:

1. Create a Slack App at <https://api.slack.com/apps>
2. Enable Interactivity for your app
3. Set the Request URL to `https://your-server-url/slack/actions`
   - If running locally, you can use a tunneling service like ngrok
4. Add the necessary Bot Token Scopes:
   - `chat:write`
   - `chat:write.public`
   - `incoming-webhook`
