import os

import sniffer.api
import termstyle

pass_fg_color = termstyle.green
pass_bg_color = termstyle.bg_default
fail_fg_color = termstyle.red
fail_bg_color = termstyle.bg_default

watch_paths = ["src/", "tests/"]


@sniffer.api.file_validator
def py_files(filename):
    """Only files ending with .py extension and not prefixed with a period"""
    return filename.endswith(".py") and not os.path.basename(
        filename
    ).startswith(".")


@sniffer.api.runnable
def execute_nose(*args):
    import nose

    return nose.run(argv=list(args))
