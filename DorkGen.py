import re
import logging
import argparse
from pathlib import Path
import json
import csv
from concurrent.futures import ThreadPoolExecutor
from tqdm import tqdm
import yaml

# Script version
VERSION = "1.0.0"

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def load_dorks():
    return [
        "site:example.com inurl:admin",
        "site:example.com intitle:index of",
        "site:example.com filetype:pdf",
        "site:example.com inurl:login",
        "site:example.com inurl:register",
        "site:example.com intitle:login",
        "site:example.com inurl:admin/config",
        "site:example.com inurl:dashboard",
        "site:example.com inurl:wp-content",
        "site:example.com intitle:index.of .git",
        "site:example.com filetype:xml",
        "site:example.com intitle:admin",
        "site:example.com inurl:wp-admin",
        "site:example.com inurl:phpmyadmin",
        "site:example.com intitle:configuration",
        "site:example.com inurl:upload",
        "site:example.com intitle:password",
        "site:example.com inurl:api",
        "site:example.com inurl:login.php",
        "site:example.com inurl:reset-password",
        "site:example.com inurl:forgot-password",
        "site:example.com inurl:change-password",
        "site:example.com inurl:user",
        "site:example.com inurl:admin-panel",
        "site:example.com inurl:panel",
        "site:example.com inurl:secure",
        "site:example.com inurl:config.php",
        "site:example.com inurl:index.php",
        "site:example.com inurl:setup",
        "site:example.com intitle:admin login",
        "site:example.com inurl:manager",
        "site:example.com inurl:/admin/",
        "site:example.com inurl:wp-login",
        "site:example.com intitle:index of /uploads",
        "site:example.com filetype:sql",
        "site:example.com inurl:backup",
        "site:example.com intitle:\"index of\" .env",
        "site:example.com inurl:/.git",
        "site:example.com inurl:/uploads/",
        "site:example.com inurl:/wp-content/uploads",
        "site:example.com intitle:index of /wp-includes",
        "site:example.com filetype:log",
        "site:example.com inurl:git-config",
        "site:example.com intitle:debug",
        "site:example.com inurl:debug",
        "site:example.com inurl:phpinfo.php",
        "site:example.com inurl:debug.log",
        "site:example.com inurl:configuration.php",
        "site:example.com intitle:index of /admin",
        "site:example.com inurl:/wp-includes/js/",
        "site:example.com inurl:robots.txt",
        "site:example.com intitle:index of /config",
        "site:example.com inurl:.git",
        "site:example.com inurl:/config/",
        "site:example.com filetype:db",
        "site:example.com intitle:index of /admin/",
        "site:example.com inurl:login.aspx",
        "site:example.com inurl:admin.asmx",
        "site:example.com inurl:admin-config",
        "site:example.com inurl:admin/dash",
        "site:example.com inurl:admin_control",
        "site:example.com inurl:manage",
        "site:example.com inurl:upload.php",
        "site:example.com intitle:index of /logs",
        "site:example.com filetype:conf",
        "site:example.com inurl:index.html",
        "site:example.com inurl:.bash_history",
        "site:example.com inurl:.env",
        "site:example.com inurl:.gitignore",
        "site:example.com filetype:json",
        "site:example.com inurl:remote-config",
        "site:example.com inurl:.gitmodules",
        "site:example.com filetype:log",
        "site:example.com inurl:admin-dashboard",
        "site:example.com inurl:wp-admin/admin.php",
        "site:example.com inurl:.htaccess",
        "site:example.com inurl:debug-backtrace",
        "site:example.com intitle:\"index of\" /uploads",
        "site:example.com inurl:admin-area",
        "site:example.com filetype:json",
        "site:example.com inurl:admin.php",
        "site:example.com inurl:rest-api",
        "site:example.com filetype:json",
        "site:example.com inurl:login.php",
        "site:example.com filetype:bak",
        "site:example.com intitle:index of .git",
        "site:example.com intitle:index of config",
        "site:example.com inurl:index.js",
        "site:example.com inurl:checkout",
        "site:example.com filetype:env",
        "site:example.com inurl:.bash_history",
        "site:example.com filetype:backup",
        "site:example.com inurl:openapi",
        "site:example.com filetype:bak",
        "site:example.com inurl:/admin_files/",
        "site:example.com inurl:upload",
        "site:example.com filetype:yaml",
        "site:example.com inurl:session_id",
        "site:example.com inurl:redis",
        "site:example.com inurl:phpinfo",
        "site:example.com filetype:dump",
        "site:example.com inurl:admin-console",
        "site:example.com intitle:index of /config.php",
        "site:example.com inurl:admin/configure",
        "site:example.com inurl:settings.php",
        "site:example.com inurl:loginform",
        "site:example.com inurl:reset-form",
        "site:example.com inurl:loginpanel",
        "site:example.com intitle:dashboard",
        "site:example.com inurl:authentication",
        "site:example.com inurl:logs/",
        "site:example.com inurl:public/",
        "site:example.com inurl:mail.php",
        "site:example.com inurl:/assets/js/",
        "site:example.com filetype:inc",
        "site:example.com inurl:.zip",
        "site:example.com inurl:/wp-content/plugins/",
        "site:example.com inurl:login.html",
        "site:example.com inurl:admin/resources",
        "site:example.com inurl:access-log",
        "site:example.com inurl:session_id",
        "site:example.com inurl:backup.zip",
        "site:example.com inurl:session-log",
        "site:example.com intitle:index of /private/",
        "site:example.com filetype:js",
        "site:example.com inurl:authentication-token",
        "site:example.com inurl:dashboard-settings",
        "site:example.com inurl:admin/settings",
        "site:example.com inurl:.git",
        "site:example.com intitle:\"index of\" /admin",
        "site:example.com filetype:env",
        "site:example.com inurl:.gitattributes",
        "site:example.com inurl:.bashrc",
        "site:example.com inurl:/admin/",
        "site:example.com inurl:admin-logs",
        "site:example.com intitle:debugging",
        "site:example.com inurl:index.yaml",
        "site:example.com intitle:site-map",
        "site:example.com inurl:password-file",
        "site:example.com intitle:index of /private",
        "site:example.com inurl:admin/config",
        "site:example.com inurl:admin/login",
        "site:example.com inurl:admin/panel",
        "site:example.com inurl:admin/dashboard",
        "site:example.com inurl:admin/settings",
        "site:example.com inurl:admin/upload",
        "site:example.com inurl:admin/backup",
        "site:example.com inurl:admin/debug",
        "site:example.com inurl:admin/phpinfo",
        "site:example.com inurl:admin/logs",
        "site:example.com inurl:admin/config.php",
        "site:example.com inurl:admin/index.php",
        "site:example.com inurl:admin/setup",
        "site:example.com inurl:admin/manager",
    ]

