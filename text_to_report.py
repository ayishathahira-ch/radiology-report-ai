import os
import openai

openai.api_key = os.getenv("OPENAI_API_KEY")

PROMPT_TEMPLATE = """
You are a medical assistant. Convert the following radiology dictation into a clean, structured report:
"{dictation}"
Format it with Findings and Conclusion sections.
"""

def generate_report_text(dictation):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": PROMPT_TEMPLATE.format(dictation=dictation)}]
    )
    return response.choices[0].message.content.strip()