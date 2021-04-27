#!/usr/bin/env python
#
# Simulates an organism

import time

import paho.mqtt.client as mqtt
import path.mqtt.publish as publish

from config import config


# Behavior:
#
# - without_air
# - breathing
#
# After receiving a "breathe"
# command, I will "breathe"
# for 2.5s and stop.
#
# When I stop, I'll be without air :D

# Lungs.breathe
# Lungs.stop_breathing
#
# MQTT client
#
# on_message:
# > if "breathe"
# >   tell lungs to breathe


class Lungs:
    def breathe(self):
        # send message that I am breathing
        # wait 2.5 seconds
        # stop breathing

    def stop_breathing(self):
        # send message that I stopped breathing


class Ear:
    """
    I am responsible for listening
    commands and redirecting them
    to the brain.
    """
    def __init__(self):
        # create mqtt client
        self.mqttc = mqtt.Client()
        # listen to stuff
        self.mqttc.on_message = self._message
        # set up brain (placeholder)
        self._brain = None

    def connect_to_brain(self, brain):
        self._brain = brain

    def _message(self, client,  userdata, message):
        # gather content of message
        payload = str(message.payload)
        # redirect message to brain
        if self._brain is None:
            raise RuntimeError('not connected to brain yet')
        self._brain.receive_msg(payload)

    def listen(self):
        """
        Listen for new messages.
        """
        # qos=2 garantees no order is lost, and I don't die :D
        # XXX: subscriptions are better made at on_connect instead of here
        self.mqttc.subscribe('orders', qos=2)
        # connect to server
        self.mqttc.connect(config.ip, port=config.port, keepalive=30)
        # Retry connection if it fails, infinite times if needed to :D
        self.mqttc.loop_forever(retry_first_connection=True)


class Brain:
    """
    I am responsible for piping commands to the
    lungs.
    """
    def __init__(self):
        self._lungs = None

    def connect_to_lungs(self, lungs):
        self._lungs = lungs

    def receive_msg(text):
        if text == 'breathe':
            if self._lungs is None:
                raise RuntimeError('lungs not connected yet')
            self._lungs.breathe()
        else:
            raise RuntimeError('BUG IN THE BRAIN'
                    'Unknown message: '
                    f'{text!r}')


class Body:
    """
    I am a frankstein of stuff

    ^*^
    """
    def __init__(self, ear, brain, lungs):
        self.ear = ear
        self.brain = brain
        self.lungs = lungs

        ear.connect_to_brain(brain)
        brain.connect_to_lungs(lungs)

    def begin_work(self):
        self.ear.listen()


def main():
    brain = Brain()
    ear = Ear()
    lungs = Lungs()

    body = Body(ear, brain, lungs)
    body.begin_work()
