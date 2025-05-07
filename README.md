# prepare
Prepare an LLM prompt for copy-paste use.

## Installation

To install, run the following command:
```bash
sudo ./install-prepare
```

To remove, run:
```bash
sudo ./remove-prepare
```

The install and removal scripts require root privileges to copy or delete Python scripts in `/usr/bin`. If you do not want to grant root privilege, you may install the script elsewhere manually.

### Dependencies

- `python3` (or `python`)
- `git`

All dependencies must be discoverable in your `$PATH`. When you use the install script, it will automatically verify these dependencies before proceeding; if any are missing, installation will be canceled.

*Note: Python 2 is not supported.*

## Usage

**To use `prepare`, simply select the directory(s) you want to provide to the LLM and enter its path as arguments. The `prepare` program outputs Markdown to standard output and execution statistics to stderr.** Here is an example (list of optional arguments are listed at the end of the document):

```bash
$ prepare src/service > prompt.md
SKIPPED: .gitignore listed
- /app/rock-paper-scissor/src/service/__pycache__

Directories: total 2, read 1, skipped 1
Files: total 3, read 3, skipped 0
Markdown: 35 lines, 812 characters (with spaces), 719 characters (without spaces)
```

Suppose your directory structure is as follows:

```bash
rock-paper-scissor/
├── README.md
├── .git/
│   └── ...
└── src/
    ├── game.py
    ├── model/
    │   ├── __init__.py
    │   └── hand.py
    ├── secret/
    │   └── api-key.env
    └── service/
        ├── __pycache__
        │   └── ...
        ├── __init__.py
        ├── ai_agent.py
        └── random_hand.py
```

If you open the generated `prompt.md` file, you will see something like this:

`````
# Project Structure and File Contents

## Structure: `/app/rock-paper-scissor/src/service`
````
└── service
    ├── __init__.py
    ├── __pycache__ (.gitignore listed)
    ├── ai_agent.py
    └── random_hand.py
````

### File Content: `/app/rock-paper-scissor/src/service/__init__.py`
````py
from .ai_agent import *
from .random_hand import *
````

### File Content: `/app/rock-paper-scissor/src/service/ai_agent.py`
````py
from model import Hand

def get_ai_hand():
    return Hand(0)  # smart ai believes that a rock is always the best play
````

### File Content: `/app/rock-paper-scissor/src/service/random_hand.py`
````py
import random
from model import Hand

def get_random_hand():
    random_hand_type = random.randint(0, 3)    # bug! random.randint(0, 2) is correct
    return Hand(random_hand_type)
````
`````

You can copy and paste this Markdown file into your preferred LLM tool-such as [ChatGPT](https://chatgpt.com/), [Claude](https://claude.ai/), or [Perplexity](https://www.perplexity.ai/)-to conveniently provide project context.

### Auto-Skip Feature

This program automatically skips files and directories that meet the following criteria:

* Hidden files and directories (any file or directory starting with a `.`)
  * Exception: the `.gitignore` file itself is not skipped.
* Any files or directories specified in `.gitignore`

*Note: Like Git, if a directory is skipped, `prepare` does not read any of its contents. Thus, the contents of skipped directories will NOT be counted in the statistics.*

## Command-Line Arguments

```bash
prepare SOURCE ... [options]
```

* `SOURCE ...`
    * Relative or absolute paths to input directories/files.
    * Multiple sources are supported.
* Options:
    * Skipping
      * `-a`: Read and include all files in the result, without skipping any
    * Output
      * `-h`: Display help message instead of running the program
      * `-s`: Show only statistics, without displaying which files and directories were skipped