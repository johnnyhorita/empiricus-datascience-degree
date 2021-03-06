# Bibliotecas
import pandas as pd
import numpy as np
from datetime import datetime
from dateutil.relativedelta import relativedelta
import math


##########################################################################################################################################

class RFCalculadora:
    """
    Calculadora de Renda Fixa
        A biblioteca esta em fase de desenvolvimento e aperfeiçoamento constante.
        No momento apenas o cálculo de NTN-F com pagamentos semestrais esta funcional.
    
    Variaveis
        df_feriado: dataFrame com feriados da Anbima
    
    Métodos
        Carrega_Feriados(caminho_arquivo)
        Método para carregar a planilha de feriados da Anbima
        
        Calcula_Prazo(dt_ini, dt_fim, convencao)
        Método para calcular dias entre a data inicial e a data final
        
        Calcula_Cupom(vl_nominal, tx_valor):
        Método para calcular o valor do cupom
        
        Data_Util(dt):
        Método para verificar se a data é uma data de dia útil
        
        Constroi_Fluxo(dt_entrada, dt_vencimento, vl_nominal, tx_rendimento, tx_valor, qt_prazo_fluxo, D1=1)
        Método para construção do fluxo de pagamentos 
        
        Calcula_Valor_Presente(vl, tx_rendimento, qt_dias_prazo):
        Método para calcular o valor presente

        Calcula_PU_LTN(dt_entrada, dt_vencimento, vl_nominal, tx_rendimento, D1=1):
        Método para calcular o valor do PU do LTN, o valor presente do Título e apresenta 
        o pagamento no vencimento
        
        Calcula_PU_NTNF(dt_entrada, dt_vencimento, vl_nominal, tx_rendimento, D1=1)
        Método para calcular o valor do PU do NTN-F, o valor presente do Título e apresenta 
        o fluxo de pagamentos semestrais
        
        Calcula_Taxa_Rendimento(vl_PU, qt_dias_prazo, vl_base=1000)
        Método para calculo da taxa de rendimento        
    
    Exemplo
        >>> objeto = RFCalculadora()
    """
    
    # Variáveis
    # Dataframe com os feriados da Anbima
    df_feriado = pd.DataFrame()
    
    # criando o método construtor
    #def __init__(self):
    #    # cria variável (atributo) dentro do objeto
    #    self.caminho_arquivo = arquivo

##########################################################################################################################################

    def Carrega_Feriados(self, caminho_arquivo):
        """
        Método para carregar a planilha de feriados da Anbima
        
        Parametro
            caminho_arquivo (string)
            Definição do caminho da planilha de feriados nacionais do 
            padrão Anbima.
        
        Retorno
            dataFrame
            Retorna um dataFrame com os dados da planilha de feriados.
        
        Observação
            Este método só funciona com planilhas no padrão da Anbima.
        
        Exemplo
            >>> Carrega_Feriados(caminho_arquivo)
        """
        try:
            dff = pd.read_excel(caminho_arquivo)
            dff.dropna(inplace=True)
            dff['Data'] = pd.to_datetime(dff['Data'])
            dff.set_index('Data', inplace=True)
            print(f'DataFrame RFCalculadora.df_feriado carregado com successo.\n')
            RFCalculadora.df_feriado = dff

            return dff

        except Exception as exception:
            print("Exception: {}".format(type(exception).__name__))
            print("Exception message: {}".format(exception))


