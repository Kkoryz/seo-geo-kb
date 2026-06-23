---
title: "Switching to the new website verification API | Google Search Central Blog | Google for Developers"
source_url: https://developers.google.com/search/blog/2013/12/switching-to-new-website-verification
category: google-search-central
section: "Google Search Central — official technical SEO + structured data docs"
date: 2013-12-23
---

# Switching to the new website verification API | Google Search Central Blog | Google for Developers

Monday, December 23, 2013

Just over a year ago we introduced a new
[API for website verification](/site-verification)
for Google services. In the spirit of keeping things simple and focusing our efforts, we've
decided to deprecate the
[old verification API method](/webmaster-tools/docs/2.0/developers_guide_protocol#AD_Verifying)
on March 31st, 2014. The rest of the API will remain unchanged, this only affects the verification
method. For more information about verification in general, please see our
[site verification Help Center article](https://support.google.com/webmasters/answer/35179).

One advantage of upgrading to the new API for verification is that it uses the same client libraries as most other Google APIs, which simplifies integration with other apps and tools. Getting started is easy, especially if you're used to other Google APIs:

-
Download the
[Google API client library](/site-verification/libraries)for your favorite programming language. -
Learn about the
[Site Verification API](/site-verification)and its methods. -
Allow your users to authenticate with
[OAuth](/identity/protocols/oauth2). - Start verifying!

If you can't wait to try it out and are a fan of command lines, here's a shortcut:

-
Download and install
[oacurl](https://code.google.com/p/oacurl/). -
Authenticate with a Google Account:
$ java -cp oacurl-1.2.0.jar com.google.oacurl.Login \ --scope https://www.googleapis.com/auth/siteverification

-
Request the verification information:
$ echo '{ "verificationMethod": "FILE", "site": { "identifier": "https://www.example.com", "type": "SITE" } }' | \ java -cp oacurl-1.2.0.jar com.google.oacurl.Fetch \ 'https://www.googleapis.com/siteVerification/v1/token' \ --content-type JSON -X=POST

-
Create and add the file to your website, then verify:
$ echo '{ "site": { "identifier": "https://www.example.com", "type": "SITE" } }' | \ java -cp oacurl-1.2.0.jar com.google.oacurl.Fetch \ 'https://www.googleapis.com/siteVerification/v1/webResource?verificationMethod=FILE' \ --content-type JSON -X=POST

- Done!

We hope this API will make it easier to implement Google site verification in your projects.
Should you have any questions, you can post in our
[Webmaster Help Forum](https://support.google.com/webmasters/threads?hl=en&thread_filter=(category:search_console)).
