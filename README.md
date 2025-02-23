# Repo-level Completion Tool

This tool is designed to assist in generating code or text based on the context provided by a repository and specific files within it. It leverages the Hugging Face Inference API to generate content using a specified model.

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

2. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Install the Tool**:
   ```bash
   pip install .
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
