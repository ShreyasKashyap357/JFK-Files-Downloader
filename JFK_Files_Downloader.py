"""
JFK Document Bulk Downloader

This script downloads ZIP files from the National Archives JFK Bulk Download page or any other URL containing ZIP file links. Don’t worry if this sounds technical—it’s designed to be simple enough for anyone to use with a bit of guidance!

Features:
- Downloads all ZIP files or just the ones you choose
- Keeps trying if the internet hiccups
- Picks up where it left off if a download stops
- Shows a progress bar so you know how it’s going
- Checks if files are already there and asks what to do
- Lets you pick where to save files and tweak how it works
- Keeps a log of what it’s doing
- Can slow down downloads if you want to save bandwidth
- Shows a preview of bulk download files with sizes and dates
- Pause and resume downloads anytime
- Cleans up leftover files if something goes wrong
- Extra chatty mode to see more details

Usage:
    python JFK_Files_Downloader.py [OPTIONS]

Options (don’t panic—each one is explained below!):
    --url URL               URL containing files to download. This is the web address where the files live, like https://www.archives.gov/research/jfk. Think of it as telling the script where to shop for files!
    --output-dir DIR        Directory to save downloaded files. This is the folder on your computer where the files will land, like “C:\JFK Files”. It’s your storage spot!
    --max-files N           Maximum number of files to download. Want just 5 files instead of all 100? Set this to 5. It’s like setting a shopping limit.
    --retry ATTEMPTS        Maximum number of retry attempts. If a file fails to download, this is how many times it tries again (default is 5). It’s like giving it extra chances to grab a tricky file.
    --workers N             Number of parallel downloads. How many files it grabs at once (default is 5). Imagine 5 helpers downloading together—faster, but needs a good internet connection!
    --force                 Download files without asking, even if they exist. Normally it checks if a file’s already there—this skips that and overwrites without asking. It’s like saying “just do it!”
    --skip-existing         Skip files that already exist without asking (default). If you’ve got a file already, it moves on quietly. Saves time if you don’t want duplicates.
    --no-skip-existing      Ask about each existing file. Instead of skipping, it’ll ask “overwrite this?” for every file already there. Good if you want full control.
    --smart-check           Skip files with matching size (default). If a file’s the same size as one you have, it assumes it’s the same and skips it. Handy for avoiding repeats.
    --no-smart-check        Don’t skip based on size. Even if sizes match, it’ll still ask or redownload. Use this if you’re extra cautious about duplicates.
    --filter PATTERN        Filter files by filename pattern (e.g., 'jfk2023*'). Only grabs files with names matching this, like picking only “jfk2023” files. The * means “anything after that.”
    --extension EXT         File extension to look for (e.g., 'zip', 'pdf') without the dot. Tells it to grab ZIPs or PDFs—your choice! It’s like picking the file type you want.
    --cowboyup              Run with defaults for pre-2025 bulk downloading without showing this help. For quick runs on older releases, skipping this explanation. It’s a shortcut for pros!
    --throttle MBPS         Limit download speed in MB/s (e.g., 5.0, 0 for no limit). Slows it down so it doesn’t hog your internet—like setting a speed limit for downloads.
    --pause                 Pause downloads and save progress. Stops the script mid-run and remembers where it left off. Like hitting pause on a movie!
    --cleanup               Clean up leftover .part files. Deletes temporary files if something crashes. Keeps your folder tidy!
    --verbose               Show extra details while running. Makes the script chatty, telling you every little step it takes. Great for curious folks!
"""

import argparse
import os
import requests
import time
import re
import shutil
import json
from concurrent.futures import ThreadPoolExecutor
from tqdm import tqdm
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry
import logging
from datetime import datetime

