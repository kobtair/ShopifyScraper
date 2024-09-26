from shopify_scraper import scraper
import os
import pandas as pd


df = pd.read_csv('saddar.csv')


for index, row in df.iterrows():
    url = row['Website']
    directory = f'./scraped_data/{url.split("//")[1].split(".")[0]}'
    if not os.path.exists(directory):
        os.makedirs(directory)
    try:
        parents = scraper.get_products(url)
        parents['website'] = url
        parents["shop"] = row['Place Name']
        parents["address"] = row['Address']
        parents["phone"] = row['Phone Number']
        parents["Latitude"] = row['Latitude']
        parents["Longitude"] = row['Longitude']
        parents["Shop Rating"] = row['Average Rating']
        parents["Total Ratings"] = row['Total Ratings']
        parents.to_csv(f'{directory}/parents.csv', index=False)
        parents.to_json(f'{directory}/parents.json', orient='records')
        print('Parents: ', len(parents))


        # children = scraper.get_variants(parents)
        # children.to_csv(f'{directory}/children.csv', index=False)
        # print('Children: ', len(children))


        # images = scraper.get_images(parents)
        # images.to_csv(f'{directory}/images.csv', index=False)
        # print('Images: ', len(images))
    except Exception as e:
        print(e)
        os.rmdir(directory)
        continue


# for url in urls:
#     directory = f'./scraped_data/{url.split("//")[1].split(".")[0]}'
#     if not os.path.exists(directory):
#         os.makedirs(directory)
#     try:
#         parents = scraper.get_products(url)
#         parents.to_csv(f'{directory}/parents.csv', index=False)
#         print('Parents: ', len(parents))


#         # children = scraper.get_variants(parents)
#         # children.to_csv(f'{directory}/children.csv', index=False)
#         # print('Children: ', len(children))


#         # images = scraper.get_images(parents)
#         # images.to_csv(f'{directory}/images.csv', index=False)
#         # print('Images: ', len(images))
#     except Exception as e:
#         print(e)
#         os.rmdir(directory)
#         continue
