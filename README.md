# Trabalho de automação com Python e Selenium

Trabalho de criação de testes e2e utilizando python com selenium. O script faz as seguintes etapas:
* cria um aluno (student)
* cria 3 cursos (courses);
* inscreve o aluno no curso de id 1
* adiciona 3 matérias (disciplines) no curso de id 1
* inscreve o aluno nas matérias de id 1,2,3

# Instalação e execução do exemplo
- Crie um ambiente virtual (virtual environment) usando a sua versão padrão do Python
```
python3 -m venv venv
```
- Ative o ambiente virtual
```
source venv/bin/activate
```
- Instale os requisitos do projeto
```
pip install -r requirements.txt
```
- Execute o teste de exemplo. Garanta que o Chrome esteja inslado na sua máquina.
```
python -m pytest -k test_final.py
```

# Referências
- [Selenium WebDriver Documentation](https://www.selenium.dev/documentation/webdriver/)
