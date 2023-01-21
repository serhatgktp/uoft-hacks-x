import cohere

apiKey = 'wiNr6FZZRUdVMXFinDLwBxixNUPm6RePVy4VRjVu'

co = cohere.Client(f'{apiKey}')
prompt = '''
    I agree that abortion should be illegal because
'''

response = co.generate(
  model='xlarge',
  prompt=f'{prompt}',
  max_tokens=250,
  temperature=0.2,
  k=0,
  p=0.75,
  frequency_penalty=0,
  presence_penalty=0,
  stop_sequences=[],
  return_likelihoods='NONE')
print('Prediction: {}'.format(response.generations[0].text))