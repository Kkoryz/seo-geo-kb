---
title: "It's 404 week at Webmaster Central | Google Search Central Blog | Google for Developers"
source_url: https://developers.google.com/search/blog/2008/08/its-404-week-at-webmaster-central
category: google-search-central
section: "Google Search Central — official technical SEO + structured data docs"
date: 2008-08-11
---

# It's 404 week at Webmaster Central | Google Search Central Blog | Google for Developers

This week we're publishing several blog posts dedicated to helping you with one response code:
404.
Response codes
are a numeric status (like 200 for "OK", 301 for "Moved Permanently")
that a webserver returns in response to a request for a URL. The 404 response code
should be returned for a file "Not Found".

When a user sends a request for your webpage, your webserver looks for the corresponding file for
the URL. If a file exists, your webserver likely responds with a 200 response code
along with a message (often the content of the page, such as the HTML).

So what's a 404? Let's say that in the link to "Visit Google Apps" above, the link is
broken because of a typing error when coding the page. Now when a user clicks "Visit Google Apps",
the particular webpage/file isn't located by the webserver. The webserver should return a
404 response code, meaning "Not Found".

Now that we're all on board with the basics of 404 errors, stay tuned for even more
information on making 404 errors good for users and for search engines.

Written by Maile Ohye, Developer Programs Tech Lead

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Missing the information I need","missingTheInformationINeed","thumb-down"],["Too complicated / too many steps","tooComplicatedTooManySteps","thumb-down"],["Out of date","outOfDate","thumb-down"],["Samples / code issue","samplesCodeIssue","thumb-down"],["Other","otherDown","thumb-down"]],[],[],["Webservers use numeric response codes to indicate the status of a URL request. A `404` code signifies that a requested file was \"Not Found.\" When a user requests a webpage, the server searches for the corresponding file. If the file isn't found, the server should return a `404` error. Future posts will discuss optimizing `404` errors for both users and search engines. Response codes such as `200` means the file is found and `301` means the file has been permanently moved.\n"]]