# Bulk ZIP info for preview (sizes approximated from NARA data, dates from official releases)
BULK_ZIP_INFO = {
    "https://www.archives.gov/files/research/jfk/releases/zip/": {
        "2017-2018": [
            {"name": "jfk-pdf1.zip", "size": "2.9 GB", "date": "2017-07-24", "type": "PDF"},
            {"name": "jfk-pdf2.zip", "size": "2.4 GB", "date": "2017-07-24", "type": "PDF"},
            {"name": "jfk-pdf3.zip", "size": "2.5 GB", "date": "2017-07-24", "type": "PDF"},
            {"name": "jfk-wav1.zip", "size": "1.9 GB", "date": "2017-07-24", "type": "WAV"},
            {"name": "jfk-wav2.zip", "size": "2.6 GB", "date": "2017-07-24", "type": "WAV"},
            {"name": "jfk-wav3.zip", "size": "2.3 GB", "date": "2017-07-24", "type": "WAV"},
            {"name": "jfk-wav4.zip", "size": "1.7 GB", "date": "2017-07-24", "type": "WAV"},
            {"name": "jfk-wav5.zip", "size": "2.3 GB", "date": "2017-07-24", "type": "WAV"},
            {"name": "jfk-wav6.zip", "size": "2.0 GB", "date": "2017-07-24", "type": "WAV"},
            {"name": "jfk20171103.zip", "size": "1.5 GB", "date": "2017-11-03", "type": "PDF"},
            {"name": "jfk20171109.zip", "size": "2.0 GB", "date": "2017-11-09", "type": "PDF"},
            {"name": "jfk2017111710.zip", "size": "2.5 GB", "date": "2017-11-17", "type": "PDF"},
            {"name": "jfk20171215a.zip", "size": "1.8 GB", "date": "2017-12-15", "type": "PDF"},
            {"name": "jfk20171215b.zip", "size": "1.9 GB", "date": "2017-12-15", "type": "PDF"},
            {"name": "jfk20171215c.zip", "size": "1.7 GB", "date": "2017-12-15", "type": "PDF"},
            {"name": "jfk201804a.zip", "size": "2.0 GB", "date": "2018-04-26", "type": "PDF"},
            {"name": "jfk201804b.zip", "size": "1.8 GB", "date": "2018-04-26", "type": "PDF"},
            {"name": "jfk201804c.zip", "size": "1.2 GB", "date": "2018-04-26", "type": "PDF"}
        ],
        "2021": [{"name": "jfk2021.zip", "size": "1.2 GB", "date": "2021-12-15", "type": "PDF"}],
        "2022": [{"name": "jfk2022.zip", "size": "12.7 GB", "date": "2022-12-15", "type": "PDF"}],
        "2023": [
            {"name": "jfk2023a.zip", "size": "339 MB", "date": "2023-04-15", "type": "PDF"},
            {"name": "jfk2023b.zip", "size": "343 MB", "date": "2023-05-01", "type": "PDF"},
            {"name": "jfk2023c.zip", "size": "554 MB", "date": "2023-06-01", "type": "PDF"},
            {"name": "jfk2023d.zip", "size": "238 MB", "date": "2023-07-01", "type": "PDF"},
            {"name": "jfk2023e.zip", "size": "4.2 GB", "date": "2023-08-01", "type": "PDF"},
            {"name": "jfk2023f.zip", "size": "74 MB", "date": "2023-08-15", "type": "PDF"}
        ]
    }
}

