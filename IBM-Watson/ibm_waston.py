# import dependencies
# open STT service
# open audio source

from ibm_watson import SpeechToTextV1
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

apikey = '0xi8pn8xSMAmubzAK8qPlDDn_ez9bJgS7HXn1Wn8_XFQ'
url = 'https://api.us-south.speech-to-text.watson.cloud.ibm.com/instances/991af58d-129d-4ff2-b7e5-493def2842d7'

authenticator = IAMAuthenticator(apikey)
stt = SpeechToTextV1(authenticator=authenticator)
stt.set_service_url(url)

with open('G2.wav', 'rb') as f:
    res = stt.recognize(audio=f, content_type='audio/wav', model='en-US_BroadbandModel', continuous=True).get_result()
    for sentence_index in range(len(res['results'])):
        text = res['results'][sentence_index]['alternatives'][0]['transcript']
        print(text)


# with open('output.txt', 'w') as out:
#     out.writelines(text)
