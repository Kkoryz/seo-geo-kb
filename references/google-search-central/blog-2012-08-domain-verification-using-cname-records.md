---
title: "Domain verification using CNAME records | Google Search Central Blog | Google for Developers"
source_url: https://developers.google.com/search/blog/2012/08/domain-verification-using-cname-records
category: google-search-central
section: "Google Search Central — official technical SEO + structured data docs"
date: 2012-08-02
---

# Domain verification using CNAME records | Google Search Central Blog | Google for Developers

Thursday, August 02, 2012

In order to use Google services like
[Webmaster Tools](https://search.google.com/search-console)
and [Google Apps](https://www.google.com/enterprise/apps/business/)
you must verify that you own the site or domain. One way you can do this is by creating a
[DNS TXT record](/search/blog/2010/03/dns-verification-ftw)
to prove your ownership of the domain. Now you can also use

**DNS**to verify ownership of your domains. This is a new domain verification option for users that are not able to create DNS

[records](https://en.wikipedia.org/wiki/CNAME_record)`CNAME`

`TXT`

records for their domains.
For example, if you own the domain **example.com**, you can verify your ownership of the domain
by creating a DNS `CNAME`

record as follows.

-
Add the domain example.com to your account either in
[Webmaster Tools](https://search.google.com/search-console)or directly on the[Verification Home page](https://www.google.com/webmasters/verification/). - Select the Domain Name Provider method of verification, then select your domain name provider that manages your DNS records or "Other" if your provider is not on this list.
-
Based on your selection you may either see the instructions to set a
`CNAME`

record or see a link to the option**Add a**. Follow the instructions to add the specified`CNAME`

record`CNAME`

record to your domain's DNS configuration. - Click the
**Verify**button.

When you click **Verify**, Google will check for the `CNAME`

record and if
everything works you will be added as a verified owner of the domain. Using this method
automatically verifies you as the owner of all websites on this domain. For example, when you
verify your ownership of example.com, you are automatically verified as an owner of
www.example.com as well as subdomains such as blog.example.com.

Sometimes DNS records take a while to make their way across the Internet. If we don't find the record immediately, we'll check for it periodically and when we find the record we'll make you a verified owner. To maintain your verification status don't remove the record, even after verification succeeds.

If you don't have access to your DNS configuration at your domain name provider you can continue
to use any of the other verification methods, such as the
[HTML file](https://support.google.com/webmasters/bin/answer.py?answer=35658), the
[ meta tag](https://support.google.com/webmasters/bin/answer.py?answer=35659) or

[Google Analytics tag](https://support.google.com/webmasters/bin/answer.py?answer=185871)in order to verify that you own a site.

If you have any questions please let us know via our
[Webmaster Help forum](https://support.google.com/webmasters/threads?hl=en&thread_filter=(category:search_console)).
