const chatbox = document.getElementById("chatBox");
const input = document.getElementById("userInput");
const sendButton = document.getElementById("sendButton");
const loadingText = document.getElementById("loadingText");



sendButton.onclick = async () => {
  const message = input.value.trim();
  if (!message) return;



  chatbox.innerHTML += `<div><strong>You:</strong> ${message}</div>`;
  input.value = "";
  loadingText.style.display = "block"; // Show loading


  try {
    const res = await fetch("/chat", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ message })
    });



    const data = await res.json();
    chatbox.innerHTML += `<div><strong>OctoBot:</strong> ${data.response}</div>`;
  } catch (err) {
    chatbox.innerHTML += `<div><strong>OctoBot:</strong> Error talking to OctoBot.</div>`;
  }


  
  loadingText.style.display = "none"; // Hide loading
  chatbox.scrollTop = chatbox.scrollHeight;
};

input.addEventListener("keydown", e => {
  if (e.key === "Enter") sendButton.click();
});