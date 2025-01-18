from pathlib import Path
import argparse


class Filter:
    def __init__(self):
        pass

    def add_condition(self):
        pass

    def is_match(self, path):
        pass


class FilterStack:
    def __init__(self):
        self.stack = []

    def add_filter(self, filter):
        self.stack.append(filter)

    def pop_filter(self):
        self.stack.pop()

    def is_match(self, path):
        for filter in self.stack:
            if filter.is_match(path):
                return True
        return False


class Content:
    def __init__(self, name, children, is_readable):
        self.name = name
        self.children = children
        self.is_readable = is_readable

    def is_file(self):
        return self.children is None

    def is_directory(self):
        return not self.is_file()


#################### Argument Parsing ####################


class Properties:
    VERBOSE, DEFAULT, SILENCE = 4, 3, 2
    GIT, GITIGNORE, PREPAREIGNORE, HIDDEN = 9, 8, 7, 6

    def __init__(self, depth, ignores, log_mode):
        self.depth = depth  # traversing options
        self.ignores = ignores  # ignore options
        self.log_mode = log_mode  # log options

    def __repr__(self):
        return f"Properties[depth={self.depth}, ignores={self.ignores}, log_mode={self.log_mode}]"


def parse_arguments():
    parser = argparse.ArgumentParser(
        description="Prepare a copy-paste ready LLM prompt."
    )

    # Positional argument for source directories/files
    parser.add_argument(
        "sources",
        nargs="+",
        help="Relative or absolute paths of input directories/files. Multiple sources are supported.",
    )

    # Traversing options
    parser.add_argument(
        "-d",
        "--depth",
        type=int,
        default=6,
        help="Set maximum recursion depth. (default=6)",
    )

    # Ignore options
    parser.add_argument(
        "-G", action="store_true", help="Include `.git` contents (not recommended)."
    )
    parser.add_argument(
        "-g", action="store_true", help="Include `.gitignore` listed contents."
    )
    parser.add_argument(
        "-p", action="store_true", help="Include `.prepareignore` listed contents."
    )
    parser.add_argument(
        "-a", action="store_true", help="Include hidden files (excluding `.git`)."
    )

    # Log options
    parser.add_argument(
        "-v", action="store_true", help="Enable verbose logging to stderr."
    )
    parser.add_argument(
        "-s", action="store_true", help="Disable logging to stderr (overrides `-v`)."
    )

    args = parser.parse_args()

    # Determine log mode
    log_mode = Properties.DEFAULT
    if args.v:
        log_mode = Properties.VERBOSE
    if args.s:
        log_mode = Properties.SILENCE

    # Collect ignore options
    ignores = []
    if args.G:
        ignores.append(Properties.GIT)
    if args.g:
        ignores.append(Properties.GITIGNORE)
    if args.p:
        ignores.append(Properties.PREPAREIGNORE)
    if args.a:
        ignores.append(Properties.HIDDEN)

    return args.sources, Properties(
        depth=args.depth, ignores=ignores, log_mode=log_mode
    )

#################### Scanning ####################


def scan_from(root, properties):
    pass


#################### Printing ####################


def content_to_prompt(content):
    pass


#################### Main ####################


def main():
    sources, property = parse_arguments()
    print(sources)
    print(repr(property))


if __name__ == "__main__":
    main()
