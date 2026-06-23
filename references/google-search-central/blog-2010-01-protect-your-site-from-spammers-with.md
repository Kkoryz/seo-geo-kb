---
title: "Protect your site from spammers with reCAPTCHA | Google Search Central Blog | Google for Developers"
source_url: https://developers.google.com/search/blog/2010/01/protect-your-site-from-spammers-with
category: google-search-central
section: "Google Search Central — official technical SEO + structured data docs"
date: 2010-01-26
---

# Protect your site from spammers with reCAPTCHA | Google Search Central Blog | Google for Developers

Tuesday, January 26, 2010

If you allow users to publish content on your website, from
[leaving comments](/search/blog/2008/09/keeping-comment-spam-off-your-site-and) to
[creating user profiles](/search/blog/2009/06/spam20-fake-user-accounts-and-spam),
you'll likely see spammers attempt to take advantage of these mechanisms to generate traffic to
their own sites. Having this spammy content on your site isn't fun for anyone. Users may be
subjected to annoying advertisements directing them to low-quality or dangerous sites containing
scams or malware. And you as a webmaster may be hosting content that violates a search engine's
[quality guidelines](/search/docs/essentials#3),
which can harm your site's standing in search results.

There are ways to handle this abuse, such as moderating comments and reviewing new user accounts, but there is often so much spam created that it can become impossible to keep up with. Spam can easily get to this unmanageable level because most spam isn't created manually by a human spammer. Instead, spammers use computer programs called "bots" to automatically fill out web forms to create spam, and these bots can generate spam much faster than a human can review it.

To level the playing field, you can take steps to make sure that only humans can interact with potentially spammable features of your website. One way to determine which of your visitors are human is by using a CAPTCHA , which stands for "completely automated public Turing test to tell computers and humans apart." A typical CAPTCHA contains an image of distorted letters which humans can read, but are not easily understood by computers. Here's an example:

You can easily take advantage of this technology on your own site by using
[reCAPTCHA](https://www.google.com/recaptcha/about/), a service
owned by Google. One unique aspect of reCAPTCHA is that data collected from the service is used to
improve the process of scanning text, such as from books or newspapers. By using reCAPTCHA, you're
not only protecting your site from spammers; you're helping to digitize the world's books.

Luis Von Ahn, one reCAPTCHA's co-founders, gives more details about how the service works in the video below:

If you'd like to implement reCAPTCHA on your own site, you can
[sign up](https://admin.recaptcha.net/accounts/signup/?next=/recaptcha/createsite/).
[Plugins are available](https://recaptcha.net/resources)
for easy installation on popular applications and programming environments such as WordPress and
PHP.
