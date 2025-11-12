from filestack import Client
client = Client('AylAk2NYkTz2r5mA8Nkjfz')

new_filelink = client.upload(filepath='sample.txt')
print(new_filelink.url)
