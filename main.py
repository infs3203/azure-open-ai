import os
from openai import AzureOpenAI

endpoint = "https://60099-m6nkk29c-swedencentral.cognitiveservices.azure.com/"
model_name = "gpt-4o"
deployment = "gpt-4o-vanilson"

subscription_key = "<API_KEY>"
api_version = "2024-12-01-preview"

client = AzureOpenAI(
    api_version=api_version,
    azure_endpoint=endpoint,
    api_key=subscription_key,
)
example_output = ''' 
{
  "question": "Which of the following types of loops are commonly used in Python for iterative operations?",
  "options": [
    "A: "for loop and while loop",
    "B: "do-while loop and repeat loop",
    "C: "foreach loop and until loop",
    "D: "if loop and switch loop"
  ],
  "correct_answer": 0,
  "explanation": "In Python, the two commonly used looping constructs are 'for' loop and 'while' loop. Python does not have 'do-while' loops, 'foreach loops', or 'until loops' natively."
}
'''

def generate_question(topic):

    response = client.chat.completions.create(
        messages=[
            {
                "role": "system",
                "content": "You are AI designed to generate a single MC question for a given topic. The output must be a JSON Object.",
            },
            {
                "role": "user",
                "content": "Topic: loops in Python",
            },
            {
                "role": "assistant",
                "content": f"{example_output}",
            },
            {
                "role": "user",
                "content": f"Topic: {topic}",
            }
        ],
        max_tokens=4096,
        temperature=1.0,
        model=deployment
    )

    return response.choices[0].message.content

q1 = generate_question("loops in Python")
q2 = generate_question("CI/CD pipeline")

print(q1)
print(q2)