import erniebot
from collections import defaultdict
class Question_generae():
    def __init__(self,content,api_key,top_p=0.2,temperature=0.5):
        self.content=content
        self.api_key=api_key
        self.top_p=top_p
        self.temperature=temperature
    def generate(self):
        erniebot.api_type = 'aistudio'
        erniebot.access_token = self.api_key
        messages=[]

        prompt="""
        我需要你给我十个选择题
        使用下列格式，回复:
        Question: [Question here][A choice][B choice][C choice][D choice]
        Answer: [Answer here]
        除了[Question here][A choice][B choice][C choice][D choice][Answer here]以外不需要任何其他文字回复，注意不要回复好的，我明白了之类的文字我只需要问答
        """
        messages.append({'role': 'user', 'content': prompt})

        #content="为什么说太阳也有生长老死世上万物皆有生死?辉煌如太阳者亦不能例外。它和众多的恒星一样，也有诞生和死亡。太阳起源于一团以氢分子为主的硕大气体云团。约50亿年前，一团原本十分稀薄的星云在某种外因的影响下开始收缩。由于引力作用，收缩一旦开始就会不断加速。在收缩过程中，动能转变成热能，使得气体温度逐渐升高，随着这团气体的密度越来越大，中心温度越来越高，一旦其核心达到了足够高的温度（约700万开），就会触发热核聚变反应。核心的热核反应“点燃”后，光辐射持续产生的“辐射压”能够有效地抵抗引力的作用，从而使得这团气体不再继续收缩，于是一个稳定的太阳就诞生了。"
        system=f"你是一个擅长总结文章并且从文章中出题的小学老师，你严谨，细心，了解小学教育，善于从文章中总结适合的、科学的、正确的题目。 而且你的回答必须依据下面的文章从文字中提取有关于科学的知识点和相关内容,我只需要科学内容不需要其他内容,而且你不能使用超出文章的知识出题只能使用下列文章的知识点！: {self.content}"
        response = erniebot.ChatCompletion.create(
            model='ernie-3.5',
            messages=messages,
            system=system,
            top_p=self.top_p,
            temperature=self.temperature,
        )
        result=response['result']
        # return result
        str=result.split('Question: ')
        QA=[[] for i in range(10)]
        for r in range(0,10):
            str_split=str[r+1].split('\n')
            QA[r].extend(str_split[0:6])
        return QA

        # QA=defaultdict(list)
        # for r in range(1,len(str)):
        #     str_split=str[r].split('\n')
        #     QA[str_split[0]].extend(str_split[1:6])
        # return QA