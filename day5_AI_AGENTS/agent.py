import os
import re
import google.generativeai as genai
from dotenv import load_dotenv
from tools import calculator, web_search, weather

# Load environment variables
load_dotenv()

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

model = genai.GenerativeModel("gemini-2.5-flash")


TOOLS = {
    "calculator": calculator,
    "search": web_search,
    "weather": weather,
}


def ask_agent(query):

    prompt = f"""
You are an AI agent that can answer questions and use tools.

Available tools:

1. calculator
Description: Performs mathematical calculations
Arguments: expression
2. wikipedia
Description: Search Wikipedia summaries
Arguments: topic
3. search
Description: Search the internet
Arguments: query
4. weather
Description: Get current weather for a city
Arguments: city
User Question:
{query}
Respond strictly in this format:
Thought: reasoning about the task
Action: tool name OR none
Action Input: input to the tool

If no tool is needed:
Thought: explain reasoning
Action: none
Action Input: none
"""

    response = model.generate_content(prompt)

    return response.text.strip()


def extract_action(text):

    tool_match = re.search(r"Action:\s*(.*)", text)
    input_match = re.search(r"Action Input:\s*(.*)", text)

    tool = tool_match.group(1).strip() if tool_match else "none"
    tool_input = input_match.group(1).strip() if input_match else None

    return tool, tool_input


def generate_final_answer(query, observation):

    prompt = f"""
User question:
{query}

Observation from tool:
{observation}

Write the final helpful answer.
"""

    response = model.generate_content(prompt)

    return response.text.strip()


def save_query(query):

    with open("queries.txt", "a", encoding="utf-8") as f:
        f.write(query + "\n")


def save_result(query, tool, answer):

    with open("results.txt", "a", encoding="utf-8") as f:
        f.write(f"Query: {query}\n")
        f.write(f"Tool used: {tool}\n")
        f.write(f"Answer:\n{answer}\n")
        f.write("---\n")


def main():

    print("\nAI Agent Ready")
    print("Type 'exit' to quit\n")

    while True:

        query = input("User: ")

        if query.lower() == "exit":
            break

        save_query(query)

        agent_response = ask_agent(query)

        print("\n" + agent_response)

        tool_name, tool_input = extract_action(agent_response)

        if tool_name != "none" and tool_name in TOOLS:

            tool_function = TOOLS[tool_name]

            observation = tool_function(tool_input)

            print(f"Observation: {observation}")

            final_answer = generate_final_answer(query, observation)

            print(f"\nFinal Answer: {final_answer}\n")

            save_result(query, tool_name, final_answer)

        else:

            response = model.generate_content(query)

            answer = response.text.strip()

            print(f"\nFinal Answer: {answer}\n")

            save_result(query, "none", answer)


if __name__ == "__main__":
    main()