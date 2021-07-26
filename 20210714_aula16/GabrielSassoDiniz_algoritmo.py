#importando toda data:

data = [[66707599984, 'Conservador', (5100, 3500, 1400, 200)],
 [55695397315, 'Conservador', (4900, 3000, 1400, 200)],
 [63743886918, 'Conservador', (4700., 3200., 1300., 200.)],
 [55941368774, 'Conservador', (4600., 3100., 1500., 200.)],
 [75486280874, 'Conservador', (5000., 3600., 1400., 200.)],
 [53164949799, 'Conservador', (5400., 3900., 1700., 400.)],
 [39898704131, 'Conservador', (4600., 3400., 1400., 300.)],
 [53740901207, 'Conservador', (5000., 3400., 1500., 200.)],
 [51735950236, 'Conservador', (4400., 2900., 1400., 200.)],
 [47305108951, 'Conservador', (4900., 3100., 1500., 100.)],
 [63858864633, 'Conservador', (5400., 3700., 1500., 200.)],
 [53363167240, 'Conservador', (4800., 3400., 1600., 200.)],
 [72133754195, 'Conservador', (4800., 3000., 1400., 100.)],
 [52802483512, 'Conservador', (4300., 3000., 1100., 100.)],
 [57925287214, 'Conservador', (4800., 3400., 1900., 200.)],
 [74354632224, 'Conservador', (5000., 3000., 1600., 200.)],
 [64020216626, 'Conservador', (5000., 3400., 1600., 400.)],
 [78223722856, 'Conservador', (5200., 3500., 1500., 200.)],
 [58245228846, 'Conservador', (5200., 3400., 1400., 200.)],
 [74490686776, 'Conservador', (4700., 3200., 1600., 200.)],
 [48646824781, 'Conservador', (4800., 3100., 1600., 200.)],
 [77381458676, 'Conservador', (5400., 3400., 1500., 400.)],
 [41615431874, 'Conservador', (5200., 4100., 1500., 100.)],
 [52163844491, 'Conservador', (5500., 4200., 1400., 200.)],
 [70276304567, 'Conservador', (4900., 3100., 1500., 200.)],
 [69119828185, 'Conservador', (5000., 3200., 1200., 200.)],
 [65441690046, 'Conservador', (5500., 3500., 1300., 200.)],
 [56457227894, 'Conservador', (4900., 3600., 1400., 100.)],
 [46939428126, 'Conservador', (4400., 3000., 1300., 200.)],
 [60979942480, 'Conservador', (5100., 3400., 1500., 200.)],
 [41648583220, 'Conservador', (5000., 3500., 1300., 300.)],
 [50376331791, 'Conservador', (4500., 2300., 1300., 300.)],
 [67008801023, 'Conservador', (4400., 3200., 1300., 200.)],
 [72149193419, 'Conservador', (5000., 3500., 1600., 600.)],
 [62830733382, 'Conservador', (5100., 3800., 1900., 400.)],
 [56716675811, 'Conservador', (4800., 3000., 1400., 300.)],
 [61089667146, 'Conservador', (5100., 3800., 1600., 200.)],
 [47795509468, 'Conservador', (4600., 3200., 1400., 200.)],
 [60899885693, 'Conservador', (5300., 3700., 1500., 200.)],
 [53433670705, 'Conservador', (5000., 3300., 1400., 200.)],
 [54850120580, 'Moderado', (7000., 3200., 4700., 1400.)],
 [71457789994, 'Moderado', (6400., 3200., 4500., 1500.)],
 [67692777563, 'Moderado', (6900., 3100., 4900., 1500.)],
 [43133573182, 'Moderado', (5500., 2300., 4000., 1300.)],
 [55150612815, 'Moderado', (6500., 2800., 4600., 1500.)],
 [48211725243, 'Moderado', (5700., 2800., 4500., 1300.)],
 [76686463776, 'Moderado', (6300., 3300., 4700., 1600.)],
 [71971000560, 'Moderado', (4900., 2400., 3300., 1000.)],
 [40307235992, 'Moderado', (6600., 2900., 4600., 1300.)],
 [44826533081, 'Moderado', (5200., 2700., 3900., 1400.)],
 [45735414894, 'Moderado', (5900., 3200., 4800., 1800.)],
 [57137146514, 'Moderado', (6100., 2800., 4000., 1300.)],
 [53657058251, 'Moderado', (6300., 2500., 4900., 1500.)],
 [52941460485, 'Moderado', (6100., 2800., 4700., 1200.)],
 [44306600683, 'Moderado', (6400., 2900., 4300., 1300.)],
 [43460747924, 'Moderado', (6600., 3000., 4400., 1400.)],
 [75590376075, 'Moderado', (6800., 2800., 4800., 1400.)],
 [68267282206, 'Moderado', (6700., 3000., 5000., 1700.)],
 [77567920298, 'Moderado', (6000., 2900., 4500., 1500.)],
 [67600419504, 'Moderado', (5700., 2600., 3500., 1000.)],
 [44902189811, 'Moderado', (5500., 2400., 3800., 1100.)],
 [62966866614, 'Moderado', (5500., 2400., 3700., 1000.)],
 [56182108880, 'Moderado', (5800., 2700., 3900., 1200.)],
 [78299785392, 'Moderado', (6000., 2700., 5100., 1600.)],
 [45206071878, 'Moderado', (5400., 3000., 4500., 1500.)],
 [57381925887, 'Moderado', (6000., 3400., 4500., 1600.)],
 [65654934891, 'Moderado', (6700., 3100., 4700., 1500.)],
 [56130640481, 'Moderado', (6300., 2300., 4400., 1300.)],
 [59667611672, 'Moderado', (5600., 3000., 4100., 1300.)],
 [40349334385, 'Moderado', (5500., 2500., 4000., 1300.)],
 [68422640081, 'Moderado', (5500., 2600., 4400., 1200.)],
 [55245923439, 'Moderado', (6100., 3000., 4600., 1400.)],
 [51286696873, 'Moderado', (5800., 2600., 4000., 1200.)],
 [41065279767, 'Moderado', (5000., 2300., 3300., 1000.)],
 [42866454119, 'Moderado', (5600., 2700., 4200., 1300.)],
 [61962944542, 'Moderado', (5700., 3000., 4200., 1200.)],
 [48623501235, 'Moderado', (5700., 2900., 4200., 1300.)],
 [49475220139, 'Moderado', (6200., 2900., 4300., 1300.)],
 [52245218531, 'Moderado', (5100., 2500., 3000., 1100.)],
 [50932926697, 'Moderado', (5700., 2800., 4100., 1300.)],
 [47432932248, 'Agressivo', (6300., 3300., 6000., 2500.)],
 [39321991579, 'Agressivo', (5800., 2700., 5100., 1900.)],
 [46283759608, 'Agressivo', (7100., 3000., 5900., 2100.)],
 [56996272538, 'Agressivo', (6300., 2900., 5600., 1800.)],
 [77232189978, 'Agressivo', (6500., 3000., 5800., 2200.)],
 [77183282421, 'Agressivo', (7600., 3000., 6600., 2100.)],
 [42857147573, 'Agressivo', (4900., 2500., 4500., 1700.)],
 [39331584043, 'Agressivo', (7300., 2900., 6300., 1800.)],
 [48130345228, 'Agressivo', (6700., 2500., 5800., 1800.)],
 [71422443953, 'Agressivo', (7200., 3600., 6100., 2500.)],
 [72508507904, 'Agressivo', (6900., 3200., 5700., 2300.)],
 [41188727558, 'Agressivo', (5600., 2800., 4900., 2000.)],
 [61358776640, 'Agressivo', (7700., 2800., 6700., 2000.)],
 [66934042323, 'Agressivo', (6300., 2700., 4900., 1800.)],
 [40622495567, 'Agressivo', (6700., 3300., 5700., 2100.)],
 [57221661311, 'Agressivo', (7200., 3200., 6000., 1800.)],
 [45159362930, 'Agressivo', (6200., 2800., 4800., 1800.)],
 [45018975174, 'Agressivo', (6100., 3000., 4900., 1800.)],
 [70685429140, 'Agressivo', (6400., 2800., 5600., 2100.)],
 [61808723477, 'Agressivo', (7200., 3000., 5800., 1600.)],
 [56363906548, 'Agressivo', (7400., 2800., 6100., 1900.)],
 [39646194720, 'Agressivo', (7900., 3800., 6400., 2000.)],
 [55385494438, 'Agressivo', (6400., 2800., 5600., 2200.)],
 [75796138061, 'Agressivo', (6300., 2800., 5100., 1500.)],
 [53595767857, 'Agressivo', (6100., 2600., 5600., 1400.)],
 [48758828080, 'Agressivo', (7700., 3000., 6100., 2300.)],
 [58387651356, 'Agressivo', (6300., 3400., 5600., 2400.)],
 [72846931192, 'Agressivo', (6400., 3100., 5500., 1800.)],
 [47046896346, 'Agressivo', (6000., 3000., 4800., 1800.)],
 [69730292799, 'Agressivo', (6900., 3100., 5400., 2100.)],
 [48177836349, 'Agressivo', (6700., 3100., 5600., 2400.)],
 [57976326635, 'Agressivo', (6900., 3100., 5100., 2300.)],
 [55710813002, 'Agressivo', (5800., 2700., 5100., 1900.)],
 [64028580439, 'Agressivo', (6800., 3200., 5900., 2300.)],
 [49962942971, 'Agressivo', (6700., 3300., 5700., 2500.)],
 [47250893163, 'Agressivo', (6700., 3000., 5200., 2300.)],
 [75559276274, 'Agressivo', (6300., 2500., 5000., 1900.)],
 [58529878272, 'Agressivo', (6500., 3000., 5200., 2000.)],
 [76005896622, 'Agressivo', (6200., 3400., 5400., 2300.)],
 [49212614633, 'Agressivo', (5900., 3000., 5100., 1800.)]]

