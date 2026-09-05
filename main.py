from openai import OpenAI
from dotenv import load_dotenv
import os

# Load API key from .env
load_dotenv()

# Create AI client
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


def analyze_resume(resume):
    prompt = f"""
You are an expert career and resume assistant.

Analyze the following resume and give beginner-friendly,
practical feedback.

Resume:
{resume}

Provide the following:

1. Overall Resume Score out of 10
2. Strengths
3. Areas to Improve
4. Skills that could be added
5. Suggestions to improve the Career Objective
6. Suggestions to improve Projects section
7. Important tips for getting an internship
"""

    response = client.responses.create(
        model="gpt-5.6-luna",
        input=prompt
    )

    return response.output_text


print("=" * 50)
print("        🤖 AI RESUME ANALYZER")
print("=" * 50)

print("\nPaste your resume below.")
print("When finished, type END on a new line.\n")

resume_lines = []

while True:
    line = input()

    if line.strip().upper() == "END":
        break

    resume_lines.append(line)

resume = "\n".join(resume_lines)

if resume.strip() == "":
    print("\n❌ No resume was entered.")
else:
    print("\n⏳ Analyzing your resume with AI...\n")

    try:
        result = analyze_resume(resume)

        print("=" * 50)
        print("        📋 AI RESUME ANALYSIS")
        print("=" * 50)

        print(result)

    except Exception as error:
        print("\n❌ Something went wrong.")
        print("Please check your API key and internet connection.")
        print("\nError:", error)
