from openai import OpenAI
client = OpenAI()

response = client.chat.completions.create(
  model="gpt-3.5-turbo",
  messages=[
    {
      "role": "system",
      "content": "You are a judge in the Supreme Court of Singapore. If all the requirements are met, grant the order. if the application does not meet the directions, dismiss it."
    },
    {
      "role": "user",
      "content": "These are the directions regarding substituted service: \n\n```\n(1) In any application for substituted service, the applicant should persuade the Court that the proposed mode of substituted service will probably be effectual in bringing the document in question to the notice of the person to be served.\n(2) Two reasonable attempts at personal service should be made before an application for an order for substituted service is filed. In an application for substituted service, the applicant shall demonstrate by way of affidavit why he or she believes that the attempts at service made were reasonable.\n(6) If substituted service is by electronic mail, it has to be shown that the electronic mail account to which the document will be sent belongs to the person to be served and that it is currently active.\n```\n\nI am a lawyer applying for substituted service. This is my submission:\n\n```\nYour honour, I am Mr X for the Plaintiff. This is an application for substituted service. We wish to send the originating claim to the defendant by email. We humbly request to grant the order. \n```\nWhat is your next line?"
    },
    {
      "role": "assistant",
      "content": "Based on the directions regarding substituted service, I would advise you to provide more details and evidence in support of your application. Specifically, you should address the following points in your submission:\n\n1. Explain why substituted service by email is likely to be effectual in bringing the document to the notice of the defendant.\n2. Provide information on the attempts at personal service that have been made and why they were considered reasonable.\n3. Demonstrate that the email account to which the document will be sent belongs to the defendant and is currently active.\n\nTherefore, I would recommend expanding your submission to address these points before the court can consider granting the order for substituted service by email."
    },
    {
      "role": "assistant",
      "content": "Dismiss the application as it does not provide sufficient details or evidence to meet the requirements for substituted service."
    }
  ],
  temperature=1,
  max_tokens=256,
  top_p=1,
  frequency_penalty=0,
  presence_penalty=0
)
