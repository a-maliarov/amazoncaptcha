#--------------------------------------------------------------------------------------------------------------

from .solver import AmazonCaptcha
from io import BytesIO
import multiprocessing
import requests
import os

#--------------------------------------------------------------------------------------------------------------

class AmazonCaptchaCollector(object):

    def __init__(self, output_folder = ''):
        self.output_folder = output_folder

    def get_captcha_image(self):
        captcha_page = requests.get('https://www.amazon.com/errors/validateCaptcha')
        captcha_link = captcha_page.text.split('<img src="')[1].split('">')[0]

        response = requests.get(captcha_link)
        image_bytes_array = BytesIO(response.content)

        captcha = AmazonCaptcha(image_bytes_array)
        captcha_image = captcha.img
        captcha_id = ''.join(captcha_link.split('/captcha/')[1].replace('.jpg', '').split('/Captcha_'))
        solution = captcha.solve()

        if solution != 'Not solved':
            print(captcha_link, solution)
            captcha_name = 'dl_' + captcha_id + '_' + solution + '.png'
            path = os.path.join(self.output_folder, captcha_name)
            captcha_image.save(path)

    def distribute_collecting(self, milestone):
        for step in milestone:
            self.get_captcha_image()

    def start(self, target, processes):
        goal = list(range(target))
        milestones = [goal[x: x + target // processes] for x in range(0, len(goal), target // processes)]

        jobs = list()
        for j in range(processes):
            p = multiprocessing.Process(target=self.distribute_collecting, args=(milestones[j], ))
            jobs.append(p)
            p.start()

        for proc in jobs:
            proc.join()

#--------------------------------------------------------------------------------------------------------------
