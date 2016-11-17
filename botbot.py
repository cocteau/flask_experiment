from os import environ
from time import sleep
from slackclient import SlackClient

slack_token = environ.get("SLACK_TOKEN")
bot_id = environ.get("BOT_ID")

at_bot = "<@" + bot_id + ">"
sc = SlackClient(slack_token)

delay = 1 # 1 second delay between reading from firehose
if sc.rtm_connect():
    print("StarterBot connected and running!")
    while True:
        output_list = sc.rtm_read()
        if output_list and len(output_list) > 0:
            for output in output_list:
                if output and 'text' in output and at_bot in output['text']:
                    # return text after the @ mention, whitespace removed
                    print output['text']
        sleep(delay)
else:
    print "Connection failed. Invalid Slack token or bot ID?"
