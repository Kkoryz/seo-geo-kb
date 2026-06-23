---
title: "How to Find Your Website’s Keywords in Google Analytics 4"
source_url: https://www.semrush.com/blog/google-analytics-keywords/
category: semrush-blog
section: "Semrush blog — SEO/GEO methodology"
date: 2024-03-13
---

# How to Find Your Website’s Keywords in Google Analytics 4

Keywords are the terms you use on your website to appear in search results for queries your audience is searching.

And using Google Analytics’ keyword reports shows you which terms drive the most users to your site, reveals traffic decreases that need to be addressed, and helps you understand the terms people use to talk about your product or service.

By the end of this article, you’ll know how to find your website’s keywords in Google Analytics 4 (GA4). And how to use relevant information about those terms to improve your site.

## Can You See Keyword Rankings in Google Analytics 4?

No, you can’t see keyword-related data in GA4 by default.

The previous version of Google Analytics showed keyword information. But it’s been removed to protect user privacy better.

**However, you can see some information about organic keywords if you connect your Google Search Console (GSC) account to GA4.**

Once you do, you’ll be able to see GSC data on impressions, clicks, average position, and click-through rate (CTR) directly in GA4.

However, most marketers still prefer to go to the source to get this data.

In a recent poll we ran for this article, we asked marketers which tool they prefer: **GSC** or the **GSC report in GA4**?

Out of 36 respondents, 86% said they use GSC directly. And only 14% said they use the GA4 option.

This is obviously a small sample size, but it does at least suggest that marketers currently underuse the GSC integration. Even though it makes performance reporting and analysis more convenient by unifying their data.

## How to See Organic Keyword Data in GA4 (via Google Search Console)

Just follow these steps to connect GSC to your existing GA4 account:

### 1. Verify Your Site in Google Search Console

