---
title: "Yahoo Mail Fixes Security Flaw, Was Open to Account HiJacking"
source_url: https://www.searchenginejournal.com/yahoo-mail-fixes-security-flaw-was-open-to-account-hijacking/476/
category: search-engine-journal
section: "Search Engine Journal — SEO/GEO news + guides"
date: 2004-04-22
---

# Yahoo Mail Fixes Security Flaw, Was Open to Account HiJacking

Yahoo Mail was open to hacker attacks due to a file size bug. ZDNet reports that a flaw in the Yahoo Mail system could have let attackers control victims’ Yahoo accounts

Yahoo has fixed a bug in its Yahoo Mail email system that would have allowed attackers to seize control of users’ email accounts. This bug enabled attackers to take control of a user’s account by simply sending them a specially crafted email.

The security flaw, according to eEye Digital Security’s Drew Copley:

Allowed attackers to by-pass the Web-mail system’s Javascript filters. Any message exceeding approximately 100kb in length would not be analysed by the filter, which is meant to strip messages of any potentially malicious Javascript.

“A remarkable note about this bug is that no one seems to have found it before,” Copley’s advisory reads. “As far as anyone knows.”


Technical Description:

———–EXAMPLE EMAIL———

SCRIPT

[->a bunch of chars here [spaces are most stealth], the whole file size will be just about 100KB]

[this causes the filter to not work… the code is then run automatically]

———————————

The pseudo-diagram above explains the scenario rather well. For whatever reason, Yahoo’s email filter simply does not work on files which exceed a certain range. This kind of software issue is relatively common. A remarkable note about this bug is that no one seems to have found it before.

Yahoo has fixed the Yahoo Mail bug.

[SEO](https://www.searchenginejournal.com/category/seo/)
