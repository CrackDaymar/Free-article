import pandas as pd

filename = 'Таблица существующих артикулов с наименованиями.xlsx'

def take_xmlx():
    xl = pd.ExcelFile(filename)
    return xl.parse('Articul')

def take_sheets():
    xl = pd.ExcelFile(filename)
    return xl.sheet_names

def main():
    all_df = take_xmlx()  # Получаем все вкладки в таблице
    new_list = []
    design_list = []
    for line in all_df.values:
        pass
        try:
            if str(line[0][3]) == '-':
                new_list.append(line[0:2])
                string = line[1]
                start = string.find('"')
                end = string.find('"', start+1)
                if start != (-1):
                    design_list.append([line[0], line[0][0:4] , line[1], string[end:]])
                # for word in words:
                #     if word[0] == '"':
                #         design_list.append([line[0][5:-1], word])
        except:
            pass
    print(design_list)
    Data = pd.DataFrame(design_list)
    #Data.to_csv('Наименование + артикул для 4-х значных данных.csv')
    Data.to_excel(excel_writer='Таблица заготовок.xlsx')




if __name__ == '__main__':
    main()
