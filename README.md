# pysnapshot : Post-Mortem Python Debugger

A post-mortem debugging tool that combines the power of `debugpy` and `debuglater` to help you investigate Python program crashes after they occur. Debugpy is the default backend used by vscode so you get free UI support.

## Features

- Post-mortem debugging capabilities using debugpy
- Crash state preservation with debuglater
- Interactive debugging session with full stack trace and variable inspection
- Compatible with VS Code and PyCharm debugging interfaces

## Installation

```bash
pip install pysnapshot
```

## Quick Start

1. Import and initialize the debugger in your code:

```python
from post_mortem_debugger import PMDebugger

debugger = PMDebugger()
debugger.enable()
```

2. When your program crashes, the debugger will automatically preserve the state and provide connection instructions.

3. Connect to the debug session using your IDE or the command line interface:

```bash
python -m post_mortem_debugger connect
```

## Requirements

- Python 3.7+
- debugpy
- debuglater

## Configuration

Set environment variables to customize behavior:

- `PMD_PORT`: Debug server port (default: 5678)
- `PMD_HOST`: Debug server host (default: localhost)
- `PMD_WAIT`: Wait for debugger connection on crash (default: True)

## Contributing

Contributions are welcome! Please read our contributing guidelines before submitting pull requests.

## License

This project is licensed under the MIT License - see the LICENSE file for details.