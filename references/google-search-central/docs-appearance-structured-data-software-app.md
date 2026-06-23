---
title: "Software App (SoftwareApplication) Schema | Google Search Central | Documentation | Google for Developers"
source_url: https://developers.google.com/search/docs/appearance/structured-data/software-app
category: google-search-central
section: "Google Search Central — official technical SEO + structured data docs"
date: 2025-12-10
---

# Software App (SoftwareApplication) Schema | Google Search Central | Documentation | Google for Developers

# Software app (`SoftwareApplication`

) structured data

Mark up software application information in the body of a web page to better display your app details in Google Search results.

## How to add structured data

Structured data is a standardized format for providing information about a page and classifying the page
content. If you're new to structured data, you can learn more about
[how structured data works](/search/docs/appearance/structured-data/intro-structured-data).

Here's an overview of how to build, test, and release structured data.

- Add the
[required properties](#structured-data-type-definitions). Based on the format you're using, learn where to[insert structured data on the page](/search/docs/appearance/structured-data/intro-structured-data#format-placement). - Follow the
[guidelines](#guidelines). - Validate your code using the
[Rich Results Test](https://search.google.com/test/rich-results)and fix any critical errors. Consider also fixing any non-critical issues that may be flagged in the tool, as they can help improve the quality of your structured data (however, this isn't necessary to be eligible for rich results). - Deploy a few pages that include your structured data and use the
[URL Inspection tool](https://support.google.com/webmasters/answer/9012289)to test how Google sees the page. Be sure that your page is accessible to Google and not blocked by a robots.txt file, the`noindex`

tag, or login requirements. If the page looks okay, you can[ask Google to recrawl your URLs](/search/docs/crawling-indexing/ask-google-to-recrawl). - To keep Google informed of future changes, we recommend that you
[submit a sitemap](/search/docs/crawling-indexing/sitemaps/build-sitemap). You can automate this with the[Search Console Sitemap API](/webmaster-tools/v1/sitemaps).

## Examples

Here's an example of a software app in JSON-LD:

<html> <head> <title>Angry Birds</title> <script type="application/ld+json"> { "@context": "https://schema.org", "@type": "SoftwareApplication", "name": "Angry Birds", "operatingSystem": "ANDROID", "applicationCategory": "GameApplication", "aggregateRating": { "@type": "AggregateRating", "ratingValue": 4.6, "ratingCount": 8864 }, "offers": { "@type": "Offer", "price": 1.00, "priceCurrency": "USD" } } </script> </head> <body> </body> </html>

Here's an example of a software app in RDFa:

<div vocab="https://schema.org/" typeof="SoftwareApplication"> <span property="name">Angry Birds</span> - REQUIRES <span property="operatingSystem">ANDROID</span> TYPE: <span property="applicationCategory" content="GameApplication">Game</span> RATING: <div property="aggregateRating" typeof="AggregateRating"> <span property="ratingValue">4.6</span> ( <span property="ratingCount">8864</span> ratings ) </div> <div property="offers" typeof="Offer"> Price: $<span property="price">1.00</span> <meta property="priceCurrency" content="USD" /> </div> </div>

Here's an example of a software app in Microdata:

<div itemscope itemtype="https://schema.org/SoftwareApplication"> <span itemprop="name">Angry Birds</span> - REQUIRES <span itemprop="operatingSystem">ANDROID</span> TYPE: <span itemprop="applicationCategory" content="GameApplication">Game</span> RATING: <div itemprop="aggregateRating" itemscope itemtype="https://schema.org/AggregateRating"> <span itemprop="ratingValue">4.6</span> ( <span itemprop="ratingCount">8864</span> ratings ) </div> <div itemprop="offers" itemscope itemtype="https://schema.org/Offer"> Price: $<span itemprop="price">1.00</span> <meta itemprop="priceCurrency" content="USD" /> </div> </div>

## Guidelines

You must follow these guidelines for your app to be eligible to appear as a rich result.

## Structured data type definitions

You must include the required properties for your content to be eligible for display as a rich result. You can also include the recommended properties to add more information about your content, which could provide a better user experience.

`SoftwareApplication`


The full definition of `SoftwareApplication`

is available at
[schema.org/SoftwareApplication](https://schema.org/SoftwareApplication).

The Google-supported properties are the following:

| Required properties | |||||
|---|---|---|---|---|---|
`name`
|
The name of the app. |
||||
`offers.price`
|
An offer to sell the app. For developers,
If the app is available without payment, set "offers": { "@type": "Offer", "price": 0 }
If the app has a price greater than 0, we recommend also including the "offers": { "@type": "Offer", "price": 1.00, "priceCurrency": "USD" } |
||||
| Rating or review |
A rating or review of the app. You must include one of the following properties:
|

| Recommended properties | |
|---|---|
`applicationCategory`
|
The type of app (for example,
`GameApplication` `SocialNetworkingApplication` `TravelApplication` `ShoppingApplication` `SportsApplication` `LifestyleApplication` `BusinessApplication` `DesignApplication` `DeveloperApplication` `DriverApplication` `EducationalApplication` `HealthApplication` `FinanceApplication` `SecurityApplication` `BrowserApplication` `CommunicationApplication` `DesktopEnhancementApplication` `EntertainmentApplication` `MultimediaApplication` `HomeApplication` `UtilitiesApplication` `ReferenceApplication`
|
`operatingSystem`
|
The operating system(s) required to use the app (for example, |

### Extended properties for app subtypes

For mobile applications and web applications, Google also supports
[ MobileApplication
](https://schema.org/MobileApplication) and

[.](https://schema.org/WebApplication)

```
WebApplication
```

Google doesn't show a rich result for Software Apps that only have the [ VideoGame](https://schema.org/VideoGame) type.
To make sure that your Software App is eligible for display as a rich result, co-type the

[type with another type. For example:](https://schema.org/VideoGame)

`VideoGame`

{ "@context": "https://schema.org", "@type": ["VideoGame", "MobileApplication"], .... }

## Troubleshooting

If you're having trouble implementing or debugging structured data, here are some resources that may help you.

- If you're using a content management system (CMS) or someone else is taking care of your site, ask them to help you. Make sure to forward any Search Console message that details the issue to them.
- Google does not guarantee that features that consume structured data will show up in search results.
For a list of common reasons why Google may not show your content in a rich result, see the
[General Structured Data Guidelines](/search/docs/appearance/structured-data/sd-policies). - You might have an error in your structured data. Check the
[list of structured data errors](https://support.google.com/webmasters/answer/13300873)and the[Unparsable structured data report](https://support.google.com/webmasters/answer/9166415). - If you received a structured data manual action against your page, the structured data on
the page will be ignored (although the page can still appear in Google Search results). To fix
[structured data issues](https://support.google.com/webmasters/answer/9044175#zippy=%2Cstructured-data-issue), use the[Manual Actions report](https://support.google.com/webmasters/answer/9044175). - Review the
[guidelines](#guidelines)again to identify if your content isn't compliant with the guidelines. The problem can be caused by either spammy content or spammy markup usage. However, the issue may not be a syntax issue, and so the Rich Results Test won't be able to identify these issues. [Troubleshoot missing rich results / drop in total rich results](https://support.google.com/webmasters/answer/13300208).- Allow time for re-crawling and re-indexing. Remember that it may take several days after
publishing a page for Google to find and crawl it. For general questions about crawling and indexing, check the
[Google Search crawling and indexing FAQ](/search/help/crawling-index-faq). - Post a question in the
[Google Search Central forum](https://support.google.com/webmasters/community).