[Log in to GSC](https://search.google.com/search-console) with the same Google email you use for GA4 if you’ve already set up your account.

If you don’t have an account yet, sign up.

Then, GSC will prompt you to add your property (website).

You can choose between two property types:

**Domain**: Collects data for all URLs on your domain and requires verification through your domain name system (DNS) provider**URL prefix**: Collects data only for URLs under a specific website section. You can verify your property through the GA4 tracking tag on your website.

Once you choose a property type, follow the instructions in our [GSC setup guide](https://www.semrush.com/blog/google-search-console/#how-to-set-up-google-search-console) to complete the process.

### 2. Connect Google Analytics and Google Search Console

To connect GSC and GA4, log in to your GA4 account and click “**Admin**” > “**Search Console links**.” (This appears under the “Product links” section.)

Go to “**Link**” to start the process.

Choose the property you want to connect to GA4 by clicking on “**Choose accounts**.”

Select the correct property and click “**Confirm**.”

Select “**Next**.”

Under “Select Web Stream,” choose a provided data stream and click “**Next**.”

The last step is to review your choices and click “**Submit**.”

Your GSC property is now connected to GA4.

### 3. Enable the Search Console Reports

GA4 won’t display GSC query data by default, so you need to enable the corresponding reports.

Go to “**Reports**” and click “**Library**” in the bottom-left corner. Then, find the “Search Console” report, click the three dots, and select “**Publish**.”

After completing this step, you should be able to see “Search Console” in the GA4 reports menu.

### 4. Access Keyword Data

Wait 48 hours for data to be available, then click “**Queries**” to view the keywords driving people to your site, along with data on:

**Clicks**: The number of clicks you get for a specific query**Impressions**: The number of times users saw your results for a given query**Click-through rate (CTR)**: The percentage of impressions that led to clicks**Average position**: The average ranking you have for a specific keyword

Note that historical GSC data is available [only for the past 16 months](https://support.google.com/analytics/answer/13682862).

## 3 Tips for Using GA4 Keyword Data to Optimize Your Website

Knowing which keywords lead users to your site is great. But it’s even better to use that data to grow your traffic.

Here are some practical tips for using GA4 keyword data to boost your search presence:

### Create Topic Clusters

A [topic or content cluster](https://www.semrush.com/blog/topic-clusters/) is a group of pages on your website that cover a similar theme. A cluster consists of a pillar (main) page and multiple cluster pages (subpages).

For example, you could have “indoor plants” as a pillar page. And “best indoor plants for beginners,” “indoor plants for air purification,” and “indoor plants for children” as cluster pages.

Google keyword analysis can help you create clusters by revealing which queries you rank well for. And you can use that information for further keyword research.

When you focus on keywords you’re already successfully ranking for, you continue building [topical authority](https://www.semrush.com/blog/topical-authority/) that expands your search presence.

To find your top-performing keywords, sort the Google Analytics organic keywords report by clicks:

Go through the list and look for patterns.

Let’s say you have a bicycle shop site that gets many visits from purchase-related queries. Such as “best mountain bikes” and “best bikes for beginners.”

That means creating additional content on bicycle buying guides would likely be great for SEO.

You can use Semrush [Keyword Magic Tool](https://www.semrush.com/analytics/keywordmagic/) to find numerous keywords you can use for your topic cluster strategy.

To start, type in a seed keyword such as “best bikes.” And click “**Search**.”

Select “**Broad Match**” to see options that are a variation of your seed keyword.

Select the “**KD %**” drop-down and enter a custom range of 0 to 49. This applies a [keyword difficulty](https://www.semrush.com/blog/keyword-difficulty/) filter that focuses only on terms you can feasibly rank for.

Check the box to the left of every suitable keyword. We recommend selecting a minimum of 50 keywords to ensure you have enough ideas.

When you’re done, click “**Send keywords**” > “**Keyword Strategy Builder**” > “**Apply**.” You can add them to a pre-existing list or create a new one.

Now, you need to group these keywords.

To do so, open the [Keyword Strategy Builder](https://www.semrush.com/analytics/keywordmanager/). Scroll down and open your keyword list.

On the next screen, click “**Cluster this list**.” The process can take up to 15 minutes—you’ll get an email notification when it’s done.

The report will show a list of pages that you can use as cluster pages. Your seed keyword (“best bikes,” in this case) will serve as the main term for your pillar page.

Then, it’s just a matter of deciding which pages you want to publish on your site.

### Find Content Refresh Opportunities

Keyword performance data helps you find pages that used to perform well but don’t anymore. [Updating these pages](https://www.semrush.com/blog/when-to-update-blog-content/) to make them more relevant to searchers can improve their performance.

To find refresh opportunities, go to the “**Queries**” report.

Click the date in the top-right corner, turn on the “**Compare**” feature, and select “Last 90 days”—this gives you enough data to work with.

Click “**Apply**.”

The table now displays how much the performance for each metric changed over the selected period.

Identify queries where you lost the most clicks.

Enter each of those queries in Google and analyze the top-ranking content to see where your page falls short. And brainstorm ways to make your content more helpful than the top-ranking pages.

### Optimize Underperforming Pages

Underperforming pages that get many impressions but comparatively few clicks likely need to be more attention-grabbing to capture users’ attention.

To find these pages, go to GA4 and click “**Search Console**” > “**Google organic search traffic**.” Look at the impressions column and find pages with high impressions but low CTR.

Optimize these pages to better stand out by adjusting their [title tags](https://www.semrush.com/blog/title-tag/) (HTML that specifies the page title and may show in search results) and [meta descriptions](https://www.semrush.com/blog/meta-description/) (HTML that provides a page summary and may show in search results).

The best place to start is by Googling the query a page ranks for. And analyzing the title tags of the top-ranking pages. Try to emulate (but not copy) them and keep them to between 50 and 60 characters.

Just make sure the title accurately represents the page’s content. For example, an article titled “How to Sew a Button (with Photos)” needs to include photos to avoid misleading searchers.

Your meta description should provide a brief and accurate summary of the page that’s around 105 characters.

Both the title tag and description should include the [primary keyword](https://www.semrush.com/blog/primary-keywords/) whenever possible.

## How to Get More Detailed Keyword Data

The GSC report in GA4 is great for basic keyword research and performance analysis.

But it doesn’t notify you when your rankings change. And it doesn’t let you track performance for a specific group of keywords.

Use Semrush’s [Position Tracking](https://www.semrush.com/position-tracking/) tool to monitor your rankings.

To set it up, enter your domain and click “**Set up tracking**.”

Add the keywords you want to track in this project.

Note that Position Tracking can import keywords directly from GSC. Just click the “**Import from …**” button, select “**Google Search Console**,” and confirm which keywords to add.

When you’re done adding keywords, click “**Add keywords to campaign**” and then “**Start Tracking**.”

The “**Landscape**” report shows a brief summary of changes over your chosen period. And information on your overall visibility, an estimate of your site's organic traffic, and the average position you rank in for your chosen terms.

The “**Overview**” tab lets you add your competitors’ domains to see how they compare to you.

Scroll down to the table to see your and your competitors’ specific rankings. And how those rankings are changing.

Use this information to proactively adjust your SEO strategy. To remain competitive.

## Centralize Your Organic Search Performance Data

Whether you’re working in-house or at an agency, integrating GSC with GA4 will give you a clearer overview of your organic search performance. Plus, you’ll save time switching between tools.

Take it a step further by using Semrush’s Position Tracking tool. So you can immediately spot changes.

Get started with Position Tracking and many more SEO tools with a free trial.
