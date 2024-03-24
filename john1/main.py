import os
from openai import OpenAI
client = OpenAI(
  api_key = os.environ['openaikey']
)

response = client.chat.completions.create(
  # change the model as desired
  model="gpt-3.5-turbo-16k-0613",
  messages=[
    {
      "role": "system",
      "content": "You are John's lawyer. "
    },
    {
      "role": "user",
      "content": "Title: John vs. Doe \nFacts: John leased an apartment from Doe. Under the lease agreement, rent is due in arrears on the 5th day of the relevant month. Doe has brought an action to recover the rent and foreclose John's lease. John is a food delivery driver and due to a recent accident, has not been able to earn enough money to pay the rent in time. If the lease is foreclosed, John's family of four will have no place to live. Usually, Doe is understanding and will give John at least a few weeks to pay the rent. However, recently there have been many people who are enquiring about renting John's place. Doe's wife has also been giving John and his family evil stares recently. \nCome up with a strategy to get Doe to restructure John's overdue payments."
    }
  ],
  temperature=1,
  max_tokens=256,
  top_p=1,
  frequency_penalty=0,
  presence_penalty=0
)

print(response)
