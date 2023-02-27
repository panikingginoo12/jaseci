"""Built in actions for Jaseci"""
from fastapi import HTTPException
from jaseci.actions.live_actions import jaseci_action
from urllib.parse import urldefrag
import metadata_parser


@jaseci_action()
def get_page_meta(url: str = ""):
    """
    Util to parse metadata out of urls and html documents
    """

    if url == "":
        raise HTTPException(status_code=400, detail=str("No url provided"))
    
    defraged_url = urldefrag(url)    

    try:
        page = metadata_parser.MetadataParser(
            url=defraged_url.url,
            url_headers={
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:94.0) Gecko/20100101 Firefox/94.0",
            },
        )
        return page.metadata
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