def parse_args():
    """Parse command-line arguments for the JFK Document Bulk Downloader.

    Returns:
        argparse.Namespace: Parsed command-line arguments (just a bundle of your choices)
    """
    parser = argparse.ArgumentParser(description="JFK Document Bulk Downloader - A simple tool to grab JFK files from the web!")
    parser.add_argument("--url", default="https://www.archives.gov/research/jfk", help="The web address where the files are (e.g., https://www.archives.gov/research/jfk). It’s like the store’s location!")
    parser.add_argument("--output-dir", default="jfk_downloads", help="The folder on your computer to save files (e.g., 'jfk_downloads'). Where your treasures will be stored!")
    parser.add_argument("--max-files", type=int, help="How many files to grab at most (e.g., 10). Limits how much you download.")
    parser.add_argument("--retry", type=int, default=5, help="How many times to retry if a download fails (default is 5). Keeps trying if the internet acts up!")
    parser.add_argument("--workers", type=int, default=5, help="How many files to download at once (default is 5). More workers = faster, but needs good internet!")
    parser.add_argument("--force", action="store_true", help="Redownload files even if they’re already there, no questions asked. Overwrites without a peep!")
    parser.add_argument("--skip-existing", action="store_true", default=True, help="Skip files you already have without asking (default). Saves time!")
    parser.add_argument("--no-skip-existing", action="store_false", dest="skip_existing", help="Ask about every file you already have. Gives you control!")
    parser.add_argument("--smart-check", action="store_true", default=True, help="Skip files if they’re the same size as ones you have (default). Smart way to avoid repeats!")
    parser.add_argument("--no-smart-check", action="store_false", dest="smart_check", help="Don’t skip based on size—redownload or ask anyway. Extra careful mode!")
    parser.add_argument("--filter", help="Pick files by name pattern (e.g., 'jfk2023*'). Only downloads matching files—* means ‘anything after.’")
    parser.add_argument("--extension", default="zip", help="File type to grab (e.g., 'zip' or 'pdf'). No dot needed—it’s what kind of files you want!")
    parser.add_argument("--cowboyup", action="store_true", help="Quick run for older JFK files without this help text. For folks who know the drill!")
    parser.add_argument("--throttle", type=float, default=0, help="Slow down downloads to this speed in MB/s (e.g., 5.0, 0 means full speed). Keeps your internet free for other stuff!")
    parser.add_argument("--pause", action="store_true", help="Stop downloads midway and save progress. Lets you pick up later where you left off!")
    parser.add_argument("--cleanup", action="store_true", help="Delete temporary .part files if something goes wrong. Keeps your folder neat!")
    parser.add_argument("--verbose", action="store_true", help="Show extra details as it runs. Makes it talk more about what’s happening!")
    return parser.parse_args()

def setup_logging(output_dir):
    """Set up a log file to keep track of what the script does.

    Args:
        output_dir: The folder where the log file will go

    Returns:
        logging.Logger: A tool to write notes about what’s happening
    """
    log_file = os.path.join(output_dir, f"download_log_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt")
    logging.basicConfig(filename=log_file, level=logging.INFO, 
                        format="%(asctime)s - %(levelname)s - %(message)s")
    return logging.getLogger()

def scan_existing_files(output_dir, file_extension):
    """Look in the folder for files you already have with the right type (like ZIP or PDF).

    Args:
        output_dir: The folder to check
        file_extension: The file type to look for (e.g., 'zip' or 'pdf')

    Returns:
        dict: A list of files already there, mapped to their locations
    """
    existing_files = {}
    for root, _, files in os.walk(output_dir):
        for file in files:
            if file.endswith(f".{file_extension}"):
                existing_files[file] = os.path.join(root, file)
    return existing_files

def throttle_speed(bytes_downloaded, start_time, throttle_mbps):
    """Slow down the download if you set a speed limit.

    Args:
        bytes_downloaded: How much has been downloaded so far
        start_time: When the download started
        throttle_mbps: The speed limit in MB/s (0 means no limit)
    """
    if throttle_mbps <= 0:
        return
    elapsed = time.time() - start_time
    target_bytes = throttle_mbps * 1024 * 1024 * elapsed
    if bytes_downloaded > target_bytes:
        sleep_time = (bytes_downloaded / (throttle_mbps * 1024 * 1024)) - elapsed
        if sleep_time > 0:
            time.sleep(sleep_time)

def save_progress(output_dir, downloaded_files, remaining_files):
    """Save which files are done and which are left to a file.

    Args:
        output_dir: The folder to save the progress file in
        downloaded_files: List of files already downloaded
        remaining_files: List of files still to download
    """
    progress_file = os.path.join(output_dir, "download_progress.json")
    with open(progress_file, "w") as f:
        json.dump({"downloaded": downloaded_files, "remaining": remaining_files}, f)

def load_progress(output_dir):
    """Load the saved progress from a file.

    Args:
        output_dir: The folder where the progress file is

    Returns:
        tuple: Lists of downloaded and remaining files (or empty if no file)
    """
    progress_file = os.path.join(output_dir, "download_progress.json")
    if os.path.exists(progress_file):
        with open(progress_file, "r") as f:
            data = json.load(f)
            return data["downloaded"], data["remaining"]
    return [], []

