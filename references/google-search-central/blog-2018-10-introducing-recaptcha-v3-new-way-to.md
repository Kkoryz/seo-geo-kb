---
title: "Introducing reCAPTCHA v3: the new way to stop bots | Google Search Central Blog | Google for Developers"
source_url: https://developers.google.com/search/blog/2018/10/introducing-recaptcha-v3-new-way-to
category: google-search-central
section: "Google Search Central — official technical SEO + structured data docs"
date: 2018-10-29
---

# Introducing reCAPTCHA v3: the new way to stop bots | Google Search Central Blog | Google for Developers

Monday, October 29, 2018

Today, we're excited to introduce reCAPTCHA v3, our newest API that helps you detect abusive
traffic on your website without user interaction. Instead of showing a CAPTCHA challenge,
[reCAPTCHA v3](/recaptcha/docs/v3)
returns a score so you can choose the most appropriate action for your website.

## A Frictionless User Experience

Over the last decade, reCAPTCHA has continuously evolved its technology. In reCAPTCHA v1, every user was asked to pass a challenge by reading distorted text and typing into a box. To improve both user experience and security, we introduced reCAPTCHA v2 and began to use many other signals to determine whether a request came from a human or bot. This enabled reCAPTCHA challenges to move from a dominant to a secondary role in detecting abuse, letting about half of users pass with a single click. Now with reCAPTCHA v3, we are fundamentally changing how sites can test for human vs. bot activities by returning a score to tell you how suspicious an interaction is and eliminating the need to interrupt users with challenges at all. reCAPTCHA v3 runs adaptive risk analysis in the background to alert you of suspicious traffic while letting your human users enjoy a frictionless experience on your site.

## More Accurate Bot Detection with "Actions"

In reCAPTCHA v3, we are introducing a new concept called "Action"—a tag that you can use to define the key steps of your user journey and enable reCAPTCHA to run its risk analysis in context. Since reCAPTCHA v3 doesn't interrupt users, we recommend adding reCAPTCHA v3 to multiple pages. In this way, the reCAPTCHA adaptive risk analysis engine can identify the pattern of attackers more accurately by looking at the activities across different pages on your website. In the reCAPTCHA admin console, you can get a full overview of reCAPTCHA score distribution and a breakdown for the stats of the top 10 actions on your site, to help you identify which exact pages are being targeted by bots and how suspicious the traffic was on those pages.

## Fighting Bots Your Way

Another big benefit that you'll get from reCAPTCHA v3 is the flexibility to prevent spam and abuse in the way that best fits your website. Previously, the reCAPTCHA system mostly decided when and what CAPTCHAs to serve to users, leaving you with limited influence over your website's user experience. Now, reCAPTCHA v3 will provide you with a score that tells you how suspicious an interaction is. There are three potential ways you can use the score. First, you can set a threshold that determines when a user is let through or when further verification needs to be done, for example, using two-factor authentication and phone verification. Second, you can combine the score with your own signals that reCAPTCHA can't access—such as user profiles or transaction histories. Third, you can use the reCAPTCHA score as one of the signals to train your machine learning model to fight abuse. By providing you with these new ways to customize the actions that occur for different types of traffic, this new version lets you protect your site against bots and improve your user experience based on your website's specific needs.

In short, reCAPTCHA v3 helps to protect your sites without user friction and gives you more power to decide what to do in risky situations. As always, we are working every day to stay ahead of attackers and keep the Internet easy and safe to use (except for bots).

Ready to get started with reCAPTCHA v3? Visit our
[developer site](/recaptcha/docs/v3)
for more details.
