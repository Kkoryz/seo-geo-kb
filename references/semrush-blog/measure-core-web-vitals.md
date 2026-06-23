---
title: "Measure Core Web Vitals with Semrush Site Audit"
source_url: https://www.semrush.com/blog/measure-core-web-vitals/
category: semrush-blog
section: "Semrush blog — SEO/GEO methodology"
date: 2021-03-09
---

# Measure Core Web Vitals with Semrush Site Audit

You’ve probably heard about Core Web Vitals — the three performance metrics Google is promoting in an effort to encourage a better user experience on the web.

Semrush now has a report within the [Site Audit](https://www.semrush.com/siteaudit/) tool to help you out.

## What Are Core Web Vitals?

Google classifies 3 metrics as the [Core Web Vitals](https://web.dev/vitals/#core-web-vitals):

**Largest Contentful Paint**([LCP](https://www.semrush.com/blog/lcp/)) — a metric that tracks loading speed.**First Input Delay**([FID](https://www.semrush.com/blog/google-inp/)) — a metric that tracks the time it takes before someone interacts with the page.**Cumulative Layout Shift**([CLS](https://www.semrush.com/blog/cumulative-layout-shift/)) — a metric that tracks visual stability on the page.

It was already announced that these 3 metrics, LCP, FID, and CLS, would become ranking factors on mobile search in June 2021.

## How Semrush Can Help

We’ll discuss optimizing your core web vitals below, but first, let’s see what data you can get from Semrush.

All you have to do is go to [Site Audit](https://www.semrush.com/siteaudit/) and set up your audit.

In step 2 of the wizard, set your user-agent to mobile if you want to evaluate your site’s mobile version, or desktop if you want to evaluate the desktop version.

Once you’re done configuring your Site Audit, run the audit and you should see results in a few minutes.

After running an audit, locate the report on your core web vitals nearby the Thematic Reports.

With this, you can quickly see a report and learn if your pages have poor, in need of improvement, or good core web vitals without adding another step to your auditing workflow.

According to Google, the pages on your site should all be “good” in regards to each of these 3 metrics.

This report can currently check up to 10 URLs on your site. You can change these 10 pages at any time from above the table in the report. Just select “Edit list” and then you’ll be able to check exactly the pages you want to.

Take a screenshot to save this information. This is what you should share with your development team along with the recommendations that will help optimize your core web vitals.

The benefit of this report is that you can re-run the audit after making adjustments and see the trend of your CWVs as they improve or worsen after any changes to the site.

In your first audit, the 10 URLs will be the first 10 that are checked by our crawler. If you set your crawl scope up as a file of URLs, we will check core web vitals for the first 10 rows of your file. After the first crawl, you can customize the 10 pages to check at any time.

This information is collected via Google Lighthouse. You can find more details about this process in our [Knowledge Base](https://www.semrush.com/kb/1102-how-do-you-collect-data-to-measure-core-web-vitals-in-site-audit) or watch a walk-through from the video below.

## Optimizing Your Core Web Vitals

Since each metric indicates a separate but related aspect of user experience, here’s how you can address them.

### Largest Contentful Paint (LCP)

This metric tracks loading speed, or more specifically how long it takes before the largest content element of the visible part of the page appears to a user.

LCP is hurt by:

- Slow server response time
- Java and CSS that blocks rendering
- Slow loading resources (especially image and video files)
- Client side rendering

- Optimize your server
- Adopt a local image CDN to serve global users faster
- Cache assets & serve HTML pages cache-first
- Minify CSS and JavaScript

### First Input Delay (FID)

This metric tracks the time it takes before a user interacts with a page by clicking or operating part of the UI. This helps you measure your webpage’s overall responsiveness.

Since this metric relies on a real user event, it can only be measured “in the field” and can’t be replicated in a lab.

However, there’s a metric called Total Blocking Time (TBT) that you can measure in Lighthouse and Semrush that is an ideal similar metric.

TBT (and FID) is hurt by:

- Long tasks
- Long JavaScript execution time
- Large JavaScript bundles
- Render-blocking JavaScript

- Reduce your JavaScript execution time
- Implement lazy-loading
- Minimize unused polyfills
- Monitor change with TBT

### Cumulative Layout Shift (CLS)

This metric tracks the visual stability of a webpage — most commonly hurt by ads, pop ups, and banners that suddenly alter the webpage while someone is on the page.

The result of a poor CLS is usually very frustrating and can cause people to yell in despair or violently exit your webpage.

**CLS is hurt by:**

- Ads causing any change in layout
- Cookie banners / notices
- Images without dimensions
- Dynamically injected content
- Embeds and iframes without dimensions
- Web fonts causing
[FOIT/FOUT](https://css-tricks.com/fout-foit-foft/)(flash of invisible text/flash of unstyled text)

- Always include <width> and <height> size attributes on your images and video elements
- Define the space for each asset on your page (ads, banners, responsive images, videos, etc)
- Load content downwards

### Other Site Audit Checks that Can Help

As far as keeping up with the rest of your site, you should also keep an eye open for these other checks in Site Audit that can help you monitor your performance.

- Slow loading pages
- Pages with too large HTML size
- Issues with broken internal JavaScript and CSS files
- Unminified CSS/JavaScript
- Issues with uncached JavaScript and CSS files
- Uncompressed JavaScript and CSS files
- Uncompressed pages
- Pages with JavaScript and CSS total size that is too large
- Pages with too many JavaScript and CSS files

There’s even a Site Performance report to quickly find your site’s performance related issues.

Now that you know what Semrush can do, go out and check your core web vitals!
