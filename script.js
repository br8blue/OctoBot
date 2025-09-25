const chatbox = document.getElementById("chatBox");
const input = document.getElementById("userInput");
const sendBtn = document.getElementById("sendButton");



sendBtn.onclick = async () => {
  const message = input.value.trim();
  if (!message) return;


  chatbox.innerHTML += `<div><strong>You:</strong> ${message}</div>`;
  input.value = "";



  try {
    const res = await fetch("/chat", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ message })
    });
    const data = await res.json();
    chatbox.innerHTML += `<div><strong>OctoBot:</strong> ${data.response}</div>`;
    chatbox.scrollTop = chatbox.scrollHeight;
  } catch (err) {
    chatbox.innerHTML += `<div><strong>OctoBot:</strong> Error talking to OctoBot.</div>`;
  }
};



input.addEventListener("keydown", e => {
  if (e.key === "Enter") sendBtn.click();
});