from dotenv import load_dotenv
from openai import OpenAI
import os


load_dotenv()
client = OpenAI()

def tranlate_to_asm(code: str):
    completion = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You are an assistant who will help translate Python, Java and C ++ javascript code into ASM assembly language. Everything that the user passes you that is not Python, JAVA or C ++ javascritp code will return false, and if it is Python ,Java or C ++ code, you will not explain the code or write a text beforehand, you will only return the translation to ASM assembly code."},
            {
                "role": "user",
                "content": code
            }
        ]
    )

    return completion.choices[0].message.content

