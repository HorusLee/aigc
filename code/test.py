from openai import OpenAI

client = OpenAI(api_key="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")


def get_image_url(prompt):
    response = client.images.generate(
        model="dall-e-2",
        prompt=prompt,
        size="1024x1024",
        quality="standard",
        n=1,
    )
    image_url = response.data[0].url
    return image_url


speech_file_path = "..\speech\speech9.mp3"
response = client.audio.speech.create(
    model="tts-1",
    voice="echo",
    input="""放你的屁"""
)

response.stream_to_file(speech_file_path)
