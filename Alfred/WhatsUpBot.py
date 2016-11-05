#!/usr/bin/env python3
"""
    WhatsUpBot Class Definition
    ---------------------------
    The WhatsUpBot is Alfred's interface to WhatsApp.
    It will correspond to a WhatsApp account that can communicate with users who ping it
    to query about the KT Residence's information.
    Essentially, it will have a list of phone numbers that are authorized to access it.
    (This is of utmost importance.)
    
    Planned Features:
    -----------------
    * Interface to the database.
    * Response to the keyword "WhatsUp", followed by certain commands:
        - ISBN
            Returns status in library.
        - Amazon<space>ISBN/ASIN
            Returns price list on Amazon and link to page.
        - RemindMe!<Space>Duration
            Will send a message about the reminder at scheduled time and date.
            Duration can be absolute as in (2016-11-29 00:00), or relative (2 days).
        - Manga<Space><Manga Title><Space><Chapter>
            Will first respond if successfully queried, then it will crawl my local manga collection for 
            the title, and if it doesn't find it there, it will try to scrape it off a list of manga sites.
            Then, it will prepare a PDF, save to local cache, and then upload the file to the user.
        - Manga?<Space><Manga Title>
            Will respond if the latest chapter is out or not.
        - Shopping
            Will return a list of items to be purchased.
        - Bring<Space><Items>
            Will add these items to a list, and then send a message to me or Sthuthi with the list.
        - Google<Space><Query>
            Will need to think about this. Should it return the scraped google page? Or should it just
            return the Google search query? I'm confused.
        - Snapshot<Space><Link>
            Will return a snapshot of a page.

"""

