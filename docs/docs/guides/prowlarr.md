# Prowlarr

This is a relatively simple guide to setting up Prowlarr on your home portal. This guide assumes you have already setup your home portal and have a working instance of Prowlarr running on your network.

## 0. Install the media category

There are a few apps that fall under the media category. To install the media category, run the following command:

NOTE: You should only run this command if you have not already installed the media category.

```bash
./scripts/media.sh
```

## 1. Integrate prowlarr with the home portal

To integrate prowlarr with the home portal, you will need to run the following script:

```bash
./scripts/prowlarr.sh
```

And that is it, the script will ask for your link to prowlarr and setup a redirect to it via the home portal.