##########################################################################################################################################

    def Calcula_Prazo(self, dt_ini, dt_fim, convencao):
        """
        Método para calcular dias entre a data inicial e a data final

        Parametros
            dt_ini (datetime): "aaaa-mm-dd"
            Onde, aaaa = ano
                  mm = mes
                  dd = dia

            dt_fim (datetime): "aaaa-mm-dd"
            Onde, aaaa = ano
                  mm = mes
                  dd = dia
            
            convencao (string): "xx/999" 
            Onde, xx = indica a sigla para dias úteis (DU) ou dias corridos (DC)
                  999= indica base de dias 
                       base 360 dias para um ano quando pressupomos que todos os meses 
                       possuem 30 dias;
                       base 252 dias para um ano quando todos os meses possuem 21 dias úteis;

        Retorno
            int
            Quantidade de dias entre a data inicial e a data final

        Exemplo
            >>> Calcula_Prazo(dt_ini, dt_fim, convencao)
        """
        try:
            # Calcula a quantidade de dias úteis do período
            qtd_dias = np.busday_count(dt_ini, dt_fim)

            # Verifica a quantidade de feriados no período, consultando a planilha de feriados
            qtd_feriados = RFCalculadora.df_feriado.loc[dt_ini:dt_fim].shape[0]

            # Se a convencao for em dias uteis 
            if convencao[0:2].upper() == "DU":
                # Verifica a quantidade de datas de feriado que caem no final de semana
                qtd_fds = RFCalculadora.df_feriado.loc[dt_ini:dt_fim].index.weekday > 4

                # Calcula a quantidade de feriados com datas úteis
                qtd_feriados_uteis = qtd_feriados - np.count_nonzero(qtd_fds == True)

                # Calcula a quantidade de dias úteis retirando os feriados
                qtd_dias = qtd_dias - qtd_feriados_uteis

            elif convencao[0:2].upper() != "DC":
                raise ValueError('Convenção inválida! Os valores suportados são DU (Dias Úteis) ou DC (Dias Corridos)')

            return qtd_dias

        except Exception as exception:
            print("Exception: {}".format(type(exception).__name__))
            print("Exception message: {}".format(exception))


##########################################################################################################################################

# NTN-F 
# Durante o "período de vida" do título, o investidor receberá cupons semestrais que equivalem a uma taxa de 10,00% ao ano sobre o valor nominal do título (R$1.000,00).

    def Calcula_Cupom(self, vl_nominal, tx_valor):
        """
        Método para calcular o valor do cupom

        Parametros
            vl_nominal (float): 9.9
            
            tx_valor (float): 9.9
            Onde, 10 equivalem a uma taxa de 10,00 % ao ano sobre o valor nominal do título R$1.000,00, calculo NTN-F

        Retorno
            int
            Valor do cálculo do cupom

        Exemplo
            >>> Calcula_Cupom(vl_nominal, tx_valor)
        """
        try:
            vl_cupom = vl_nominal * ((1 + (tx_valor/100))**(1/2) - 1)
            return vl_cupom

        except Exception as exception:
            print("Exception: {}".format(type(exception).__name__))
            print("Exception message: {}".format(exception))


##########################################################################################################################################

    def Data_Util(self, dt):
        """
        Método para verificar se a data é uma data de dia útil

        Parametros
            dt (datetime): "aaaa-mm-dd"
            Onde, aaaa = ano
                  mm = mes
                  dd = dia

        Retorno
            Boolean
            True: Quando a data for um dia útil (Segunda, Terça, Quarta, Quinta, Sexta)
            False: Quando a data for um dia não útil (Sábado, Domingo e Feriados)

        Exemplo
            >>> Data_Util(dt)
        """
        try:
            # Verifica se a data é um feriado
            if len(RFCalculadora.df_feriado.loc[dt:dt]) > 0:
                return False
            elif dt.weekday() > 4:
                return False
            else:
                return True

        except Exception as exception:
            print("Exception: {}".format(type(exception).__name__))
            print("Exception message: {}".format(exception))


