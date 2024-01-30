import typer
from typing_extensions import Annotated
import vertexai
from vertexai.language_models import TextGenerationModel
from google.cloud import aiplatform
from google.oauth2 import service_account

PROJECT_ID="ai-skejool"
MODEL_NAME="text-bison@001"
MODEL_PARAMS={
    "temperature": 0.5,
    "max_output_tokens": 1024
}
CREDENTIALS = service_account.Credentials.from_service_account_file(
    'gcl-creds.json')
SYSTEM_PROMPT = """
    You are an AI assistant that generates a productive schedule for a day given an agenda describing the main tasks, activities and priorities. 
    You must prepare the schedule such that it first describes the time when the activity starts, then the time when that activity ends, followed by total duration of that activity. For example, if there is an activity to be performed for an hour starting at 10am, you must show it as: '10:00 AM to 11:00 AM (1 hour): <activity to be performed>'.
    You must also keep reasonable time gaps between the events.
    Provide a motivational message and/or an inspirational quote to start the day.
    Please start your response with \"Hello from the AI Skejool Bot! Here's a productive schedule plan to manage your priorities for today:\"

    Agenda: """

app = typer.Typer()

def gen_schedule(prompt: str):
    """
    
    """
    aiplatform.init(
        project=PROJECT_ID,
        credentials=CREDENTIALS,)
    initial_prompt = SYSTEM_PROMPT
    vertexai.init(project=PROJECT_ID)
    model = TextGenerationModel.from_pretrained(MODEL_NAME)
    return model.predict(initial_prompt + prompt, **MODEL_PARAMS)

@app.command()
def genschedule(agenda: Annotated[str, typer.Argument(help="Please describe your agenda or main priorities for today. Example: \"I have a meeting with the team at 10am, followed by a lunch with a client at 12pm. Also, have to work on project around 3pm for at least 2 hours. Have to run to the grocery store in late evening.\"")]):
    typer.echo(gen_schedule(agenda).text)

@app.command()
def getschedule(agenda: Annotated[str, typer.Option(prompt="Whats on agenda today?")]):
    if agenda == "exit":
        print("Goodbye!")
    else:
        typer.echo(gen_schedule(agenda).text)

if __name__ == "__main__":
    app()
