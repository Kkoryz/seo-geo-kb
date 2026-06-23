---
title: "ChatGPT Searches Google Shopping to Create its Recommendations"
source_url: https://www.semrush.com/blog/chatgpt-searches-google-shopping/
category: semrush-blog
section: "Semrush blog — SEO/GEO methodology"
date: 2026-01-20
---

# ChatGPT Searches Google Shopping to Create its Recommendations

More and more research is unwrapping the hidden logic and processes that happen in the background of ChatGPT's search functions.

Interestingly, most of these lean on Google. For example, [previous experiments](https://www.semrush.com/blog/chatgpt-definitely-uses-google/) have confirmed that ChatGPT uses SerpApi for its search functionality.

The reason why is pretty simple: Google has had 27+ years to build an enormous information ecosystem.

And now, investigations from [Oliver de Segonzac](https://www.linkedin.com/posts/resoneo_openai-is-building-a-search-engine-with-googles-activity-7405615667732824064-Bd9M?utm_source=share&utm_medium=member_desktop&rcm=ACoAABpEIj0BN92wBlLnha8Ns3kS6w3kmCz5Hk0), [Alexis Rylko,](https://www.linkedin.com/posts/alexisrylko_chatgpt-shopping-powered-by-google-shopping-activity-7400628344746041344-wSJy?utm_source=share&utm_medium=member_desktop&rcm=ACoAABpEIj0BN92wBlLnha8Ns3kS6w3kmCz5Hk0) and [Tom Wells](https://www.linkedin.com/posts/tom-loves-data_as-openai-announces-some-new-shopping-features-activity-7398816516416172032-VLqQ?utm_source=share&utm_medium=member_desktop&rcm=ACoAABpEIj0BN92wBlLnha8Ns3kS6w3kmCz5Hk0) have also suggested that ChatGPT runs encoded queries through Google Shopping for composing its product carousel recommendations.

This could have real implications for optimization, so we set out to test this for ourselves.

## The TL;DR: Focus Your Product Optimization On Google Shopping

The previous belief was that the information collected from ChatGPT’s [query fan-out](https://www.semrush.com/blog/query-fan-out/) (the Google searches that ChatGPT runs in the background to build a comprehensive response) was the main factor behind product inclusion.

But our experiment confirms that this isn’t the case.

ChatGPT does create additional shopping queries that it sends to Google Shopping. Most of the time, the Google Shopping results will then shape the final products that are included in ChatGPT’s response.

The usual query fan-out still occurs, but this informs the conversational answer that’s alongside the product selection.

**Key takeaways**:

- ChatGPT runs two sets of fan-out queries for responses with product carousels. The first are contextual, used for forming the written part of the answer. The second are Google Shopping searches, where ChatGPT corrects for these results.
- Brands in ecommerce should focus on optimizing for Google Shopping first and foremost. Products that rank highly here are very likely to be included in any ChatGPT Shopping recommendations.

## How We Ran Our ChatGPT Shopping Experiment

We set out to deep dive into the fan-out queries that shape the final answers, testing first whether ChatGPT is creating these shopping queries, and then whether the resulting products matched.

Therefore the first step was to peek behind the curtain at the fan-out queries taking place.

### Step 1: Asking ChatGPT for Product Recommendations

We logged in to ChatGPT and simply asked for product suggestions with some defined criteria. The aim here is to engage with the platform as a user would and give some guidelines for the resulting products.

In this example, we used: “best budget Android phones with great cameras”.

### Step 2: Finding the Fan-Out Queries

You can use a solution like Semrush Enterprise AIO to automatically identify these hidden background searches, but it’s also possible using Chrome Dev Tools. Here’s what to do:

- Open Chrome Dev Tools
- On the Network tab > Fetch/XHR, filter using the conversation URL that ChatGPT creates (the final part of the URL) starting with a number
- Hit the refresh button to reload the conversation and allow the results to be captured
- Use CMD+ F to search the dev tools panel for “search_model_queries”
- Here you’ll find the query fan outs under “queries”

In this case we have: "best budget Android phones with great cameras 2025" and "what defines a budget Android phone and which budget phones have good cameras 2024 2025".

### Step 3: Finding the Shopping Fan-Out Queries

Shopping fan-out queries are hidden with an additional layer of encoding.

This is a bit trickier, but they can be found using these steps:

- In the same file as before, search for “id_to_token_map”.
- Find the piece of text beside this that starts with “ey”. This is a piece of Base64 data that we’ll need to decode.
- Copy the complete snippet (in this example it was about 500 characters) without the beginning and ending quote marks.
- Paste the data into a free tool like
[Base64 Decode](https://www.base64decode.org/)to make it readable and reveal the shopping fan-out queries.

Here’s the result:

The most important element is after “query” where we see “cheap+android+smartphones+good+camera+2025”. This is the shopping fan-out query. Typically, you’ll see only 1-2 unique queries here.

### Step 4: Comparing the Results

Now we have all the information needed to compare results. Just enter the shopping fan-out query into Google Shopping. Remember to check that the locale-location settings match in ChatGPT and Google Shopping for accuracy.

Here’s what we saw for the Android phone example:

**Google Shopping**

**ChatGPT**

The first two entries are found in both Google Shopping and ChatGPT. **In fact the retailer, title, and price information match exactly. **

## The Results: Shopping Query Fan-Out Is ChatGPT’s Additional Search Layer

After running the experiment 100 times, we found that the top ChatGPT product was included in Google Shopping’s first 3 results 75% of the time. There was also substantial overlap with the second and third results.

### Why Does ChatGPT Use Google Shopping Results?

ChatGPT uses Google Shopping Results because they’re such a rich source of data. This isn’t just a selection of products, but a library that includes reviews and live pricing info. Products can be confidently recommended with the correct prices and retailers.

While ChatGPT is making efforts to move away from Google and Google Shopping (shown by the recent Etsy integration, as well as its new Shopping Research features), it can’t yet match this user experience. Google’s ecosystem is just too vast.

Accurate live pricing info is crucial, especially when prices can fluctuate at a moment’s notice during ecommerce events like Black Friday.

### What Does This Mean for Ecommerce Brands?

It means that ecommerce brands need to consider their shopping feeds and ensure that any product pages or listings that feed these are always up to date. Google Shopping is the most important of these, undoubtedly ChatGPT and other platforms are working to create their own.

For product queries in ChatGPT, the logic seems to be separated into: 1. Retrieving buyer-guide context and 2. Retrieving the products from Google Shopping.

Therefore right now, optimizing your Google Shopping results is one of the most important factors for appearing in the ChatGPT product carousel.

Additionally, brands need to prepare for the future. In-chat purchasing and agentic e-commerce are only going to continue to grow. Developments like [Google’s Universal Commerce Protocol (UCP)](https://developers.google.com/merchant/ucp) will streamline these processes.

We’re approaching a world where transactions happen directly inside the chat, without ever visiting your website.

### About the Experiment

This experiment was based on the fan-out queries of 100 prompts. Each prompt was run 5 times, with the most common top products in the carousel recorded to correct for the probabilistic nature of LLMs.

While this is a small sample size, it gives a clear starting point for AI shopping optimization. We’ll continue to examine shopping query fan-out with larger datasets to provide further insights.

You can run this test for yourself. While we used a logged in account, you may see different results depending on whether you’re logged in, have a free account, or have a paid account. This was seen in [similar ChatGPT and Google experiments](https://backlinko.com/chatgpt-using-google-search) we’ve conducted.

## Semrush Enterprise AI Optimization

[Semrush Enterprise AI Optimization](https://www.semrush.com/lp/enterprise-aio/en/?utm_source=blogcontent&utm_medium=blog&utm_campaign=research) lets brands track and optimize for thousands of prompts across all leading LLMs, with targeted analysis of ChatGPT and AI shopping placements.
