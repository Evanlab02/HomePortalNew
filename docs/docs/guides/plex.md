# Plex Media Server

This is a relatively simple guide to setting up Plex Media Server on your home portal. This guide assumes you have already setup your home portal and have a working instance of Plex Media Server running on your network.

## 0. Install the media category

There are a few apps that fall under the media category. To install the media category, run the following command:

NOTE: You should only run this command if you have not already installed the media category.

```bash
./scripts/media.sh
```

## 1. Integrate plex with the home portal

To integrate Plex with the home portal, you will need to run the following script:

```bash
./scripts/plex.sh
```

And that is it, the script will ask for your link to plex and setup a redirect to it via the home portal.