def is_valid_domain(domain):
    pattern = re.compile(r'^(?:[a-zA-Z0-9-]+\.)+[a-zA-Z]{2,}$')
    return re.match(pattern, domain) is not None

def replace_domain(dorks, old_domain, new_domain):
    return [dork.replace(old_domain, new_domain) for dork in dorks]

def save_dorks_to_file(dorks, file_path, format_type, dry_run):
    try:
        if dry_run:
            logging.info(f"Dry run: Would save modified Google dorks to {file_path}")
            return

        if format_type == "json":
            with file_path.open("w") as f:
                json.dump(dorks, f, indent=4)
        elif format_type == "csv":
            with file_path.open("w", newline='') as f:
                writer = csv.writer(f)
                writer.writerow(["Dork"])
                writer.writerows([[dork] for dork in dorks])
        else:
            with file_path.open("w") as f:
                for dork in dorks:
                    f.write(dork + "\n")
        logging.info(f"Modified Google dorks saved to {file_path}")
    except IOError as e:
        logging.error(f"An error occurred while writing to the file: {e}")

def load_custom_dorks(file_path):
    try:
        with file_path.open("r") as f:
            return [line.strip() for line in f.readlines()]
    except IOError as e:
        logging.error(f"An error occurred while reading the custom dorks file: {e}")
        return []

