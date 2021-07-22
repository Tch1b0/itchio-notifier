# itchio-notifier

## Purpose
This telegram bot notifies you **every day** at the same time(or on command) about your current games and their analytics.

## Adjustments
Currently, the bot notifies the User at **9 AM CEST**.<br>
I am planning to let the User be able to change that.  

## Setting up
Replace `<telegram-token>` with your telegram bot-token.
Replace `<telegram-user-id>` with your `id` on telegram.
Replace `<itch.io-token>` with your itch.io API-token.
```
$ git clone https://github.com/Tch1b0/itchio-notifier
```
```
$ cd itchio-notifier
```
```
$ echo <telegram-token> > token/telegram.txt
```
```
$ echo <telegram-user-id> > token/telegram-id.txt
```
```
$ echo <itch.io-token> > token/itchio.txt
```
```
$ docker-compose up -d
```

## Requirements
* docker