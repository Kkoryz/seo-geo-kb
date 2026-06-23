---
title: "Full Technical SEO Checklist (from Start to Finish)"
source_url: https://www.semrush.com/blog/technical-seo-checklist/
category: semrush-blog
section: "Semrush blog — SEO/GEO methodology"
date: 2024-09-18
---

# Full Technical SEO Checklist (from Start to Finish)

Technical SEO is mainly about making sure search engines can find, understand, and properly index (save) your site, but it goes beyond that. Technical SEO also involves creating a seamless user experience for your visitors.

Technical SEO is the foundation on which your SEO success relies. Because many of these activities need to occur before your other SEO tactics have a chance of driving results.

When approaching technical SEO for any website, following a structured process is helpful. That’s why we’ve put together this SEO’s technical checklist.

While creating this checklist, we also analyzed over 50,000 domains to see how common some of these issues are. We'll share specific data points from our research as we go.

Now, let’s look at the checklist items, one by one.

## 1. Look for Crawling and Indexing Issues

Make sure search engines like Google are able to discover (crawl) and save (index) your site properly to ensure your pages can rank in search results.

### Check Whether Your Site Is Indexed

This is the absolute first thing you need to do because your site won’t show in search results if it isn’t indexed.

The best way to check your indexing status is through Google Search Console (GSC).

