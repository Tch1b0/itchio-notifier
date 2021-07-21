# itchio-notifier

## Setting up
Replace `<telegram-token>` with your telegram bot-token.
Replace `<telegram-user-id>` with your `id` on telegram.
Replace `<itch.io-token>` with your itch.io API-token.
```
$ git pull https://github.com/Tch1b0/itchio-notifier
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