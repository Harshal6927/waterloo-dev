# Python Discord Code Jam - Sublime Suns

## Local Setup

> This project built using `Python 3.12.x`

### Token

Create a discord application and get token from the [Discord Developer Portal](https://discord.com/developers/applications) and add it to the `.env` file. Refer to the `.env.example` file for the format.

### Database

We are using [pickle](https://docs.python.org/3/library/pickle.html) to store the data. The database file is `data/database.pkl`. You can delete this file to reset the database.

### Virutal Environment

Clone this repo and open the folder, then run the below to commands in the terminal to create a virtual environment.

```bash
py -m venv venv
```

Activate virutal environment

```bash
.\venv\Scripts\activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

### Run the application

```bash
py main.py
```

### Development

If you added any new slash commands or updated the existing ones, you need to sync the commands with the discord server. To sync the commands, first add your discord user id in `cogs/admin.py` file and run the following command in the discord server.

Note: you have to start the bot before running this command

```bash
!sync
```
