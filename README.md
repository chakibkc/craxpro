# CraxPro

Python automation script for creating forum posts from rotating title/data files.

## Overview

CraxPro reads paired lines from:

- `craxpro/data/titlecrax.txt`
- `craxpro/data/datacrax.txt`

For each pair, it builds a forum post payload, sends it with `httpx`, writes the response to `logs.txt`, waits for a random delay, and continues until the input files are empty. The project also validates that both data files contain the same number of lines before running.

Use this project only on systems and accounts you own or have explicit permission to automate. Do not use it to publish private, stolen, fraudulent, or otherwise unauthorized data.

## Project Structure

```text
.
├── craxpro/
│   ├── config.py          # Tags and rotating request headers
│   ├── credit.py          # Profile credit lookup helper
│   ├── getters.py         # Environment and data-file readers
│   ├── main.py            # Main posting loop
│   ├── validator.py       # Input validation helpers
│   ├── logs.txt           # Runtime log output
│   └── data/
│       ├── datacrax.txt   # One message/data item per line
│       └── titlecrax.txt  # One title per line
├── requirements.txt
└── README.md
```

## Requirements

- Python 3.10+
- A forum account/session that you are authorized to automate
- Valid request/session values in a local `.env` file

Install dependencies:

```bash
python -m pip install -r requirements.txt
```

## Configuration

Create a `.env` file in the directory where you run the script:

```env
XFTOKEN=your_xf_token
COOKIES={"cookie_name":"cookie_value"}
LINK=example.com
PROFILE=your-profile-path
```

Notes:

- `XFTOKEN` is the forum request token.
- `COOKIES` must be valid JSON because the script loads it with `json.loads`.
- `LINK` should not include `https://`.
- `PROFILE` is passed to the credit/profile helper.

Do not commit `.env`, cookies, tokens, or real session data to GitHub.

## Input Files

Add one item per line in each data file:

```text
craxpro/data/titlecrax.txt
craxpro/data/datacrax.txt
```

Both files must have the same number of lines. The script removes the first line from each file after using it.

## Usage

From inside the `craxpro` directory, run:

```bash
python main.py
```

The script will:

1. Validate environment settings and input-file lengths.
2. Build a post using the first title and first data line.
3. Send the request.
4. Append response information to `logs.txt`.
5. Wait 70 to 120 seconds before the next post.
6. Stop when the data files are empty.



## License

Add a license file if you plan to share or accept contributions.
