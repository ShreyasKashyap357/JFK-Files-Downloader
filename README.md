# JFK Files Downloader - Your Portal to Historical Records!

Greetings, history detectives! Welcome to **JFK Files Downloader**, a Python script built to retrieve official JFK assassination records from the National Archives (https://www.archives.gov/research/jfk). Covering releases from 2017 to 2025, this tool fetches a treasure trove of declassified files—CIA memos, FBI reports, audio recordings, and more—tied to November 22, 1963. Whether you’re a coding newbie, a researcher, or just intrigued, this script makes downloading these files a snap!

This project lives on GitHub at [ShreyasKashyap357/JFK-Files-Downloader](https://github.com/ShreyasKashyap357/JFK-Files-Downloader). Contributions, issues, and stars are welcome!

## Why This Tool Shines
Say goodbye to endless clicking! Here’s what sets this script apart:
- Downloads bulk ZIP files (2017-2023) or individual files (e.g., 2025’s 2,182 PDFs and more)
- Supports all declassified file types—PDFs, WAVs, and beyond—in individual mode
- Runs up to 5 downloads at once in individual mode for speed
- Retries failed downloads to beat internet hiccups
- Shows progress bars for every file
- Pauses and resumes long downloads—like a history DVR
- Cleans up temp files if things crash
- Limits speed to share your internet with other apps
- Previews bulk files with names, sizes, dates, and types
- Logs every step in a timestamped file
- Chats more with verbose mode
- Handles existing files your way—skip, overwrite, or ask!

## JFK Release History: The Complete Timeline
The JFK Records Act of 1992 sparked these releases. Here’s the detailed rundown with document counts and dates:
- **2017 Releases**:
  - **July 24**: 3,810 documents (first wave with PDFs and WAV audio files)
  - **October 26**: 2,891 documents (early follow-up)
  - **November 3**: 676 documents
  - **November 9**: 13,213 documents
  - **November 17**: 10,744 documents
  - **December 15**: 3,539 documents (some PDFs bundle multiple records due to batch scanning)
- **2018 Release**:
  - **April 26**: 18,731 documents (final 2017-2018 batch, also with scanning quirks)
- **2021 Release**:
  - **December 15**: 1,491 documents (a concise but vital drop)
- **2022 Release**:
  - **December 15**: 13,173 documents (a massive one-day release)
- **2023 Releases**:
  - **April 13**: 422 documents (start of 2023’s phased releases)
  - **April 27**: 355 documents
  - **May 11**: 502 documents
  - **June 13**: 290 documents
  - **June 27**: 1,103 documents
  - **August 24**: 21 documents (smallest 2023 batch)
- **2025 Release**:
  - **March 18**: 63,400 pages in 2,182 files—7 PM IST (1,123 files), 10:30 PM IST (1,059 files), per Trump’s directive

## File Sizes and Details: Bulk Downloads
For 2017-2023, bulk ZIPs are available via email (`bulkdownload@nara.gov`) or https://www.archives.gov/files/research/jfk/releases/zip/. Here’s the breakdown with MD5 hashes:
- **2017-2018 Total: ~36.1 GB**
  - **July 24, 2017**:
    - jfk-pdf1.zip (2.9 GB, MD5: 80e2188593fca6467acc1c4214f3ba9b)
    - jfk-pdf2.zip (2.4 GB, MD5: 55af7bb87eb760c9e6dead830a97fc7c)
    - jfk-pdf3.zip (2.5 GB, MD5: ae800b0b61302e0efe82b3014700d911)
    - jfk-wav1.zip (1.9 GB, MD5: 98fc25b58445d399ef5842c403c56661)
    - jfk-wav2.zip (2.6 GB, MD5: 83404cb0760f5dba932c8214b34a3f4a)
    - jfk-wav3.zip (2.3 GB, MD5: f94ac4a195443ab66c601cbb4ca92dd1)
    - jfk-wav4.zip (1.7 GB, MD5: 8730b6e5efd6e23c477b5c20b0a5887a)
    - jfk-wav5.zip (2.3 GB, MD5: e838012e01444430d7aa1bc4bc2d2ba4)
    - jfk-wav6.zip (2.0 GB, MD5: 3ba6263405a2f2373fff0bb8aeada662)
  - **November 3, 2017**:
    - jfk20171103.zip (2.6 GB, MD5: 6b4ab22682c8827a4dc25906de9814ac)
  - **November 9, 2017**:
    - jfk20171109.zip (3.2 GB, MD5: 96080aff5e40925b3330c9169c70cfc9)
  - **November 17, 2017**:
    - jfk2017111710.zip (3.7 GB, MD5: f619fabd567e4ffa4e4176107322f0f8)
  - **December 15, 2017**:
    - jfk20171215a.zip (2.0 GB, MD5: d6928b8efc1fcd6f301c0b89e850173d)
    - jfk20171215b.zip (2.2 GB, MD5: d9e719011679b755c4f9f22fe9956640)
    - jfk20171215c.zip (1.9 GB, MD5: d664566a0c925464bcd9349334591d71)
  - **April 26, 2018**:
    - jfk201804a.zip (1.1 GB, MD5: 74f0fffb568724abda4a0f02ae8cb825)
    - jfk201804b.zip (1.0 GB, MD5: 4464ea7788a479f7b3badc0e9b4e6f9c)
    - jfk201804c.zip (1.2 GB, MD5: 7ebf15c13c0605e7ce3b83ce3ba90770)
- **2021 Total: 1.2 GB**
  - **December 15, 2021**:
    - jfk2021.zip (1.2 GB, MD5: 3b41d5d25a211c681a8c5f79e3720b70)
- **2022 Total: 12.7 GB**
  - **December 15, 2022**:
    - jfk2022.zip (12.7 GB, MD5: 350323648f093d3aa7b204c5445e33da)
- **2023 Total: ~5.7 GB**
  - **April 13, 2023**:
    - jfk2023a.zip (339 MB, MD5: 5c5f2eb2db9b259362e1437909892e97)
  - **April 27, 2023**:
    - jfk2023b.zip (343 MB, MD5: 6fc670f350cd3f32a7f53aaf72ffe443)
  - **May 11, 2023**:
    - jfk2023c.zip (554 MB, MD5: 907cbb9a2b9a3f48069a9bb90d152829)
  - **June 13, 2023**:
    - jfk2023d.zip (238 MB, MD5: 4452423375cd3f885677ff380c7af365)
  - **June 27, 2023**:
    - jfk2023e.zip (4.2 GB, MD5: b48fefd4f94f23b19f8aa890921e53b4)
  - **August 24, 2023**:
    - jfk2023f.zip (74 MB, MD5: b42f95619706901b69cf2e104747009d)
- **2025 Total: ~5.1-5.5 GB** (estimated, 6 GB uncompressed, 2,182 files, no bulk ZIP as of March 20, 2025)

Total across 2017-2025: ~61-62 GB. Make sure your drive has room!

## Bulk vs. Individual Downloads: A Deep Dive
This script offers two distinct download modes, each tailored to different needs:
- **Bulk Mode**:
  - **Purpose**: Downloads pre-zipped files for 2017-2018, 2021, 2022, and 2023 from a dedicated ZIP repository (e.g., https://www.archives.gov/files/research/jfk/releases/zip/). These ZIPs bundle all files from a release—PDFs, WAVs, or others—into one neat package.
  - **Process**: The script scans the page for `.zip` links (customizable via --extension), matches them to its internal list (lines 45-111), and displays a preview before starting. For instance, running it on the 2023 ZIP page shows: “jfk2023a.zip: 339 MB, Released on 2023-04-13, Type: PDF” and “jfk-wav1.zip: 1.9 GB, Released on 2017-07-24, Type: WAV” if WAVs are present. It then asks for confirmation (“Ready to start?”) before fetching each ZIP.
  - **Advantages**: Lightning-fast—downloads one file instead of thousands. Minimal processing since files are pre-bundled. Ideal for grabbing entire releases like 2022’s 12.7 GB in one shot. Uses less temporary space (e.g., 12.7 GB vs. 25 GB unzipped).
  - **Limitations**: Limited to years with bulk ZIPs (2017-2023). No granular control—you get the full batch (e.g., all 18 ZIPs from 2017-2018). Can’t filter within ZIPs—everything comes as-is.
  - **Best For**: Complete collections of older releases when speed and simplicity matter.
- **Individual Mode**:
  - **Purpose**: Downloads individual declassified files—PDFs, WAVs, or any type—from any release page (e.g., https://www.archives.gov/research/jfk/release-2025). It’s your go-to for 2025’s 2,182 files or cherry-picking from earlier years.
  - **Process**: Scans the page for links matching your --extension (default “zip”, but try “pdf” or “wav”). Applies filters (e.g., --filter "jfk*") and downloads each file separately. For 2025, it grabs all 2,182 files (mostly PDFs) unless limited. For 2017, it could fetch individual WAVs if linked. No preview for huge sets like 2025 (too many files!), but you see progress bars per file.
  - **Advantages**: Ultimate flexibility—download PDFs, WAVs, or other types from any year. Pause/resume works great for long lists (saves progress to “download_progress.json”). Filter by name or limit with --max-files for precision (e.g., 5 WAVs from 2017).
  - **Limitations**: Slower than bulk—fetching 2,182 files takes time vs. one ZIP. Needs more temp space (e.g., 12 GB for 2025 vs. 6 GB zipped). No batch preview due to volume, though progress bars keep you posted.
  - **Best For**: 2025’s files (no bulk ZIP yet), specific file types (e.g., WAVs from 2017), or custom subsets from any release.

## What You’ll Need to Get Started
- **Python 3**: Free from https://www.python.org/downloads/. It’s the engine behind this script!
- **Libraries**: Install via terminal or IDE:
  ```pip install requests tqdm```
  - “requests”: Pulls files from the web
  - “tqdm”: Draws progress bars
- **Internet**: 50 Mbps downloads 2025’s 6 GB in ~30 minutes. Slower works—just takes longer!
- **Disk Space**: Bulk mode needs space for ZIPs (e.g., 12.7 GB for 2022). Individual mode needs ~12 GB for 2025 (6 GB files + 6 GB temp).

## How to Run It: Terminal or IDE
1. Clone or download this repo to a folder (e.g., “D:\JFK Files”)
2. Launch it your way:
   - **Terminal**:
     - Windows: Win + R, “cmd”, Enter
     - Mac/Linux: Open “Terminal”
     - Navigate: ```cd D:\JFK Files```
     - Run: ```python JFK_Files_Downloader.py```
   - **VS Code**:
     - Open folder: File > Open Folder > “D:\JFK Files”
     - Open script: Double-click `JFK_Files_Downloader.py`
     - Run: “Run Python File” triangle (top right) or F5
     - Output: “Terminal” tab below
   - **PyCharm**:
     - Open project: File > Open > “D:\JFK Files”
     - Open script: Double-click `JFK_Files_Downloader.py`
     - Run: Right-click > Run ‘JFK_Files_Downloader’ or Shift + F10
     - Output: “Run” tab
3. First run shows a help screen—see options below!

## Usage Examples: Get Creative!
- **Bulk 2023 ZIPs**:
  ```python JFK_Files_Downloader.py --url https://www.archives.gov/files/research/jfk/releases/zip/```
  Output: “jfk2023a.zip: 339 MB, Released on 2023-04-13, Type: PDF”
- **5 WAVs from 2017**:
  ```python JFK_Files_Downloader.py --url https://www.archives.gov/research/jfk --extension wav --max-files 5```
- **2025 PDFs with Throttle**:
  ```python JFK_Files_Downloader.py --url https://www.archives.gov/research/jfk/release-2025 --extension pdf --throttle 5.0```
- **Pause Mid-Run**:
  ```python JFK_Files_Downloader.py --pause```
- **Verbose Details**:
  ```python JFK_Files_Downloader.py --verbose```

## What You’ll See
- **Progress Bars**: “jfk-wav1.zip: 76%|██████████  | 1.45G/1.9G [00:33<00:10, 45.0MB/s]”
- **Logs**: “download_log_20250320_171800.txt”
- **Errors**: “jfk2023a.zip: Failed after 5 tries - Timeout”

## Options: Your Control Panel
Run ```python JFK_Files_Downloader.py``` for details:
- **--url URL**: Web address for files. Default: https://www.archives.gov/research/jfk. Use https://www.archives.gov/files/research/jfk/releases/zip/ for bulk or https://www.archives.gov/research/jfk/release-2025 for 2025.
- **--output-dir DIR**: Folder to save files. Default: “jfk_downloads”. Try “D:\JFK_Records” for a custom path.
- **--max-files N**: Limits files downloaded. Set to 5 to grab only 5 out of 100—perfect for testing or small hauls!
- **--retry ATTEMPTS**: Retries per failed download. Default 5—tries 5 times if the web falters.
- **--workers N**: Simultaneous downloads. Default 5—lower to 2 for slow nets, up to 8 for speed!
- **--force**: Overwrites existing files without asking. Freshens your collection fast!
- **--skip-existing**: Skips files you have. Default on—avoids duplicates effortlessly.
- **--no-skip-existing**: Asks “overwrite?” for existing files. Full control mode!
- **--smart-check**: Skips if sizes match. Default on—size match means same file.
- **--no-smart-check**: Ignores size matches—checks every file. For the cautious!
- **--filter PATTERN**: Grabs files by name pattern. “jfk2023*” gets 2023 files—* is a wildcard!
- **--extension EXT**: File type to fetch. Default “zip”—use “pdf” or “wav” for individual files!
- **--cowboyup**: Fast pre-2025 bulk run, no help screen. Pro shortcut!
- **--throttle MBPS**: Caps speed (e.g., 5.0 MB/s). Saves bandwidth for other tasks!
- **--pause**: Stops and saves progress. Resume later—great for big jobs!
- **--cleanup**: Deletes temp “.part” files. Keeps things tidy!
- **--verbose**: Shows extra details—retries, times, and more!

## Code Efficiency: Performance Breakdown
- **Parallel Downloads**: 5 threads (line 363) in individual mode—5 files at 1 min each drop from 5 min to ~1 min!
- **Retry Logic**: 5 retries (line 104) with backoff (line 262: 1s, 2s, 4s)—beats network drops.
- **Memory Use**: 16 KB chunks (line 252)—100 MB file uses just 16 KB RAM.
- **Progress Saving**: “download_progress.json” (line 165)—pause/resume is smooth.
- **Speed Control**: Throttles via line 149—balances download and other internet use.

## Code Tweaking: Make It Yours
Edit `JFK_Files_Downloader.py`:
- **Default Folder**: Line 84: `default="jfk_downloads"` to `"D:\JFK_Archives"`—set your preferred save spot.
- **Worker Count**: Line 90: `default=5` to `default=8`—up to 8 for speed, down to 3 for stability.
- **Chunk Size**: Line 252: `chunk_size=16384` to `32768`—32 KB chunks for faster writes (test on SSDs!).
- **Retry Boost**: Line 88: `default=5` to `default=7`—7 retries for tough networks (max wait ~64s).
- **Throttle Default**: Line 99: `default=0` to `default=3.0`—starts at 3 MB/s for shared connections.
- **Verbose Always**: Line 102: `action="store_true"` to `default=True`—chatty by default.
- **File Type**: Line 95: `default="zip"` to `default="wav"`—focus on WAVs out of the box.
- **Timeout**: Line 248: `timeout=10` to `timeout=15`—15s for slow servers.

## Troubleshooting: Fix It Fast
- **“Python not found”**: Install from https://www.python.org/downloads/. Test: ```python --version```
- **“No module”**: ```pip install requests tqdm```. Verify: ```pip list```
- **“No files”**: Check URL/internet. Test: ```ping archives.gov```
- **“Disk full”**: 2025 needs 12 GB. Check: ```dir``` (Windows) or ```df -h``` (Mac/Linux)
- **“Slow”**: Test at https://speedtest.net. Adjust --workers or --throttle

## Future Ideas
- **Size Preview**: Estimate total GB upfront
- **File Sorting**: Prioritize by size or type
- **Retry Queue**: Redo failures at the end

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details. Feel free to use, modify, and share!

## Start Your Journey!
Clone this repo, save as `JFK_Files_Downloader.py`, and explore JFK history—terminal or IDE, you’re set! Questions? Open an issue or reach out!