##########################################################################################################################################

    def Constroi_Fluxo(self, dt_entrada, dt_vencimento, vl_nominal, tx_rendimento, tx_valor, qt_prazo_fluxo, D1=1):
        """
        Método para construção do fluxo de pagamentos 

        Parametros
            dt_entrada (datetime): "aaaa-mm-dd"
            Onde, aaaa = ano
                  mm = mes
                  dd = dia

            dt_vencimento (datetime): "aaaa-mm-dd"
            Onde, aaaa = ano
                  mm = mes
                  dd = dia

            vl_nominal (float): 9.9

            tx_rendimento (float): 9.9
            
            tx_valor (float): 9.9
            Onde, 10 equivalem a uma taxa de 10,00 % ao ano sobre o valor nominal do título R$1.000,00, calculo NTN-F

            qt_prazo_fluxo (int): 99
            Onde, 0 indica que o fluxo de pagamento do cupom é no vencimento;
                  1 indica que o fluxo de pagamento do cupom é mensal;
                  6 indica que o fluxo de pagamento do cupom é semestral;
                  12 indica que o fluxo de pagamento do cupom é anual;

            D1 (int): 9
            Onde, 1 indica que as datas de pagamento do fluxo devem ser dias úteis;
                  0 indica que as datas de pagamento não serão tratadas como dias úteis;           

        Retorno 
            dataFrame
            Monta um fluxo de pagamento semestral iniciando pela data de compra até 
            a data do vencimento        

        Exemplo
            >>> Constroi_Fluxo(dt_entrada, dt_vencimento, vl_nominal, tx_rendimento, qt_prazo_fluxo, D1=1)
        """
        try:
            # A data da compra é a data efetiva do inicio do fluxo D+1
            # a data de entrada indica a data que a transação foi adquirida pelo cliente
            dt_compra = dt_entrada + relativedelta(days=1)

            # Se o parametro D1 for igual a 1 indica que a data de compra e de vencimento devem ser um dia útil
            if D1 == 1:
                convencao = "DU/252"
                # Adiciona 1 na data de compra até que seja um dia útil
                while not RFCalculadora.Data_Util(self, dt_compra):
                    dt_compra = dt_compra + relativedelta(days=1)

                # Adiciona 1 na data de vencimento até que seja um dia útil
                while not RFCalculadora.Data_Util(self, dt_vencimento):
                    dt_vencimento = dt_vencimento + relativedelta(days=1)
            else:
                convencao = "DC/360"

            # Cria dataframe para incluir os fluxos de pagamentos
            column_names = ["Tipo", "Data Entrada", "Data Compra", "Data Pagamento", "Dias"]
            dffx = pd.DataFrame(columns = column_names)
            
            # Define a primeira data do fluxo
            # Fluxo pagamento mensal
            if qt_prazo_fluxo == 1:
                dt_fluxo = dt_compra + relativedelta(months=qt_prazo_fluxo)
                dt_fluxo = "01/" + str(dt_fluxo.month) + "/" + str(dt_fluxo.year)
            # Fluxo pagamento semestral
            elif qt_prazo_fluxo == 6:
                # Define a primeira data do semestre
                if math.ceil(dt_compra.month/6) == 1:
                    dt_fluxo = "01/07/" + str(dt_compra.year)
                else:
                    dt_fluxo = "01/01/" + str(dt_compra.year + 1)
            # Fluxo pagamento anual
            elif qt_prazo_fluxo == 12:
                dt_fluxo = dt_compra + relativedelta(months=qt_prazo_fluxo)
                dt_fluxo = "01/01/" + str(dt_fluxo.year)

            # Fluxo pagamento no vencimento
            elif qt_prazo_fluxo == 0:
                # Função de cálculo de dias entre datas
                qtd_dias_uteis = RFCalculadora.Calcula_Prazo(self, dt_compra, dt_vencimento, convencao)

                # Fluxo de pagamento do cupom
                fluxo = {"Tipo": "Principal", "Data Entrada": dt_entrada.strftime("%d/%m/%Y"), "Data Compra": dt_compra.strftime("%d/%m/%Y"), "Data Pagamento": dt_vencimento.strftime("%d/%m/%Y"), "Dias": qtd_dias_uteis}
                dffx = dffx.append(fluxo, ignore_index = True)
                
                # Cálcula o valor presente do título
                dffx["VP"] = RFCalculadora.Calcula_Valor_Presente(self, vl_nominal, tx_rendimento, qtd_dias_uteis)
            
            # Fluxo de pagamentos até o vencimento
            if qt_prazo_fluxo != 0:
                dt_fluxo = datetime.strptime(dt_fluxo, '%d/%m/%Y').date()

                while dt_fluxo <= dt_vencimento:
                    dt_valida = dt_fluxo

                    # Verifica se o mês é igual a Janeiro, em caso positivo soma 1 no dia, pois o dia padrão é 1 (feriado).
                    if (dt_valida.month == 1 and D1 == 1):
                        dt_valida = dt_valida + relativedelta(days=1)

                    # Verifica se o primeiro dia do semestre não é dia útil, em caso positivo soma 1 no dia. 
                    while (dt_valida.weekday() > 4 and D1 == 1):
                        dt_valida = dt_valida + relativedelta(days=1)

                    # Função de cálculo de dias entre datas
                    qtd_dias_uteis = RFCalculadora.Calcula_Prazo(self, dt_compra, dt_valida, convencao)

                    # Fluxo de pagamento do cupom
                    fluxo = {"Tipo": "Cupom", "Data Entrada": dt_entrada.strftime("%d/%m/%Y"), "Data Compra": dt_compra.strftime("%d/%m/%Y"), "Data Pagamento": dt_valida.strftime("%d/%m/%Y"), "Dias": qtd_dias_uteis}
                    dffx = dffx.append(fluxo, ignore_index = True)

                    dt_fluxo = dt_fluxo + relativedelta(months=qt_prazo_fluxo)

                    # Cálcula o valor do cupom 
                    vl_cupom = RFCalculadora.Calcula_Cupom(self, vl_nominal, tx_valor)
                    vl_cupom = round(vl_cupom, 5)

                    # valor da taxa de rendimento
                    tx_rendimento = round(tx_rendimento, 4)            

                    # Cálcula o valor presente dos cupons a serem recebidos
                    dffx["VP"] = vl_cupom / ((1 + (tx_rendimento / 100)) ** (dffx["Dias"] / 252))
            
            return dffx

        except Exception as exception:
            print("Exception: {}".format(type(exception).__name__))
            print("Exception message: {}".format(exception))


