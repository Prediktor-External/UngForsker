import os
import pandas as pd

def main():
    # ÅPNE SOLDATA I PANDAS
    datagrunnlagsmappen = os.chdir('../datagrunnlag')
    soldata_fil = os.path.join(os.getcwd(), 'hIrr.txt')
    soldata_innhold = pd.read_csv(soldata_fil)

    # Lag et navn på kolonne 1
    soldata_innhold.columns = ['w_pr_m2']

    # Lag en ny kolonne med W for alle 1000 kvadratmeterne
    soldata_innhold['totalt_w'] = soldata_innhold['w_pr_m2'] * 1000

    # Lag en rad med antall timer siden 0
    import math
    soldata_innhold['time'] = [int(math.floor(i / 10)) for i in range(0,719)]

    # Gjennomsnittlig produksjon pr time
    gjennomsnitt = soldata_innhold.groupby(by='time').mean()

    print(gjennomsnitt)


if __name__ == "__main__":
    main()