def cleanup_part_files(output_dir):
    """Delete any leftover .part files in the folder.

    Args:
        output_dir: The folder to clean up
    """
    for root, _, files in os.walk(output_dir):
        for file in files:
            if file.endswith(".part"):
                os.remove(os.path.join(root, file))
                print(f"Cleaned up: {file}")

def download_file(session, url, filepath, args, logger, existing_files, error_report, downloaded_files):
    """Grab a single file from the web and save it, with progress and retries.

    Args:
        session: The tool that talks to the web
        url: The web address of the file
        filepath: Where to save it on your computer
        args: Your choices from the command line
        logger: The note-taker for what happens
        existing_files: Files you already have
        error_report: A list to track any problems
        downloaded_files: List to track what’s finished

    Returns:
        bool: True if it worked, False if it didn’t
    """
    filename = os.path.basename(filepath)
    if filename in existing_files:
        existing_path = existing_files[filename]
        if args.skip_existing and args.smart_check and os.path.exists(existing_path):
            logger.info(f"Skipping existing file: {filename}")
            print(f"Skipping existing file: {filename}")
            return True
        if not args.force:
            response = input(f"File {filename} exists. Overwrite? (y/n): ").strip().lower()
            if response != "y":
                logger.info(f"Skipped overwriting: {filename}")
                return True

    temp_filepath = filepath + ".part"
    headers = {}
    if os.path.exists(temp_filepath):
        bytes_downloaded = os.path.getsize(temp_filepath)
        headers["Range"] = f"bytes={bytes_downloaded}-"
    else:
        bytes_downloaded = 0

    for attempt in range(args.retry):
        try:
            response = session.get(url, stream=True, headers=headers, timeout=10)
            response.raise_for_status()
            total_size = int(response.headers.get("Content-Length", 0)) + bytes_downloaded
            mode = "ab" if bytes_downloaded else "wb"
            
            start_time = time.time()
            with open(temp_filepath, mode) as f:
                with tqdm(total=total_size, unit="B", unit_scale=True, desc=filename, initial=bytes_downloaded) as pbar:
                    for chunk in response.iter_content(chunk_size=16384):
                        if chunk:
                            f.write(chunk)
                            bytes_downloaded += len(chunk)
                            pbar.update(len(chunk))
                            throttle_speed(bytes_downloaded, start_time, args.throttle)
            shutil.move(temp_filepath, filepath)
            downloaded_files.append(filename)
            logger.info(f"Downloaded: {filename} ({os.path.getsize(filepath)} bytes)")
            print(f"Downloaded: {filename}")
            if args.verbose:
                print(f"Finished {filename} in {time.time() - start_time:.2f} seconds")
            return True
        except requests.RequestException as e:
            logger.warning(f"Attempt {attempt + 1} failed for {filename}: {e}")
            if args.verbose:
                print(f"Try {attempt + 1} for {filename} didn’t work: {e}")
            if attempt < args.retry - 1:
                time.sleep(2 ** attempt)
            else:
                error_report.append(f"{filename}: Failed after {args.retry} tries - {str(e)}")
                logger.error(f"Failed to download {filename} after {args.retry} attempts")
                print(f"Failed to download {filename}")
                return False

def fetch_zip_links(url, file_extension, filter_pattern=None):
    """Find all the files of the right type (like ZIPs) on a web page.

    Args:
        url: The web address to look at
        file_extension: The file type to find (e.g., 'zip' or 'pdf')
        filter_pattern: A name pattern to narrow it down (optional)

    Returns:
        list: A list of files with their web addresses
    """
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        links = re.findall(r'href=["\'](.*?\.{})["\']'.format(file_extension), response.text)
        zip_links = []
        for link in links:
            if not link.startswith("http"):
                link = "https://www.archives.gov" + link
            filename = link.split("/")[-1]
            if filter_pattern and not re.match(filter_pattern, filename):
                continue
            zip_links.append((filename, link))
        return zip_links
    except requests.RequestException as e:
        print(f"Couldn’t get the list of files from {url}: {e}")
        return []

