const chatbox = document.getElementById("chatbox");
const input = document.getElementById("userInput");
const sendButton = document.getElementById("sendButton");
const loadingText = document.getElementById("loadingText");



sendButton.onclick = async () => {
  const message = input.value.trim();
  if (!message) return;



  chatbox.innerHTML += `<div><strong>You:</strong> ${message}</div>`;
  input.value = "";
  loadingText.style.display = "block";



try {
  const res = await fetch("http://127.0.0.1:5000/chat", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ message })
  });

  if (!res.ok) {
    throw new Error(`HTTP error ${res.status}`);
  }

  const data = await res.json();
  chatbox.innerHTML += `<div><strong>OctoBot:</strong> ${data.response}</div>`;
} catch (err) {
  console.error("Fetch error:", err);
  chatbox.innerHTML += `<div><strong>OctoBot:</strong> Oops! We bumped into an error with OctoBot. Please try again at a later time.</div>`;
}




  loadingText.style.display = "none";
  chatbox.scrollTop = chatbox.scrollHeight;
};



input.addEventListener("keydown", e => {
  if (e.key === "Enter") sendButton.click();
});