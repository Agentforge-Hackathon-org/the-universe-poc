import ai21
import openai
from anthropic import AsyncAnthropic, HUMAN_PROMPT, AI_PROMPT


async def ai21_complete(api_key: str, prompt: str):
    ai21.api_key = api_key
    response = ai21.Completion.execute(
        model="j2-ultra",
        prompt=prompt,
        maxTokens=200,
        temperature=0.4,
    )
    return response


async def gpt_complete(api_key: str, prompt: str):
    openai.api_key = api_key

    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt}
        ]
    )

    return completion.choices[0].message


async def claude_complete(api_key: str, prompt: str):
    anthropic = AsyncAnthropic(api_key=api_key)
    completion = await anthropic.completions.create(
        model="claude-1-100k",
        max_tokens_to_sample=300,
        prompt=f"{HUMAN_PROMPT} {prompt}{AI_PROMPT}",
    )
    return completion.completion
