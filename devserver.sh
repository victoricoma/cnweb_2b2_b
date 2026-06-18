echo "-- Instalando as Dependencias da Instancia --"
pip install -r requirements.txt
echo "-- Organizando os Diretórios do Python ---"
python -m pip install --upgrade pip
echo "---- Projeto Pronto para Uso ----"
echo ""
for i in {5..1}; do
    echo -ne "Seu servidor será iniciado em ${i} segundos... \r"
    sleep 1
done
clear
py app.py