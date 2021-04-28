# Setup (Mac)

- Install mosquitto (MQTT server/broker)

  ```
  brew install mosquitto
  ```

- Install venv and dependencies

  ```
  python3 -m venv .venv
  source .venv/bin/activate
  pip install -r requirements.txt
  ```

- Start

  ```
  MQTT_PORT=1887 ./broker
  source .venv/bin/activate; MQTT_PORT=1887 ./brain
  source .venv/bin/activate; MQTT_PORT=1887 ./organism2
  ```

  Or:

  ```
  MQTT_PORT=1887 tmux
  # inside tmux
  ./broker
  source .venv/bin/activate; ./brain
  source .venv/bin/activate; ./organism2
  ```

# Other stuff

MQTT prototype

What do I want to test?

Different way of communication for:

- Client 1 Reading an order and executing it
- Client 2 sending an order and seeing that it has been executed
