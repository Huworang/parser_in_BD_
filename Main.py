
import time
from Mysql import Working_database
from Parsing import Parsing_web
from Data import urls, table_names_fields, tegs_table_4



def Main():
    
    big_parsing = Working_database()

    yes_no = input("Нужно ли создать/проверить таблицы? (y - проверить)\n")
    if yes_no == 'y': big_parsing.Create_db()

    #time.sleep(3600)

    url_metallportal = Parsing_web(urls[0])

    list_reference_resources = ["1", urls[0].split('/')[-2].split('.')[0], urls[0]]
    list_reference_resources.append(url_metallportal.Reference_resources(tegs_table_4[0]))
    big_parsing.Add_data("Справочник_ресурсов", list_reference_resources)

    time.sleep(3600)




    url_obrabotka = Parsing_web(urls[1])
    text = url_obrabotka.Reference_resources(tegs_table_4[1])

    url_partnerzakaz = Parsing_web(urls[2])
    text = url_partnerzakaz.Reference_resources(tegs_table_4[2])

    url_iprom = Parsing_web(urls[3])
    text = url_iprom.Reference_resources(tegs_table_4[3])

    url_metalloobrabotchiki = Parsing_web(urls[4])
    text = url_metalloobrabotchiki.Reference_resources(tegs_table_4[4])

    url_prom_market = Parsing_web(urls[5])
    text = url_prom_market.Reference_resources(tegs_table_4[5])
    
    

    print(text)
    time.sleep(3600)



    big_parsing.Close_connection()



   

    

if __name__ == '__main__':
    Main()


