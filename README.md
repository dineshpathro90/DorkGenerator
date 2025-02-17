<div align="left" style="position: relative;">
<h1>DORKGENERATOR</h1>
<p align="left">
	<em><code>❯ The Google Dorks Generator is a powerful tool designed to automate the process of creating Google dork queries for bug bounty hunting and security research. This tool allows you to replace a placeholder domain in a list of predefined dorks with one or more target domains, supporting various output formats and offering extensive customization options.</code></em>
</p>
<p align="left">
	<img src="https://img.shields.io/github/license/dineshpathro90/DorkGenerator?style=default&logo=opensourceinitiative&logoColor=white&color=0080ff" alt="license">
	<img src="https://img.shields.io/github/last-commit/dineshpathro90/DorkGenerator?style=default&logo=git&logoColor=white&color=0080ff" alt="last-commit">
	<img src="https://img.shields.io/github/languages/top/dineshpathro90/DorkGenerator?style=default&color=0080ff" alt="repo-top-language">
	<img src="https://img.shields.io/github/languages/count/dineshpathro90/DorkGenerator?style=default&color=0080ff" alt="repo-language-count">
</p>
<p align="left"><!-- default option, no dependency badges. -->
</p>
<p align="left">
	<!-- default option, no dependency badges. -->
</p>
</div>
<br clear="right">


---
## 👾 Features
- Multiple Domains: Process multiple target domains concurrently.
- Custom Dorks: Add custom dorks from a file to extend the default list.
- Output Formats: Save the modified dorks in txt, json, or csv formats.
- Exclude Dorks: Exclude specific dorks from being processed.
- Limit: Limit the number of dorks processed per domain.
- Dry Run: Perform a dry run to see what changes would be made without modifying any files.
- Verbose Mode: Enable detailed logging for debugging purposes.
- Configuration File: Use a YAML configuration file to specify all options.
- Concurrency: Efficiently process multiple domains using concurrent execution.

---
## Configuration File
#### You can use a YAML configuration file to specify all options. Here's an example configuration file:
```
domains:
  - example.com
  - test.com
output_dir: ./output
format: json
custom_dorks: custom_dorks.txt
exclude:
  - "site:example.com inurl:admin"
limit: 50
dry_run: true
verbose: true
```

---
## Run the tool with the configuration file:
```
python3 DorkGen.py --config config.yaml
```

---

## 📁 Project Structure

```sh
└── DorkGenerator/
    ├── DorkGen.py
    └── README.md
```


### 📂 Project Index
<details open>
	<summary><b><code>DORKGENERATOR/</code></b></summary>
	<details> <!-- __root__ Submodule -->
		<summary><b>__root__</b></summary>
		<blockquote>
			<table>
			<tr>
				<td><b><a href='https://github.com/dineshpathro90/DorkGenerator/blob/master/DorkGen.py'>DorkGen.py</a></b></td>
			</tr>
			</table>
		</blockquote>
	</details>
</details>

---
## 🚀 Getting Started

### ☑️ Prerequisites

Before getting started with DorkGenerator, ensure your runtime environment meets the following requirements:

- **Programming Language:** Python


### ⚙️ Installation

Install DorkGenerator using one of the following methods:

**Build from source:**

1. Clone the DorkGenerator repository:
```sh
❯ git clone https://github.com/dineshpathro90/DorkGenerator/
```

2. Navigate to the project directory:
```sh
❯ cd DorkGenerator
```


### 🤖 Usage
Run DorkGenerator using the following command:
```sh
python3 DorkGen.py example.com test.com --output-dir ./output --format json --custom-dorks custom_dorks.txt --exclude "site:example.com inurl:admin" --limit 50 --dry-run --verbose
```

---
## 📌 Options

- **`domains`**: One or more target domains to replace in the dorks.
- **`--output-dir`**: Specify the output directory where the files will be saved. Default is the current directory.
- **`--format`**: Choose the output file format (txt, json, csv). Default is txt.
- **`--custom-dorks`**: Path to a file containing custom dorks. Each dork should be on a new line.
- **`--exclude`**: Dorks to exclude from processing.
- **`--limit`**: Limit the number of dorks processed per domain.
- **`--dry-run`**: Perform a dry run to see what changes would be made without modifying any files.
- **`--verbose`**: Enable verbose logging for debugging purposes.
- **`--version`**: Show the version of the script and exit.
- **`--config`**: Path to a YAML configuration file specifying domains, output directory, format, custom dorks file, exclude list, limit, dry run, and verbose mode.

---

## 🔰 Contributing

- **💬 [Join the Discussions](https://github.com/dineshpathro90/DorkGenerator/discussions)**: Share your insights, provide feedback, or ask questions.
- **🐛 [Report Issues](https://github.com/dineshpathro90/DorkGenerator/issues)**: Submit bugs found or log feature requests for the `DorkGenerator` project.
- **💡 [Submit Pull Requests](https://github.com/dineshpathro90/DorkGenerator/blob/main/CONTRIBUTING.md)**: Review open PRs, and submit your own PRs.

<details closed>
<summary>Contributing Guidelines</summary>

1. **Fork the Repository**: Start by forking the project repository to your github account.
2. **Clone Locally**: Clone the forked repository to your local machine using a git client.
   ```sh
   git clone https://github.com/dineshpathro90/DorkGenerator/
   ```
3. **Create a New Branch**: Always work on a new branch, giving it a descriptive name.
   ```sh
   git checkout -b new-feature-x
   ```
4. **Make Your Changes**: Develop and test your changes locally.
5. **Commit Your Changes**: Commit with a clear message describing your updates.
   ```sh
   git commit -m 'Implemented new feature x.'
   ```
6. **Push to github**: Push the changes to your forked repository.
   ```sh
   git push origin new-feature-x
   ```
7. **Submit a Pull Request**: Create a PR against the original project repository. Clearly describe the changes and their motivations.
8. **Review**: Once your PR is reviewed and approved, it will be merged into the main branch. Congratulations on your contribution!
</details>

<details closed>
<summary>Contributor Graph</summary>
<br>
<p align="left">
   <a href="https://github.com{/dineshpathro90/DorkGenerator/}graphs/contributors">
      <img src="https://contrib.rocks/image?repo=dineshpathro90/DorkGenerator">
   </a>
</p>
</details>

---
