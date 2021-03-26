# Heroku

Heroku lets you deploy, run and manage applications written in Ruby, Node.js, Java, Python, Clojure, Scala, Go and PHP.


Dependency mechanisms vary across languages: in Ruby you use a Gemfile, in Python a requirements.txt, in Node.js a package.json, in Java a pom.xml and so on.

## Building applications

When the Heroku platform receives the application source, it initiates a build of the source application. The build mechanism is typically language specific, but follows the same pattern, typically retrieving the specified dependencies, and creating any necessary assets (whether as simple as processing style sheets or as complex as compiling code).


## Running applications on dynos

Heroku executes applications by running a command you specified in the Procfile, on a dyno that’s been preloaded with your prepared slug (in fact, with your release, which extends your slug and a few items not yet defined: config vars and add-ons).


## Config vars

`heroku config:set ENCRYPTION_KEY=my_secret_launch_codes`
An application’s configuration is everything that is likely to vary between environments (staging, production, developer environments, etc.). This includes backing services such as databases, credentials, or environment variables that provide some specific information to your application.

## Add-ons
Applications typically make use of add-ons to provide backing services such as databases, queueing & caching systems, storage, email services and more. Add-ons are provided as services by Heroku and third parties - there’s a large marketplace of add-ons you can choose from.