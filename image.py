from openai import OpenAI

client = OpenAI()

# Generate an image
response = client.images.generate(prompt="A futuristic cityscape at sunset",
                                  n=1,
                                  size="1024x1024")
# Get the URL of the generated image
image_url = response.data[0].url
print("Generated Image URL:", image_url)