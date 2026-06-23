---
title: "New in structured data: FAQ and How-to | Google Search Central Blog | Google for Developers"
source_url: https://developers.google.com/search/blog/2019/05/new-in-structured-data-faq-and-how-to
category: google-search-central
section: "Google Search Central — official technical SEO + structured data docs"
date: 2019-05-08
---

# New in structured data: FAQ and How-to | Google Search Central Blog | Google for Developers

Wednesday, May 08, 2019

Over the last few weeks, we've been discussing structured data: first providing
[best practices](/search/blog/2019/04/enriching-search-results-structured-data)
and then showing how to
[monitor it with Search Console](/search/blog/2019/05/monitoring-structured-data-with-search-console).
Today we are announcing support for FAQ and How-to structured data on Google Search and the
Google Assistant, including new reports in Search Console to monitor how your site is performing.

In this post, we provide details to help you implement structured data on your FAQ and how-to pages in order to make your pages eligible to feature on Google Search as rich results and How-to Actions for the Assistant. We also show examples of how to monitor your search appearance with new Search Console enhancement reports.

## How-to on Search and the Google Assistant

How-to rich results provide users with richer previews of web results that guide users through step-by-step tasks. For example, if you provide information on how to tile a kitchen backsplash, tie a tie, or build a treehouse, you can add How-to structured data to your pages to enable the page to appear as a rich result on Search and a How-to Action for the Assistant.

Add structured data to the steps, tools, duration, and other properties to enable a How-to rich
result for your content on the search page. If your page uses images or video for each step,
make sure to mark up your visual content to enhance the preview and expose a more visual
representation of your content to users. Learn more about the required and recommended
properties you can use on your markup in the
[How-to developer documentation](/search/docs/appearance/structured-data/how-to).

Your content can also start surfacing on the Assistant through new voice guided experiences. This feature lets you expand your content to new surfaces, to help users complete tasks wherever they are, and interactively progress through the steps using voice commands.

As shown in the Google Home Hub example below, the Assistant provides a conversational, hands-free
experience that can help users complete a task. This is an incredibly lightweight way for web
developers to expand their content to the Assistant. For more information about How-to for the
Assistant, visit
[Build a How-to Guide Action with Markup](/actions/content-actions/how-to).

To help you monitor How-to markup issues, we launched a
[report in Search Console](https://support.google.com/webmasters/answer/7552505)
that shows all errors, warnings and valid items for pages with HowTo structured data. Learn more about how to use the report to
[monitor your results](/search/blog/2019/05/monitoring-structured-data-with-search-console).

## FAQ on Search and the Google Assistant

An FAQ page provides a list of frequently asked questions and answers on a particular topic. For
example, an FAQ page on an e-commerce website might provide answers on shipping destinations,
purchase options, return policies, and refund processes. By using
`FAQPage`

structured data, you
can make your content eligible to display these questions and answers to display directly on
Google Search and the Assistant, helping users to quickly find answers to frequently asked
questions.

FAQ structured data is only for official questions and answers; don't add FAQ structured data on
forums or other pages where users can submit answers to questions - in that case, use the
[Q&A Page markup](/search/docs/appearance/structured-data/qapage).

You can learn more about implementation details in the
[FAQ developer documentation](/search/docs/appearance/structured-data/faqpage).

To provide more ways for users to access your content, FAQ answers can also be surfaced on the
Google Assistant. Your users can invoke your FAQ content by asking direct questions and get the
answers that you marked up in your FAQ pages. For more information, visit
[Build an FAQ Action with Markup](/actions/content-actions/faq).

To help you monitor FAQ issues and search appearance, we also launched an
[FAQ report in Search Console](https://support.google.com/webmasters/answer/7552505)
that shows all errors, warnings and valid items related to your marked-up FAQ pages.

We would love to hear your thoughts on how FAQ or How-to structured data works for you. Send us
any feedback either through
[Twitter](https://twitter.com/googlesearchc) or
[our forum](https://support.google.com/webmasters/threads?thread_filter=(category:structured_data)).
