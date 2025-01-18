# prepare
Prepare a copy-and-paste-ready LLM prompt for directories.

## Installation
To install, run the following.

```bash
sudo ./install-prepare
```

To uninstall, run the following.
```bash
sudo ./uninstall-prepare
```

If you want to explicitly set or change what python executable that this program would use, for example `python3.11`, run the following.

```bash
sudo ./install-prepare python3.11
```

### Dependencies
You need `python3.*`, `python3` or `python` to run this program.

*Note: Python 2 is not Python.*

## How to use
For example, if your project seems like this:

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

Open the root path of your project in a terminal, and run the following.

```bash
$ prepare src/service > prompt-service.md
Total 1 directories, 1 loaded, 0 skipped
Total 3 files, 3 loaded, 0 skipped
```

When you open the `prompt-service.md`, the contents of the file is as the following. This is called as **Prompt Markdown**.

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

Starting from this prompt markdown, you can freely make the question and copy-and-paste it to your favorite LLM, like [ChatGPT](https://chatgpt.com/), [Claude](https://claude.ai/) or [Perplexity](https://www.perplexity.ai/).

### Auto Skipping
This program automatically skips some contents(file and directory) if they are one of:

* Contents of `.git` directory and itself
* Found match pattern in `.gitignore`
* Found match pattern in `.prepareignore`
* Hidden

For example, since `src/secret/*` is listed on `.gitignore`, the following command's markdown result does not contain any sensitive contents. Note that non-root `.gitignore` and `.prepareignore` files are also recognized.

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
kil
* `SOURCE ...`: relative or absolute path of ingredients. Multiple sources are supported.
* options:
  * `-h`: help message
  * `-G`: include `.git` contents (not recommended)
  * `-g`: include `.gitignore` listed contents
  * `-p`: include `.prepareignore` listed contents
  * `-a`: include hidden files (does not include git-related ones)
  * `-v`: verbose stderr log message