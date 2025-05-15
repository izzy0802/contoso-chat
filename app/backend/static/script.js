document.querySelector("form").addEventListener("submit", async (e) => {
  e.preventDefault();

  const question = document.querySelector("textarea").value;

  const response = await fetch("/chat", {
    method: "POST",
    headers: {
      "Content-Type": "application/json"
    },
    body: JSON.stringify({ question })
  });

  const data = await response.json();
  alert(data.choices[0].message.content);
});
