<h1 align="center" id="project-title">backpack.tf-ws-service</h1>

<img align="center" src="https://socialify.git.ci/LucasHenriqueDiniz/backpack.tf-ws-service/image?font=KoHo&language=1&name=1&owner=1&theme=Light" alt="backpack.tf-ws-service" width="640" height="320" />

<p align="center">This is a improved version of the original backpack.tf-ws-service, with the focus on being lightweight in MongoDB (so it can be used in free tier) and with a better code structure and logging.</p>

# Table of Contents

This is a table of contents for the README file:

- [Project Title](#project-title)
- [Table of Contents](#table-of-contents)
- [Important Notes](#important-notes)
- [Description](#Description)
- [Features](#features)
- [Requirements](#requirements)
- [Installation](#installation)
- [Issues](#issues)
- [Contribute](#contribute)
- [License](#license)

## Important Notes

- This project is a fork of the original [backpack.tf-ws-service](https://github.com/purplebarber/backpack.tf-ws-service), with the focus on being lightweight in MongoDB (so it can be used in free tier) and with a better code structure and logging.
- This project is not affiliated with backpack.tf in any way.
- You need a backpack.tf API token to use this project.
- This project is in development, so it may have bugs and issues.

## Description

backpack.tf-ws-service is a script designed to connect to backpack.tf's websocket service and gather listing data.

It also calls the backpack.tf snapshot endpoint frequently to ensure the data is kept up to date.

This listings are stored in a MongoDB database.

## Features

- Real-time listing updates from backpack.tf's websocket service (using the backpack.tf websocket API)
- Frequent snapshot updates from backpack.tf's snapshot endpoint
- Storage of listing data in a MongoDB database (using pymongo)
- Prioritized items (items that get their snapshots retrieved more frequently)

## Requirements

- Python 3.10+
- A MongoDB instance running
- A backpack.tf API token

## Installation

1. **Clone the repository:**

```bash
git clone https://github.com/LucasHenriqueDiniz/backpack.tf-ws-service.git
```

2. **Install the required dependencies:**

```bash
pip install -r requirements.txt
```

3. **Create the json file with the api token and mongo settings (example in config-example.json):**

   ```json
   {
     "mongo_uri": "YOUR_MONGO_URI",
     "database_name": "YOUR_DATABASE_NAME",
     "collection_name": "YOUR_COLLECTION_NAME",
     "bptf_token": "YOUR_BPTF_TOKEN",
     "websocket_url": "wss://ws.backpack.tf/events",
     "print_events": 3,
     "prioritized_items": ["Mann Co. Supply Crate Key"]
   }
   ```

- **mongo_uri:** MongoDB URI to connect to the database
- - <strong>Example:</strong> mongodb+srv://<MANGODB_USER>:<MANGODB_USER_PASSWORD>@backpacktf-database.123.mongodb.net/
- **database_name:** Database name where the data will be stored
- - <strong>Example:</strong> backpacktf
- **collection_name:** Collection name where the data will be stored
- - <strong>Example:</strong> listings
- **bptf_token:** backpack.tf API token
- - You can get it [here](https://backpack.tf/developer/apikey/view)
- **websocket_url:** backpack.tf websocket url
- - <strong>Use:</strong> wss://ws.backpack.tf/events
- **print_events:** logging from the code
- - <strong>Example:</strong> 0 = critical, 1 = all, 2 = errors, 3 = errors and warnings, 4 = debug
- **prioritized_items:** Items that will have their snapshots retrieved more frequently
- - <strong>Example:</strong> ["Mann Co. Supply Crate Key"]

4. **Run the main.py script (ensure you have a mongodb instance running too):**

```bash
python main.py
```

## Issues

If you encounter any issues, please open an issue in the issues tab.

## Contribute

Contributions are always welcome! Please create a pull request with your changes.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
