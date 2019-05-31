import markovify
import time

from slackclient import SlackClient


BOT_TOKEN = ""
GROUP_TOKEN = ""


def main():
    """
    Startup logic and the main application loop to monitor Slack events.
    """

    # Create the slackclient instance
    sc = SlackClient(BOT_TOKEN)

    # Connect to slack
    if not sc.rtm_connect():
        raise Exception("Couldn't connect to slack.")

    # Where the magic happens

    while True:
        # Examine latest events
        for slack_event in sc.rtm_read():

            # Disregard events that are not messages
            if not slack_event.get('type') == "message":
                continue

            message = slack_event.get("text")
            user = slack_event.get("user")
            channel = slack_event.get("channel")

            if not message or not user:
                continue

            ######
            # Commands we're listening for.
            ######

            if "ping" in message.lower():
                sc.rtm_send_message(channel, "ping")

        # Sleep for half a second
        time.sleep(0.5)


if __name__ == '__main__':
    main()