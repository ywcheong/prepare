# prepare
Prepare a copy-and-paste-ready LLM prompt for directories.

## Installation
To install, run the following:
```bash
sudo ./install-prepare
```

To uninstall, run the following:
```bash
sudo ./uninstall-prepare
```

If you want to explicitly set or change the Python executable that this program uses (ex: `python3.11`), run:
```bash
sudo ./install-prepare python3.11
```

### Dependencies
You need `python3.*`, `python3` or `python` to run this program.

*Note: Python 2 is not supported.*

## How to use
For example, if your project structure looks like this:

```
rock-paper-scissor/
├── README.md
├── .git/
│   └── (truncated)
└── src/
    ├── game.py
    ├── model/
    │   ├── __init__.py
    │   └── hand.py
    ├── secret/
    │   └── api-key.env
    └── service/
        ├── __init__.py
        ├── ai_agent.py
        └── random_hand.py
```

Open the root path of your project in a terminal and run:

```bash
$ prepare src/service > prompt-service.md
Total 1 directories, 1 loaded, 0 skipped
Total 3 files, 3 loaded, 0 skipped
```

When you open the `prompt-service.md`, it will contain the following **Prompt Markdown**:

```
    The following text describes structure and contents of this project.
    Please read the text and answer the question at the end.

    # Structure of the Project
    src/service/
    ├── __init__.py
    ├── ai_agent.py
    └── random_hand.py

    # Contents of Each File
    ## src/service/__init__.py
    ```py
    from .ai_agent import *
    from .random_hand import *
    ```

    ## src/service/ai_agent.py
    ```py
    from model import Hand

    def get_ai_hand():
        return Hand(0)
    ```

    ## src/service/__init__.py
    ```py
    import random
    from model import Hand

    def get_random_hand():
        random_hand_type = random.randint(0, 3)
        return Hand(random_hand_type)
    ```

    # Question
```

You can now create a question based on this prompt markdown and copy-paste it into your favorite LLM tool like [ChatGPT](https://chatgpt.com/), [Claude](https://claude.ai/) or [Perplexity](https://www.perplexity.ai/).

### Auto Skipping
This program automatically skips certain contents (files and directories) if they match any of these criteria:

* Located in `.git` directory or its subdirectories.
* Listed in `.gitignore`.
* Listed in `.prepareignore`.
* Hidden files or directories.

For example, since `src/secret/*` is listed in `.gitignore`, running the following command ensures sensitive contents are excluded from the markdown output:

```
$ prepare . > propmt-src.md
SKIPPED: .git folder
- .git (76 directories, 48 files)
SKIPPED: .gitignore listed contents
- src/secret/* (0 directories, 1 files)
Total 53 directories, 4 loaded, 49 skipped
Total 83 files, 7 loaded, 76 skipped
```

## Arguments

```bash
prepare SOURCE ... [options]
```

* `SOURCE ...`
    * Relative or absolute paths of input directories/files.
    * Multiple sources are supported.
* Options:
    * `-h`: Display help message.
    * `-G`: Include `.git` contents (not recommended).
    * `-g`: Include `.gitignore` listed contents.
    * `-p`: Include `.prepareignore` listed contents.
    * `-a`: Include hidden files (excluding `.git`).
    * `-v`: Enable verbose logging to stderr.
    * `-s`: Disable stderr message (ignoring `-v`).