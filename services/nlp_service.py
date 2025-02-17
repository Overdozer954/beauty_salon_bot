import openai

class NLPService:
    def __init__(self, api_key):
        openai.api_key = api_key

    async def get_response(self, prompt):
        response = openai.Completion.create(
            engine="text-davinci-003",  # Или другая модель
            prompt=prompt,
            max_tokens=150
        )
        return response.choices[0].text.strip()