async function sendQuestion() {
  const question = document.getElementById("question").value;

  const responseElement = document.getElementById("response");
  responseElement.textContent = "⏳ Enviando...";

  try {
    const response = await fetch("/chat", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ question }),
    });

    const data = await response.json();
    const message = data.choices?.[0]?.message?.content;

    responseElement.textContent = message || "❌ Nenhuma resposta encontrada.";
  } catch (error) {
    responseElement.textContent = `Erro: ${error.message}`;
  }
}
