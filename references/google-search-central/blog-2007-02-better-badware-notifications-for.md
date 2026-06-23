---
title: "Better badware notifications for site owners | Google Search Central Blog | Google for Developers"
source_url: https://developers.google.com/search/blog/2007/02/better-badware-notifications-for
category: google-search-central
section: "Google Search Central — official technical SEO + structured data docs"
date: 2007-02-26
---

# Better badware notifications for site owners | Google Search Central Blog | Google for Developers

Monday, February 26, 2007

In the fight against badware, protecting Google users by showing warnings before they visit
dangerous sites is only a small piece of the puzzle. It's even more important to help site owners
protect their own users, and we've been working on this with
[StopBadware.org](https://www.stopbadware.org/).
A few months ago we took the first step and integrated malware notifications into
[Webmaster Tools](/search/blog/2006/11/badware-alerts-for-your-sites). I'm pleased to
announce that we are now including more detailed information in these notifications, and are also
sending them to site owners via email.

## Webmaster Tools notifications

Now instead of simply informing site owners that their sites have been flagged and suggesting next steps, we're also showing example URLs that we've determined to be dangerous. This can be helpful when the malicious content is hard to find. For example, a common occurrence with compromised sites is the insertion of a 1-pixel iframe causing the automatic download of badware from another site. By providing example URLs, site owners are one step closer to diagnosing the problem and ultimately re-securing their sites.

## Email notifications

In addition to notifying Webmaster Tools users, we've also begun sending email notifications to some of the owners of sites that we flag for badware. We don't have a perfect process for determining a site owner's email address, so for now we're sending the notifications to likely site owner aliases for the domain in question (for example, webmaster@, admin@, etc). We considered using whois records, but these often contain contact information for the hosting provider or registrar, and you can guess what might happen if a web host learned that one of its client sites was distributing badware. We're planning to allow site owners to provide a preferred email address for notifications through Webmaster Tools, so look for this change in the future.