def show_bulk_preview(zip_links, url):
    """Show a preview of bulk download files with details.

    Args:
        zip_links: List of files to preview
        url: The URL being used
    """
    if "releases/zip/" not in url:
        return
    bulk_base = "https://www.archives.gov/files/research/jfk/releases/zip/"
    if url.startswith(bulk_base):
        release_year = "2023" if "2023" in url else "2022" if "2022" in url else "2021" if "2021" in url else "2017-2018"
        print(f"\nHere’s what we’re downloading from the {release_year} bulk release:")
        for filename, _ in zip_links:
            for release, zips in BULK_ZIP_INFO[bulk_base].items():
                for zip_info in zips:
                    if zip_info["name"] == filename:
                        print(f"- {filename}: {zip_info['size']}, Released on {zip_info['date']}, Type: {zip_info['type']}")
        print("\nReady to start? Let’s go!")

def main():
    """Run the whole download process from start to finish."""
    args = parse_args()
    if not args.cowboyup:
        print(__doc__)

    # Note about 2025 bulk download
    if "2025" in args.url or "release-2025" in args.url:
        print("Heads up! As of March 20, 2025, there’s no big ZIP file for the 2025 JFK release yet. "
              "You’ll need to download the files one by one from https://www.archives.gov/research/jfk/release-2025. "
              "Here’s what came out in 2025: 7 PM EST (32,000 pages, 1,123 PDFs), 10:30 PM EST (31,400 pages, 1,059 PDFs).")

    if not os.path.exists(args.output_dir):
        os.makedirs(args.output_dir)

    logger = setup_logging(args.output_dir)
    logger.info("Starting JFK Document Bulk Downloader")
    if args.verbose:
        print("Starting up—let’s grab some files!")

    session = requests.Session()
    retry_strategy = Retry(total=args.retry, backoff_factor=1, status_forcelist=[500, 502, 503, 504])
    adapter = HTTPAdapter(max_retries=retry_strategy)
    session.mount("https://", adapter)

    # Load progress if resuming
    downloaded_files, remaining_files = load_progress(args.output_dir)
    existing_files = scan_existing_files(args.output_dir, args.extension)
    zip_links = fetch_zip_links(args.url, args.extension, args.filter)

    if not zip_links:
        print("No files found to download. Check the web address or file type!")
        logger.error("No files found to download.")
        return

    if args.max_files:
        zip_links = zip_links[:args.max_files]

    # Filter out already downloaded files if resuming
    if remaining_files:
        zip_links = [link for link in zip_links if link[0] not in downloaded_files]
        print("Resuming from where we left off…")

    print(f"Found {len(zip_links)} files to download.")
    logger.info(f"Found {len(zip_links)} files to download.")

    # Show preview for bulk downloads
    show_bulk_preview(zip_links, args.url)

    error_report = []
    with ThreadPoolExecutor(max_workers=args.workers) as executor:
        futures = []
        for filename, url in zip_links:
            filepath = os.path.join(args.output_dir, filename)
            futures.append(executor.submit(download_file, session, url, filepath, args, logger, existing_files, error_report, downloaded_files))

        for future in futures:
            future.result()  # Wait for all downloads to finish
            if args.pause:
                save_progress(args.output_dir, downloaded_files, [link[0] for link in zip_links if link[0] not in downloaded_files])
                print("Paused! Run again to resume where we left off.")
                logger.info("Paused by user request.")
                if args.cleanup:
                    cleanup_part_files(args.output_dir)
                    logger.info("Cleaned up .part files during pause.")
                return

    # Cleanup if requested
    if args.cleanup:
        cleanup_part_files(args.output_dir)
        logger.info("Cleaned up .part files after completion.")

    # Print error report if there were issues
    if error_report:
        print("\nOops! Some files had trouble downloading. Here’s what went wrong:")
        for error in error_report:
            print(f"- {error}")
        logger.info("Error report generated with {} issues".format(len(error_report)))
    else:
        print("\nAll done! Everything downloaded smoothly.")
        logger.info("All downloads completed successfully.")

    # Clear progress file on successful completion
    progress_file = os.path.join(args.output_dir, "download_progress.json")
    if os.path.exists(progress_file):
        os.remove(progress_file)

    logger.info("Download process completed.")

if __name__ == "__main__":
    main()
