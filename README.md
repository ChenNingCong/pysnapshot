# pysnapshot : Post-Mortem Python Debugger

A post-mortem debugging tool that combines the power of `debugpy` and `debuglater` to help you investigate Python program crashes after they occur. Debugpy is the default backend used by vscode so you get free UI support.

## Features

- Post-mortem debugging capabilities using debugpy
- Crash state preservation with debuglater
- Interactive debugging session with full stack trace and variable inspection
- Compatible with VS Code and PyCharm debugging interfaces

## Installation

```bash
pip install git+https://github.com/ChenNingCong/pysnapshot
```

## Quick Start

1. Import the library and install the hook as early as possible

```python
import pysnapshot
pysnapshot.install_exception_snapshot_hook("exception")
```

2. When your program crashes, the debugger will save the stack trace to the file `exception.dump`.

3. You can also use the snapshot hook to save the stack trace explicitly. This won't stop the program.
```python
pysnapshot.snapshot("checkpoint")
```

4.  Launch the debugger server with `python -m pysnapshot --filename exception.dump --endpoint 5678`.

5. In vscode, launch the debugger with the "attach" configuration.

## Requirements

- Python 3.7+

## Contributing

Contributions are welcome! Please read our contributing guidelines before submitting pull requests.

## License

This project is licensed under the MIT License - see the LICENSE file for details.