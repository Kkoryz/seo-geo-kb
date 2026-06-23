---
title: "Flash indexing with external resource loading | Google Search Central Blog | Google for Developers"
source_url: https://developers.google.com/search/blog/2009/06/flash-indexing-with-external-resource
category: google-search-central
section: "Google Search Central — official technical SEO + structured data docs"
date: 2009-06-19
---

# Flash indexing with external resource loading | Google Search Central Blog | Google for Developers

We just added external resource loading to our
Flash indexing
capabilities. This means that when a SWF file loads content from some other file—whether it's
text, HTML, XML, another SWF, etc.—we can index this external content too, and associate it with
the parent SWF file and any documents that embed it.

This new capability improves search quality by allowing relevant content contained in external
resources to appear in response to users' queries. For example, this result currently comes up in
response to the query
2002 VW Transporter 888:

Prior to this launch, this result did not appear, because all of the relevant content is contained
in an XML file loaded by a SWF file.

To date, when Google encounters SWF files on the web, we can:

Index textual content displayed as a user interacts with the file. We click buttons and enter
input, just like a user would.

Discover links within Flash files.

Load external resources and associate the content with the parent file.

Support common JavaScript techniques for embedding Flash, such as SWFObject and
SWFObject2.

Index sites scripted with AS1 and AS2, even if the ActionScript is obfuscated.

If you don't want your SWF file or any of its external resources crawled by search engines, please
use an appropriate robots.txt rule.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Missing the information I need","missingTheInformationINeed","thumb-down"],["Too complicated / too many steps","tooComplicatedTooManySteps","thumb-down"],["Out of date","outOfDate","thumb-down"],["Samples / code issue","samplesCodeIssue","thumb-down"],["Other","otherDown","thumb-down"]],[],[],["Google now indexes content loaded externally by SWF files, associating it with the parent SWF and embedding documents. This enhances search quality by including relevant external content in search results. Google indexes textual content displayed through user interaction, discovers links within Flash files, loads external resources, and supports common JavaScript embedding techniques. Sites using AS1, AS2, and AS3 are also indexed. To prevent crawling, utilize a `robots.txt` rule.\n"]]
