# REACT3

## Create a Next.js App
  
  - To build a complete web application with React from scratch:
    - 1 -  Code has to be bundled using a bundler like webpack and transformed using a compiler like Babel.
    - 2 -  You need to do production optimizations such as code splitting.
    - 3 -  You might want to statically pre-render some pages for performance and SEO. You might also want to use server-side rendering or client-side rendering.
    - 4 -  You might have to write some server-side code to connect your React app to your data store.
  - Next.js has the best-in-class "Developer Experience" and many built-in features; a sample of them are:
    - 1 - An intuitive page-based routing system (with support for dynamic routes)
    - 2 - Pre-rendering, both static generation (SSG) and server-side rendering (SSR) are supported on a per-page basis
    - 3 - Automatic code splitting for faster page loads
    - 4 - Client-side routing with optimized prefetching
    - 5 - Built-in CSS and Sass support, and support for any CSS-in-JS library
    - 6 - Development environment with Fast Refresh support
    - 7 - API routes to build API endpoints with Serverless Functions
    - 8 - Fully extendable
    
---
## Why Next.js

Next.js is built on top of React – a frontend development library for building user interfaces, which is for most first choice when it comes to web applications.

**Server side rendering & static site generation with Next.js:**

Next.js became popular because it solved a problem that  many web developers used to have with web applications rendered on the client side (in the browser). Those Single Page Applications (SPAs) featured improved UX because they required no reloading from the user and provided additional interactivity.

Next.js provides an out-of-the-box solution for *server side rendering (SSR)* of React components. With Next.js, developers can render the JavaScript code on the server and send simple indexable HTML to the user. This wasn’t entirely impossible to do before Next.js appeared. But it required a lot of tweaking with issues related to caching, server load, on-demand content or the architecture of the application itself. It all took away from the time you could dedicate to the business logic of your application.

Next.js can also help you with static site generation (SSG) – another SEO friendly way of building websites and applications. In this case, rather than during runtime, your HTML is generated during build time. When the user requests a page, a pre-made static HTML page is sent to them. A website like this is very fast, but it’s not quite as suitable as SSR for interactive web applications that take a lot of user input, because it needs to be rebuilt every time new input is provided. As a result, it’s a better choice for simple applications (such as blogs) in which the content typically doesn’t change based on the user’s actions.


![](https://tsh.io/wp-content/uploads/2021/03/ssg-vs-ssr-mechanics-overview.png)