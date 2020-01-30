# -*- coding: utf-8 -*- 

from flask import Flask, render_template,redirect, url_for, send_from_directory, flash
from forms import MyForm

import pandas as pd
import xlrd
from pandas import read_excel


app = Flask(__name__, static_url_path='')
app.config['SECRET_KEY'] = '@11tahe89!'



@app.route('/', methods=['GET', 'POST'])
def importador():
    print('Entrou na rota')
    try:
        print('entrou no try')
        form = MyForm()
        a = ''
        url_ =''
        excecao_ = ''
        output_ =''
        
        if form.validate_on_submit():
            print('entrou no if da validação')
            url_ = form.url.data
            excecao_ = form.excecao.data
            output_ = form.output.data
            xlsx = pd.read_excel(url_) # abre o arquivo xlsx
            frame = pd.DataFrame(xlsx) # cria um dataframe geral do arquivo
            print(url_)
            print(excecao_)
            print(output_)

            arq_all = open (str(output_)+'Escala-geral.txt', 'a')
            
            print('abriu o arquivo txt')

            t1e = frame.loc[0, 'GRUPO1 E']
            t1s = frame.loc[0, 'GRUPO1 S']
            t2e = frame.loc[0, 'GRUPO2 E']
            t2s = frame.loc[0, 'GRUPO2 S']
            t3e = frame.loc[0, 'GRUPO3 E']
            t3s = frame.loc[0, 'GRUPO3 S']
            t4e = frame.loc[0, 'GRUPO4 E']
            t4s = frame.loc[0, 'GRUPO4 S']
            print('leu os grupos')
            print(frame.head())
            ida = frame.loc[0, 'ID A'].astype(int)
            idb = frame.loc[0, 'ID B'].astype(int)
            idc = frame.loc[0, 'ID C'].astype(int)
            print(ida, idb, idc)
            
            print('Leus ids')
            ano = frame.loc[0, 'ANO'].astype(int)
            mes = frame.loc[0, 'MÊS'].astype(int)
            print('depois dos frames')

            dia = 0
            for i in frame['GRUPO1'].dropna():
                print('Entrou no for grupo1')
                dia=dia+1
                if (i == 1):
                    arq_all.write ("INSERT INTO dia (id,data,descricao,entrada,nome,saida,escala) VALUES (nextval('dia_seq'),"+"'"+str(ano)+"-"+str(mes)+"-"+str(dia)+"','"+str(excecao_)+"',"+str(t1e)+"','Exceção',"+str(t1s)+","+str(ida)+");"+'\n')
                    
                    arq = open (str(output_)+'Grupo 1 mes-'+str(mes)+'.txt', 'a')
                    arq.write ("INSERT INTO dia (id,data,descricao,entrada,nome,saida,escala) VALUES (nextval('dia_seq'),"+"'"+str(ano)+"-"+str(mes)+"-"+str(dia)+"','"+str(excecao_)+"',"+str(t1e)+"','Exceção',"+str(t1s)+","+str(ida)+");"+'\n')
                    arq.close ()
                
                
                
                elif (i == 0):
                    arq_all.write ("INSERT INTO dia (id,data,descricao,entrada,nome,saida,escala) VALUES (nextval('dia_seq'),"+"'"+str(ano)+"-"+str(mes)+"-"+str(dia)+"','"+str(excecao_)+"','null','Exceção','null',"+str(ida)+");"+'\n')
                    
                    arq = open (str(output_)+'Grupo 1 mes-'+str(mes)+'.txt', 'a')
                    arq.write ("INSERT INTO dia (id,data,descricao,entrada,nome,saida,escala) VALUES (nextval('dia_seq'),"+"'"+str(ano)+"-"+str(mes)+"-"+str(dia)+"','"+str(excecao_)+"','null','Exceção','null',"+str(ida)+");"+'\n')
                    arq.close ()
            print('Arquivo criado com sucesso!!')

            dia=0
            for i in frame['GRUPO2'].dropna():
                print('Entrou no for grupo2')    
                dia=dia+1
                if (i == 1):
                    arq_all.write ("INSERT INTO dia (id,data,descricao,entrada,nome,saida,escala) VALUES (nextval('dia_seq'),"+"'"+str(ano)+"-"+str(mes)+"-"+str(dia)+"','"+str(excecao_)+"',"+str(t2e)+",'Exceção',"+str(t2s)+","+str(idb)+");"+'\n')

                    arq = open (str(output_)+'Grupo 2 mes-'+str(mes)+'.txt', 'a')
                    arq.write ("INSERT INTO dia (id,data,descricao,entrada,nome,saida,escala) VALUES (nextval('dia_seq'),"+"'"+str(ano)+"-"+str(mes)+"-"+str(dia)+"','"+str(excecao_)+"',"+str(t2e)+",'Exceção',"+str(t2s)+","+str(idb)+");"+'\n')
                    arq.close ()
                
                
                
                elif (i == 0):
                    arq_all.write ("INSERT INTO dia (id,data,descricao,entrada,nome,saida,escala) VALUES (nextval('dia_seq'),"+"'"+str(ano)+"-"+str(mes)+"-"+str(dia)+"','"+str(excecao_)+"','null','Exceção','null',"+str(ida)+");"+'\n')
                    
                    arq = open (str(output_)+'Grupo 2 mes-'+str(mes)+'.txt', 'a')
                    arq.write ("INSERT INTO dia (id,data,descricao,entrada,nome,saida,escala) VALUES (nextval('dia_seq'),"+"'"+str(ano)+"-"+str(mes)+"-"+str(dia)+"','"+str(excecao_)+"','null','Exceção','null',"+str(ida)+");"+'\n')
                    arq.close ()
            print('Arquivo criado com sucesso!!')

            dia=0
            for i in frame['GRUPO3'].dropna():
                print('Entrou no for grupo3')    
                dia=dia+1
                if (i == 1):
                    arq_all.write ("INSERT INTO dia (id,data,descricao,entrada,nome,saida,escala) VALUES (nextval('dia_seq'),"+"'"+str(ano)+"-"+str(mes)+"-"+str(dia)+"','"+str(excecao_)+"',"+str(t3e)+",'Exceção',"+str(t3s)+","+str(idc)+");"+'\n')

                    arq = open (str(output_)+'Grupo 3 mes-'+str(mes)+'.txt', 'a')
                    arq.write ("INSERT INTO dia (id,data,descricao,entrada,nome,saida,escala) VALUES (nextval('dia_seq'),"+"'"+str(ano)+"-"+str(mes)+"-"+str(dia)+"','"+str(excecao_)+"',"+str(t3e)+",'Exceção',"+str(t3s)+","+str(idc)+");"+'\n')
                    arq.close ()
                
               
                
                elif (i == 0):
                    arq_all.write ("INSERT INTO dia (id,data,descricao,entrada,nome,saida,escala) VALUES (nextval('dia_seq'),"+"'"+str(ano)+"-"+str(mes)+"-"+str(dia)+"','"+str(excecao_)+"','null','Exceção','null',"+str(ida)+");"+'\n')
                    
                    arq = open (str(output_)+'Grupo 3 mes-'+str(mes)+'.txt', 'a')
                    arq.write ("INSERT INTO dia (id,data,descricao,entrada,nome,saida,escala) VALUES (nextval('dia_seq'),"+"'"+str(ano)+"-"+str(mes)+"-"+str(dia)+"','"+str(excecao_)+"','null','Exceção','null',"+str(ida)+");"+'\n')
                    arq.close ()
            print('Arquivo criado com sucesso!!')

            dia=0
            for i in frame['GRUPO4'].dropna():
                print('Entrou no for grupo4')    
                dia=dia+1
                if (i == 1):
                    arq_all.write ("INSERT INTO dia (id,data,descricao,entrada,nome,saida,escala) VALUES (nextval('dia_seq'),"+"'"+str(ano)+"-"+str(mes)+"-"+str(dia)+"','"+str(excecao_)+"',"+str(t4e)+",'Exceção',"+str(t4s)+","+str(ida)+");"+'\n')

                    arq = open (str(output_)+'Grupo 4 mes-'+str(mes)+'.txt', 'a')
                    arq.write ("INSERT INTO dia (id,data,descricao,entrada,nome,saida,escala) VALUES (nextval('dia_seq'),"+"'"+str(ano)+"-"+str(mes)+"-"+str(dia)+"','"+str(excecao_)+"',"+str(t4e)+",'Exceção',"+str(t4s)+","+str(ida)+");"+'\n')
                    arq.close ()
                
                
                
                elif (i == 0):
                    arq_all.write ("INSERT INTO dia (id,data,descricao,entrada,nome,saida,escala) VALUES (nextval('dia_seq'),"+"'"+str(ano)+"-"+str(mes)+"-"+str(dia)+"','"+str(excecao_)+"','null','Exceção','null',"+str(ida)+");"+'\n')
                    
                    arq = open (str(output_)+'Grupo 4 mes-'+str(mes)+'.txt', 'a')
                    arq.write ("INSERT INTO dia (id,data,descricao,entrada,nome,saida,escala) VALUES (nextval('dia_seq'),"+"'"+str(ano)+"-"+str(mes)+"-"+str(dia)+"','"+str(excecao_)+"','null','Exceção','null',"+str(ida)+");"+'\n')
                    arq.close ()
            print('Arquivo criado com sucesso!!')

                
            arq_all.close()
            print('Arquivo criado com sucesso!!')
            flash('Arquivos gerados com sucesso!', "alert-success")
    except:
        flash('Falha ao gerar os arquivos!', 'error')

    return render_template('home.html', form=form)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port= 8083, debug=True)