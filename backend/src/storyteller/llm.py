from anthropic import AsyncAnthropic, HUMAN_PROMPT, AI_PROMPT


async def claude_complete(api_key: str, prompt: str):
    anthropic = AsyncAnthropic(api_key=api_key)
    completion = await anthropic.completions.create(
        model="claude-1-100k",
        max_tokens_to_sample=300,
        prompt=f"{HUMAN_PROMPT} {prompt}{AI_PROMPT}",
    )
    return completion.completion
