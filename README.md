# First Honeypot

A simple Python-based honeypot that listens on port 2222 and logs incoming connection attempts.  
Designed as a lightweight trap to catch unauthorized access attempts for learning and monitoring purposes.

---

## Features

- Listens for incoming TCP connections on port 2222  
- Logs connection IP addresses and any received data to a file  
- Minimal dependencies and easy to run  
- Designed for educational use and basic monitoring

---

## Installation

Make sure you have Python 3.13 or higher installed.

Clone this repository:

```bash
git clone https://github.com/yourusername/honeypot-lite.git
cd honeypot-lite
```

No additional dependencies are required at this time.

---

## Usage

Run the honeypot script:

```bash
python honeypot.py
```

You should see the following output indicating the honeypot is active:

```
[+] Honeypot listening on port 2222
```

To stop the honeypot, press `Ctrl+C`. You might see a KeyboardInterrupt traceback, which is normal.

---

## Example Connection

You can test the honeypot by connecting via telnet:

```bash
telnet localhost 2222
```

Expected output:

```
Trying ::1...
Connection failed: Connection refused
Trying 127.0.0.1...
Connected to localhost.
Escape character is '^]'.
^CConnection closed by foreign host.
```

---

## Example Logs

Sample log entries created when connections are made:

```
[2025-06-29 12:58:14] Connection from 127.0.0.1:51540 — Data: 
[2025-06-29 12:58:22] Connection from 127.0.0.1:39172 — Data: 
```

Logs are saved in the `logs/connections.log` file.

---

## Project Structure

```
honeypot-lite/
│
├── honeypot.py          # Main honeypot script
├── .gitignore           # Git ignore file to exclude logs and caches
├── logs/                # Directory where connection logs are saved
│   └── connections.log
└── README.md            # This file
```

---

## Future Improvements

- Add alert notifications (e.g., Telegram or email)  
- Implement IP blocking or rate limiting to mitigate attacks  
- Simulate fake services or files to trap attackers further  
- Add configuration options for ports and logging verbosity

---

## Author

ov3rfl0wz — cybersecurity enthusiast and learner.

---

## License

This project is open source and available under the MIT License.
