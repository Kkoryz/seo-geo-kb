---
title: "Download search queries data using Python | Google Search Central Blog | Google for Developers"
source_url: https://developers.google.com/search/blog/2011/12/download-search-queries-data-using
category: google-search-central
section: "Google Search Central — official technical SEO + structured data docs"
date: 2011-12-22
---

# Download search queries data using Python | Google Search Central Blog | Google for Developers

Thursday, December 22, 2011

For all the developers who have expressed interest in getting programmatic access to the search
queries data for their sites in Webmaster Tools, we've got some good news. You can now get access
to your search queries data in
[CSV format](https://en.wikipedia.org/wiki/Comma-separated_values)
using a open source Python script from the
[webmaster-tools-downloads](https://code.google.com/p/webmaster-tools-downloads/)
project. Search queries data is not currently available via the Webmaster Tools API, which has
been a common API user request that we're considering for the next API update. For those of you
who need access to search queries data right now, let's look at an example of how the search
queries downloader Python script can be used to download your search queries data and upload it
to a Google Spreadsheet in Google Docs.

## Example usage of the search queries downloader Python script

-
If Python is not already installed on your machine, download and install
[Python](https://python.org/download/). -
Download and install the
[Google Data APIs Python Client Library](https://code.google.com/apis/gdata/articles/python_client_lib). -
Create a folder and add the
script to the newly created folder.`downloader.py`

-
Copy the
script to the same folder as`example-create-spreadsheet.py`

`downloader.py`

and edit it to replace the example values for`website`

,`email`

and`password`

with valid values for your Webmaster Tools verified site. -
Open a Terminal window and run the
`example-create-spreadsheet.py`

script by entering`python example-create-spreadsheet.py`

at the terminal window command line. - Visit Google Docs to see a new spreadsheet containing your search queries data.

If you just want to download your search queries data in a .csv file without uploading the data to
a Google spreadsheet use
[ example-simple-download.py](https://code.google.com/p/webmaster-tools-downloads/source/browse/example-simple-download.py)
instead of

`example-create-spreadsheet.py`

in the example above.
You could easily configure these scripts to be run daily or monthly to archive and view your search queries data across larger date ranges than the current one month of data that is available in Webmaster Tools, for example, by setting up a cron job or using Windows Task Scheduler.

An important point to note is that this script example includes user name and password credentials within the script itself. If you plan to run this in a production environment you should follow security best practices like using encrypted user credentials retrieved from a secure data storage source. The script itself uses HTTPS to communicate with the API to protect these credentials.

Take a look at the search queries downloader script and start using search queries data in your
own scripts or tools. Let us know if you have questions or feedback in the
[Webmaster Help Forum](https://support.google.com/webmasters/community/label?lid=462896acb3879639&hl=en).
