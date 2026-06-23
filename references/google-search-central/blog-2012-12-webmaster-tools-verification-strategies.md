---
title: "Webmaster Tools verification strategies | Google Search Central Blog | Google for Developers"
source_url: https://developers.google.com/search/blog/2012/12/webmaster-tools-verification-strategies
category: google-search-central
section: "Google Search Central — official technical SEO + structured data docs"
date: 2012-12-17
---

# Webmaster Tools verification strategies | Google Search Central Blog | Google for Developers

Monday, December 17, 2012

[Verifying ownership](https://support.google.com/webmasters/answer/9008080)
of your website is the first step towards using
[Google Webmaster Tools](https://search.google.com/search-console). To
help you keep verification simple and reduce its maintenance to a minimum, especially when you
have multiple people using Webmaster Tools, we've put together a small list of tips and tricks
that we'd like to share with you:

- The method that you choose for verification is up to you, and may depend on your CMS and hosting providers. If you want to be sure that changes on your side don't result in an accidental loss of the verification status, you may even want to consider using two methods in parallel.
-
Back in 2009, we
[updated the format of the verification](/search/blog/2009/10/changes-to-website-verification-in). If you're still using the old format, we recommend moving to the newer version. The newer`meta`

tag and fileis called`meta`

tag`google-site-verification`

, and the newer file format contains just one line with the file name. While we're currently supporting ye olde format, using the newer one ensures that you're good to go in the future. -
When removing users' access in Webmaster Tools, remember to remove any active associated
verification tokens (for example, a file or a
`meta`

tag). Leaving them on your server means that these users would be able to gain access again at any time. You can view the site owners list in Webmaster Tools under Configuration / Users. -
If multiple people need to access the site, we recommend using the
[add users](https://support.google.com/webmasters/answer/7687615)functionality in Webmaster Tools. This makes it easier for you to maintain the access control list without having to modify files or settings on your servers. - Also, if multiple people from your organization need to use Webmaster Tools, it can be a good policy to only allow users with email addresses from your domain. By doing that, you can verify at a glance that only users from your company have access. Additionally, when employees leave, access to Webmaster Tools is automatically taken care of when that account is disabled.
-
Consider using
[restricted](https://support.google.com/webmasters/answer/7687615)(read-only) access where possible. Settings generally don't need to be changed on a daily basis, and when they do need to be changed, it can be easier to document them if they have to go through a central account.

We hope these tips help you to simplify the situation around verification of your website in
Webmaster Tools. For more questions about verification, you can drop by our
[Webmaster Help Forums](https://support.google.com/webmasters/community).
