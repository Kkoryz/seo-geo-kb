---
title: "App Engine IP Range Change Notice | Google Search Central Blog | Google for Developers"
source_url: https://developers.google.com/search/blog/2014/03/app-engine-ip-range-change-notice
category: google-search-central
section: "Google Search Central — official technical SEO + structured data docs"
date: 2014-03-18
---

# App Engine IP Range Change Notice | Google Search Central Blog | Google for Developers

Google uses a wide range of IP addresses for its different services, and the addresses may change
without notification.
Google App Engine
is a Platform as a Service offering which hosts a wide variety of 3rd party applications. This
post announces changes in the IP address range and headers used by the Google App Engine
URLFetch (outbound HTTP) and outbound sockets APIs.

While we recommend that App Engine IP ranges not be used to filter inbound requests, we are aware
that some services have created filters that rely on specific addresses. Google App Engine will be
changing its IP range beginning this month. Please see
these instructions
to determine App Engine's IP range.

Additionally, the HTTP
User-Agent header string
that historically allowed identification of individual App Engine applications should no longer
be relied on to identify the application. With the introduction of outbound
sockets for App Engine,
applications may now make HTTP requests without using the URLFetch API, and those
requests may set a User-Agent of their own choosing.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Missing the information I need","missingTheInformationINeed","thumb-down"],["Too complicated / too many steps","tooComplicatedTooManySteps","thumb-down"],["Out of date","outOfDate","thumb-down"],["Samples / code issue","samplesCodeIssue","thumb-down"],["Other","otherDown","thumb-down"]],[],[],["Google App Engine is altering its IP address range for `URLFetch` and outbound sockets APIs, with changes beginning this month. Instructions for determining the new IP range are provided. Services relying on specific App Engine IP addresses for filters will need to adjust. Additionally, the `User-Agent` header is no longer a reliable identifier for App Engine applications, as the introduction of outbound sockets permits applications to customize it or send request without using `URLFetch` API.\n"]]
