:: for py v3.11.1. for some reason new modules don't work as right with it
:: py -m nuitka ../src --standalone --output-dir=../dist --python-flag=-O

:: for older Python versions cuz they have the support for it
nuitka ../src --standalone --output-dir=../dist --python-flag=-O