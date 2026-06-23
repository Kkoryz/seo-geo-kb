---
title: "Improved Flash indexing | Google Search Central Blog | Google for Developers"
source_url: https://developers.google.com/search/blog/2008/06/improved-flash-indexing
category: google-search-central
section: "Google Search Central — official technical SEO + structured data docs"
date: 2008-07-01
---

# Improved Flash indexing | Google Search Central Blog | Google for Developers

Tuesday, July 01, 2008

We've received numerous requests to improve our indexing of Adobe Flash files. Today, Ron Adler
and Janis Stipins—software engineers on our indexing team—will provide us with more
in-depth information about our recent announcement that
[we've greatly improved our ability to index Flash](https://googleblog.blogspot.com/2008/06/google-learns-to-crawl-flash.html).

**Which Flash files can Google better index now?** We've improved our ability to index textual
content in SWF files of all kinds. This includes Flash "gadgets" such as buttons or menus,
self-contained Flash websites, and everything in between.

**What content can Google better index from these Flash files?** All of the text that users
can see as they interact with your Flash file. If your website contains Flash, the textual
content in your Flash files can be used when Google generates a snippet for your website. Also,
the words that appear in your Flash files can be used to match query terms in Google searches.

In addition to finding and indexing the textual content in Flash files, we're also discovering URLs that appear in Flash files, and feeding them into our crawling pipeline—just like we do with URLs that appear in non-Flash webpages. For example, if your Flash application contains links to pages inside your website, Google may now be better able to discover and crawl more of your website.

**What about non-textual content, such as images?** At present, we are only discovering and
indexing textual content in Flash files. If your Flash files only include images, we will not
recognize or index any text that may appear in those images. Similarly, we do not generate any
anchor text for Flash buttons which target some URL, but which have no associated text.

Also note that we do not index FLV files, such as the videos that play on YouTube, because these files contain no text elements.

**How does Google "see" the contents of a Flash file?** We've developed an algorithm that
explores Flash files in the same way that a person would, by clicking buttons, entering input,
and so on. Our algorithm remembers all of the text that it encounters along the way, and that
content is then available to be indexed. We can't tell you all of the proprietary details, but
we can tell you that the algorithm's effectiveness was
[improved](https://www.adobe.com/devnet/flashplayer/articles/swf_searchability)
by utilizing Adobe's new Searchable SWF library.

**What do I need to do to get Google to index the text in my Flash files?** Basically, you
don't need to do anything. The improvements that we have made do not require any special action
on the part of web designers or webmasters. If you have Flash content on your website, we will
automatically begin to index it, up to the limits of our current technical ability (see next
question).

That said, you should be aware that Google is now able to see the text that appears to visitors of your website. If you prefer Google to ignore your less informative content, such as a "copyright" or "loading" message, consider replacing the text within an image, which will make it effectively invisible to us.

**What are the current technical limitations of Google's ability to index Flash?** There are
three main limitations at present, and we are already working on resolving them:

- Googlebot does not execute some types of JavaScript. So if your web page loads a Flash file via JavaScript, Google may not be aware of that Flash file, in which case it will not be indexed.
- We currently do not attach content from external resources that are loaded by your Flash files. If your Flash file loads an HTML file, an XML file, another SWF file, etc., Google will separately index that resource, but it will not yet be considered to be part of the content in your Flash file.
- While we are able to index Flash in almost all of the languages found on the web, currently there are difficulties with Flash content written in bidirectional languages. Until this is fixed, we will be unable to index Hebrew language or Arabic language content from Flash files.

We're already making progress on these issues, so stay tuned!

**Update in July 2008**: Everyone, thanks for your great questions and feedback. Our focus is
to improve search quality for all users, and with better Flash indexing we create more meaningful
search results. Listed below, we've also answered some of the most prevalent questions. Thanks
again!

A flash site in search results for the query nasa deep impact animation before and after the improvements mentioned in this post

*Helping us access and index your Flash files*

@fintan: We verified with Adobe that the textual content from legacy sites, such as those scripted with AS1 and AS2, can be indexed by our new algorithm.

@andrew, jonny m, erichazann, mike, ledge, stu, rex, blog, dis: For our July 1st launch, we didn't enable Flash indexing for Flash files embedded via

`SWFObject`

. We're now rolling out an update that enables support for common JavaScript techniques for embedding Flash, including`SWFObject`

and`SWFObject2`

.@mike: At this time, content loaded dynamically from resource files is not indexed. We've noted this feature request from several webmasters—look for this in a near future update.


Update on July 29, 1010:Please note that our ability to[load external resources]is live.

*Interaction of HTML pages and Flash*

@captain cuisine: The text found in Flash files is treated similarly to text found in other files, such as HTML, PDFs, etc. If the Flash file is embedded in HTML (as many of the Flash files we find are), its content is associated with the parent URL and indexed as single entity.

@jeroen: Serving the same content in Flash and an alternate HTML version could cause us to find duplicate content. This won't cause a penalty—we don't lower a site in ranking because of duplicate content. Be aware, though, that search results will most likely only show one version, not both.

@All: We're trying to serve users the most relevant results possible regardless of the file type. This means that standalone Flash, HTML with embedded Flash, HTML only, PDFs, etc., can all have the potential to be returned in search results.


*Indexing large Flash files*

@dsfdgsg: We've heard requests for deep linking (linking to specific content inside file) not just for Flash results, but also for other large documents and presentations. In the case of Flash, the ability to deep link will require additional functionality in Flash with which we integrate.

@All: The majority of the existing Flash files on the web are fine in regard to filesize. It shouldn't be too much of a concern.


*More details about our Flash indexing algorithm*

@brian, marcos, bharath: Regarding ActionScript, we're able to find new links loaded through ActionScript. We explore Flash like a website visitor does, we do not decompile the SWF file. Unless you're making ActionScript visible to users, Google will not expose ActionScript code.

@dlocks: We respect

`nofollow`

wherever we encounter it in HTML.
