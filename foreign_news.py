import os
import pandas as pd

foreignList=[
'adnkronos',
'Agence France-Presse',
'Al Jazeera',
'Anadolu Agency',
'Associated Press',
'BBC News',
'BBC NEWS',
'Belarusian Telegraph Agency',
'BelTA',
'Bernama',
'BERNAMA',
'Bloomberg',
'BLOOMBERG',
'Bloomberg News',
'CCTV News',
'CCTV5',
'broadcaster CCTV',
'CCTV News',
'China Central Television',
'Central News Agency',
'Deccan Herald',
'DECCAN HERALD',
'Der Spiegel',
'dpa',
'DPA',
'Emirates News Agency',
'Fars News Agency',
'Hindustan Times',
'HINDUSTAN TIMES',
'Indo-Asian News Service',
'Interfax',
'International Herald Tribune',
'International Herald Tribune/New',
'International Islamic News Agency',
'Islamic Republic News Agency',
'ITAR-TASS',
'Jiji Press',
'Korean Central News Agency',
'Korean Herald',
'Kyodo News',
'Mehr News Agency',
'MEHR news agency',
'Mehr news agency',
'Morning Herald',
'Philippine News Agency',
'Press Association',
'Press Trust of India',
'Qatar News Agency',
'Reuters',
'Reuters.',
'REUTERS',
'REUTERS:',
'REUTERS,',
'Reuters Health',
'RIA Novosti',
'Ria Novosti',
'RIA-Novosti',
'Rodong Sinmun',
'SaPa',
'SAPA',
'Saudi Press Agency',
'The Canadian Press',
'The Guardian',
'-The Guardian',
'theguardian.com',
'the Guardian',
'Belfast Telegraph',
'TELEGRAPH',
'Daily Telegraph',
'DAILY TELEGRAPH',
'Telegraph.co.uk',
'telegraph.co.uk',
'Telegraph)',
'Sunday Telegraph',
'SUNDAY TELEGRAPH',
'The Telegraph)',
'The Telegraph ##',
'The Telegraph reported',
'The Telegraph UK',
'Independent ==',
'The Independent),',
'Times of India',
'United News of India',
'Xinhua',
'Xinhua News Agency',
'Xinhua news agency',
'Yonhap',
'Yonhap News Agency',
'Zee News',
'Zee.news',
'ZEE NEWS',
'Zee News',
'AAP',
'AFP',
'ANI',
'BBC',
'CNN',
'CP',
'DPA',
'IANS',
'ICC',
'KCNA',
'MTI',
'ndtv',
'NDTV',
'PTI',
'TASS',
'UNI',
'XINHUA',
'YONHAP',
'WION']

dir_path = r'dn_dataset'
csvfile = open("Removed_DN_files.csv", "w")


count=0
# iterate each file in a directory
for file in os.listdir(dir_path):
    cur_path = os.path.join(dir_path, file)
    # check if it is a file
    if os.path.isfile(cur_path):
        with open(cur_path, 'r') as file:
            # read all content of a file and search string
            fileContent = file.read()
            if [ele for ele in foreignList if(ele in fileContent)]:
#             if foreignList in file.read():
                count += 1
                csvfile.write(cur_path+", "+"\n")
                file.close()
                os.remove(cur_path)
                print('Removed article  : ',cur_path)
                print(count)
            else:
                file.close(
