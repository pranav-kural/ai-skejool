# AI Skejool

Vertex AI powered personal assistant to quickly plan a productive schedule.

## Features

- **Natural Language Processing**: Understands natural language to create a schedule.
- **Vertex AI**: Uses state-of-the-art text generation models to generate a schedule.
- **Easy to Use**: Simple command line interface to generate a schedule with a single command.

## Setup

### Google Cloud, Vertex AI, Project Setup

Before you can use this app locally, you will have to setup a project on Google Cloud, enable the Vertex AI API for that project, and obtain service account credentials (unless you want to use an alternative authentication mechanism).

1. [Select or create a Cloud Platform project.](https://console.cloud.google.com/project)
2. [Enable billing for your project.](https://cloud.google.com/billing/docs/how-to/modify-project#enable_billing_for_a_project)
3. [Enable the Vertex AI API.](https://cloud.google.com/vertex-ai/docs/start/use-vertex-ai-python-sdk)
4. [Setup Authentication.](https://googleapis.dev/python/google-api-core/latest/auth.html)

Once, you are done with the steps above, you can download the service account credentials as a JSON file and name it `gcl-creds.json`. This file will be used to authenticate the app with Google Cloud APIs.

NOTE: If you name your Google Cloud project something other than `ai-skejool`, you will have to update the `PROJECT_ID` variable in the `skejool.py` file.

### Local Setup

1. Clone the repository and navigate to the directory.
2. Add the `gcl-creds.json` service account credentials file that you downloaded earlier to the root of this directory. You can read more about authentication with Google Cloud APIs [here](https://googleapis.dev/python/google-api-core/latest/auth.html).
3. Install the required packages using `pip install -r requirements.txt`. You may want to use a virtual environment for this, more information [here](https://packaging.python.org/en/latest/guides/installing-using-pip-and-virtual-environments/#creating-a-virtual-environment).
4. Run the script using `python skejool.py getschedule` or `python skejool.py genschedule <basic description of your agenda for today>`.

## Commands

- `genschedule`: Generates a schedule based on the input provided.
  - Usage `python skejool.py genschedule <basic description of your agenda for today>`
  - Quicker execution by providing the description directly as an argument.
- `getschedule`: Provides a prompt to enter a description and then generates a schedule based on the input provided.
  - Usage `python skejool.py getschedule`
  - Easier to describe the agenda in a prompt.

## Example

### Using `genschedule` command

```bash
> python skejool.py genschedule "Wake up around 7, be done with breakfast by 9. Start the day by studying AI for 2 hours, then 1 hour on leetcode. Have a rice bowl in lunch, maximum 60 minutes, and then be ready for a zoom meeting at 4pm. Work on assignment for a few hours and after hitting the gym have dinner by 8pm. Read book before bed for 30 mins. Remember to take small breaks"

>>> "Hello from the AI Skejool Bot! Here's a productive schedule plan to manage your priorities for today:

    **7:00 AM** - Wake up and get ready for the day.

    **7:30 AM** - Eat a healthy breakfast.

    **8:00 AM to 10:00 AM (2 hours)**: Study AI.

    **10:00 AM to 11:00 AM (1 hour)**: Work on LeetCode problems.

    **11:00 AM to 12:00 PM (1 hour)**: Take a break and go for a walk or do some other activity that you enjoy.

    **12:00 PM to 1:00 PM (1 hour)**: Eat lunch.

    **1:00 PM to 4:00 PM (3 hours)**: Work on your assignment.

    **4:00 PM to 5:00 PM (1 hour)**: Attend your Zoom meeting.

    **5:00 PM to 6:00 PM (1 hour)**: Go to the gym or do some other physical activity.

    **6:00 PM to 7:00 PM (1 hour)**: Eat dinner.

    **7:00 PM to 8:00 PM (1 hour)**: Read a book or do some other activity that you enjoy.

    **8:00 PM to 9:00 PM (1 hour)**: Get ready for bed and go to sleep.

    Remember to take breaks in between activities and to listen to your body. If you start to feel tired, take a break and do something else for a while. You can also use the Pomodoro Technique to help you stay focused and avoid burnout.
```

### Using `getschedule` command

```
> python skejool.py getschedule

>>> Whats your agenda for today?: Wake up around 7, be done with breakfast by 9. Start the day by studying AI for 2 hours, then 1 hour on leetcode. Have a rice bowl in lunch, maximum 60 minutes, and then be ready for a zoom meeting at 4pm. Work on assignment for a few hours and after hitting the gym have dinner by 8pm. Read book before bed for 30 mins. Remember to take small breaks

>>> Hello from the AI Skejool Bot! Here's a productive schedule plan to manage your priorities for today:

    **7:00 AM** - Wake up and get ready for the day.

    **7:30 AM** - Eat a healthy breakfast.

    **8:00 AM to 10:00 AM (2 hours)**: Study AI.

    **10:00 AM to 11:00 AM (1 hour)**: Work on LeetCode problems.

    **11:00 AM to 12:00 PM (1 hour)**: Take a break and go for a walk or do some other activity that you enjoy.

    **12:00 PM to 1:00 PM (1 hour)**: Eat lunch.

    **1:00 PM to 4:00 PM (3 hours)**: Work on your assignment.

    **4:00 PM to 5:00 PM (1 hour)**: Attend your Zoom meeting.

    **5:00 PM to 6:00 PM (1 hour)**: Go to the gym or do some other physical activity.

    **6:00 PM to 7:00 PM (1 hour)**: Eat dinner.

    **7:00 PM to 8:00 PM (1 hour)**: Read a book or do some other activity that you enjoy.

    **8:00 PM to 9:00 PM (1 hour)**: Get ready for bed and go to sleep.

    Remember to take breaks in between activities and to listen to your body. If you start to feel tired, take a break and do something else for a while. You can also use the Pomodoro Technique to help you stay focused and avoid burnout.
```

## Contributing

Feel free to create a fork or use the code.
