import facebook
import time
import os
import random


def uploader(token, title, currentframe, length):
    token = token
    fb = facebook.GraphAPI(access_token=token)

    # profile = fb.get_object(id=102750666053085, fields='feed', limit='100')
    # latestMessage = profile['feed']['data'][0]['message']
    # latestFrame = int(latestMessage.split(" ")[-4])

    title = title
    currentFrame = currentframe
    length = length

    print(currentFrame)

    if not os.path.isdir('./frames'):
        os.mkdir('./frames')

    while currentFrame <= length:
        imagePath = './frames/' + str(currentFrame) + '.jpg'
        image = open(imagePath, 'rb')
        fb.put_photo(image=image, message=title + "\nFrame " + str(currentFrame) + " out of " + str(length))
        print("Uploaded " + str(currentFrame))
        time.sleep(random.choice([60, 5]))

        currentFrame += 1

    time.sleep(86400)


uploader(
    'EAAHyLBJeZB38BAAZCY3gee5J0jspLRsCQvjv9UtKIqMuCTNZALqZCtRVHdPXcsLHJ12cr9ghjHUkTMa7YgqEB4sqYEYdshZA9NXyjhDtXhWDrsL0Q5ViOvGgEu6y6PXf7WO7uWun5K17RvxgKaQeiNM3qlNcwWN9jXbiuuLJ1TrZACy3IDSdOp',
    'Suratha - IRAJ Ft. Killer B & Kaizer',
    1,
    2448
)