In [GSC](https://search.google.com/search-console/about), head to the "**Pages**" report. This will show you exactly which pages are indexed and which are excluded.

The pages that aren’t indexed will be grouped by the specific reason.

Here are a few reasons you might see:

**Crawled - currently not indexed**: Google actually looked at these pages but decided they weren't worth indexing. This usually means the content is low quality or the pages are too similar to existing pages.**Blocked by**: Your robots.txt file is telling Google not to crawl these pages. Double-check your robots.txt file to make sure you're not accidentally blocking important content.**robots.txt****Excluded by**: You might have accidentally added noindex tags to your pages. This explicitly tells Google, "Don't put these pages in search results." Remove this tag from important pages you want to be indexed.**‘noindex’ tag**

Fix these issues, then use the "**Validate Fix**" button that corresponds to a given issue to ask Google to recrawl your pages.

### Check for Any Duplicates of Your Website

Having duplicate versions of your site can harm your SEO efforts because search engines view these as separate websites, even though they display the same content. Because they’re all **technically** different versions.

How often do sites run into this issue?

In our study of over 50,000 domains, we found that 27% of websites had both HTTP and HTTPS versions accessible at the same time. Which means this issue is quite common on the web.

For example, your website might be accessible at:

- https://yourdomain.com
- https://www.yourdomain.com
- http://yourdomain.com
- http://www.yourdomain.com

Check if your site is accessible through multiple URLs by entering each variation in your browser.

If multiple versions load, you need to pick one preferred version and redirect all others to it.

Use the HTTPS version as your primary URL (either with or without www—that's your preference). Then implement a [301 permanent redirect](https://www.semrush.com/blog/301-redirects/), so users and search engines are forwarded to your preferred version.

### Make Sure Your Robots.txt File Is Accurately Set Up

An incorrectly configured [robots.txt](https://www.semrush.com/blog/beginners-guide-robots-txt/) file can block important pages from being crawled, so review your robots.txt file to make sure it’s properly configured.

From our dataset, only 2% of websites had robots.txt configuration issues. That’s not a lot of websites, but the consequences can be severe if you happen to have this issue.

A robots.txt file is a plain text file that tells search engine crawlers which parts of your site they’re allowed to access—and which parts to avoid.

The file contains lines that can look like this:

`User-agent: *`

Disallow: /admin/

Disallow: /login/

Allow: /

Your robots.txt file will be located at “yourdomain.com/robots.txt.” Check the "Disallow" directives specifically to make sure you’re not blocking important folders or pages.

### Fix Redirect Chains & Loops

Redirect chains and loops hurt your SEO because they slow things down for users, waste [crawl budget](https://www.semrush.com/blog/crawl-budget/) (search engine resources used to crawl your site), and make it harder for search engines to pass full ranking power to your pages.

So, you should check for and fix these redirect issues to keep your site running smoothly.

A redirect chain occurs when a URL redirects to another URL and then to another, instead of directly reaching the final destination.

A loop happens when a URL redirects to a URL that redirects back to the original, creating an infinite loop.

Both of these issues occur due to ongoing changes to your website, such as when you restructure URLs and don’t carefully manage redirects during the process.

How common is this problem?

About 12% of websites in our study had redirect chains or loops affecting their performance.

Use Semrush [Site Audit](https://www.semrush.com/siteaudit/) tool to find redirect-related issues on your site.

[Set up a project](https://www.semrush.com/kb/539-configuring-site-audit) in the tool to run a full audit. (It only takes a few minutes for most sites.)

Then, go to the "**Issues**" tab and search for "redirect" in the search bar to see any redirect chains or loops.

And the specific URLs involved:

Fixing these issues is simple:

**For chains**, update any links or redirects to point directly to the final destination URL**For loops**, make sure URLs don’t redirect back to themselves

### Fix Broken Links

Broken internal links direct users to webpages that no longer exist, leading to 404 error pages when they’re clicked. This results in a poor user experience and can signal to search engines that your site isn't well-maintained.

Broken links can be either internal links to your own content or external links pointing to other websites.

In our analysis of over 50,000 domains, we discovered that 52% of websites had broken internal/external links that needed fixing.

The [Site Audit](https://www.semrush.com/siteaudit/) tool can help you easily spot if this issue exists for your site. Go to the “**Issues**” tab and search for “broken.”

You’ll see errors if broken links are present.

If you click on the detected items, you’ll see the affected pages:

Once you've identified broken links, you have different options depending on the type:

**For broken internal links**:

- Restore the deleted page if possible
- Set up a 301 redirect to send users to a similar relevant page

**For broken external links**:

- Replace the link with an updated version of the page if it exists elsewhere
- Remove the link entirely if no suitable replacement exists
- Find an alternative resource that provides similar information and link to it instead

It’s a good idea to schedule a broken link check every week. It's surprising how quickly these can pile up, especially on larger sites.

You can set up automated crawls with Site Audit.

### Fix Server Errors

Server errors (5xx errors) are problematic because they prevent search engines from crawling and indexing your content.

A server error indicates that there is something wrong with the server itself. Our technical SEO study revealed that about 10% of websites experience some sort of server error on a regular basis.

One of the most common server errors is the 500 Internal Server Error, which is essentially your server's way of saying, "Something went wrong, but I'm not sure what."

Other server errors include:

**502 Bad Gateway**: This occurs when your server tries to communicate with another server to fulfill a request, but receives an invalid response**503 Service Unavailable**: This typically occurs when the server is overloaded with requests or is currently under maintenance**504 Gateway Timeout**: This happens when the server doesn’t respond in time

You can check for server errors on your own by searching for “5xx” errors in [Site Audit](https://www.semrush.com/siteaudit/).

If you see any errors, click on the link to see the problematic pages and the specific error codes they’re returning. This information will be crucial for troubleshooting.

Fixing server errors requires technical expertise. So work with your developer or hosting provider to resolve them.

## 2. Optimize for User Experience

Search engines tend to reward websites that prioritize a good user experience (UX). Plus, a good experience keeps visitors engaged and encourages them to explore your content.

Here are the main aspects to address:

### Make Sure Your Site Is Mobile-Friendly

Search engines primarily use the mobile version of your site for ranking and indexing, so you should make sure your website displays and functions properly on smartphones.

To check your site's mobile-friendliness, use the [Website Grader](https://website.grader.com/) tool. Just enter your domain and email address, and the tool will analyze whether your site is optimized for mobile.

The tool will show you exactly where your mobile experience falls short and what needs fixing. So you can work alongside your developer team to make the necessary changes.

### Improve Your Core Web Vitals

Improve your [Core Web Vitals](https://www.semrush.com/blog/core-web-vitals/). Google uses them as a ranking factor.

The Core Web Vitals are a set of three main metrics that evaluate your webpage’s overall user experience.

The actual metrics are:

**Largest Contentful Paint (LCP)**: Measures how quickly the main content of your page loads and becomes visible to users. Google wants this to happen within 2.5 seconds for a good user experience.**Interaction to Next Paint (INP)**: Measures how quickly your page responds visually after a user interacts with it (like clicking a button or tapping a link). Specifically, it tracks the time from when you click something to when you see the page update or change. This should happen in less than 200 milliseconds for a good experience.**Cumulative Layout Shift (CLS)**: Measures visual stability (i.e., how much elements jump around as the page loads). Google wants your CLS score under 0.1.

Not many websites are fully optimized for these metrics.

According to our study, 96% of websites had at least one page that failed the Core Web Vitals assessment test.

You can use Google Search Console to see your Core Web Vitals performance.

In [GSC](https://search.google.com/search-console/about), navigate to “**Core Web Vitals**” from the sidebar and click "**Open Report**” to see the data.

Then, look for pages marked as "Poor" or "Needs Improvement." These pages have failed the Core Web Vitals assessment test and need optimization.

Take those URLs and run them through Google’s [PageSpeed Insights](https://pagespeed.web.dev/) tool to get specific recommendations on how to fix the issues.

Like this:

Work with your developer to implement the suggested fixes.

### Avoid Intrusive Interstitials

Avoid intrusive interstitials because they create a poor user experience, especially on mobile devices with limited screen space.

Intrusive interstitials are pop-ups or overlays that cover a significant portion of your content, making it difficult for users to access the information they came for.

What exactly counts as an intrusive interstitial? Here are a few examples:

- Full screen pop-ups that cover the main content immediately after a user lands on your page
- Stand-alone interstitials that users must dismiss before accessing your content
- Layouts where the
[above-the-fold](https://www.semrush.com/blog/above-the-fold/)area is occupied by an ad, but the main content is actually underneath

Not all interstitials are problematic, though. Google makes exceptions for:

- Legal obligations like cookie notices or age verification dialogs
- Login dialogs on sites where content is behind a paywall
- Small banners that use a reasonable amount of screen space and can be easily dismissed
- Exit-intent pop-ups that appear when someone is about to leave
- Small pop-ups that appear after a user has been on the page for a while

## 3. Work On Your Website Navigation

Make sure your site has a fairly simple navigation system that will allow users to find important content easily and help search engines understand your site.

### Improve Your Website Structure

A well-structured website is crucial for search engines and users because it determines how efficiently search engines can crawl and understand your content and how easily visitors can navigate your site.

The ideal structure resembles a hierarchy that makes logical sense. Your homepage is at the top, followed by main category pages, then subcategories, and finally individual pages.

This creates clear paths for both users and search engines to follow.

Each page should be accessible within three or four clicks from your homepage. As you can see in the example above.

### Interlink Your Pages

[Internal linking](https://www.semrush.com/blog/internal-links/) creates pathways between different pages on your site, allowing search engine crawlers to discover your content while helping users find related information.

Look for opportunities to add contextual links within your content. When adding links, use descriptive [anchor text](https://www.semrush.com/blog/anchor-text/) rather than generic "click here" or "read more" phrases.

The text you use for the link lets users know where they’re about to go and helps Google understand what the linked page is about.

Some other effective internal linking tactics include:

- Linking from your navigation menu to your most important pages to give them extra authority
- Creating
[hub pages](https://www.semrush.com/blog/content-hub/)(main topic pages) that bring together and link to all your related content in one place - Adding "related posts" sections at the end of articles

Don't go overboard, though. Too many internal links on a page can look spammy.

### Use Breadcrumbs

[Breadcrumbs](https://www.semrush.com/blog/breadcrumbs-for-websites/) improve navigation and help both users and search engines better understand your site’s structure.

They appear at the top of a page and show the path to that page within your site. Users can click on them to easily go back to previous sections.

However, not all sites need to use breadcrumbs.

Breadcrumbs are only worth implementing if your site is relatively large with multiple layers of hierarchical content (like ecommerce stores).

### Fix Orphan Pages

Fix [orphan pages](https://www.semrush.com/blog/orphan-pages/) because they’re difficult for users and search engines to discover—they have no incoming internal links.

These pages tend to accumulate on larger sites pretty easily.

In our analysis of over 50,000 domains, we found that 69% of those websites had at least one orphan page. So, this issue is quite common.

You can check if your site has any orphan pages using Semrush [Site Audit](https://www.semrush.com/siteaudit/) tool. Go to the “**Issues**” tab and search for “orphan.”

Fix the issue by adding links to the orphan page from other relevant pages.

## 4. Meet Other Technical Requirements

There are many other general best practices that Google wants you to follow for your site.

### Use HTTPS

[Hypertext transfer protocol secure](https://www.semrush.com/blog/what-is-https/) (HTTPS) is the secure version of HTTP that encrypts the connection between the user's browser and your website. To protect sensitive information like login credentials, payment details, and other personal data.

Google has used HTTPS as a ranking signal since 2014, giving a slight SEO advantage to secure sites.

More importantly, modern browsers mark non-HTTPS sites as "Not Secure," which can erode user trust and increase [bounce rates](https://www.semrush.com/blog/bounce-rate/).

You can implement HTTPS on your site by acquiring a Secure Sockets Layer (SSL) certificate. Many web hosting services offer this when you sign up, often for free.

This is more of an advanced technical SEO task, so talk to your development team to get this implemented if it’s not already.

### Implement Hreflang for International Pages

[Hreflang tags](https://www.semrush.com/blog/hreflang-attribute-101/) are used for multilingual or multiregional sites to tell search engines which language and region each version of your page is intended for, ensuring users see the most relevant version in search results.

For example, if we search for the official Disney site in the U.S., we see the American English version:

If we do the same in Germany, we see German version of the page:

Implementing hreflang is simple. Just add the appropriate tags to the <head> section of each language/country-specific version of your page.

For example, if your website targets audiences in the United States, Germany, and Japan, add these hreflang tags to all three versions:

`<link rel="alternate" hreflang="x-default" href="https://yourwebsite.com" />`

<link rel="alternate" hreflang="en-us" href="https://yourwebsite.com" />

<link rel="alternate" hreflang="de-de" href="https://yourwebsite.com/de/" />

<link rel="alternate" hreflang="ja-jp" href="https://yourwebsite.com/jp/" />

The first tag indicates the default or fallback page that should be shown to users when no other variant is appropriate.

Other tags specify the different language or country versions available on your site, ensuring Google serves the right one based on a user's location and language settings.

### Add Schema Markup

[Schema markup](https://www.semrush.com/blog/schema-markup/) is a type of code that helps search engines understand the content on your pages more clearly.

While it's not a direct ranking factor, schema markup enables rich results (special listings on search results pages), which can improve click-through rates.

There are many types of schema markup, but you should focus on the most relevant ones for your specific content types. Which may include:

- Organization (for your homepage)
- Product (for ecommerce product pages)
- Article (for blog posts or news)
- Event (for event pages)
- Recipe (for food sites)
- Review (for product or service reviews)

The easiest way to generate schema is to use a [Schema Markup Generator](https://technicalseo.com/tools/schema-markup-generator/).

To get started:

- Select the type of markup you need
- Fill out the form you see on the left-hand side
- The tool will automatically generate the code for you

Once the code is generated, you can add it to the <head> section of your page’s HTML.

After implementation, use Google's [Rich Results Test](https://search.google.com/test/rich-results) tool to verify that your schema is implemented correctly.

## 5. Resolve Content-Specific Technical Issues

This section of our tech SEO checklist addresses how to resolve common content-specific technical issues that can affect your SEO performance.

### Address Duplicate Content

Address [duplicate content](https://www.semrush.com/blog/duplicate-content/) issues because they can hurt your site’s credibility and make it harder for Google to index and rank your content for relevant search terms.

Duplicate content is content that’s identical or highly similar to content that exists elsewhere on your website or on another website.

About 41% of websites had internal duplicate content issues, according to our analysis of over 50,000 domains.

Use [Site Audit](https://www.semrush.com/siteaudit/) to quickly find out if you have duplicate content on your own site.

Just search for “Duplicate” under the “Issues” tab.

Address duplicate content issues by:

- Adding
[canonical tags](https://www.semrush.com/blog/canonical-url-guide/)to identify the primary version of your content - Consolidating duplicate pages into a single, main page and setting up 301 redirects from the old URLs to the main one

### Fix Thin Content

Identify and improve [thin content](https://www.semrush.com/blog/thin-content/) because it can negatively impact your search engine rankings and user experience.

Thin content is a term search engines use to describe pages that offer little to no value to users.

To identify thin content on your site, look for pages that are:

- Poorly written and don’t deliver valuable information
- Copied from other sites
- Filled with ads or spammy links
- Auto-generated using AI or a programmatic method

Once you've identified thin content, take action to improve it:

First, remove or rewrite any directly copied content.

This is the most serious issue. Plagiarism isn't just an SEO problem—it's an ethical one, too.

For the content that’s thin but original, beef it up with meaningful insights, examples, or practical tips that actually help your audience.

For pages overwhelmed with ads, reduce promotions and focus on the user experience.

For auto-generated fluff, either rework it into something useful or get rid of it entirely.

### Ensure All Pages Have Metadata

Metadata helps search engines understand your content and match it to relevant search queries, and it's what users see in search results when deciding whether to click on your page.

So you should ensure all your pages have complete, optimized metadata to improve your search visibility and click-through rates.

Metadata includes elements like the title tag and [meta description](https://www.semrush.com/blog/meta-description/), which summarize the page’s content and purpose. And can be displayed in search results.

(Technically, the title tag isn’t a [meta tag](https://www.semrush.com/blog/meta-tag/) from an HTML perspective. But it’s important for your SEO and worth discussing alongside other metadata.)

Run a free [website audit](https://www.semrush.com/siteaudit/) for a quick meta tag review. To find missing meta descriptions or title tags across your entire site, use Semrush Site Audit tool.

Just filter your results for “Meta tags” from the “Issues” tab. Click the number next to an issue for a full list of pages with that problem.

Then, go through and fix each issue. To improve your visibility (and possibly your appearance) in search results.

From what we've seen, issues with meta tags are quite common across the web.

In our analysis of more than 50,000 websites, we discovered that a staggering 70% were missing meta descriptions, and 10% didn't even have a title tag on some of their pages.

## Put This Technical SEO Audit Checklist Into Action

Now that you know what technical SEO action items to prioritize, it’s time to execute.

Semrush [Site Audit](https://www.semrush.com/siteaudit/) tool helps you identify and fix all the technical issues quickly and efficiently.

Sign up for a free account to get started today.
