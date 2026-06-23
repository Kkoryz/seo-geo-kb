---
title: "Page explorer"
source_url: https://ahrefs.com/academy/how-to-use-ahrefs/site-audit/page-explorer
category: ahrefs-academy
section: "Ahrefs Academy — SEO courses"
date: 2026-06-03
---

# Page explorer

Add a top 1% marketer to your team

Module 7

Page Explorer shows you all the raw data collected during the crawl.

Use any of the preset filters to slice and dice through it as you see fit. Or create your own advanced filters by mixing and matching 250+ available data points.

Below are some actionable ways to use this report.

Let’s say you’ve acquired a new Amazon affiliate website where the previous site owner had hardcoded all of the affiliate links. Your goal is to find these links so you can change them to yours.

Click on the Advanced filter. Change the rule to Is valid (200) internal HTML page and leave the condition as Yes.

Next, create a group. Change the rule to External outlinks and set the criteria to contains with a value of “amazon.com”. Since Amazon also uses a shortened domain—amzn.to—create the same rule and set the criteria to contains with the value of amzn.to.

Change the operator from AND to OR.

Click Apply and you’ll see all the URLs matching these rules.

If you’re running regular or scheduled audits of your website, you can compare changes over time based on either pages or a particular issue.

To compare pages, scroll down to the data table and toggle Show changes under the Changes button.

You’ll be able to see the changes that have occurred since the last crawl. For convenience, filter your results by new, lost, or no change from the All filter results dropdown to.

To compare individual issues, you can also filter crawl results based on numerical, boolean, or text changes in fields. This opens up a few use cases.

See which content pages experience a decrease in traffic (also known as content decay) beyond a certain threshold.

Let’s take Ahrefs’ blog and check for articles that lost at least 10% of their organic traffic. Click on Advanced filter. Then change the rule to Organic traffic with the operator Dropped by at least (%) set to 10%.

From here, we can prioritize the 35 potential articles by sorting them after the absolute traffic numbers under the Changes column.

Pages with a [noindex tag](https://ahrefs.com/seo/glossary/noindex-tag) prevent search engines from discovering them. In the long term, such pages will not pass any link equity to other pages.

To check for pages that became non-indexable, click on Advanced filter. Change the rule to Is indexable page with the value Changed to No.

Remove the noindex tag if not placed on purpose.

Google rewrites meta descriptions in [62.78% cases](https://ahrefs.com/blog/meta-description-study/).

To check if Google isn’t displaying the original meta description, click on Advanced filter. Change the rule to Meta description set to Changed.

Pinpoint SEO issues with accuracy.

Our SiteAuditBot crawls and stores historical HTML & text snapshots of each page, so you can compare raw vs. rendered code and changes in the text copy of a page.

Let’s take our recently updated [About us](https://ahrefs.com/about) page. To check the changes in HTML code:

Open the View source tab under the URL details panel of a page

Select Rendered HTML

Select a date under the historical crawl dropdown


The code that was deleted is highlighted in red, while text that was added is highlighted in green.

NOTE

If you don’t want Ahrefs SiteAuditBot to store a snapshot of your page, you can add the noarchive tag in your robots.txt file.

Investigate hreflang issues with ease.

Open the URL details panel of a page and click on the Hreflangs tab to see the whole hreflang cluster of a page.

Errors with pages and links are highlighted in red, which lets you quickly spot which link is missing or was added by mistake.

KEEP LEARNING

Read some of the articles on the [Ahrefs blog](https://ahrefs.com/blog/):

About this course## How to Use Ahrefs

Learn practical ways to use Ahrefs' SEO tools and reports to improve SEO.

62 lessons

3h 18m

How to analyze yours and your competitors’ websites with Site Explorer

How to increase your AI visibility in LLMs with Brand Radar

How to master keyword research with Keywords Explorer

How to improve your on-page and technical SEO with Site Audit

How to track and improve your Google rankings with Rank Tracker

How to find untapped keyword and link building opportunities with Content Explorer
