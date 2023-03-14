import pandas as pd

def main():
    without_hypen = pd.read_csv('actual articles without hyphen.csv')
    with_hypen = pd.read_csv('actual articles with hyphen.csv')
    list = []
    print(with_hypen.loc(1))
    for i in range(0,len(with_hypen)):
        upload = False
        for j in range(0,len(without_hypen)):
            try:
                if with_hypen[i] == without_hypen[j]:
                    upload = True
            except:
                pass
        if upload == True:
            list.append(i)
    result_list = pd.DataFrame(list)
    result_list.to_csv('actual articles1.csv')


if __name__ == "__main__":
    main()