# MIT License

# Copyright (c) 2023 David Rice

# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.


import os

from chat_character import ChatCharacter


def main():
    openai_api_key = os.environ['OPENAI_API_KEY']

    interviewee_prompt = 'You are Sir Isaac Newton. You give brief and concise answers. You are interested in physics and calculus. You were not ever hit on the head with an apple, but in fact it was a pear instead.'
    interviewer_prompt = 'You are a journalist. You are interviwing Sir Isaac Newton. You ask short and concise questions. You are very inquisitive and you always follow up a response with another question. You always ask a question after a response.'

    interviewer = ChatCharacter(openai_api_key, interviewer_prompt)
    interviewee = ChatCharacter(openai_api_key, interviewee_prompt)

    total_tokens_used = 0

    intro = "Hello Mr. Newton! It's great to be here with you today. What would you like to talk about?"

    print(f'Journalist: {intro}')
    interviewee_response = interviewee.get_chat_response(intro)
    print(f'Newton: {interviewee_response.content}\n')

    while total_tokens_used < 3800:
        interviewer_response = interviewer.get_chat_response(interviewee_response.content)
        print(f'Journalist: {interviewer_response.content}')
        interviewee_response = interviewee.get_chat_response(interviewer_response.content)
        print(f'Newton: {interviewee_response.content}\n')

        total_tokens_used = interviewee_response.total_tokens_used

    wrap_up = "Well, that's all the time we have for today. Is there else anything you'd like to add?"

    print(f'Journalist: {wrap_up}')
    interviewee_response = interviewee.get_chat_response(wrap_up)
    print(f'Newton: {interviewee_response.content}\n')

    print(f'Journalist: Thank you for your time, Mr. Newton!')


if __name__ == '__main__':
    main()
