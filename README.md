# HTTP Test DANE

This implements a DANE for testing purposes according to ISO/IEC 23009-5 SAND.
It implementes a HTTP SAND Channel that a DASH client can connect to.
SAND messages that may be sent and received by this test DANE do not reflect
real operations but merely serve as example behaviour.

## Requirements

- [pip](https://pip.pypa.io/en/stable/)

## Installation

```pip install -r requirements.txt```

## Usage

```python hhtp_test_dane.py run --port tcp_port```

By default, the server listens on port 5000.

## Help

```python http_test_dane run --help```

```
Usage: http_test_dane.py run [OPTIONS]

  Run the Test DANE and listen to port 'port'.

Options:
  --port INTEGER  Listening port of the Test DANE.
  --help          Show this message and exit.
```

## Endpoints

### /pc

Responds with a DaneCapabilites Proxy Caching to a POST request.

