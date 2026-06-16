#!/bin/bash

echo "Bem-vindo(a) a calculadora!"

echo "Por favor, digite seu nome: "
read nome

echo "Olá, $nome!"

sudo apt install python3 -y

echo "Só um momento..."

python3 calculadora.py
