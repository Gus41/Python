from datetime import datetime



if __name__ == '__main__':
    print("-----")
    data = datetime(2024,1,22) #yy/mm/ddp
    now = datetime.now()

    data_str = '2022-04-20'
    format_date = '%Y-%m-%d'
    date = datetime.strptime(data_str,format_date)
    print(date)
    


    print(now)
    print(data)