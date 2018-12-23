# Slick

**Easy to use secure file sending**

Slick makes it easy to send files or chat between two people. It is end-to-end encrypted, and uses HTTPS as its transport.

## Installation

Using python 3.7, run:

`pip install slick-app`

## Usage

To start slick, run `sk`. Running `/help` you'll get:

```
/list           -- show active friends and nearby people
/add  [subject] -- add a person
/talk [subject] -- talk to someone
/end            -- stop talking to someone
/quit           -- quit the program
/send           -- send a file
/get            -- get a file
/info
```

### Adding a friend

To add a friend, use the `/add` command. They will need to approve the request on their side by adding you back.

### Interacting with a friend

To interact with a specific friend, use `/talk [name]`

### Chatting

Once you're interacting with a friend, anything you type without a leading slash will be interpretted as chatting.

### Sending a file

To send a file, use `/send`

### Receiving a file

To receive a file, use `/get #`

## Design

Slick uses multicast DNS to broadcast a) a digest of the certificate used by HTTPS b) a tor service to facilitate the initial key exchange.