

from __future__ import annotations

import aiohttp
from attr import dataclass
from bs4 import BeautifulSoup, Tag
from fastapi import FastAPI

app = FastAPI()


@dataclass(slots=True, frozen=True)
class EbayItem:
    title: str
    subtitle: str
    state: str
    price: str
    bids: str
    logistic_cost: str
    location: str

    @classmethod
    def from_tag(cls, tag: Tag) -> EbayItem:

        title = tag.find('div', 's-item__title').string
        subtitle = tag.find('div', 's-item__subtitle').find('span').string
        # state = tag.find('div', 's-item__subtitle')
        price = tag.find('span', 's-item__price').string
        logistic_cost = tag.find('span', 's-item__shipping s-item__logisticsCost').string
        location = tag.find('span', 's-item__location s-item__itemLocation').string

        return cls(title, subtitle, None, price, None, logistic_cost, location)


@dataclass(slots=True, frozen=True)
class WallapopItem:
    title: str
    description: str
    price: str

    @classmethod
    def from_tag(cls, tag: Tag) -> WallapopItem:

        title = tag.find('span', 'product-info-title').string
        description = tag.find('p', 'product-info-description').string
        price = tag.find('span', 'product-info-price').string

        return cls(title, description, price)


async def fetch_ebay_search_url(http: aiohttp.ClientSession, url: str):

    async with await http.get('https://www.ebay.es/sch/i.html?_from=R40&_trksid=p2380057.m570.l1313&_nkw=kinesis&_sacat=0') as response:

        thing = await response.text()

        soup = BeautifulSoup(thing, 'lxml')

        items = soup.find_all('div', 's-item__info clearfix')

        for item in items[1:]:
            try:

                print(EbayItem.from_tag(item))

            except AttributeError:
                print('Error in one')

            print()


async def fetch_wallapop_search_url(http: aiohttp.ClientSession, url: str):

    async with await http.get('https://es.wallapop.com/motos') as response:

        # async with await http.get('https://es.wallapop.com/app/search?keywords=kinesis'
        #                           '&filters_source=search_box'
        #                           '&longitude=-3.69196&latitude=40.41956') as response:
        thing = await response.text()

        soup = BeautifulSoup(thing, 'lxml')

        items = soup.find_all('div', 'card js-masonry-item card-product product')

        for item in items:
            try:

                print(WallapopItem.from_tag(item))

            except AttributeError:
                print('Error in one')

            print()


@app.get('/')
async def root():

    async def search():

        async with aiohttp.ClientSession() as http:

            # await fetch_ebay_searched_url(http, 'fck me')
            await fetch_wallapop_search_url(http, 'fck me')

            return {'response': 'yea'}

    # loop = asyncio.new_event_loop()
    # asyncio.set_event_loop(loop)
    # json = asyncio.ensure_future(search())
    # print(type(json))
    # json = 'yes'

    # return {'Are we on business': 'Yas',
    #         'thing': json}

    return await search()
