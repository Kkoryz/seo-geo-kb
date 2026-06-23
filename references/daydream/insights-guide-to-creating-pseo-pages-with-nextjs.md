---
title: "Guide to Creating pSEO Pages With Next.js"
source_url: https://www.withdaydream.com/library/insights/guide-to-creating-pseo-pages-with-nextjs
category: daydream
section: "Daydream — GEO library (how LLMs crawl & index)"
date: 2025-03-01
---

# Guide to Creating pSEO Pages With Next.js

Next.js, a React-based framework introduced in 2016, has quickly become one of the go-to solutions for building fast, scalable web applications. Widely adopted by developers and companies of all sizes, from startups to large enterprises, Next.js is known for its versatility and powerful features.

When it comes to building programmatic SEO (pSEO) engines, Next.js stands out as a top choice. Its ability to generate dynamic pages at scale, combined with its strong SEO capabilities, makes it ideal for projects that require high-output, SEO-focused content. In this guide, we’ll walk you through how to use Next.js to create scalable, SEO-optimized pages that automatically generate content based on your data.

## Benefits of Next.js for Building pSEO Pages

**Hybrid Static & Server Rendering**:

Next.js supports static generation and server-side rendering, ensuring your pages are fast and optimized for SEO.**Route Pre-fetching**:

Next.js automatically pre-fetches linked pages in the background, improving page load times and providing a smoother user experience.**No Configuration Needed**:

Next.js provides built-in SEO optimizations with minimal configuration, helping you focus on creating high-quality content.

## Steps to Build pSEO Pages with Next.js

Let’s walk through the steps of creating pSEO pages for the long-tail search query "Top Attractions in [City Name].”

### Step 1: Choose Your Data Source

Before you start coding, choosing the right data source for your project is essential. Each data source type has its advantages and limitations:

#### Static Data (JSON or YAML files)

Best for small datasets that don’t change frequently. Ideal for lists of cities or attractions that remain consistent over time. It's simple, fast, and easy to manage but lacks flexibility for dynamic content.

**☝🏼Use case:** If you are dealing with a small list of attractions in different cities that rarely change, static data is often sufficient and easy to manage.

#### CMS (Contentful, Sanity, Strapi)

Suitable for projects that require non-technical teams to manage content. CMS platforms are excellent if your content changes frequently or you need a user-friendly interface for managing data.

**☝🏼Use case:** If you have a team of content creators updating attraction information, CMSs provide an easy way for them to handle the data without developers needing to make updates.

#### Database (MySQL, MongoDB, PostgreSQL)

Ideal for large-scale, dynamic applications that need complex querying. A database is a powerful solution if you're dealing with massive datasets or require real-time updates.

**☝🏼Use case:** If you're building a large directory of attractions across cities and need to scale the content easily, a database might be your best option.

#### API (Public/Private APIs)

Best for real-time data or when you don’t want to store large datasets locally. APIs can fetch live data, which is useful for constantly changing or third-party-sourced content.

☝🏼**Use case: ** If the attraction data is constantly changing (e.g., user reviews or opening hours) or is pulled from third-party sources (like a tourism API), using an API makes the most sense.

For this guide, we'll use JSON data for simplicity. Here’s a sample JSON data structure for cities and attractions:

[

{ "city": "Paris", "attraction": "Eiffel Tower" },

{ "city": "New York", "attraction": "Statue of Liberty" },

{ "city": "Tokyo", "attraction": "Tokyo Tower" }

]

### Step 2: Create Dynamic Routes

Next.js allows you to create dynamic routes to generate pages based on your data. Create a new folder called city under the pages directory, and then create a file named [slug].js inside it: /pages/city/[slug].js

This file will serve as a template for generating dynamic city pages (e.g., city/new-york or city/paris).

Next, define the paths to generate at build time using getStaticPaths. Here’s how to do it with data fetched from the JSON file:

import cities from '../../data/cities.json';

export async function getStaticPaths() {

const paths = cities.map((city) => ({

params: { slug: city.city.toLowerCase().replace(/\s+/g, '-') },

}));

return { paths, fallback: false };

}

This code tells Next.js which paths to pre-render at build time based on the cities in the JSON file.

### Step 3: Fetch Data for Each Page

Once the dynamic routes are set up, we need to fetch the data for each individual page. Use getStaticProps to retrieve the specific city data based on the slug parameter:

import cities from '../../data/cities.json';

export async function getStaticProps({ params }) {const cityData = cities.find((city) => city.city.toLowerCase().replace(/\s+/g, '-') === params.slug);return { props: { cityData } };}

This fetches the data for the specific city (e.g., city/new-york or city/paris) based on the slug parameter passed to getStaticProps.

### Step 4: Build the Dynamic Page

After fetching the data, you can use it to render the page content dynamically. Here's an example of the CityPage component, which takes the cityData as a prop and displays it:

import Head from 'next/head';

export default function CityPage({ cityData }) {

return (

<div>

<Head>

<title>Visit {cityData.city} - Top Attraction</title>

<meta

name="description"

content={`Discover the top attraction in ${cityData.city}: ${cityData.attraction}. Plan your trip today!`}

/>

</Head>

<h1>Visit {cityData.city}</h1>

<p>Top attraction: {cityData.attraction}</p>

</div>

);

}

This template generates a unique page for each city, incorporating dynamic SEO elements like the title and meta description.

### Step 5: Deploy Your Site

Once everything is set up, you can deploy your site to a platform like Vercel, which integrates seamlessly with Next.js. Vercel will ensure your pages are optimized for speed and SEO.

## Work with Daydream to Create a pSEO Program with Next.js

Though Next.js provides a powerful foundation for building pSEO pages, launching a successful programmatic strategy requires significant effort and complex coordination with a variety of stakeholders — from content and SEO strategists to engineering and design teams.

If you’re looking for a partner to build and deploy your pSEO from start to finish, consider partnering with daydream. We work with some of the fastest-growing startups like Descript, Notion, and Tome to build and scale high-performing pSEO engines.

**Interested in getting started with programmatic SEO? Send a message to ****thenukak@withdaydream.com****. **
