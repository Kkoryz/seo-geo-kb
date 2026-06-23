---
title: "If you see a \"we couldn't find your verification file\" error when you try to verify | Google Search Central Blog | Google for Developers"
source_url: https://developers.google.com/search/blog/2006/03/if-you-see-we-couldnt-find-your
category: google-search-central
section: "Google Search Central — official technical SEO + structured data docs"
date: 2006-03-09
---

# If you see a "we couldn't find your verification file" error when you try to verify | Google Search Central Blog | Google for Developers

If you see a "we couldn't find your verification file" error when you try to verify

March 09, 2006

When you
verify site ownership,
we check to see if the verification file exists on your webserver. We also make sure that your
server returns a status of 404 (not found) when we request a file that doesn't exist.
We do this to make sure that when we check to see if the verification file exists, we're getting
the right response because it does exist and not because the server is misconfigured.

Some of you have gotten the following message when trying to verify your site:
"We couldn't find your verification file. Make sure it is named correctly and is
uploaded to the correct location." But when you check the file in a browser, it does
exist.

We have looked into this and have found that we are displaying the incorrect error message. What
is actually happening in this case is that when we request a file that doesn't exist, we are
getting a response other than 404 or 200. (If we get a response of
200, we display a
different error message.)

We are working to display the correct response for these cases. In the meantime, if you see this
message when you try to verify and your verification does exist in the correct location, check
your webserver configuration and make sure that it returns a status of 404 when a
request is made for a non-existent page.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Missing the information I need","missingTheInformationINeed","thumb-down"],["Too complicated / too many steps","tooComplicatedTooManySteps","thumb-down"],["Out of date","outOfDate","thumb-down"],["Samples / code issue","samplesCodeIssue","thumb-down"],["Other","otherDown","thumb-down"]],[],[],["Site verification checks involve confirming the existence of a verification file and ensuring the server returns a `404` status for non-existent files. An incorrect error message (\"We couldn't find your verification file\") is displayed when the server returns a status other than `404` or `200` for missing files. If this error occurs and the file exists, users should verify their server configuration to ensure it produces a `404` status for files not present. The developers are working to fix the error message.\n"]]
