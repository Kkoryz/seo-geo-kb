---
title: "Search Console API announcements | Google Search Central Blog | Google for Developers"
source_url: https://developers.google.com/search/blog/2020/08/search-console-api-announcements
category: google-search-central
section: "Google Search Central — official technical SEO + structured data docs"
date: 2020-08-06
---

# Search Console API announcements | Google Search Central Blog | Google for Developers

Thursday, August 06, 2020

Over the past year, we have been working to upgrade the infrastructure of the
[Search Console API](/webmaster-tools), and we are happy to let you know that we're
almost there. You might have already noticed some minor changes, but in general, our goal was to
make the migration as invisible as possible. This change will help Google to improve the
performance of the API as demand grows.

Note that **if you're not querying the API yourself you don't need to take action**.
If you are querying the API for your own data or if you maintain a tool which uses that data
(for example, a WordPress plugin), read on. Below is a summary of the changes:

-
**Changes on Google Cloud Platform dashboard**: you'll see is a drop in the old API usage report and an increase in the new one. -
**API key restriction changes**: if you have previously set API key restrictions, you might need to change them. -
**Discovery document changes**: if you're querying the API using a third-party API library or querying the[Webmasters Discovery Document](https://www.googleapis.com/discovery/v1/apis/webmasters/v3/rest)directly, you will need to update it by the end of the year.

Please note that other than these changes, the **API is backward compatible** and
there are currently no changes in scope or functionality.

## Google Cloud Platform (GCP) changes

In the
[Google Cloud Console dashboards](https://cloud.google.com/monitoring/charts/dashboards),
you will notice a traffic drop for the legacy API and an increase in calls to the new one. This
is the same API, just under the new name.


You can monitor your API usage on the
[new Google Search Console API page](https://console.cloud.google.com/apis/api/searchconsole.googleapis.com/overview).

## API key restriction changes

As mentioned in the introduction, these instructions are important only if you query the data yourself or provide a tool that does that for your users.

To check if you have an API restriction active on your API key, follow
[these steps](https://cloud.google.com/docs/authentication/api-keys#adding_api_restrictions)
in the [credentials page](https://console.cloud.google.com/apis/credentials)
and make sure the Search Console API is not restricted. If you have added an API restriction for
your API keys **you will need to take action by August 31**.

In order to allow your API calls to be migrated automatically to the new API infrastructure, you need to make sure the Google Search Console API is not restricted.

- If your API restrictions are set to "Don't restrict key" you're all set.
-
If your API restrictions are set to "Restrict key",
**the Search Console API should be checked as shown in the image below**.


## Discovery document changes

If you're querying the Search Console API using an
[external API library](/api-client-library), or
querying the
[Webmasters API discovery document](https://www.googleapis.com/discovery/v1/apis/webmasters/v3/rest)
directly **you will need to take action** as we'll drop the support in the
Webmasters discovery document. Our current plan is to support it until December 31, 2020 - but
**we'll provide more details and guidance in the coming months**.

If you have any questions, you can ask in the
[help community](https://support.google.com/webmasters/threads?thread_filter=(category:search_console))
or the Google Webmasters [Twitter handle](https://twitter.com/googlesearchc).