##########################################################################################################################################

    def Calcula_Valor_Presente(self, vl, tx_rendimento, qt_dias_prazo):
        """
        Método para calcular o valor presente
        
        Parametros
            vl (float): 9.9
            
            tx_rendimento (float): 9.9

            qt_dias_prazo (int): 9

        Retorno 
            float        
            Calculo do valor presente

        Exemplo
            >>> Calcula_Valor_Presente(vl, tx_rendimento, qt_dias_prazo)
        """
        try:
            # Cálcula o valor presente
            vl_presente = (vl / ((1 + (tx_rendimento / 100)) ** (qt_dias_prazo / 252)))

            return vl_presente

        except Exception as exception:
            print("Exception: {}".format(type(exception).__name__))
            print("Exception message: {}".format(exception))



##########################################################################################################################################            
    def Calcula_PU_LTN(self, dt_entrada, dt_vencimento, vl_nominal, tx_rendimento, D1=1):
        """
        Método para calcular o valor do PU do LTN, o valor presente do Título e apresentar 
        o fluxo de pagamentos

        Parametros
            dt_entrada (datetime): "aaaa-mm-dd"
            Onde, aaaa = ano
                  mm = mes
                  dd = dia

            dt_vencimento (datetime): "aaaa-mm-dd"
            tipo = datetime
            Onde, aaaa = ano
                  mm = mes
                  dd = dia;

            vl_nominal (float): 9.9

            tx_rendimento (float): 9.9

            D1 (int): 1
            Onde, 1: indica que as datas de pagamento do fluxo devem ser dias úteis;
                  0: indica que as datas de pagamento não serão tratadas como dias úteis;

        Retorno
            dataFrame, float, float
            Retorna o fluxo de pagamento semestral iniciando pela data de compra até a data do vencimento,
            o Valor face do título e o Valor presente do título (PU)
            
        Exemplo
            >>> Calcula_PU_LTN(dt_entrada, dt_vencimento, vl_nominal, tx_rendimento, D1=1)
        """
        try:
            dt_entrada = datetime.strptime(dt_entrada, '%d/%m/%Y').date()
            dt_vencimento = datetime.strptime(dt_vencimento, '%d/%m/%Y').date()

            # A taxa é fixa 10.00 % para calculo de LTN
            tx_valor = 10 
            # Calcula o valor presente dos cupons a serem recebidos
            df_fluxo = RFCalculadora.Constroi_Fluxo(self, dt_entrada, dt_vencimento, vl_nominal, tx_rendimento, tx_valor, 0, D1)

            vl_principal = round(df_fluxo["VP"].iloc[-1], 6)
            vl_pu = round(vl_principal, 6)

            return df_fluxo, vl_principal, vl_pu

        except Exception as exception:
            print("Exception: {}".format(type(exception).__name__))
            print("Exception message: {}".format(exception))


           ##########################################################################################################################################            
    def Calcula_PU_NTNF(self, dt_entrada, dt_vencimento, vl_nominal, tx_rendimento, D1=1):
        """
        Método para calcular o valor do PU do NTN-F, o valor presente do Título e apresentar 
        o fluxo de pagamentos semestrais

        Parametros
            dt_entrada (datetime): "aaaa-mm-dd"
            Onde, aaaa = ano
                  mm = mes
                  dd = dia

            dt_vencimento (datetime): "aaaa-mm-dd"
            tipo = datetime
            Onde, aaaa = ano
                  mm = mes
                  dd = dia;

            vl_nominal (float): 9.9

            tx_rendimento (float): 9.9

            D1 (int): 1
            Onde, 1: indica que as datas de pagamento do fluxo devem ser dias úteis;
                  0: indica que as datas de pagamento não serão tratadas como dias úteis;

        Retorno
            dataFrame, float, float
            Retorna o fluxo de pagamento semestral iniciando pela data de compra até a data do vencimento,
            o Valor face do título e o Valor presente do título (PU)
            
        Exemplo
            >>> Calcula_PU_NTNF(dt_entrada, dt_vencimento, vl_nominal, tx_rendimento, D1=1)
        """
        try:
            dt_entrada = datetime.strptime(dt_entrada, '%d/%m/%Y').date()
            dt_vencimento = datetime.strptime(dt_vencimento, '%d/%m/%Y').date()

            # A taxa é fixa 10.00 % para calculo de NTN-F
            tx_valor = 10 
            # Calcula o valor presente dos cupons a serem recebidos
            df_fluxo = RFCalculadora.Constroi_Fluxo(self, dt_entrada, dt_vencimento, vl_nominal, tx_rendimento, tx_valor, 6, D1)

            # Calcula o valor presente do título (valor face)
            qt_dias_prazo = df_fluxo["Dias"].iloc[-1]
            vl_principal = RFCalculadora.Calcula_Valor_Presente(self, vl_nominal, tx_rendimento, qt_dias_prazo)
            vl_principal = round(vl_principal, 9)

            # Inclui o valor do principal no fluxo
            dt_e = df_fluxo["Data Entrada"].iloc[-1]
            dt_c = df_fluxo["Data Compra"].iloc[-1]
            dt_p = df_fluxo["Data Pagamento"].iloc[-1]
            du = df_fluxo["Dias"].iloc[-1]
            df_principal = {"Tipo": "Principal", "Data Entrada": dt_e, "Data Compra": dt_c, "Data Pagamento": dt_p, "Dias": du, "VP": vl_principal}
            df_fluxo = df_fluxo.append(df_principal, ignore_index = True)

            vl_pu_ntnf = df_fluxo["VP"].sum()        
            vl_pu_ntnf = round(vl_pu_ntnf, 6)

            return df_fluxo, vl_principal, vl_pu_ntnf

        except Exception as exception:
            print("Exception: {}".format(type(exception).__name__))
            print("Exception message: {}".format(exception))


##########################################################################################################################################

    def Calcula_Taxa_Rendimento(self, vl_PU, qt_dias_prazo, vl_base=1000):
        """
        Método para calculo da taxa de rendimento

        Parametros
            vl_PU (float): 9.9
            
            qt_dias_prazo (int): 9
            
            vl_base (int): 999
            Onde, 100 : base de cálculo para porcentagem 100 
                  1000: base de cálculo para porcentagem 1000

        Retorno
            float        
            Calculo da taxa de rendimento

        Exemplo
            >>> Calcula_Taxa_Rendimento(vl_PU, qt_dias_prazo, vl_base=1000)
            
        """
        try:
            vl_tx_anual = 0.0
            vl_tx_anual = ((vl_base / vl_PU) ** (252 / qt_dias_prazo)) - 1
            vl_tx_anual = round((vl_tx_anual * 100), 4)

            return vl_tx_anual

        except Exception as exception:
            print("Exception: {}".format(type(exception).__name__))
            print("Exception message: {}".format(exception))


##########################################################################################################################################
