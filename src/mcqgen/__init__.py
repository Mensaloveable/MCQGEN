import os
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_ollama import ChatOllama

load_dotenv()


def main() -> None:
    print("Hello from mcqgen!")

    information = """
    Asiwaju Bola Ahmed Adekunle Tinubu GCFR (born 29 March 1952) is a Nigerian politician serving as the 16th and current president of Nigeria since 2023.[1] He previously served as the governor of Lagos State from 1999 to 2007 and senator for Lagos West in the Third Republic.[2]

Tinubu spent his early life in southwestern Nigeria and later moved to the United States where he studied accounting at Chicago State University. He returned to Nigeria in the 1980s and was employed by Mobil Nigeria as an accountant, before entering politics as a Lagos West senatorial candidate in 1992 under the banner of the Social Democratic Party. After the military dictator Sani Abacha dissolved the Senate in 1993, Tinubu went into exile and became an activist campaigning for the return of democracy as a part of the National Democratic Coalition movement.[3]

In the first post-transition Lagos State gubernatorial election, Tinubu won by a wide margin as a member of the Alliance for Democracy. Four years later, he won re-election to a second term. After leaving office in 2007, he played a key role in forming the All Progressives Congress in 2013. In 2023, he was elected president, defeating Atiku Abubakar and Peter Obi.[4]

Under his leadership the government ended prior fuel subsidies, citing fiscal pressures,[5] dissolved the governing boards of numerous federal agencies and state-owned enterprises, replaced the majority of military and paramilitary leadership, supported regional efforts to respond to the 2025 Benin coup d'état while engaging with security cooperation with the United States against the Islamic State and survived an alleged coup attempt.[6][7]

Early life
Tinubu was born in Lagos to a Muslim family from the Yoruba ethnic group,[8] the son of Abibatu Mogaji, the Ìyál'ọ́jà of Lagos. He is generally accepted in reliable sources to have been born in 1952;[9] this year of birth is sometimes disputed by political opponents, who argue that he is much older. Some reliable sources note that his age has not been verified.[10][11]

Education
Tinubu attended St. John's Primary School, Aroloya, Lagos before proceeding to Children Home School in Ibadan.[12] Tinubu arrived in the United States in 1975, where he commenced undergraduate studies first at Richard J. Daley College in Chicago and then at Chicago State University where he majored in accounting and management. He worked odd jobs as a dishwasher, night security guard and cab driver to support himself through college.[13] He made the honor dean's list as an undergraduate and taught remedial class tutorials, some of his classmates credited his lectures for their improved grades. Tinubu was the university accounting society president in his senior year. His cumulative GPA was 3.54.[13] Tinubu graduated summa cum laude with a Bachelor of Science in Business Administration in 1979.[14][15]

Early career
After graduating, Tinubu worked as an accountant for the American companies Arthur Andersen, Deloitte and GTE Services Corporation.[16][17] At Deloitte, he gained experience in auditing and management consultancy services for Fortune 500 corporations. He was a consultant for Saudi Aramco's joint venture partner National Oil, helping to establish their accounting and auditing system and leading to his first financial breakthrough.[18] Tinubu moved to London where he was recruited as an auditor for Mobil Oil UK before later joining Mobil Producing Nigeria Unlimited (now Seplat Energy[19]) as a senior company executive and treasurer in the 1980s.[20][18]

Tinubu actively contributed and raised funds for community development programs in Lagos leading Primrose Group, a political action organization advocating for fundamental progressive changes in the state's politics during the Babangida administration. He later opted fully to enter politics in exchange for his lucrative job at Mobil.[21]
    """

    summary_template = """
    Given the information {information} about a person, I want you to generate:
    1. summary of the person's life
    2. Interesting facts about the person
    """

    summary_prompt_template = PromptTemplate(
        input_variables=["information"],
        template=summary_template,
    )

    # OpenAI
    llm1 = ChatOllama(
        model="gemma-assistant",
        temperature=0.7,
        # api_key=os.getenv("OPENAI_API_KEY"),
    )

    # Gemini
    llm = ChatGoogleGenerativeAI(
        model="gemini-3.5-flash-lite",  # was "gemini-2.5-flash" 
        temperature=0.7,
        timeout=30,
        max_retries=1,
        api_key=os.getenv("GOOGLE_API_KEY"),
    )

    chain1 = summary_prompt_template | llm1
    chain2 = summary_prompt_template | llm

    # result1 = chain1.run(information=information)
    # result2 = chain2.run(information=information)

    response1 = chain1.invoke({"information": information})
    response2 = chain2.invoke({"information": information})

    # print the results
    print("Result from OpenAI GPT-4:")
    # print(result1.content)
    print("\nResponse from OpenAI GPT-4:")
    print(response1.content)

    print("\nResult from Google Gemini Pro:")
    # print(result2.content)
    print("\nResponse from Google Gemini Pro:")
    print(response2.content)


if __name__ == "__main__":
    main()
