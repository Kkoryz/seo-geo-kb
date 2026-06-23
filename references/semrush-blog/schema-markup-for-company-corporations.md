---
title: "Organization Schema: What It Is & How to Implement It"
source_url: https://www.semrush.com/blog/schema-markup-for-company-corporations/
category: semrush-blog
section: "Semrush blog — SEO/GEO methodology"
date: 2017-07-26
---

# Organization Schema: What It Is & How to Implement It

## What Is Organization Schema?

Organization schema is a type of structured data you can add to your site’s HTML code. To help search engines better understand your organization.

It looks like this on the backend:

And gives search engines information like:

- Your company’s name
- The company’s physical address
- Your company’s business description
- Links to your social media profiles

## Why Is Organization Schema Important for SEO?

Organization schema tells search engines more about your company.

While structured data isn’t a ranking factor itself, using it can make it easier for search engines to show your webpage for relevant queries.

Organization schema, in particular, helps Google display your business information as a [rich result](https://www.semrush.com/blog/rich-snippets/) or [knowledge panel](https://www.semrush.com/blog/google-knowledge-panel/)—with images, links, and additional information.

Like this:

These eye-catching results can help your business stand out on the search engine results page (SERP). And potentially [attract more clicks](https://developers.google.com/search/docs/appearance/structured-data/intro-structured-data) and organic (or unpaid) traffic.

This is especially beneficial for [local SEO](https://www.semrush.com/blog/ultimate-local-seo-checklist/).

By using schema, organizations can highlight their business's location, operating hours, and contact details for search engines.

Which can, in turn, generate rich results that can drive more foot traffic to your physical locations.

**Further reading: ***How to Improve Your SEO by Using Schema Markup: Tips From Pros*

## How to Implement Organization Schema

To implement organization schema, you need to write the organization [schema markup](https://www.semrush.com/blog/schema-markup/). And add it to your website.

You can do this by using a plugin, using AI, or writing your schema markup manually.

Here’s how to create JSON-LD organization schema. Plus an example.

### Use a Plugin to Add Organization Schema to Your Site

Plugins that let you add schema markup through JSON-LD include SchemaPro, Rank Math, and Yoast.

Using plugins gives you less control over customization. But it can make implementation faster.

For example, you can create organization schema using the Yoast plugin by simply filling out a form.

Image Source: **Yoast**

### Use AI to Generate Organization Schema Markup

Another way to create organization schema markup is with the help of an AI tool. Like ChatGPT.

Use the following prompt, making sure to replace the data with your company’s information:

*“Hi, can you create JSON-LD organization schema markup for my business?*

*Type of organization: OnlineBusinessOrganization name: Best Online BusinessOfficial website: bestonlinebusiness.comBusiness description: We are number oneAddress: Superior Street, Top-Notch State, Greatest Country 11111Email: numberone@bestonlinebusiness.comContact number: +1 111 111 1111Links to social accounts: https://www.x.com/bestonlinebusiness, https://www.facebook.com/bestonlinebusiness, https://www.linkedin.com/company/bestonlinebusinessOfficial logo: best-logo-ever.jpg”*

ChatGPT generated this code:

Copy the code. And add it to the <head> section of your website’s HTML.

### Write Organization Schema Markup Manually

To start, open an HTML editor such as Notepad or Notepad++.

Then, create a new <script> tag. And set the type attribute of the script tag to "application/ld+json."

Here’s what that should look like:

`<script type="application/ld+json">`

</script>

Next, add your JSON-LD code within your script tags using the structure below and fill in the relevant information for your organization:

|
|
|
|
| “@context” | Specifies the schema.org vocabulary | "https://schema.org" |
| “@type” | Defines the type of organization | "Organization" or a subcategory like “EducationalOrganization” View the full list of subcategories at |
| “name” | Your organization's name | "Acme Corporation" |
| “url” | Your organization's website | "https://www.acme.com" |
| “logo” | URL of your organization's logo | "https://www.acme.com/logo.png" |
| “address” | Physical address | Barcelona, Spain 08026 Carrer del Freser See the example below for the exact address structure to use. |
| “contactPoint” | Contact information | telephone: +1-555-123-4567, contactType": customer service See the example below for the exact contact structure to use. |
| “sameAs” | Links to your social media profiles | ["https://www.facebook.com/acme", "https://twitter.com/acme"] |

Alternatively, copy/paste the code below into your editor and then enter your organization's information inside the empty quotes (“”):

`<script type="application/ld+json">`

{

"@context": "https://schema.org",

"@type": "Organization",

"@id": "",

"name": "",

"url": "",

"address": {

"@type": "PostalAddress",

"addressLocality": "",

"addressCountry": "",

"postalCode": "",

"streetAddress": ""

},

"logo": "",

"description": "",

"sameAs": [

"",

"",

""]

}

</script>

You can also include any additional fields that apply to your specific needs. For more properties, check out Schema.org’s [full property list](https://schema.org/Organization).

Once you’re happy with your JSON-LD markup, add the code snippet to the <head> or <body> section of your homepage’s HTML code.

### Examples of JSON-LD Organization Schema

If you need inspiration or more guidance, here are two great examples of organization schema:

**Here’s an example of JSON-LD organization schema for a library:**

`<script type="application/ld+json">`

{

"@context": "https://schema.org",

"@type": "Library",

"name": "Central City Library",

"url": "https://www.centralcitylibrary.org",

"logo": "https://www.centralcitylibrary.org/logo.png",

"address": {

"@type": "PostalAddress",

"streetAddress": "456 Book Lane",

"addressLocality": "Central City",

"addressRegion": "ST",

"postalCode": "67890",

"addressCountry": "US"

},

"telephone": "+1-555-987-6543",

"email": "info@centralcitylibrary.org",

"openingHours": "Mo,Tu,We,Th,Fr 09:00-20:00 Sa 10:00-17:00",

"areaServed": "Central City",

"sameAs": [

"https://www.facebook.com/centralcitylibrary",

"https://twitter.com/centralcitylib"

]

}

</script>

**Here’s another organization schema example for a restaurant: **

`<script type="application/ld+json">`

{

"@context": "https://schema.org",

"@type": "Restaurant",

"name": "Gourmet Delight",

"url": "https://www.gourmetdelight.com",

"logo": "https://www.gourmetdelight.com/logo.png",

"image": "https://www.gourmetdelight.com/restaurant-image.jpg",

"address": {

"@type": "PostalAddress",

"streetAddress": "789 Tasty Avenue",

"addressLocality": "Flavortown",

"addressRegion": "ST",

"postalCode": "54321",

"addressCountry": "US"

},

"telephone": "+1-555-789-0123",

"servesCuisine": ["Italian", "Mediterranean"],

"priceRange": "$$",

"openingHours": "Mo-Sa 11:00-23:00 Su 12:00-22:00",

"menu": "https://www.gourmetdelight.com/menu",

"acceptsReservations": "True",

"sameAs": [

"https://www.facebook.com/gourmetdelight",

"https://www.instagram.com/gourmetdelight"

]

}

</script>

## How to Test Your Organization Schema

Once you’ve implemented your schema, test it to make sure it’s working correctly.

Here are three tools you can use to do this:

### Site Audit

Test your schema with our [free SEO checker](https://www.semrush.com/siteaudit/). For full-site monitoring, step up to Semrush Site Audit.

First, open the Site Audit tool. By signing in to your Semrush account. And clicking “**Site Audit**” under “On Page & Tech SEO.”

If you have an existing project for the website you want to test, click on that.

Alternatively, create a new project with the relevant domain by clicking “**+ Create project**.” To automatically run a site audit.

Next, you’ll be asked to configure your Site Audit settings. If you’re a beginner or just trying out the tool, you can proceed with the pre-set metrics.

Alternatively, check out our [guide to configuring Site Audit](https://www.semrush.com/kb/539-configuring-site-audit#:~:text=To%20set%20up%20a%20Site,Troubleshooting%20Site%20Audit%20for%20help.) for more information.

Click “**Start Site Audit**” when you’re done.

Whether you’ve clicked on an existing project or created a new one, you’ll be taken to Site Audit’s “Overview” dashboard.

Find the “Markup” section and click “**View details.**”

On the next screen, you’ll see:

- How many of your checked pages contain schema markup
- The type of schema markup found on each page
- Any schema markup that’s invalid

Like this:

Scroll down to find a table entitled “Structured Data Items.”

If any of the items are invalid, like your organization schema, click “**View all invalid items**” at the bottom.

Click on any entry in the “Affected Fields” column to see specific errors per identified issue.

Now you can see the errors and fix them. If you’re not sure how to fix an error, click on “**Why and how to fix it**” for more information.

Once you’ve fixed the errors, rerun the audit to check they’ve been rectified.

### Schema Markup Validator

The [schema markup validator](https://validator.schema.org/) is Schema.org’s official testing tool.

To test a webpage you’ve already added organization schema to, enter the URL in the field under “**Fetch URL**.” And click “**Run test**.”

Alternatively, test a code snippet you’ve written but haven’t implemented by clicking on the “**Code snippet**” tab.

Paste your code into the box and click “**Run test**.”

Ideally, you’re looking for a “0 Errors” and “0 Warnings” result like this:

If there are any errors, the tool will highlight them so you can easily find and fix them.

### Rich Result Test

The [Rich Results Test](https://search.google.com/test/rich-results) is the Google organization schema markup checker. But it can also verify other structured data on your site.

You can use the Rich Result Test to see what rich results your pages can generate based on the schema you already have. But you can also use it to test the validity of existing or drafted schema markup.

Test your drafted schema markup before implementing it by going to the tool and clicking on the “**Code**” tab.

Paste your code into the box. And click “**Test Code**.”

If your code is valid, you’ll see a green checkmark in the “Test results” section. Along with a “1 valid item detected” message.

Like this:

Now, you can go ahead and paste the organization schema into your website’s HTML.

## Best Practices for Using Organization Schema

Here are some best practices to keep in mind when implementing organization schema:

- Use JSON-LD format where possible
- Only include accurate and up-to-date information. Information in your schema markup should match other details about your company across the web. This includes your Google Business Profile and info on your website and socials.
- Add as much relevant information as possible. For example, the “LocalBusiness” subcategory lets you add opening hours, prices, geo-coordinates, and more.
- Add as many “@sameAs” links as possible. This will improve your credibility and add context.
- Follow Google’s
[spam guidelines](https://developers.google.com/search/docs/essentials/spam-policies). Don’t use structured data to mislead users. Make sure the information you provide is truthful and accurate. - Use the most specific type of schema possible for your organization. For example, if you're a restaurant, use "Restaurant" instead of just "LocalBusiness."
- Test your schema implementation with our
[SEO check](https://www.semrush.com/siteaudit/)for a quick markup review, or use Semrush Site Audit for a holistic site-wide scan.

## Leverage Schema to Maximize Your Search Presence

Organization schema is a great way to improve your company’s overall SERP visibility.

Ultimately, that can improve the amount of traffic you get to your website. And, potentially, your number of customers.

Semrush [SEO Audit](https://www.semrush.com/siteaudit/) tool makes it easy to view and test your structured data. Along with a wealth of other technical data about your website’s SEO performance.

Sign up for free and start improving your website’s SEO performance today.

*This post was updated in 2024. Excerpts from the original article by Rachel Baker may remain.*
