# AI-Skejool Bot
# Generate a productive schedule for a day given an agenda describing the main tasks, activities and priorities.
# source: https://github.com/pranav-kural/

# Install dependencies: pip install -r requirements.txt
import typer
from typing_extensions import Annotated
from vertexai.language_models import TextGenerationModel
from google.cloud import aiplatform
from google.oauth2 import service_account

# Project variables

# Project name as on Google Cloud
PROJECT_ID="ai-skejool"
# Model to be used for inference
MODEL_NAME="text-bison@001"
# Model parameters
MODEL_PARAMS={
    "temperature": 0.5,
    "max_output_tokens": 1024
}
# Credentials from your service account credentials file
CREDENTIALS = service_account.Credentials.from_service_account_file(
    'gcl-creds.json')
# Prompt for LLM model
SYSTEM_PROMPT = """
    You are an AI assistant that generates a productive schedule for a day given an agenda describing the main tasks, activities and priorities. 
    You must prepare the schedule such that it first describes the time when the activity starts, then the time when that activity ends, followed by total duration of that activity. For example, if there is an activity to be performed for an hour starting at 10am, you must show it as: '10:00 AM to 11:00 AM (1 hour): <activity to be performed>'.
    You must also keep reasonable time gaps between the events.
    Provide a motivational message and/or an inspirational quote to start the day.
    Please start your response with \"Hello from the AI Skejool Bot! Here's a productive schedule plan to manage your priorities for today:\"

    Agenda: """
# Typer instance
app = typer.Typer()

# Method to handle model invocation and response
def gen_schedule(agenda: str):
    """
    Method to query the text generation model and return the response
    :param agenda: Takes as input a string describing the main tasks, activities and priorities
    :return: The response from the model
    """
    # Initialize Vertex AI with the project and credentials
    aiplatform.init(
        project=PROJECT_ID,
        credentials=CREDENTIALS,)
    # Get the pre-trained text-generation model
    model = TextGenerationModel.from_pretrained(MODEL_NAME)
    # Query the model with system prompt and agenda, and return the response
    return model.predict(SYSTEM_PROMPT + agenda, **MODEL_PARAMS)

# command to generate schedule by taking agenda as command line argument
@app.command()
def genschedule(agenda: Annotated[str, typer.Argument(help="Please describe your agenda or main priorities for today. Example: \"I have a meeting with the team at 10am, followed by a lunch with a client at 12pm. Also, have to work on project around 3pm for at least 2 hours. Have to run to the grocery store in late evening.\"")]):
    """
    Generate a productive schedule for a day given an agenda describing the main tasks, activities and priorities.
    :param agenda: Takes as input a string describing the main tasks, activities and priorities
    """
    typer.echo(gen_schedule(agenda).text)

# command to generate schedule after taking agenda through prompt
@app.command()
def getschedule(agenda: Annotated[str, typer.Option(prompt="Whats on agenda today?")]):
    """
    Get a productive schedule for a day given an agenda describing the main tasks, activities and priorities.
    :param agenda: Takes as input a string describing the main tasks, activities and priorities
    """
    if agenda == "exit":
        print("Goodbye!")
    else:
        typer.echo(gen_schedule(agenda).text)

if __name__ == "__main__":
    # Run the Typer app
    app()
