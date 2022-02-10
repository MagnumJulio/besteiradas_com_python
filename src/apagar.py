#cata números 2 dígitos

import pyperclip
import re

def tupleFilter(tup, li):
    for i in tup:
        j = i[1]
        # print(j)
        li.append(j)


def writeList(li):
    string = ''
    for i in li:
        string += i+' '
    return string


# string = '''   Logo Total IP News      Home     Total IP     Soluções     Serviços     FAQ     Blog         Notícias         Artigos     TV Total IP     Imprensa         Total IP na Mídia         Press Release     Trabalhe Conosco         Vagas Abertas         Envie seu Currículo     Contato  Quais os DDDs de cada Estado do Brasil?  Escrito em 21/11/2013. Postado em Notícias, Todas categorias  A Total IP explica o conceito e lista todos os códigos de área  A Discagem Direta a Distância (DDD) é o sistema empregado para ligações interurbanas a partir da inserção de prefixos regionais. No Brasil, são utilizados 67 códigos de área diferentes, espalhados por todo o território nacional. Com tantos números diferentes, é fácil fazer confusão. Para te ajudar, listamos abaixo todos os DDDs do país e os Estados aos quais eles correspondem:  Centro-Oeste – Distrito Federal (61) – Goiás (62 e 64) – Mato Grosso (65 e 66) – Mato Grosso do Sul (67)  Nordeste – Alagoas (82) – Bahia (71, 73, 74, 75 e 77) – Ceará (85 e 88) – Maranhão (98 e 99) – Paraíba (83) – Pernambuco (81 e 87) – Piauí (86 e 89) – Rio Grande do Norte (84) – Sergipe (79)  Norte – Acre (68) – Amapá (96) – Amazonas (92 e 97) – Pará (91, 93 e 94) – Rondônia (69) – Roraima (95) – Tocantins (63)  Sudeste – Espírito Santo (27 e 28) – Minas Gerais (31, 32, 33, 34, 35, 37 e 38) – Rio de Janeiro (21, 22 e 24) – São Paulo (11, 12, 13, 14, 15, 16, 17, 18 e 19)  Sul – Paraná (41, 42, 43, 44, 45 e 46) – Rio Grande do Sul (51, 53, 54 e 55) – Santa Catarina (47, 48 e 49)  Conhecer os códigos de área é fundamental para evitar gastos em empresas onde há uma demanda muito grande por ligações. Utilizando os recursos da solução integrada de voz Total IP, é possível realizar ligações pela rota de menor custo e até mesmo bloquear chamadas de uma campanha para uma determinada região. Pronto! Com a lista, você já pode ligar sem problemas!  A Total IP oferece a melhor solução para contact centers do mercado. Acesse o site www.totalip.com.br e conheça todos os nossos benefícios e diferenciais. Curtir isso: Carregando... Relacionado Estratégias do discador garantem maior efetividade nas campanhas  Planejamento propicia economia na operação Com a utilização cada vez mais constante de discadores automáticos, as empresas vem se preocupando com o aumento da produtividade, pois essas ferramentas são responsáveis por aumentar a entrega de ligações a seus operadores. Porém, acabam  esquecendo de traçar um método de otimizar a potencialidade…  14/10/2013  Em "Notícias" Nono dígito: Migração continua em 2014  Mais cinco Estados terão combinações alteradas até dezembro A Agência Nacional de Telecomunicações - Anatel dará sequência ao plano de migração dos telefones celulares do país para números de nove dígitos em 2014. O objetivo da medida é criar mais combinações, pois, devido à crescente demanda por acessos móveis no…  15/01/2014  Em "Notícias" 31-10-13 | Aserc  Estratégias do Discador. Planejamento propicia redução de custos e facilidades na gestão Por Fernando Lujan* A tendência da adoção de discadores automáticos, por parte das empresas de contact centers, é uma prática cada vez mais comum. O aumento da produtividade com a realização de mais ligações em menos tempo ou…  31/10/2013  Em  Tags: Call Center, Contact Center, DDD, Discagem direta a distância, Total IP Enquete Quais dessas ferramentas mais auxiliam no home office da sua empresa?      Gravação de Voz e Tela     VPN     Soluções em Nuvem     Relatórios Web   Tags  Gravação de voz robôs ligações URA Receptiva tecnologia no atendimento feedback PABX IP URA de Pesquisa DAC ASR TTS Inteligência Artificial discador Diretora Comercial produtividade atendimento Atendimento ao Cliente Fernando Lujan Recuperação de Crédito SAC Carlos Henrique Mencaci Contact Center Call Center telemarketing Cobrança Ariane Abreu Tecnologia URA Agente Virtual Unidade de Resposta Audível home office contact centers URA ativa clipping Economia Whatsapp Gestão de Monitoria Relacionamento Cliente Gravação de Voz e Tela URA Reversa Relatórios Agente Virtual - CPC Serviço de Atendimento ao Consumidor  Copyright © 2020 Total IP. Todos os direitos reservados.  Central de atendimento (11) 3355-3400 – Ligue agora e aumente a produtividade da sua empresa!  '''

lista = list()
rgx = re.compile(r'(\(?)(\d{2})(\)|,)')
clip = pyperclip.paste()
print(clip)

#não é uma lista bem lista
mo = rgx.findall(clip)  

#catch only the number in the tuples that are in the list mo
tupleFilter(mo, lista)   

# print(writeList(lista))

pyperclip.copy(writeList(lista))
# print(mo)