no_class = [[45926320819, '', (5800., 4000., 1200., 200.)],
 [52559670741, '', (5700., 4400., 1500., 400.)],
 [59016004832, '', (5400., 3900., 1300., 400.)],
 [66175672425, '', (5100., 3500., 1400., 300.)],
 [53330429526, '', (5700., 3800., 1700., 300.)],
 [43765563403, '', (5100., 3800., 1500., 300.)],
 [68020822591, '', (5400., 3400., 1700., 200.)],
 [53939481689, '', (5100., 3700., 1500., 400.)],
 [47014057561, '', (4600., 3600., 1000., 200.)],
 [57183542047, '', (5100., 3300., 1700., 500.)],
            
 [68518284363, '', (5000., 2000., 3500., 1000.)],
 [65806049885, '', (5900., 3000., 4200., 1500.)],
 [54128073086, '', (6000., 2200., 4000., 1000.)],
 [41306785494, '', (6100., 2900., 4700., 1400.)],
 [65234831039, '', (5600., 2900., 3600., 1300.)],
 [50964498067, '', (6700., 3100., 4400., 1400.)],
 [50810951429, '', (5600., 3000., 4500., 1500.)],
 [48765044397, '', (5800., 2700., 4100., 1000.)],
 [41960083761, '', (6200., 2200., 4500., 1500.)],
 [76657763082, '', (5600., 2500., 3900., 1100.)],
            
 [64726487742, '', (6500., 3200., 5100., 2000.)],
 [75746566283, '', (6400., 2700., 5300., 1900.)],
 [78576734793, '', (6800., 3000., 5500., 2100.)],
 [56440141847, '', (5700., 2500., 5000., 2000.)],
 [66827423000, '', (5800., 2800., 5100., 2400.)],
 [45267873396, '', (6400., 3200., 5300., 2300.)],
 [46387191493, '', (6500., 3000., 5500., 1800.)],
 [54273611732, '', (7700., 3800., 6700., 2200.)],
 [75135392881, '', (7700., 2600., 6900., 2300.)],
 [64703873108, '', (6000., 2200., 5000., 1500.)]]



