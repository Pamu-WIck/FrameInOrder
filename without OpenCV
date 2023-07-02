import facebook
import time
import os
import random

token = 'token here'
fb = facebook.GraphAPI(access_token=token)

profile = fb.get_object(id=102750666053085, fields='feed', limit='100')
# latestMessage = profile['feed']['data'][0]['message']
# latestFrame = int(latestMessage.split(" ")[-4])

title = "Title"
currentFrame = 647
length = 1989

print(currentFrame)

if not os.path.isdir('./frames'):
    os.mkdir('./frames')

while currentFrame <= length:
    imagePath = './frames/' + str(currentFrame) + '.jpg'
    image = open(imagePath, 'rb')
    fb.put_photo(image=image, message=title + " Frame " + str(currentFrame) + " out of " + str(length))
    print("Uploaded " + str(currentFrame))
    time.sleep(random.choice([60,120]))

    currentFrame += 1

time.sleep(86400)
