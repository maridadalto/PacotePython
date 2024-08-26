from setuptools import setup, find_packages

setup(
    name="IMC",
    version="0.1.0",
    author="Marina",
    author_email="maridadalto@live.com",
    description="Função para calcular o IMC",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/seu_usuario/meu_projeto",  # URL do seu projeto, se houver
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
