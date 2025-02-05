import random
from app.models.petit_lenormand_model import PetitLenormandCard

PETIT_LENORMAND_CARDS = [
    PetitLenormandCard(number=1, name="Cavalheiro/Valete",
                       description="Representa o movimento, de passagem, algo que não fica. Pode representar pessoas de fora, ou um mensageiro. Também pode indicar uma vanguarda.", positivity=0),
    PetitLenormandCard(number=2, name="Trevo",
                       description="Boa sorte, pode se jogar que vai dar bom. Mas dependendo do contexto, de acordo com a leitura braisileira, pode indicar um obstáculo ou desventura.", positivity=1),
    PetitLenormandCard(number=3, name="Navio",
                       description="Algo que vem de fora, agente externo, pode trazer ideia de mudança. Também pode representar um veículo, como um carro.", positivity=0),
    PetitLenormandCard(number=4, name="Casa",
                       description="Intimidade, aconchego, conforto. Normalmente visto como a base de uma pessoa, ou algo que é muito pessoal. Normalmente ideia de Privado ou Privacidade.", positivity=0),
    PetitLenormandCard(number=5, name="Árvore",
                       description="Saúde, paz, meditação, ou algo que está enraizado, depende das cartas vizinhas para ditar o significado.", positivity=0),
    PetitLenormandCard(number=6, name="Nuvens",
                       description="Confusão, costumam cobrir a verdade, só não se escondem da carta Sol.", positivity=-1),
    PetitLenormandCard(number=7, name="Serpente/Cobra",
                       description="Hipocrisia, a cobra possui o próprio veneno. Também pode ser uma representação feminina, amante ou rival, dependendo do contexto.", positivity=-1),
    PetitLenormandCard(number=8, name="Caixão",
                       description="Fim esperado, você não pode fazer nada, é inevitável.", positivity=-1),
    PetitLenormandCard(number=9, name="Buquê",
                       description="Alegria, felicidade. Pode representar um presente. Se for avaliar a positividade, ela tem peso maior que as outras.", positivity=2),
    PetitLenormandCard(number=10, name="Foice",
                       description="Corte, representando sempre uma divisão ou separação.", positivity=0),
    PetitLenormandCard(number=11, name="Chicote",
                       description="Esforço físico, problemas conflitantes, dor, sofrimento. Também pode representar um teor sexual dependendo do contexto.", positivity=-1),
    PetitLenormandCard(number=12, name="Pássaros",
                       description="Comunicação verbal, telefonema, voz, rumores, FOFOCA. Também pode ser uma fadiga ou um cansaço.", positivity=0),
    PetitLenormandCard(number=13, name="Criança",
                       description="Início de algo que possui um desenvolvimento muito lento. Também pode ser uma Ingenuidade, confiança, algo espontâneo e alegria.", positivity=1),
    PetitLenormandCard(number=14, name="Raposa",
                       description="Medo, insegurança, muito cauteloso (até demais). Pode ser visto como uma traição ou sedução de algo. Possui malícia.", positivity=-1),
    PetitLenormandCard(number=15, name="Urso",
                       description="Proteção, está em boas mãos. Pode ser a representatividade de um patrão. Também tem a ver com própria espiritualidade e estar mais consigo.", positivity=0),
    PetitLenormandCard(number=16, name="Estrelas",
                       description="Sonhos pouco palpaveis, esperança, futuro, audio visual e noção de noite.", positivity=1),
    PetitLenormandCard(number=17, name="Cegonha",
                       description="Vida nova, mudanças, inovação.", positivity=0),
    PetitLenormandCard(number=18, name="Cachorro",
                       description="Lealdade, amizade, melhor amigo. Pode ser um romance virando amizade.", positivity=1),
    PetitLenormandCard(number=19, name="Torre",
                       description="Estratégia, ver as coisas do alto, ter um tempo só. Pode representar um órgão público. Se for sobre alguém, pode ser que a pessoa seja mais voltada para si, reflexiva.", positivity=0),
    PetitLenormandCard(number=20, name="Jardins",
                       description="Encontros, festas, lugar público, nada íntimo. Pode dizer que a pessoa é alerta para tudo.", positivity=0),
    PetitLenormandCard(number=21, name="Montanha",
                       description="Dificuldade, desafios, obstáculos. Pode ser recompensador se atingir o topo.", positivity=-1),
    PetitLenormandCard(number=22, name="Caminhos",
                       description="Escolhas, situação onde se faz necessário tomar uma decisão.", positivity=0),
    PetitLenormandCard(number=23, name="Ratos",
                       description="Pequenos problemas que se multiplicam se não forem resolvidos de imediato. Confusão, estresse, ansiedade.", positivity=-1),
    PetitLenormandCard(number=24, name="Coração",
                       description="Amor próprio, muito amor, algo que fará bem ao coração. Possui positividade alta.", positivity=2),
    PetitLenormandCard(number=25, name="Anel/Aliança",
                       description="Contrato, parceria, representa o firmamento de uma relação.", positivity=0),
    PetitLenormandCard(number=26, name="Livro",
                       description="Estudos ou algo que ainda não foi revelado, um segredo.", positivity=0),
    PetitLenormandCard(number=27, name="Carta",
                       description="Mensagem que é trazida, comunicação por escrita. Pode representar documentos.", positivity=0),
    PetitLenormandCard(number=28, name="Homem",
                       description="Representação da figura masculina. Pode representar quem está fazendo a pergunta ou homens relacionados a pessoa", positivity=0),
    PetitLenormandCard(number=29, name="Mulher",
                       description="Representação da figura feminina. Pode representar quem está fazendo a pergunta ou mulheres relacionadas a pessoa", positivity=0),
    PetitLenormandCard(number=30, name="Lírios",
                       description="Maturidade, honestidade, pureza. Pode representar o envelhecer, ou uma pessoa mais velha. Dependendo do contexto pode indicar castidade.", positivity=1),
    PetitLenormandCard(number=31, name="Sol",
                       description="Êxito, esclarecimento de ideias, poder, prosperidade, financias, fartura. Pode ser visto como Identidade.", positivity=1),
    PetitLenormandCard(number=32, name="Lua",
                       description="Romântico, reputação, clareza em situações obscuras. Pode ser visto como amor platônico e sentimentos profundos.", positivity=1),
    PetitLenormandCard(number=33, name="Chave",
                       description="Oportunidade, aberturas. Pode significar que tudo está aberto ou irá abrir portas. Carta excelente para identificar soluções de problemas.", positivity=1),
    PetitLenormandCard(number=34, name="Peixes",
                       description="Pequenos investimentos com grandes retornos. Fartura, prosperidade, abundância.", positivity=1),
    PetitLenormandCard(number=35, name="Àncora",
                       description="Estabilidade, trabalho. Mas também pode ser prisão ou estagnação.", positivity=1),
    PetitLenormandCard(number=36, name="Cruz",
                       description="Carregar coisas que não precisa, peso, punição. Pode ser visto como carregar as dores dos outros.", positivity=-1)
]


def shuffle_cards(shuffle_times: int = 1):
    """
    Shuffles a list of cards.

    Returns:
        list: A shuffled list of cards.
    """
    for _ in range(shuffle_times):
        random.shuffle(PETIT_LENORMAND_CARDS)
    return PETIT_LENORMAND_CARDS.copy()
