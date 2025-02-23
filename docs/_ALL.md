# Repo-level Completion Tool

Welcome to the documentation for the Repo-level Completion Tool. This tool is designed to assist in generating code or text based on the context provided by a repository and specific files within it. It leverages the Hugging Face Inference API to generate content using a specified model.

## Table of Contents

1. [Features](#features)
2. [Installation](#installation)
3. [Usage](#usage)
4. [Example](#example)
5. [License](#license)
6. [Contributing](#contributing)
7. [Contact](#contact)

## Features

- **Contextual Completion**: Provide a repository name and a list of files to give the model context.
- **Customizable Prompt**: You can specify a custom prompt to guide the model's output.
- **Streamed Response**: The tool streams the response from the model, allowing you to see the output as it's generated.

## Installation

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/deniskropp/repo-hf-cli.git
   cd repo-hf-cli
   ```

2. **Install the Tool**:
   
   ```bash
   pip install -e .
   ```

## Usage

1. **Set Up Your Hugging Face Token**:
   Make sure you have a Hugging Face API token. You can set it as an environment variable:
   ```bash
   export HF_TOKEN='your_huggingface_token'
   ```

2. **Run the Tool**:
   ```bash
   repo-hf-cli --model Qwen/Qwen2.5-Coder-32B-Instruct --repo awesome-ai --prompt "Complete the function to calculate the sum of two numbers" file1.py file2.py target_file.py
   ```

   - `--model`: The model to use for generation. Default is `Qwen/Qwen2.5-Coder-32B-Instruct`.
   - `--repo`: The name of the repository. Default is `awesome-ai`.
   - `--prompt`: A custom prompt to guide the model.
   - `files`: A list of files. The last file is the target file where the generated content will be appended.

## Example

```bash
repo-hf-cli --model Qwen/Qwen2.5-Coder-32B-Instruct --repo my-repo --prompt "Implement a function to sort an array" utils.py main.py target_file.py
```

This command will use the specified model to generate content based on the context provided by `utils.py` and `main.py`, and the generated content will be appended to `target_file.py`.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contributing

Contributions are welcome! Please feel free to open issues or submit pull requests.

## Contact

For any questions or feedback, you can reach out to the author at [dok@directfb1.org](mailto:dok@directfb1.org).

---

Enjoy using the Repo-level Completion Tool! 🚀


# Repo-level Completion Tool

## API Reference

### Command Line Interface

#### `repo-hf-cli`

##### Arguments

- `--model`: The model to use for generation. Default is `Qwen/Qwen2.5-Coder-32B-Instruct`.
- `--repo`: The name of the repository. Default is `awesome-ai`.
- `--prompt`: A custom prompt to guide the model.
- `files`: A list of files. The last file is the target file where the generated content will be appended.

##### Example

```bash
repo-hf-cli --model Qwen/Qwen2.5-Coder-32B-Instruct --repo my-repo --prompt "Implement a function to sort an array" utils.py main.py target_file.py
```

### Python API

#### `repo_hf_cli.repo_hf_cli.run`

##### Parameters

- `args`: An object containing the command line arguments.

##### Example

```python
from repo_hf_cli.repo_hf_cli import run
import argparse

parser = argparse.ArgumentParser(description='Your script description')
parser.add_argument('--model', type=str, default='Qwen/Qwen2.5-Coder-32B-Instruct', help='Model name')
parser.add_argument('--repo', type=str, default='awesome-ai', help='Repository name')
parser.add_argument('--prompt', type=str, help='Prompt for the model')
parser.add_argument('files', nargs='+', help='List of files')
args = parser.parse_args()

run(args)
```

---

This documentation provides a comprehensive overview of the Repo-level Completion Tool, including installation, usage, and API references. If you have any questions or need further assistance, feel free to reach out! 🚀

# Repo-level Completion Tool

## Troubleshooting

### Common Issues

1. **Model Not Found**:
   - Ensure that the model name specified in the `--model` argument is correct and available on Hugging Face.
   - Example: `Qwen/Qwen2.5-Coder-32B-Instruct`

2. **File Not Found**:
   - Ensure that the file paths provided in the `files` argument are correct and accessible.
   - Example: `file1.py file2.py target_file.py`

3. **Hugging Face Token Not Set**:
   - Ensure that the Hugging Face API token is set as an environment variable.
   - Example: `export HF_TOKEN='your_huggingface_token'`

4. **Permission Denied**:
   - Ensure that you have the necessary permissions to read the files and write to the target file.
   - Example: `chmod +r file1.py` and `chmod +w target_file.py`

### Solutions

1. **Check Model Availability**:
   - Visit the [Hugging Face Model Hub](https://huggingface.co/models) to verify the model name and availability.

2. **Verify File Paths**:
   - Use absolute paths or ensure that the relative paths are correct.

3. **Set Environment Variable**:
   - Use the `export` command to set the `HF_TOKEN` environment variable in your terminal session.

4. **Adjust File Permissions**:
   - Use the `chmod` command to adjust file permissions as needed.

---

If you encounter any issues that are not covered in this section, please feel free to open an issue on the [GitHub repository](https://github.com/deniskropp/repo-hf-cli/issues).

# Repo-level Completion Tool

## Changelog

### Version 0.1.0 (Initial Release)

- **Features**:
  - Added support for contextual completion using repository and file context.
  - Added customizable prompt support.
  - Added streamed response support for real-time output.
- **Bug Fixes**:
  - Fixed file reading and writing issues.
  - Improved error handling for missing files and incorrect model names.
- **Improvements**:
  - Enhanced documentation with usage examples and API references.
  - Added troubleshooting section for common issues.

---

Thank you for using the Repo-level Completion Tool! If you have any feedback or suggestions, please don't hesitate to share them. 🚀

# Repo-level Completion Tool

## Acknowledgments

- **Hugging Face**: For providing the powerful Inference API and a wide range of models.
- **Contributors**: For their valuable contributions and feedback.

---

Enjoy using the Repo-level Completion Tool! 🚀

# Repo-level Completion Tool

## Support

If you need support or have any questions, you can reach out to the author at [dok@directfb1.org](mailto:dok@directfb1.org) or open an issue on the [GitHub repository](https://github.com/deniskropp/repo-hf-cli/issues).

---

Happy coding! 🚀