# passo 1 : definindo k==5
k=5
i=1
tipoinvpessoal=[]
for elemento in no_class:
    listdist=[]    
#distancia do novo com os ja dados:
    for lista in data:
        valores=elemento[2]
        valores2=lista[2]
        d=((valores[0]-valores2[0])**2 + (valores[1]-valores2[1])**2 + (valores[2]-valores2[2])**2 + (valores[3]-valores2[3])**2)**0.5
        listdist.append(d) 

#colocar em ordem crescente
    a=sorted(listdist)

#determinar qual sao os 5 menores
    kmenores=[]
    for i in range(0,k):
        kmenores.append(a[i])
    print(f'Os k(5) menores distancias em relação ao {i+1} é: {kmenores}')

#pegar a posição dos kmenores
    posicao=[]
    for distancia1 in kmenores:
        for distancia2 in listdist:
            if(distancia1==distancia2):
               # if(listdist.index(distancia2) in posicao):
                    #continue
                #else:    
                posicao.append(listdist.index(distancia2))
    print(f'As posiçoes desses são: {posicao}')

#pegar o tipo de investidor dos kmenores
    tipoinv=[]
    for numero in posicao:
        tipoinv.append(data[numero][1])
    print(tipoinv)

#calcular A MODA DISSO! - e estipular o tipo de investidor 
    c=0
    a=0
    m=0
    for tipo in tipoinv:
        if(tipo=='Conservador'):
            c+=1
        if(tipo=='Agressivo'):
            a+=1
        if(tipo=='Moderado'):
            m+=1
    if(c>=a and a>=m):
        tipoinvpessoal.append('Conservador')
    elif(a>=c and c>=m):
        tipoinvpessoal.append('Agressivo')
    elif(m>=a and a>=c):
        tipoinvpessoal.append('Moderado')

    print(tipoinvpessoal)
    



#for cpf in no class - e no final zerar tudo, menos o tipo inv pessoal, que vai ter todos os tipos



