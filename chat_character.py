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


import openai


class ChatResponse:
    def __init__(self, response: dict) -> None:
        self._response = response

    @property
    def content(self) -> str:
        return self._response['choices'][0]['message']['content']

    @property
    def total_tokens_used(self) -> int:
        return self._response['usage']['total_tokens']


class ChatCharacter:
    def __init__(self, api_key: str, system_prompt: str) -> None:
        openai.api_key = api_key

        self._system_prompt = system_prompt
        self.reset()
        
    def reset(self) -> None:
        self._messages = [ {'role': 'system', 'content': self._system_prompt} ]

    @property
    def system_prompt(self) -> str:
        return self._system_prompt

    @system_prompt.setter
    def system_prompt(self, prompt: str) -> None:
        if self._messages[0]['role'] == 'system':
            self._messages[0]['content'] = prompt
        else:
            raise RuntimeError('Invalid structure of ChatCharacter._messages')

    def get_chat_response(self, message: str) -> ChatResponse:
        self._messages.append({'role': 'user', 'content': message})

        response = openai.ChatCompletion.create(
            model='gpt-3.5-turbo',
            messages=self._messages
        )

        self._messages.append(response['choices'][0]['message'])

        return ChatResponse(response)