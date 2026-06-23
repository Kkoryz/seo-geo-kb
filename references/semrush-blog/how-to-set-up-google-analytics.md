---
title: "How to Set Up GA4: A Complete Step-by-Step Guide (2025)"
source_url: https://www.semrush.com/blog/how-to-set-up-google-analytics/
category: semrush-blog
section: "Semrush blog — SEO/GEO methodology"
date: 2021-09-09
---

# How to Set Up GA4: A Complete Step-by-Step Guide (2025)

## What Is GA4?

Google Analytics 4 (GA4) is a free tool for tracking visits to websites and apps. It also tracks interactions that occur on these platforms.

This tool provides insights into traffic numbers, user demographics, most-visited pages, and more. Google developed GA4 and its predecessor, Universal Analytics (UA).

In this guide, we’ll explain how GA4 differs from UA, how to set up GA4, and how to use it to track your website’s performance.

## How GA4 Tracking Differs from UA

UA was the earlier version of Google Analytics before Google launched GA4 in October 2020.

GA4 differs from UA in key ways:

**User interactions**: UA called user interactions “hits,” with specific hit types for page views, events, and other interactions. GA4 calls all user interactions “events.”**Google Analytics account structure**: UA accounts could contain multiple properties, which could then contain multiple views for filtered data segments. GA4 accounts can still contain multiple[properties](https://www.semrush.com/blog/how-to-set-up-google-analytics/#2--create-a-ga4-property), but they cannot contain views. Unlike UA properties, GA4 properties can receive multiple data streams from websites and apps. UA properties tracked data from only one source.

Standard UA accounts stopped processing data on July 1, 2023. If you want to track website performance with Google Analytics, you need to set up GA4.

**Further reading***: **Differences Between GA4 and UA*

## How to Set up GA4

Setting up GA4 involves five main steps:

[Create a GA4 Account](https://www.semrush.com/blog/how-to-set-up-google-analytics/#1--create-a-ga4-account)[Create a GA4 Property](https://www.semrush.com/blog/how-to-set-up-google-analytics/#2--create-a-ga4-property)[Provide Your Business Details](https://www.semrush.com/blog/how-to-set-up-google-analytics/#3--provide-your-business-details)[Provide Your Business Objectives](https://www.semrush.com/blog/how-to-set-up-google-analytics/#4--provide-your-business-objectives)[Create a Data Stream](https://www.semrush.com/blog/how-to-set-up-google-analytics/#5--create-a-data-stream)

### 1. Create a GA4 Account

You need a Google Analytics account to set up GA4. If you don’t already have one, go to[https://analytics.google.com/](https://analytics.google.com/) and log in to your Google account.

After logging in, click the gear icon on the left sidebar to access the “**Admin**” settings.

On the Admin dashboard, click “**+ Create**” > “**Account**” to create your Google Analytics account.

Give your account a name in the “Account name” field. Use the “Account Data Sharing Settings” to select how you want to [share your data with Google](https://support.google.com/analytics/answer/1011397).

Click “**Next**” when you’re done.

### 2. Create a GA4 Property

A GA4 property is a collection of data from a website or app. A simple property example is one that has data from only a single website or app. If you have more advanced reporting needs, set up a property that gathers [data from multiple sources](https://support.google.com/analytics/answer/9679158).

To create a GA4 property, provide a name in the “Property name” field. The name must contain at least four characters. Then, specify your preferred time zone and currency.

Click “Next.”

### 3. Provide Your Business Details

Fill out the “Industry category” and “Business size” fields.

Click “Next.”

### 4. Provide Your Business Objectives

Select at least one business objective. GA4 uses these choices to tailor its [default reports](https://support.google.com/analytics/answer/12924488#default-reports) to meet your needs.

If you select “**Get baseline reports**,” GA4 will provide reports [covering the entire customer life cycle](https://support.google.com/analytics/answer/12924233#access-collection) instead of reports focused on a single business objective.

Click “Create.”

Google Analytics’ terms of service agreement will appear. Adjust the country setting if needed.

Review the agreement. If you accept, click “**I Accept**.”

### 5. Create a Data Stream

A **data stream** sends data from your website or app to your GA4 property. Creating a data stream depends on whether your source is a website, iOS app, or Android app.

To create a data stream from a website, click “**Web**.”

Type your domain in the “Website URL” field. Provide a name in the “Stream name” field.

Then click “**Create stream**.”

A window will appear showing your data stream’s [measurement ID](https://www.semrush.com/blog/google-analytics-tracking-id/) and other details.

Save the measurement ID somewhere convenient. You may need it later.

After creating your website’s data stream, the next step is to install GA4 on your website.

**Further reading***: **This guide** covers creating data streams for iOS and Android apps.*

## How to Install GA4 on Your Website

Watch this video for an overview of the GA4 installation process on a website:

Below, we’ll share the steps for these three GA4 installation methods:

Use the first method if you have [Google Tag Manager (GTM)](https://www.semrush.com/blog/google-tag-manager/) on your site.

Use the second method if you used a website builder like WordPress, Squarespace, or Wix and don’t have GTM.

If your website doesn’t have GTM and can’t integrate with GA4, use the third method to install GA4 manually.

### Method 1: Install GA4 with Google Tag Manager

GTM is a platform for adding code snippets (called “tags”) to a website without direct code edits. This includes tags for GA4.

If you want to use this method but don’t have GTM installed, [follow these steps](https://www.semrush.com/blog/google-tag-manager/#how-to-set-up-google-tag-manager) to set it up first. You’ll create a “container” that holds tags and other modifications in GTM.

Then, go to[https://tagmanager.google.com/](https://tagmanager.google.com/) and log in to your Google account.

Select your website’s GTM container.

Click “**Add a new tag**” on your container’s workspace overview.

Click “**Untitled Tag**” to name your tag, like “**GA4 Setup**.”

Click anywhere in the “**Tag Configuration**” panel.

From the “Choose tag type” window, select “**Google Tag**.”

Fill out the “Tag ID” field with your GA4 data stream’s measurement ID. If you haven’t saved it, [learn how to find it here](https://support.google.com/analytics/answer/12270356?hl=en).

Adjust the tag’s configuration, shared event, and advanced settings if needed.

Click anywhere in the “**Triggering**” panel to specify when GTM should load the GA4 tag. That tag sends data from your website to GA4.

From the “Choose a trigger” window, select “**Initialization - All Pages**.” This will load the GA4 tag before any other tags.

Click “**Save**” to save your new tag.

Next, test your GA4 tag by clicking “**Preview**” on the container’s workspace overview.

The Google Tag Assistant will open in a new tab. Type your domain into the “Your website’s URL” field and click “**Connect**.”

Your website will open in a new window. Leave it open and return to Tag Assistant.

If Tag Assistant connects successfully, a “Connected!” window will appear. Click “**Continue**.”

In Tag Assistant, check the “Tags Fired” category in the “Output of [your measurement ID]” panel. If you see your GA4 tag there, GTM loaded it successfully.

Close Tag Assistant and your website. Then, click “**Submit**” in the container’s workspace overview to finalize your GTM changes.

A “Submit Changes” window will appear.

Leave “Submission Configuration” as “Publish and Create Version.” Then use:

- The “Version Name” field to name the new version of your website (e.g., “GA4 installed”)
- The “Version Description” field to provide details of your changes

Click “**Publish**” to activate your GA4 installation.

### Method 2: Install GA4 Using an Integration

Some website builders (like Squarespace and Wix) have native GA4 integration. They include built-in features to connect a site with GA4. You just add your GA4 [measurement ID](https://www.semrush.com/blog/how-to-set-up-google-analytics/#5--create-a-data-stream).

Follow these guides to install GA4 using your website builder’s native integration:

WordPress doesn’t have native GA4 integration. Instead, use a third-party plugin. Many are available, including Google’s [Site Kit](https://sitekit.withgoogle.com/) plugin, which we’ll demonstrate here.

Log in to your WordPress admin dashboard and click “**Plugins**” > “**Add New Plugin**.”

On the “Add Plugins” page, type “site kit” into the search field.

Then, press “**Enter**” or “**return**” on your keyboard to run the search.

Look for “Site Kit by Google – Analytics, Search Console, AdSense, Speed.” Click “**Install Now**" to add the plugin.

Then click “**Activate**.”

You’ll see a success message confirming Site Kit activation. Click “**Start setup**.”

On the setup screen, check the box that says “**Connect Google Analytics as part of your setup**,” then click “**Sign in with Google**.”

Sign in and grant Site Kit access to your Google account as prompted.

Site Kit will guide you through [these three steps](https://sitekit.withgoogle.com/documentation/getting-started/connecting-services/):

- Verifying ownership of your website
- Turning on metrics in Site Kit
- Setting up
[Google Search Console (GSC)](https://www.semrush.com/blog/google-search-console/)

When you finish, you’ll see a screen labeled “Set up Google Analytics.” Click “**Next**” to install GA4 on your site.

On the “Connect Service” screen, use the “Account,” “Property,” and “Web data stream” drop-downs to select the GA4 [account](https://www.semrush.com/blog/how-to-set-up-google-analytics/#1--create-a-ga4-account), [property](https://www.semrush.com/blog/how-to-set-up-google-analytics/#2--create-a-ga4-property), and [data stream](https://www.semrush.com/blog/how-to-set-up-google-analytics/#5--create-a-data-stream) you created.

Then click “**Configure Analytics**.”

A success message will confirm GA4 is installed on your website.

### Method 3: Install GA4 Manually

To install GA4 manually, go to the “Web stream details”window for your website’s data stream in GA4. Click “**Admin**” in the left sidebar.

Under “Property settings,” select “**Data collection and modification**” > “**Data streams**.”

Click your website’s data stream.

In the “Web stream details” window, scroll down and select “**View tag instructions**.”

Click “**Install manually**.”

A code snippet will appear. Copy it using the clipboard icon.

Paste the snippet into each page’s HTML, immediately after the opening <head> tag.

Save your changes.

## How to Track Events with GA4

UA treated “events” as specific user interactions (excluding page loads). GA4 considers **all** interactions as “events.”

GA4 events examples include:

- Page loads
- First visits
- Form submissions
- Adding items to a shopping cart

To see events in GA4, click “**Reports**” in the left sidebar.

Then click “**Engagement**” > “**Events**.”

You’ll see a list of events GA4 detected for a specific date range.

Each event entry shows:

**Event count**: Total triggers of that event**Total users**: Unique users who triggered the event**Event count per user**: Average triggers per user**Total revenue**: Total revenue the event generated

Click the date range at the top to change the event reporting time frame.

Click any event in the report to get event-specific metrics like:

- Event count by country
- Event count by gender
- Events per session

For example, here’s the user_engagement event report:

You can also create an “Exploration” (an advanced custom report) for certain events.

**Further reading***: **How to Create a Custom GA4 Events Exploration*

## How to Track Conversions with GA4

A conversion is an event that fulfills a business goal. Examples include:

- A product demonstration booking
- An order placement
- A file download

GA4 doesn’t provide default conversion events, so you must [set them up yourself](https://support.google.com/analytics/answer/12966437) to match your goals. GA4 will then record them as they occur.

To view conversions, click “**Reports**” in the left sidebar.

Then click “**Engagement**” > “**Conversions**.”

For any given date range, you’ll see:

**Conversions**: The number of times the conversion event occurred**Total users**: How many unique users converted**Total revenue**: Revenue earned from that event

Use the Conversions metric in other GA4 reports to track conversions by traffic source, page, or other attributes. For example, in the [Pages and screens report](https://support.google.com/analytics/answer/12926732), you can see how many conversions occurred on each page.

Click the “**All events**” drop-down under the Conversion metric to see results for specific conversion events.

## How to Import Data to GA4

You can import data from other sources (like [CRM tools](https://www.semrush.com/blog/crm-tools/)) into GA4. This centralizes your data so you can analyze it all in one platform.

Data you can import includes:

- Ad cost data
- Item data
- User ID data
- Client ID data
- Offline event data

You can import data manually with a CSV file, or you can schedule regular imports from a CSV file on an SFTP server.

To do this, click “**Admin**” in the left sidebar.

Under “Property settings,” select “**Data collection and modification**” > “**Data import**.”

Click “**Create data source**.”

Give the data source a descriptive name and select the data type you’re importing.

Scroll down and choose your import source.

If your import source is a CSV file, click “**Upload CSV**” to upload the file. If you’re using an SFTP server, switch the import source to “**SFTP**,” fill out your server details, and set up the import schedule.

Click “**Next**.”

Map the data fields from your source to GA4’s fields.

Click “**Import**.”

The import will start right away.

If you’re importing from SFTP, click the pencil icon to rename your import fields to match the CSV.

Then click “**Create & generate key**.”

GA4 will produce a public key to authorize the connection to your SFTP server. Copy this key and add it to your server settings.

GA4 will import your data according to the schedule you set. Then you can analyze data from GA4 and other sources together.

## Types of Analyses in GA4

GA4 can help you analyze:

**Number of users who visited your website**. You can spot trends over time by adjusting the date range.**Demographics of your website visitors**. Includes country, city, language, gender, and interests.

**Most popular pages**. Includes how well they drive conversions.

**Events****happening on your website**

**Conversions****on your website**

**Top traffic sources**. Tracks organic search, email, referrals, and direct visits.

**Devices users use to visit your website**. Distinguishes desktop vs. mobile and even operating systems and browsers.

**Purchase journeys**. Tracks from the start of a session to the viewing of a product to the checkout, and highlights where users drop off in the purchase funnel.

Use these findings to assess how well your website increases brand awareness, grows your customer base, and drives sales.

If you need easier-to-read reports, [AI Narratives for GA4](https://www.semrush.com/apps/ai-narratives-for-ga4/) can help. It uses your GA4 data to deliver straightforward reports on page views, conversions, revenue, and more, along with recommendations for improvements.

AI Narratives for GA4 can also send automated email reports and notify you of unusual traffic changes.

Consider connecting GA4 with other tools for deeper insights. For example, Semrush’s [Organic Traffic Insights](https://www.semrush.com/organic_traffic_insights/) integrates with GA4 and GSC to show keyword, user, and session data from those tools and from Semrush’s own database for your landing pages.

It can also reveal which keywords drive traffic to your pages—even if GA4 labels them as “**(not provided)**.” Then it shows your ranking positions and share of traffic for those keywords.

## Get Started with GA4

Setting up GA4 requires some initial steps, but the free data on website performance makes it worthwhile.

To enhance your GA4 experience, use [AI Narratives for GA4](https://www.semrush.com/apps/ai-narratives-for-ga4/) and [Organic Traffic Insights](https://www.semrush.com/organic_traffic_insights/). These tools can enrich your GA4 reports with recommended next steps and offer a broader view of your search rankings.

Try both for free with a [Semrush account](https://www.semrush.com/signup/).

## FAQs

### How Do I Get Access to GA4?

To get access to GA4, sign up for a Google account, then create a Google Analytics account. Follow [GA4’s onboarding steps](https://www.semrush.com/blog/how-to-set-up-google-analytics/#how-to-set-up-ga4). If you’re installing GA4 on a site, use GTM, a GA4 integration, or manually add the GA4 snippet to your webpages.

### What Is the Best Practice for a GA4 Setup?

Google recommends no more than three data streams (one for a website, one for iOS, and one for Android) per GA4 property. For multiple websites or apps, set up multiple GA4 properties if your data measurement objectives require them.

### How Much Does It Cost to Set up GA4?

GA4 is free to set up. You may incur costs if you use paid third-party tools or integrations. For example, if you have a Semrush account, you can use [AI Narratives for GA4](https://www.semrush.com/apps/ai-narratives-for-ga4/) for free for seven days, then pay $39/month afterward.
