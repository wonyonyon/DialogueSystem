### Coffee-ordering system

-------------------------------------------------------------------------
This repository is a coffee-ordering system, its includes dialogue management, language generation and language understanding components.

Run the bot
--------------
```
    cd server
    python bot.py
```

Folder structure
--------------
```
├── data_helper        - this file contains the data loader and process.
│
│
├── module               - this folder contains any model of your project.
│   └── DM               - dialogue manager
│   └── NLG              - nature language geneator
│   └── NLU              - nature language understanding
│   └── Service          - this folder contains calculate how much the coffee
│
│
├── knowledge             - this folder contains knowledge.
│   └── reader.py
│   
├── app                  - this folder contains the website of this project/system.
|
│ 
└── server                - this folder contains the background of this project/system.
|
│ 
└── config                - this folder contains the config of this project/system.

```

- Add machine learning model in NLU module
- Add deep learning model in NLU module
- Add yaml configurtion file