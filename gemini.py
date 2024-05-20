import google.generativeai

api_key = "REDACTED"
google.generativeai.configure(api_key=api_key)
model = google.generativeai.GenerativeModel('gemini-pro')
response = model.generate_content("What is the meaning of life?")
print(response)