def process_domain(domain, output_file, format_type, custom_dorks_file=None, exclude_dorks=None, limit=None, dry_run=False):
    google_dorks = load_dorks()

    if custom_dorks_file:
        custom_dorks = load_custom_dorks(custom_dorks_file)
        google_dorks.extend(custom_dorks)

    if exclude_dorks:
        google_dorks = [dork for dork in google_dorks if dork not in exclude_dorks]

    if limit:
        google_dorks = google_dorks[:limit]

    if not is_valid_domain(domain):
        logging.error("Invalid domain format. Please enter a valid domain.")
        return

    modified_dorks = replace_domain(google_dorks, "example.com", domain)
    save_dorks_to_file(modified_dorks, output_file, format_type, dry_run)

def main(domains, output_dir, format_type, custom_dorks_file=None, exclude_dorks=None, limit=None, dry_run=False, verbose=False):
    if verbose:
        logging.getLogger().setLevel(logging.DEBUG)

    with ThreadPoolExecutor() as executor:
        futures = []
        for domain in domains:
            output_path = output_dir / f"modified_dorks_{domain}.{format_type}"
            futures.append(executor.submit(process_domain, domain, output_path, format_type, custom_dorks_file, exclude_dorks, limit, dry_run))

        for future in tqdm(futures, desc="Processing domains"):
            future.result()

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Modify Google dorks for target domains. This script allows you to replace a placeholder domain "
                    "in a list of Google dorks with one or more target domains. It supports custom dorks, multiple "
                    "output formats, concurrent processing of domains, and more."
    )
    parser.add_argument(
        "domains",
        nargs='+',
        help="One or more target domains to replace in the dorks. Example: targetdomain.com anotherdomain.com"
    )
    parser.add_argument(
        "--output-dir",
        type=str,
        default=".",
        help="Output directory where the files will be saved. Default is the current directory."
    )
    parser.add_argument(
        "--format",
        type=str,
        choices=["txt", "json", "csv"],
        default="txt",
        help="Output file format. Choices are 'txt', 'json', or 'csv'. Default is 'txt'."
    )
    parser.add_argument(
        "--custom-dorks",
        type=str,
        help="Path to a file containing custom dorks. Each dork should be on a new line."
    )
    parser.add_argument(
        "--exclude",
        type=str,
        nargs='*',
        help="Dorks to exclude from processing. Example: 'site:example.com inurl:admin' 'site:example.com filetype:pdf'"
    )
    parser.add_argument(
        "--limit",
        type=int,
        help="Limit the number of dorks processed per domain."
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Perform a dry run, showing what changes would be made without modifying any files."
    )
    parser.add_argument(
        "--verbose",
        action="store_true",
        help="Enable verbose logging for debugging purposes."
    )
    parser.add_argument(
        "--version",
        action="version",
        version=f"{VERSION}",
        help="Show the version of the script and exit."
    )
    parser.add_argument(
        "--config",
        type=str,
        help="Path to a configuration file in YAML format. The file can specify domains, output directory, format, custom dorks file, exclude list, limit, dry run, and verbose mode."
    )

    args = parser.parse_args()

    if args.config:
        with open(args.config, 'r') as config_file:
            config = yaml.safe_load(config_file)
            domains = config.get("domains", args.domains)
            output_dir = Path(config.get("output_dir", args.output_dir))
            format_type = config.get("format", args.format)
            custom_dorks_file = Path(config.get("custom_dorks", args.custom_dorks)) if args.custom_dorks else None
            exclude_dorks = config.get("exclude", args.exclude)
            limit = config.get("limit", args.limit)
            dry_run = config.get("dry_run", args.dry_run)
            verbose = config.get("verbose", args.verbose)
    else:
        domains = args.domains
        output_dir = Path(args.output_dir)
        format_type = args.format
        custom_dorks_file = Path(args.custom_dorks) if args.custom_dorks else None
        exclude_dorks = args.exclude
        limit = args.limit
        dry_run = args.dry_run
        verbose = args.verbose

    main(domains, output_dir, format_type, custom_dorks_file, exclude_dorks, limit, dry_run, verbose)
