# 🎉 Bot de Aniversário  

Este projeto em **Python** automatiza o envio de mensagens de aniversário via **WhatsApp Web**, garantindo que ninguém seja esquecido em datas especiais!  

## 📌 Como Funciona  

1. O bot lê uma **planilha** contendo:  
   - 📌 Nome  
   - 📞 Número de telefone  
   - 🎂 Data de nascimento  
2. Ele verifica se há aniversariantes no dia atual.  
3. Para cada aniversariante válido:  
   - Abre uma aba no **Google Chrome** com o link do **WhatsApp Web**  
   - Insere uma mensagem personalizada automaticamente  
   - Envia a mensagem 🎊  

O processo se repete até que todos os aniversariantes sejam notificados.  

## 🚀 Possíveis Aplicações  

🔹 Lembretes de aniversários para grupos, empresas ou igrejas.  
🔹 Notificações automatizadas para outras datas importantes.  
🔹 Adaptação para diferentes tipos de envios e integrações com outras APIs.  

## 🛠 Requisitos  

- Python 3.12
- Bibliotecas:  
  - `openpyxl` (para manipulação de planilhas Excel)  
  - `pyautogui` (para automação de teclado e mouse)  
  - `time` (para controle de tempo)  
  - `datetime` (para manipulação de datas)  
  - `webbrowser` (para abrir URLs)  
  - `urllib.parse` (para manipulação de URLs)  

## 💡 Personalização  

Você pode modificar o código para:  
✔️ Alterar a mensagem enviada.  
✔️ Usar diferentes formatos de planilha.  
✔️ Incluir novos filtros para envio.  

Se quiser contribuir ou melhorar o projeto, sinta-se à vontade para enviar um **Pull Request**! 🚀  
