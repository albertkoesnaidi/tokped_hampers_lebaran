import requests
import json
import pandas as pd

url = 'https://gql.tokopedia.com/graphql/SearchProductQueryV4'
# payload = [{'operationName': "SearchProductQueryV4",
#             'variables': {
#                 'params':f"device=desktop&navsource=&ob=23&page=0&q=hampers%20lebaran&related=true&rows=60&safe_search=false&scheme=https&shipping=&source=search&srp_component_id=01.07.00.00&srp_page_id=&srp_page_title=&st=product&start=0&topads_bucket=true&unique_id=f26e9e1aceba5cf83c8c3a87796f09d7&user_addressId=112724953&user_cityId=252&user_districtId=3526&user_id=34305312&user_lat=-7.260598599999998&user_long=112.7838025&user_postCode=60115&user_warehouseId=0&variants="
#             },
#             'query':"query SearchProductQueryV4($params: String!) {\n  ace_search_product_v4(params: $params) {\n    header {\n      totalData\n      totalDataText\n      processTime\n      responseCode\n      errorMessage\n      additionalParams\n      keywordProcess\n      componentId\n      __typename\n    }\n    data {\n      banner {\n        position\n        text\n        imageUrl\n        url\n        componentId\n        trackingOption\n        __typename\n      }\n      backendFilters\n      isQuerySafe\n      ticker {\n        text\n        query\n        typeId\n        componentId\n        trackingOption\n        __typename\n      }\n      redirection {\n        redirectUrl\n        departmentId\n        __typename\n      }\n      related {\n        position\n        trackingOption\n        relatedKeyword\n        otherRelated {\n          keyword\n          url\n          product {\n            id\n            name\n            price\n            imageUrl\n            rating\n            countReview\n            url\n            priceStr\n            wishlist\n            shop {\n              city\n              isOfficial\n              isPowerBadge\n              __typename\n            }\n            ads {\n              adsId: id\n              productClickUrl\n              productWishlistUrl\n              shopClickUrl\n              productViewUrl\n              __typename\n            }\n            badges {\n              title\n              imageUrl\n              show\n              __typename\n            }\n            ratingAverage\n            labelGroups {\n              position\n              type\n              title\n              url\n              __typename\n            }\n            componentId\n            __typename\n          }\n          componentId\n          __typename\n        }\n        __typename\n      }\n      suggestion {\n        currentKeyword\n        suggestion\n        suggestionCount\n        instead\n        insteadCount\n        query\n        text\n        componentId\n        trackingOption\n        __typename\n      }\n      products {\n        id\n        name\n        ads {\n          adsId: id\n          productClickUrl\n          productWishlistUrl\n          productViewUrl\n          __typename\n        }\n        badges {\n          title\n          imageUrl\n          show\n          __typename\n        }\n        category: departmentId\n        categoryBreadcrumb\n        categoryId\n        categoryName\n        countReview\n        customVideoURL\n        discountPercentage\n        gaKey\n        imageUrl\n        labelGroups {\n          position\n          title\n          type\n          url\n          __typename\n        }\n        originalPrice\n        price\n        priceRange\n        rating\n        ratingAverage\n        shop {\n          shopId: id\n          name\n          url\n          city\n          isOfficial\n          isPowerBadge\n          __typename\n        }\n        url\n        wishlist\n        sourceEngine: source_engine\n        __typename\n      }\n      violation {\n        headerText\n        descriptionText\n        imageURL\n        ctaURL\n        ctaApplink\n        buttonText\n        buttonType\n        __typename\n      }\n      __typename\n    }\n    __typename\n  }\n}\n"
# }]

# req = requests.post(url, json=payload).json()
# rows = req[0]['data']['ace_search_product_v4']['data']['products']
# print(rows[0])
# for i in range(5):
#     print(i, rows[i]['name'])

def get_params():
    params=["device=desktop&navsource=&ob=23&page=0&q=hampers%20lebaran&related=true&rows=60&safe_search=false&scheme=https&shipping=&source=search&srp_component_id=01.07.00.00&srp_page_id=&srp_page_title=&st=product&start=0&topads_bucket=true&unique_id=f26e9e1aceba5cf83c8c3a87796f09d7&user_addressId=112724953&user_cityId=252&user_districtId=3526&user_id=34305312&user_lat=-7.260598599999998&user_long=112.7838025&user_postCode=60115&user_warehouseId=0&variants="]
    for i in range(1,101):
        param=f"device=desktop&navsource=&ob=23&page={i}&q=hampers%20lebaran&related=true&rows=60&safe_search=false&scheme=https&shipping=&source=search&srp_component_id=01.07.00.00&srp_page_id=&srp_page_title=&st=product&start={(i-1)*60}&topads_bucket=true&unique_id=f26e9e1aceba5cf83c8c3a87796f09d7&user_addressId=112724953&user_cityId=252&user_districtId=3526&user_id=34305312&user_lat=-7.260598599999998&user_long=112.7838025&user_postCode=60115&user_warehouseId=0&variants="
        params.append(param)
    return params

def scrape_data(param):
    payload = [{'operationName': "SearchProductQueryV4",
            'variables': {
                'params':param
            },
            'query':"query SearchProductQueryV4($params: String!) {\n  ace_search_product_v4(params: $params) {\n    header {\n      totalData\n      totalDataText\n      processTime\n      responseCode\n      errorMessage\n      additionalParams\n      keywordProcess\n      componentId\n      __typename\n    }\n    data {\n      banner {\n        position\n        text\n        imageUrl\n        url\n        componentId\n        trackingOption\n        __typename\n      }\n      backendFilters\n      isQuerySafe\n      ticker {\n        text\n        query\n        typeId\n        componentId\n        trackingOption\n        __typename\n      }\n      redirection {\n        redirectUrl\n        departmentId\n        __typename\n      }\n      related {\n        position\n        trackingOption\n        relatedKeyword\n        otherRelated {\n          keyword\n          url\n          product {\n            id\n            name\n            price\n            imageUrl\n            rating\n            countReview\n            url\n            priceStr\n            wishlist\n            shop {\n              city\n              isOfficial\n              isPowerBadge\n              __typename\n            }\n            ads {\n              adsId: id\n              productClickUrl\n              productWishlistUrl\n              shopClickUrl\n              productViewUrl\n              __typename\n            }\n            badges {\n              title\n              imageUrl\n              show\n              __typename\n            }\n            ratingAverage\n            labelGroups {\n              position\n              type\n              title\n              url\n              __typename\n            }\n            componentId\n            __typename\n          }\n          componentId\n          __typename\n        }\n        __typename\n      }\n      suggestion {\n        currentKeyword\n        suggestion\n        suggestionCount\n        instead\n        insteadCount\n        query\n        text\n        componentId\n        trackingOption\n        __typename\n      }\n      products {\n        id\n        name\n        ads {\n          adsId: id\n          productClickUrl\n          productWishlistUrl\n          productViewUrl\n          __typename\n        }\n        badges {\n          title\n          imageUrl\n          show\n          __typename\n        }\n        category: departmentId\n        categoryBreadcrumb\n        categoryId\n        categoryName\n        countReview\n        customVideoURL\n        discountPercentage\n        gaKey\n        imageUrl\n        labelGroups {\n          position\n          title\n          type\n          url\n          __typename\n        }\n        originalPrice\n        price\n        priceRange\n        rating\n        ratingAverage\n        shop {\n          shopId: id\n          name\n          url\n          city\n          isOfficial\n          isPowerBadge\n          __typename\n        }\n        url\n        wishlist\n        sourceEngine: source_engine\n        __typename\n      }\n      violation {\n        headerText\n        descriptionText\n        imageURL\n        ctaURL\n        ctaApplink\n        buttonText\n        buttonType\n        __typename\n      }\n      __typename\n    }\n    __typename\n  }\n}\n"
}]
    req = requests.post(url, json=payload).json()
    rows = req[0]['data']['ace_search_product_v4']['data']['products']
    sc_data=[]
    # for i in range(0,len(rows)):
    for i in range(0,len(rows)):
        nama_produk = rows[i]['name']
        if len(rows[i]['badges'])>0:
            badges = rows[i]['badges'][0]['title']
        else:
            badges = 'No Badges'
        count_rating = rows[i]['countReview']
        disc_percent = rows[i]['discountPercentage']
        harga = rows[i]['price']
        rating = rows[i]['rating']
        rating_avg = rows[i]['ratingAverage']
        nama_toko = rows[i]['shop']['name']
        lokasi = rows[i]['shop']['city']
        official = rows[i]['shop']['isOfficial']
        powerbadge = rows[i]['shop']['isPowerBadge']
        temp=[]
        for j in rows[i]['labelGroups']:
            temp.append(j['title'])
        sc_data.append((nama_produk, badges,count_rating, disc_percent, harga, rating, rating_avg, nama_toko, lokasi, official, powerbadge, temp))

    return sc_data
    


if __name__ == '__main__':
    params = get_params()
    data_fin = []
    for i in range(0, len(params)):
        param = params[i]
        data = scrape_data(param)
        data_fin.extend(data)
    df= pd.DataFrame(data=data_fin, columns=['nama_produk', 'badges', 'count_rating', 'disc_percent','harga', 'rating', 'rating_avg', 'nama_toko', 'lokasi', 'official', 'powerbadge', 'list_labelGroups'])
    df.to_csv('hampers_lebaran_tokpret.csv', index=False)



#name, badges[0][title], count_review, discount_Percentage, labelGroups[0][title], price, rating, ratingAverage, shop[0][name], shop[0]['city], shop[0][isOfficial], shop[0], isPowerBadge
#whislist